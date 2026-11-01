import importlib.util,json,itertools,time
from fractions import Fraction as F
from pathlib import Path
P=Path(__file__).resolve().parent; ROOT=P.parents[2]
s=importlib.util.spec_from_file_location('av',ROOT/'context/propertyb-m6-66-20261029/avoided/verify.py');av=importlib.util.module_from_spec(s);s.loader.exec_module(av);c=av.c;c.M=66
start=time.process_time();rows=[];branches=[]
def ell_for(ds,blocks):
 ell={b:1 for b in blocks}
 for j,d in enumerate(ds):ell[1<<j]=d-sum(bool(b&(1<<j)) for b in blocks)
 ell[0]=66-sum(ell.values());return {t:n for t,n in ell.items() if n}
from functools import lru_cache
from math import comb
@lru_cache(None)
def support_min(d,q):
 if d==0:return 0
 ans=5*d
 for t in range(1,d+1):
  for e in range(t-1,min(comb(t,2),q)+1):
   alpha=max(c.ceilings(t*t,t+2*e),c.ceilings(2*t-e-1,2))
   u=5 if t==1 else max(6,5*alpha)
   ans=min(ans,u+support_min(d-t,q-e))
 return ans
@lru_cache(None)
def quota(f,N):
 q=max(0,c.ceilings(5*f-N,4))
 while support_min(f,q)>N:q+=1
 return q
def deletion(v,pos,ell,j):
 bit=1<<j;other=((1<<len(pos))-1)^bit;typ=[T for T,n in ell.items() if n and T&bit];cells=[]
 for a,T in enumerate(typ):
  for U in typ[a:]:
   cap=c.C(ell[T],2) if T==U else ell[T]*ell[U]
   if cap:cells.append((T,U,cap,c.weight(v,pos,pos[j],T,U)+c.weight(v,pos,pos[j],U,T)))
 core=next(x for x in cells if x[0]==bit and x[1]==bit);rest=[x for x in cells if x!=core];quotas=[]
 for R in range(1<<len(pos)):
  if R&~other:continue
  f=sum(n for T,n in ell.items() if T&bit and not T&R)
  quotas.append((R,quota(f,v-1-R.bit_count())))
 best=None
 for z in itertools.product(*(range(x[2]+1) for x in rest)):
  zcore=max([0]+[q-sum(k for k,cell in zip(z,rest) if not (cell[0]|cell[1])&R) for R,q in quotas])
  if zcore>core[2]:continue
  val=zcore*core[3]+sum(k*cell[3] for k,cell in zip(z,rest))
  if best is None or val<best:best=val
 assert best is not None
 return best

def bound(v,pos,ell):
 dels={pos[j]:deletion(v,pos,ell,j) for j in range(len(pos))};total=F(0)
 for h in range(1,v+1):
  A=sum(n*c.endpoint(v,pos,h,T,True) for T,n in ell.items());B=sum(n*c.endpoint(v,pos,h,T,False) for T,n in ell.items());Q=sum(n*(m-(T==U))*c.weight(v,pos,h,T,U) for T,n in ell.items() for U,m in ell.items());total+=min(A,B,Q-dels.get(h,F(0)))
 return total
def best(v,ds,blocks):
 ans=None
 for shift in (0,-1,1,-2):
  pos=tuple(range(v//2-1+shift,v//2-1+shift+len(ds)))
  for perm in sorted(set(itertools.permutations(ds))):
   ell=ell_for(perm,blocks);u=bound(v,pos,ell)
   row=dict(v=v,degrees=ds,blocks=blocks,assigned=perm,positions=pos,U=str(u),strict=u<1)
   if ans is None or u<F(ans['U']):ans=row
   if u<1:return row
 return ans
for v in range(34,39):
 for d in range(c.ceilings(v-1,5),396//v+1):
  n=2*(v-1)-5*d;emax=d+(396-v*d)//n
  for e in range(d,emax+1):
   r=best(v,[d,e],[3]);rows.append(r)
   if r['strict']:branches.append(dict(v=v,d=d,e=e,status='two_pass'));continue
   t=n-1-(5*e-(v-1))
   if t<=0:branches.append(dict(v=v,d=d,e=e,status='pool_gap',t=t));continue
   # y is chosen minimum-degree in the actual unit-neighbor pool of x.
   budget=396-v*d-n*(e-d)
   fmax=e+budget//t
   fails=[];count=0
   for f in range(e,fmax+1):
    for blocks in ([3,5,6],[7]):
     r=best(v,[d,e,f],blocks);rows.append(r);count+=1
     if not r['strict']:fails.append(r)
   branches.append(dict(v=v,d=d,e=e,n=n,t=t,fmax=fmax,budget=budget,status='three_gap' if fails else 'three_pass',count=count,failures=fails))
result=dict(rows=rows,branches=branches,cpu_seconds=time.process_time()-start,stats=av.stats)
(P/'ADAPTIVE_COMPONENT.json').write_text(json.dumps(result,indent=2))
for v in range(34,39):
 print('v',v,'branches',sum(b['v']==v for b in branches),'gaps',[(b['d'],b['e'],b.get('fmax'),b['status'],len(b.get('failures',[]))) for b in branches if b['v']==v and b['status'] not in ('two_pass','three_pass')])
print('CPU',result['cpu_seconds'])
