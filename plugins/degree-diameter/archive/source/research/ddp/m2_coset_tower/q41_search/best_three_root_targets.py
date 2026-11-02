"""Only three ordinary BFS runs on the already saved best; no candidate search."""
from collections import Counter, deque
from pathlib import Path
import json
import time

HERE=Path(__file__).resolve().parent
started=time.process_time()
data=list(map(int,(HERE/'search.best.edges').read_text().split()))
n,m=data[:2]
assert (n,m)==(1066,2665)
adj=[[] for _ in range(n)]
for u,v in zip(data[2::2],data[3::2]):
    adj[u].append(v);adj[v].append(u)
regions=[('leaf',0,820),('block',820,1025),('head',1025,1066)]
rows=[]
for source,root,_ in regions:
    distance=[-1]*n;distance[root]=0;queue=deque([root])
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if distance[v]<0:
                distance[v]=distance[u]+1;queue.append(v)
    assert -1 not in distance
    targets={}
    for name,lo,hi in regions:
        missing=[v for v in range(lo,hi) if distance[v]>5]
        coordinates=([[v%41,v//41] for v in missing] if name=='leaf' else
                     [[(v-820)%41,(v-820)//41] for v in missing] if name=='block' else
                     [v-1025 for v in missing])
        targets[name]=dict(missing_count=len(missing),distance_histogram=dict(sorted(Counter(distance[lo:hi]).items())),
                           missing_vertex_ids=missing,missing_coordinates=coordinates)
    rows.append(dict(source_layer=source,root_vertex=root,
                     missing_total=sum(x['missing_count'] for x in targets.values()),targets=targets))
matrix=[[row['targets'][target]['missing_count'] for target,_,_ in regions] for row in rows]
weights=[820,205,41]
assert [row['missing_total'] for row in rows]==[84,64,60]
assert all(weights[i]*matrix[i][j]==weights[j]*matrix[j][i] for i in range(3) for j in range(3))
pair_classes={}
for i,(source,_,_) in enumerate(regions):
    for j,(target,_,_) in enumerate(regions):
        if j<i:continue
        count=weights[i]*matrix[i][j]
        if i==j:
            assert count%2==0
            count//=2
        pair_classes[source+'-'+target]=count
assert sum(pair_classes.values())==42230
result=dict(scope='Exactly three BFS on the previously saved best edge list; no search or new graph',
            root_and_target_order=['leaf','block','head'],missing_matrix=matrix,
            bad_unordered_pairs_by_layer=pair_classes,rows=rows,cpu_seconds=time.process_time()-started)
(HERE/'best.three_root_targets.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ('missing_matrix','bad_unordered_pairs_by_layer','cpu_seconds')},indent=2))
