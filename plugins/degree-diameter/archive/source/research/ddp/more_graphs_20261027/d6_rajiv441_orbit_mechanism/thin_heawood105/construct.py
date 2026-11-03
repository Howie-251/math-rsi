"""One thin-incidence application of the exactly recovered flag operator."""
from pathlib import Path
from collections import Counter, deque
import json
import time

OUT=Path(__file__).resolve().parent
START=time.process_time()
assert json.loads((OUT/'PREDICTION.json').read_text())['frozen_before_construction']
# Fano points and lines are nonzeroF2^3 vectors, incidence by zero dotproduct.
heawood=[(p,7+l) for p in range(7) for l in range(7) if ((p+1)&(l+1)).bit_count()%2==0]
assert len(heawood)==21
lines=[tuple(i for i,e in enumerate(heawood) if v in e) for v in range(14)]
assert all(len(L)==3 for L in lines)
flags=[(p,L) for L in range(14) for p in lines[L]]
assert len(flags)==42
ix={flag:i for i,flag in enumerate(flags)}
edges=set()
def edge(a,b):
    assert a!=b
    edges.add(tuple(sorted((a,b))))
for i,(p,L) in enumerate(flags):
    for a in lines[L]:
        if a!=p: edge(a,21+i)
    for M in heawood[p]:
        if M==L:continue
        for q in lines[M]:
            if q!=p:edge(21+i,63+ix[q,M])
    for M in heawood[p]:
        if M!=L:edge(63+i,63+ix[p,M])
n=105
adj=[[] for _ in range(n)]
for a,b in edges:adj[a].append(b);adj[b].append(a)
assert len(edges)==189 and Counter(map(len,adj))=={4:63,3:42}
path=OUT/'graph105.edges'
with path.open('w') as f:
    f.write(f'{n} {len(edges)}\n')
    for a,b in sorted(edges):f.write(f'{a} {b}\n')
distances=[]
for s in range(n):
    dist=[-1]*n;dist[s]=0;todo=deque([s])
    while todo:
        a=todo.popleft()
        for b in adj[a]:
            if dist[b]<0:dist[b]=dist[a]+1;todo.append(b)
    assert min(dist)>=0
    distances.append(dist)
classes=[list(range(21)),list(range(21,63)),list(range(63,105))]
bad_by_types={};first_witness={}
for i in range(3):
    for j in range(i,3):
        pairs=[(a,b) for a in classes[i] for b in classes[j] if a<b or i!=j]
        bad=[(a,b,distances[a][b]) for a,b in pairs if distances[a][b]>4]
        bad_by_types['ABC'[i]+'ABC'[j]]=len(bad)
        if bad:first_witness['ABC'[i]+'ABC'[j]]=list(bad[0])
result=dict(status='EXACT_SINGLE_CONSTRUCTION_COMPLETE',n=n,m=len(edges),max_degree=4,
            min_degree=3,connected=True,simple=True,actual_D=max(map(max,distances)),
            ordinary_bad_unordered_pairs=sum(bad_by_types.values()),bad_by_types=bad_by_types,
            first_witness_by_types=first_witness,
            prediction_AA_all_within4=(bad_by_types['AA']==0),
            prediction_CC_has_distance_over4=(bad_by_types['CC']>0),
            full_target_passed=not any(bad_by_types.values()),
            CPU_seconds=time.process_time()-START,old_source_BFS=0,
            edge_file=path.name,scope='ExactlyoneHeawoodedge-star(s2,t1)geometry and recoveredflagoperator; no repairs.')
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
