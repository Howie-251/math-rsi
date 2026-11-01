"""Eighteen actual forced high-codegree B-B inputs of type23.
Only two Π shapes (equal/different), with codegree4/5 and optional common
singleton. Exact stabilizer S2xS3 transports six representative layouts.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations_with_replacement,permutations
from collections import Counter
import json,sys,time
P=Path(__file__).resolve().parent;root=P.parents[3];sys.dont_write_bytecode=True
sys.path[:0]=[str(root/'context/propertyb34/round01/high-math'),str(root/'computations'),str(root/'computations/propertyb33/round01')]
from subset_position_dp import SubsetEngine
from multilock import json_value
st=time.perf_counter();cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text());mu={int(t):c for t,c in cat['representatives'][23]['counts'].items()};bs=[(3,4,24),(3,8,20),(3,12,16)];maps=[]
for p2 in permutations([0,1]):
 for p3 in permutations([2,3,4]):
  mm=list(p2)+list(p3)+[5,6];maps.append((mm,[sum(1<<mm[i] for i in range(7) if t>>i&1) for t in range(128)]))
def canon(ns):
 best=None;bestm=None
 for m,tab in maps:
  k=tuple(sorted((tab[t],c) for t,c in ns.items()))
  if best is None or k<best:best=k;bestm=m
 return best,bestm
def split(p,r,q):
 ns=Counter()
 for t,c in mu.items():
  a=int(t in p) if t else 7-len(p);b=int(t in r) if t else 7-len(r);v=q.get(t,0);vv=[c-a-b+v,a-v,b-v,v];assert min(vv)>=0
  for mask,n in zip([t,t+32,t+64,t+96],vv):ns[mask]+=n
 return {t:c for t,c in ns.items() if c}
results=[];cache={};solved=0
for p,r in combinations_with_replacement(bs,2):
 for lam in [4,5]:
  js=[0,1] if p==r else [None]
  for j in js:
   q={3:1}
   if p==r:
    pair=next(t for t in p if t!=3 and t.bit_count()==2);single=next(t for t in p if t.bit_count()==1);q[pair]=1
    if j:q[single]=1
    q[0]=lam-2-j
   else:q[0]=lam-1
   ns=split(p,r,q);key,m=canon(ns);eng=SubsetEngine(25,7,ns)
   if key in cache:
    cp=cache[key];w=dict(positions=[cp[m[i]] for i in range(7)],counts=ns)
    # Evaluate the transported layout directly, not another DP.
    from multilock import Profile,rows,total_bound
    from pure_quota import certificate
    pr=Profile(25,5,w['positions'],ns);cs=[certificate(pr,i) for i in range(7)];w['bound']=total_bound(rows(pr,deductions={pr.positions[i]:cs[i]['loss'] for i in range(7)}))
   else:
    w=eng.solve();cp=[0]*7
    for i,jj in enumerate(m):cp[jj]=w['positions'][i]
    cache[key]=cp;solved+=1
   w=eng.verify(w);raw=sum(min(rr['A'],rr['B'],rr['C']) for rr in w['rows']);results.append(dict(id=23,T=3,P=p,Q=r,joint=q,codegree=lam,equal_partitions=p==r,common_singleton_selected=j,raw_ABC_bound=raw,**w))
summary=dict(scope=__doc__,cases=len(results),representative_DP_solves=solved,strict=sum(z['raw_ABC_bound']<1 for z in results),maximum_raw=max(z['raw_ABC_bound'] for z in results),elapsed_seconds=time.perf_counter()-st)
(P/'K5_TYPE23_HIGH_PAIR.json').write_text(json.dumps(json_value(dict(summary=summary,results=results)),indent=2)+'\n');print(json.dumps(json_value(summary),indent=2));print([(z['equal_partitions'],z['codegree'],z['common_singleton_selected'],str(z['raw_ABC_bound'])) for z in results[:8]])
