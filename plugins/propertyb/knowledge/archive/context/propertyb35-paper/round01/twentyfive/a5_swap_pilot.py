"""Exact pair-type coefficients for the a5 group-preserving swap obstruction.
Diagnostic LP over local pair types only; no enumeration of hypergraphs.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product,permutations
from functools import lru_cache
from math import comb
import json,time
import numpy as np
from scipy.optimize import linprog
P=Path(__file__).resolve().parent;start=time.perf_counter()
parts=[(1,1,1,1,1),(2,1,1,1,0),(2,2,1,0,0),(3,1,1,0,0),(3,2,0,0,0),(4,1,0,0,0),(5,0,0,0,0)]
partindex={tuple(sorted(p)):i for i,p in enumerate(parts)}
qtypes=[sum(comb(x,2) for x in p) for p in parts]
orb=[((1,2,2,3,4),Q(6,23)),((1,2,3,3,3),Q(10,23)),((1,3,3,3,3),Q(3,23)),((2,2,2,3,3),Q(4,23))]
perms=[]
for pattern,w in orb:
    pp=sorted(set(permutations(pattern)));perms.extend((p,w/len(pp)) for p in pp)
local={(r,c,d):Q(comb(5-c-d,r-c),comb(5,r)) if 0<=r-c<=5-c-d else Q() for r in range(6) for c in range(6) for d in range(6-c)}
@lru_cache(None)
def probkey(key):
    if any(c+d>5 for c,d in key):return Q()
    z=Q()
    for r,w in perms:
      x=w
      for ri,(c,d) in zip(r,key):
        x*=local[ri,c,d]
        if not x:break
      z+=x
    return z

def prob(c,d):return probkey(tuple(sorted(zip(c,d))))
def symprob(c,d):return prob(c,d)+prob(d,c)
def coefficient(a,b,t):
    out=Q()
    for j in range(5):
      mult=(a[j]-t[j])*(b[j]-t[j])
      if not mult:continue
      c=[a[i]+b[i]-t[i]-(i==j) for i in range(5)];d=[int(i==j) for i in range(5)]
      out+=mult*symprob(c,d)
    if sum(t)==1:
      j=next(j for j in range(5) if t[j]);m=6-a[j]-b[j]
      assert m>=0
      out+=m*symprob(a,b)
    return 2*out

def compositions(n,k):
    if k==1:yield (n,);return
    for a in range(n+1):
      for b in compositions(n-a,k-1):yield (a,)+b
comps=list(compositions(5,5));patterns=set()
for a in comps:
 for b in comps:
  for t in product(*(range(min(x,y)+1) for x,y in zip(a,b))):
    st=sum(t)
    if st>=5 or any(x+y-z>5 for x,y,z in zip(a,b,t)):continue
    if st>=2 and sum(z>0 for z in t)>1:continue
    x=tuple(sorted(zip(a,b,t)));y=tuple(sorted(zip(b,a,t)));patterns.add(min(x,y))
print('pair types',len(patterns),'generation sec',time.perf_counter()-start,flush=True)
records=[]
for k,z in enumerate(sorted(patterns)):
    a=tuple(x[0] for x in z);b=tuple(x[1] for x in z);t=tuple(x[2] for x in z)
    ia=partindex[tuple(sorted(a))];ib=partindex[tuple(sorted(b))]
    c=coefficient(a,b,t)
    records.append(dict(groups=z,types=[ia,ib],intersection=sum(t),same_group_cross_incidence=sum(x*y for x,y in zip(a,b)),coefficient=c))
    if k%1000==0:print('coeff',k,'cache',probkey.cache_info(),'sec',time.perf_counter()-start,flush=True)
# pair variables + 7 edge-type counts. Equalities explained in REPORT supplement.
n=len(records);rows=[];rhs=[]
def add(fun,val):rows.append([float(fun(r)) for r in records]+[0]*7);rhs.append(float(val))
add(lambda r:1,595)
add(lambda r:r['intersection'],525)
add(lambda r:comb(r['intersection'],2),50)
add(lambda r:r['same_group_cross_incidence'],2875)
for j in range(7):
 row=[r['types'].count(j) for r in records]+[(-34 if l==j else 0) for l in range(7)]
 rows.append(row);rhs.append(0)
rows.append([0]*n+[1]*7);rhs.append(35)
rows.append([0]*n+qtypes);rhs.append(100)
cost=[-float(r['coefficient']) for r in records]+[0]*7
res=linprog(cost,A_eq=np.array(rows),b_eq=np.array(rhs),bounds=[(0,None)]*n+[(0,None)]*6+[(0,5)],method='highs')
active=[]
if res.success:
 for r,x in zip(records,res.x[:n]):
  if x>1e-7:active.append({**r,'lp_count':float(x),'rational_count':str(Q(float(x)).limit_denominator(1000000))})
summary=dict(scope=__doc__,pair_types=n,lp_success=res.success,maximum_lp=float(-res.fun) if res.success else None,required_threshold='114/23',threshold_float=114/23,active_pair_types=active,edge_type_counts=[float(x) for x in res.x[n:]] if res.success else None,coefficient_cache=str(probkey.cache_info()),elapsed_seconds=time.perf_counter()-start)
def convert(x):
 if isinstance(x,Q):return str(x)
 if isinstance(x,dict):return {k:convert(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [convert(v) for v in x]
 return x
(P/'A5_SWAP_PILOT.json').write_text(json.dumps(convert(dict(summary=summary,pair_types=records)),indent=2)+'\n')
print(json.dumps(convert(summary),indent=2))
