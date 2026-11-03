"""Complete variable-deletion polarity73 monotone construction CNF.

Prepare and decode only; no solver. All deletion sets and all new edges
remain free. Old edges are implicit K[x] AND K[y]; degrees and every real
surviving pair use this same adjacency. No necessary-screen CNF is added.
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
spec = importlib.util.spec_from_file_location('complete_variable_baseline', HERE.parent / 'screen.py')
baseline = importlib.util.module_from_spec(spec)
spec.loader.exec_module(baseline)
save = baseline.save
SCOPE = ('All polarity73 monotone completions at the specified retained order: '
         'all deletion sets and all new edges are variable; all surviving old '
         'edges remain. Exact degree eight and actual diameter at most two. '
         'This is the ambient monotone family, not arbitrary graphs of this order.')
EXPECTED = {58: (173093, 558930), 59: (173035, 558699)}


def pair(x, y):
    assert x != y
    return (x, y) if x < y else (y, x)


def adjacency(size, edges):
    adj = [set() for _ in range(size)]
    for x, y in edges:
        assert 0 <= x < y < size
        adj[x].add(y)
        adj[y].add(x)
    return adj


def inspect_graph(size, old, kept, added, target_n, degree_target):
    """Independent full BFS on the explicit retained graph, no CNF paths."""
    kept, added = set(kept), set(added)
    endpoint_fail = sorted(xy for xy in added if not set(xy) <= kept)
    edges = {xy for xy in old | added if set(xy) <= kept}
    adj = adjacency(size, edges)
    bad = []
    for x in sorted(kept):
        distances = {x: 0}
        queue = deque([x])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if v not in distances:
                    distances[v] = distances[u] + 1
                    queue.append(v)
        bad.extend([x, y] for y in sorted(kept) if y > x and
                   (y not in distances or distances[y] > 2))
    degrees = {x: len(adj[x]) for x in sorted(kept)}
    checks = dict(retained_count=len(kept) == target_n,
                  new_edge_endpoints_retained=not endpoint_fail,
                  retained_exact_degree=all(d == degree_target for d in degrees.values()),
                  deleted_degree_zero=not endpoint_fail,
                  all_pairs_distance_at_most_two=not bad)
    return dict(valid=all(checks.values()), checks=checks, retained_count=len(kept),
                edges=len(edges), degrees_original_labels=degrees,
                bad_pairs_original_labels=bad, invalid_added_edges=endpoint_fail), edges


def build(size, old, target_n, degree_target=8):
    """Also accepts tiny unique-common-neighbor backgrounds for sanity."""
    assert 0 < target_n < size and 0 < degree_target < size - 1
    helper, support = baseline.load_helpers()

    class Emitter(helper.CNFEmitter):
        def __init__(self):
            super().__init__(None)
            self.clauses = []

        def add_clause(self, *literals):
            assert all(type(lit) is int for lit in literals)
            self.clauses.append(tuple(literals))
            super().add_clause(*literals)

    em, old = Emitter(), set(old)
    adj = adjacency(size, old)
    keep = {x: em.new_var('retained_vertex') for x in range(size)}
    new = {xy: em.new_var('actual_new_edge') for xy in combinations(range(size), 2)
           if xy not in old}
    groups = {}

    def mark(name, before):
        groups[name] = dict(first_clause=before + 1, last_clause=em.clause_count)

    before = em.clause_count
    helper.enforce_exact(em, [-keep[x] for x in range(size)], size-target_n,
                         'exact_deleted_count')
    mark('retained_count', before)
    before = em.clause_count
    for (x, y), var in new.items():
        em.add_clause(-var, keep[x])
        em.add_clause(-var, keep[y])
    mark('new_edge_endpoints_retained', before)
    degree_records = []
    for x in range(size):
        before = em.clause_count
        inputs = [keep[y] if y in adj[x] else new[pair(x, y)]
                  for y in range(size) if y != x]
        thresholds = helper.unary_thresholds(em, inputs, degree_target+1,
                                             'retained_degree_threshold')
        # Both bounds are conditional: the deleted vertex's counter still
        # sees its retained old neighbors, although its actual degree is 0.
        em.add_clause(-keep[x], thresholds[degree_target-1])
        em.add_clause(-keep[x], -thresholds[degree_target])
        degree_records.append(dict(vertex=x, first_clause=before+1,
                                   last_clause=em.clause_count))
    coverage, mixed_terms, double_terms = [], 0, 0
    universe = set(range(size))
    for (x, y), direct in new.items():
        common = adj[x] & adj[y]
        assert len(common) == 1, ('ambient nonedge needs one old witness', x, y)
        middle = next(iter(common))
        literals = [-keep[x], -keep[y], keep[middle], direct]
        for z in sorted(adj[x] - common):
            literals.append(new[pair(y, z)])
            mixed_terms += 1
        for z in sorted(adj[y] - common):
            literals.append(new[pair(x, z)])
            mixed_terms += 1
        for z in sorted(universe - {x, y} - adj[x] - adj[y]):
            out = em.new_var('actual_two_new_edge_path')
            helper.add_iff_and(em, out, new[pair(x, z)], new[pair(y, z)])
            literals.append(out)
            double_terms += 1
        assert len(literals) == size + 1
        em.add_clause(*literals)
        coverage.append(dict(pair=[x, y], old_common_neighbor=middle,
                             clause=em.clause_count))
    return dict(size=size, old=old, target_n=target_n, degree_target=degree_target,
                emitter=em, support=support, keep=keep, new=new, groups=groups,
                degrees=degree_records, coverage=coverage,
                mixed_path_literals=mixed_terms, two_new_path_variables=double_terms)


def check_assignment(model, label, kept, added):
    """Extend a complete K/X assignment through every auxiliary definition."""
    kept, added = set(kept), set(added)
    assert kept <= model['keep'].keys() and added <= model['new'].keys()
    em, support = model['emitter'], model['support']
    values = {var: x in kept for x, var in model['keep'].items()}
    values.update({var: xy in added for xy, var in model['new'].items()})
    false_ids = {i for i, clause in enumerate(em.clauses, 1)
                 if support.evaluate_clause(clause, values, i)}
    assert len(values) == em.variable_count
    assert false_ids == {i for i, clause in enumerate(em.clauses, 1)
                         if not any(values[abs(lit)] == (lit > 0) for lit in clause)}
    graph, _ = inspect_graph(model['size'], model['old'], kept, added,
                             model['target_n'], model['degree_target'])

    def satisfied(row):
        return not any(row['first_clause'] <= i <= row['last_clause'] for i in false_ids)

    for name, row in model['groups'].items():
        assert satisfied(row) == graph['checks'][name], (label, name)
    # Mixed-path simplification is valid under the new-edge endpoint guards.
    # Deliberate false-endpoint assignments check those guards and rejection;
    # valid-endpoint assignments additionally compare every degree and pair.
    valid_endpoints = graph['checks']['new_edge_endpoints_retained']
    if valid_endpoints:
        for row in model['degrees']:
            x = row['vertex']
            expected = x not in kept or graph['degrees_original_labels'][x] == model['degree_target']
            assert satisfied(row) == expected, (label, 'degree', x)
        bad = set(map(tuple, graph['bad_pairs_original_labels']))
        for row in model['coverage']:
            assert (row['clause'] not in false_ids) == (tuple(row['pair']) not in bad)
    assert (not false_ids) == graph['valid']
    return dict(label=label, kept=len(kept), added_edges=len(added),
                valid_graph=graph['valid'], checks=graph['checks'],
                bad_pairs=len(graph['bad_pairs_original_labels']),
                clauses_checked=em.clause_count, false_clauses=len(false_ids),
                all_degree_and_pair_constraints_compared_to_graph=valid_endpoints)


def tiny_sanity():
    star = {(0, x) for x in range(1, 5)}
    windmill = star | {(1, 2), (3, 4)}
    wm = build(5, windmill, 4, degree_target=2)
    rows = [check_assignment(wm, 'delete_center_close_C4_required_mixed_paths',
                             {1, 2, 3, 4}, {(1, 3), (2, 4)}),
            check_assignment(wm, 'same_kept_missing_new_edges', {1, 2, 3, 4}, set()),
            check_assignment(wm, 'new_edge_deleted_endpoint', {0, 1, 2, 3}, {(1, 4)})]
    sm = build(5, star, 4, degree_target=2)
    leaves_cycle = {(1, 2), (2, 3), (3, 4), (1, 4)}
    rows.append(check_assignment(sm, 'deleted_center_counter4_target2_two_new_paths',
                                 {1, 2, 3, 4}, leaves_cycle))
    assert [row['valid_graph'] for row in rows] == [True, False, False, True]
    return rows


def semantic_sanity(model):
    size, n = model['size'], model['target_n']
    kept = set(range(size-n, size))
    rows = tiny_sanity()
    rows += [check_assignment(model, 'ambient_all_kept_no_new', set(range(size)), set()),
             check_assignment(model, 'all_deleted_no_new', set(), set()),
             check_assignment(model, 'explicit_last_n_kept_no_new', kept, set()),
             check_assignment(model, 'explicit_last_n_kept_complete_graph', kept,
                              {xy for xy in model['new'] if set(xy) <= kept})]
    return dict(status='PASSED_EXPLICIT_K_AND_FULL_ADJACENCY_SEMANTICS',
                solver_calls=0, records=rows)


def prepare(n):
    target = HERE / f'n{n}'
    assert not any((target / name).exists() for name in ('input.cnf', 'encoding.json', 'variable_map.json'))
    cpu, wall = time.process_time(), time.monotonic()
    data = baseline.geometry()
    model = build(73, set(data['edges']), n)
    em = model['emitter']
    assert (em.variable_count, em.clause_count) == EXPECTED[n]
    assert model['mixed_path_literals'] == 36288 and model['two_new_path_variables'] == 124992
    sanity = semantic_sanity(model)
    target.mkdir(exist_ok=True)
    with (target / 'input.cnf').open('w') as output:
        output.write(f'p cnf {em.variable_count} {em.clause_count}\n')
        for clause in em.clauses:
            output.write(' '.join(map(str, clause)) + ' 0\n')
    save(target / 'variable_map.json', dict(keep=model['keep'],
         new_edges=[dict(edge=xy, variable=var) for xy, var in model['new'].items()]))
    save(target / 'sanity.json', sanity)
    record = dict(status='PREPARED_NOT_RUN', scope=SCOPE, n=n, ambient_n=73,
                  degree_target=8, variables=em.variable_count, clauses=em.clause_count,
                  variable_kinds=em.kind_counts, groups=model['groups'],
                  degree_records=model['degrees'], coverage_records=model['coverage'],
                  mixed_path_literals=model['mixed_path_literals'],
                  two_new_path_variables=model['two_new_path_variables'],
                  old_edge_variables_eliminated=True, both_degree_bounds_guarded=True,
                  screen_constraints_added=False, fixed_deletion_set=False,
                  screen_choices_fixed=False, solver_calls=0,
                  elapsed_cpu=time.process_time()-cpu, elapsed_wall=time.monotonic()-wall)
    save(target / 'encoding.json', record)
    print(json.dumps({key: record[key] for key in ('status', 'n', 'variables', 'clauses',
                                                  'elapsed_cpu', 'elapsed_wall')}, indent=2))


def decode(n, log=None):
    target = HERE / f'n{n}'
    log = log or target / 'solver.log'
    record = json.loads((target / 'encoding.json').read_text())
    mapping = json.loads((target / 'variable_map.json').read_text())
    assert record['n'] == n and record['ambient_n'] == 73 and record['degree_target'] == 8
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
    clause_check = support.check_dimacs(target / 'input.cnf', values, record['variables'], record['clauses'])
    keep_vars = {int(x): var for x, var in mapping['keep'].items()}
    new_vars = {tuple(row['edge']): row['variable'] for row in mapping['new_edges']}
    old = set(baseline.geometry()['edges'])
    assert set(keep_vars) == set(range(73))
    assert set(new_vars) == set(combinations(range(73), 2)) - old
    assert len(new_vars) == len(mapping['new_edges'])
    primary = list(keep_vars.values()) + list(new_vars.values())
    assert len(primary) == len(set(primary))
    kept = {x for x, var in keep_vars.items() if values[var]}
    added = {xy for xy, var in new_vars.items() if values[var]}
    verification, edges = inspect_graph(73, old, kept, added, n, 8)
    labels = sorted(kept)
    compact = {x: i for i, x in enumerate(labels)}
    compact_edges = sorted(pair(compact[x], compact[y]) for x, y in edges)
    (target / 'candidate.edges').write_text(f'{len(labels)} {len(compact_edges)}\n' +
        ''.join(f'{x} {y}\n' for x, y in compact_edges))
    target_graph = clause_check['all_clauses_satisfied'] and verification['valid']
    result = dict(status='SAT_COMPLETE_VARIABLE_TARGET_CHECKED' if target_graph else
                  'SAT_DECODE_VALIDATION_FAILED', scope=SCOPE, requested_n=n,
                  n=len(labels), edges=compact_edges,
                  target_graph=target_graph, compact_to_original=labels,
                  deleted=sorted(set(range(73))-kept),
                  added_edges_original_labels=sorted(added),
                  explicit_compact_edge_file='candidate.edges',
                  all_bad_pairs_compact=[[compact[x], compact[y]]
                      for x, y in verification['bad_pairs_original_labels']],
                  verification=verification, model_check=clause_check,
                  source_solver_log=str(log))
    save(target / 'candidate.json', result)
    print(json.dumps(dict(status=result['status'], retained=len(kept), edges=len(edges),
                         bad_pairs=len(result['all_bad_pairs_compact']),
                         target_graph=target_graph), indent=2))
    if not target_graph:
        raise SystemExit(2)


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
