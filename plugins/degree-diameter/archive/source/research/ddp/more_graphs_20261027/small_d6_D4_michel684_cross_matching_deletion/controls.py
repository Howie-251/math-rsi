"""Exactly3 cross-matching deletions. No old-source BFS or recipe import."""
import resource
resource.setrlimit(resource.RLIMIT_CPU,(13,13))
from pathlib import Path
from collections import deque,Counter
import json,time
OUT=Path(__file__).resolve().parent;SOURCE=Path('research/ddp/m1_sources/684_recovered_construction.json');start=time.process_time();src=json.loads(SOURCE.read_text())
M,N,R=src['m'],src['n'],src['r'];assert(M,N,R)==(38,9,23)
V=src['voltage_sets'];S0=[tuple(x) for x in V[0][0]];S1=[tuple(x) for x in V[1][1]];cross=[tuple(x) for x in V[0][1]]
assert cross==[(2,2),(2,6),(24,3)] and len(S0)==len(S1)==4 and pow(R,N,M)==1
rp=[pow(R,j,M) for j in range(N)]
def inv(g):a,b=g;return(-rp[-b%N]*a%M,-b%N)
assert set(map(inv,S0))==set(S0) and set(map(inv,S1))==set(S1) and list(map(inv,cross))==[tuple(x) for x in V[1][0]]
def encode(side,a,b):return side*M*N+a*N+b
def coord(v):side,v=divmod(v,M*N);a,b=divmod(v,N);return {'side':side,'normal':a,'phase':b}
def save(name,obj):(OUT/name).write_text(json.dumps(obj,indent=2)+'\n')
save('SOURCE_INPUT.json',{'source_file':str(SOURCE),'source_reconstruction_andD4':'Inherited existing684 exactrecipe binding; recover_684.py was not imported or executed','m':M,'n':N,'r':R,'law':'(a,b)*(c,d)=(a+r^b*c mod38,b+d mod9)','vertex_id':'side*342+normal*9+phase','internal0':S0,'internal1':S1,'cross0to1':cross,'inverse_cross1to0':list(map(inv,cross)),'published_source_D':4,'source_D_BFS_repeated':False,'roots_representative':[0,342]})
def build(keep):
 ss=[[S0,keep],[list(map(inv,keep)),S1]];adj=[[] for _ in range(684)]
 for side in range(2):
  for a in range(M):
   for j in range(N):
    u=encode(side,a,j)
    for target in range(2):
     for c,d in ss[side][target]:adj[u].append(encode(target,(a+rp[j]*c)%M,(j+d)%N))
 for u,a in enumerate(adj):
  assert len(a)==len(set(a))==6 and u not in a and all(u in adj[v] for v in a);a.sort()
 edges=[(u,v) for u,a in enumerate(adj) for v in a if u<v];assert len(edges)==2052
 return adj,edges

def radius(adj,root):
 dist=[-1]*684;dist[root]=0;q=deque([root])
 while q:
  u=q.popleft()
  if dist[u]==4:continue
  for v in adj[u]:
   if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
 hist=Counter(d for d in dist if d>=0);missing=[v for v,d in enumerate(dist) if d<0];slots=[]
 for side in range(2):
  for phase in range(9):
   covered=[a for a in range(38) if dist[encode(side,a,phase)]>=0];miss=[a for a in range(38) if dist[encode(side,a,phase)]<0]
   slots.append({'side':side,'phase':phase,'target_count':38,'covered':len(covered),'missing':len(miss),'missing_normals':miss})
 return {'root':root,'root_coordinates':coord(root),'radius':4,'R4_histogram':[hist[d] for d in range(5)],'covered':684-len(missing),'missing':len(missing),'first_missing_id':missing[0] if missing else None,'first_missing_coordinates':coord(missing[0]) if missing else None,'minimum_slot_coverage':min(s['covered'] for s in slots),'slots':slots,'all_missing_ids':missing,'actual_global_D':None,'ordinary_bad_unordered_pairs':None}

cases=[];hit=None;rootchecks=0
with (OUT/'CASES.jsonl').open('w') as log:
 for i,deleted in enumerate(cross):
  keep=[g for j,g in enumerate(cross) if j!=i];adj,edges=build(keep)
  (OUT/f'case_{i}.edges').write_text('684 2052\n'+''.join(f'{u} {v}\n' for u,v in edges))
  roots=[]
  for root in [0,342]:
   rr=radius(adj,root);rootchecks+=1;roots.append(rr);save(f'case_{i}_root_{root}.json',rr)
   if rr['missing']:break
  passed=len(roots)==2 and all(not r['missing'] for r in roots)
  case={'case':i,'deleted_cross_voltage':deleted,'deleted_inverse_voltage':inv(deleted),'retained_cross_voltages':keep,'n':684,'m':2052,'degree':6,'simple':True,'matching_edges_removed':342,'roots_checked':[r['root'] for r in roots],'R4_records':[{k:v for k,v in rr.items() if k not in ['slots','all_missing_ids']} for rr in roots],'root_files':[f'case_{i}_root_{rr["root"]}.json' for rr in roots],'second_root_state':'CHECKED' if len(roots)==2 else 'NOT_NEEDED_AFTER_FIRST_ROOT_FAIL','connected':True if passed else None,'status':'HIT_D4_PENDING_PARENT' if passed else 'IDENTITY_ROOT_R4_FAIL','actual_global_D':4 if passed else None,'ordinary_bad_unordered_pairs':None}
  cases.append(case);log.write(json.dumps(case)+'\n');log.flush()
  save('checkpoint.json',{'status':'HIT' if passed else 'RUNNING','completed_cases':len(cases),'planned_cases':3,'root_R4_checks':rootchecks,'CPU_seconds':time.process_time()-start})
  if passed:
   hit=case;(OUT/'candidate684.edges').write_text((OUT/f'case_{i}.edges').read_text());save('HIT.json',case);save('PARAMETERS.json',{'source':'SOURCE_INPUT.json','deleted_cross_voltage':deleted,'retained_cross_voltages':keep,'law':'(a,b)*(c,d)=(a+23^b*c mod38,b+d mod9)','encoding':'side*342+normal*9+phase','roots':[0,342]});break
r={'status':'HIT_STOP_REMAINDER_UNTESTED' if hit else 'COMPLETE_ALL3_CROSS_DELETIONS_NO_D4','prediction':'SUPPORTED_PRODUCER_PENDING_PARENT' if hit else 'REFUTED_COMPLETE_FIXED_THREE_CONTROLS','target_Delta':6,'target_D':4,'savedL':441,'n':684,'m':2052,'actual_graph_degree':6,'controls_planned':3,'controls_completed':len(cases),'controls_untested':3-len(cases),'actual_candidate_graphs':len(cases),'actual_identity_root_R4_checks':rootchecks,'hits':int(hit is not None),'actual_global_D':4 if hit else None,'ordinary_bad_unordered_pairs':None,'cases':cases,'CPU_seconds':time.process_time()-start,'source_BFS':0,'fullglobalD_BFS':0,'solver_calls':0,'changed_voltage_phase_seed':False,'scope':'Exactly the3 original crossmatching deletions at unchangedm38/n9/r23. Not other6regular684graphs or allsource surgeries.'}
save('WORKER_RESULT.json',r);save('checkpoint.json',{'status':r['status'],'controls_completed':len(cases),'controls_untested':r['controls_untested'],'actual_root_R4_checks':rootchecks});print(json.dumps(r),flush=True)
