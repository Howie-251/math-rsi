from pathlib import Path
from itertools import combinations_with_replacement, permutations, product
from collections import Counter
from fractions import Fraction
from math import comb
import json,time
P=Path(__file__).resolve().parent
st=time.process_time()
def C(n,k):return comb(n,k) if 0<=k<=n else 0
def extra(t,r):
 if t=='P':return 0
 if t==0:return C(11,r-5)+C(11,r)
 return C(11+t,r)
def bad(types,a,r):
 return a*C(12,r-4)+(30-a)*C(12,r)-max(a-1,0)*C(8,r-8)+sum(extra(t,r) for t in types)
order=['P',0,2,3,4]
tables={}
for ts in combinations_with_replacement(order,4):
 best=[];fails=[]
 for a in range(31):
  z=min((Fraction(bad(ts,a,r),C(16,r)),r,bad(ts,a,r),C(16,r)) for r in range(17))
  best.append({'a':a,'ratio':str(z[0]),'r':z[1],'U':z[2],'D':z[3]})
  if z[0]>=1:fails.append(a)
 tables[ts]={'types':ts,'fails':fails,'best':best}
allowed=[m for m in range(32) if m.bit_count() in (0,2,3,4)]
perms=[(0,)+q for q in permutations(range(1,5))]
maps=[[sum(1<<p[i] for i in range(5) if m>>i&1) for m in range(32)] for p in perms]
def canon(tr):return min(tuple(sorted(mp[m] for m in tr)) for mp in maps)
domain=list(combinations_with_replacement(allowed,4))
assert len(domain)==23751
orbits=Counter(canon(t) for t in domain)
assert sum(orbits.values())==23751
# Independent domain decomposition: form each representative's orbit explicitly,
# check disjointness and exact equality to the original labeled multiset domain.
seen=set()
for tr,n in orbits.items():
 orb={tuple(sorted(mp[m] for m in tr)) for mp in maps}
 assert len(orb)==n and not seen.intersection(orb)
 seen.update(orb)
assert seen==set(domain)
rows=[];stats=Counter();tail=[]
for tr,labels in sorted(orbits.items()):
 stats['marked_trace_orbits']+=1
 # Each pair is already in F; no pair may occur in all four exceptions.
 if any(sum((m>>i&1) and (m>>j&1) for m in tr)>3 for i in range(5) for j in range(i)):
  stats['pair_filter_orbits']+=1;continue
 if sum(m.bit_count()-1 for m in tr if m&1)>4:
  stats['x_star_cover_filter_orbits']+=1;continue
 h=tuple(sum(m>>v&1 for m in tr) for v in range(5))
 a0=5-h[0]
 ts=[tuple(sorted(('P' if m>>v&1 else m.bit_count() for m in tr),key=order.index)) for v in range(5)]
 if a0 not in tables[ts[0]]['fails']:
  stats['x_anchor_closed_orbits']+=1;continue
 choices=[]
 for v in range(1,5):
  choices.append([a for a in tables[ts[v]]['fails'] if 7<=1+a+h[v]<=13])
 candidates=0
 for rest in product(*choices[:3]):
  last=30-a0-sum(rest)
  if last not in choices[3]:continue
  a=(a0,)+rest+(last,)
  deg=tuple(1+x+y for x,y in zip(a,h))
  ex=sum(max(d-9,0) for d in deg)
  if ex>4 or sum(d==7 for d in deg)>3:continue
  candidates+=1
  tail.append({'traces':tr,'attachments':a,'degrees':deg,'F_high_excess':ex,'orbit_labels':labels})
 rows.append({'traces':tr,'labels':labels,'h':h,'a_x':a0,'types_by_v':ts,'failure_a_by_v':[tables[t]['fails'] for t in ts],'remaining_compositions':candidates})
 if candidates:stats['tail_trace_orbits']+=1
 else:stats['other_anchor_or_degrees_closed_orbits']+=1
stats['tail_compositions']=len(tail)
assert sum(stats[k] for k in ('pair_filter_orbits','x_star_cover_filter_orbits','x_anchor_closed_orbits','other_anchor_or_degrees_closed_orbits','tail_trace_orbits'))==len(orbits)
out={'scope':'Complete marked S4 exception-trace multiset domain; necessary local inputs only, no full H realizability claim. F contains unique degree6 x=bit0; exactly3 seven globally gives at most3 in F; other F degrees>=7; total F excess above9<=4; pair multiplicity<=4; x-star union coverage gives sum(|T|-1)<=4. Full safe r0..16/a0..30 sets used at all anchors.','labeled_traces':23751,'S4_orbits':len(orbits),'stats':dict(stats),'thresholds':list(tables.values()),'rows':rows,'tail':tail,'cpu_seconds':time.process_time()-st}
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS',dict(stats),'CPU',out['cpu_seconds'])
print('TAIL_HEAD',tail[:3])
