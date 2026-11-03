"""Exact joint boundary completion: prepare or decode, never launch a solver.

Freeze precisely the source O/O induced graph, including nonedges. Every
R-incident adjacency is free; all degrees and all actual pairs are checked.
No order61 defect restriction, edit radius, or independent cross-degree is
imposed. Preparation retains the complete target CNF during source sanity.
"""
import argparse
import collections
import importlib.util
from itertools import combinations, product
import json
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
HELPER = ROOT / 'context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/code/n62/n62_ab_cnf.py'
SOURCES = {
    'n58': dict(n=58, source='computations/dd82/construction/twin59_to_58_deflation_run/component.path1.edges'),
    'n60': dict(n=60, source='computations/dd82/construction/fullgraph60_weighted_run/candidate.current.edges'),
}
SCOPE = ('Exact degree8 diameter2 completion with all original bad-pair endpoints R '
         'free to change every incident edge, and only the saved source O/O induced '
         'subgraph fixed; anchored construction domain, not all graphs of this order')


def save(path, record):
    path.write_text(json.dumps(record, indent=2) + '\n')


def pair(a, b):
    assert a != b
    return (a, b) if a < b else (b, a)


def load_helpers():
    # Reuse definitions only: do not instantiate the historical ABEncoder
    # or invoke its guarded main, data, branch conditions, or old jobs.
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location('joint_boundary_generic_cnf', HELPER)
    helper = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = helper
    spec.loader.exec_module(helper)
    return helper


def read_source(path, expected_n):
    with path.open() as source:
        n, claimed_edges = map(int, source.readline().split())
        raw = [tuple(map(int, line.split())) for line in source if line.strip()]
    assert n == expected_n
    assert all(len(edge) == 2 for edge in raw)
    assert all(0 <= a < n and 0 <= b < n and a != b for a, b in raw)
    edges = {pair(a, b) for a, b in raw}
    assert len(edges) == len(raw) == claimed_edges == n * 4
    neighbors = [set() for _ in range(n)]
    for a, b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)
    assert [len(row) for row in neighbors] == [8] * n
    # Exact original definition of an uncovered pair; no invalid source B.
    bad = [(a, b) for a, b in combinations(range(n), 2)
           if b not in neighbors[a] and not neighbors[a].intersection(neighbors[b])]
    repair = sorted({vertex for ab in bad for vertex in ab})
    assert bad and repair
    return n, edges, bad, repair


def evaluate_clause(literals, values, clause_id):
    """Extend already-known inputs through the emitted acyclic equivalences.

    AND/counter defining clauses introduce one output at a time. With the
    primary assignment given, unit consequences determine that output before
    the next auxiliary definition. A false degree/coverage clause is reported,
    never used to alter the input assignment. No SAT solver is called.
    """
    unknown = {}
    for literal in literals:
        var, required = abs(literal), literal > 0
        if var in values:
            if values[var] == required:
                return False
        else:
            unknown[var] = required
    if not unknown:
        return True
    assert len(unknown) == 1, (clause_id, 'auxiliary definition order is not evaluable', literals)
    var, value = next(iter(unknown.items()))
    values[var] = value
    return False


