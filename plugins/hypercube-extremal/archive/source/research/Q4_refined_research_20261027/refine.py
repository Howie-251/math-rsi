"""PSD Gram optimization with frequent exhaustive separation; six nonredundant blocks.
Every saved best is checked against ALL complete Q4 representatives. Restricted
smooth objective values alone are never reported as mathematical upper bounds.
"""
import argparse,time,json,numpy as np
from scipy.optimize import minimize
from model import Model,P
from fold_old import fold
from sdp_core import vec
ap=argparse.ArgumentParser();ap.add_argument('--cycles',type=int,default=60);ap.add_argument('--iterations',type=int,default=120);ap.add_argument('--restart',action='store_true');a=ap.parse_args()
M=Model();od=M.oldnv;dims=M.dims[6:];bs=np.cumsum(np.r_[0,np.array(dims)**2]);nvar=M.nv-od
x0=np.load(P/'adaptive_best.npz')['x']
vv=M.evaluate(x0);best=float(vv.max());
extraactive=np.load(P/'adaptive_latest.npz')['active']
active=np.unique(np.r_[extraactive,np.argsort(vv)[-3500:]]);isin=np.zeros(M.N,bool);isin[active]=1
st=time.time();history=[];x=x0.copy();np.savez(P/'refine_best.npz',x=x,upper=best)
def from_y(y):
 x=np.zeros(M.nv);Ls=[]
 for j,n in enumerate(dims):
  l=y[bs[j]:bs[j+1]].reshape(n,n);Ls.append(l);q=l@l.T
  if j<5:
   f=M.fb[j];x[od+M.fs[j]:od+M.fs[j+1]]=np.bincount(f['orbit'],weights=q[f['ii'],f['jj']],minlength=len(f['counts']))/f['counts']
  else:x[-45:]=vec(q)
 return x,Ls
for cy in range(a.cycles):
 Ls=[]
 for j,n in enumerate(dims):
  w,U=np.linalg.eigh(M.matrix(x,j+6));Ls.append(U*np.sqrt(np.maximum(w,1e-7)))
 y=np.concatenate([l.ravel() for l in Ls]);A=M.amat(active);d=M.dd[active];tau=3e-6 if cy<10 else 1e-6
 count=0
 def fun(y):
  global count
  xx,L=from_y(y);v=d+A@xx;vmax=v.max();p=np.exp((v-vmax)/tau);z=p.sum();p/=z;f=vmax+tau*np.log(z);m=A.T@p
  grad=np.concatenate([(2*M.moment(m,j+6)@l).ravel() for j,l in enumerate(L)]);count+=1
  return f,grad
 res=minimize(fun,y,method='L-BFGS-B',jac=True,options=dict(maxiter=a.iterations,ftol=1e-14,gtol=1e-9,maxcor=15,maxls=35));x,L=from_y(res.x);v=M.evaluate(x);ub=float(v.max());restricted=float(v[active].max())
 if ub<best:best=ub;np.savez(P/'refine_best.npz',x=x,upper=best,cycle=cy)
 add=np.where((v>restricted-3*tau)&~isin)[0]
 if len(add)>600:add=add[np.argsort(v[add])[-600:]]
 active=np.r_[active,add];isin[add]=1
 rec=dict(cycle=cy,tau=tau,full_upper=ub,restricted_max=restricted,best_upper=best,rows=len(active),added=len(add),calls=count,success=bool(res.success),seconds=time.time()-st)
 history.append(rec);(P/'refine_history.json').write_text(json.dumps(history,indent=2));np.savez(P/'refine_latest.npz',x=x,upper=ub,active=active)
 print(rec,flush=True)
