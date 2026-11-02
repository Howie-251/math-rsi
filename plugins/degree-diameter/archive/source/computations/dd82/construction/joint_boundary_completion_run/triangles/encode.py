"""Append actual per-vertex triangle upper budgets to the sorted target CNF.

No generator or solver runs on import. All previous clauses and IDs survive
as an unchanged input prefix. Triangle indicators refer to the same A.
"""
import argparse
import collections
from copy import deepcopy
import importlib.util
from itertools import combinations, product
import json
from pathlib import Path
import shutil
import sys
import time

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
PARENT = BASE / 'sorted'
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('joint_boundary_triangles_base_encode', BASE / 'encode.py')
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
ROOT = base.ROOT
BUDGETS = {'n58': 3, 'n60': 2}


def save(path, record):
    path.write_text(json.dumps(record, indent=2) + '\n')


def exact_and_clauses(output, inputs):
    """All clauses of output iff the two/three actual free edges are true."""
    assert len(inputs) in (2, 3)
    return [(-output, edge) for edge in inputs] + [(output, *(-edge for edge in inputs))]


def conjunction_sanity():
    results = []
    for width in (2, 3):
        inputs, output = tuple(range(1, width+1)), width+1
        clauses = exact_and_clauses(output, inputs)
        checked = 0
        for bits in product((False, True), repeat=width+1):
            values = {var: value for var, value in enumerate(bits, 1)}
            actual = all(any(values[abs(literal)] == (literal > 0) for literal in clause)
                         for clause in clauses)
            expected = values[output] == all(values[var] for var in inputs)
            assert actual == expected
            checked += 1
        results.append(dict(free_edge_factors=width, complete_assignments_checked=checked,
                            defining_clauses=len(clauses)))
    return dict(status='PASSED', cases=results, solver_calls=0,
                scope='Only the new exact two/three-factor conjunction definitions')


def read_assignment(path, variable_count):
    values = {}
    with path.open() as source:
        for line in source:
            assert line.startswith('v ')
            literals = list(map(int, line.split()[1:]))
            assert literals[-1] == 0
            for literal in literals[:-1]:
                assert literal != 0
                var, value = abs(literal), literal > 0
                assert var not in values or values[var] == value
                values[var] = value
    assert set(values) == set(range(1, variable_count+1))
    return values


def triangle_extension(helper, n, free, fixed, parent_variables, parent_clauses, values, budget):
    class EvaluatedEmitter(helper.CNFEmitter):
        def __init__(self):
            super().__init__(None)
            self.variable_count = parent_variables
            self.clauses = []
            self.values = dict(values)
            self.false_clause_ids = []

        def add_clause(self, *literals):
            super().add_clause(*literals)
            self.clauses.append(tuple(literals))
            absolute_clause = parent_clauses + self.clause_count
            if base.evaluate_clause(literals, self.values, absolute_clause):
                self.false_clause_ids.append(absolute_clause)

    emitter = EvaluatedEmitter()
    incident = [[] for _ in range(n)]
    fixed_counts = [0] * n
    indicator_records, constant_triangles = [], []
    simplified_zero, visited = 0, 0

    def edge(a, b):
        ab = base.pair(a, b)
        return free[ab] if ab in free else fixed[ab]

    for vertices in combinations(range(n), 3):
        visited += 1
        terms = [edge(a, b) for a, b in combinations(vertices, 2)]
        if any(term is False for term in terms):
            simplified_zero += 1
            continue
        inputs = [term for term in terms if term is not True]
        if not inputs:
            constant_triangles.append(vertices)
            for vertex in vertices:
                fixed_counts[vertex] += 1
            continue
        # With constants only on O/O, a nonconstant triangle has either
        # one fixed-true edge and two free edges, or three free edges.
        assert all(not isinstance(var, bool) for var in inputs) and len(inputs) in (2, 3)
        out = emitter.new_var('actual_triangle_indicator')
        first_clause = emitter.clause_count + 1
        for clause in exact_and_clauses(out, inputs):
            emitter.add_clause(*clause)
        indicator_records.append(dict(vertices=vertices, variable=out, actual_free_edge_inputs=inputs,
                                      first_added_clause=first_clause, last_added_clause=emitter.clause_count))
        for vertex in vertices:
            incident[vertex].append(out)
    assert visited == n*(n-1)*(n-2)//6
    triangle_definition_clauses = emitter.clause_count

    count_records = []
    for vertex in range(n):
        residual = budget-fixed_counts[vertex]
        first_clause = emitter.clause_count + 1
        forbidden_threshold = None
        if residual < 0:
            # A fully fixed triangle excess really makes the anchor impossible.
            emitter.add_clause()
        elif residual < len(incident[vertex]):
            thresholds = helper.unary_thresholds(emitter, incident[vertex], residual+1,
                                                  'triangle_upper_threshold')
            forbidden_threshold = thresholds[residual]
            assert forbidden_threshold is not None
            emitter.add_clause(-forbidden_threshold)
        count_records.append(dict(vertex=vertex, total_triangle_upper_budget=budget,
            fixed_triangle_count=fixed_counts[vertex], residual_variable_upper_budget=residual,
            incident_triangle_indicators=incident[vertex], forbidden_threshold=forbidden_threshold,
            first_added_clause=first_clause, last_added_clause=emitter.clause_count))
    assert set(emitter.values) == set(range(1, emitter.variable_count+1))
    source_counts = [fixed_counts[v] + sum(emitter.values[var] for var in incident[v]) for v in range(n)]
    return emitter, dict(
        unordered_triples_visited=visited, simplified_fixed_zero_triples=simplified_zero,
        fully_fixed_triangles=constant_triangles, triangle_indicators=indicator_records,
        triangle_definition_clauses=triangle_definition_clauses,
        per_vertex_upper_bounds=count_records, source_triangle_counts=source_counts,
        source_triangle_histogram=dict(sorted(collections.Counter(source_counts).items())))


