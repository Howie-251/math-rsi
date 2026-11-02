"""Exact necessary deletion screen for monotone polarity73 completion.

Prepare/decode/sanity only. This module never invokes a SAT solver.
SAT means a deletion-screen candidate, not a degree-eight target graph.
"""
import argparse
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CASES = {'n58': 58, 'n59': 59}
SCOPE = ('All deletion sets of the saved polarity73 geometry at the specified order; '
         'necessary monotone-completion screen only, no target graph or completion encoded.')


def save(path, obj):
    path.write_text(json.dumps(obj, indent=2) + '\n')


def load_helpers():
    """Definitions only: no historical main, encoder or experiment is run."""
    sys.dont_write_bytecode = True
    path = ROOT / 'computations/dd82/construction/joint_boundary_completion_run/encode.py'
    spec = importlib.util.spec_from_file_location('polarity73_generic_support', path)
    support = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = support
    spec.loader.exec_module(support)
    return support.load_helpers(), support


def geometry():
    meta = json.loads((HERE / 'geometry.json').read_text())
    lines = (HERE / 'geometry.edges').read_text().splitlines()
    n, edge_count = map(int, lines[0].split())
    edges = [tuple(map(int, line.split())) for line in lines[1:] if line.strip()]
    assert n == 73 and len(edges) == edge_count == 324
    assert len(set(edges)) == edge_count and all(0 <= u < v < n for u, v in edges)
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    absolute, outer = set(meta['absolute_vertices']), set(meta['outside_vertices'])
    nucleus = meta['nucleus']
    assert absolute | outer | {nucleus} == set(range(73))
    assert len(absolute) == 9 and len(outer) == 63 and nucleus not in absolute | outer
    assert all(len(adj[x]) == (8 if x in absolute else 9) for x in range(73))
    return dict(adj=adj, edges=edges, absolute=absolute, outer=outer, nucleus=nucleus)


def direct_screen(deleted, n, data=None):
    """Pure Python actual-H predicates; no CNF or solver is consulted."""
    assert n in (58, 59)
    deleted = set(deleted)
    assert deleted <= set(range(73))
    data = data or geometry()
    adj, outer = data['adj'], data['outer']
    survivors = set(range(73)) - deleted
    removed_neighbors = {x: len(adj[x] & deleted) for x in range(73)}
    degrees = {x: len(adj[x] & survivors) for x in survivors}
    saturated = {x for x in survivors if degrees[x] == 8}
    outer_fail = sorted(x for x in survivors & outer if not adj[x] & deleted & outer)
    degree_fail = sorted(x for x in survivors if len(adj[x]) == 9 and not adj[x] & deleted)
    forbidden = [[f, u, v] for f in sorted(deleted)
                 for u, v in combinations(sorted(adj[f] & saturated), 2) if v not in adj[u]]
    groups = dict(exact_deleted_count=len(deleted) == 73 - n,
                  outer_deleted_at_least_eight=len(deleted & outer) >= 8,
                  retained_outer_triangle_hit=not outer_fail,
                  retained_degree9_loses_neighbor=not degree_fail,
                  deleted_center_saturated_pair=not forbidden)
    return dict(passes_screen=all(groups.values()), groups=groups,
                deleted=sorted(deleted), F=sorted(deleted & outer), survivors=sorted(survivors),
                saturated=sorted(saturated), removed_neighbor_counts=removed_neighbors,
                retained_degrees=degrees, deficits={x: 8 - degrees[x] for x in survivors},
                violations=dict(outer_triangle_hit=outer_fail, degree9=degree_fail,
                                deleted_center_saturated_pairs=forbidden))


