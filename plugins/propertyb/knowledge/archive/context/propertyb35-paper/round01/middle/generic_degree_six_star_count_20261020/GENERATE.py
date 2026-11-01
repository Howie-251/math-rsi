"""All six4links covering20points, excess4; exact balanced-star count."""
from pathlib import Path
from itertools import combinations,combinations_with_replacement,product,permutations
from math import comb
import json,time
P=Path(__file__).resolve().parent;st=time.process_time();D=comb(20,10)
def C(n,k):return comb(n,k) if 0<=k<=n else 0
supports={m:[sum(1<<i for i in z) for z in combinations(range(6),m)] for m in range(2,6)}
patterns=[(2,2,2,2),(3,2,2),(3,3),(4,2),(5,)]
def blocks(key):
 B=[set() for _ in range(6)]
 for p,s in enumerate(key):
  for i in range(6):
   if s>>i&1:B[i].add(p)
 if max(map(len,B))>4:return None
 nxt=len(key)
 for b in B:
  while len(b)<4:b.add(nxt);nxt+=1
 assert nxt==20
 if len({frozenset(b) for b in B})!=6:return None
 return [sum(1<<p for p in b) for b in B]
def count(lm):
 U=[0]*64
 for s in range(1,64):lo=s&-s;U[s]=U[s^lo]|lm[lo.bit_length()-1]
 both=0
 for r in range(1,64):
  b=63^r
  while b:
   if not U[r]&U[b]:both+=(-1 if (r.bit_count()+b.bit_count())%2 else 1)*C(20-U[r].bit_count()-U[b].bit_count(),10-U[r].bit_count())
   b=(b-1)&(63^r)
 return D-both
acts=[]
for p in permutations(range(6)):acts.append([sum(1<<p[i] for i in range(6) if s>>i&1) for s in range(64)])
result=[]
for pat in patterns:
 group={m:pat.count(m) for m in set(pat)};parts=[list(combinations_with_replacement(supports[m],num)) for m,num in group.items()]
 raw={tuple(sorted(z for group in x for z in group)) for x in product(*parts)}
 domain={k for k in raw if blocks(k) is not None};unseen=set(domain);orbits=[]
 while unseen:
  rep=min(unseen);orb={tuple(sorted(a[s] for s in rep)) for a in acts};assert orb<=unseen
  unseen-=orb;lm=blocks(rep);v=count(lm)
  orbits.append({'representative_repeat_supports':rep,'repeat_point_link_subsets':[[i for i in range(6) if s>>i&1] for s in rep],'orbit_size':len(orb),'orbit_members':sorted(orb),'block_repeated_occupancy':[sum(s>>i&1 for s in rep) for i in range(6)],'link_masks':lm,'C_count':v})
 orbits.sort(key=lambda z:(z['C_count'],z['representative_repeat_supports']))
 result.append({'repeat_multiplicities':pat,'raw_labels':len(raw),'valid_labels':len(domain),'excluded_labels':sorted(raw-domain),'orbits':orbits,'orbit_count':len(orbits),'minimum_C':orbits[0]['C_count'],'minimum_shapes':[r['representative_repeat_supports'] for r in orbits if r['C_count']==orbits[0]['C_count']]})
out={'scope':__doc__,'balanced_sample_count':D,'complete':True,'patterns':result,'raw_labels':sum(r['raw_labels'] for r in result),'valid_labels':sum(r['valid_labels'] for r in result),'orbit_count':sum(r['orbit_count'] for r in result),'minimum_C':min(r['minimum_C'] for r in result),'cpu_seconds':time.process_time()-st}
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='patterns'});print([(r['repeat_multiplicities'],r['raw_labels'],r['valid_labels'],r['orbit_count'],r['minimum_C'],r['minimum_shapes']) for r in result])
