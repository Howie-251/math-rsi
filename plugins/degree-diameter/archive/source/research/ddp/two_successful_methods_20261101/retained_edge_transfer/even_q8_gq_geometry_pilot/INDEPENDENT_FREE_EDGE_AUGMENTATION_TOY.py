import collections,json,time
from pathlib import Path
D=Path(__file__).resolve().parent

def gadget(k,peer):
    # A regular host-code example, not an asserted diameter-three host.
    M=4;delta=1;Delta=delta+k;N=M+M*k+1;h=N-1
    adj=[set()for _ in range(N)]
    def edge(a,b):adj[a].add(b);adj[b].add(a)
    for c in range(0,M,2):edge(c,c+1)
    clone=lambda c,r:M+c*k+r
    for c in range(M):
        for r in range(k):edge(clone(c,r),c^1)
    f=clone(0,0);g=clone(2,0);edge(h,f)
    if peer:edge(f,g)
    return adj,h,f,g,Delta

def bfs(adj,s):
    dist=[None]*len(adj);dist[s]=0;q=collections.deque([s])
    while q:
        v=q.popleft()
        for w in adj[v]:
            if dist[w]is None:dist[w]=dist[v]+1;q.append(w)
    return dist

before,h,f,g,cap=gadget(2,False);after,h2,f2,g2,cap2=gadget(2,True)
assert(h,f,g,cap)==(h2,f2,g2,cap2)
db=bfs(before,h);da=bfs(after,h)
reachable_before=[c for c in range(4)if db[c]is not None and db[c]<=3]
reachable_after=[c for c in range(4)if da[c]is not None and da[c]<=3]
assert reachable_before==[0,1]and reachable_after==[0,1,3]
assert all(len(n)<=cap for n in after)
assert da[3]==3 and all(b in after[a]for a,b in zip([h,f,g],[f,g,3]))
illegal,ih,iff,ig,icap=gadget(1,True)
assert len(illegal[iff])==3>icap==2

thresholds=[]
for name,delta,M in [('balanced',81,4160),('Payne',80,4032)]:
    first=next(k for k in range(1,100)if(delta+2*k+1)**2//4>=M)
    thresholds.append(dict(source=name,delta=delta,M=M,excluded_uniform_k=[1,first-1],max_excluded_cap=delta+first-1,bound_at_max=(delta+2*(first-1)+1)**2//4,first_unexcluded_k=first,first_unexcluded_cap=delta+first,bound_at_first=(delta+2*first+1)**2//4))
result=dict(status='PREDICTION_SUPPORTED_PAPER_PROOF_AND_ONE_DEGREE_LEGAL_ROUTE_GADGET',necessary_bound='M<=floor((delta+2*k+1)^2/4)',helper_inequality='M<=(k+1)*p_h+sum_neighbor_B_p_g',CPU_seconds=time.process_time(),CPU_budget_seconds=5,toy=dict(host='two disjoint matching edges,delta1,C=all4,D=empty',uniform_k=2,cap=cap,vertices=len(after),all_vertex_degrees=[len(n)for n in after],all_degrees_legal=True,source_targets_reachable_within3_before_peer=reachable_before,source_targets_reachable_within3_after_peer=reachable_after,new_peer_route=[h,f,g,3],distance_to_old3_before=db[3],distance_to_old3_after=da[3],first_pin_targets=3,first_pin_bound=3,k1_same_extra_edges=dict(cap=icap,first_pin_degree=len(illegal[iff]),legal=False),full_graph_D3_claimed=False),thresholds=thresholds,tiny_helper_BFS_runs=2,q8_graph_BFS_runs=0,old_toys_rerun=0,new_largegraphs=0,field_geometry_projection_rechecks=0,Lean_runs=0,solver_calls=0,exhaustive_configurations=0,external_review_calls=0,new_graph_or_Lean_count=0,global_record_or_priority_claim=False)
for name,data in [('INDEPENDENT_FREE_EDGE_AUGMENTATION_RESULT.json',result),('INDEPENDENT_FREE_EDGE_AUGMENTATION_TERMINAL.json',dict(status='TERMINAL_PAPER_AND_TINY_ROUTE_TEST_COMPLETE',running=False,active_processes=[],CPU_seconds=result['CPU_seconds'],CPU_budget_seconds=5,new_graphs=0,Lean_runs=0,external_review_calls=0))]:
    (D/name).write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(result),flush=True)
