import time
START=time.process_time()
from pathlib import Path
from itertools import product
from collections import deque
import json,resource
resource.setrlimit(resource.RLIMIT_CPU,(10,10))
HERE=Path(__file__).resolve().parent
PRIOR=5.474706358
BAR=[1,0,3,2];M=[[2,1,4],[2,1,4],[1,2,7],[1,2,7]];V=[1,2,4,7];FULL=(1<<64)-1

def save(n,x):(HERE/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
if(HERE/'ATTEMPT.json').exists():raise RuntimeError('one shot')
save('ATTEMPT.json',{'status':'STARTED','prior_and_prep':PRIOR,'casecap':30})
def app(cols,x):return(cols[0]if x&1 else 0)^(cols[1]if x&2 else 0)^(cols[2]if x&4 else 0)
for p in range(4):
 assert app(M[BAR[p]],V[p])==V[BAR[p]]
 assert all(app(M[BAR[p]],app(M[p],x))==x for x in range(8))
words=[]
for n in range(4):
 for w in product(range(4),repeat=n):
  pack=0
  for x in range(8):
   out={x}
   for p in w:out={app(M[p],y)^(V[p]if lam else 0)for y in out for lam in [0,1]}
   pack|=sum(1<<y for y in out)<<(8*x)
  words.append((w,pack))
checked=0;hit=None;records=[];self_fails=0;projection_fail=0
for q in range(1,11):
 for r in range(1,11):
  a=[0]*33;b=[0]*33
  for j in range(11):
   a[j]=11+j;a[11+j]=22+j;a[22+j]=(j+1)%11
   b[j]=22+j;b[11+j]=(j+q)%11;b[22+j]=11+(j+r)%11
  ai=[0]*33;bi=[0]*33
  for u in range(33):ai[a[u]]=u;bi[b[u]]=u
  C=[[a[u],ai[u],b[u],bi[u]]for u in range(33)]
  assert all(u not in row and len(set(row))==4 for u,row in enumerate(C))
  covers=[];bad=None;self_pass=True
  for root in [0,11,22]:
   cover=[0]*33;reachable=set()
   for w,pack in words:
    v=root
    for p in w:v=C[v][p]
    cover[v]|=pack;reachable.add(v)
   self_pass &= cover[root]==FULL
   covers.append({'type_root':root,'self_full8':cover[root]==FULL,'full_target_count':sum(x==FULL for x in cover),'controller_targets_reachable':len(reachable)})
   if bad is None:
    for v,pack in enumerate(cover):
     if pack!=FULL:
      x=next(x for x in range(8)if (pack>>(8*x))&255!=255)
      mask=(pack>>(8*x))&255;missing=next(y for y in range(8)if not(mask>>y&1))
      bad={'root':root,'target':v,'source_x':x,'missing_y':missing,'fiber_covered_for_x':mask.bit_count(),'no_controller_route':v not in reachable}
      break
  checked+=1
  if not self_pass:self_fails+=1
  if bad and bad['no_controller_route']:projection_fail+=1
  records.append({'q':q,'r':r,'self_pass':self_pass,'firstbad':bad,'root_summaries':covers})
  if bad is None:hit={'q':q,'r':r,'controller':C};break
 if hit:break
status='COMPLETE_NO_FIXED_ARC_UNIFORM_TRIANGLE_C33_C11'if hit is None else'POINT_COVER_HIT_PENDING_PRODUCER'
producer=False;roots=0
if hit:
 C=hit['controller'];edges=set()
 for u in range(33):
  for x in range(8):
   for p in range(4):
    for lam in [0,1]:
     v=8*C[u][p]+(app(M[p],x)^(V[p]if lam else 0));old=8*u+x
     assert old!=v;edges.add(tuple(sorted((old,v))))
 assert len(edges)==1056
 with(HERE/'candidate_d8_D3_n264.edges').open('w')as f:
  f.write('264 1056\n')
  for u,v in sorted(edges):f.write(f'{u} {v}\n')
 adj=[[]for _ in range(264)]
 for u,v in edges:adj[u].append(v);adj[v].append(u)
 assert all(len(z)==len(set(z))==8 for z in adj)
 producer=True
 for root in range(264):
  d=[-1]*264;d[root]=0;todo=deque([root])
  while todo:
   u=todo.popleft()
   for v in adj[u]:
    if d[v]<0:d[v]=d[u]+1;todo.append(v)
  roots+=1
  if -1 in d or max(d)>3:producer=False;break
 save('PARAMETERS.json',{'n':264,'m':1056,'degree':8,'p':1,'q':hit['q'],'r':hit['r'],'controller':C,'maps':M,'v':V,'producer_roots':roots,'producer_D3':producer,'fresh_Lean_ARIS':'PENDING'})
 status='CANDIDATE264_PRODUCER_PASS_PENDING_FRESH'if producer else'UNKNOWN_POINT_PRODUCER_DISCREPANCY'
save('ALL_PARAMETER_RESULTS.json',records)
r={'status':status,'normalized_parameters_checked':checked,'full_domain':100,'domain_complete':checked==100 or hit is not None,'prediction_any_full_supported':hit is not None,'all_self_controller_fibres_pass':self_fails==0,'first_bad_is_projection_count':projection_fail,'hit_parameters':None if hit is None else[1,hit['q'],hit['r']],'graph_generated':hit is not None,'producer_roots':roots,'producer_pass':producer,'native_CPU':time.process_time()-START,'prior_plus_prep_CPU':PRIOR,'case_CPU':PRIOR+time.process_time()-START,'case_cap':30,'oldgraphs_BFS_Lean_ARIS_solver':0,'scope':'fixedARCchart;33controllerthree-types/C11voltage pnonzero,qnonzero,rnonzero;unitnormalized100. notgeneralC33/8D3','new_accepted_graph_parameter_Lean':[0,0,0],'next':'STOP_FIXED_FAMILY_NO_MOREm_ORCHARTS','terminal':True}
save('RESULT.json',r);save('TERMINAL.json',r)
print(json.dumps(r,ensure_ascii=False),flush=True)
