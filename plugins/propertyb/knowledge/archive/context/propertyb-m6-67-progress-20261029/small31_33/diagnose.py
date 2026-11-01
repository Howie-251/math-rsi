"""Exact exploratory link-component quota and local probability check; M=66."""
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path
import importlib.util,itertools,json,time
ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('kernel',ROOT/'propertyB_small_k/propertyB_m6_certificate.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c);c.M=66
@lru_cache(None)
def support_min(d,q):
    """Lower bound on union size, relaxed over graph-component (t,e)."""
    if d==0:return 0
    ans=5*d
    for t in range(1,d+1):
      for e in range(t-1,min(comb(t,2),q)+1):
        alpha=c.ceilings(t*t,t+2*e)
        alpha=max(alpha,c.ceilings(2*t-e-1,2))
        u=5 if t==1 else max(6,5*alpha)
        if e<comb(t,2)-t//2:u=max(u,11)
        ans=min(ans,u+support_min(d-t,q-e))
    return ans
@lru_cache(None)
def quota(v,d):
    old=max(0,c.ceilings(5*d-(v-1),4))
    q=old
    while support_min(d,q)>v-1:q+=1
    return q
old_delete=c.bad_pair_deletion
def strengthened(v,pos,ell,j):
    h=pos[j];d=sum(n for T,n in ell.items() if T&(1<<j));q=quota(v,d)
    typ=[T for T in ell if T&(1<<j)];cells=[]
    for i,T in enumerate(typ):
      for U in typ[i:]:
        cap=comb(ell[T],2) if T==U else ell[T]*ell[U]
        if cap:cells.append((c.weight(v,pos,h,T,U)+c.weight(v,pos,h,U,T),cap))
    val=F(0)
    for w,cap in sorted(cells):
      z=min(q,cap);val+=z*w;q-=z
    assert q==0
    return val
c.bad_pair_deletion=strengthened

def two(v,d,e,l=1):return {0:66-d-e+l,1:d-l,2:e-l,3:l}
def best(v,ell):
    return min((c.profile_bound(v,p,ell),p) for p in itertools.permutations(range(v//2-6,v//2+8),len(next(iter(ell.values()))) if False else 2))
def main():
    start=time.process_time();data=[]
    for v in (31,32,33):
      for d in range(c.ceilings(v-1,5),396//v+1):
        n=2*(v-1)-5*d
        if n<=0:continue
        upper=d+(396-v*d)//n
        for e in range(d,upper+1):
          U,p=best(v,two(v,d,e))
          data.append(dict(v=v,d=d,e=e,lam=1,U=str(U),positions=p,strict=U<1,quotas=[quota(v,d),quota(v,e)]))
    print(json.dumps({'rows':data,'failures':[x for x in data if not x['strict']],'cpu_seconds':time.process_time()-start},indent=2))
if __name__=='__main__':main()
