#!/usr/bin/env python3
"""Literal degree/full-N structure only: no R2, BFS, new graph or solver."""
import collections
import json
from pathlib import Path
import resource
import time

OUT=Path(__file__).resolve().parent
START=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(5,5))

def save(result):
    (OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

with (OUT.parent/'graph_d26_D3_n7531.edges').open() as stream:
    n,m=map(int,next(stream).split())
    assert (n,m)==(7531,97750)
    adj=[set() for _ in range(n)]
    rows=0
    for text in stream:
        a,b=map(int,text.split())
        adj[a].add(b)
        adj[b].add(a)
        rows+=1
    assert rows==m
hist=dict(sorted(collections.Counter(map(len,adj)).items()))
assert hist=={25:306,26:7225}
low={v for v,nbs in enumerate(adj) if len(nbs)==25}
high=set(range(n))-low
low_edges=sorted((u,v) for u in low for v in adj[u]&low if u<v)
if low_edges:
    save({'status':'COUNTEREXAMPLE_LOW_LOW_EDGE','edge':low_edges[0],
          'CPU_seconds':time.process_time()-START})
    raise SystemExit(0)
assert all(adj[v]<=high for v in low)
classes=collections.defaultdict(list)
for v in sorted(low):
    classes[tuple(sorted(adj[v]))].append(v)
ordered=sorted(classes.items(),key=lambda item:item[1][0])
seen={}
for i,(nbs,members) in enumerate(ordered):
    assert len(nbs)==25
    for h in nbs:
        if h in seen:
            j=seen[h]
            save({'status':'COUNTEREXAMPLE_DISTINCT_CLASS_NEIGHBORHOOD_INTERSECTION',
                  'class_representatives':[ordered[j][1][0],members[0]],
                  'common_high_vertex':h,'CPU_seconds':time.process_time()-START})
            raise SystemExit(0)
        seen[h]=i
size_hist=dict(sorted(collections.Counter(len(members) for _,members in ordered).items()))
assert len(ordered)==289 and size_hist=={1:272,2:17}
assert set(seen)==high and len(seen)==7225
assert {v for v in low if v>=7242}==set(range(7242,7531))
old_low=sorted(v for v in low if v<7242)
assert len(old_low)==17
# Pure adjacency identities, not distance expansion: each high vertex belongs
# to exactly one class neighborhood, hence all its low neighbors are that class.
assert all((adj[h]&low)==set(ordered[i][1]) for h,i in seen.items())
result={'status':'PASS_FIXED7531_SINGLE_RETAINED_EDGE_CAP26_EXTENSION_OBSTRUCTED',
    'literal_input':'../graph_d26_D3_n7531.edges','n':7531,'m':97750,
    'degree_histogram':hist,'available_degree25_vertices':306,
    'new_clone_low_vertices':289,'old_chosen_flag_low_vertices':17,
    'old_low_labels':old_low,'low_low_edges':0,
    'low_full_neighborhood_size':25,'all_low_neighbors_high_degree26':True,
    'equal_full_neighborhood_classes':289,'class_size_histogram':size_hist,
    'doubleton_classes':[members for _,members in ordered if len(members)==2],
    'distinct_class_high_neighborhoods_pairwise_disjoint':True,
    'class_neighborhood_union_size':7225,'class_neighborhood_union_exactly_high_vertices':True,
    'every_high_vertex_low_neighbors_exactly_one_entire_class':True,
    'minimum_new_vertex_pins_for_low_class_D3_coverage':289,
    'permitted_new_vertex_degree':26,
    'strict_scope':'fixed7531 + exactlyone new vertex; retainall old edges; maxdegree26; targetD3',
    'open_scope':['multiple cooperative additions','rewiring','other sources'],
    'new_graphs_generated':0,'R2_expansions':0,'BFS_runs':0,'solver_calls':0,
    'CPU_seconds':time.process_time()-START,'worker_count':1,'further_work_running':False}
save(result)
