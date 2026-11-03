"""Two fixed C29 sides and a completely free six-regular cross matrix.

Prepare/decode never invoke a solver. Only generic CNF primitives and generic
assignment checks are imported; no previous graph-completion model is used.
"""
import argparse
from collections import deque
import importlib.util
from itertools import combinations, product
import json
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location(
    'free_cross_generic_checks', HERE.parent / 'joint_boundary_completion_run/encode.py')
support = importlib.util.module_from_spec(spec)
spec.loader.exec_module(support)
helper = support.load_helpers()
SCOPE = ('Exact Hamilton subfamily: the induced graphs on 0..28 and 29..57 '
         'are fixed standard C29 cycles, and all 841 cross edges are free, '
         'with row and column sums six and every actual pair at distance at '
         'most two. No circulant, symmetry, matching, geometry, or P=I constraint. '
         'This is not the general two-factor family or all 58-vertex graphs.')
EXPECTED_CNF = (31581, 102341)


class RetainedEmitter(helper.CNFEmitter):
    def __init__(self):
        super().__init__(None)
        self.clauses = []

    def add_clause(self, *literals):
        self.clauses.append(tuple(literals))
        super().add_clause(*literals)


def save(path, record):
    path.write_text(json.dumps(record, indent=2) + '\n')


def cycle_edges(m):
    assert m >= 3
    return {tuple(sorted((offset+i, offset+(i+1) % m)))
            for offset in (0, m) for i in range(m)}


def far_pairs(m):
    return [(i, j) for i, j in combinations(range(m), 2)
            if min(j-i, m-(j-i)) > 2]


def build(m, cross_degree):
    """The same restricted matrix model serves small semantics and C29."""
    assert m >= 3 and 0 <= cross_degree <= m

    em = RetainedEmitter()
    cross = [[em.new_var('cross_edge') for j in range(m)] for i in range(m)]
    degrees, coverage, groups = [], [], []

    def mark(name, before):
        groups.append(dict(name=name, first_clause=before+1,
                           last_clause=em.clause_count, clauses=em.clause_count-before))

    before = em.clause_count
    for side in ('left', 'right'):
        for index in range(m):
            inputs = cross[index] if side == 'left' else [cross[i][index] for i in range(m)]
            first = em.clause_count+1
            helper.enforce_exact(em, inputs, cross_degree, 'cross_degree_threshold')
            degrees.append(dict(side=side, index=index, variables=inputs,
                                first_clause=first, last_clause=em.clause_count))
    mark('exact_cross_row_and_column_degrees', before)

    before = em.clause_count
    for i in range(m):
        for j in range(m):
            em.add_clause(cross[i][j], cross[(i-1) % m][j], cross[(i+1) % m][j],
                          cross[i][(j-1) % m], cross[i][(j+1) % m])
            coverage.append(dict(side='cross', pair=[i, m+j], clause=em.clause_count))
    mark('cross_actual_direct_or_mixed_two_edge_paths', before)

    for side in ('left', 'right'):
        before = em.clause_count
        for i, j in far_pairs(m):
            paths = []
            for middle in range(m):
                a, b = ((cross[i][middle], cross[j][middle]) if side == 'left'
                        else (cross[middle][i], cross[middle][j]))
                out = em.new_var('actual_two_cross_edge_path')
                helper.add_iff_and(em, out, a, b)
                paths.append(out)
            em.add_clause(*paths)
            offset = 0 if side == 'left' else m
            coverage.append(dict(side=side, pair=[offset+i, offset+j],
                                 clause=em.clause_count, path_variables=paths))
        mark(side+'_far_pairs_actual_shared_cross_neighbors', before)
    return dict(m=m, cross_degree=cross_degree, emitter=em, cross=cross,
                degrees=degrees, coverage=coverage, clause_groups=groups)


