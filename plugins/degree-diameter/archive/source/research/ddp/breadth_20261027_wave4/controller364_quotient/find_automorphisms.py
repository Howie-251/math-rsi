from pathlib import Path
import json, signal, time
import networkx as nx

P = Path(__file__).resolve().parent
B = P.parent.parent / 'breadth_20261027_wave3'
Q = json.loads((B / 'hexagon_partial_fold_scout/Q_data.json').read_text())
adj = Q['H3_graph']
G = nx.Graph()
G.add_nodes_from(range(364))
G.add_edges_from((u, v) for u, row in enumerate(adj) for v in row if u < v)
assert G.number_of_edges() == 714
E = {tuple(sorted(e)) for e in G.edges()}

class BudgetFinished(Exception):
    pass
def alarm(*_):
    raise BudgetFinished
signal.signal(signal.SIGPROF, alarm)
t = time.process_time()
signal.setitimer(signal.ITIMER_PROF, 20)
found = []
tasks = []
current = None
def record(mapping, source):
    p = [mapping[i] for i in range(364)]
    assert sorted(p) == list(range(364))
    assert {tuple(sorted((p[u], p[v]))) for u, v in E} == E
    if any(p[i] != i for i in range(364)) and p not in [x['permutation'] for x in found]:
        found.append(dict(source=source, permutation=p))
try:
    current = 'first_two_unrooted_automorphisms'
    matcher = nx.algorithms.isomorphism.GraphMatcher(G, G)
    for j, mapping in enumerate(matcher.isomorphisms_iter()):
        record(mapping, current)
        if j == 1:
            break
    tasks.append(current)
    for source, anchors in [('root0_to1', [(0, 1)]),
                            ('root0_fixed_neighbor_exchange', [(0, 0), (adj[0][0], adj[0][1])])]:
        current = source
        A, Bgraph = G.copy(), G.copy()
        nx.set_node_attributes(A, 0, 'anchor')
        nx.set_node_attributes(Bgraph, 0, 'anchor')
        for color, (u, v) in enumerate(anchors, 1):
            A.nodes[u]['anchor'] = color
            Bgraph.nodes[v]['anchor'] = color
        matcher = nx.algorithms.isomorphism.GraphMatcher(A, Bgraph,
                    node_match=lambda a,b: a['anchor'] == b['anchor'])
        mapping = next(matcher.isomorphisms_iter(), None)
        if mapping is not None:
            record(mapping, current)
        tasks.append(current)
    status = 'FIXED_VF2_TASKS_COMPLETE'
except BudgetFinished:
    status = 'AUTOMORPHISM_PHASE_CPU_LIMIT'
finally:
    signal.setitimer(signal.ITIMER_PROF, 0)
out = dict(status=status, input='Q_data.json H3_graph', vertices=364, edges=714,
           engine='installed networkx GraphMatcher VF2',
           CPU_limit_seconds=20, CPU_seconds=time.process_time()-t,
           completed_fixed_tasks=tasks, stopped_task=current,
           verified_nonidentity_automorphisms=found,
           full_automorphism_group_enumerated=False,
           full_group_order_known=False)
(P / 'automorphisms.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps({k:v for k,v in out.items() if k != 'verified_nonidentity_automorphisms'}, indent=2))
print('nonidentity_maps', len(found))
