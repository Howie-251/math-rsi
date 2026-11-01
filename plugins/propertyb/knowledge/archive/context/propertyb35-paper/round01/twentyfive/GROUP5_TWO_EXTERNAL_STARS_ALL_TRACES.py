"""All 193 positive-singleton pair cases of the four still surviving inventories.
Use exact S5 on G and interchange x/y to transport already computed layouts.
No unknown outer-point labels or hypergraphs are enumerated.
"""
from pathlib import Path
from itertools import permutations
from collections import Counter
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent;root=P.parents[3];sys.dont_write_bytecode=True
sys.path[:0]=[str(root/'context/propertyb34/round01/high-math'),str(root/'computations'),str(root/'computations/propertyb33/round01')]
from subset_position_dp import SubsetEngine
from multilock import json_value
src=json.loads((P/'GROUP5_TWO_EXTERNAL_STARS_PILOT.json').read_text());old=json.loads((P/'GROUP5_TWO_EXTERNAL_STARS_COMPLETE.json').read_text());st=time.perf_counter();maps=[]
for p in permutations(range(5)):
 for sw in [False,True]:
  m=list(p)+([6,5] if sw else [5,6]);maps.append((m,[sum(1<<m[i] for i in range(7) if t>>i&1) for t in range(128)]))
def canon(ns):
 best=None;bestm=None
 for m,tab in maps:
  k=tuple(sorted((tab[t],c) for t,c in ns.items()))
  if best is None or k<best:best=k;bestm=m
 return best,bestm

def inventory(mu,p,r,T):
 ns=Counter()
 for t,c in mu.items():
  a=int(t in p) if t else 7-len(p);b=int(t in r) if t else 7-len(r);q=int(t==T)
  vals=[c-a-b+q,a-q,b-q,q];assert min(vals)>=0
  for mask,n in zip([t,t|32,t|64,t|96],vals):ns[mask]+=n
 return {t:c for t,c in ns.items() if c}
cache={}
for z in old['results']:
 ns={int(t):c for t,c in z['counts'].items()};key,m=canon(ns);cp=[0]*7
 for i,j in enumerate(m):cp[j]=z['positions'][i]
 cache[key]=(Q(z['bound']),cp)
results=[];solved=transported=0
for f in src['domain']:
 if f['id']not in [1,5,9,10]:continue
 mu={int(t):c for t,c in f['mu'].items()}
 for dd in f['singleton_domains']:
  for pair in dd['pairs']:
   ns=inventory(mu,pair['P'],pair['Q'],dd['T']);key,m=canon(ns);eng=SubsetEngine(25,7,ns);tm=time.perf_counter()
   if key in cache:
    bound,cp=cache[key];z=dict(bound=bound,positions=[cp[m[i]] for i in range(7)],counts=ns);transported+=1
   else:
    z=eng.solve();cp=[0]*7
    for i,j in enumerate(m):cp[j]=z['positions'][i]
    cache[key]=(z['bound'],cp);solved+=1
   z=eng.verify(z);results.append(dict(id=f['id'],T=dd['T'],P=pair['P'],Q=pair['Q'],dp_or_replay_seconds=time.perf_counter()-tm,**z))
 print(f['id'],'complete cases',sum(z['id']==f['id'] for z in results),flush=True)
summary=dict(scope=__doc__,cases=len(results),strict=sum(z['bound']<1 for z in results),new_DP_solves=solved,transported_witnesses=transported,canonical_cases=len(cache),elapsed_seconds=time.perf_counter()-st)
(P/'GROUP5_TWO_EXTERNAL_STARS_ALL_TRACES.json').write_text(json.dumps(json_value(dict(summary=summary,results=results)),indent=2)+'\n');print(json.dumps(summary,indent=2))
