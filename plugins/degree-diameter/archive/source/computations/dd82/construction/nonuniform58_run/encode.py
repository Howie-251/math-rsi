"""A fixed C28 and C30, six free disjoint right chords, and all cross edges.

Only generic CNF primitives and full-assignment checks are reused. No old
model builder, excess-permutation normalization, or fixed chord choice is used.
"""
import argparse
from collections import Counter, deque
import importlib.util
from itertools import combinations, product
import json
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location(
    'nonuniform_generic_checks', HERE.parent / 'joint_boundary_completion_run/encode.py')
support = importlib.util.module_from_spec(spec)
spec.loader.exec_module(support)
helper = support.load_helpers()
EXPECTED_CNF = (73701, 235491)
SCOPE = ('58 vertices partitioned into a fixed induced C28 and a fixed C30 plus '
         'six freely chosen pairwise disjoint noncycle chords. All 840 cross '
         'edges and all 405 possible right chords are variables. Left cross '
         'degree is six; right cross degree plus chord degree is six. All '
         'actual pairs have distance at most two. No J+P normalization, fixed '
         'chord endpoints or pairings, or additional symmetry constraints. '
         'This construction family is not all 58-vertex graphs.')


class Emitter(helper.CNFEmitter):
    def __init__(self):
        super().__init__(None)
        self.clauses = []

    def add_clause(self, *literals):
        self.clauses.append(tuple(literals))
        super().add_clause(*literals)


def save(path, record):
    path.write_text(json.dumps(record, indent=2) + '\n')


def pair(i, j):
    assert i != j
    return (min(i, j), max(i, j))


def cycle_edges(size):
    return {pair(i, (i+1) % size) for i in range(size)}


def build(left_size, right_size, cross_degree, chord_count):
    """The same fixed-cycle/free-edge encoding serves small semantic checks."""
    a, b, d, q = left_size, right_size, cross_degree, chord_count
    assert a >= 3 and b >= 4 and 1 <= d <= min(a, b) and 0 <= q <= b//2
    assert a*d == b*d-2*q
    em = Emitter()
    left_cycle, right_cycle = cycle_edges(a), cycle_edges(b)
    chords = {ij: em.new_var('right_chord')
              for ij in combinations(range(b), 2) if ij not in right_cycle}
    cross = [[em.new_var('cross_edge') for j in range(b)] for i in range(a)]
    free = {(a+i, a+j): var for (i, j), var in chords.items()}
    free.update({(i, a+j): cross[i][j] for i in range(a) for j in range(b)})
    fixed_edges = left_cycle | {(a+i, a+j) for i, j in right_cycle}
    counters, coverage, paths, groups = [], [], [], []

    def edge(i, j):
        ij = pair(i, j)
        return free[ij] if ij in free else ij in fixed_edges

    def mark(name, before):
        groups.append(dict(name=name, first_clause=before+1,
                           last_clause=em.clause_count, clauses=em.clause_count-before))

    def count(inputs, target, relation, kind, **record):
        first = em.clause_count+1
        if relation == 'exact':
            helper.enforce_exact(em, inputs, target, kind+'_threshold')
            units = 0 if not inputs else 1 if target in (0, len(inputs)) else 2
        else:
            assert relation == 'at_most' and target == 1
            thresholds = helper.unary_thresholds(em, inputs, 2, kind+'_threshold')
            units = int(thresholds[1] is not None)
            if units:
                em.add_clause(-thresholds[1])
        counters.append(dict(kind=kind, target=target, relation=relation,
                             first_clause=first, last_clause=em.clause_count,
                             unit_clauses=list(range(em.clause_count-units+1, em.clause_count+1)),
                             **record))

    before = em.clause_count
    for j in range(b):
        count([var for ij, var in chords.items() if j in ij], 1, 'at_most',
              'right_chord_incidence', vertex=j)
    mark('right_chords_form_a_matching', before)
    before = em.clause_count
    count(list(chords.values()), q, 'exact', 'total_chords')
    mark('exact_number_of_right_chords', before)
    before = em.clause_count
    for i in range(a):
        count(cross[i], d, 'exact', 'left_cross_degree', vertex=i)
    mark('left_cross_degrees', before)
    before = em.clause_count
    for j in range(b):
        inputs = [cross[i][j] for i in range(a)] + [var for ij, var in chords.items() if j in ij]
        count(inputs, d, 'exact', 'right_cross_plus_chord_degree', vertex=j)
    mark('right_cross_plus_chord_degrees', before)

    before = em.clause_count
    for i, j in combinations(range(a+b), 2):
        direct = edge(i, j)
        if direct is True:
            coverage.append(dict(pair=[i, j], clause=None, fixed_direct=True))
            continue
        terms, fixed_path = [], None
        for middle in range(a+b):
            if middle in (i, j):
                continue
            first, second = edge(i, middle), edge(middle, j)
            if first is False or second is False:
                continue
            if first is True and second is True:
                fixed_path = middle
                break
            terms.append((middle, first, second))
        if fixed_path is not None:
            coverage.append(dict(pair=[i, j], clause=None, fixed_middle=fixed_path))
            continue
        inputs = [] if direct is False else [direct]
        for middle, first, second in terms:
            if first is True or second is True:
                out = second if first is True else first
                kind = 'fixed_chord' if out <= len(chords) else 'fixed_cross'
            else:
                out = em.new_var('actual_two_free_edge_path')
                helper.add_iff_and(em, out, first, second)
                kinds = sorted('chord' if var <= len(chords) else 'cross' for var in (first, second))
                kind = '_'.join(kinds)
            inputs.append(out)
            paths.append(dict(pair=[i, j], middle=middle, kind=kind, variable=out))
        em.add_clause(*dict.fromkeys(inputs))
        coverage.append(dict(pair=[i, j], clause=em.clause_count))
    mark('all_actual_pair_coverage', before)
    return dict(left_size=a, right_size=b, cross_degree=d, chord_count=q,
                emitter=em, chords=chords, cross=cross, free=free,
                fixed_edges=fixed_edges, counters=counters, coverage=coverage,
                paths=paths, clause_groups=groups)


