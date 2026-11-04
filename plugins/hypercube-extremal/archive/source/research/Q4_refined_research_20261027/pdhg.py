"""Convex PSD/simplex saddle search with exhaustive row separation.
Numerical candidates are never certified here; use certify_six.py afterward.
"""
import argparse,time,json,numpy as np
from scipy import sparse
from model import Model,P
from sdp_core import vec
ap=argparse.ArgumentParser();ap.add_argument('--steps',type=int,default=12000);ap.add_argument('--tau',type=float,default=12.);args=ap.parse_args()
M=Model();od=M.oldnv;dims=M.dims[6:];st=time.time()
xx=np.load(P/'adaptive_best.npz')['x'];best=float(M.evaluate(xx).max());np.savez(P/'pdhg_best.npz',x=xx,upper=best)
rows=np.unique(np.r_[np.load(P/'adaptive_latest.npz')['active'],np.load(P/'polish_dual.npz')['active']]);olddual=np.load(P/'polish_dual.npz');p=np.zeros(len(rows));p[np.searchsorted(rows,olddual['active'])]=olddual['p'];p=np.maximum(p,0);p/=p.sum()
counts=np.r_[*[f['ordered_counts'] for f in M.fb],np.array([1 if i==j else 2 for i in range(9) for j in range(i,9)])];sq=np.sqrt(counts)
z=xx[od:]*sq;zb=z.copy();zavg=z.copy();pavg=p.copy();hist=[]
def simplex(a):
 v=np.sort(a)[::-1];s=np.cumsum(v)-1;k=np.nonzero(v-s/(np.arange(len(v))+1)>0)[0][-1];return np.maximum(a-s[k]/(k+1),0)
def cone(z):
 x=np.r_[np.zeros(od),z/sq];out=np.zeros(M.nv-od)
 for j in range(6):
  q=M.matrix(x,j+6);w,U=np.linalg.eigh(q);q=(U*np.maximum(w,0))@U.T
  if j<5:
   f=M.fb[j];out[M.fs[j]:M.fs[j+1]]=np.bincount(f['orbit'],weights=q[f['ii'],f['jj']],minlength=len(f['counts']))/f['counts']
  else:out[-45:]=vec(q)
 return out*sq

def setup(rows):
 A=M.amat(rows)[:,od:];B=A@sparse.diags(1/sq);d=M.dd[rows]
 v=np.random.default_rng(42).normal(size=B.shape[1]);v/=np.linalg.norm(v)
 for _ in range(40):v=B.T@(B@v);v/=np.linalg.norm(v)
 norm2=float(v@(B.T@(B@v)));return B,d,norm2
B,d,norm2=setup(rows);tau=args.tau;sig=.9/(tau*norm2)
print('START',best,'rows',len(rows),'norm2',norm2,'tau',tau,'sigma',sig,flush=True)
for it in range(args.steps):
 pn=simplex(p+sig*(B@zb+d));zn=cone(z-tau*(B.T@pn));zb=2*zn-z;z=zn;p=pn
 # Uniform running average within a separation epoch remains PSD.
 t=it%400+1;zavg+=(z-zavg)/t;pavg+=(p-pavg)/t
 if it%400==399:
  candidates=[z,zavg];upp=[]
  for cand in candidates:
   x=np.r_[np.zeros(od),cand/sq];vv=M.evaluate(x);up=float(vv.max());upp.append(up)
   if up<best:best=up;np.savez(P/'pdhg_best.npz',x=x,upper=best,iteration=it)
  mins=[];m=np.r_[np.zeros(od),(B.T@p)/sq] # moment expects original coefficient m; transform back correctly below
  m=np.r_[np.zeros(od),(B.T@p)*sq]
  for j in range(6):mins.append(float(np.linalg.eigvalsh(M.moment(m,j+6))[0]))
  rec=dict(iteration=it,full_upper=upp,best=best,dual_objective=float(p@d),min_eigs=mins,rows=len(rows),seconds=time.time()-st);hist.append(rec);(P/'pdhg_history.json').write_text(json.dumps(hist,indent=2));print(rec,flush=True)
  # Separate using average, also cover high-score rows at current point.
  threshold=min(upp);extra=np.where(vv>threshold-5e-5)[0];extra=np.setdiff1d(extra,rows)
  if len(extra)>500:extra=extra[np.argsort(vv[extra])[-500:]]
  if len(extra):
   newrows=np.union1d(rows,extra);pp=np.zeros(len(newrows));pp[np.searchsorted(newrows,rows)]=p;p=pp;rows=newrows;B,d,norm2=setup(rows);sig=.9/(tau*norm2);pavg=p.copy()
  zavg=z.copy();pavg=p.copy()
