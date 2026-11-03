from pathlib import Path
from collections import Counter
import json,subprocess,resource,time,sys,os
P=Path(__file__).resolve().parent;S=P.parent/'hexagon_partial_fold_scout';started=time.process_time();wall=time.monotonic()
D=json.loads((S/'Q_data.json').read_text());W=json.loads((S/'witness12_state.json').read_text());regions=json.loads((P/'regions.json').read_text());state=W['states'];cp=W['h3_extra_copies'];original_state=state.copy();original_cp=cp.copy()
Q=D['Q'];h_of=D['H3_neighbors'];HN=D['H3_graph'];HQ=D['H3_generic_neighbors'];absolute=D['H3_absolute']
def check(st,cc):
 if len(st)!=33033 or len(cc)!=364 or any(x not in (0,1,2) for x in st) or any(x not in (0,1,2) for x in cc):return None
 loads=[sum(st[v]!=0 if not st[u] else st[v]==st[u] for v in Q[u])+(cc[h_of[u]] if h_of[u]>=0 else 0) for u in range(33033)]
 hd=[7-int(absolute[h])+sum(st[u]!=0 for u in HQ[h])+sum(cc[k] for k in HN[h]) for h in range(364)]
 if max(loads)>2 or max(hd)>12:return None
 return loads,hd
assert check(state,cp) is not None
def objective(st,cc):return sum(x!=0 for x in st)+sum(cc)
records=[];hit=False
for i,reg in enumerate(regions):
 (P/'current_state.json').write_text(json.dumps(dict(states=state,h3_extra_copies=cp),separators=(',',':'))+'\n')
 before=objective(state,cp);r0=resource.getrusage(resource.RUSAGE_CHILDREN)
 out=P/f'region_{i}_stdout.txt';err=P/f'region_{i}_stderr.txt'
 with out.open('w') as of,err.open('w') as ef:
  try:run=subprocess.run([sys.executable,str(P/'worker.py'),str(i)],stdout=of,stderr=ef,timeout=13);returncode=run.returncode
  except subprocess.TimeoutExpired:returncode='WALL_LIMIT'
 r1=resource.getrusage(resource.RUSAGE_CHILDREN);cpu=r1.ru_utime+r1.ru_stime-r0.ru_utime-r0.ru_stime
 f=P/f'region_{i}_result.json'
 r=json.loads(f.read_text()) if f.exists() else dict(region=i,name=reg['name'],status='UNKNOWN_PROCESS_LIMIT',incumbent_returned=False)
 r.update(process_returncode=returncode,child_process_CPU_seconds=cpu,global_objective_before=before,accepted=False)
 if r.get('candidate_file'):
  c=json.loads((P/r['candidate_file']).read_text());candidate=c['states'];cc=c['h3_extra_copies'];checked=check(candidate,cc)
  R=set(reg['generic_ids']);H=set(reg['H3_ids']);outside_fixed=all(candidate[u]==state[u] for u in range(33033) if u not in R) and all(cc[h]==cp[h] for h in range(364) if h not in H)
  after=objective(candidate,cc);r.update(candidate_global_objective=after,direct_all_vertex_degree_check=checked is not None,outside_variables_fixed=outside_fixed)
  if checked is not None and outside_fixed and after>=before:
   r.update(accepted=True,objective_gain=after-before,deleted_splits=sum(state[u]!=0 and candidate[u]==0 for u in R),added_splits=sum(state[u]==0 and candidate[u]!=0 for u in R),recolored_splits=sum(state[u] and candidate[u] and state[u]!=candidate[u] for u in R),changed_H3_copy_variables=sum(cp[h]!=cc[h] for h in H))
   state=candidate;cp=cc
  else:r['reject_reason']='invalid degrees, nonlocal changes or lower objective'
 elif r.get('status')==2:
  r['unexpected_infeasible_despite_checked_baseline']=True
 r['global_order_after']=33397+objective(state,cp);records.append(r)
 print(json.dumps(dict(region=i,status=r['status'],incumbent=r['incumbent_returned'],accepted=r['accepted'],gain=r.get('objective_gain'),order=r['global_order_after'],CPU_seconds=cpu)),flush=True)
 if 33397+objective(state,cp)>=42343:hit=True;break
 if r.get('unexpected_infeasible_despite_checked_baseline'):break
loads,hd=check(state,cp);degrees=[]
for u,st in enumerate(state):degrees.extend([10+loads[u]]*(2 if st else 1))
for h in range(364):degrees.extend([hd[h]]*(1+cp[h]))
best=dict(states=state,state_meaning=['merged','split_color0','split_color1'],h3_extra_copies=cp,pad=[],split_fibers=sum(x!=0 for x in state),H3_extra_copies=sum(cp),core_order=len(degrees),max_degree=max(degrees),diameter_upper_bound=5,diameter_basis='author arbitrary-pairing partial-fold and H3-blowup theorems')
(P/'best_state.json').write_text(json.dumps(best,separators=(',',':'))+'\n')
(P/'best_loads.json').write_text(json.dumps(dict(generic_loads=loads,H3_copy_degrees=hd,direct_all_vertex_check=True),separators=(',',':'))+'\n')
total_child=sum(r['child_process_CPU_seconds'] for r in records)
result=dict(status='HIT_CORE_ABOVE_42342' if hit else 'FOUR_PREDETERMINED_JOINT_SUBPROBLEMS_TERMINAL',regions_planned=4,regions_attempted=len(records),sequential_regions=True,workers=1,initial_core_order=41636,best_core_order=len(degrees),gain_from_source_core=len(degrees)-41636,best_split_fibers=best['split_fibers'],best_H3_extra_copies=sum(cp),degree_histogram=dict(sorted(Counter(degrees).items())),free_degree_slots=sum(12-x for x in degrees),target_order=42343,regions=records,child_process_CPU_seconds=total_child,driver_CPU_seconds=time.process_time()-started,total_CPU_seconds=total_child+time.process_time()-started,wall_seconds=time.monotonic()-wall,explicit_large_graph_generated=False,full_BFS_performed=False,padding_twins_not_optimized=True)
(P/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='regions'},indent=2),flush=True)