def graph_check(a, b, d, q, selected_chords, cross):
    """Expand actual edges, then check degrees and all-source BFS."""
    assert len(cross) == a and all(len(row) == b for row in cross)
    assert all(value in (0, 1) for row in cross for value in row)
    selected_chords = set(selected_chords)
    assert all(0 <= i < j < b and (i, j) not in cycle_edges(b) for i, j in selected_chords)
    edges = cycle_edges(a) | {(a+i, a+j) for i, j in cycle_edges(b) | selected_chords}
    edges.update((i, a+j) for i in range(a) for j in range(b) if cross[i][j])
    neighbors = [set() for _ in range(a+b)]
    for i, j in edges:
        neighbors[i].add(j)
        neighbors[j].add(i)
    bad, maximum, connected = [], 0, True
    for source in range(a+b):
        distance = [-1]*(a+b)
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
        bad.extend([source, other] for other in range(source+1, a+b)
                   if distance[other] < 0 or distance[other] > 2)
    chord_degrees = [sum(j in ij for ij in selected_chords) for j in range(b)]
    left_cross = list(map(sum, cross))
    right_cross = [sum(cross[i][j] for i in range(a)) for j in range(b)]
    right_combined = [x+y for x, y in zip(right_cross, chord_degrees)]
    degrees = list(map(len, neighbors))
    exact_degrees = degrees == [d+2]*(a+b)
    in_scope = (len(selected_chords) == q and max(chord_degrees) <= 1
                and left_cross == [d]*a and right_combined == [d]*b)
    return dict(n=a+b, edges=sorted(edges), degrees=degrees, exact_degrees=exact_degrees,
                selected_chords=sorted(selected_chords), chord_degrees=chord_degrees,
                left_cross_degrees=left_cross, right_cross_degrees=right_cross,
                right_combined_degrees=right_combined, connected=connected,
                diameter=maximum if connected else None, bad_pairs=bad,
                in_scope=in_scope, target_graph=exact_degrees and not bad,
                model_target=in_scope and not bad)