def build_model(helper, n, source_edges, repair, degree_target, output=None, retain_clauses=False):
    """The same encoder serves actual targets and a tiny exhaustive check."""
    class EvaluatedEmitter(helper.CNFEmitter):
        def __init__(self, destination):
            super().__init__(destination)
            self.values = {}
            self.false_clause_ids = []
            self.clauses = [] if retain_clauses else None

        def add_clause(self, *literals):
            super().add_clause(*literals)
            if self.clauses is not None:
                self.clauses.append(tuple(literals))
            if evaluate_clause(literals, self.values, self.clause_count):
                self.false_clause_ids.append(self.clause_count)

    em = EvaluatedEmitter(output)
    repair = frozenset(repair)
    outside = tuple(vertex for vertex in range(n) if vertex not in repair)
    free = {ab: em.new_var('free_A_edge') for ab in combinations(range(n), 2)
            if ab[0] in repair or ab[1] in repair}
    fixed = {ab: ab in source_edges for ab in combinations(outside, 2)}
    assert len(free) + len(fixed) == n * (n-1) // 2
    em.values.update({var: ab in source_edges for ab, var in free.items()})
    degrees, coverage, groups = [], [], []

    def edge(a, b):
        ab = pair(a, b)
        return free[ab] if ab in free else fixed[ab]

    def mark(name, before):
        groups.append(dict(name=name, first_clause=before+1, last_clause=em.clause_count,
                           clauses=em.clause_count-before))

    try:
        before = em.clause_count
        for a in range(n):
            fixed_degree, variables = 0, []
            for b in range(n):
                if b == a:
                    continue
                value = edge(a, b)
                if isinstance(value, bool):
                    fixed_degree += int(value)
                else:
                    variables.append(value)
            residual = degree_target - fixed_degree
            first_clause = em.clause_count + 1
            helper.enforce_exact(em, variables, residual, 'exact_degree_threshold')
            degrees.append(dict(vertex=a, total_target=degree_target, fixed_degree=fixed_degree,
                                free_incident_variables=variables, residual_target=residual,
                                first_clause=first_clause, last_clause=em.clause_count))
        mark('all_original_vertices_exact_degree', before)

        before = em.clause_count
        simplifications = collections.Counter()
        for a, b in combinations(range(n), 2):
            direct = edge(a, b)
            if direct is True:
                coverage.append(dict(pair=[a, b], status='tautology_fixed_direct_edge',
                                     coverage_clause=None, fixed_path=[a, b]))
                simplifications['coverage_fixed_direct'] += 1
                continue
            terms, fixed_middle = [], None
            counts = collections.Counter()
            for middle in range(n):
                if middle in (a, b):
                    continue
                left, right = edge(a, middle), edge(middle, b)
                if left is False or right is False:
                    counts['zero_path'] += 1
                elif left is True and right is True:
                    fixed_middle = middle
                    break
                elif left is True:
                    assert not isinstance(right, bool)
                    terms.append((middle, 'literal', right))
                    counts['one_fixed_edge_path'] += 1
                elif right is True:
                    assert not isinstance(left, bool)
                    terms.append((middle, 'literal', left))
                    counts['one_fixed_edge_path'] += 1
                else:
                    assert not isinstance(left, bool) and not isinstance(right, bool)
                    terms.append((middle, 'and', (left, right)))
                    counts['two_free_edge_path'] += 1
            if fixed_middle is not None:
                coverage.append(dict(pair=[a, b], status='tautology_fixed_two_edge_path',
                                     coverage_clause=None, fixed_path=[a, fixed_middle, b]))
                simplifications['coverage_fixed_two_edge_path'] += 1
                continue
            literals = [] if direct is False else [direct]
            path_records = []
            for middle, kind, term in terms:
                if kind == 'and':
                    out = em.new_var('actual_two_free_edge_path')
                    helper.add_iff_and(em, out, *term)
                    literals.append(out)
                    path_records.append(dict(middle=middle, kind=kind, variable=out,
                                             edge_inputs=list(term)))
                else:
                    literals.append(term)
                    path_records.append(dict(middle=middle, kind=kind, variable=term))
            # A literal can witness several actual paths; duplicate OR terms
            # do not add a coverage obligation. Every witness remains logged.
            literals = list(dict.fromkeys(literals))
            em.add_clause(*literals)
            coverage.append(dict(pair=[a, b], status='emitted', direct=direct,
                                 coverage_clause=em.clause_count, literals=literals,
                                 actual_middle_vertices=n-2, path_simplifications=dict(counts),
                                 path_records=path_records))
            simplifications.update(counts)
            simplifications['coverage_emitted'] += 1
        mark('all_actual_original_pair_coverage_with_faithful_constant_simplification', before)
        assert len(coverage) == n * (n-1) // 2
        assert set(em.values) == set(range(1, em.variable_count+1))
        em.finish()
    except BaseException:
        em.abort()
        raise
    return dict(emitter=em, free=free, fixed=fixed, outside=outside,
                degrees=degrees, coverage=coverage, clause_groups=groups,
                simplifications=dict(simplifications))


def check_dimacs(path, values, variables, clauses):
    """Read the saved input afresh and evaluate every actual emitted clause."""
    false_ids, count = [], 0
    assert set(values) == set(range(1, variables+1))
    with path.open() as source:
        assert source.readline().split() == ['p', 'cnf', str(variables), str(clauses)]
        for line in source:
            literals = list(map(int, line.split()))
            assert literals and literals[-1] == 0
            count += 1
            if not any(values[abs(literal)] == (literal > 0) for literal in literals[:-1]):
                false_ids.append(count)
    assert count == clauses
    return dict(clauses_checked=count, assigned_variables=len(values), false_clause_ids=false_ids,
                all_clauses_satisfied=not false_ids)


def write_assignment(path, values):
    with path.open('w') as output:
        for start in range(1, len(values)+1, 100):
            signed = [var if values[var] else -var for var in range(start, min(start+100, len(values)+1))]
            output.write('v ' + ' '.join(map(str, signed)) + ' 0\n')


