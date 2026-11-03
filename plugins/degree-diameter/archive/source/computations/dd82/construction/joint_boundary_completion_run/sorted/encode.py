"""Append proved R-to-O row ordering to the exact joint-boundary inputs.

Preparation and decoding only. The parent input body is copied verbatim;
the new clauses choose labels within R while O stays pointwise fixed.
"""
import argparse
from copy import deepcopy
import importlib.util
from itertools import product
import json
from pathlib import Path
import shutil
import sys
import time

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('joint_boundary_sorted_base_encode', BASE / 'encode.py')
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
ROOT = base.ROOT


def save(path, record):
    path.write_text(json.dumps(record, indent=2) + '\n')


def lex_extension(helper, initial_variables, rows):
    """Exact adjacent-row lex constraints with equivalent prefix variables."""
    class MemoryEmitter(helper.CNFEmitter):
        def __init__(self):
            super().__init__(None)
            self.variable_count = initial_variables
            self.clauses = []

        def add_clause(self, *literals):
            super().add_clause(*literals)
            self.clauses.append(tuple(literals))

    emitter = MemoryEmitter()
    prefixes, row_records = [], []
    assert rows and rows[0] and all(len(row) == len(rows[0]) for row in rows)
    for row_index, (left, right) in enumerate(zip(rows, rows[1:])):
        first_clause = emitter.clause_count + 1
        previous = True
        for column, (x, y) in enumerate(zip(left, right)):
            # Equal preceding columns require 0<=1 at this column.
            if previous is True:
                emitter.add_clause(-x, y)
            else:
                emitter.add_clause(-previous, -x, y)
            if column == len(left)-1:
                continue  # No unused final prefix variable.
            out = emitter.new_var('lex_equal_prefix')
            if previous is not True:
                emitter.add_clause(-out, previous)
            emitter.add_clause(-out, -x, y)
            emitter.add_clause(-out, x, -y)
            guard = [] if previous is True else [-previous]
            emitter.add_clause(*guard, -x, -y, out)
            emitter.add_clause(*guard, x, y, out)
            prefixes.append(dict(variable=out, previous_prefix=previous, left=x, right=y,
                                 adjacent_rows=[row_index, row_index+1], through_column=column))
            previous = out
        row_records.append(dict(adjacent_rows=[row_index, row_index+1],
                                first_added_clause=first_clause, last_added_clause=emitter.clause_count))
    return emitter, prefixes, row_records


def small_lex_sanity(helper):
    """Exhaust every input and prefix assignment for widths1,2,3 only."""
    widths = []
    for width in (1, 2, 3):
        rows = [list(range(1, width+1)), list(range(width+1, 2*width+1))]
        emitter, prefixes, unused = lex_extension(helper, 2*width, rows)
        checked, accepted = 0, 0
        for bits in product((False, True), repeat=emitter.variable_count):
            values = {var: value for var, value in enumerate(bits, 1)}
            left = tuple(values[var] for var in rows[0])
            right = tuple(values[var] for var in rows[1])
            actual = all(any(values[abs(var)] == (var > 0) for var in clause)
                         for clause in emitter.clauses)
            exact_prefixes = all(values[entry['variable']] ==
                                 (left[:entry['through_column']+1] == right[:entry['through_column']+1])
                                 for entry in prefixes)
            expected = left <= right and exact_prefixes
            assert actual == expected, (width, bits, actual, expected)
            checked += 1
            accepted += int(actual)
        widths.append(dict(width=width, complete_assignments_checked=checked,
                           accepted_assignments=accepted, added_variables=len(prefixes),
                           clauses=emitter.clause_count))
    return dict(status='PASSED', checks=widths, solver_calls=0,
                scope='Exact truth tables of only the new lex/prefix clauses; no old C5 rerun')


