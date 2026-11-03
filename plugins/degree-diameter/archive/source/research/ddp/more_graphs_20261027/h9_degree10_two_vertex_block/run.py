"""Complete adjacent-two-new-vertices cover model; no assumed column symmetry."""
import os
for n in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[n]='1'
import resource,time,json,sys,warnings
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(115,115))
t0=time.process_time();wall=time.perf_counter();H=Path(__file__).resolve().parent;B=H.parent/'h9_other_degrees';ROOT=H.parents[3]
sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen

def save(name,value):
 def strings(x):
  if isinstance(x,str):return[x]
  if isinstance(x,dict):return[s for y in x.values() for s in strings(y)]
  if isinstance(x,(list,tuple)):return[s for y in x for s in strings(y)]
  return[]
 assert not screen('\n'.join(strings(value)));(H/name).write_text(json.dumps(value,indent=2)+'\n')
assert not (H/'terminal.json').exists(),'One-shot two-point batch already has terminal data'
import numpy as np
from scipy.optimize import linprog,milp,LinearConstraint,Bounds
from scipy.sparse import csr_matrix,hstack,vstack
N=33397;C=364;W=(N+63)//64
meta=json.loads((H/'radius3.json').read_text());cap=json.loads((B/'degree10_capacity.json').read_text());pins=meta['pins'];assert pins==cap['available_vertices']
r3=(H/'radius3.u64.bin').read_bytes();r4=(B/'degree10_radius4.u64.bin').read_bytes();assert len(r3)==len(r4)==C*W*8
U3=np.unpackbits(np.frombuffer(r3,dtype=np.uint8).reshape(C,W*8),axis=1,bitorder='little')[:,:N].T
U4=np.unpackbits(np.frombuffer(r4,dtype=np.uint8).reshape(C,W*8),axis=1,bitorder='little')[:,:N].T
assert np.all(U3<=U4)
# Store each ordered pair as two independently padded46byte coverer sets.
packed=np.hstack([np.packbits(U4,axis=1,bitorder='little'),np.packbits(U3,axis=1,bitorder='little')]);unique,rep,inv=np.unique(packed,axis=0,return_index=True,return_inverse=True)
(H/'ordered_pair_rows.u8.bin').write_bytes(unique.tobytes());R=len(unique)
A4=csr_matrix(U4[rep],dtype=float);A3=csr_matrix(U3[rep],dtype=float);S=A4+A3
counts3,hist3=np.unique(U3.sum(axis=1),return_counts=True)
save('model.json',dict(source_n=N,source_m=166425,target_n=N+2,target_Delta=10,target_D=5,pins=pins,
 binary_variables=2*C,variable_order='First364 x=A neighbors, next364 y=B neighbors',each_pin_cap=9,
 oldtarget_constraints_before_dedup=2*N,ordered_pair_rows=R,coverage_rows_after_pair_dedup=2*R,
 pair_row_file='ordered_pair_rows.u8.bin',pair_row_bytes=92,pair_row_layout='46littlebitorder bytes for R4coverers followed by46littlebitorder bytes for R3coverers',
 representative_oldtargets=rep.tolist(),target_to_pairrow=inv.tolist(),R3_coverer_count_histogram={str(int(a)):int(b) for a,b in zip(counts3,hist3)},
 constraints=['R4_x(target)+R3_y(target)>=1','R3_x(target)+R4_y(target)>=1','sumx<=9','sumy<=9'],
 old_R4_only_symmetry_used=False,extra_pin_fixings=[],
 LP_projection_proof='For any fractional feasible x,y let t=x+y. Adding the two cover inequalities gives (R4+R3)t>=2, bounds give0<=t<=2 and total<=18. Conversely any such t gives x=y=t/2, which satisfies each original inequality and each sum<=9. Thus min total in this364variable LP is exactly the full728variable LP optimum. This averaging is not an integer symmetry restriction.'))
save('terminal.json',dict(status='RUNNING_ONE_LP',LP_calls=1,MIP_calls=0,incumbent=False))
t=time.process_time()
with warnings.catch_warnings(record=True) as warns:
 warnings.simplefilter('always');lp=linprog(np.ones(C),A_ub=-S,b_ub=-np.full(R,2.),bounds=(0,2),method='highs',options={'time_limit':25.,'threads':1})
lpd=dict(status=int(lp.status),message=str(lp.message),objective=None if lp.fun is None else float(lp.fun),CPU_seconds=time.process_time()-t,
 time_limit=25.,variables=C,cover_rows=R,max_t=None if lp.x is None else float(lp.x.max()),warnings=[str(w.message) for w in warns])
save('LP_result.json',lpd);print('LP '+json.dumps(lpd),flush=True)
strict=False;dual=None
if lp.status==0:
 y=np.floor(np.maximum(0,-lp.ineqlin.marginals)*1000000).astype(np.int64);loads=np.asarray(S.T@y).reshape(-1).astype(np.int64);D=1000000;z=np.maximum(0,loads-D);num=int(2*y.sum()-2*z.sum());strict=num>18*D
 dual=dict(denominator=D,lower_bound_numerator=num,strictly_excludes_total18=strict,
 positive_row_weights=[[int(i),int(v)] for i,v in enumerate(y) if v],per_column_loads=loads.tolist(),per_column_upper_penalties=z.tolist(),
 proof='Multiply covering rows by positive integer weights. For0<=t<=2,2sumweights<=sumload*t<=Dsumt+2sumpositive(load-D). Thus Dsumt>=numerator.')
 save('integer_LP_dual.json',dual)
