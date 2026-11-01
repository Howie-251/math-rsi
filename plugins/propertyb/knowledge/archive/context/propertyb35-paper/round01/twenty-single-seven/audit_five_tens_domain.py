"""Independent domain description: RGS partitions + direct inclusion/exclusion inventory."""
from pathlib import Path
from itertools import product,combinations
from math import prod
import json,time
HERE=Path(__file__).parent
start=time.process_time();wall=time.time()
def partitions(n):
 for a in product(range(n),repeat=n-1):
  r=(0,)+a
  if any(r[i]>1+max(r[:i]) for i in range(1,n)):continue
  yield tuple(tuple(i for i in range(n) if r[i]==b) for b in range(max(r)+1))
def can(P):return tuple(sorted(tuple(sorted(B)) for B in P))
def moments(ns,n):return {u:sum(c for t,c in ns.items() if (t>>1)&u==u) for u in range(1,1<<n)}
old=json.loads((HERE/'UNIT_FOUR_DP.json').read_text())['cases']
allowed=set()
for r in old:
 if r['neighbor_degrees']!=[10]*4 or r['strict']:continue
 I=moments({int(t):n for t,n in r['counts'].items()},4)
 allowed.add((can(r['partition']),tuple(I[u] for u in range(1,16))))
found=set()
for P in partitions(5):
 if any(len(B)>4 for B in P):continue
 tri=list(combinations(range(5),3))
 for vals in product((0,1),repeat=10):
  I={u:(10 if u.bit_count()==1 else 3 if u.bit_count()==2 else 0) for u in range(1,32)}
  I.update({sum(1<<i for i in S):v for S,v in zip(tri,vals)})
  valid=True
  for S in combinations(range(5),4):
   pr=can(tuple(tuple(S.index(i) for i in B if i in S) for B in P if any(i in S for i in B)))
   local=tuple(I[sum(1<<S[i] for i in range(4) if u>>i&1)] for u in range(1,16))
   if (pr,local) not in allowed:valid=False;break
  if not valid:continue
  J={0:28,**{u:I[u]-sum(all(not(u>>i&1) or i in B for i in range(5)) for B in P) for u in range(1,32)}}
  mu={t:sum((-1)**((u^t).bit_count())*v for u,v in J.items() if u&t==t) for t in range(32)}
  if min(mu.values())<0:continue
  ns={t<<1:v for t,v in mu.items()};ns[1]=7-len(P)
  for B in P:ns[1+sum(1<<(i+1) for i in B)]=1
  found.add(tuple(sorted((t,n) for t,n in ns.items() if n)))
saved=json.loads((HERE/'FIVE_TENS.json').read_text())['cases'];target={tuple(sorted((int(t),n) for t,n in r['counts'].items() if n)) for r in saved}
assert found==target
out=dict(status='PASS',scope='Independent RGS/direct Mobius necessary-domain equality for five degree10 unit neighbours; no independent arithmetic replay here',domain_count=len(found),cpu_seconds=time.process_time()-start,wall_seconds=time.time()-wall)
(HERE/'FIVE_TENS_DOMAIN_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
