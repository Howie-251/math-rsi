#!/usr/bin/env python3
"""One fixed released7531 graph, using immutable ORIGINAL7242 source pins."""
import collections
import json
from pathlib import Path
import resource
import time

OUT=Path(__file__).resolve().parent
SRC=OUT.parent
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
START=time.process_time()

def write(name,value):
    (OUT/name).write_text(json.dumps(value,indent=2)+'\n')

assert not (OUT/'graph_d26_D3_n7531.edges').exists(), 'one candidate, no overwrite'
release=json.loads((OUT/'ROOT_GRAPH_RELEASE.json').read_text())
assert release['full_fixed_graph_execution_authorized'] is True
precheck=json.loads((OUT/'PRECHECK_RESULT.json').read_text())
assert precheck['status']=='PASS_FIXED_OVOID_PRODUCT_PACKING_AWAIT_ROOT_GRAPH_RELEASE'
ordered=json.loads((OUT/'ORDERED_CENTERS.json').read_text())['centers']
assert len(ordered)==289
# Materialize the immutable snapshot before constructing any current adjacency.
immutable_rows=[{'index':row['index'],'center':row['old_center_label'],
                 'point':row['point'],'spread_index':row['spread_index'],
                 'spread_line':row['spread_line'],
                 'original_source_pins':row['source_full_neighborhood_ordered']}
                for row in ordered]
write('IMMUTABLE_SOURCE_PINS.json',{
    'source_edge_table':'../graph_d25_D3_n7242.edges',
    'source_n':7242,'source_m':90525,
    'pin_semantics':'ORIGINAL full source25neighborhood; never current(center)',
    'order':'precheckedascendingovoidpointIDouter, frozen spread indexinner',
    'rows':immutable_rows})
# All future pins come only from this serialized snapshot, stored as tuples.
immutable=json.loads((OUT/'IMMUTABLE_SOURCE_PINS.json').read_text())['rows']
PINS=tuple(tuple(row['original_source_pins']) for row in immutable)
CENTERS=tuple(row['center'] for row in immutable)
assert len(PINS)==289 and all(len(p)==len(set(p))==25 for p in PINS)

with (SRC/'graph_d25_D3_n7242.edges').open() as stream:
    n,m=map(int,next(stream).split())
    assert (n,m)==(7242,90525)
    adj=[set() for _ in range(n)]
    source_edges=set()
    for text in stream:
        a,b=map(int,text.split())
        assert a<b and (a,b) not in source_edges
        source_edges.add((a,b))
        adj[a].add(b)
        adj[b].add(a)
assert len(source_edges)==90525 and all(len(nbs)==25 for nbs in adj)
assert all(set(pins)==adj[center] for center,pins in zip(CENTERS,PINS))
load=collections.Counter(v for pins in PINS for v in pins)
assert len(load)==7225 and set(load.values())=={1}
# One bounded source-induced diagnostic; adjacency of centers is permitted.
center_set=set(CENTERS)
center_edges=sorted((a,b) for a in CENTERS for b in (adj[a]&center_set) if a<b)
center_degree={a:len(adj[a]&center_set) for a in CENTERS}
assert len(center_edges)==136
assert collections.Counter(center_degree.values())=={1:272,0:17}
write('CENTERS_INDUCED_CHECK.json',{
    'status':'PASS136DISJOINT_EDGES_PLUS17ISOLATES',
    'source':'../graph_d25_D3_n7242.edges','center_count':289,
    'edge_count':136,'edges':center_edges,
    'degree_histogram':{'0':17,'1':272},
    'isolated_centers':sorted(a for a,d in center_degree.items() if d==0),
    'centers_need_not_be_independent':True,
    'fixed_original_pins_not_current_center_neighbors':True})

