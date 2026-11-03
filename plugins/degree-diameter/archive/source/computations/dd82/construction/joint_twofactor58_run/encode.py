"""Free two-regular internal graphs and free six-regular cross edges.

Right-side relabeling normalizes the cross excess permutation to I. Neither
internal graph, its cycle type, nor any diagonal cross entry is fixed.
Prepare/decode never launch a solver; sanity builds only small models.
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
    'twofactor_generic_checks', HERE.parent / 'joint_boundary_completion_run/encode.py')
support = importlib.util.module_from_spec(spec)
spec.loader.exec_module(support)
helper = support.load_helpers()
EXPECTED_CNF = (206103, 674424)
SCOPE = ('All 58-vertex degree-eight diameter-two graphs admitting a 29+29 '
         'partition with induced internal degree two and cross degree six. '
         'Both internal graphs and all cross edges are free. Right relabeling '
         'normalizes H0*C+C*H1+C to J+I without fixing any cycle type. '
         'No extra symmetry, triangle, diagonal-C, or Hamilton-exclusion clauses. '
         'This partition family is not all 58-vertex graphs.')


class Emitter(helper.CNFEmitter):
    def __init__(self):
        super().__init__(None)
        self.clauses = []

    def add_clause(self, *literals):
        self.clauses.append(tuple(literals))
        super().add_clause(*literals)


def save(path, record):
    path.write_text(json.dumps(record, indent=2) + '\n')


def build(m, cross_degree):
    """Exact model at arbitrary small m, with cross counts fixed to J+I.

    A positive regular instance necessarily has 5*cross_degree == m+1.
    Other parameters remain useful explicit negative semantic assignments.
    """
    assert m >= 3 and 1 <= cross_degree <= m
    em = Emitter()
    internal = []
    for side in range(2):
        matrix = [[0]*m for _ in range(m)]
        for i, j in combinations(range(m), 2):
            matrix[i][j] = matrix[j][i] = em.new_var('internal_edge')
        internal.append(matrix)
    cross = [[em.new_var('cross_edge') for j in range(m)] for i in range(m)]
    counters, coverage, groups = [], [], []

    def exact(inputs, target, kind, **record):
        first = em.clause_count+1
        helper.enforce_exact(em, inputs, target, kind+'_threshold')
        units = 1 if target in (0, len(inputs)) else 2
        counters.append(dict(kind=kind, target=target, first_clause=first,
                             last_clause=em.clause_count,
                             unit_clauses=list(range(em.clause_count-units+1, em.clause_count+1)),
                             **record))

    def AND(a, b, kind):
        assert a and b
        out = em.new_var(kind)
        helper.add_iff_and(em, out, a, b)
        return out

    def mark(name, before):
        groups.append(dict(name=name, first_clause=before+1,
                           last_clause=em.clause_count, clauses=em.clause_count-before))

    before = em.clause_count
    for side in range(2):
        for i in range(m):
            exact([internal[side][i][j] for j in range(m) if j != i], 2,
                  'internal_degree', side=side, vertex=i)
    mark('all_internal_degrees_two', before)
    before = em.clause_count
    for side in range(2):
        for i in range(m):
            inputs = cross[i] if side == 0 else [cross[j][i] for j in range(m)]
            exact(inputs, cross_degree, 'cross_degree', side=side, vertex=i)
    mark('all_cross_degrees_six', before)

    before = em.clause_count
    for i in range(m):
        for j in range(m):
            inputs = [cross[i][j]]
            inputs += [AND(internal[0][i][k], cross[k][j], 'mixed_cross_path')
                       for k in range(m) if k != i]
            inputs += [AND(cross[i][k], internal[1][k][j], 'mixed_cross_path')
                       for k in range(m) if k != j]
            assert len(inputs) == 2*m-1
            exact(inputs, 1+int(i == j), 'cross_routes', pair=[i, j])
    mark('all_cross_route_counts_J_plus_I', before)

    for side in range(2):
        before = em.clause_count
        for i, j in combinations(range(m), 2):
            inputs = [internal[side][i][j]]
            inputs += [AND(internal[side][i][k], internal[side][k][j], 'same_side_path')
                       for k in range(m) if k not in (i, j)]
            inputs += [AND(cross[i][k], cross[j][k], 'same_side_path') if side == 0
                       else AND(cross[k][i], cross[k][j], 'same_side_path') for k in range(m)]
            assert len(inputs) == 2*m-1
            em.add_clause(*inputs)
            coverage.append(dict(side=side, pair=[side*m+i, side*m+j], clause=em.clause_count))
        mark('side_'+str(side)+'_all_actual_pair_coverage', before)
    return dict(m=m, cross_degree=cross_degree, emitter=em, internal=internal,
                cross=cross, counters=counters, coverage=coverage, clause_groups=groups)


def graph_check(h0, h1, cross, cross_degree):
    """Construct the actual graph and count routes from adjacency sets/BFS."""
    m = len(cross)
    for matrix in (h0, h1, cross):
        assert len(matrix) == m and all(len(row) == m for row in matrix)
        assert all(value in (0, 1) for row in matrix for value in row)
    for matrix in (h0, h1):
        assert all(matrix[i][i] == 0 for i in range(m))
        assert all(matrix[i][j] == matrix[j][i] for i, j in combinations(range(m), 2))
    edges = {(side*m+i, side*m+j) for side, matrix in enumerate((h0, h1))
             for i, j in combinations(range(m), 2) if matrix[i][j]}
    edges.update((i, m+j) for i in range(m) for j in range(m) if cross[i][j])
    neighbors = [set() for _ in range(2*m)]
    for a, b in edges:
        neighbors[a].add(b)
        neighbors[b].add(a)
    bad, maximum, connected = [], 0, True
    for source in range(2*m):
        distance = [-1]*(2*m)
        distance[source] = 0
        queue = deque([source])
        while queue:
            vertex = queue.popleft()
            for other in neighbors[vertex]:
                if distance[other] < 0:
                    distance[other] = distance[vertex]+1
                    queue.append(other)
        connected = connected and -1 not in distance
        maximum = max(maximum, max(distance))
        bad.extend([source, other] for other in range(source+1, 2*m)
                   if distance[other] < 0 or distance[other] > 2)
    degrees = list(map(len, neighbors))
    internal_degrees = [list(map(sum, matrix)) for matrix in (h0, h1)]
    cross_degrees = [list(map(sum, cross)), [sum(cross[i][j] for i in range(m)) for j in range(m)]]
    routes = [[int(m+j in neighbors[i])+len(neighbors[i] & neighbors[m+j])
               for j in range(m)] for i in range(m)]
    mismatches = [[i, j, routes[i][j], 1+int(i == j)]
                  for i in range(m) for j in range(m) if routes[i][j] != 1+int(i == j)]
    exact_blocks = (internal_degrees == [[2]*m]*2 and cross_degrees == [[cross_degree]*m]*2)
    target = degrees == [cross_degree+2]*(2*m) and not bad
    return dict(n=2*m, edges=sorted(edges), degrees=degrees,
                internal_degrees=internal_degrees, cross_degrees=cross_degrees,
                exact_block_degrees=exact_blocks, diameter=maximum if connected else None,
                connected=connected, bad_pairs=bad, cross_route_counts=routes,
                cross_route_mismatches=mismatches, target_graph=target,
                normalized_target=exact_blocks and not bad and not mismatches)


def check_explicit(model, name, h0, h1, cross):
    m, em = model['m'], model['emitter']
    graph = graph_check(h0, h1, cross, model['cross_degree'])
    values = {model['internal'][side][i][j]: bool(matrix[i][j])
              for side, matrix in enumerate((h0, h1)) for i, j in combinations(range(m), 2)}
    values.update({model['cross'][i][j]: bool(cross[i][j]) for i in range(m) for j in range(m)})
    false = {index for index, clause in enumerate(em.clauses, 1)
             if support.evaluate_clause(clause, values, index)}
    assert set(values) == set(range(1, em.variable_count+1))
    assert false == {index for index, clause in enumerate(em.clauses, 1)
                     if not any(values[abs(lit)] == (lit > 0) for lit in clause)}
    permitted, failed_degrees, failed_routes = set(), [], []
    for row in model['counters']:
        if row['kind'] == 'cross_routes':
            i, j = row['pair']
            actual = graph['cross_route_counts'][i][j]
        else:
            field = 'internal_degrees' if row['kind'] == 'internal_degree' else 'cross_degrees'
            actual = graph[field][row['side']][row['vertex']]
        failed = false.intersection(range(row['first_clause'], row['last_clause']+1))
        assert bool(failed) == (actual != row['target'])
        assert failed <= set(row['unit_clauses'])
        permitted.update(row['unit_clauses'])
        if actual != row['target']:
            if row['kind'] == 'cross_routes':
                failed_routes.append([*row['pair'], actual, row['target']])
            else:
                failed_degrees.append([row['kind'], row['side'], row['vertex']])
    assert failed_routes == graph['cross_route_mismatches']
    same_bad = sorted(row['pair'] for row in model['coverage'] if row['clause'] in false)
    assert same_bad == [pair for pair in graph['bad_pairs'] if pair[0]//m == pair[1]//m]
    permitted.update(row['clause'] for row in model['coverage'])
    assert false <= permitted  # Every counter/AND definition holds.
    assert (not false) == graph['normalized_target']
    record = dict(name=name, n=2*m, cross_degree=model['cross_degree'],
                  variables=em.variable_count, clauses=em.clause_count,
                  assigned_variables=len(values), false_clauses=len(false),
                  failed_degrees=failed_degrees, cross_route_mismatches=len(failed_routes),
                  bad_pairs=len(graph['bad_pairs']), same_side_bad_pairs=len(same_bad),
                  diameter=graph['diameter'], target_graph=graph['target_graph'],
                  normalized_target=graph['normalized_target'], complete_semantics_matches=True)
    return record, values


def right_relabel(h0, h1, cross, order):
    """order[new_right_label] is its old label; C'=CQ, H1'=Q^T H1 Q."""
    m = len(cross)
    assert sorted(order) == list(range(m))
    return ([row[:] for row in h0], [[h1[i][j] for j in order] for i in order],
            [[row[j] for j in order] for row in cross])


def normalize(h0, h1, cross, cross_degree):
    graph = graph_check(h0, h1, cross, cross_degree)
    m = len(cross)
    excess = [[value-1 for value in row] for row in graph['cross_route_counts']]
    assert all(value in (0, 1) for row in excess for value in row)
    assert all(sum(row) == 1 for row in excess)
    assert all(sum(excess[i][j] for i in range(m)) == 1 for j in range(m))
    order = [row.index(1) for row in excess]
    normalized = right_relabel(h0, h1, cross, order)
    after = graph_check(*normalized, cross_degree)
    inverse = {old: new for new, old in enumerate(order)}
    relabel = lambda v: v if v < m else m+inverse[v-m]
    assert set(map(tuple, after['edges'])) == {tuple(sorted((relabel(a), relabel(b))))
                                              for a, b in graph['edges']}
    assert not after['cross_route_mismatches']
    assert after['target_graph'] == graph['target_graph']
    return normalized, order


def adjacency(m, edges):
    matrix = [[0]*m for _ in range(m)]
    for i, j in edges:
        assert i != j
        matrix[i][j] = matrix[j][i] = 1
    return matrix


def cycle(m):
    return adjacency(m, [(i, (i+1) % m) for i in range(m)])


def cycle_decomposition(matrix, offset=0):
    """List each induced cycle once, using actual full-graph vertex labels."""
    neighbors = [[j for j, value in enumerate(row) if value] for row in matrix]
    assert all(len(row) == 2 for row in neighbors)
    unused, result = set(range(len(matrix))), []
    while unused:
        start = min(unused)
        order = [start]
        previous, current = start, min(neighbors[start])
        while current != start:
            assert current in unused and current not in order
            order.append(current)
            following = next(vertex for vertex in neighbors[current] if vertex != previous)
            previous, current = current, following
        assert len(order) >= 3
        unused.difference_update(order)
        result.append(dict(vertices=[offset+vertex for vertex in order], length=len(order)))
    return result


def semantic_sanity():
    cpu = time.process_time()
    em = Emitter()
    a, b, out = (em.new_var('truth') for _ in range(3))
    helper.add_iff_and(em, out, a, b)
    for av, bv, ov in product((False, True), repeat=3):
        values = {a: av, b: bv, out: ov}
        assert all(any(values[abs(lit)] == (lit > 0) for lit in clause) for clause in em.clauses) == (ov == (av and bv))
    h0 = cycle(4)
    h1 = adjacency(4, [(0, 1), (1, 3), (3, 2), (2, 0)])
    cross = [[int(i == j) for j in range(4)] for i in range(4)]
    model = build(4, 1)
    original, _ = check_explicit(model, 'valid_graph_before_P_normalization', h0, h1, cross)
    assert original['target_graph'] and not original['normalized_target']
    assert original['cross_route_mismatches'] == 8 and not original['bad_pairs']
    records, normalizations = [original], []
    for order in ([0, 1, 2, 3], [2, 0, 3, 1]):
        relabeled = right_relabel(h0, h1, cross, order)
        normalized, restoring = normalize(*relabeled, 1)
        row, _ = check_explicit(model, 'normalized_after_right_order_'+str(order), *normalized)
        assert row['target_graph'] and row['normalized_target'] and not row['false_clauses']
        records.append(row)
        normalizations.append(dict(initial_order=order, restoring_order=restoring,
                                   exact_labeled_edge_isomorphism_checked=True))
    normalized, _ = normalize(h0, h1, cross, 1)
    row, _ = check_explicit(model, 'same_side_covered_cross_routes_fail', h0, h0, cross)
    assert row['bad_pairs'] == 4 and row['same_side_bad_pairs'] == 0 and not row['failed_degrees']
    records.append(row)
    h1_9 = adjacency(9, [(i, (i+2) % 9) for i in range(9)])
    cross9 = [[int((j-i) % 9 in (2, 7)) for j in range(9)] for i in range(9)]
    row, _ = check_explicit(build(9, 2), 'cross_counts_exact_but_same_side_fails', cycle(9), h1_9, cross9)
    assert row['same_side_bad_pairs'] == row['bad_pairs'] == row['false_clauses'] == 27
    assert not row['cross_route_mismatches'] and not row['failed_degrees']
    records.append(row)
    changed_cross = [row[:] for row in normalized[2]]
    changed_cross[0][1] = 0
    row, _ = check_explicit(model, 'cross_degree_failure', normalized[0], normalized[1], changed_cross)
    assert row['failed_degrees'] == [['cross_degree', 0, 0], ['cross_degree', 1, 1]]
    records.append(row)
    changed_h0 = [row[:] for row in normalized[0]]
    changed_h0[0][1] = changed_h0[1][0] = 0
    row, _ = check_explicit(model, 'internal_degree_failure', changed_h0, normalized[1], normalized[2])
    assert row['failed_degrees'] == [['internal_degree', 0, 0], ['internal_degree', 0, 1]]
    records.append(row)
    return dict(status='SMALL_SEMANTICS_PASSED', AND_truth_assignments=8,
                explicit_assignments=len(records), records=records, normalizations=normalizations,
                positive_example=dict(m=4, internal_degree=2, cross_degree=1, cross_excess=1),
                official_m29_model_built=False, solver_calls=0, elapsed_cpu=time.process_time()-cpu)


def prepare(output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    assert not any((output_dir / name).exists() for name in ('input.cnf', 'encoding.json', 'variable_map.json'))
    cpu, wall = time.process_time(), time.monotonic()
    sanity = semantic_sanity()
    model = build(29, 6)
    em = model['emitter']
    assert (em.variable_count, em.clause_count) == EXPECTED_CNF
    cross = [[int((j-i) % 29 in range(6)) for j in range(29)] for i in range(29)]
    source, values = check_explicit(model, 'explicit_two_cycles_and_six_offsets_sanity_only', cycle(29), cycle(29), cross)
    assert not source['failed_degrees'] and not source['normalized_target']
    with (output_dir / 'input.cnf').open('w') as output:
        output.write(f'p cnf {em.variable_count} {em.clause_count}\n')
        for clause in em.clauses:
            output.write(' '.join(map(str, clause)) + ' 0\n')
    checked = support.check_dimacs(output_dir / 'input.cnf', values, em.variable_count, em.clause_count)
    assert len(checked['false_clause_ids']) == source['false_clauses']
    sanity.update(official_m29_model_built=True, explicit_m29_assignment=source,
                  saved_DIMACS_explicit_assignment_check=checked)
    save(output_dir / 'sanity.json', sanity)
    save(output_dir / 'variable_map.json', dict(n=58, side_size=29, internal_degree=2, cross_degree=6,
         H0_variables=model['internal'][0], H1_variables=model['internal'][1], C_variables=model['cross'],
         P_normalized=True, fixed_internal_edges=[], fixed_C_entries=[]))
    record = dict(status='PREPARED_NOT_RUN', scope=SCOPE, n=58, side_size=29,
                  internal_degree=2, cross_degree=6, degree_target=8, expected_edges=232,
                  variables=em.variable_count, clauses=em.clause_count, variable_kinds=em.kind_counts,
                  clause_groups=model['clause_groups'], counter_records=model['counters'],
                  same_side_coverage_records=model['coverage'], primary_variables=1653,
                  P_normalized=True, cycle_types_fixed=False, C_diagonal_fixed=False,
                  extra_symmetry_or_Hamilton_exclusion_clauses=False, solver_calls=0,
                  elapsed_cpu=time.process_time()-cpu, elapsed_wall=time.monotonic()-wall)
    save(output_dir / 'encoding.json', record)
    print(json.dumps({key: record[key] for key in ('status', 'scope', 'variables', 'clauses',
                                                  'elapsed_cpu', 'elapsed_wall')}, indent=2))


def decode(output_dir, model_path=None):
    model_path = model_path or output_dir / 'solver.log'
    record = json.loads((output_dir / 'encoding.json').read_text())
    mapping = json.loads((output_dir / 'variable_map.json').read_text())
    assert record['n'] == mapping['n'] == 58 and mapping['side_size'] == 29
    assert mapping['internal_degree'] == 2 and mapping['cross_degree'] == 6
    assert (record['variables'], record['clauses']) == EXPECTED_CNF
    # Check the deterministic primary numbering without building the model.
    next_var = 0
    for name in ('H0_variables', 'H1_variables'):
        matrix = mapping[name]
        assert len(matrix) == 29 and all(len(row) == 29 for row in matrix)
        assert all(matrix[i][i] == 0 for i in range(29))
        for i, j in combinations(range(29), 2):
            next_var += 1
            assert matrix[i][j] == matrix[j][i] == next_var
    assert mapping['C_variables'] == [[next_var+29*i+j+1 for j in range(29)] for i in range(29)]
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
    checked = support.check_dimacs(output_dir / 'input.cnf', values, record['variables'], record['clauses'])
    assert checked['all_clauses_satisfied'], 'Saved full DIMACS assignment fails clauses'
    h0, h1, cross = ([[int(values[var]) if var else 0 for var in row] for row in mapping[name]]
                     for name in ('H0_variables', 'H1_variables', 'C_variables'))
    graph = graph_check(h0, h1, cross, 6)
    target = graph['normalized_target'] and len(graph['edges']) == 232
    internal_cycles = (dict(H0=cycle_decomposition(h0), H1=cycle_decomposition(h1, 29))
                       if graph['internal_degrees'] == [[2]*29]*2 else None)
    result = dict(status='SAT_JOINT_TWOFACTOR_TARGET_CHECKED' if target else 'SAT_DECODE_VALIDATION_FAILED',
                  scope=SCOPE, n=58, edges=graph['edges'], H0=h0, H1=h1, C=cross,
                  internal_cycles=internal_cycles,
                  P=[[value-1 for value in row] for row in graph['cross_route_counts']],
                  P_is_identity=not graph['cross_route_mismatches'], target_graph=target,
                  verification=graph, all_bad_pairs=graph['bad_pairs'], model_check=checked,
                  source_model=str(model_path), independent_external_verification_performed=False)
    (output_dir / 'candidate.edges').write_text(f"58 {len(graph['edges'])}\n" +
        ''.join(f'{a} {b}\n' for a, b in graph['edges']))
    save(output_dir / 'candidate.json', result)
    print(json.dumps(dict(status=result['status'], n=58, edges=len(graph['edges']),
                         bad_pairs=len(graph['bad_pairs']), target_graph=target), indent=2))
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
