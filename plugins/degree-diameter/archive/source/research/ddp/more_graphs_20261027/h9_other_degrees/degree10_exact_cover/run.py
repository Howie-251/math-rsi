"""One exact all364pin cover feasibility model, with a preceding LP and integer dual check."""
import os
for n in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[n]='1'
import resource
resource.setrlimit(resource.RLIMIT_CPU,(120,120))
from pathlib import Path
from datetime import datetime,timezone
import json,sys,time,warnings,math
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[4];BASE=HERE.parent
sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen
start=time.process_time();wall=time.perf_counter()
def save(fn,x):
 def strings(z):
  if isinstance(z,str):return[z]
  if isinstance(z,dict):return[s for y in z.values() for s in strings(y)]
  if isinstance(z,(list,tuple)):return[s for y in z for s in strings(y)]
  return[]
 assert not screen('\n'.join(strings(x)))
 (HERE/fn).write_text(json.dumps(x,indent=2)+'\n')
assert not (HERE/'terminal.json').exists(),'One-shot task already has terminal data'
save('PREDICTION.json',dict(status='FROZEN_BEFORE_LP_OR_MIP',timestamp=datetime.now(timezone.utc).isoformat(),
 prediction_id='N10_FULL364_EXACT10PIN_COVER',hypothesis='The fixednonregular33397source mayadmit some<=10oldpinscoveringall33397targets; testtheentire364pinspace withoutsymmetryorsearchseeds.',
 target_Delta=10,target_D=5,source_n=33397,target_n=33398,
 scope='All364degree<10oldvertices, completeR4cover inequalities, cardinality<=10; no prespecifiedpins,groupfixedpoints,newsourceornewnewhelpers.',
 budgets='OneLP then atmostoneMIP; wholeprocess hard120CPU, singlethread, no continuation.'))
import numpy as np
from scipy.optimize import linprog,milp,Bounds,LinearConstraint
from scipy.sparse import csr_matrix,vstack
cap=json.loads((BASE/'degree10_capacity.json').read_text());N=cap['n'];P=cap['available_vertices'];C=len(P);W=(N+63)//64
assert N==33397 and C==364
raw=(BASE/'degree10_radius4.u64.bin').read_bytes();assert len(raw)==C*W*8
rows=np.unpackbits(np.frombuffer(raw,dtype=np.uint8).reshape(C,W*8),axis=1,bitorder='little')[:,:N].T
packed=np.packbits(rows,axis=1,bitorder='little');unique,representatives,inverse=np.unique(packed,axis=0,return_index=True,return_inverse=True)
U=np.unpackbits(unique,axis=1,bitorder='little')[:,:C];assert np.all(U.sum(axis=1)>0)
A=csr_matrix(U,dtype=float);R=A.shape[0]
(HERE/'unique_cover_rows.u8.bin').write_bytes(unique.tobytes())
save('model.json',dict(source_n=N,pins=P,binary_variables=C,target_rows_before_dedup=N,unique_cover_rows=R,
 row_bytes=unique.shape[1],row_layout='littlebitorder, ascending364pinindices',row_file='unique_cover_rows.u8.bin',
 representative_source_targets=representatives.tolist(),target_to_unique_row=inverse.tolist(),coverage_rhs=1,pin_cardinality_at_most=10,
 unproved_symmetry_constraints=[]))
save('terminal.json',dict(status='RUNNING_ONE_LP',LP_calls=1,MILP_calls=0,incumbent=False))
t0=time.process_time()
with warnings.catch_warnings(record=True) as warns:
 warnings.simplefilter('always')
 lp=linprog(np.ones(C),A_ub=-A,b_ub=-np.ones(R),bounds=(0,None),method='highs',options={'time_limit':15.0,'threads':1})
lpCPU=time.process_time()-t0
lpd=dict(status=int(lp.status),message=str(lp.message),objective=float(lp.fun) if lp.fun is not None else None,CPU_seconds=lpCPU,
 warnings=[str(w.message) for w in warns],cover_rows=R)
save('LP_result.json',lpd)
# A rational integer dual is useful only if it actually proves the strict10threshold.
dual_closed=False
if lp.status==0:
 y=np.maximum(0,-lp.ineqlin.marginals)
 D=1000000;weights=np.floor(y*D).astype(np.int64)
 colloads=np.asarray(A.T@weights).reshape(-1).astype(np.int64)
 denom=max(D,int(colloads.max()));total=int(weights.sum())
 assert np.all(colloads<=denom) and np.all(weights>=0)
 dual_closed=total>10*denom
 save('integer_dual.json',dict(valid=True,denominator=denom,total_row_weight=total,
   strict_proves_more_than10=dual_closed,weighted_rows=[dict(unique_row=i,source_target=int(representatives[i]),weight=int(w)) for i,w in enumerate(weights) if w],
   per_pin_column_loads=colloads.tolist(),proof='Foranycover x>=0, sumweights<=sum_a columnload_a*x_a<=denominator*sum_a x_a.'))
