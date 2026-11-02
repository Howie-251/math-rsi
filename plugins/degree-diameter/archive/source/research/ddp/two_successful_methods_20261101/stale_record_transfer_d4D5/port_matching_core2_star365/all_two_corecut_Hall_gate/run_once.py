"""One exact necessary Hall gate over all original two-core-edge cuts."""
import time
START=time.process_time()
from pathlib import Path
from collections import deque, Counter
import json, resource
resource.setrlimit(resource.RLIMIT_CPU,(16,16))
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[5]
SRC=ROOT/'research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/source_and_single'
PRIOR=2.251687814+.3

def save(fn,d): (HERE/fn).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
if (HERE/'ATTEMPT.json').exists():raise RuntimeError('one-shot entiretwo-cut Hall gate already started')
save('ATTEMPT.json',{'status':'STARTED','prior_plus_prep_CPU':PRIOR,'wholecase_cap':20})
lines=(SRC/'source364.edges').read_text().splitlines()
es=[tuple(map(int,l.split()))for l in lines[1:]if l.strip()]
adj=[[]for _ in range(364)]
for u,v in es:adj[u].append(v);adj[v].append(u)
ports=json.loads((SRC/'PORT_BINDING.json').read_text())['eligible_ports'];ps=set(ports)
classes=json.loads((SRC/'PORT_CLASSES.json').read_text())['R2_class_members']
cores=[v for v in range(364)if v not in ps]
coreedges=[(u,v)for u,v in es if u not in ps and v not in ps]
assert len(coreedges)==630 and len(cores)==336
old=json.loads((HERE.parent/'joint_fixed_first_P/FOUR_CORE_R4_SUPPORTS.json').read_text())
r4={p:sum(1<<i for i,d in enumerate(row)if d>=0) for p,row in zip(old['P'],old['rows_distances0_to4_else_minus1'])}
newqueries=0
for root in cores:
 if root in r4:continue
 dist=[-1]*364;dist[root]=0;q=deque([root])
 while q:
  u=q.popleft()
  if dist[u]==4:continue
  for v in adj[u]:
   if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
 r4[root]=sum(1<<v for v,d in enumerate(dist)if d>=0);newqueries+=1
assert newqueries==332
layer2=[]
for b,members in zip(ports,classes):layer2.append(sum(1<<t for t in members if t!=b and t not in adj[b]))
near={v:sum(1<<i for i,p in enumerate(ports)if p in adj[v])for v in cores}
assert all(x.bit_count()<=1 for x in near.values())
save('SOURCE_SUPPORT_BINDING.json',{'coreedges':coreedges,'core_R4_masks_decimal_strings':{str(k):str(v)for k,v in r4.items()},'layer2_masks_decimal_strings':[str(z)for z in layer2],'ports':ports,'near_port_bits':near,'new_depth4_queries':newqueries,'reused_depth4_queries':4,'source_allroot_D5_or_28portballs':0})
checked=0;shared=0;surv=[];margin_min=999;minw=None;hist=Counter();completed=True
with (HERE/'ALL_CUTPAIR_HALL_COUNTS.tsv').open('w')as f:
 f.write('edgeindex0\tedgeindex1\thardowners\tnearports\tmargin\n')
 for i,(a,b) in enumerate(coreedges):
  if time.process_time()-START>15:completed=False;break
  for j in range(i+1,len(coreedges)):
   c,d=coreedges[j]
   if len({a,b,c,d})!=4:shared+=1;continue
   cover=r4[a]|r4[b]|r4[c]|r4[d]
   hardbits=sum(1<<k for k,m in enumerate(layer2)if m & ~cover)
   nearbits=near[a]|near[b]|near[c]|near[d]
   h=hardbits.bit_count();n=nearbits.bit_count();margin=h-n
   checked+=1;hist[(h,n)]+=1
   f.write(f'{i}\t{j}\t{h}\t{n}\t{margin}\n')
   if margin<margin_min:
    margin_min=margin;minw={'edgeindices':[i,j],'cuts':[[a,b],[c,d]],'P':[a,b,c,d],'hard_owner_count':h,'hard_owner_ports':[ports[k]for k in range(28)if hardbits>>k&1],'near_port_count':n,'near_ports':[ports[k]for k in range(28)if nearbits>>k&1]}
   if margin<=0 and len(surv)<10:surv.append({'edgeindices':[i,j],'cuts':[[a,b],[c,d]],'hard':h,'near':n})
expected=630*629//2-sum(len([u for u in adj[v]if u not in ps])*(len([u for u in adj[v]if u not in ps])-1)//2 for v in cores)
assert expected==196371
if completed:assert checked==expected and shared==1764
survivor_count=sum(v for (h,n),v in hist.items()if h<=n)
status='UNKNOWN_NATIVE_CPU_CAP' if not completed else ('COMPLETE_NO_ALL_TWO_CORECUTS_ALL_PORTMATCHINGS_BY_HALL' if survivor_count==0 else 'COMPLETE_HALL_GATE_WITH_SURVIVORS_NOT_YET_MATCHED')
result={'status':status,'domain':'allunorderedpairs ofvertexdisjointoriginalcorecoreedges in actualnatural364','expected_pair_count':expected,'actual_pairs_checked':checked,'shared_pairs_excluded':shared,'completed':completed,'prediction_all_hard_gt_near_supported':completed and survivor_count==0,'minimum_Hall_deficit':margin_min,'minimum_deficit_witness':minw,'hard_near_histogram':[{'hard':h,'near':n,'count':v}for(h,n),v in sorted(hist.items())],'Hall_survivor_count':survivor_count,'first_survivors':surv,'new_depth4_support_queries':332,'reused_support_queries':4,'source_D5_BFS_old28portballs_matching_solver_graph_oldroots_Lean_ARIS':0,'actual_native_CPU':time.process_time()-START,'prior_case_and_preparation_CPU':PRIOR,'case_CPU':PRIOR+time.process_time()-START,'case_cap':20,'scope':'fixednatural364source; all2disjointoriginalcorecuts + arbitrary28portperfectmatching + one4starP; nootheredits','new_accepted_graph_parameter_Lean':[0,0,0],'next':'STOP_REASSESS_NO_THIRD_CUT_OR_OTHER_SOURCE_AUTOMATIC','terminal':True}
save('RESULT.json',result);save('TERMINAL.json',result)
print(json.dumps(result,ensure_ascii=False),flush=True)
