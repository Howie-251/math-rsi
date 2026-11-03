from pathlib import Path
from itertools import combinations
from collections import deque,Counter
import json,time,resource
B=Path(__file__).resolve().parent;resource.setrlimit(resource.RLIMIT_CPU,(3,3));t0=time.process_time();assert not (B/'RESULT.json').exists()
def save(n,o):(B/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
edges=sorted({tuple(sorted((i,(i+1)%5))) for i in range(5)}|{(i,i+5) for i in range(5)}|{tuple(sorted((5+i,5+(i+2)%5))) for i in range(5)});assert len(edges)==15
rows=[];survivors=[];hist=Counter();minD=100;best=None;rootqueries=0
for ordinal,sub in enumerate(combinations(range(15),9)):
 g=[[] for _ in range(19)];sx=set(sub);nextv=10
 def add(u,v):g[u].append(v);g[v].append(u)
 for e,(u,v) in enumerate(edges):
  if e in sx:add(u,nextv);add(nextv,v);nextv+=1
  else:add(u,v)
 assert nextv==19 and sum(map(len,g))==48 and sum(4-len(a) for a in g)==28 and all(0<4-len(a)<=2 for a in g)
 diam=0;far=None
 for root in range(19):
  rootqueries+=1;d=[-1]*19;d[root]=0;q=deque([root])
  while q:
   u=q.popleft()
   for v in g[u]:
    if d[v]<0:d[v]=d[u]+1;q.append(v)
  mx=max(d)
  if mx>diam:diam=mx;far=[root,d.index(mx)]
 hist[diam]+=1
 if diam<minD:minD=diam;best={'pattern':ordinal,'subdivided_edge_indices':list(sub),'diameter':diam,'farthest_pair':far,'adjacency':g}
 if diam<=4:survivors.append({'pattern':ordinal,'subdivided_edge_indices':list(sub),'diameter':diam,'adjacency':g,'spokes_per_helper':[4-len(a) for a in g]})
 rows.append({'pattern':ordinal,'subdivided_edge_indices':list(sub),'diameter':diam,'farthest_pair':far})
save('SKELETON.json',{'graph':'standardPetersen10','vertices':10,'edges':edges,'rule':'subdivideexact9distinctedgesonce'});save('ALL_PATTERN_METRICS.json',rows);save('SURVIVORS.json',survivors);save('BEST_METRIC_PATTERN.json',best)
newcpu=time.process_time()-t0
r={'status':'METRIC_SURVIVORS_PENDING_28PORT_ASSIGNMENT' if survivors else 'COMPLETE_NO_FIXED_PETERSEN9SUBDIVISION19_COOPERATIVE_HELPER_FAMILY','patterns':len(rows),'expected_domain':5005,'helper_metric_BFS_roots':rootqueries,'diameter_histogram':dict(hist),'minimum_helper_diameter':minD,'survivors':len(survivors),'prediction_supported':bool(survivors),'new_numeric_CPU':newcpu,'read_CPU_charge':.5,'prepare_CPU_charge':.25,'case_CPU':.75+newcpu,'case_cap':5,'source_or_target383_BFS_oldball_portassignment_solver_Lean_ARIS':0,'new_accepted_graph_parameter_Lean':[0,0,0],'terminal':True,'scope':'fixednatural364preservedhost/freeportsdistance5;Petersen10eachof9distinctedgesonesubdivision;nototherhelpergraphs/general4D5','next':'assignmentinterfaceifmetricpass;elseSTOPnoother_subdivisioncount_skeletonladder'}
save('RESULT.json',r);save('TERMINAL.json',{'terminal':True,'result':'RESULT.json'});print(json.dumps(r,ensure_ascii=False))