def independent_small_target(n, edges, degree_target):
    """Separate BFS semantics for tiny verification, not encoder path logic."""
    adjacency = [[] for _ in range(n)]
    for a, b in edges:
        adjacency[a].append(b)
        adjacency[b].append(a)
    if any(len(row) != degree_target for row in adjacency):
        return False
    for start in range(n):
        distances = {start: 0}
        queue = collections.deque([start])
        while queue:
            a = queue.popleft()
            for b in adjacency[a]:
                if b not in distances:
                    distances[b] = distances[a]+1
                    queue.append(b)
        if len(distances) != n or max(distances.values()) > 2:
            return False
    return True


def small_input_sanity(helper):
    """Compare one actual small CNF against all its128 anchored edge choices."""
    n, degree_target, repair = 5, 2, (0, 2)
    cycle = {pair(vertex, (vertex+1) % n) for vertex in range(n)}
    model = build_model(helper, n, cycle, repair, degree_target, retain_clauses=True)
    em, free, fixed = model['emitter'], model['free'], model['fixed']
    assert len(free) == 7 and independent_small_target(n, cycle, degree_target)
    assert not em.false_clause_ids
    checked, accepted = 0, 0
    for bits in product((False, True), repeat=len(free)):
        values = {var: bit for var, bit in zip(free.values(), bits)}
        actual_edges = {ab for ab, value in fixed.items() if value}
        actual_edges.update(ab for (ab, var), bit in zip(free.items(), bits) if bit)
        false_ids = []
        for clause_id, literals in enumerate(em.clauses, 1):
            if evaluate_clause(literals, values, clause_id):
                false_ids.append(clause_id)
        assert len(values) == em.variable_count
        # Complete-assignment evaluation is distinct from extension itself.
        actual_false = [index for index, literals in enumerate(em.clauses, 1)
                        if not any(values[abs(var)] == (var > 0) for var in literals)]
        assert actual_false == false_ids
        semantic_target = independent_small_target(n, actual_edges, degree_target)
        assert (not false_ids) == semantic_target, (bits, false_ids, semantic_target)
        checked += 1
        accepted += int(semantic_target)
    assert checked == 128
    return dict(status='PASSED', n=n, source='explicit five-cycle', degree_target=degree_target,
                repair=list(repair), outside=list(model['outside']), free_edges=len(free),
                primary_assignments_checked=checked, accepted_targets=accepted,
                variables=em.variable_count, clauses=em.clause_count,
                solver_calls=0, scope='This actual tiny CNF versus independent degree/BFS semantics only')


