"""Exploratory pricing of copositive C5/Horn inequalities. NOT part of the final
PSD certificate unless separately optimized and verified. Failed separation is
not a proof that the moment matrices are completely positive.
"""
import numpy as np,time,json
from model import Model,P
M=Model();z=np.load(P/'dual_target_candidate.npz');m=M.amat(z['rows']).T@z['p'];rng=np.random.default_rng(532);out=[];st=time.time()
H=np.ones((5,5));
for i in range(5):H[i,(i+1)%5]=H[(i+1)%5,i]=-1
for b in range(6,12):
 mat=M.moment(m,b);ind=np.where(np.diag(mat)>1e-9)[0];d=np.sqrt(np.diag(mat)[ind]);R=mat[np.ix_(ind,ind)]/d[:,None]/d[None,:];best=1e9;bestids=None
 for trial in range(1000):
  ids=rng.choice(len(ind),5,replace=False)
  for step in range(30):
   delta=np.stack([2*((R[:,ids]*H[i]).sum(axis=1)-R[:,ids[i]])-2*(R[ids[i],ids]@H[i]-1) for i in range(5)])
   delta[:,ids]=np.inf;ij=np.unravel_index(np.argmin(delta),delta.shape)
   if delta[ij]>-1e-10:break
   ids[ij[0]]=ij[1]
  cost=float((H*R[np.ix_(ids,ids)]).sum())
  if cost<best:best=cost;bestids=ind[ids].copy()
  if best<-.1:break
 out.append(dict(block=b,minimum_equal_scaled_cost=best,states=bestids.tolist(),seconds=time.time()-st));print(out[-1],flush=True)
(P/'horn_pricing.json').write_text(json.dumps(out,indent=2))