def prepare(case):
    started_cpu, started_wall = time.process_time(), time.monotonic()
    source_dir, target = BASE / case, HERE / case
    target.mkdir(exist_ok=True)
    assert not (target / 'input.cnf').exists() and not (target / 'encoding.json').exists(), 'Preserve prior sorted preparation'
    encoding = json.loads((source_dir / 'encoding.json').read_text())
    assert encoding['status'] == 'PREPARED_NOT_RUN' and encoding['n'] == int(case[1:])
    mapping = json.loads((source_dir / 'edge_variables.json').read_text())
    free = {(a, b): var for a, b, var in mapping['rows']}
    fixed = {(a, b): bool(value) for a, b, value in mapping['fixed_rows']}
    repair = encoding['repair_vertices']
    outside = encoding['outside_vertices']
    assert repair == sorted(repair) and outside == sorted(outside)
    rows = [[free[base.pair(a, b)] for b in outside] for a in repair]
    helper = base.load_helpers()
    lex_sanity = small_lex_sanity(helper)
    extension, prefixes, row_records = lex_extension(helper, encoding['variables'], rows)
    expected_counts = {'n58': (759, 4554), 'n60': (816, 4896)}
    assert (len(prefixes), extension.clause_count) == expected_counts[case]

    # Sort only R and consistently relabel every incident edge, including R/R.
    n, source_edges, original_bad, original_repair = base.read_source(
        ROOT / encoding['source_graph'], encoding['n'])
    assert original_repair == repair and [list(ab) for ab in original_bad] == encoding['original_bad_pairs']
    ordered_old = sorted(repair, key=lambda a: tuple(base.pair(a, b) in source_edges for b in outside))
    permutation = {vertex: vertex for vertex in outside}
    permutation.update({old: new for old, new in zip(ordered_old, repair)})
    assert sorted(permutation) == sorted(permutation.values()) == list(range(n))
    relabelled = {base.pair(permutation[a], permutation[b]) for a, b in source_edges}
    relabelled_bad = sorted(base.pair(permutation[a], permutation[b]) for a, b in original_bad)
    rebuilt = base.build_model(helper, n, relabelled, repair, 8, retain_clauses=True)
    emitter = rebuilt['emitter']
    assert rebuilt['free'] == free and rebuilt['fixed'] == fixed
    assert emitter.variable_count == encoding['variables'] and emitter.clause_count == encoding['clauses']

    # Establish that the in-memory auxiliary definitions are the exact existing
    # input definitions before using their relabelled source assignment.
    with (source_dir / 'input.cnf').open('r', encoding='ascii') as stream:
        assert stream.readline().split() == ['p', 'cnf', str(encoding['variables']), str(encoding['clauses'])]
        for index, expected in enumerate(emitter.clauses, 1):
            actual = tuple(map(int, stream.readline().split()))
            assert actual == (*expected, 0), ('base clause differs', index)
        assert not stream.read().strip()

    # Copy the old body itself, not a reserialization of the in-memory clauses.
    with (source_dir / 'input.cnf').open('rb') as source:
        source.readline()
        with (target / 'input.cnf').open('wb') as output:
            output.write(f"p cnf {extension.variable_count} {encoding['clauses']+extension.clause_count}\n".encode('ascii'))
            shutil.copyfileobj(source, output, length=1024*1024)
            for clause in extension.clauses:
                output.write((' '.join(map(str, clause)) + ' 0\n').encode('ascii'))

    values = dict(emitter.values)
    for prefix in prefixes:
        previous = prefix['previous_prefix']
        equal_before = True if previous is True else values[previous]
        values[prefix['variable']] = equal_before and values[prefix['left']] == values[prefix['right']]
    sanity = base.check_dimacs(target / 'input.cnf', values, extension.variable_count,
                               encoding['clauses']+extension.clause_count)
    bad_set = set(relabelled_bad)
    bad_clause_ids = [entry['coverage_clause'] for entry in rebuilt['coverage']
                      if tuple(entry['pair']) in bad_set]
    assert None not in bad_clause_ids and len(bad_clause_ids) == len(original_bad)
    assert sanity['false_clause_ids'] == emitter.false_clause_ids == bad_clause_ids
    sanity.update(status='PASSED_RELABELLED_SOURCE_ASSIGNMENT_SANITY',
                  source_graph=encoding['source_graph'], original_bad_pairs=original_bad,
                  relabelled_bad_pairs=relabelled_bad, bad_pair_coverage_clause_ids=bad_clause_ids,
                  source_relabeling=[[old, permutation[old]] for old in range(n)],
                  source_satisfies_full_target=False,
                  satisfies_every_clause_except_relabelled_original_bad_pair_coverage=True,
                  all_added_lex_clauses_satisfied=True, complete_target_input_retained=True,
                  relaxed_input_written=False, solver_calls=0,
                  base_prefix_checked_clause_by_clause=True)
    save(target / 'source_sanity.json', sanity)
    save(target / 'lex_sanity.json', lex_sanity)
    base.write_assignment(target / 'source.assignment.txt', values)
    (target / 'relabelled_source.edges').write_text(f'{n} {len(relabelled)}\n' +
        ''.join(f'{a} {b}\n' for a, b in sorted(relabelled)))
    shutil.copyfile(source_dir / 'edge_variables.json', target / 'edge_variables.json')
    save(target / 'lex_constraints.json', dict(
        row_vertex_order=repair, column_vertex_order=outside, row_variables=rows,
        prefix_definitions=prefixes, adjacent_row_clause_groups=row_records,
        all_clause_indices_relative_to_added_body=True))

    record = deepcopy(encoding)
    record.update(scope=encoding['scope']+'; R-to-O rows lexicographically sorted by relabeling R only',
                  variables=extension.variable_count, clauses=encoding['clauses']+extension.clause_count,
                  added_variables=len(prefixes), added_clauses=extension.clause_count,
                  base_prefix=dict(input=str((source_dir/'input.cnf').relative_to(ROOT)),
                                   variables=encoding['variables'], clauses=encoding['clauses'],
                                   body_copied_verbatim=True, auxiliary_definitions_compared_to_input=True),
                  row_order=dict(rows=repair, columns=outside, direction='lexicographically nondecreasing',
                                 outside_labels_fixed=True, ties_allowed=True,
                                 graph_automorphism_assumed=False, RR_edges_relabelled_consistently=True),
                  source_assignment_sanity='PASSED_RELABELLED_SOURCE_ASSIGNMENT_SANITY',
                  lex_sanity='PASSED', relabelled_source_bad_pairs=relabelled_bad,
                  inherited_small_input_sanity=dict(
                     path=str((source_dir/'small_input_sanity.json').relative_to(ROOT)), rerun=False),
                  cnf_bytes=(target/'input.cnf').stat().st_size,
                  preparation_cpu_seconds=time.process_time()-started_cpu,
                  preparation_wall_seconds=time.monotonic()-started_wall)
    # The historical source small sanity remains an explicit inherited receipt.
    record.pop('small_input_sanity', None)
    record['variable_kinds'].update(extension.kind_counts)
    record['clause_groups'].append(dict(name='lexicographic_R_to_O_row_order',
        first_clause=encoding['clauses']+1, last_clause=record['clauses'], clauses=extension.clause_count))
    record['source_dependencies'] = ['computations/dd82/construction/joint_boundary_completion_run/encode.py',
                                    'computations/dd82/construction/joint_boundary_completion_run/sorted/encode.py']
    record['review_status'] = 'Root-managed review of this sorted delta; prior base review alone does not attest it'
    save(target / 'encoding.json', record)
    print(json.dumps({key: record[key] for key in ('status', 'case', 'variables', 'clauses',
                     'added_variables', 'added_clauses', 'cnf_bytes',
                     'preparation_cpu_seconds', 'preparation_wall_seconds')}, indent=2))


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