def graph_check(matrix, cross_degree):
    """Expand every actual edge, then BFS; do not use coverage clauses."""
    m = len(matrix)
    assert all(len(row) == m and all(value in (0, 1) for value in row) for row in matrix)
    edges = cycle_edges(m) | {(i, m+j) for i in range(m) for j in range(m) if matrix[i][j]}
    adjacent = [set() for _ in range(2*m)]
    for a, b in edges:
        adjacent[a].add(b)
        adjacent[b].add(a)
    bad, maximum, connected = [], 0, True
    for source in range(2*m):
        distances = [-1]*(2*m)
        distances[source] = 0
        queue = deque([source])
        while queue:
            vertex = queue.popleft()
            for other in adjacent[vertex]:
                if distances[other] < 0:
                    distances[other] = distances[vertex]+1
                    queue.append(other)
        connected = connected and -1 not in distances
        maximum = max(maximum, max(distances))
        bad.extend([source, other] for other in range(source+1, 2*m)
                   if distances[other] < 0 or distances[other] > 2)
    degrees = list(map(len, adjacent))
    return dict(n=2*m, edges=sorted(edges), degrees=degrees,
                degree_target=cross_degree+2, exact_degrees=degrees == [cross_degree+2]*(2*m),
                diameter=maximum if connected else None, connected=connected,
                bad_pairs=bad, target_graph=not bad and degrees == [cross_degree+2]*(2*m))


def check_explicit_matrix(model, name, matrix):
    """Assign C explicitly and extend every exact auxiliary definition."""
    m, em = model['m'], model['emitter']
    assert len(matrix) == m
    graph = graph_check(matrix, model['cross_degree'])
    values = {model['cross'][i][j]: bool(matrix[i][j]) for i in range(m) for j in range(m)}
    false = {index for index, clause in enumerate(em.clauses, 1)
             if support.evaluate_clause(clause, values, index)}
    assert set(values) == set(range(1, em.variable_count+1))
    # Re-evaluate complete values, including every AND and counter clause.
    assert false == {index for index, clause in enumerate(em.clauses, 1)
                     if not any(values[abs(literal)] == (literal > 0) for literal in clause)}
    coverage_bad = [row['pair'] for row in model['coverage'] if row['clause'] in false]
    assert sorted(coverage_bad) == graph['bad_pairs']
    permitted_false = {row['clause'] for row in model['coverage']}
    failed_degrees = []
    for row in model['degrees']:
        region = set(range(row['first_clause'], row['last_clause']+1))
        wrong = sum(values[var] for var in row['variables']) != model['cross_degree']
        assert bool(false.intersection(region)) == wrong
        if wrong:
            failed_degrees.append([row['side'], row['index']])
        permitted_false.update(region)
    assert false <= permitted_false  # In particular all AND definitions hold.
    assert (not false) == graph['target_graph']
    counts = {side: sum(row['clause'] in false for row in model['coverage'] if row['side'] == side)
              for side in ('cross', 'left', 'right')}
    record = dict(name=name, n=2*m, cross_degree=model['cross_degree'],
                  variables=em.variable_count, clauses=em.clause_count,
                  assigned_variables=len(values), false_clauses=len(false),
                  exact_degrees=graph['exact_degrees'], failed_degrees=failed_degrees,
                  bad_pairs=len(graph['bad_pairs']), bad_pairs_by_type=counts,
                  diameter=graph['diameter'], target_graph=graph['target_graph'],
                  complete_clause_check_matches_BFS=True)
    return record, values


def circulant_matrix(m, offsets):
    return [[int((j-i) % m in offsets) for j in range(m)] for i in range(m)]


