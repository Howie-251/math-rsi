"""Joint completion of a deletable cyclic cross source and two free factors.

All left factor edges and both right layers F and M are free. Every actual
path uses these same edges and R = F OR M. Only generic helpers are inherited.
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
    'free_factors_cyclic_generic_checks', HERE.parent/'joint_boundary_completion_run/encode.py')
support = importlib.util.module_from_spec(spec)
spec.loader.exec_module(support)
helper = support.load_helpers()
OFFICIAL_OFFSETS = (0, 3, 6, 10, 14, 19)
SCOPE = ('All378 left edges are free and form an induced simple2factor; '
         'old cross column j<28 allows only i-j mod28 in '
         '{0,3,6,10,14,19}, with all168 allowed bits deletable; both new '
         'columns are free. All435 F edges and435 M edges are free. F is a '
         'simple2factor, M a disjoint six-edge matching, and actual right '
         'adjacency is F union M. Cross rows have degree6; each cross column '
         'degree plus M degree is6. All1653 actual pairs must have distance '
         'at most2. New supports may overlap. The accepted fixed-source '
         '5+5 and5+6 exclusion proofs give redundant new-column degree6 cuts. '
         'No fixed left or right cycle type or order, endpoints, P normalization, or '
         'finished-graph symmetry. This is not all58vertex graphs.')


class Emitter(helper.CNFEmitter):
    def __init__(self):
        super().__init__(None)
        self.clauses = []

    def add_clause(self, *literals):
        self.clauses.append(tuple(literals))
        super().add_clause(*literals)


def save(path, record):
    path.write_text(json.dumps(record, indent=2)+'\n')


def pair(i, j):
    assert i != j
    return (min(i, j), max(i, j))


def cycle_edges(order):
    return {pair(order[i], order[(i+1) % len(order)]) for i in range(len(order))}


def allowed_cross(a, offsets, i, j):
    return j >= a or (i-j) % a in offsets


def add_iff_or(em, out, first, second):
    em.add_clause(-first, out)
    em.add_clause(-second, out)
    em.add_clause(first, second, -out)


def build(left_size, offsets):
    """Same source-mask, two-layer and all-pair encoder for small/official use."""
    a, offsets = left_size, tuple(offsets)
    b, d = a+2, len(offsets)
    assert a >= 3 and len(set(offsets)) == d and all(0 <= x < a for x in offsets)
    assert 1 <= d <= min(a, b//2)
    em = Emitter()
    left = {ij: em.new_var('left_factor_edge') for ij in combinations(range(a), 2)}
    right_pairs = list(combinations(range(b), 2))
    factor = {ij: em.new_var('right_factor_edge') for ij in right_pairs}
    matching = {ij: em.new_var('right_matching_edge') for ij in right_pairs}
    cross = [[em.new_var('old_cross_edge' if j < a else 'new_cross_edge')
              if allowed_cross(a, offsets, i, j) else None
              for j in range(b)] for i in range(a)]
    primary_count = em.variable_count
    right = {ij: em.new_var('actual_right_union') for ij in right_pairs}
    free = dict(left)
    free.update({(a+i, a+j): var for (i, j), var in right.items()})
    free.update({(i, a+j): cross[i][j] for i in range(a) for j in range(b)
                 if cross[i][j] is not None})
    counters, overlaps, coverage, paths, groups = [], [], [], [], []

    def edge(i, j):
        ij = pair(i, j)
        return free[ij] if ij in free else False

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
    for ij in right_pairs:
        add_iff_or(em, right[ij], factor[ij], matching[ij])
        em.add_clause(-factor[ij], -matching[ij])
        overlaps.append(dict(pair=list(ij), clause=em.clause_count))
    mark('actual_right_union_and_layer_disjointness', before)
    before = em.clause_count
    for i in range(a):
        count([var for ij, var in left.items() if i in ij], 2, 'exact',
              'left_factor_degree', vertex=i)
    mark('left_factor_degrees', before)
    before = em.clause_count
    for j in range(b):
        count([var for ij, var in factor.items() if j in ij], 2, 'exact',
              'right_factor_degree', vertex=j)
    mark('right_factor_degrees', before)
    before = em.clause_count
    for j in range(b):
        count([var for ij, var in matching.items() if j in ij], 1, 'at_most',
              'right_matching_degree', vertex=j)
    count(list(matching.values()), d, 'exact', 'total_matching_edges')
    mark('right_matching_and_redundant_total', before)
    before = em.clause_count
    for i in range(a):
        count([var for var in cross[i] if var is not None], d, 'exact',
              'left_cross_degree', vertex=i)
    mark('left_cross_degrees', before)
    before = em.clause_count
    for j in range(b):
        inputs = [cross[i][j] for i in range(a) if cross[i][j] is not None]
        inputs += [var for ij, var in matching.items() if j in ij]
        count(inputs, d, 'exact', 'right_cross_plus_matching_degree', vertex=j)
    mark('right_cross_plus_matching_degrees', before)

    # These paper lemmas apply only to this exact source, not to the small models.
    if a == 28 and offsets == OFFICIAL_OFFSETS:
        before = em.clause_count
        for j in (28, 29):
            count([cross[i][j] for i in range(a)], 6, 'exact',
                  'right_new_cross_degree', vertex=j)
        mark('proved_new_column_degree_six', before)

    before = em.clause_count
    for i, j in combinations(range(a+b), 2):
        direct = edge(i, j)
        if direct is True:
            coverage.append(dict(pair=[i, j], clause=None, fixed_direct=True))
            continue
        terms, fixed_middle = [], None
        for k in range(a+b):
            if k in (i, j):
                continue
            first, second = edge(i, k), edge(k, j)
            if first is False or second is False:
                continue
            if first is True and second is True:
                fixed_middle = k
                break
            terms.append((k, first, second))
        if fixed_middle is not None:
            coverage.append(dict(pair=[i, j], clause=None, fixed_middle=fixed_middle))
            continue
        inputs = [] if direct is False else [direct]
        for k, first, second in terms:
            if first is True or second is True:
                out = second if first is True else first
            else:
                out = em.new_var('actual_two_edge_path')
                helper.add_iff_and(em, out, first, second)
            inputs.append(out)
            paths.append(dict(pair=[i, j], middle=k, variable=out))
        em.add_clause(*dict.fromkeys(inputs))
        coverage.append(dict(pair=[i, j], clause=em.clause_count))
    mark('all_actual_pair_coverage', before)
    assert len(coverage) == (a+b)*(a+b-1)//2
    return dict(left_size=a, right_size=b, offsets=offsets, cross_degree=d,
                matching_count=d, emitter=em, left=left, factor=factor, matching=matching,
                right=right, cross=cross,
                primary_variables=primary_count, counters=counters, overlaps=overlaps,
                coverage=coverage, paths=paths, clause_groups=groups)


def graph_check(a, offsets, selected_left, selected_factor, selected_matching, cross):
    """Expand F union M as a set, then check actual degrees and all-source BFS."""
    b, d = a+2, len(offsets)
    left, factor, matching = set(selected_left), set(selected_factor), set(selected_matching)
    assert all(0 <= i < j < a for i, j in left)
    assert all(0 <= i < j < b for i, j in factor | matching)
    assert len(cross) == a and all(len(row) == b for row in cross)
    assert all(value in (0, 1) for row in cross for value in row)
    edges = left | {(a+i, a+j) for i, j in factor | matching}
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
    left_degree = [sum(i in ij for ij in left) for i in range(a)]
    factor_degree = [sum(j in ij for ij in factor) for j in range(b)]
    matching_degree = [sum(j in ij for ij in matching) for j in range(b)]
    left_cross = list(map(sum, cross))
    right_cross = [sum(cross[i][j] for i in range(a)) for j in range(b)]
    combined = [x+y for x, y in zip(right_cross, matching_degree)]
    unsupported = [[i, j] for i in range(a) for j in range(b)
                   if cross[i][j] and not allowed_cross(a, offsets, i, j)]
    degrees = list(map(len, neighbors))
    exact_degrees = degrees == [d+2]*(a+b)
    in_scope = (not unsupported and left_degree == [2]*a and not factor.intersection(matching)
                and factor_degree == [2]*b and max(matching_degree) <= 1
                and len(matching) == d and left_cross == [d]*a and combined == [d]*b)
    return dict(n=a+b, edges=sorted(edges), degrees=degrees, exact_degrees=exact_degrees,
                left_factor_degrees=left_degree, factor_degrees=factor_degree, matching_degrees=matching_degree,
                factor_matching_overlap=sorted(factor & matching), unsupported_cross=unsupported,
                left_cross_degrees=left_cross, right_cross_degrees=right_cross,
                right_combined_degrees=combined, connected=connected,
                diameter=maximum if connected else None, bad_pairs=bad,
                in_scope=in_scope, target_graph=exact_degrees and not bad,
                model_target=in_scope and not bad)


def cycle_decomposition(size, selected_factor, label_offset=0):
    neighbors = [set() for _ in range(size)]
    for i, j in selected_factor:
        neighbors[i].add(j); neighbors[j].add(i)
    assert all(len(row) == 2 for row in neighbors)
    unseen, result = set(range(size)), []
    while unseen:
        start, previous, current, order = min(unseen), None, min(unseen), []
        while current != start or not order:
            order.append(current); unseen.remove(current)
            following = min(neighbors[current] - ({previous} if previous is not None else set()))
            previous, current = current, following
        result.append(dict(vertices=[label_offset+x for x in order], length=len(order)))
    return result


def write_dimacs(path, model):
    em = model['emitter']
    with path.open('w') as output:
        output.write(f'p cnf {em.variable_count} {em.clause_count}\n')
        for clause in em.clauses:
            output.write(' '.join(map(str, clause))+' 0\n')


def check_explicit(model, name, selected_left, selected_factor, selected_matching, cross):
    a, b, d = (model[key] for key in ('left_size', 'right_size', 'cross_degree'))
    left, factor, matching = set(selected_left), set(selected_factor), set(selected_matching)
    graph = graph_check(a, model['offsets'], left, factor, matching, cross)
    assert not graph['unsupported_cross'], 'Fixed nonedges are not primary assignment choices'
    em = model['emitter']
    values = {var: ij in left for ij, var in model['left'].items()}
    values.update({var: ij in factor for ij, var in model['factor'].items()})
    values.update({var: ij in matching for ij, var in model['matching'].items()})
    values.update({var: bool(cross[i][j]) for i, row in enumerate(model['cross'])
                   for j, var in enumerate(row) if var is not None})
    false = {index for index, clause in enumerate(em.clauses, 1)
             if support.evaluate_clause(clause, values, index)}
    assert set(values) == set(range(1, em.variable_count+1))
    assert false == {index for index, clause in enumerate(em.clauses, 1)
                     if not any(values[abs(lit)] == (lit > 0) for lit in clause)}
    for ij, var in model['right'].items():
        assert values[var] == (ij in factor | matching)
    permitted, failures = set(), []
    fields = dict(left_factor_degree='left_factor_degrees',
                  right_factor_degree='factor_degrees', right_matching_degree='matching_degrees',
                  left_cross_degree='left_cross_degrees',
                  right_new_cross_degree='right_cross_degrees',
                  right_cross_plus_matching_degree='right_combined_degrees')
    for row in model['counters']:
        actual = len(matching) if row['kind'] == 'total_matching_edges' else graph[fields[row['kind']]][row['vertex']]
        wrong = actual != row['target'] if row['relation'] == 'exact' else actual > row['target']
        failed = false.intersection(range(row['first_clause'], row['last_clause']+1))
        assert bool(failed) == wrong
        assert failed <= set(row['unit_clauses'])
        permitted.update(row['unit_clauses'])
        if wrong:
            failures.append(dict(kind=row['kind'], vertex=row.get('vertex'), actual=actual, target=row['target']))
    failed_overlaps = []
    for row in model['overlaps']:
        wrong = tuple(row['pair']) in factor & matching
        assert (row['clause'] in false) == wrong
        permitted.add(row['clause'])
        if wrong:
            failed_overlaps.append(row['pair'])
    bad = sorted(row['pair'] for row in model['coverage'] if row['clause'] in false)
    assert bad == graph['bad_pairs']
    permitted.update(row['clause'] for row in model['coverage'] if row['clause'] is not None)
    assert false <= permitted
    assert (not false) == graph['model_target']
    actual_edges, active_paths = set(map(tuple, graph['edges'])), Counter()

    def edge_kind(i, j):
        if i < a and j < a:
            return 'L'
        if min(i, j) < a:
            return 'C'
        ij = pair(i-a, j-a)
        return 'FM' if ij in factor & matching else 'F' if ij in factor else 'M'

    for row in model['paths']:
        i, j = row['pair']; k = row['middle']
        real = pair(i, k) in actual_edges and pair(k, j) in actual_edges
        assert values[row['variable']] == real
        if real:
            active_paths['_'.join(sorted((edge_kind(i, k), edge_kind(k, j))))] += 1
    record = dict(name=name, left_size=a, right_size=b, offsets=model['offsets'],
                  left_factor_edges=sorted(left), factor_edges=sorted(factor),
                  matching_edges=sorted(matching), cross_matrix=cross,
                  actual_edges=graph['edges'], variables=em.variable_count, clauses=em.clause_count,
                  assigned_variables=len(values), false_clauses=len(false), false_clause_ids=sorted(false),
                  failed_counters=failures, failed_layer_disjointness=failed_overlaps,
                  exact_degrees=graph['exact_degrees'], in_scope=graph['in_scope'],
                  bad_pairs=bad, diameter=graph['diameter'], target_graph=graph['target_graph'],
                  model_target=graph['model_target'], active_path_types=dict(active_paths),
                  actual_union_checked=True, complete_clause_semantics_matches_BFS=True)
    return record, values


def matrix_from_rows(size, rows):
    return [[int(j in row) for j in range(size)] for row in rows]


def semantic_sanity(output_dir):
    cpu, wall = time.process_time(), time.monotonic()
    for operation in ('AND', 'OR'):
        em = Emitter()
        first, second, out = (em.new_var('truth') for _ in range(3))
        (helper.add_iff_and if operation == 'AND' else add_iff_or)(em, out, first, second)
        for x, y, z in product((False, True), repeat=3):
            values = {first: x, second: y, out: z}
            actual = all(any(values[abs(lit)] == (lit > 0) for lit in clause) for clause in em.clauses)
            assert actual == (z == ((x and y) if operation == 'AND' else (x or y)))
    model = build(4, (0, 1))
    write_dimacs(output_dir/'small_4_6.cnf', model)
    assert sum(var is not None for row in model['cross'] for var in row) == 16
    cross = matrix_from_rows(6, [(0, 3), (1, 4), (2, 5), (4, 5)])
    left_cycle = cycle_edges([0, 1, 2, 3])
    triangles = cycle_edges([0, 3, 5]) | cycle_edges([1, 2, 4])
    six_cycle = cycle_edges([0, 3, 2, 1, 4, 5])
    matching = {(0, 2), (1, 3)}
    records, assignments = [], []

    def case(name, factor, match, matrix, left=left_cycle, current=model, filename='small_4_6.cnf'):
        row, values = check_explicit(current, name, left, factor, match, matrix)
        checked = support.check_dimacs(output_dir/filename, values, row['variables'], row['clauses'])
        assert checked['false_clause_ids'] == row['false_clause_ids']
        row.update(saved_cnf=filename, saved_DIMACS_assignment_checked=True)
        records.append(row)
        assignments.append(dict(name=name, cnf=filename,
                                values=[v if values[v] else -v for v in range(1, len(values)+1)]))
        return row

    row = case('positive_two_right_triangles_overlapping_new_supports', triangles, matching, cross)
    assert row['model_target'] and row['active_path_types'].get('F_M', 0)
    assert len(cycle_decomposition(6, triangles)) == 2
    noncanonical = cycle_edges([0, 1, 3, 2])
    assert noncanonical != left_cycle
    row = case('positive_noncanonical_left_cycle', triangles, matching, cross, left=noncanonical)
    assert row['model_target']
    row = case('positive_single_right_six_cycle', six_cycle, matching, cross)
    assert row['model_target']
    perm = {0: 0, 1: 1, 2: 5, 3: 3, 4: 4, 5: 2}
    relabeled = [[cross[i][perm[j]] for j in range(6)] for i in range(4)]
    row = case('positive_new_column_degrees_one_and_two',
               {pair(perm[i], perm[j]) for i, j in triangles},
               {pair(perm[i], perm[j]) for i, j in matching}, relabeled)
    assert row['model_target'] and [sum(relabeled[i][j] for i in range(4)) for j in (4, 5)] == [2, 1]
    changed = matrix_from_rows(6, [(0, 4), (1, 4), (2, 5), (3, 5)])
    row = case('all_structural_degrees_correct_but_coverage_fails', triangles, matching, changed)
    assert row['in_scope'] and row['exact_degrees'] and row['bad_pairs'] and not row['failed_counters']
    assert [8, 9] in row['bad_pairs']
    changed = [r[:] for r in cross]; changed[0][0] = 0
    row = case('cross_row_and_column_degree_failure', triangles, matching, changed)
    assert {r['kind'] for r in row['failed_counters']} == {'left_cross_degree', 'right_cross_plus_matching_degree'}
    row = case('factor_degree_failure', triangles-{(0, 3)}, matching, cross)
    assert {r['kind'] for r in row['failed_counters']} == {'right_factor_degree'}
    row = case('left_factor_degree_failure', triangles, matching, cross, left=left_cycle-{(0, 1)})
    assert {r['kind'] for r in row['failed_counters']} == {'left_factor_degree'}
    row = case('matching_count_failure', triangles, {(0, 2)}, cross)
    assert {r['kind'] for r in row['failed_counters']} == {'total_matching_edges', 'right_cross_plus_matching_degree'}
    row = case('matching_degree_failure_with_real_two_matching_path', triangles, {(0, 2), (0, 4)}, cross)
    assert any(r['kind'] == 'right_matching_degree' and r['vertex'] == 0 for r in row['failed_counters'])
    assert row['active_path_types'].get('M_M', 0)
    row = case('factor_matching_overlap_still_uses_union', triangles, {(0, 3), (1, 2)}, cross)
    assert row['failed_layer_disjointness'] == [[0, 3], [1, 2]] and not row['failed_counters']
    model6 = build(6, (0, 1))
    write_dimacs(output_dir/'small_6_8.cnf', model6)
    cross6 = matrix_from_rows(8, [(5, 6), (0, 6), (1, 7), (2, 7), (3, 4), (4, 5)])
    left_triangles = cycle_edges([0, 1, 2]) | cycle_edges([3, 4, 5])
    row = case('disconnected_left_factor_all_degrees_correct_coverage_failure',
               cycle_edges(list(range(8))), {(0, 2), (1, 3)}, cross6,
               left=left_triangles, current=model6, filename='small_6_8.cnf')
    assert row['in_scope'] and row['exact_degrees'] and not row['failed_counters']
    assert [2, 3] not in row['bad_pairs'] and [0, 3] in row['bad_pairs']
    assert len(cycle_decomposition(6, left_triangles)) == 2
    assert row['active_path_types'].get('C_C', 0) and not row['model_target']
    save(output_dir/'small_assignments.json', assignments)
    record = dict(status='SMALL_SEMANTICS_PASSED', AND_truth_assignments=8, OR_truth_assignments=8,
                  explicit_assignments=len(records), records=records,
                  official_28_30_model_built=False, solver_calls=0,
                  elapsed_cpu=time.process_time()-cpu, elapsed_wall=time.monotonic()-wall)
    save(output_dir/'small_sanity.json', record)
    return record


def official_fixture():
    """The paper MATH_SCOPE object, only a preset semantic check, never a search."""
    left = cycle_edges([0, 8, 4, 7, 11, 15, 20, 27, 5, 9, 13, 18, 12, 3,
                        16, 17, 6, 21, 22, 10, 23, 24, 14, 25, 26, 19, 1, 2])
    factor = cycle_edges(list(range(27))+[28, 29, 27])
    matching = {(2, 7), (3, 8), (4, 9), (5, 10), (6, 28), (11, 29)}
    cross = [[int((i-j) % 28 in OFFICIAL_OFFSETS) for j in range(28)]+[0, 0]
             for i in range(28)]
    for i in range(2, 12):
        cross[i][i] = 0
        cross[i][28 if i <= 6 else 29] = 1
    return left, factor, matching, cross


def official_six_six_fixture():
    """A deterministic degree-valid semantic fixture, still not a target graph."""
    left, factor, matching, cross = official_fixture()
    for i, j in ((12, 28), (13, 29)):
        cross[i][i] = 0
        cross[i][j] = 1
    matching.difference_update({(6, 28), (11, 29)})
    matching.update({(6, 12), (11, 13)})
    return left, factor, matching, cross


def prepare(output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    assert not any((output_dir/name).exists() for name in ('input.cnf', 'encoding.json', 'variable_map.json'))
    cpu, wall = time.process_time(), time.monotonic()
    small = json.loads((output_dir/'small_sanity.json').read_text())
    assert small['status'] == 'SMALL_SEMANTICS_PASSED' and not small['official_28_30_model_built']
    model = build(28, OFFICIAL_OFFSETS)
    em = model['emitter']
    assert model['primary_variables'] == 1472 and len(model['left']) == 378
    assert len(model['factor']) == len(model['matching']) == len(model['right']) == 435
    assert em.kind_counts['old_cross_edge'] == 168 and em.kind_counts['new_cross_edge'] == 56
    assert len(model['coverage']) == 1653
    old_source, _ = check_explicit(model, 'MATH_SCOPE_five_five_cut_negative', *official_fixture())
    assert old_source['in_scope'] and old_source['exact_degrees']
    assert old_source['failed_counters'] == [
        dict(kind='right_new_cross_degree', vertex=j, actual=5, target=6) for j in (28, 29)]
    assert old_source['false_clauses'] == len(old_source['bad_pairs'])+2
    source, values = check_explicit(model, 'six_six_degree_valid_preset_not_candidate',
                                    *official_six_six_fixture())
    assert source['in_scope'] and source['exact_degrees'] and not source['model_target']
    assert not source['failed_counters'] and not source['failed_layer_disjointness']
    assert [0, 27] in source['bad_pairs']
    assert all([i, 28] not in source['bad_pairs'] for i in range(28))
    write_dimacs(output_dir/'input.cnf', model)
    checked = support.check_dimacs(output_dir/'input.cnf', values, em.variable_count, em.clause_count)
    assert checked['false_clause_ids'] == source['false_clause_ids']
    assert len(checked['false_clause_ids']) == len(source['bad_pairs'])
    support.write_assignment(output_dir/'preset.assignment.txt', values)
    save(output_dir/'sanity.json', dict(status='OFFICIAL_PRESET_SEMANTICS_PASSED',
         small_sanity='small_sanity.json', preset_source='PROVED_CUT_DELTA.md',
         official_28_30_model_built=True, explicit_official_assignment=source,
         original_five_five_cut_negative=old_source,
         saved_DIMACS_explicit_assignment_check=checked, preset_is_search_candidate=False,
         solver_calls=0))
    save(output_dir/'variable_map.json', dict(n=58, left_size=28, right_size=30,
         offsets=OFFICIAL_OFFSETS, cross_degree=6, matching_count=6,
         left_factor_variables=[dict(pair=list(ij), variable=var) for ij, var in model['left'].items()],
         factor_variables=[dict(pair=list(ij), variable=var) for ij, var in model['factor'].items()],
         matching_variables=[dict(pair=list(ij), variable=var) for ij, var in model['matching'].items()],
         actual_right_variables=[dict(pair=list(ij), variable=var) for ij, var in model['right'].items()],
         cross_variables=model['cross']))
    record = dict(status='PREPARED_NOT_RUN', scope=SCOPE, n=58, left_size=28, right_size=30,
                  offsets=OFFICIAL_OFFSETS, cross_degree=6, matching_count=6,
                  degree_target=8, expected_edges=232, primary_variables=1472,
                  left_factor_variables=378,
                  factor_variables=435, matching_variables=435, old_cross_variables=168,
                  new_cross_variables=56, actual_right_union_variables=435,
                  variables=em.variable_count, clauses=em.clause_count,
                  variable_kinds=em.kind_counts, clause_groups=model['clause_groups'],
                  counter_records=model['counters'], coverage_records=model['coverage'],
                  layer_disjointness_records=model['overlaps'], all_pair_count=1653,
                  fixed_left_cycle_type=False, fixed_right_cycle_type=False,
                  fixed_left_circle_order=False, new_supports_forced_disjoint=False,
                  proved_new_cross_degrees=[6, 6],
                  cut_proofs=['ROW_CHANGE_GEOMETRY.md', 'DELETION_56_FEASIBILITY.md'],
                  P_normalized=False, solver_calls=0,
                  elapsed_cpu=time.process_time()-cpu, elapsed_wall=time.monotonic()-wall)
    save(output_dir/'encoding.json', record)
    print(json.dumps({key: record[key] for key in ('status', 'variables', 'clauses', 'elapsed_cpu', 'elapsed_wall')}, indent=2))


def decode(output_dir, model_path=None):
    model_path = model_path or output_dir/'solver.log'
    record = json.loads((output_dir/'encoding.json').read_text())
    mapping = json.loads((output_dir/'variable_map.json').read_text())
    assert (mapping['n'], mapping['left_size'], mapping['right_size'], mapping['cross_degree'], mapping['matching_count']) == (58, 28, 30, 6, 6)
    assert mapping['offsets'] == list(OFFICIAL_OFFSETS)
    assert mapping['left_factor_variables'] == [dict(pair=list(ij), variable=k+1)
                                               for k, ij in enumerate(combinations(range(28), 2))]
    right_pairs = list(combinations(range(30), 2))
    assert mapping['factor_variables'] == [dict(pair=list(ij), variable=k+379) for k, ij in enumerate(right_pairs)]
    assert mapping['matching_variables'] == [dict(pair=list(ij), variable=k+814) for k, ij in enumerate(right_pairs)]
    expected_cross, next_var = [], 1249
    for i in range(28):
        row = []
        for j in range(30):
            if allowed_cross(28, OFFICIAL_OFFSETS, i, j):
                row.append(next_var); next_var += 1
            else:
                row.append(None)
        expected_cross.append(row)
    assert next_var == 1473 and mapping['cross_variables'] == expected_cross
    assert mapping['actual_right_variables'] == [dict(pair=list(ij), variable=k+1473) for k, ij in enumerate(right_pairs)]
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
    save(output_dir/'model_check.json', checked)
    assert checked['all_clauses_satisfied'], 'Saved complete DIMACS model fails clauses'
    left = {tuple(row['pair']) for row in mapping['left_factor_variables'] if values[row['variable']]}
    factor = {tuple(row['pair']) for row in mapping['factor_variables'] if values[row['variable']]}
    matching = {tuple(row['pair']) for row in mapping['matching_variables'] if values[row['variable']]}
    for row in mapping['actual_right_variables']:
        assert values[row['variable']] == (tuple(row['pair']) in factor | matching)
    cross = [[0 if var is None else int(values[var]) for var in row] for row in mapping['cross_variables']]
    graph = graph_check(28, OFFICIAL_OFFSETS, left, factor, matching, cross)
    target = graph['model_target'] and len(graph['edges']) == 232
    result = dict(status='SAT_FREE_FACTORS_CYCLIC_TARGET_CHECKED' if target else 'SAT_DECODE_VALIDATION_FAILED',
                  scope=SCOPE, n=58, edges=graph['edges'], cross_matrix=cross,
                  right_factor_edges_full_labels=[[28+i, 28+j] for i, j in sorted(factor)],
                  right_matching_edges_full_labels=[[28+i, 28+j] for i, j in sorted(matching)],
                  left_factor_edges=sorted(left), left_factor_cycles=cycle_decomposition(28, left),
                  right_factor_cycles=cycle_decomposition(30, factor, 28),
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
    args.output_dir.mkdir(parents=True, exist_ok=True)
    if args.action == 'prepare':
        prepare(args.output_dir)
    elif args.action == 'decode':
        decode(args.output_dir, args.model)
    else:
        result = semantic_sanity(args.output_dir)
        print(json.dumps({key: result[key] for key in ('status', 'explicit_assignments', 'elapsed_cpu', 'elapsed_wall')}, indent=2))


if __name__ == '__main__':
    main()
