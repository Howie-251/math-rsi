"""One hard4-CPU feasibility call; no graph IO or retries."""
import resource
resource.setrlimit(resource.RLIMIT_CPU,(4,4))
from pathlib import Path
import json,sys,time,warnings
START=time.process_time()
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix
prefix=Path(sys.argv[1]);out=Path(sys.argv[2]);d=json.loads(Path(str(prefix)+'.json').read_text())
K=d['unique_nonzero_masks'];W=d['mask_words_per_row'];T=d['missing_count']
masks=np.fromfile(str(prefix)+'.masks.u64.bin',dtype=np.uint64).reshape(K,W)
rr=[];cc=[]
for j in range(T):
 cols=np.flatnonzero((masks[:,j//64]>>np.uint64(j%64))&np.uint64(1)).astype(np.int32)
 rr.append(np.full(len(cols),j,dtype=np.int32));cc.append(cols)
rr.append(np.full(K,T,dtype=np.int32));cc.append(np.arange(K,dtype=np.int32))
ridx=np.concatenate(rr);cidx=np.concatenate(cc)
A=coo_matrix((np.ones(len(ridx)),(ridx,cidx)),shape=(T+1,K)).tocsc()
with warnings.catch_warnings():
 warnings.filterwarnings('ignore',message='Unrecognized options detected')
 res=milp(c=np.ones(K),integrality=np.ones(K,dtype=np.uint8),bounds=Bounds(np.zeros(K),np.ones(K)),
  constraints=LinearConstraint(A,np.r_[np.ones(T),-np.inf],np.r_[np.full(T,np.inf),4.0]),
  options={'time_limit':2.5,'presolve':False,'threads':1})
anchors=None
if res.x is not None:
 chosen=np.flatnonzero(res.x>.5)
 if len(chosen)<=4:
  combined=np.bitwise_or.reduce(masks[chosen],axis=0) if len(chosen) else np.zeros(W,dtype=np.uint64)
  full=np.full(W,np.uint64(2**64-1))
  if T%64:full[-1]=np.uint64((1<<(T%64))-1)
  if np.array_equal(combined,full):anchors=sorted(d['representatives'][int(i)] for i in chosen)
out.write_text(json.dumps({'status':int(res.status),'message':str(res.message),'verified_anchor_incumbent':anchors,
 'variables':K,'rows':T+1,'nonzeros':int(A.nnz),'CPU_seconds':time.process_time()-START,'hard_process_CPU_limit':4,'solver_time_limit':2.5,'presolve':False},indent=2)+'\n')