def build(case, output=None):
    helper, support = load_helpers()
    data = geometry()
    n = CASES[case]

    class Emitter(helper.CNFEmitter):
        def __init__(self):
            super().__init__(output)
            self.clauses = []

        def add_clause(self, *literals):
            assert all(type(lit) is int for lit in literals)
            self.clauses.append(tuple(literals))
            super().add_clause(*literals)

    em = Emitter()
    deleted = {x: em.new_var('deleted_original_vertex') for x in range(73)}
    sat, neighbor_thresholds = {}, {}
    try:
        for x in range(73):
            target = len(data['adj'][x]) - 8
            thresholds = helper.unary_thresholds(
                em, [deleted[y] for y in sorted(data['adj'][x])], target + 1,
                'deleted_neighbor_exact_threshold')
            neighbor_thresholds[x] = list(thresholds)
            conditions = [-deleted[x], -thresholds[target]]
            if target:
                conditions.append(thresholds[target - 1])
            out = em.new_var('retained_saturated_iff')
            sat[x] = out
            # out iff retained AND exactly deg_H(x)-8 deleted neighbors.
            for literal in conditions:
                em.add_clause(-out, literal)
            em.add_clause(out, *(-literal for literal in conditions))
        count = helper.unary_thresholds(em, list(deleted.values()), 74 - n,
                                        'total_deleted_threshold')
        outer_count = helper.unary_thresholds(em, [deleted[x] for x in sorted(data['outer'])],
                                              8, 'outer_deleted_threshold')
        definition_end = em.clause_count
        groups = {}

        def group(name, clauses):
            first = em.clause_count + 1
            for clause in clauses:
                em.add_clause(*clause)
            groups[name] = dict(first_clause=first, last_clause=em.clause_count,
                                clauses=em.clause_count - first + 1)

        d = 73 - n
        group('exact_deleted_count', [(count[d - 1],), (-count[d],)])
        group('outer_deleted_at_least_eight', [(outer_count[7],)])
        group('retained_outer_triangle_hit', [tuple([deleted[x]] + [deleted[y]
              for y in sorted(data['adj'][x] & data['outer'])]) for x in sorted(data['outer'])])
        group('retained_degree9_loses_neighbor', [tuple([deleted[x]] + [deleted[y]
              for y in sorted(data['adj'][x])]) for x in range(73) if len(data['adj'][x]) == 9])
        pair_records = [[f, u, v] for f in range(73)
                        for u, v in combinations(sorted(data['adj'][f]), 2)
                        if v not in data['adj'][u]]
        group('deleted_center_saturated_pair',
              [(-deleted[f], -sat[u], -sat[v]) for f, u, v in pair_records])
        em.finish()
    except BaseException:
        em.abort()
        raise
    return dict(emitter=em, support=support, geometry=data, n=n, deleted=deleted, sat=sat,
                neighbor_thresholds=neighbor_thresholds, definition_end=definition_end,
                groups=groups, pair_records=pair_records)


def semantic_sanity(model, assignments):
    """A few explicit deletion assignments, not a deletion-set search."""
    em, support = model['emitter'], model['support']
    records = []
    for deleted in assignments:
        direct = direct_screen(deleted, model['n'], model['geometry'])
        values = {var: x in deleted for x, var in model['deleted'].items()}
        false_ids = []
        for number, clause in enumerate(em.clauses, 1):
            if support.evaluate_clause(clause, values, number):
                false_ids.append(number)
        assert len(values) == em.variable_count
        assert not any(i <= model['definition_end'] for i in false_ids)
        actual_sat = set(direct['saturated'])
        assert all(values[var] == (x in actual_sat) for x, var in model['sat'].items())
        for name, bounds in model['groups'].items():
            satisfied = not any(bounds['first_clause'] <= i <= bounds['last_clause'] for i in false_ids)
            assert satisfied == direct['groups'][name], (name, sorted(deleted))
        complete_false = [i for i, clause in enumerate(em.clauses, 1)
                          if not any(values[abs(lit)] == (lit > 0) for lit in clause)]
        assert complete_false == false_ids
        records.append(dict(deleted=sorted(deleted), passes_screen=direct['passes_screen'],
                            groups=direct['groups'], false_clauses=len(false_ids)))
    return dict(status='PASSED_EXPLICIT_ASSIGNMENT_SEMANTICS', solver_calls=0,
                assignments=len(records), all73_sat_equivalences_checked=True,
                every_constraint_group_compared=True, records=records)


def explicit_assignments(n):
    samples = json.loads((HERE / 'two_fiber_examples.json').read_text())['samples']
    sample = next(set(row['deletion']) for row in samples if row['n'] == n)
    d = 73 - n
    return [set(), set(range(73)), set(range(d)), set(range(0, 2*d, 2)), sample]


