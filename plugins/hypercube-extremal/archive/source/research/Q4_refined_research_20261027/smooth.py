"""Independent PSD-feasible Gram-factor search, with exhaustive row separation.
The objective is a smooth approximation of the local maximum. No optimizer
termination flag is used as a mathematical certificate.
"""
from pathlib import Path
import numpy as np,time,json,argparse
from scipy.optimize import minimize
from scipy.special import logsumexp
from model import Model,P
from sdp_core import vec
ap=argparse.ArgumentParser();ap.add_argument('--rounds',type=int,default=6);ap.add_argument('--iterations',type=int,default=250);args=ap.parse_args()
M=Model();nv=M.nv;dims=M.dims;bs=np.cumsum(np.r_[0,np.array(dims)**2]);st=time.time();history=[]
x0=np.load(P/'fullface_best.npz')['x'];base=M.evaluate(x0);best=float(base.max());active=np.unique(np.r_[np.argsort(base)[-3500:],np.load(P/'fullface_dual.npz')['active']]);isin=np.zeros(M.N,bool);isin[active]=1
L=[]
for b,n in enumerate(dims):
 w,U=np.linalg.eigh(M.matrix(x0,b));L.append(U*np.sqrt(np.maximum(w,1e-6)))
y=np.concatenate([l.ravel() for l in L]);np.savez(P/'smooth_best.npz',x=x0,upper=best)
def build(y):
 x=np.zeros(nv);Ls=[]
 for b,n in enumerate(dims):
  l=y[bs[b]:bs[b+1]].reshape(n,n);Ls.append(l);q=l@l.T
  if b<6:x[M.os[b]:M.os[b+1]]=vec(q)
  elif b<11:
   f=M.fb[b-6];x[M.oldnv+M.fs[b-6]:M.oldnv+M.fs[b-5]]=np.bincount(f['orbit'],weights=q[f['ii'],f['jj']],minlength=len(f['counts']))/f['counts']
  else:x[-45:]=vec(q)
 return x,Ls
for run in range(args.rounds):
 A=M.amat(active);dd=M.dd[active];temperature=[1e-4,3e-5,1e-5,3e-6,1e-6,3e-7,1e-7][min(run,6)];count=0
 def fun(y):
  global count
  x,Ls=build(y);v=dd+A@x;m=v.max();e=np.exp((v-m)/temperature);p=e/e.sum();f=m+temperature*np.log(e.sum());mom=A.T@p
  grad=np.concatenate([(2*M.moment(mom,b)@l).ravel() for b,l in enumerate(Ls)]);count+=1
  if count%50==0:print('run',run,'call',count,'tau',temperature,'smooth',f,'localmax',m,'grad',np.linalg.norm(grad),'sec',time.time()-st,flush=True)
  return f,grad
 res=minimize(fun,y,method='L-BFGS-B',jac=True,options=dict(maxiter=args.iterations,ftol=1e-14,gtol=1e-8,maxcor=12,maxls=35));y=res.x;x,_=build(y);v=M.evaluate(x);ub=float(v.max());local=float(v[active].max())
 if ub<best:best=ub;np.savez(P/'smooth_best.npz',x=x,upper=best,run=run)
 extra=np.where((v>local-2e-5)&~isin)[0]
 if len(extra)>800:extra=extra[np.argsort(v[extra])[-800:]]
 active=np.r_[active,extra];isin[extra]=1
 history.append(dict(run=run,upper=ub,best=best,temperature=temperature,iterations=res.nit,success=bool(res.success),message=str(res.message),rows=len(active),added=len(extra),seconds=time.time()-st))
 (P/'smooth_history.json').write_text(json.dumps(history,indent=2));np.savez(P/'smooth_latest.npz',y=y,x=x,upper=ub,active=active)
 print('DONE',history[-1],flush=True)
