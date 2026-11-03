from pathlib import Path
from collections import deque,Counter
import json,time

P=Path(__file__).resolve().parent
t=time.process_time()
lines=(P/'source.raw.edges').read_text().splitlines()
raw=[tuple(map(int,row.split())) for row in lines if row.strip()]
n=1+max(max(e) for e in raw);m=len(raw)
assert n==170 and m==595
edges=sorted(tuple(sorted(e)) for e in raw)
assert len(set(edges))==m and all(u!=v and 0<=u<v<n for u,v in edges)
with (P/'source.edges').open('w') as f:
    print(n,m,file=f)
    for u,v in edges:print(u,v,file=f)
ei={e:i for i,e in enumerate(edges)}
adj=[[] for _ in range(n)]
for u,v in edges:adj[u].append(v);adj[v].append(u)
for row in adj:row.sort()
assert all(len(row)==7 for row in adj)
distances=[];dist_hist=Counter();route_hist=Counter();pairs=[];unique=None
for root in range(n):
    dist=[-1]*n;dist[root]=0;q=deque([root])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
    assert min(dist)>=0 and max(dist)==3
    distances.append(dist);dist_hist.update(dist)
    paths=[[] for _ in range(n)]
    for a in adj[root]:
        for b in adj[a]:
            if b==root:continue
            for v in adj[b]:
                if v==a:continue
                if dist[v]==3:paths[v].append([root,a,b,v])
    for v in range(n):
        if dist[v]!=3:continue
        count=len(paths[v]);assert count>0;route_hist[count]+=1
        if root<v:
            pairs.append(dict(pair=[root,v],NB3_path_count=count,paths=paths[v]))
            if count==1 and unique is None:
                path=paths[v][0]
                unique=dict(pair=[root,v],source_distance=3,unique_length3_path=path,
                            unique_path_edge_ids=[ei[tuple(sorted((a,b)))] for a,b in zip(path,path[1:])],
                            claim='No path of length<=3 in the 340 lift can use a vertical edge, since it would project to at most2 horizontal edges. The unique 3-edge base path has one sign parity, so one sheet target is unreachable within3 for every signing.')
source=dict(status='COMPLETE',vertices=n,edges=m,simple=True,degree_histogram=dict(Counter(map(len,adj))),connected=True,
            all_source_BFS_roots=n,diameter=3,ordered_distance_histogram=dict(sorted(dist_hist.items())),
            ordered_distance3_pairs=sum(route_hist.values()),ordered_d3_NB3_path_count_histogram=dict(sorted(route_hist.items())),
            unordered_d3_pairs=len(pairs),BFS_repeated=False)
(P/'source_check.json').write_text(json.dumps(source,indent=2)+'\n')
(P/'source_distances.json').write_text(json.dumps(distances,separators=(',',':'))+'\n')
(P/'distance3_paths.json').write_text(json.dumps(pairs,indent=2)+'\n')
result=dict(status='UNIQUE_THREE_PATH_OBSTRUCTION_STOP' if unique else 'NO_UNIQUE_THREE_PATH_CONTINUE_TO_XOR_NECESSITY',
            source=source,unique_three_path_witness=unique,sign_assignments_tested=0,lift340_generated=False)
if unique is None:
    constraints=[]
    for row in pairs:
        if row['NB3_path_count']!=2:continue
        mask=0
        for path in row['paths']:
            for a,b in zip(path,path[1:]):mask^=1<<ei[tuple(sorted((a,b)))]
        constraints.append(dict(pair=row['pair'],paths=row['paths'],coefficient_edge_ids=[i for i in range(m) if mask>>i&1],rhs=1))
    basis={};contradiction=None
    for index,row in enumerate(constraints):
        mask=sum(1<<e for e in row['coefficient_edge_ids']);rhs=1;combination=1<<index
        while mask:
            pivot=mask.bit_length()-1
            if pivot not in basis:basis[pivot]=(mask,rhs,combination);break
            old,oldrhs,oldcomb=basis[pivot];mask^=old;rhs^=oldrhs;combination^=oldcomb
        if not mask and rhs:
            contradiction=[j for j in range(len(constraints)) if combination>>j&1];break
    result.update(status='TWO_PATH_XOR_CONTRADICTION_STOP' if contradiction else 'TWO_PATH_XOR_CONSISTENT_OTHER_ROUTE_CONSTRAINTS_OPEN',
                  two_path_constraints=len(constraints),Gaussian_rank=len(basis),XOR_unsatisfiable=contradiction is not None,
                  contradiction_constraint_ids=contradiction,
                  scope='Only exactly2 route pairs impose XOR difference1. No >=3-route pair was forced pairwise different.',
                  constraints=constraints)
result['CPU_seconds']=time.process_time()-t
(P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['constraints']},indent=2))