def check_explicit(model, name, selected_chords, cross):
    a, b, d, q = (model[key] for key in ('left_size', 'right_size', 'cross_degree', 'chord_count'))
    em = model['emitter']
    graph = graph_check(a, b, d, q, selected_chords, cross)
    values = {var: ij in selected_chords for ij, var in model['chords'].items()}
    values.update({model['cross'][i][j]: bool(cross[i][j]) for i in range(a) for j in range(b)})
    false = {index for index, clause in enumerate(em.clauses, 1)
             if support.evaluate_clause(clause, values, index)}
    assert set(values) == set(range(1, em.variable_count+1))
    assert false == {index for index, clause in enumerate(em.clauses, 1)
                     if not any(values[abs(lit)] == (lit > 0) for lit in clause)}
    permitted, failures = set(), []
    fields = dict(right_chord_incidence='chord_degrees', left_cross_degree='left_cross_degrees',
                  right_cross_plus_chord_degree='right_combined_degrees')
    for row in model['counters']:
        actual = len(selected_chords) if row['kind'] == 'total_chords' else graph[fields[row['kind']]][row['vertex']]
        wrong = actual != row['target'] if row['relation'] == 'exact' else actual > row['target']
        failed = false.intersection(range(row['first_clause'], row['last_clause']+1))
        assert bool(failed) == wrong
        assert failed <= set(row['unit_clauses'])
        permitted.update(row['unit_clauses'])
        if wrong:
            failures.append(dict(kind=row['kind'], vertex=row.get('vertex'), actual=actual, target=row['target']))
    bad = sorted(row['pair'] for row in model['coverage'] if row['clause'] in false)
    assert bad == graph['bad_pairs']
    permitted.update(row['clause'] for row in model['coverage'] if row['clause'] is not None)
    assert false <= permitted
    assert (not false) == graph['model_target']
    active_paths = Counter(row['kind'] for row in model['paths'] if values[row['variable']])
    # Check every emitted mixed or free/free witness directly against its two
    # actual edges, including true witnesses in assignments violating degrees.
    actual_edges = set(map(tuple, graph['edges']))
    for row in model['paths']:
        i, j = row['pair']; k = row['middle']
        assert values[row['variable']] == (pair(i, k) in actual_edges and pair(k, j) in actual_edges)
    return dict(name=name, n=a+b, variables=em.variable_count, clauses=em.clause_count,
                assigned_variables=len(values), false_clauses=len(false), failed_counters=failures,
                exact_degrees=graph['exact_degrees'], in_scope=graph['in_scope'],
                bad_pairs=len(bad), diameter=graph['diameter'], target_graph=graph['target_graph'],
                model_target=graph['model_target'], active_path_types=dict(active_paths),
                complete_clause_semantics_matches_BFS=True), values


def matrix_from_rows(size, rows):
    return [[int(j in row) for j in range(size)] for row in rows]


