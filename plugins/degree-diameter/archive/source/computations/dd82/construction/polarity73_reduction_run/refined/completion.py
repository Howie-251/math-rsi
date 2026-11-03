"""Exact fixed-deletion monotone completion; prepare/decode only, no solver.

Only the saved deleted labels are imported from the refined screen. All
arbitrary screen neighbor choices are released. Every allowed new edge is
one actual undirected adjacency shared by degree and distance constraints.
"""
import argparse
from collections import deque
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('polarity_completion_baseline', HERE.parent / 'screen.py')
baseline = importlib.util.module_from_spec(spec)
spec.loader.exec_module(baseline)
save = baseline.save
SCOPE = ('All monotone degree-eight diameter-two completions of the saved deletion '
         'set; all surviving old edges retained, all other eligible edges free. '
         'No arbitrary refined-screen neighbor choices are fixed.')


def pair(x, y):
    assert x != y
    return (x, y) if x < y else (y, x)


def surviving_graph(n, deleted):
    assert len(deleted) == len(set(deleted)) == 73 - n
    assert all(type(x) is int and 0 <= x < 73 for x in deleted)
    labels = sorted(set(range(73)) - set(deleted))
    compact = {x: i for i, x in enumerate(labels)}
    data = baseline.geometry()
    old = {pair(compact[x], compact[y]) for x, y in data['edges']
           if x in compact and y in compact}
    return labels, old


def graph_check(n, edges, degree_target):
    """Direct graph semantics: full BFS, independently of CNF path records."""
    assert all(0 <= x < y < n for x, y in edges)
    adj = [set() for _ in range(n)]
    for x, y in edges:
        adj[x].add(y)
        adj[y].add(x)
    bad, distances = [], {}
    for source in range(n):
        distance = {source: 0}
        queue = deque([source])
        while queue:
            x = queue.popleft()
            for y in adj[x] - distance.keys():
                distance[y] = distance[x] + 1
                queue.append(y)
        for y in range(source + 1, n):
            d = distance.get(y)
            distances[source, y] = d
            if d is None or d > 2:
                bad.append([source, y])
    degrees = list(map(len, adj))
    summary = dict(n=n, edges=len(edges), degrees=degrees,
                   exact_degrees=all(d == degree_target for d in degrees),
                   diameter_at_most_two=not bad, bad_pairs=bad,
                   valid=all(d == degree_target for d in degrees) and not bad)
    return summary, distances


def build(n, old, degree_target=8):
    helper, support = baseline.load_helpers()

    class Emitter(helper.CNFEmitter):
        def __init__(self):
            super().__init__(None)
            self.clauses = []

        def add_clause(self, *literals):
            assert all(type(lit) is int for lit in literals)
            self.clauses.append(tuple(literals))
            super().add_clause(*literals)

    em = Emitter()
    adj = [set() for _ in range(n)]
    for x, y in old:
        assert 0 <= x < y < n
        adj[x].add(y)
        adj[y].add(x)
    deficits = [degree_target - len(row) for row in adj]
    free = {xy: em.new_var('actual_added_edge') for xy in combinations(range(n), 2)
            if xy not in old and all(deficits[x] > 0 for x in xy)}

    def edge(x, y):
        xy = pair(x, y)
        return True if xy in old else free.get(xy, False)

    degree_records, coverage_records = [], []
    for x in range(n):
        variables = [var for xy, var in free.items() if x in xy]
        first = em.clause_count + 1
        helper.enforce_exact(em, variables, deficits[x], 'exact_added_degree')
        degree_records.append(dict(vertex=x, deficit=deficits[x],
                                   first_clause=first, last_clause=em.clause_count))
    for x, y in combinations(range(n), 2):
        if (x, y) in old or adj[x] & adj[y]:
            coverage_records.append(dict(pair=[x, y], clause=None))
            continue
        direct = edge(x, y)
        literals = [] if direct is False else [direct]
        for z in range(n):
            if z in (x, y):
                continue
            left, right = edge(x, z), edge(z, y)
            if left is False or right is False:
                continue
            if left is True:
                assert right is not True
                literals.append(right)
            elif right is True:
                literals.append(left)
            else:
                out = em.new_var('actual_two_new_edge_path')
                helper.add_iff_and(em, out, left, right)
                literals.append(out)
        em.add_clause(*dict.fromkeys(literals))
        coverage_records.append(dict(pair=[x, y], clause=em.clause_count))
    return dict(n=n, old=old, degree_target=degree_target, emitter=em,
                free=free, deficits=deficits, degrees=degree_records,
                coverage=coverage_records, support=support)