def semantic_sanity():
    start = time.process_time()
    # All eight valuations establish the full bidirectional AND truth table.
    em = RetainedEmitter()
    a, b, out = (em.new_var('truth_table') for _ in range(3))
    helper.add_iff_and(em, out, a, b)
    for av, bv, ov in product((False, True), repeat=3):
        values = {a: av, b: bv, out: ov}
        satisfied = all(any(values[abs(lit)] == (lit > 0) for lit in clause) for clause in em.clauses)
        assert satisfied == (ov == (av and bv))
    cases = [
        ('triangular_prism', 3, 1, circulant_matrix(3, {0}), (0, 0, 0), True),
        ('both_coverages_valid', 6, 2, circulant_matrix(6, {0, 3}), (0, 0, 0), True),
        ('cross_covered_but_same_side_fails', 6, 3, circulant_matrix(6, {0, 2, 4}), (0, 3, 3), False),
        ('same_side_covered_but_cross_fails', 7, 2, circulant_matrix(7, {0, 3}), (7, 0, 0), False),
    ]
    records = []
    for name, m, degree, matrix, expected_bad, expected_target in cases:
        row, _ = check_explicit_matrix(build(m, degree), name, matrix)
        assert tuple(row['bad_pairs_by_type'][side] for side in ('cross', 'left', 'right')) == expected_bad
        assert row['exact_degrees'] and row['target_graph'] == expected_target
        records.append(row)
    changed = circulant_matrix(6, {0, 3})
    changed[0][0], changed[0][1] = 0, 1
    for name, matrix, wrong_side in (
            ('rows_correct_columns_wrong', changed, 'right'),
            ('columns_correct_rows_wrong', list(map(list, zip(*changed))), 'left')):
        row, _ = check_explicit_matrix(build(6, 2), name, matrix)
        assert row['failed_degrees'] == [[wrong_side, 0], [wrong_side, 1]]
        assert not row['target_graph']
        records.append(row)
    return dict(status='SMALL_MATRIX_SEMANTICS_PASSED', AND_truth_table_assignments=8,
                matrix_assignments=len(records), records=records,
                official_C29_model_built=False, solver_calls=0,
                elapsed_cpu=time.process_time()-start)