def semantic_sanity():
    cpu, wall = time.process_time(), time.monotonic()
    em = Emitter()
    first, second, out = (em.new_var('truth') for _ in range(3))
    helper.add_iff_and(em, out, first, second)
    for x, y, z in product((False, True), repeat=3):
        values = {first: x, second: y, out: z}
        assert all(any(values[abs(lit)] == (lit > 0) for lit in clause) for clause in em.clauses) == (z == (x and y))
    model = build(4, 6, 2, 2)
    chords = {(0, 2), (1, 3)}
    cross = matrix_from_rows(6, [(0, 1), (3, 4), (2, 5), (4, 5)])
    records = []
    row, _ = check_explicit(model, 'positive_C4_C6_two_chords', chords, cross)
    assert row['model_target'] and not row['false_clauses']
    assert all(row['active_path_types'].get(kind, 0) for kind in ('fixed_chord', 'chord_cross', 'cross_cross'))
    records.append(row)
    changed = matrix_from_rows(6, [(0, 3), (1, 4), (2, 5), (4, 5)])
    row, _ = check_explicit(model, 'all_degrees_correct_but_coverage_fails', chords, changed)
    assert row['in_scope'] and row['bad_pairs'] and not row['failed_counters']
    records.append(row)
    changed = [row[:] for row in cross]; changed[0][0] = 0
    row, _ = check_explicit(model, 'cross_degree_failure', chords, changed)
    assert {r['kind'] for r in row['failed_counters']} == {'left_cross_degree', 'right_cross_plus_chord_degree'}
    records.append(row)
    row, _ = check_explicit(model, 'chord_number_and_degree_failure', {(0, 2)}, cross)
    assert {r['kind'] for r in row['failed_counters']} == {'total_chords', 'right_cross_plus_chord_degree'}
    records.append(row)
    # Two chords meeting at right vertex 0 violate the matching rule. Their
    # path from 2 to 5 is still a genuine two-free-edge witness and must be
    # represented faithfully before the degree constraints reject the graph.
    model7 = build(5, 7, 2, 2)
    cross7 = matrix_from_rows(7, [(i, (i+1) % 7) for i in range(5)])
    row, _ = check_explicit(model7, 'matching_failure_with_real_chord_chord_path', {(0, 2), (0, 5)}, cross7)
    assert any(r['kind'] == 'right_chord_incidence' and r['vertex'] == 0 for r in row['failed_counters'])
    assert row['active_path_types'].get('chord_chord', 0) > 0
    records.append(row)
    return dict(status='SMALL_SEMANTICS_PASSED', AND_truth_assignments=8,
                explicit_assignments=len(records), records=records,
                official_28_30_model_built=False, solver_calls=0,
                elapsed_cpu=time.process_time()-cpu, elapsed_wall=time.monotonic()-wall)


