"""Rank-one column generation with exact exhaustive local-row separation.
Each face-root ray is averaged under the ROOT STABILIZER, not separately
quotiented in its two flag arguments. This preserves relative orientation.
The resulting primal matrices are PSD by construction; final rounding is
certified separately with integer arithmetic.
"""
from pathlib import Path
import numpy as np,time,json,argparse
from scipy import sparse
from scipy.optimize._highspy import _core as hs
from model import Model,P
ap=argparse.ArgumentParser();ap.add_argument('--rounds',type=int,default=400);ap.add_argument('--restart',action='store_true');ap.add_argument('--rays-per-block',type=int,default=4);ap.add_argument('--prefix',default='polish');args=ap.parse_args()
M=Model();nv=M.nv;N=M.N
path=P/(args.prefix+'_best.npz');x0=np.load(path)['x'] if args.restart and path.exists() else np.load(P/'adaptive_best.npz')['x']
V=[];blockids=[]
def add(b,v):
 c=M.ray(b,v);V.append(c);blockids.append(b);return c
for b in range(6,12):
 q=M.matrix(x0,b);t=float(np.trace(q))
 if t>1e-12:
  c=np.zeros(nv)
  if b<11:c[M.oldnv+M.fs[b-6]:M.oldnv+M.fs[b-5]]=x0[M.oldnv+M.fs[b-6]:M.oldnv+M.fs[b-5]]/t
  else:c[-45:]=x0[-45:]/t
  V.append(c);blockids.append(b)
 w,U=np.linalg.eigh(q)
 for j in np.where(w>1e-6)[0][-5:]:add(b,U[:,j])
base=M.evaluate(x0);best=float(base.max());rng=np.random.default_rng(974)
active=np.unique(np.r_[np.argsort(base)[-2500:],rng.choice(N,500,replace=False)]);isin=np.zeros(N,bool);isin[active]=1;A=M.amat(active)
VV=np.column_stack(V);AA=sparse.csc_matrix(np.c_[-np.ones(len(active)),A@VV]);lp=hs.HighsLp();lp.num_col_=AA.shape[1];lp.num_row_=len(active)
lp.col_cost_=np.r_[1.,np.zeros(len(V))];lp.col_lower_=np.zeros(AA.shape[1]);lp.col_upper_=np.full(AA.shape[1],np.inf);lp.col_upper_[0]=1
lp.row_lower_=np.full(len(active),-np.inf);lp.row_upper_=-M.dd[active];lp.a_matrix_.format_=hs.MatrixFormat.kColwise;lp.a_matrix_.start_=AA.indptr.astype(np.int32);lp.a_matrix_.index_=AA.indices.astype(np.int32);lp.a_matrix_.value_=AA.data
h=hs._Highs();h.setOptionValue('output_flag',False);h.setOptionValue('solver','simplex');h.setOptionValue('threads',1);h.setOptionValue('simplex_strategy',1)
h.setOptionValue('primal_feasibility_tolerance',1e-9);h.setOptionValue('dual_feasibility_tolerance',1e-9);h.passModel(lp)
st=time.time();hist=[];np.savez(path,x=x0,upper=best,iteration=-1)
for it in range(args.rounds):
 h.run();status=h.getModelStatus()
 if status!=hs.HighsModelStatus.kOptimal:print('FAIL',h.modelStatusToString(status),flush=True);break
 sol=h.getSolution();xx=np.array(sol.col_value);weights=np.maximum(xx[1:],0);nr=len(V);VV=np.column_stack(V);x=VV@weights;vals=M.evaluate(x);ub=float(vals.max());obj=float(xx[0])
 if ub<best:best=ub;np.savez(path,x=x,upper=best,iteration=it)
 p=-np.array(sol.row_dual);mom=A.T@p;mins=[];new=[]
 for b in range(6,12):
  mat=M.moment(mom,b);w,U=np.linalg.eigh(mat);mins.append(float(w[0]))
  for k in np.where(w< -1e-8)[0][:args.rays_per_block]:new.append(add(b,U[:,k]))
 hist.append(dict(iteration=it,restricted_objective=obj,full_upper=ub,best_upper=best,min_eig=min(mins),block_min_eigs=mins,rays=nr,rows=len(active),seconds=time.time()-st))
 (P/(args.prefix+'_history.json')).write_text(json.dumps(hist,indent=2));np.savez(P/(args.prefix+'_dual.npz'),p=p,active=active,obj=obj,mins=mins)
 extra=np.where((vals>obj+2e-8)&~isin)[0]
 if len(extra)>300:extra=extra[np.argsort(vals[extra])[-300:]]
 print(args.prefix,it,'obj',obj,'upper',ub,'best',best,'rays',nr,'rows',len(active),'newrows',len(extra),'mineig',min(mins),'sec',time.time()-st,flush=True)
 drop=np.where((weights<1e-11)&(np.arange(nr)<max(0,nr-48)))[0]
 if len(drop):
  h.deleteCols(len(drop),(1+drop).astype(np.int32));ds=set(drop.tolist());keep=[k for k in range(len(V)) if k not in ds];V=[V[k] for k in keep];blockids=[blockids[k] for k in keep]
 if new:
  B=sparse.csc_matrix(A@np.column_stack(new));k=len(new);h.addCols(k,np.zeros(k),np.zeros(k),np.full(k,np.inf),B.nnz,B.indptr.astype(np.int32),B.indices.astype(np.int32),B.data)
 if len(extra):
  B=M.amat(extra);VV=np.column_stack(V);AA=sparse.csr_matrix(np.c_[-np.ones(len(extra)),B@VV]);h.addRows(len(extra),np.full(len(extra),-np.inf),-M.dd[extra],AA.nnz,AA.indptr.astype(np.int32),AA.indices.astype(np.int32),AA.data)
  A=sparse.vstack([A,B],format='csr');active=np.r_[active,extra];isin[extra]=1
 if not len(extra) and not len(new):print('STOP',best,flush=True);break