def prepare(case):
    started_cpu, started_wall = time.process_time(), time.monotonic()
    parent_dir, target = PARENT / case, HERE / case
    target.mkdir(exist_ok=True)
    assert not (target / 'input.cnf').exists() and not (target / 'encoding.json').exists(), 'Preserve prior triangle preparation'
    encoding = json.loads((parent_dir / 'encoding.json').read_text())
    assert encoding['status'] == 'PREPARED_NOT_RUN' and encoding['n'] == int(case[1:])
    parent_sanity = json.loads((parent_dir / 'source_sanity.json').read_text())
    assert parent_sanity['status'] == 'PASSED_RELABELLED_SOURCE_ASSIGNMENT_SANITY'
    mapping = json.loads((parent_dir / 'edge_variables.json').read_text())
    free = {(a, b): var for a, b, var in mapping['rows']}
    fixed = {(a, b): bool(value) for a, b, value in mapping['fixed_rows']}
    n = encoding['n']
    assert not set(free).intersection(fixed)
    assert set(free).union(fixed) == set(combinations(range(n), 2))
    values = read_assignment(parent_dir / 'source.assignment.txt', encoding['variables'])
    helper = base.load_helpers()
    small = conjunction_sanity()
    emitter, triangle_record = triangle_extension(helper, n, free, fixed, encoding['variables'],
                                                   encoding['clauses'], values, BUDGETS[case])
    assert not emitter.false_clause_ids
    assert max(triangle_record['source_triangle_counts']) <= BUDGETS[case]

    # Keep the exact sorted body, including every original pair obligation.
    with (parent_dir / 'input.cnf').open('rb') as source:
        header = source.readline().decode('ascii').split()
        assert header == ['p', 'cnf', str(encoding['variables']), str(encoding['clauses'])]
        with (target / 'input.cnf').open('wb') as output:
            output.write(f"p cnf {emitter.variable_count} {encoding['clauses']+emitter.clause_count}\n".encode('ascii'))
            shutil.copyfileobj(source, output, length=1024*1024)
            for clause in emitter.clauses:
                output.write((' '.join(map(str, clause)) + ' 0\n').encode('ascii'))
    sanity = base.check_dimacs(target / 'input.cnf', emitter.values, emitter.variable_count,
                               encoding['clauses']+emitter.clause_count)
    assert sanity['false_clause_ids'] == parent_sanity['false_clause_ids'] == parent_sanity['bad_pair_coverage_clause_ids']
    sanity.update(status='PASSED_TRIANGLE_EXTENDED_SOURCE_ASSIGNMENT_SANITY',
                  source_graph=parent_sanity['source_graph'],
                  original_bad_pairs=parent_sanity['original_bad_pairs'],
                  relabelled_bad_pairs=parent_sanity['relabelled_bad_pairs'],
                  bad_pair_coverage_clause_ids=parent_sanity['bad_pair_coverage_clause_ids'],
                  source_relabeling=parent_sanity['source_relabeling'],
                  source_satisfies_full_target=False,
                  satisfies_every_clause_except_relabelled_original_bad_pair_coverage=True,
                  all_added_triangle_and_upper_bound_clauses_satisfied=True,
                  complete_target_input_retained=True, relaxed_input_written=False, solver_calls=0,
                  source_triangle_counts=triangle_record['source_triangle_counts'],
                  source_triangle_histogram=triangle_record['source_triangle_histogram'])
    save(target / 'source_sanity.json', sanity)
    save(target / 'conjunction_sanity.json', small)
    save(target / 'triangle_constraints.json', triangle_record)
    base.write_assignment(target / 'source.assignment.txt', emitter.values)
    shutil.copyfile(parent_dir / 'edge_variables.json', target / 'edge_variables.json')

    record = deepcopy(encoding)
    record.update(scope=encoding['scope']+'; explicit proven per-vertex triangle upper budget '+str(BUDGETS[case]),
                  variables=emitter.variable_count, clauses=encoding['clauses']+emitter.clause_count,
                  triangle_added_variables=emitter.variable_count-encoding['variables'],
                  triangle_added_clauses=emitter.clause_count,
                  triangle_budget=BUDGETS[case], triangle_free_assumption=False,
                  triangle_indicators=len(triangle_record['triangle_indicators']),
                  fully_fixed_triangle_count=len(triangle_record['fully_fixed_triangles']),
                  source_assignment_sanity='PASSED_TRIANGLE_EXTENDED_SOURCE_ASSIGNMENT_SANITY',
                  conjunction_sanity='PASSED',
                  sorted_parent_prefix=dict(input=str((parent_dir/'input.cnf').relative_to(ROOT)),
                      variables=encoding['variables'], clauses=encoding['clauses'], body_copied_verbatim=True),
                  inherited_sanity_receipts=dict(
                      source=str((parent_dir/'source_sanity.json').relative_to(ROOT)),
                      lex=str((parent_dir/'lex_sanity.json').relative_to(ROOT)),
                      tiny_graph=str((BASE/case/'small_input_sanity.json').relative_to(ROOT)),
                      graph_or_lex_checks_rerun=False),
                  cnf_bytes=(target/'input.cnf').stat().st_size,
                  preparation_cpu_seconds=time.process_time()-started_cpu,
                  preparation_wall_seconds=time.monotonic()-started_wall)
    # Existing added_variables/clauses refer to the earlier base prefix;
    # update their cumulative meaning and retain the sorted-stage deltas.
    record['sorted_stage_added_variables'] = encoding['added_variables']
    record['sorted_stage_added_clauses'] = encoding['added_clauses']
    record['added_variables'] += record['triangle_added_variables']
    record['added_clauses'] += record['triangle_added_clauses']
    record['variable_kinds'].update(emitter.kind_counts)
    record.pop('lex_sanity', None)
    record['clause_groups'].append(dict(name='actual_triangle_equivalences',
        first_clause=encoding['clauses']+1,
        last_clause=encoding['clauses']+triangle_record['triangle_definition_clauses'],
        clauses=triangle_record['triangle_definition_clauses']))
    record['clause_groups'].append(dict(name='per_vertex_triangle_upper_bounds_only',
        first_clause=encoding['clauses']+triangle_record['triangle_definition_clauses']+1,
        last_clause=record['clauses'],
        clauses=emitter.clause_count-triangle_record['triangle_definition_clauses']))
    record['source_dependencies'].append(
        'computations/dd82/construction/joint_boundary_completion_run/triangles/encode.py')
    record['review_status'] = 'Root-managed review of this triangle delta; no execution/review acceptance inferred'
    save(target / 'encoding.json', record)
    print(json.dumps({key: record[key] for key in ('status', 'case', 'variables', 'clauses',
          'triangle_budget', 'triangle_indicators', 'triangle_added_variables', 'triangle_added_clauses',
          'cnf_bytes', 'preparation_cpu_seconds', 'preparation_wall_seconds')}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'decode'))
    parser.add_argument('--case', choices=tuple(base.SOURCES), required=True)
    parser.add_argument('--log', type=Path)
    args = parser.parse_args()
    if args.action == 'prepare':
        prepare(args.case)
    else:
        base.HERE = HERE
        base.decode(args.case, args.log)
