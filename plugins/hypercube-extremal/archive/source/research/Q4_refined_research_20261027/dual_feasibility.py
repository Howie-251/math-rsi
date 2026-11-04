"""Numerical diagnostic: can the current local PSD relaxation support density 0.59?
A feasible local distribution is NOT a genuine high-dimensional C4-free graph.
An unsuccessful numerical run is not an infeasibility certificate.
"""
import numpy as np,json,time,argparse
from scipy import sparse
from model import Model,P
from sdp_core import vec
ap=argparse.ArgumentParser();ap.add_argument('--target',type=float,default=.59);ap.add_argument('--iterations',type=int,default=3000);a=ap.parse_args()
M=Model();z=np.load(P/'adaptive_latest.npz');rows=z['active'];AA=M.amat(rows);A=AA[:,M.oldnv:];d=M.dd[rows];R=len(rows);st=time.time()
counts=np.r_[*[f['ordered_counts'] for f in M.fb],np.array([1 if i==j else 2 for i in range(9) for j in range(i,9)])]
B=A@sparse.diags(1/np.sqrt(counts))
v=np.ones(R)/np.sqrt(R)
for _ in range(50):v=B@(B.T@v);v/=np.linalg.norm(v)
lip=2*float(v@(B@(B.T@v)));step=.99/lip

def simplex(x):
 u=np.sort(x)[::-1];s=np.cumsum(u)-1;k=np.nonzero(u-s/(np.arange(len(u))+1)>0)[0][-1];return np.maximum(x-s[k]/(k+1),0)
def proj(z):
 def at(mu):return simplex(z+mu*d)
 lo,hi=-1.,1.
 while at(lo)@d>a.target:lo*=2
 while at(hi)@d<a.target:hi*=2
 for _ in range(36):
  mu=(lo+hi)/2;p=at(mu)
  if p@d>a.target:hi=mu
  else:lo=mu
 return at((lo+hi)/2)
def fg(p):
 m=A.T@p;mm=np.r_[np.zeros(M.oldnv),m];negative=np.zeros(M.nv);mins=[];value=0
 for j in range(6):
  mat=M.moment(mm,j+6);w,U=np.linalg.eigh(mat);mins.append(float(w[0]));wn=np.minimum(w,0);value+=float(wn@wn);q=(U*wn)@U.T
  if j<5:
   f=M.fb[j];negative[M.oldnv+M.fs[j]:M.oldnv+M.fs[j+1]]=np.bincount(f['orbit'],weights=q[f['ii'],f['jj']])/f['counts']
  else:negative[-45:]=vec(q)
 return value,2*(A@negative[M.oldnv:]),mins
# initialize near the current primal active distribution
x=np.load(P/'adaptive_best.npz')['x'];val=d+AA@x;p=np.exp((val-val.max())/5e-5);p/=p.sum();p=proj(p);y=p.copy();t=1.;best=1.;history=[]
for it in range(a.iterations):
 f,g,mins=fg(y);pnew=proj(y-step*g);tnew=(1+np.sqrt(1+4*t*t))/2;ynew=pnew+(t-1)/tnew*(pnew-p)
 if np.dot(ynew-pnew,pnew-p)>0 and it%200==199:tnew=1.;ynew=pnew.copy()
 p,y,t=pnew,ynew,tnew
 if it%50==0:
  ff,gg,mm=fg(p)
  if ff<best:best=ff;np.savez(P/'dual_feasible_candidate.npz',p=p,rows=rows,target=a.target,min_eigs=mm,violation=ff)
  rec=dict(iteration=it,violation=ff,best=best,min_eigs=mm,density=float(p@d),mass=float(p.sum()),step=step,seconds=time.time()-st)
  history.append(rec);(P/'dual_feasibility_history.json').write_text(json.dumps(history,indent=2));print(rec,flush=True)
  if min(mm)>=-1e-12:print('NUMERIC_FEASIBILITY_REACHED',flush=True);break
