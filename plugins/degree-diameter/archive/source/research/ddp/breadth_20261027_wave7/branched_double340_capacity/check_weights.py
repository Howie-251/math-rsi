from pathlib import Path
from collections import Counter
import json,time

P=Path(__file__).resolve().parent
B=P.parent/'signed_double340'
t=time.process_time()
lines=(B/'source.edges').read_text().splitlines()
n,m=map(int,lines[0].split());edges=[tuple(map(int,row.split())) for row in lines[1:]]
assert n==170 and m==595 and edges==sorted(set(edges))
ei={e:i for i,e in enumerate(edges)}
paths=json.loads((B/'distance3_paths.json').read_text())
unique=[row for row in paths if row['NB3_path_count']==1]
assert len(unique)==5130
weights=[0]*m
for row in unique:
    assert len(row['paths'])==1
    path=row['paths'][0]
    assert len(path)==4 and len(set(path))==4
    for u,v in zip(path,path[1:]):weights[ei[tuple(sorted((u,v)))]]+=1
assert sum(weights)==3*5130
incident=[[] for _ in range(n)]
for index,(u,v) in enumerate(edges):incident[u].append(index);incident[v].append(index)
assert all(len(row)==7 for row in incident)
mv=[max(weights[e] for e in row) for row in incident]
argmax=[next(e for e in row if weights[e]==mv[v]) for v,row in enumerate(incident)]
assert all(2*weights[e]<=mv[u]+mv[v] for e,(u,v) in enumerate(edges))
fine=sum(mv)//2;coarse=(n//2)*max(weights)
out=dict(status='ALL_BRANCH_MATCHINGS_CAPACITY_OBSTRUCTED' if fine<5130 else 'MATCHING_WEIGHT_BOUND_NOT_DECISIVE_STOP',
         source_vertices=n,source_edges=m,required_unique_paths=5130,
         edge_weight_sum=sum(weights),edge_weight_histogram=dict(sorted(Counter(weights).items())),
         maximum_edge_weight=max(weights),coarse_85_times_maxw=coarse,
         vertex_max_weight_histogram=dict(sorted(Counter(mv).items())),vertex_max_weight_sum=sum(mv),
         fine_floor_half_sum_vertex_max=fine,
         shortfall_from_5130=5130-fine,
         edge_weights=[dict(edge_id=e,edge=list(pair),weight=weights[e]) for e,pair in enumerate(edges)],
         vertex_maxima=[dict(vertex=v,maximum_incident_weight=mv[v],attaining_edge_id=argmax[v]) for v in range(n)],
         all_edge_dual_inequalities_checked=True,
         inequality='covered_unique_paths <= sum_{e in B} w_e <= floor(sum_v m_v / 2), for every base-edge matching B',
         scope='Only this fixed170 source with K2,2 branches on a matching and verticals exactly at uncovered vertices.',
         CPU_seconds=time.process_time()-t,matchings_searched=0,signings_searched=0,
         graphs_generated=0,BFS_performed=False,pending=[])
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['edge_weights','vertex_maxima']},indent=2))
