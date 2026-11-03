"""One actual literal degree/near-star profile; no BFS or construction search."""
from collections import Counter
from pathlib import Path
import json
import time

START=time.process_time()
OUT=Path(__file__).resolve().parent
recipe=json.loads((OUT/'construction.author.json').read_text())
n=recipe['order']
assert (n,recipe['degree'],recipe['diameter'])==(2836,5,6)
adj=[set() for _ in range(n)]
edges=set()
duplicates=loops=0
for row in (OUT/'source2836.author.edges.txt').read_text().splitlines():
    if not row.strip() or row.startswith('#'):
        continue
    u,v=sorted(map(int,row.split()))
    assert 0<=u<=v<n
    loops+=u==v
    duplicates+=(u,v) in edges
    edges.add((u,v));adj[u].add(v);adj[v].add(u)
assert loops==duplicates==0 and len(edges)==7090
degrees=list(map(len,adj))
free=[u for u,d in enumerate(degrees) if d<5]
saturated=[sum(degrees[v]==5 for v in row) for row in adj]
types={'base_incidence':0,'base_layer':0,'layer_layer':0}
for u,v in edges:
    types['base_incidence' if v<2730 else 'layer_layer' if u>=2730 else 'base_layer']+=1
assert types=={'base_incidence':6719,'base_layer':212,'layer_layer':159}
layer_type_counts=Counter((sum(v<1365 for v in adj[u]),
                          sum(1365<=v<2730 for v in adj[u]),
                          sum(v>=2730 for v in adj[u])) for u in range(2730,2836))
assert layer_type_counts==Counter({(1,1,3):106})
result={'status':'ACTUAL_2836_SOURCE_FULLY_SATURATED_EDGE_PRESERVING_EXTENSION_EXCLUDED',
        'target_Delta':5,'target_D':6,'savedL':2836,'savedL_date':'2026-10-27',
        'source_n':n,'source_m':len(edges),'simple':True,'loops':loops,'duplicate_edges':duplicates,
        'source_degree_histogram':dict(Counter(degrees)),'source_actual_D':None,
        'source_reported_D':6,'source_D_basis':'Author verification.author.txt reused; not rerun',
        'free_vertices':free,'free_count':len(free),'free_slots':sum(5-d for d in degrees),
        'min_saturated_neighbors':min(saturated),'saturated_neighbor_count_histogram':dict(Counter(saturated)),
        'low_saturated_prototypes':[] if min(saturated)==5 else [u for u,c in enumerate(saturated) if c==min(saturated)],
        'spare_star_prototypes':[u for u,c in enumerate(saturated) if c==0 and adj[u]],
        'author_type_binding':{'points':[0,1364],'lines':[1365,2729],'layer':[2730,2835]},
        'edge_type_counts':types,'layer_vertices_with_one_point_one_line_three_layer_neighbors':106,
        'prediction_disposition':'SUPPORTED_NO_FREE_ACTUAL_VERTICES',
        'exclusion_scope':'Any connected proper enlargement retaining all source edges and maximumdegree5, with any positive number of new vertices; not a general order2837 graph exclusion',
        'proof':'Every old vertex already has degree5, so retaining all old edges forbids every old-to-new edge. Any nonempty newvertex set is disconnected from the old source.',
        'not_excluded':'Source-edge deletion/rewiring, different source, or arbitrary degree5 diameter6 graphs',
        'actual_candidate_n':None,'actual_candidate_D':None,'ordinary_bad_unordered_pairs':None,
        'construction_candidates_evaluated':0,'anchor_searches':0,'BFS_runs':0,
        'running':False,'pending':[],'CPU_seconds':time.process_time()-START,
        'author_primary':'https://github.com/f4t4nt/degree-diameter-graphs/tree/main/graphs/deg5/dia6'}
(OUT/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(OUT/'terminal.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
