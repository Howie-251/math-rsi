"""Exact joint-shadow consistency + six PSD cones, optimized by rank-one column generation.
A row is an attainable unordered 4-tuple of partial Q4 shadows of one C4-free Q4.
"""
from pathlib import Path
import argparse,numpy as np,time,json
from scipy import sparse
from scipy.optimize._highspy import _core as hs
from sdp_core import vec,unpack
ap=argparse.ArgumentParser();ap.add_argument('--rounds',type=int,default=120);ap.add_argument('--restart',action='store_true');args=ap.parse_args()
P=Path(__file__).resolve().parent;m=np.load(P/'full_meta.npz');dims=m['dims'];starts=m['starts'];d=m['d'];N=len(d)
C=sparse.load_npz(P/'full_C.npz').astype(float)/96;sh=np.load(P/'joint_shadows.npy');Nfull=len(sh);dd=d[sh].mean(axis=1)
ray_b=[];ray_v=[];R=[]
def add(b,v):
 v=np.asarray(v);v=v/np.linalg.norm(v);ray_b.append(b);ray_v.append(v)
 co=np.asarray(C[:,starts[b]:starts[b+1]]@vec(np.outer(v,v))).ravel();R.append(co);return co
saved=np.load(P/('joint_best.npz' if args.restart and (P/'joint_best.npz').exists() else 'extension_best.npz'))
for b,n in enumerate(dims):
 w,V=np.linalg.eigh(unpack(saved['x'][starts[b]:starts[b+1]],n))
 for k in np.where(w>1e-11)[0]:add(b,V[:,k])
base=d+C@saved['x'];basevals=base[sh].mean(axis=1);best=float(basevals.max());rng=np.random.default_rng(47)
active=np.unique(np.r_[np.argsort(basevals)[-2500:],rng.choice(Nfull,500,replace=False)]);isin=np.zeros(Nfull,bool);isin[active]=True
RR=np.column_stack(R);AR=RR[sh[active]].mean(axis=1)
AA=sparse.csc_matrix(np.c_[-np.ones(len(active)),AR]);lp=hs.HighsLp();lp.num_col_=AA.shape[1];lp.num_row_=len(active)
lp.col_cost_=np.r_[1.,np.zeros(len(R))];lp.col_lower_=np.zeros(AA.shape[1]);lp.col_upper_=np.full(AA.shape[1],np.inf);lp.col_upper_[0]=1
lp.row_lower_=np.full(len(active),-np.inf);lp.row_upper_=-dd[active]
lp.a_matrix_.format_=hs.MatrixFormat.kColwise;lp.a_matrix_.start_=AA.indptr.astype(np.int32);lp.a_matrix_.index_=AA.indices.astype(np.int32);lp.a_matrix_.value_=AA.data
h=hs._Highs();h.setOptionValue('output_flag',False);h.setOptionValue('solver','simplex');h.setOptionValue('threads',1);h.setOptionValue('simplex_strategy',1)
h.setOptionValue('primal_feasibility_tolerance',1e-9);h.setOptionValue('dual_feasibility_tolerance',1e-9);h.passModel(lp)
st=time.time();hist=[];np.savez(P/'joint_best.npz',x=saved['x'],upper=best,dims=dims,starts=starts,iteration=-1)
for it in range(args.rounds):
 h.run();status=h.getModelStatus()
 if status!=hs.HighsModelStatus.kOptimal:print('FAIL',h.modelStatusToString(status),flush=True);break
 sol=h.getSolution();xx=np.array(sol.col_value);weights=np.maximum(xx[1:],0);nr=len(R);RR=np.column_stack(R)
 vals=(d+RR@weights)[sh].mean(axis=1);ub=float(vals.max());obj=float(xx[0]);x=np.zeros(starts[-1])
 for k,v in enumerate(ray_v):x[starts[ray_b[k]]:starts[ray_b[k]+1]]+=weights[k]*vec(np.outer(v,v))
 if ub<best:best=ub;np.savez(P/'joint_best.npz',x=x,upper=best,dims=dims,starts=starts,iteration=it)
 pactive=-np.array(sol.row_dual);p=np.bincount(sh[active].ravel(),weights=np.repeat(pactive/4,4),minlength=N);mom=C.T@p;mins=[];newcols=[]
 for b,n in enumerate(dims):
  M=unpack(mom[starts[b]:starts[b+1]],n);M=(M+np.diag(np.diag(M)))/2;w,V=np.linalg.eigh(M);mins.append(float(w[0]))
  for k in np.where(w < -1e-7)[0][:3]:newcols.append(add(b,V[:,k]))
 hist.append({'iteration':it,'restricted_objective':obj,'full_upper':ub,'best_upper':best,'min_eig':min(mins),'rays':nr,'rows':len(active),'seconds':time.time()-st})
 (P/'joint_history.json').write_text(json.dumps(hist,indent=2));np.savez(P/'joint_dual.npz',p=p,pactive=pactive,active=active,obj=obj,mins=mins)
 extra=np.where((vals>obj+1e-8)&~isin)[0]
 if len(extra)>500:extra=extra[np.argsort(vals[extra])[-500:]]
 print('joint',it,'obj',obj,'upper',ub,'best',best,'rays',nr,'rows',len(active),'newrows',len(extra),'mineig',min(mins),'sec',time.time()-st,flush=True)
 drop=np.where((weights<1e-11)&(np.arange(nr)<max(0,nr-24)))[0]
 if len(drop):
  h.deleteCols(len(drop),(1+drop).astype(np.int32));dropset=set(drop.tolist());keep=[k for k in range(len(R)) if k not in dropset]
  ray_b=[ray_b[k] for k in keep];ray_v=[ray_v[k] for k in keep];R=[R[k] for k in keep]
 if newcols:
  co=np.column_stack(newcols);B=sparse.csc_matrix(co[sh[active]].mean(axis=1));k=len(newcols)
  h.addCols(k,np.zeros(k),np.zeros(k),np.full(k,np.inf),B.nnz,B.indptr.astype(np.int32),B.indices.astype(np.int32),B.data)
 if len(extra):
  RR=np.column_stack(R);AA=sparse.csr_matrix(np.c_[-np.ones(len(extra)),RR[sh[extra]].mean(axis=1)])
  h.addRows(len(extra),np.full(len(extra),-np.inf),-dd[extra],AA.nnz,AA.indptr.astype(np.int32),AA.indices.astype(np.int32),AA.data);active=np.r_[active,extra];isin[extra]=True
 if not len(extra) and not len(newcols):print('STOP',best,flush=True);break