def prepare(case):
    target = HERE / case
    target.mkdir(exist_ok=True)
    assert not any((target / name).exists() for name in ('input.cnf', 'encoding.json', 'variable_map.json'))
    cpu, wall = time.process_time(), time.monotonic()
    model = build(case, target / 'input.cnf')
    em = model['emitter']
    sanity = semantic_sanity(model, explicit_assignments(model['n']))
    save(target / 'sanity.json', sanity)
    save(target / 'variable_map.json', dict(
        deleted={str(x): var for x, var in model['deleted'].items()},
        sat={str(x): var for x, var in model['sat'].items()},
        deleted_neighbor_thresholds=model['neighbor_thresholds'],
        sat_definition='not D[x] AND deleted_H_neighbors[x] == degree_H[x]-8',
        absolute_vertices=sorted(model['geometry']['absolute']),
        outer_vertices=sorted(model['geometry']['outer']), nucleus=model['geometry']['nucleus']))
    record = dict(status='PREPARED_NOT_RUN', target_graph=False, scope=SCOPE,
                  case=case, n=model['n'], ambient_n=73, deleted_target=73-model['n'],
                  variables=em.variable_count, clauses=em.clause_count,
                  variable_kinds=em.kind_counts, primary_deletion_variables=73,
                  sat_variables=73, constraint_groups=model['groups'],
                  defining_clauses=model['definition_end'],
                  saturated_pair_records=model['pair_records'],
                  solver_calls=0, source_geometry=['geometry.edges', 'geometry.json'],
                  necessary_only=True, completion_edge_variables=0,
                  mathematical_dependency='proofs/dd82/construction/POLARITY73_REDUCTION_CANDIDATE.md',
                  aggregate_bound_used=False, elapsed_cpu=time.process_time()-cpu,
                  elapsed_wall=time.monotonic()-wall)
    save(target / 'encoding.json', record)
    print(json.dumps({key: record[key] for key in ('status','case','variables','clauses','elapsed_cpu','elapsed_wall')}, indent=2))


def decode(case, log=None):
    target = HERE / case
    log = log or target / 'solver.log'
    record = json.loads((target / 'encoding.json').read_text())
    mapping = json.loads((target / 'variable_map.json').read_text())
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
    assert saw_sat, 'A terminal SAT assignment is required for decode'
    _, support = load_helpers()
    check = support.check_dimacs(target / 'input.cnf', values, record['variables'], record['clauses'])
    assert check['all_clauses_satisfied'], 'Saved assignment does not satisfy saved input'
    deleted = {int(x) for x, var in mapping['deleted'].items() if values[var]}
    data = geometry()
    direct = direct_screen(deleted, CASES[case], data)
    assert direct['passes_screen']
    assert all(values[var] == (int(x) in direct['saturated']) for x, var in mapping['sat'].items())
    survivors = direct['survivors']
    S = set(survivors)
    edges = [(u, v) for u, v in data['edges'] if u in S and v in S]
    bad = [[u, v] for u, v in combinations(survivors, 2)
           if v not in data['adj'][u] and not (data['adj'][u] & data['adj'][v] & S)]
    added_edges_required = 4 * len(S) - len(edges)
    assert sum(direct['deficits'].values()) == 2 * added_edges_required
    result = dict(status='SAT_DELETION_SCREEN_CANDIDATE_ONLY', target_graph=False,
                  monotone_completion_found=False, **direct,
                  retained_H_edges_original_labels=edges, all_bad_pairs_original_labels=bad,
                  bad_pair_count=len(bad), edge_deficit=added_edges_required,
                  retained_edge_count=len(edges), compact_to_original=survivors,
                  source_solver_log=str(log), model_check=check)
    save(target / 'deletion_candidate.json', result)
    compact = {x: i for i, x in enumerate(survivors)}
    (target / 'retained_H.edges').write_text(f'{len(S)} {len(edges)}\n' +
        ''.join(f'{compact[u]} {compact[v]}\n' for u, v in edges))
    print(json.dumps(dict(status=result['status'], target_graph=False, case=case,
                         deleted=sorted(deleted), bad_pairs=len(bad), edge_deficit=added_edges_required), indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'decode', 'sanity'))
    parser.add_argument('--n', type=int, choices=(58, 59), required=True)
    parser.add_argument('--log', type=Path)
    args = parser.parse_args()
    case = f'n{args.n}'
    if args.action == 'prepare':
        prepare(case)
    elif args.action == 'decode':
        decode(case, args.log)
    else:
        model = build(case)
        print(json.dumps(semantic_sanity(model, explicit_assignments(model['n'])), indent=2))
