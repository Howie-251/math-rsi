"""PSD column generation and row separation, with optional exact-completion cuts.
All reported upper bounds are evaluated on all 90179 partial types.
"""
from pathlib import Path
import argparse,numpy as np,time,json
from scipy import sparse
from scipy.optimize._highspy import _core as hs
from sdp_core import vec,unpack
ap=argparse.ArgumentParser();ap.add_argument('--baseline',action='store_true');ap.add_argument('--rounds',type=int,default=100);ap.add_argument('--restart',action='store_true');args=ap.parse_args()
P=Path(__file__).resolve().parent;tag='baseline' if args.baseline else 'extension'
m=np.load(P/'full_meta.npz');dims=m['dims'];starts=m['starts'];d=m['d'];N=len(d)
C=sparse.load_npz(P/'full_C.npz').astype(float)/96;E=sparse.load_npz(P/'full_eq.npz').astype(float);neq=E.shape[1]
U=np.zeros((N,0)) if args.baseline else np.load(P/'completion_support.npz')['U'].astype(float)/24
nc=U.shape[1];reg=1e-7;ray_b=[];ray_v=[];R=[]
def add(b,v):
 v=np.asarray(v);v=v/np.linalg.norm(v);ray_b.append(b);ray_v.append(v)
 co=np.asarray(C[:,starts[b]:starts[b+1]]@vec(np.outer(v,v))).ravel();R.append(co);return co
saved=np.load(P/(tag+'_best.npz' if args.restart and (P/(tag+'_best.npz')).exists() else 'warm_best.npz'))
for b,n in enumerate(dims):
 w,V=np.linalg.eigh(unpack(saved['x'][starts[b]:starts[b+1]],n))
 for k in np.where(w>1e-11)[0]:add(b,V[:,k])
mu=saved['mu'] if 'mu' in saved else np.zeros(nc)
baseval=d+C@saved['x']+E@saved['lam']+U@mu;rng=np.random.default_rng(40)
active=np.unique(np.r_[np.argsort(baseval)[-2500:],rng.choice(N,500,replace=False)]);isin=np.zeros(N,bool);isin[active]=True
RR=np.column_stack(R);rstart=2*neq+1+nc
AA=sparse.hstack([E[active],-E[active],-np.ones((len(active),1)),sparse.csr_matrix(U[active]),sparse.csr_matrix(RR[active])],format='csc')
lp=hs.HighsLp();lp.num_col_=AA.shape[1];lp.num_row_=len(active)
lp.col_cost_=np.r_[np.full(2*neq,reg),1.,np.zeros(nc+len(R))];lp.col_lower_=np.zeros(AA.shape[1]);lp.col_upper_=np.full(AA.shape[1],np.inf);lp.col_upper_[2*neq]=1
lp.row_lower_=np.full(len(active),-np.inf);lp.row_upper_=-d[active]
lp.a_matrix_.format_=hs.MatrixFormat.kColwise;lp.a_matrix_.start_=AA.indptr.astype(np.int32);lp.a_matrix_.index_=AA.indices.astype(np.int32);lp.a_matrix_.value_=AA.data
h=hs._Highs();h.setOptionValue('output_flag',False);h.setOptionValue('solver','simplex');h.setOptionValue('threads',1);h.setOptionValue('simplex_strategy',4)
h.setOptionValue('primal_feasibility_tolerance',1e-9);h.setOptionValue('dual_feasibility_tolerance',1e-9);h.passModel(lp)
best=float(baseval.max());st=time.time();history=[]
np.savez(P/(tag+'_best.npz'),x=saved['x'],lam=saved['lam'],mu=mu,upper=best,dims=dims,starts=starts,iteration=-1)
for it in range(args.rounds):
 h.run();status=h.getModelStatus()
 if status!=hs.HighsModelStatus.kOptimal:print('FAIL',h.modelStatusToString(status),flush=True);break
 sol=h.getSolution();xx=np.array(sol.col_value);lam=xx[:neq]-xx[neq:2*neq];mu=np.maximum(xx[2*neq+1:rstart],0);weights=np.maximum(xx[rstart:],0);nr=len(R)
 RR=np.column_stack(R);vals=d+RR@weights+E@lam+U@mu;ub=float(vals.max());obj=xx[2*neq];x=np.zeros(starts[-1])
 for k,v in enumerate(ray_v):x[starts[ray_b[k]]:starts[ray_b[k]+1]]+=weights[k]*vec(np.outer(v,v))
 if ub<best:
  best=ub;np.savez(P/(tag+'_best.npz'),x=x,lam=lam,mu=mu,upper=best,dims=dims,starts=starts,iteration=it)
 p=np.zeros(N);p[active]=-np.array(sol.row_dual);mom=np.asarray(C.T@p).ravel();mins=[];newcols=[]
 for b,n in enumerate(dims):
  M=unpack(mom[starts[b]:starts[b+1]],n);M=(M+np.diag(np.diag(M)))/2;w,V=np.linalg.eigh(M);mins.append(float(w[0]))
  for k in np.where(w < -2e-7)[0][:2]:newcols.append(add(b,V[:,k]))
 history.append({'iteration':it,'restricted_objective':obj,'full_upper':ub,'best_upper':best,'min_eig':min(mins),'rays':nr,'rows':len(active),'seconds':time.time()-st,'active_completion_cuts':int((mu>1e-8).sum()),'max_mu':float(mu.max()) if len(mu) else 0})
 (P/(tag+'_history.json')).write_text(json.dumps(history,indent=2));np.savez(P/(tag+'_dual.npz'),p=p,mins=mins,obj=obj)
 extra=np.where((vals>obj+1e-8)&~isin)[0]
 if len(extra)>400:extra=extra[np.argsort(vals[extra])[-400:]]
 print(tag,it,'obj',obj,'upper',ub,'best',best,'rays',nr,'rows',len(active),'newrows',len(extra),'mineig',min(mins),'mu',int((mu>1e-8).sum()),'sec',time.time()-st,flush=True)
 drop=np.where((weights<1e-11)&(np.arange(nr)<max(0,nr-20)))[0]
 if len(drop):
  h.deleteCols(len(drop),(rstart+drop).astype(np.int32));dropset=set(drop.tolist());keep=[k for k in range(len(R)) if k not in dropset]
  ray_b=[ray_b[k] for k in keep];ray_v=[ray_v[k] for k in keep];R=[R[k] for k in keep]
 if newcols:
  B=sparse.csc_matrix(np.column_stack(newcols)[active]);k=len(newcols);h.addCols(k,np.zeros(k),np.zeros(k),np.full(k,np.inf),B.nnz,B.indptr.astype(np.int32),B.indices.astype(np.int32),B.data)
 if len(extra):
  RR=np.column_stack(R);AA=sparse.hstack([E[extra],-E[extra],-np.ones((len(extra),1)),sparse.csr_matrix(U[extra]),sparse.csr_matrix(RR[extra])],format='csr')
  h.addRows(len(extra),np.full(len(extra),-np.inf),-d[extra],AA.nnz,AA.indptr.astype(np.int32),AA.indices.astype(np.int32),AA.data);active=np.r_[active,extra];isin[extra]=True
 if not len(extra) and not len(newcols):print('STOP',best,flush=True);break
