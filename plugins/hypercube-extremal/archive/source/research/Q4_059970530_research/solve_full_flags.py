"""Full-Q4 completion consistency, old six PSD blocks, plus genuine empty-face and vertex-root blocks.
All candidates are evaluated on the exhaustive 3312331 representative family.
"""
from pathlib import Path
import argparse,numpy as np,time,json
from scipy import sparse
from scipy.optimize._highspy import _core as hs
from sdp_core import vec,unpack
ap=argparse.ArgumentParser();ap.add_argument('--rounds',type=int,default=150);ap.add_argument('--restart',action='store_true');args=ap.parse_args()
P=Path(__file__).resolve().parent;m=np.load(P/'full_meta.npz');od=m['dims'];os=m['starts'];dims=np.r_[od,45,9];starts=np.cumsum(np.r_[0,dims*(dims+1)//2]);d=m['d'];nv=int(starts[-1]);oldnv=int(os[-1])
C=sparse.load_npz(P/'full_C.npz').astype(float)/96
F=sparse.csr_matrix((np.memmap(P/'new_flags_vals.bin',dtype=np.int16,mode='r'),np.memmap(P/'new_flags_cols.bin',dtype=np.int32,mode='r'),np.memmap(P/'new_flags_ptr.bin',dtype=np.int64,mode='r')),shape=(3312331,1080)).astype(float)/48
sh=np.load(P/'full_flags_shadows.npy');N=len(sh);dd=d[sh].mean(axis=1)
def amat(rows):
 s=sh[rows];a=(C[s[:,0]]+C[s[:,1]]+C[s[:,2]]+C[s[:,3]])/4
 return sparse.hstack([a,F[rows]],format='csr')
def evaluate(x):return (d+C@x[:oldnv])[sh].mean(axis=1)+F@x[oldnv:]
rb=[];rv=[];V=[]
def add(b,v):
 v=np.asarray(v);v/=np.linalg.norm(v);rb.append(b);rv.append(v);col=np.zeros(nv);col[starts[b]:starts[b+1]]=vec(np.outer(v,v));V.append(col);return col
saved=np.load(P/('full_flags_best.npz' if args.restart and (P/'full_flags_best.npz').exists() else 'joint_best.npz'));x0=np.zeros(nv);x0[:len(saved['x'])]=saved['x']
for b,n in enumerate(dims):
 w,U=np.linalg.eigh(unpack(x0[starts[b]:starts[b+1]],n))
 for k in np.where(w>1e-11)[0]:add(b,U[:,k])
base=evaluate(x0);best=float(base.max());rng=np.random.default_rng(59)
active=np.unique(np.r_[np.argsort(base)[-2500:],rng.choice(N,500,replace=False)]);isin=np.zeros(N,bool);isin[active]=1;A=amat(active)
VV=np.column_stack(V);AA=sparse.csc_matrix(np.c_[-np.ones(len(active)),A@VV]);lp=hs.HighsLp();lp.num_col_=AA.shape[1];lp.num_row_=len(active)
lp.col_cost_=np.r_[1.,np.zeros(len(V))];lp.col_lower_=np.zeros(AA.shape[1]);lp.col_upper_=np.full(AA.shape[1],np.inf);lp.col_upper_[0]=1
lp.row_lower_=np.full(len(active),-np.inf);lp.row_upper_=-dd[active]
lp.a_matrix_.format_=hs.MatrixFormat.kColwise;lp.a_matrix_.start_=AA.indptr.astype(np.int32);lp.a_matrix_.index_=AA.indices.astype(np.int32);lp.a_matrix_.value_=AA.data
h=hs._Highs();h.setOptionValue('output_flag',False);h.setOptionValue('solver','simplex');h.setOptionValue('threads',1);h.setOptionValue('simplex_strategy',1)
h.setOptionValue('primal_feasibility_tolerance',1e-9);h.setOptionValue('dual_feasibility_tolerance',1e-9);h.passModel(lp)
st=time.time();hist=[];np.savez(P/'full_flags_best.npz',x=x0,upper=best,dims=dims,starts=starts,iteration=-1)
for it in range(args.rounds):
 h.run();status=h.getModelStatus()
 if status!=hs.HighsModelStatus.kOptimal:print('FAIL',h.modelStatusToString(status),flush=True);break
 sol=h.getSolution();xx=np.array(sol.col_value);weights=np.maximum(xx[1:],0);nr=len(V);VV=np.column_stack(V);x=VV@weights;vals=evaluate(x);ub=float(vals.max());obj=float(xx[0])
 if ub<best:best=ub;np.savez(P/'full_flags_best.npz',x=x,upper=best,dims=dims,starts=starts,iteration=it)
 p=-np.array(sol.row_dual);mom=A.T@p;mins=[];new=[]
 for b,n in enumerate(dims):
  M=unpack(mom[starts[b]:starts[b+1]],n);M=(M+np.diag(np.diag(M)))/2;w,U=np.linalg.eigh(M);mins.append(float(w[0]))
  for k in np.where(w < -1e-7)[0][:3]:new.append(add(b,U[:,k]))
 hist.append({'iteration':it,'restricted_objective':obj,'full_upper':ub,'best_upper':best,'min_eig':min(mins),'block_min_eigs':mins,'rays':nr,'rows':len(active),'seconds':time.time()-st})
 (P/'full_flags_history.json').write_text(json.dumps(hist,indent=2));np.savez(P/'full_flags_dual.npz',p=p,active=active,obj=obj,mins=mins)
 extra=np.where((vals>obj+1e-8)&~isin)[0]
 if len(extra)>500:extra=extra[np.argsort(vals[extra])[-500:]]
 print('full-flags',it,'obj',obj,'upper',ub,'best',best,'rays',nr,'rows',len(active),'newrows',len(extra),'mineig',min(mins),'sec',time.time()-st,flush=True)
 drop=np.where((weights<1e-11)&(np.arange(nr)<max(0,nr-24)))[0]
 if len(drop):
  h.deleteCols(len(drop),(1+drop).astype(np.int32));ds=set(drop.tolist());keep=[k for k in range(len(V)) if k not in ds];rb=[rb[k] for k in keep];rv=[rv[k] for k in keep];V=[V[k] for k in keep]
 if new:
  B=sparse.csc_matrix(A@np.column_stack(new));k=len(new);h.addCols(k,np.zeros(k),np.zeros(k),np.full(k,np.inf),B.nnz,B.indptr.astype(np.int32),B.indices.astype(np.int32),B.data)
 if len(extra):
  B=amat(extra);VV=np.column_stack(V);AA=sparse.csr_matrix(np.c_[-np.ones(len(extra)),B@VV])
  h.addRows(len(extra),np.full(len(extra),-np.inf),-dd[extra],AA.nnz,AA.indptr.astype(np.int32),AA.indices.astype(np.int32),AA.data)
  A=sparse.vstack([A,B],format='csr');active=np.r_[active,extra];isin[extra]=1
 if not len(extra) and not len(new):print('STOP',best,flush=True);break