def check_explicit_assignment(model, label, added):
    """Evaluate every clause from explicit full adjacency, without SAT."""
    assert set(added) <= model['free'].keys()
    em, support = model['emitter'], model['support']
    values = {var: xy in added for xy, var in model['free'].items()}
    false_ids = {i for i, clause in enumerate(em.clauses, 1)
                 if support.evaluate_clause(clause, values, i)}
    assert set(values) == set(range(1, em.variable_count + 1))
    assert false_ids == {i for i, clause in enumerate(em.clauses, 1)
                         if not any(values[abs(lit)] == (lit > 0) for lit in clause)}
    graph, distances = graph_check(model['n'], model['old'] | set(added), model['degree_target'])
    for row in model['degrees']:
        satisfied = not any(row['first_clause'] <= i <= row['last_clause'] for i in false_ids)
        assert satisfied == (graph['degrees'][row['vertex']] == model['degree_target'])
    constraints = {row['clause'] for row in model['coverage'] if row['clause'] is not None}
    constraints.update(i for row in model['degrees']
                       for i in range(row['first_clause'], row['last_clause'] + 1))
    assert false_ids <= constraints
    for row in model['coverage']:
        distance = distances[tuple(row['pair'])]
        covered = distance is not None and distance <= 2
        assert (row['clause'] not in false_ids) == covered
    assert (not false_ids) == graph['valid']
    return dict(label=label, added_edges=len(added), false_clauses=len(false_ids),
                exact_degrees=graph['exact_degrees'], bad_pairs=len(graph['bad_pairs']),
                valid_graph=graph['valid'], variables_checked=len(values),
                clauses_checked=em.clause_count)


def semantic_sanity(model):
    cycle = {pair(x, (x + 1) % 5) for x in range(5)}
    tiny = build(5, {(0, 1)}, degree_target=2)
    rows = [check_explicit_assignment(tiny, 'C5_valid_new_old_and_new_new_paths', cycle - {(0, 1)}),
            check_explicit_assignment(tiny, 'single_old_edge_invalid', set()),
            check_explicit_assignment(tiny, 'complete_graph_wrong_degree', set(tiny['free']))]
    saturated = build(6, {(0, 1), (0, 2), (1, 2), (3, 4), (3, 5), (4, 5)}, degree_target=2)
    rows.append(check_explicit_assignment(saturated, 'two_triangles_degree_valid_distance_invalid', set()))
    assert rows[0]['valid_graph'] and not any(row['valid_graph'] for row in rows[1:])
    assert rows[-1]['exact_degrees'] and rows[-1]['bad_pairs'] == 9
    rows += [check_explicit_assignment(model, 'saved_H_no_added_edges', set()),
             check_explicit_assignment(model, 'saved_H_all_eligible_edges', set(model['free']))]
    return dict(status='PASSED_EXPLICIT_FULL_ADJACENCY_SEMANTICS', solver_calls=0,
                all_clauses_checked=True, degree_and_BFS_semantics_compared=True, records=rows)


