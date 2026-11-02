"""One bounded full four-guard binary cover model from saved native masks."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
import json,pathlib,resource,time,warnings
P=pathlib.Path(__file__).resolve().parent;START=time.process_time();WALL=time.monotonic()
resource.setrlimit(resource.RLIMIT_CPU,(29,30))
import numpy as np
from scipy.optimize import Bounds,LinearConstraint,milp
from scipy.sparse import csc_matrix,vstack
r=json.loads((P/'prepared.json').read_text());T=len(r['missing']);K=len(r['representatives']);W=r['mask_words_per_row']
assert T==750 and K==13026 and not r['zero_cover_targets']
raw=np.fromfile(P/'prepared.masks.u64.bin',dtype=np.uint8).reshape(K,W*8)
cover=np.unpackbits(raw,axis=1,bitorder='little')[:,:T].T
M=vstack([csc_matrix(cover),csc_matrix(np.ones((1,K)))],format='csc')
M.indices=M.indices.astype(np.int32);M.indptr=M.indptr.astype(np.int32)
model={'status':'MODEL_READY_ONE_MIP','source_n':r['source_n'],'source_m':r['source_m'],'mandatory':r['pins'],'old_missing_targets':T,'unique_anchor_columns':K,'full_eligible_anchors':r['eligible_anchors'],'guards_limit':4,'binary_variables':K,'cover_rows':T,'cardinality_rows':1,'matrix_nnz':int(M.nnz),'LP_calls':0,'MIP_calls':1,'time_limit_seconds':25,'threads':1,'CPU_before_solver':time.process_time()-START,'source_mask_format':'native little-index uint64 rows; reps order from prepared.json','normalization':'identical nonzero guard masks represented by smallest eligible label; repeated identical masks never improve a cover'}
(P/'MIP_MODEL.json').write_text(json.dumps(model,indent=2)+'\n');print(json.dumps(model),flush=True)
t0=time.process_time();w0=time.monotonic()
with warnings.catch_warnings(record=True) as ws:
 warnings.simplefilter('always')
 ans=milp(c=np.zeros(K),integrality=np.ones(K),bounds=Bounds(np.zeros(K),np.ones(K)),constraints=LinearConstraint(M,np.r_[np.ones(T),0.],np.r_[np.full(T,np.inf),4.]),options={'time_limit':25.,'threads':1,'presolve':True,'mip_rel_gap':0.,'disp':False})
solverCPU=time.process_time()-t0
selected=None;checked=False
if ans.x is not None:
 chosen=np.flatnonzero(ans.x>.5);selected=[r['representatives'][int(i)] for i in chosen]
 checked=len(chosen)<=4 and np.all(cover[:,chosen].sum(axis=1)>=1) and np.all(np.abs(ans.x-np.rint(ans.x))<1e-5)
 assert checked
out={'status':'FEASIBLE_INDEPENDENT_MASK_CHECK_PASSED' if selected is not None else ('SOLVER_INFEASIBLE_UNCERTIFIED' if ans.status==2 else 'UNKNOWN_NO_INCUMBENT'),'scipy_status':int(ans.status),'message':str(ans.message),'guards':selected,'mask_cover_check':checked,'solver_CPU_seconds':solverCPU,'solver_wall_seconds':time.monotonic()-w0,'worker_CPU_seconds':time.process_time()-START,'worker_wall_seconds':time.monotonic()-WALL,'MIP_calls':1,'LP_calls':0,'warnings':[str(w.message) for w in ws],'mip_node_count':None if getattr(ans,'mip_node_count',None) is None else int(ans.mip_node_count),'mip_gap':None if getattr(ans,'mip_gap',None) is None else float(ans.mip_gap)}
(P/'MIP_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
