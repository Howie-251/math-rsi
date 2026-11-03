from pathlib import Path
from collections import Counter
import json, time

P = Path(__file__).resolve().parent
B = P.parent.parent / 'breadth_20261027_wave3' / 'hexagon_partial_fold_scout'
t = time.process_time()
q = json.loads((B / 'Q_data.json').read_text())
Q, HQ, absolute = q['Q'], q['H3_generic_neighbors'], q['H3_absolute']

def check(path):
    state = list(map(int, path.read_text().split()))
    assert len(state) == 33033 and set(state) <= {0, 1, 2}
    S = sum(x != 0 for x in state)
    generic = []
    bad = []
    squared = 0
    for u, st in enumerate(state):
        load = sum(state[v] != 0 if st == 0 else state[v] == st for v in Q[u])
        degree = 10 + load
        generic.extend([degree] * (1 if st == 0 else 2))
        squared += (1 if st == 0 else 2) * max(0, degree - 12) ** 2
        if degree > 12:
            bad.append({'fiber': u, 'state': st, 'degree_each_point': degree})
    h3 = [7 - int(absolute[h]) + sum(state[u] != 0 for u in HQ[h]) for h in range(364)]
    degrees = generic + h3
    assert len(degrees) == 33397 + S
    legal = max(degrees) <= 12
    return dict(state_file=path.name, split_fibers=S, core_order=len(degrees),
                legal_maxdegree12=legal, maximum_degree=max(degrees),
                degree_histogram=dict(sorted(Counter(degrees).items())),
                H3_degree_histogram=dict(sorted(Counter(h3).items())),
                generic_violating_fibers=len(bad), actual_violating_vertices=sum(d > 12 for d in degrees),
                weighted_squared_excess=squared,
                degree_excess_units=sum(max(0, d - 12) for d in degrees),
                violation_examples=bad[:12],
                exceeds_saved_42342=legal and len(degrees) > 42342,
                copies_fixed_zero=True, padding_twins=0, full_graph_generated=False)

results = [check(path) for path in sorted(P.glob('*.states'))]
logs = [json.loads(line) for line in (P / 'search_log.jsonl').read_text().splitlines()]
byname = {r['state_file']: r for r in results}
for row in logs:
    k = row['start']
    legal = byname[f'start{k}_best_legal.states']
    final = byname[f'start{k}_final.states']
    near = byname[f'start{k}_anneal_end.states']
    assert legal['legal_maxdegree12'] and legal['split_fibers'] == row['best_legal_S']
    assert final['split_fibers'] == row['final_S'] and final['weighted_squared_excess'] == row['final_weighted_squared_excess']
    assert near['split_fibers'] == row['anneal_end_S'] and near['weighted_squared_excess'] == row['anneal_end_weighted_squared_excess']
out = dict(status='EXACT_LOCAL_DEGREE_CHECK_COMPLETE',
           scope='recomputed from Q adjacency and final ternary states, independent of search caches',
           states=results, verifier_CPU_seconds=time.process_time() - t,
           original_tau_incidence_reconstruction=False, full_BFS_performed=False,
           geometry_diameter_scope='D<=5 conditional on the original H9/tau data and cited partial-fold theorem')
(P / 'degree_check.json').write_text(json.dumps(out, indent=2) + '\n')
best = max((r for r in results if r['legal_maxdegree12']), key=lambda r:r['core_order'])
print(json.dumps(dict(best_legal=best, verifier_CPU_seconds=out['verifier_CPU_seconds']), indent=2))
