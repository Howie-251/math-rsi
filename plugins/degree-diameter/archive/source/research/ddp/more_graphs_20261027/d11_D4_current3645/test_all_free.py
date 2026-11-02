"""Onecompleteall7freeR3test; exportonlyifwholegraphconditionpasses."""
from pathlib import Path
from collections import Counter,deque
import json,time,resource,shutil

OUT=Path(__file__).resolve().parent
start=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(1,1))
load=lambda p:json.loads(p.read_text())
prediction=load(OUT/'COVER_PREDICTION.json')
assert prediction['frozen_before_coverage_algorithm']
pins=prediction['free_vertices'];assert pins==[3456,3489,3564,3571,3583,3603,3643]
source=OUT/prediction['source']
with source.open() as f:
    n,m=map(int,f.readline().split());assert (n,m)==(3645,20044)
    adj=[[] for _ in range(n)]
    for line in f:
        u,v=map(int,line.split());adj[u].append(v);adj[v].append(u)
assert pins==[v for v in range(n) if len(adj[v])<11]
assert all(len(adj[p])==10 for p in pins)
dist=[-1]*n;q=deque()
for p in pins:dist[p]=0;q.append(p)
while q:
    u=q.popleft()
    if dist[u]==3:continue
    for v in adj[u]:
        if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
missing=[v for v in range(n) if dist[v]<0]
result=dict(source_file=str(source),source_n=n,source_m=m,degree_cap=11,target_D=4,savedL=3645,
    free_vertices=pins,original_free_degrees=[10]*7,covered_count=n-len(missing),missing_count=len(missing),
    missing=missing,missing_core3444=sum(v<3444 for v in missing),missing_layer201=sum(v>=3444 for v in missing),
    R3_distance_histogram=dict(sorted(Counter(x for x in dist if x>=0).items())),
    prediction_supported=not missing,graph_generated=False,actual_candidate_n=None,actual_candidate_D=None,
    oldsource_allBFS=0,multisource_R3_runs=1,witness_targeted_BFS_runs=0,pending=[])
if not missing:
    graph=OUT/'graph_d11_D4_n3646.edges'
    with source.open() as old,graph.open('w') as new:
        old.readline();new.write('3646 20051\n');shutil.copyfileobj(old,new)
        for p in pins:new.write(f'{p} 3645\n')
    result.update(status='PRODUCER_COMPLETE3646_ROOT_CHECK_PENDING',new_vertex=3645,new_n=3646,new_m=20051,
        new_degree=7,graph_generated=True,actual_candidate_n=3646,actual_candidate_D=None,graph_file=str(graph),
        all_source_edges_retained=True,actual_current_R3_missing=0,pending=['Root independentfirstD4acceptance'])
else:
    witness=missing[0];d=[-1]*n;d[witness]=0;q=deque([witness])
    while q:
        u=q.popleft()
        if d[u]==4:continue
        for v in adj[u]:
            if d[v]<0:d[v]=d[u]+1;q.append(v)
    distances=[d[p] for p in pins];assert distances==[4]*7
    result.update(status='ALL_EDGE_PRESERVING_EXTENSIONS_OF_FIXED_SOURCE_EXCLUDED_BY_FREEPORT_R3',
        first_missing_target=witness,first_missing_layer='old3444' if witness<3444 else 'insertedlayer',
        free_to_first_missing_distances=distances,witness_targeted_BFS_runs=1,
        exclusion_scope='Atleastonenewvertex;retainallsourceedges;maxdegree11;anynumberhelpersandevenaddedoldoldportedges',
        proof='Anylength<=4newroot->missingtargetroutehasalastnewedgewhoseoldendpointisanoriginalfreeport;atmost3oldstepsremain,butall7freeportR3missestarget.',
        edge_deletion_or_absorption_excluded=False)
result['CPU_seconds']=time.process_time()-start
(OUT/'COVER_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='missing'}))