def prepare(case):
    started_cpu, started_wall = time.process_time(), time.monotonic()
    target = HERE / case
    target.mkdir(exist_ok=True)
    assert not (target / 'input.cnf').exists() and not (target / 'encoding.json').exists(), 'Preserve prior preparation'
    helper = load_helpers()
    source_spec = SOURCES[case]
    n, source_edges, bad, repair = read_source(ROOT / source_spec['source'], source_spec['n'])
    small = small_input_sanity(helper)
    save(target / 'small_input_sanity.json', small)
    model = build_model(helper, n, source_edges, repair, 8, output=target / 'input.cnf')
    em, free, fixed = model['emitter'], model['free'], model['fixed']
    bad_set = set(bad)
    bad_clause_ids = [entry['coverage_clause'] for entry in model['coverage']
                      if tuple(entry['pair']) in bad_set]
    assert len(bad_clause_ids) == len(bad) and None not in bad_clause_ids
    source_check = check_dimacs(target / 'input.cnf', em.values, em.variable_count, em.clause_count)
    assert source_check['false_clause_ids'] == em.false_clause_ids == bad_clause_ids
    source_check.update(status='PASSED_SOURCE_ASSIGNMENT_SANITY', source_graph=source_spec['source'],
                        original_bad_pairs=bad, bad_pair_coverage_clause_ids=bad_clause_ids,
                        satisfies_full_target=False,
                        satisfies_every_clause_except_original_bad_pair_coverage=True,
                        target_input_retains_all_bad_pair_coverage=True,
                        relaxed_input_written=False, solver_calls=0)
    save(target / 'source_sanity.json', source_check)
    write_assignment(target / 'source.assignment.txt', em.values)
    save(target / 'edge_variables.json', dict(format=['u', 'v', 'variable'],
        rows=[[a, b, var] for (a, b), var in free.items()],
        fixed_format=['u', 'v', 'value'], fixed_rows=[[a, b, int(value)] for (a, b), value in fixed.items()]))
    save(target / 'degree_constraints.json', model['degrees'])
    save(target / 'coverage.json', dict(records=model['coverage']))
    result = dict(status='PREPARED_NOT_RUN', solver_calls=0, case=case, scope=SCOPE, n=n,
                  degree_target=8, source_graph=source_spec['source'], source_edges=len(source_edges),
                  original_bad_pairs=bad, repair_vertices=repair, outside_vertices=model['outside'],
                  variables=em.variable_count, clauses=em.clause_count, variable_kinds=em.kind_counts,
                  primary_edge_variables=len(free), fixed_pairs=len(fixed),
                  fixed_edges=sum(fixed.values()), fixed_nonedges=len(fixed)-sum(fixed.values()),
                  all_original_pair_count=n*(n-1)//2,
                  coverage_clauses=model['simplifications'].get('coverage_emitted', 0),
                  simplified_fixed_coverage_pairs=n*(n-1)//2-model['simplifications'].get('coverage_emitted', 0),
                  simplifications=model['simplifications'], clause_groups=model['clause_groups'],
                  exact_degree_constraints=len(model['degrees']),
                  all_bad_pair_obligations_retained=True, relaxed_input_written=False,
                  source_assignment_sanity='PASSED_SOURCE_ASSIGNMENT_SANITY', small_input_sanity='PASSED',
                  cnf_bytes=(target / 'input.cnf').stat().st_size,
                  mathematical_dependencies=['proofs/dd82/construction/JOINT_BOUNDARY_COMPLETION_DIRECTION.md'],
                  helper_reuse='CNFEmitter, enforce_exact, add_iff_and; generic definitions only',
                  no_order61_defect_assumptions=True, edit_radius=None,
                  independently_fixed_R_O_degree_split=False,
                  review_status='Root-managed source and Gemini review; implementation does not attest acceptance',
                  preparation_cpu_seconds=time.process_time()-started_cpu,
                  preparation_wall_seconds=time.monotonic()-started_wall)
    save(target / 'encoding.json', result)
    print(json.dumps({key: result[key] for key in ('status', 'case', 'n', 'primary_edge_variables',
          'variables', 'clauses', 'coverage_clauses', 'cnf_bytes',
          'preparation_cpu_seconds', 'preparation_wall_seconds')}, indent=2))


def decode(case, log_path=None):
    target = HERE / case
    log_path = log_path or target / 'solver.log'
    encoding = json.loads((target / 'encoding.json').read_text())
    values, sat = {}, False
    with log_path.open() as source:
        for line in source:
            if line.strip() == 's SATISFIABLE':
                sat = True
            if line.startswith('v '):
                for literal in map(int, line.split()[1:]):
                    if literal:
                        var, value = abs(literal), literal > 0
                        assert var not in values or values[var] == value
                        values[var] = value
    assert sat
    checked = check_dimacs(target / 'input.cnf', values, encoding['variables'], encoding['clauses'])
    save(target / 'model_check.json', checked)
    assert checked['all_clauses_satisfied']
    mapping = json.loads((target / 'edge_variables.json').read_text())
    free_pairs = {(a, b) for a, b, var in mapping['rows']}
    fixed_pairs = {(a, b) for a, b, value in mapping['fixed_rows']}
    assert not free_pairs.intersection(fixed_pairs)
    assert free_pairs.union(fixed_pairs) == set(combinations(range(encoding['n']), 2))
    edges = [(a, b) for a, b, var in mapping['rows'] if values[var]]
    edges.extend((a, b) for a, b, value in mapping['fixed_rows'] if value)
    edges.sort()
    assert len(edges) == encoding['n'] * 4
    save(target / 'candidate.json', dict(n=encoding['n'], edges=edges, source_case=case,
         source_solver_log=str(log_path), status='SAT_CANDIDATE_PENDING_INDEPENDENT_BFS'))
    (target / 'candidate.edges').write_text(f"{encoding['n']} {len(edges)}\n" +
                                          ''.join(f'{a} {b}\n' for a, b in edges))
    write_assignment(target / 'model.assignment.txt', values)
    print(json.dumps(dict(status='SAT_CANDIDATE_PENDING_INDEPENDENT_BFS', n=encoding['n'],
                          edges=len(edges), source_case=case), indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'decode'))
    parser.add_argument('--case', choices=tuple(SOURCES), required=True)
    parser.add_argument('--log', type=Path)
    args = parser.parse_args()
    prepare(args.case) if args.action == 'prepare' else decode(args.case, args.log)