if dual_closed:
 final=dict(status='EXACT_INTEGER_DUAL_EXCLUDES10PIN_COVER',incumbent=False,LP_calls=1,MILP_calls=0,
  integer_dual_lower_bound=dict(numerator=total,denominator=denom),source_n=N,target_n=N+1,
  scope='Wholefixed33397source onevertexextension with<=10oldpins; coveredR4matrixisthereusedboundedBFSdata, no generalgraphupperbound.',
  new_graphs=0,new_lower_bounds=0)
elif lp.status!=0:
 final=dict(status='LP_UNKNOWN_NO_MIP_STARTED',incumbent=False,LP_calls=1,MILP_calls=0,scope='Noimpossibilityclaim;timeboundLPdidnotdecide.',new_graphs=0,new_lower_bounds=0)
else:
 save('terminal.json',dict(status='RUNNING_ONE_MIP',LP_calls=1,MILP_calls=1,incumbent=False,LP_objective=lpd['objective']))
 M=vstack([A,np.ones((1,C))],format='csc');lb=np.r_[np.ones(R),-np.inf];ub=np.r_[np.full(R,np.inf),10.]
 tlim=max(1.0,113.0-(time.process_time()-start));t0=time.process_time()
 with warnings.catch_warnings(record=True) as warns:
  warnings.simplefilter('always')
  answer=milp(np.zeros(C),integrality=np.ones(C),bounds=Bounds(0,1),constraints=LinearConstraint(M,lb,ub),
              options={'time_limit':tlim,'threads':1,'presolve':True,'disp':True})
 mr=dict(status=int(answer.status),message=str(answer.message),CPU_seconds=time.process_time()-t0,
   time_limit=tlim,incumbent=answer.x is not None,warnings=[str(w.message) for w in warns])
 save('MIP_result.json',mr)
 if answer.x is not None:
  x=np.rint(answer.x).astype(int);assert np.max(abs(answer.x-x))<1e-5 and np.all((x==0)|(x==1))
  selected=np.flatnonzero(x);assert len(selected)<=10 and np.all(A@x>=1)
  balls=[int.from_bytes(raw[i*W*8:(i+1)*W*8],'little') for i in selected]
  union=0
  for b in balls:union|=b
  assert union&((1<<N)-1)==(1<<N)-1
  pins=[P[i] for i in selected]
  # Degrees are read from the original known edge source; no newBFS.
  degrees=[0]*N
  with (BASE/'degree10_source.edges').open() as f:
   n,m=map(int,next(f).split());assert(n,m)==(N,166425)
   for line in f:
    u,v=map(int,line.split());degrees[u]+=1;degrees[v]+=1
  assert all(degrees[p]<10 for p in pins)
  hit=dict(target_n=N+1,new_vertex=N,pins=pins,new_vertex_degree=len(pins),old_pin_degrees=[degrees[p] for p in pins],
   all_source_vertices_R4_covered=True,missing_targets=[],source_edges_retained=True,source_file=str((BASE/'degree10_source.edges').relative_to(ROOT)),
   source_old_D5_basis='Knowngeometric33397fold; finalnewgraph requiresrootuniqueallsourcecheck',new_graph_generated=False)
  save('hit.json',hit)
  final=dict(status='FEASIBLE_EXACT10PIN_COVER_FOUND_AWAIT_ROOT_GRAPH',incumbent=True,pins=pins,LP_calls=1,MILP_calls=1,
    new_graphs=0,new_lower_bounds=0,pending=['rootgenerategraphandindependentallsourceBFS'])
 else:
  final=dict(status='RAW_MIP_INFEASIBLE_NO_TRUSTED_CERTIFICATE' if answer.status==2 else 'UNKNOWN_NO_INCUMBENT_WINDOW_CLOSED',
    incumbent=False,LP_calls=1,MILP_calls=1,new_graphs=0,new_lower_bounds=0,pending=[])
final.update(LP_objective=lpd['objective'],unique_cover_rows=R,total_CPU_seconds=time.process_time()-start,
 total_wall_seconds=time.perf_counter()-wall,workers=1,BFS_repeated=False,solver_threads=1)
save('terminal.json',final);print(json.dumps(final,indent=2),flush=True)
