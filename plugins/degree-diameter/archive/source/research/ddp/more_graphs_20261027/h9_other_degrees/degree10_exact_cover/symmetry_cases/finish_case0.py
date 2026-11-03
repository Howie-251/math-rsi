"""Finish the unresolved LP slice and at most one MIP within the original batch CPU budget."""
import os
for n in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[n]='1'
import resource,time,json,warnings,sys
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(98,98))
t0=time.process_time();wall=time.perf_counter();H=Path(__file__).resolve().parent;E=H.parent;B=E.parent;ROOT=H.parents[5]
sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen

def save(p,x):
 def s(z):
  if isinstance(z,str):return[z]
  if isinstance(z,dict):return[t for v in z.values() for t in s(v)]
  if isinstance(z,(tuple,list)):return[t for v in z for t in s(v)]
  return[]
 assert not screen('\n'.join(s(x)));p.write_text(json.dumps(x,indent=2)+'\n')
old=json.loads((H/'terminal.json').read_text());assert old['MIP_calls']==0 and old['measured_process_CPU_seconds']<20
save(H/'early_terminal.json',old)
save(H/'FINISH_CASE0_SCOPE.json',dict(reason='The first driver stopped after a conservative8second LP subwindow although over100CPU of the original authorized batch remained. Preserve that history and finish only the still unresolved case0 without changing constraints.',
 original_total_CPU_cap=120,first_process_CPU=old['measured_process_CPU_seconds'],new_process_hard_CPU=98,
 new_MIP_calls_max=1,new_cases=0,model_unchanged=True,no_extra_symmetry_fix=True))
import numpy as np
from scipy.sparse import csr_matrix,vstack
from scipy.optimize import linprog,milp,Bounds,LinearConstraint
p=H/'case0';m=json.loads((p/'model.json').read_text());free=m['free_columns'];ones=m['fixed_one_columns'];cap=m['remaining_pin_cap'];R=m['deduplicated_remaining_rows'];C=len(free)
U=np.unpackbits(np.frombuffer((p/'rows.u8.bin').read_bytes(),dtype=np.uint8).reshape(R,m['row_bytes']),axis=1,bitorder='little')[:,:C]
A=csr_matrix(U,dtype=float)
t=time.process_time()
with warnings.catch_warnings(record=True) as w:
 warnings.simplefilter('always');lp=linprog(np.ones(C),A_ub=-A,b_ub=-np.ones(R),bounds=(0,None),method='highs',options={'time_limit':25.,'threads':1})
lpd=dict(status=int(lp.status),message=str(lp.message),remaining_objective=None if lp.fun is None else float(lp.fun),total_objective=None if lp.fun is None else len(ones)+float(lp.fun),CPU_seconds=time.process_time()-t,time_limit=25.,warnings=[str(z.message) for z in w])
save(p/'LP_completion_result.json',lpd);print('LP '+json.dumps(lpd),flush=True)
strict=False;hit=None;mr=None
if lp.status==0:
 weights=np.floor(np.maximum(0,-lp.ineqlin.marginals)*1000000).astype(np.int64)
 loads=np.asarray(A.T@weights).reshape(-1).astype(np.int64);den=max(1000000,int(loads.max(initial=0)));total=int(weights.sum());strict=total>cap*den
 if strict:save(p/'integer_dual.json',dict(denominator=den,total_row_weight=total,fixed_one_count=len(ones),remaining_pin_cap=cap,strictly_excludes_remaining_cap=True,weighted_reduced_rows=[[int(i),int(w)] for i,w in enumerate(weights) if w],per_free_column_loads=loads.tolist(),proof='Every remaining cover has denominator times sum(x) at least totalrowweight.'))
