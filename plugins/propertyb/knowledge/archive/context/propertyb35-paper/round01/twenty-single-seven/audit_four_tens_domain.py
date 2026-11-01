"""Independent RGS/direct-Mobius generator for the 332 four degree10 unit-neighbour inventories."""
from pathlib import Path
from itertools import combinations,product
from fractions import Fraction as F
import json,time
HERE=Path(__file__).parent;start=time.time();cpu=time.process_time()
def canon(P):return tuple(sorted(tuple(B) for B in P))
def parts():
 for tail in product(range(4),repeat=3):
  r=(0,)+tail
  if any(r[i]>max(r[:i])+1 for i in range(1,4)):continue
  yield tuple(tuple(i for i in range(4) if r[i]==j) for j in range(max(r)+1))
def restrict(P,S):return canon(tuple(tuple(S.index(i) for i in B if i in S) for B in P if any(i in S for i in B)))
old=json.loads((HERE/'UNIT_THREE.json').read_text())['cases'];strict=set()
lookup={}
for idx,r in enumerate(old):
 if r['strict'] or idx in strict:continue
 key=(tuple(r['neighbor_degrees']),tuple(r['neighbor_codegrees']),canon(r['partition']))
 lookup.setdefault(key,set()).add(r['neighbor_triple'])
patterns=((10,10,10,10),);pairs=list(combinations(range(4),2));triples=list(combinations(range(4),3));found=set()
for ds in patterns:
 for P in parts():
  for cs in product((1,2,3),repeat=6):
   pm=dict(zip(pairs,cs));choices=[lookup.get((tuple(ds[i] for i in S),tuple(pm[q] for q in combinations(S,2)),restrict(P,S)),()) for S in triples]
   if any(not a for a in choices):continue
   for ts in product(*choices):
    for q in range(min(ts)+1):
     I={**{1<<i:ds[i] for i in range(4)},**{sum(1<<i for i in S):n for S,n in zip(pairs,cs)},**{sum(1<<i for i in S):n for S,n in zip(triples,ts)},15:q}
     J={0:28,**{u:n-sum(all(not(u>>i&1) or i in B for i in range(4)) for B in P) for u,n in I.items()}}
     mu={t:sum((-1)**((u^t).bit_count())*n for u,n in J.items() if u&t==t) for t in range(16)}
     if min(mu.values())<0:continue
     ns={t<<1:n for t,n in mu.items()};ns[1]=7-len(P)
     for B in P:ns[1+sum(1<<(i+1) for i in B)]=1
     found.add((ds,tuple(sorted((t,n) for t,n in ns.items() if n))))
target=set()
for filename in ['UNIT_FOUR_DOMAIN.json']:
 for r in json.loads((HERE/filename).read_text())['cases']:
  if r['neighbor_degrees']!=[10]*4:continue
  target.add((tuple(r['neighbor_degrees']),tuple(sorted((int(t),n) for t,n in r['counts'].items() if n))))
assert found==target,(len(found),len(target),len(found-target),len(target-found))
result=dict(status='PASS',scope=__doc__,inventory_count=len(found),cpu_seconds=time.process_time()-cpu,wall_seconds=time.time()-start)
(HERE/'FOUR_TENS_DOMAIN_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
