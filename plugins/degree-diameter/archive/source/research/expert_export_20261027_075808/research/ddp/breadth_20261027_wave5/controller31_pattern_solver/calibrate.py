from pathlib import Path
from collections import Counter
import json,time
from core import make_problem,read_graph,mv,rank,L,INV
P=Path(__file__).resolve().parent;R=P.parent.parent;started=time.process_time()
source30=R/'breadth_20261027_wave4/mizuno_d3_source/construction.json'
d=json.loads(source30.read_text());C=d['controller'];edges=[(u,v) for u,row in enumerate(C) for v in row if u<v]
problem,pre=make_problem(30,edges);G=problem['graph'];ports=G['ports'];direct=[[0]*30 for _ in range(30)]
for u in range(30):
 for a in C[u]:
  for b in C[a]:
   if b==u:continue
   for c in C[b]:
    if c!=a:direct[u][c]+=1
for row,(u,v) in enumerate(problem['pairs']):assert direct[u][v]==problem['raw_counts'][row]*(2 if u==v else 1)
assert len(problem['paths'])==540 and pre['status']=='REJECT_ORDER_NOT31'
Ts=[[None]*4 for _ in range(30)]
for e,(u,v) in enumerate(G['edges']):
 p=ports[u].index(v);opt=problem['edge_options'][e][0];Ts[u][p]=opt['matrix'];Ts[v][INV[p]]=opt['inverse_matrix']
def route_rank(walk):
 cols=[]
 for u,v in zip(walk,walk[1:]):
  t=ports[u].index(v);cols=[mv(Ts[u][t],x) for x in cols]+[L[INV[t]]]
 return rank(cols)
predicted=Counter()
for pid,path in enumerate(problem['paths']):
 expected=2 if pid in problem['edge_options'][path['edge']][0]['bad_path_ids'] else 3
 assert route_rank(path['vertices'])==expected and route_rank(list(reversed(path['vertices'])))==expected
 predicted[expected]+=1
source31=R/'breadth_20261027_wave4/controller31_triangle_extension/best_raw_coverage.json'
n,es=read_graph(source31);p31,r31=make_problem(n,es)
assert r31['status']=='REJECT_RAW_SHORTWALK_GAP' and r31['missing_ordered_pairs']==34
result=dict(status='CALIBRATION_PASS',source30=str(source30),source30_edges=len(edges),source30_paired_NB3=len(problem['paths']),source30_unlabelled_direct_counts_equal_paired_model=True,source30_all540_path_rank_predictions_equal_actual_matrix_routes_and_reverse=True,source30_first_option_paired_rank_histogram=dict(predicted),source30_not_a_global_baseline_or_certificate=True,old31_fixture=str(source31),old31_precheck=r31,old31_solver_invoked=False,production_graphs_generated=0,CPU_seconds=time.process_time()-started)
(P/'calibration.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
