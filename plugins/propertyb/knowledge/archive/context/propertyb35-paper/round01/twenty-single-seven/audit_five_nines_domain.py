"""Independent five-star domain: RGS all partitions, symmetric view join, direct Mobius."""
from pathlib import Path
from itertools import combinations,product
from collections import defaultdict
from fractions import Fraction as F
import json,time
HERE=Path(__file__).parent;cpu=time.process_time();wall=time.time()
def canon(P):return tuple(sorted(tuple(B) for B in P))
def partitions(n):
 for tail in product(range(n),repeat=n-1):
  r=(0,)+tail
  if any(r[i]>max(r[:i])+1 for i in range(1,n)):continue
  P=tuple(tuple(i for i in range(n) if r[i]==j) for j in range(max(r)+1))
  if max(map(len,P))<=4:yield P

def restrict(P,S):return canon(tuple(tuple(S.index(i) for i in B if i in S) for B in P if any(i in S for i in B)))
views=defaultdict(list)
for source,cert in [('REFINED_FOUR_DP.json','JOINT_REFINED_FOUR.json'),('FOUR_WITH_TEN_DP.json','JOINT_FOUR_WITH_TEN.json')]:
 rows=json.loads((HERE/source).read_text())['cases'];strict={z['source_id'] for z in json.loads((HERE/cert).read_text())['results'] if F(z.get('bound',2))<1}
 for idx,r in enumerate(rows):
  if r['strict'] or idx in strict:continue
  ns={int(t):n for t,n in r['counts'].items()};I={u:sum(n for t,n in ns.items() if t&(u<<1)==u<<1) for u in range(1,16)}
  views[(tuple(r['neighbor_degrees']),canon(r['partition']))].append(I)
patterns=((9,9,9,9,9),);found=set();rawjoins=0
for ds in patterns:
 for P in partitions(5):
  choices=[]
  for S in combinations(range(5),4):
   cs=[]
   for I in views[(tuple(ds[i] for i in S),restrict(P,S))]:
    cs.append({sum(1<<S[i] for i in range(4) if u>>i&1):n for u,n in I.items()})
   choices.append(cs)
  if any(not a for a in choices):continue
  choices.sort(key=len)
  def visit(j,I):
   global rawjoins
   if j<len(choices):
    for J in choices[j]:
     if all(u not in I or I[u]==n for u,n in J.items()):visit(j+1,I|J)
    return
   rawjoins+=1
   for five in (0,1):
    inc={0:28,**{u:I[u]-sum(all(not(u>>i&1) or i in B for i in range(5)) for B in P) for u in range(1,31)},31:five}
    mu={t:sum((-1)**((u^t).bit_count())*n for u,n in inc.items() if u&t==t) for t in range(32)}
    if min(mu.values())<0:continue
    ns={t<<1:n for t,n in mu.items()};ns[1]=7-len(P)
    for B in P:ns[1+sum(1<<(i+1) for i in B)]=1
    found.add((ds,tuple(sorted((t,n) for t,n in ns.items() if n))))
  visit(0,{})
saved=json.loads((HERE/'FIVE_NINES_DOMAIN.json').read_text())['cases'];target={(tuple(r['neighbor_degrees']),tuple(sorted((int(t),n) for t,n in r['counts'].items() if n))) for r in saved}
assert found==target,(len(found),len(target),len(found-target),len(target-found))
out=dict(status='PASS',scope=__doc__,domain_count=len(found),raw_view_joins=rawjoins,counts_by_degrees={str(ds):sum(s==ds for s,_ in found) for ds in patterns},cpu_seconds=time.process_time()-cpu,wall_seconds=time.time()-wall)
(HERE/'FIVE_NINES_DOMAIN_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