def prepare(output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    assert not any((output_dir / name).exists() for name in
                   ('input.cnf', 'encoding.json', 'variable_map.json'))
    cpu, wall = time.process_time(), time.monotonic()
    sanity = semantic_sanity()
    model = build(29, 6)
    em = model['emitter']
    assert (em.variable_count, em.clause_count) == EXPECTED_CNF
    assert len(far_pairs(29)) == 348
    assert em.kind_counts == dict(cross_edge=841, cross_degree_threshold=10556,
                                  actual_two_cross_edge_path=20184)
    # An explicit degree-eight graph checks actual emitted clauses without
    # restricting C to this deliberately simple example in the SAT model.
    source, values = check_explicit_matrix(model, 'C29_six_consecutive_offsets_sanity_only',
                                          circulant_matrix(29, set(range(6))))
    assert source['exact_degrees'] and not source['target_graph']
    with (output_dir / 'input.cnf').open('w') as output:
        output.write(f'p cnf {em.variable_count} {em.clause_count}\n')
        for clause in em.clauses:
            output.write(' '.join(map(str, clause)) + ' 0\n')
    reread = support.check_dimacs(output_dir / 'input.cnf', values, em.variable_count, em.clause_count)
    assert len(reread['false_clause_ids']) == source['false_clauses'] == source['bad_pairs']
    sanity.update(official_C29_model_built=True, explicit_C29_assignment=source,
                  saved_DIMACS_explicit_assignment_check=reread)
    save(output_dir / 'sanity.json', sanity)
    save(output_dir / 'variable_map.json', dict(n=58, side_size=29, cross_degree=6,
         cross_variables=model['cross'], fixed_internal_edges=sorted(cycle_edges(29)),
         P_variables=[], P_normalized=False))
    record = dict(status='PREPARED_NOT_RUN', scope=SCOPE, n=58, side_size=29,
                  cross_degree=6, degree_target=8, expected_edges=232,
                  variables=em.variable_count, clauses=em.clause_count,
                  variable_kinds=em.kind_counts, clause_groups=model['clause_groups'],
                  cross_cover_clauses=841, same_side_cover_clauses=696,
                  same_side_AND_witnesses=20184, fixed_internal_edges=58,
                  P_normalized=False, circulant_cross_matrix_required=False,
                  degree_records=model['degrees'], coverage_records=model['coverage'],
                  solver_calls=0, elapsed_cpu=time.process_time()-cpu,
                  elapsed_wall=time.monotonic()-wall)
    save(output_dir / 'encoding.json', record)
    print(json.dumps({key: record[key] for key in ('status', 'scope', 'variables', 'clauses',
                                                  'elapsed_cpu', 'elapsed_wall')}, indent=2))


def decode(output_dir, model_path=None):
    model_path = model_path or output_dir / 'solver.log'
    record = json.loads((output_dir / 'encoding.json').read_text())
    mapping = json.loads((output_dir / 'variable_map.json').read_text())
    assert record['n'] == mapping['n'] == 58 and mapping['side_size'] == 29
    assert record['cross_degree'] == mapping['cross_degree'] == 6
    assert (record['variables'], record['clauses']) == EXPECTED_CNF
    assert mapping['cross_variables'] == [[29*i+j+1 for j in range(29)] for i in range(29)]
    assert mapping['fixed_internal_edges'] == [list(edge) for edge in sorted(cycle_edges(29))]
    values, saw_sat = {}, False
    for line in model_path.read_text().splitlines():
        if line.strip() == 's SATISFIABLE':
            saw_sat = True
        if line.startswith('v '):
            for literal in map(int, line.split()[1:]):
                if literal:
                    var, value = abs(literal), literal > 0
                    assert var not in values or values[var] == value
                    values[var] = value
    assert saw_sat, 'A terminal SAT model is required'
    clause_check = support.check_dimacs(output_dir / 'input.cnf', values,
                                         record['variables'], record['clauses'])
    assert clause_check['all_clauses_satisfied'], 'Saved full DIMACS assignment fails clauses'
    matrix = [[int(values[var]) for var in row] for row in mapping['cross_variables']]
    graph = graph_check(matrix, 6)
    routes = [[matrix[i][j]+matrix[(i-1) % 29][j]+matrix[(i+1) % 29][j]
               +matrix[i][(j-1) % 29]+matrix[i][(j+1) % 29]
               for j in range(29)] for i in range(29)]
    permutation = [[value-1 for value in row] for row in routes]
    is_permutation = (all(value in (0, 1) for row in permutation for value in row)
                      and all(sum(row) == 1 for row in permutation)
                      and all(sum(permutation[i][j] for i in range(29)) == 1 for j in range(29)))
    target = graph['target_graph'] and len(graph['edges']) == 232 and is_permutation
    result = dict(status='SAT_FREE_CROSS_TARGET_CHECKED' if target else 'SAT_DECODE_VALIDATION_FAILED',
                  scope=SCOPE, n=58, edges=graph['edges'], side_size=29,
                  fixed_internal_edges=mapping['fixed_internal_edges'], C=matrix, P=permutation,
                  P_is_permutation=is_permutation, cross_route_counts=routes,
                  target_graph=target, verification=graph, all_bad_pairs=graph['bad_pairs'],
                  model_check=clause_check, source_model=str(model_path),
                  independent_external_verification_performed=False)
    (output_dir / 'candidate.edges').write_text(f"58 {len(graph['edges'])}\n" +
        ''.join(f'{a} {b}\n' for a, b in graph['edges']))
    save(output_dir / 'candidate.json', result)
    print(json.dumps(dict(status=result['status'], n=58, edges=len(graph['edges']),
                         bad_pairs=len(graph['bad_pairs']), target_graph=target,
                         P_is_permutation=is_permutation), indent=2))
    if not target:
        raise SystemExit(2)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'decode', 'sanity'))
    parser.add_argument('--output-dir', '--out-dir', type=Path, default=HERE)
    parser.add_argument('--model', '--log', type=Path)
    args = parser.parse_args(argv)
    if args.action == 'prepare':
        prepare(args.output_dir)
    elif args.action == 'decode':
        decode(args.output_dir, args.model)
    else:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        result = semantic_sanity()
        save(args.output_dir / 'small_sanity.json', result)
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
