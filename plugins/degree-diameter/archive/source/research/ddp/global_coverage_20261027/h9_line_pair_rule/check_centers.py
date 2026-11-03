"""One edge-common-neighbor pass on knownK; no BFS, clique search or candidates."""
from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
import json,resource,sys,time
resource.setrlimit(resource.RLIMIT_CPU,(10,10))
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3]
sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen
prediction=dict(prediction_id='P7_ADJACENT_CENTERS_CANNOT_SUPPLY987',
                status='FROZEN_BEFORE_SINGLE_COMMON_NEIGHBOR_PASS',timestamp=datetime.now(timezone.utc).isoformat(),
                hypothesis='For fixedK, the adjacentcenter lineimage rule cannot supply987 newvertices under degree12.',
                one_per_line_combinatorial_subcase='One geometric line contributes at most one newpoint; each center covers<=91distinctlines, so987 would need>=11distinctactualcorecenters.',
                planned_test='EveryedgeofaK11has>=9commonneighbors. Compute the global maximum once; no clique enumeration if the test fails to decide.',
                separate_duplicate_safe_paper_bound='Everynewpoint usesatleastonecoredegree slot in U=N_K[C]. For ccliquecenters, |U|<=c(14-c)<=49; mindegK7 gives totalnewpoints<=245, even with repeatedline labels.',
                BFS_planned=False,clique_search_planned=False,packing_planned=False,new_graph_planned=False)
s=json.dumps(prediction,ensure_ascii=False,indent=2)+'\n';assert not screen(s);(HERE/'P7_PREDICTION.json').write_text(s)
start=time.process_time()
source=ROOT/'research/ddp/global_coverage_20261027/h9_bare_core_clones/bare_core.edges'
with source.open() as f:
    n,m=map(int,next(f).split());adj=[set() for _ in range(n)];edges=[]
    for line in f:
        u,v=map(int,line.split());adj[u].add(v);adj[v].add(u);edges.append((u,v))
assert (n,m)==(41356,234318) and len(edges)==m
hist=Counter();kappa=-1;witness=None
for u,v in edges:
    common=adj[u].intersection(adj[v]);k=len(common);hist[k]+=1
    if k>kappa:kappa=k;witness=dict(u=u,v=v,common_neighbors=sorted(common))
assert sum(hist.values())==m
D=max(map(len,adj));mind=min(map(len,adj));cmax=min(D+1,kappa+2)
budget_size=max(c*(D+2-c) for c in range(1,cmax+1))
x=dict(status='COMPLETE_SINGLE_COMMON_NEIGHBOR_PASS',source=str(source.relative_to(ROOT)),
       n=n,m=m,maximum_degree=D,minimum_degree=mind,edge_intersections_evaluated=m,
       max_edge_common_neighbors=kappa,max_witness=witness,edge_common_neighbor_histogram=dict(sorted(hist.items())),
       proven_core_clique_upper_bound=cmax,clique_bound_reason='In a cclique everyedgehasatleastc-2commonneighbors.',
       K11_excluded_by_max_common_neighbors=kappa<9,
       one_per_geometric_line_newpoint_bound=91*cmax,
       one_per_geometric_line_total_order_bound=n+91*cmax,
       arbitrary_repeated_linevertices_bound=(D-mind)*budget_size,
       arbitrary_repeated_linevertices_total_order_bound=n+(D-mind)*budget_size,
       budget_bound_formula='Everynewvertexhasatleastonepin in N_K[C]; |N_K[C]|<=c(D+2-c), old deficit<=D-mindegK.',
       budget_bound_scope='Any numberofdistinctnewverticesperline isallowed, but everyline mustmeetoneofthese clique-centered sigma-lines and everyfoldedpointimageofthatline mustbe a pin.',
       general_lineimage_family_excluded=False,target_newvertices=987,
       graph_generated=False,BFS_count=0,clique_enumeration_count=0,packing_calls=0,solver_calls=0,workers=1,
       CPU_seconds=time.process_time()-start)
def strings(x):
    if isinstance(x,str):return [x]
    if isinstance(x,dict):return [s for y in x.values() for s in strings(y)]
    if isinstance(x,list):return [s for y in x for s in strings(y)]
    return []
assert not screen('\n'.join(strings(x)))
(HERE/'P7_RESULT.json').write_text(json.dumps(x,indent=2)+'\n')
print(json.dumps(x,indent=2))