def prepare(output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    assert not any((output_dir/name).exists() for name in ('input.cnf', 'encoding.json', 'variable_map.json'))
    cpu, wall = time.process_time(), time.monotonic()
    sanity = semantic_sanity()
    model = build(28, 30, 6, 6)
    em = model['emitter']
    assert (em.variable_count, em.clause_count) == EXPECTED_CNF
    assert len(model['chords']) == 405 and len(model['free']) == 1245
    chords = {(4, 28), (5, 29), (0, 6), (1, 7), (2, 8), (3, 9)}
    # The paper design's explicit degree-eight assignment: delete rows28/29
    # of the even-offset circulant, only for sanity, not as a SAT restriction.
    cross = [[int((j-i) % 30 in (0, 2, 4, 6, 8, 10)) for j in range(30)] for i in range(28)]
    source, values = check_explicit(model, 'explicit_degree_eight_sanity_only', chords, cross)
    assert source['in_scope'] and source['exact_degrees'] and not source['model_target']
    with (output_dir/'input.cnf').open('w') as output:
        output.write(f'p cnf {em.variable_count} {em.clause_count}\n')
        for clause in em.clauses:
            output.write(' '.join(map(str, clause))+' 0\n')
    checked = support.check_dimacs(output_dir/'input.cnf', values, em.variable_count, em.clause_count)
    assert len(checked['false_clause_ids']) == source['false_clauses'] == source['bad_pairs']
    sanity.update(official_28_30_model_built=True, explicit_official_assignment=source,
                  saved_DIMACS_explicit_assignment_check=checked)
    save(output_dir/'sanity.json', sanity)
    save(output_dir/'variable_map.json', dict(n=58, left_size=28, right_size=30,
         chord_variables=[dict(pair=list(ij), variable=var) for ij, var in model['chords'].items()],
         cross_variables=model['cross'], fixed_cycle_edges=sorted(model['fixed_edges']),
         cross_degree=6, chord_count=6, fixed_chord_entries=[], P_normalized=False))
    record = dict(status='PREPARED_NOT_RUN', scope=SCOPE, n=58, left_size=28, right_size=30,
                  cross_degree=6, chord_count=6, degree_target=8, expected_edges=232,
                  primary_variables=1245, chord_variables=405, cross_variables=840,
                  variables=em.variable_count, clauses=em.clause_count,
                  variable_kinds=em.kind_counts, clause_groups=model['clause_groups'],
                  counter_records=model['counters'], coverage_records=model['coverage'],
                  P_normalized=False, chord_endpoints_or_pairs_fixed=False,
                  solver_calls=0, elapsed_cpu=time.process_time()-cpu,
                  elapsed_wall=time.monotonic()-wall)
    save(output_dir/'encoding.json', record)
    print(json.dumps({key: record[key] for key in ('status', 'scope', 'variables', 'clauses', 'elapsed_cpu', 'elapsed_wall')}, indent=2))


def decode(output_dir, model_path=None):
    model_path = model_path or output_dir/'solver.log'
    record = json.loads((output_dir/'encoding.json').read_text())
    mapping = json.loads((output_dir/'variable_map.json').read_text())
    assert (record['variables'], record['clauses']) == EXPECTED_CNF
    assert (mapping['n'], mapping['left_size'], mapping['right_size'], mapping['cross_degree'], mapping['chord_count']) == (58, 28, 30, 6, 6)
    possible = [ij for ij in combinations(range(30), 2) if ij not in cycle_edges(30)]
    assert mapping['chord_variables'] == [dict(pair=list(ij), variable=index+1) for index, ij in enumerate(possible)]
    assert mapping['cross_variables'] == [[406+30*i+j for j in range(30)] for i in range(28)]
    assert mapping['fixed_cycle_edges'] == [list(ij) for ij in sorted(cycle_edges(28) | {(28+i, 28+j) for i, j in cycle_edges(30)})]
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
    checked = support.check_dimacs(output_dir/'input.cnf', values, record['variables'], record['clauses'])
    assert checked['all_clauses_satisfied'], 'Saved full DIMACS assignment fails clauses'
    chords = {tuple(row['pair']) for row in mapping['chord_variables'] if values[row['variable']]}
    cross = [[int(values[var]) for var in row] for row in mapping['cross_variables']]
    graph = graph_check(28, 30, 6, 6, chords, cross)
    target = graph['model_target'] and len(graph['edges']) == 232
    result = dict(status='SAT_NONUNIFORM_TARGET_CHECKED' if target else 'SAT_DECODE_VALIDATION_FAILED',
                  scope=SCOPE, n=58, edges=graph['edges'], cross_matrix=cross,
                  right_chords_full_labels=[[28+i, 28+j] for i, j in sorted(chords)],
                  fixed_cycles=[list(range(28)), list(range(28, 58))],
                  target_graph=target, verification=graph, model_check=checked,
                  source_model=str(model_path), independent_external_verification_performed=False)
    save(output_dir/'candidate.json', result)
    (output_dir/'candidate.edges').write_text(f"58 {len(graph['edges'])}\n"+
        ''.join(f'{i} {j}\n' for i, j in graph['edges']))
    print(json.dumps(dict(status=result['status'], n=58, edges=len(graph['edges']), bad_pairs=len(graph['bad_pairs'])), indent=2))
    if not target:
        raise SystemExit(2)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('sanity', 'prepare', 'decode'))
    parser.add_argument('--output-dir', type=Path, default=HERE)
    parser.add_argument('--model', type=Path)
    args = parser.parse_args(argv)
    if args.action == 'prepare':
        prepare(args.output_dir)
    elif args.action == 'decode':
        decode(args.output_dir, args.model)
    else:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        result = semantic_sanity()
        save(args.output_dir/'small_sanity.json', result)
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