def prepare(n):
    source = HERE / f'n{n}' / 'deletion_candidate.json'
    deleted = json.loads(source.read_text())['deleted']
    labels, old = surviving_graph(n, deleted)
    target = HERE / f'completion_n{n}'
    assert not any((target / name).exists() for name in ('input.cnf', 'encoding.json', 'variable_map.json'))
    cpu, wall = time.process_time(), time.monotonic()
    model = build(n, old)
    sanity = semantic_sanity(model)
    em = model['emitter']
    target.mkdir(exist_ok=True)
    with (target / 'input.cnf').open('w') as output:
        output.write(f'p cnf {em.variable_count} {em.clause_count}\n')
        for clause in em.clauses:
            output.write(' '.join(map(str, clause)) + ' 0\n')
    save(target / 'variable_map.json', dict(deleted=sorted(deleted), compact_to_original=labels,
         old_edges_compact=sorted(old), added_edge_variables=[dict(edge=xy, variable=var)
                                                             for xy, var in model['free'].items()]))
    save(target / 'sanity.json', sanity)
    record = dict(status='PREPARED_NOT_RUN', scope=SCOPE, n=n, degree_target=8,
                  deletion_source=str(source), deleted=sorted(deleted), screen_choices_fixed=False,
                  variables=em.variable_count, clauses=em.clause_count,
                  variable_kinds=em.kind_counts, added_edge_variables=len(model['free']),
                  retained_edges=len(old), deficits=model['deficits'],
                  bad_pairs=sum(row['clause'] is not None for row in model['coverage']),
                  degree_records=model['degrees'], coverage_records=model['coverage'],
                  solver_calls=0, elapsed_cpu=time.process_time()-cpu,
                  elapsed_wall=time.monotonic()-wall)
    save(target / 'encoding.json', record)
    print(json.dumps({key: record[key] for key in ('status', 'n', 'variables', 'clauses',
                                                  'bad_pairs', 'elapsed_cpu', 'elapsed_wall')}, indent=2))


def decode(n, log=None):
    target = HERE / f'completion_n{n}'
    log = log or target / 'solver.log'
    record = json.loads((target / 'encoding.json').read_text())
    mapping = json.loads((target / 'variable_map.json').read_text())
    assert record['n'] == n and record['degree_target'] == 8
    assert record['deleted'] == mapping['deleted'] and not record['screen_choices_fixed']
    values, saw_sat = {}, False
    for line in log.read_text().splitlines():
        if line.strip() == 's SATISFIABLE':
            saw_sat = True
        if line.startswith('v '):
            for literal in map(int, line.split()[1:]):
                if literal:
                    var, value = abs(literal), literal > 0
                    assert var not in values or values[var] == value
                    values[var] = value
    assert saw_sat, 'A terminal SAT model is required'
    _, support = baseline.load_helpers()
    clauses = support.check_dimacs(target / 'input.cnf', values, record['variables'], record['clauses'])
    assert clauses['all_clauses_satisfied']
    labels, old = surviving_graph(n, mapping['deleted'])
    assert labels == mapping['compact_to_original']
    assert old == set(map(tuple, mapping['old_edges_compact']))
    free = {tuple(row['edge']): row['variable'] for row in mapping['added_edge_variables']}
    deficits = [8 - sum(x in xy for xy in old) for x in range(n)]
    expected = {xy for xy in combinations(range(n), 2)
                if xy not in old and all(deficits[x] > 0 for x in xy)}
    assert set(free) == expected and len(free) == len(mapping['added_edge_variables'])
    assert len(set(free.values())) == len(free)
    added = {xy for xy, var in free.items() if values[var]}
    edges = old | added
    verification, _ = graph_check(n, edges, 8)
    assert verification['valid'] and len(edges) == 4*n
    (target / 'candidate.edges').write_text(f'{n} {len(edges)}\n' +
        ''.join(f'{x} {y}\n' for x, y in sorted(edges)))
    result = dict(status='SAT_COMPLETION_CHECKED', scope=SCOPE, n=n, target_graph=True,
                  monotone_completion_found=True, screen_choices_fixed=False,
                  deleted=mapping['deleted'], compact_to_original=labels,
                  retained_old_edges=len(old), added_edges=len(added),
                  added_edges_original_labels=[[labels[x], labels[y]] for x, y in sorted(added)],
                  explicit_compact_edge_file='candidate.edges', model_check=clauses,
                  verification=verification, source_solver_log=str(log))
    save(target / 'candidate.json', result)
    print(json.dumps(dict(status=result['status'], n=n, edges=len(edges),
                         added_edges=len(added), target_graph=True), indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'decode'))
    parser.add_argument('--n', type=int, choices=(58, 59), required=True)
    parser.add_argument('--log', type=Path)
    args = parser.parse_args()
    if args.action == 'prepare':
        prepare(args.n)
    else:
        decode(args.n, args.log)
