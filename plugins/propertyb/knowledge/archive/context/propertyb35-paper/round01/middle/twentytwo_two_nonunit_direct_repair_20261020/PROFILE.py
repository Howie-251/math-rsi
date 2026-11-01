#!/usr/bin/env python3
from math import comb
from itertools import combinations_with_replacement,permutations
from pathlib import Path
from fractions import Fraction as F
import json,time
P=Path(__file__).resolve().parent;start=time.process_time()
def C(n,k):return comb(n,k) if 0<=k<=n else 0
masks=[m for m in range(32) if m.bit_count() in (0,2,3,4)]
keys=list(combinations_with_replacement(masks,2));assert len(keys)==351
perms=list(permutations(range(5)))
def image(m,p):return sum(1<<p[i] for i in range(5) if m>>i&1)
def orbit(k):return {tuple(sorted((image(k[0],p),image(k[1],p)))) for p in perms}
def exception(mask,v,r):
 j=mask.bit_count()
 if j==0:return C(12,r-5)+C(12,r)
 if mask>>v&1:return 0
 return C(12+j,r)
def one(key):
 kvals=[];rcaps=[]
 for v in range(5):
  caps=[]
  for r in range(9,18):
   D=C(17,r);R=C(13,r-4);B=C(13,r);J=C(9,r-8)
   E=sum(exception(m,v,r) for m in key)
   good=[c for c in range(33) if c*R+(32-c)*B-max(c-1,0)*J+E<D]
   assert good==list(range(len(good))) # Monotone strict-safe initial segment.
   caps.append(dict(outside_red=r,sample=D,red_count=R,blue_count=B,joint_floor=J,exception_count=E,max_safe_c=max(good,default=-1)))
  k=max(a['max_safe_c'] for a in caps)+1
  kvals.append(k);rcaps.append(caps)
 return dict(traces=list(key),sizes=[m.bit_count() for m in key],intersection=(key[0]&key[1]).bit_count(),multiplicities=[sum(bool(m>>v&1) for m in key) for v in range(5)],k=kvals,sum_k=sum(kvals),unconditional=sum(kvals)>32,per_point_r_caps=rcaps)
def feasible(row,delta=0,Delta=35,cover=False):
 lo=[];hi=[]
 for v,mv in enumerate(row['multiplicities']):
  lower=max(0,row['k'][v],delta-1-mv)
  if cover:
   ext=sum(5-m.bit_count() for m in row['traces'] if m>>v&1)
   lower=max(lower,(17-ext+3)//4)
  lo.append(lower);hi.append(min(32,Delta-1-mv))
 if any(a>b for a,b in zip(lo,hi)) or sum(lo)>32 or sum(hi)<32:return None
 witness=lo[:];remaining=32-sum(lo)
 for i in range(5):take=min(remaining,hi[i]-witness[i]);witness[i]+=take;remaining-=take
 assert remaining==0
 return dict(attachment_lower=lo,attachment_upper=hi,attachment_witness=witness,degree_witness=[1+a+m for a,m in zip(witness,row['multiplicities'])])
rows=[];seen=set()
for key in keys:
 if key in seen:continue
 orb=orbit(key);seen|=orb;rep=min(orb);assert rep==key
 row=one(key);row['orbit_size']=len(orb);row['members']=[list(k) for k in sorted(orb)]
 row['remaining_modes']={}
 for name,d,D,cov in [('general',0,35,False),('Delta9',0,9,False),('Delta8',0,8,False),('delta6_paircover',6,35,True),('delta7_paircover',7,35,True),('delta6_Delta9_paircover',6,9,True),('delta7_Delta9_paircover',7,9,True)]:
  row['remaining_modes'][name]=feasible(row,d,D,cov)
 rows.append(row)
assert seen==set(keys)
summary={name:dict(residual_orbits=sum(r['remaining_modes'][name] is not None for r in rows),residual_labeled=sum(r['orbit_size'] for r in rows if r['remaining_modes'][name] is not None)) for name in rows[0]['remaining_modes']}
result=dict(scope='22-point qGamma(F)=2, two actual exception traces; only threshold-based oneRED/F and outside-red9..17 samples; not H enumeration',labeled_trace_pairs=len(keys),orbits=len(rows),summary=summary,cases=rows,cpu_seconds=time.process_time()-start)
P.joinpath('PROFILE.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))
for r in rows: print(r['traces'],r['sizes'],r['intersection'],r['k'],r['sum_k'], [k for k,v in r['remaining_modes'].items() if v is not None])