mr=None;hit=None
if strict:status='EXACT_INTEGER_LP_DUAL_EXCLUDES_WHOLE_TWO_VERTEX_MODEL'
elif lp.status==2:status='RAW_LP_INFEASIBLE_NO_TRUSTED_CERTIFICATE'
elif lp.status!=0:status='LP_UNKNOWN_NO_MIP'
elif lp.fun>18+1e-7:status='FLOAT_LP_EXCLUDES_NO_INTEGER_CERTIFICATE'
else:
 t=time.process_time()
 M=vstack([hstack([A4,A3],format='csr'),hstack([A3,A4],format='csr'),
   csr_matrix(np.r_[np.ones(C),np.zeros(C)][None,:]),csr_matrix(np.r_[np.zeros(C),np.ones(C)][None,:])],format='csc')
 lb=np.r_[np.ones(2*R),-np.inf,-np.inf];ub=np.r_[np.full(2*R,np.inf),9.,9.]
 limit=max(.1,108.-(time.process_time()-t0));save('terminal.json',dict(status='RUNNING_ONE_MIP',LP_calls=1,MIP_calls=1,incumbent=False,LP_objective=lpd['objective'],time_limit=limit))
 print('START_MIP '+json.dumps(dict(time_limit=limit,vars=2*C,rows=2*R+2,LP_objective=lpd['objective'])),flush=True)
 with warnings.catch_warnings(record=True) as warns:
  warnings.simplefilter('always');ans=milp(np.zeros(2*C),integrality=np.ones(2*C),bounds=Bounds(0,1),constraints=LinearConstraint(M,lb,ub),options={'time_limit':limit,'threads':1,'presolve':True,'disp':False})
 mr=dict(status=int(ans.status),message=str(ans.message),CPU_seconds=time.process_time()-t,time_limit=limit,incumbent=ans.x is not None,
 node_count=getattr(ans,'mip_node_count',None),warnings=[str(w.message) for w in warns]);save('MIP_result.json',mr)
 if ans.x is not None:
  x=np.rint(ans.x).astype(int);assert np.max(abs(ans.x-x))<1e-5 and np.all((x==0)|(x==1));assert np.all(M@x>=lb-1e-8) and np.all(M@x<=ub+1e-8)
  ai=np.flatnonzero(x[:C]).tolist();bi=np.flatnonzero(x[C:]).tolist();A=[pins[i] for i in ai];BB=[pins[i] for i in bi];assert len(A)<=9 and len(BB)<=9
  def union(raw,idx):
   out=0
   for i in idx:out|=int.from_bytes(raw[i*W*8:(i+1)*W*8],'little')
   return out
  full=(1<<N)-1;coverZ=union(r4,ai)|union(r3,bi);coverW=union(r3,ai)|union(r4,bi);assert coverZ&full==full and coverW&full==full
  deg=[0]*N
  with (B/'degree10_source.edges').open() as f:
   n,m=map(int,next(f).split());assert (n,m)==(N,166425)
   for line in f:
    u,v=map(int,line.split());deg[u]+=1;deg[v]+=1
  adds={p:int(p in A)+int(p in BB) for p in set(A)|set(BB)};assert all(deg[p]+n<=10 for p,n in adds.items())
  hit=dict(source_n=N,target_n=N+2,source_m=166425,target_m=166426+len(A)+len(BB),
    A=A,B=BB,new_vertices=[N,N+1],new_edge=[N,N+1],new_vertex_full_neighbors={str(N):A+[N+1],str(N+1):BB+[N]},
    new_degrees=[1+len(A),1+len(BB)],old_pin_degree_after={str(p):deg[p]+v for p,v in adds.items()},
    full33397targets_R4A_union_R3B=True,full33397targets_R3A_union_R4B=True,missingZ=[],missingW=[],
    full_original_ball_matrix_recheck=True,source_edges_retained=True,source_file=str((B/'degree10_source.edges').relative_to(ROOT)),
    new_graph_generated=False,root_wholegraph_verification_pending=True)
  save('hit.json',hit);print('HIT '+json.dumps(hit),flush=True);status='COMPLETE_TWO_VERTEX_COVER_FOUND_AWAIT_ROOT'
 else:status='RAW_MIP_INFEASIBLE_NO_TRUSTED_CERTIFICATE' if ans.status==2 else 'UNKNOWN_NO_INCUMBENT_WINDOW_CLOSED'
final=dict(status=status,incumbent=hit is not None,source_n=N,target_n=N+2,target_Delta=10,target_D=5,
 LP_calls=1,MIP_calls=int(mr is not None),LP=lpd,MIP=mr,ordered_pair_rows=R,binary_variables=2*C,
 whole_fixedsource_two_vertex_model_excluded=bool(strict),total_process_CPU_seconds=time.process_time()-t0,total_wall_seconds=time.perf_counter()-wall,
 radius3_CPU_seconds=meta['CPU_seconds'],total_known_native_and_solver_CPU=time.process_time()-t0+meta['CPU_seconds'],
 bounded_R3_balls_new=364,R4_balls_reused=364,new_allsource_BFS=0,new_graphs=0,new_lower_bounds=0,workers=1,solver_threads=1,
 old_R4_only_symmetry_used=False,extra_pin_fixings=[],no_new_point_required_to_form_valid_intermediate_graph=True)
save('RESULT.json',final);save('terminal.json',final);print('FINAL '+json.dumps(final),flush=True)
