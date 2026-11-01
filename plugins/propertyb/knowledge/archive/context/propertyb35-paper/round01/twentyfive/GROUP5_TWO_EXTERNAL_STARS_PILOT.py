"""Real same-edge/different-outer-group caller for seven locks G+x+y.
Generate every positive-singleton local pair domain for seven remaining group
inventories; run one chosen nontrivial seven-lock pilot per inventory.
"""
from pathlib import Path
from collections import Counter
from itertools import combinations_with_replacement
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent;root=P.parents[3];sys.dont_write_bytecode=True
sys.path[:0]=[str(root/'context/propertyb34/round01/high-math'),str(root/'computations'),str(root/'computations/propertyb33/round01')]
from subset_position_dp import SubsetEngine
from multilock import json_value
st=time.perf_counter();cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text());star=json.loads((P/'GROUP5_EXTERNAL_STAR_COMPLETE.json').read_text());ids=[1,5,7,8,9,10,18]
def extend(mu,p,r,T):
 ns=Counter()
 for t,c in mu.items():
  a=int(t in p) if t else 7-len(p);b=int(t in r) if t else 7-len(r);q=int(t==T)
  ss=[c-a-b+q,a-q,b-q,q]
  if min(ss)<0:return None
  for mask,n in zip([t,t|32,t|64,t|96],ss):ns[mask]+=n
 ns={t:c for t,c in ns.items() if c}
 assert sum(ns.values())==35 and all(t.bit_count()<=5 for t in ns)
 assert all(sum(c for t,c in ns.items() if t>>i&1)==7 for i in range(7))
 assert all(sum(c for t,c in ns.items() if t>>i&1 and t>>j&1)==(2 if j<5 else 1) for i in range(7) for j in range(i+1,7))
 assert all(not(t&96==96) or t==T|96 for t in ns)
 return ns
families=[]
for i in ids:
 mu={int(t):c for t,c in cat['representatives'][i]['counts'].items()};ps=next(f['residual_partitions'] for f in star['families'] if f['id']==i);td=[]
 for T in [1,2,4,8,16]:
  if not mu.get(T,0):continue
  pp=[p for p in ps if T in p];pairs=[]
  for p,r in combinations_with_replacement(pp,2):
   ns=extend(mu,p,r,T)
   if ns is not None:pairs.append(dict(P=p,Q=r))
  td.append(dict(T=T,multiplicity=mu[T],partitions=len(pp),pairs=pairs))
 chosen=min(td,key=lambda z:(len(z['pairs']),z['T']));assert chosen['pairs']
 families.append(dict(id=i,mu=mu,singleton_domains=td,chosen_T=chosen['T'],chosen_pair_count=len(chosen['pairs'])))
results=[]
for f in families:
 d=next(d for d in f['singleton_domains'] if d['T']==f['chosen_T']);p=d['pairs'][0];ns=extend(f['mu'],p['P'],p['Q'],d['T']);tm=time.perf_counter();eng=SubsetEngine(25,7,ns);z=eng.verify(eng.solve())
 results.append(dict(id=f['id'],T=d['T'],P=p['P'],Q=p['Q'],dp_seconds=time.perf_counter()-tm,**z));print(f['id'],d['T'],p,z['bound'],float(z['bound']),flush=True)
summary=dict(scope=__doc__,families=7,all_singleton_domains=sum(len(f['singleton_domains']) for f in families),chosen_pair_domain_total=sum(f['chosen_pair_count'] for f in families),pilot_cases=7,strict=sum(z['bound']<1 for z in results),elapsed_seconds=time.perf_counter()-st)
(P/'GROUP5_TWO_EXTERNAL_STARS_PILOT.json').write_text(json.dumps(json_value(dict(summary=summary,domain=families,results=results)),indent=2)+'\n');print(json.dumps(summary,indent=2))