steps=[]
for i,pins in enumerate(PINS):
    current_n=len(adj)
    assert current_n==7242+i
    before=collections.Counter(len(adj[p]) for p in pins)
    assert all(len(adj[p])<26 for p in pins)
    assert before=={25:25}
    # Complete CURRENT graph radius2: includes every earlier new clone.
    dist={p:0 for p in pins}
    frontier=set(pins)
    for d in (1,2):
        reached={v for u in frontier for v in adj[u]}-dist.keys()
        dist.update({v:d for v in reached})
        frontier=reached
    uncovered=sorted(set(range(current_n))-dist.keys())
    assert not uncovered,(i,len(uncovered),uncovered[:10])
    oldclone_hist=dict(sorted(collections.Counter(dist[v] for v in range(7242,current_n)).items()))
    adj.append(set(pins))
    for p in pins:
        adj[p].add(current_n)
    assert len(adj[current_n])==25
    steps.append({'step':i,'new_vertex':current_n,'center':CENTERS[i],
        'immutable_pin_row':i,'pins':list(pins),'pin_count':25,
        'pin_degree_before':dict(sorted(before.items())),
        'current_n_before':current_n,'complete_current_R2_covered':len(dist),
        'R2_uncovered_count':0,
        'R2_distance_histogram':dict(sorted(collections.Counter(dist.values()).items())),
        'earlier_new_vertex_distance_histogram':oldclone_hist,
        'all_pins_are_original_source_vertices':True,
        'new_new_edges_added':0})
assert len(adj)==7531
hist=dict(sorted(collections.Counter(map(len,adj)).items()))
assert hist=={25:306,26:7225}
assert all(u not in nbs for u,nbs in enumerate(adj))
assert all(u in adj[v] for u,nbs in enumerate(adj) for v in nbs)
assert all(v<7242 for u in range(7242,7531) for v in adj[u])
edges={(u,v) for u,nbs in enumerate(adj) for v in nbs if u<v}
assert len(edges)==97750 and source_edges<=edges
assert len(edges-source_edges)==7225
# Exactly one ordinary connectivity BFS, never source or candidate allroots.
q=collections.deque([0])
seen={0}
while q:
    u=q.popleft()
    for v in adj[u]:
        if v not in seen:
            seen.add(v)
            q.append(v)
assert len(seen)==7531
with (OUT/'graph_d26_D3_n7531.edges').open('w') as stream:
    stream.write('7531 97750\n')
    for a,b in sorted(edges):
        stream.write(f'{a} {b}\n')
CPU=time.process_time()-START
write('EXTENSION_STEPS.json',{
    'status':'ALL289_COMPLETE_CURRENT_R2_CHECKS_PASS','steps':steps,
    'immutable_source_pins':'IMMUTABLE_SOURCE_PINS.json',
    'source_edges_retained':90525,'new_vertices':289,'new_edges':7225,
    'new_new_edges':0,'degree_load_maximum':1})
result={'status':'PRODUCER_PASS_FIXED7531_CANDIDATE_AWAIT_INDEPENDENT_ACCEPTANCE',
    'target_Delta':26,'target_D':3,'n':7531,'m':97750,
    'source_n':7242,'source_m':90525,'source_degree':25,
    'source_edges_retained':90525,'new_vertices':289,'new_edges':7225,'new_new_edges':0,
    'immutable_original_source_pins':True,'pins_per_clone':25,
    'current_R2_checks':289,'current_R2_uncovered_count':0,
    'current_graph_includes_all_earlier_clones':True,
    'degree_histogram':hist,'maximum_degree':26,'simple':True,'reciprocal':True,
    'centers_induced_edges':136,'centers_induced_degree_histogram':{'0':17,'1':272},
    'source_pin_degree_load_maximum':1,'source_BFS_runs':0,'candidate_allroots_BFS_runs':0,
    'ordinary_final_root0_connectivity_BFS_runs':1,'root0_connectivity_covered':7531,
    'solver_calls':0,'worker_count':1,'producer_CPU_seconds':CPU,
    'candidate_graphs_generated':1,'alternative_fields_ovoids_spreads_or_completion_variants':0,
    'independent_acceptance':'ROOT_OWNED_PENDING_FRESH_LITERAL_CHECK',
    'concrete_Lean':'SEPARATE_TASK','public_record_claim':False,
    'public_comparison':'ROOT_PASSED_LIMITED7514FORMULA_BASELINE_NOTGLOBAL_OR_PRIORITY_CERTIFICATE',
    'further_construction_running':False}
write('RESULT.json',result)
write('TERMINAL.json',{'status':'PRODUCER_FIXED7531_LOCAL_CONSTRUCTION_TERMINAL','result':result})
print(json.dumps(result,indent=2))