if strict:status='EXACT_INTEGER_DUAL_INFEASIBLE'
elif lp.status!=0:status='LP_COMPLETION_UNKNOWN_NO_MIP'
elif lp.fun>cap+1e-7:status='FLOAT_LP_BOUND_EXCLUDES_NO_INTEGER_CERTIFICATE'
else:
 limit=max(.1,93.-(time.process_time()-t0));t=time.process_time();M=vstack([A,np.ones((1,C))],format='csc')
 save(H/'terminal.json',dict(status='RUNNING_ONLY_CASE0_MIP',original_batch=True,prior_cases_exactly_excluded=[1,2,3,4],incumbent=False,time_limit=limit,prior_process_CPU=old['measured_process_CPU_seconds']))
 print('START_MIP '+json.dumps(dict(case=0,time_limit=limit,LP_total=lpd['total_objective'])),flush=True)
 with warnings.catch_warnings(record=True) as w:
  warnings.simplefilter('always');ans=milp(np.zeros(C),integrality=np.ones(C),bounds=Bounds(0,1),constraints=LinearConstraint(M,np.r_[np.ones(R),-np.inf],np.r_[np.full(R,np.inf),cap]),options={'threads':1,'time_limit':limit,'presolve':True,'disp':False})
 mr=dict(status=int(ans.status),message=str(ans.message),CPU_seconds=time.process_time()-t,time_limit=limit,incumbent=ans.x is not None,warnings=[str(z.message) for z in w],node_count=getattr(ans,'mip_node_count',None));save(p/'MIP_result.json',mr)
 if ans.x is not None:
  x=np.rint(ans.x).astype(int);assert np.max(abs(ans.x-x))<1e-5 and np.all((x==0)|(x==1));assert np.all(A@x>=1) and x.sum()<=cap
  selected=sorted(ones+[free[i] for i in np.flatnonzero(x)]);assert len(selected)<=10
  model=json.loads((E/'model.json').read_text());pins=[model['pins'][c] for c in selected];N=33397;W=(N+63)//64;raw=(B/'degree10_radius4.u64.bin').read_bytes();assert len(raw)==364*W*8;union=0
  for c in selected:union|=int.from_bytes(raw[c*W*8:(c+1)*W*8],'little')
  assert union&((1<<N)-1)==(1<<N)-1
  deg=[0]*N
  with (B/'degree10_source.edges').open() as f:
   n,edges=map(int,next(f).split());assert(n,edges)==(N,166425)
   for line in f:
    a,b=map(int,line.split());deg[a]+=1;deg[b]+=1
  assert all(deg[z]<10 for z in pins)
  hit=dict(case=0,pins=pins,selected_columns=selected,source_n=N,target_n=N+1,new_vertex=N,new_vertex_degree=len(pins),old_pin_degrees=[deg[z] for z in pins],all33397_original_R4_targets_covered=True,missing_targets=[],source_edges_retained=True,source_file=str((B/'degree10_source.edges').relative_to(ROOT)),graph_generated=False,root_fullgraph_verification_pending=True)
  save(H/'hit.json',hit);print('HIT '+json.dumps(hit),flush=True);status='FEASIBLE_FULL_COVER_VERIFIED_AWAIT_ROOT'
 else:status='RAW_MIP_INFEASIBLE_NO_TRUSTED_CERTIFICATE' if ans.status==2 else 'MIP_UNKNOWN_NO_INCUMBENT'
c0=json.loads((p/'RESULT.json').read_text());c0['initial_LP_unknown']=c0['LP'];c0.update(status=status,LP=lpd,LP_calls=2,MIP_calls=int(mr is not None),MIP=mr,incumbent=hit is not None,completion_process_CPU=time.process_time()-t0);save(p/'RESULT.json',c0)
result=json.loads((H/'RESULT.json').read_text());result['cases']=[c0 if c['case']==0 else c for c in result['cases']]
result.update(status='FEASIBLE_FULL_COVER_FOUND_AWAIT_ROOT' if hit else ('ALL_FIVE_CASES_EXACT_INTEGER_DUAL_EXCLUDED' if strict else 'FIVE_CASE_BATCH_FINISHED_NO_INCUMBENT'),incumbent=hit is not None,pins=None if not hit else hit['pins'],LP_calls=6,MIP_calls=int(mr is not None),whole_family_excluded=strict,completion_process_CPU=time.process_time()-t0,original_batch_total_CPU=old['measured_process_CPU_seconds']+time.process_time()-t0,completion_wall=time.perf_counter()-wall)
save(H/'RESULT.json',result);save(H/'terminal.json',result);print('FINAL '+json.dumps({k:v for k,v in result.items() if k!='cases'}),flush=True)
