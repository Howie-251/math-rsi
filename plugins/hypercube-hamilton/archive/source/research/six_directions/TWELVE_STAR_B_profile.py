"""Exact marked B geometry choices for the first30 root-star class."""
from pathlib import Path
from itertools import combinations,permutations
from collections import Counter
import json
P=Path(__file__).resolve().parent
Z=(7,11,13,19,21);units=(1,2,4,8,16)
maps=[tuple(sum(((x>>q[d])&1)<<d for d in range(5)) for x in range(32)) for q in permutations(range(5))]
def canonical(J,U):
 candidates=[((tuple(sorted(tr[x] for x in J)),tuple(sorted(tr[x] for x in U))),q) for q,tr in enumerate(maps)]
 return min(candidates)
groups={};choices=[]
for t in Z:
 for pair in combinations(units,2):
  U=set(units)-set(pair);J=(set(Z)-{t})|U;key,mapindex=canonical(J,U)
  groups.setdefault(key,[]).append((t,pair))
  choices.append({'consumed_t':t,'pair':pair,'omitted':sorted(U),'majority':sorted(J),'canonical_key':key,'permutation_index_to_canonical':mapindex})
keys=sorted(groups);index={key:i for i,key in enumerate(keys)}
rows=[]
for key in keys:
 J,U=key;pq=sorted(set(units)-set(U))
 rows.append({'index':index[key],'minority':[0],'majority':J,'omitted':U,'forced_pair':pq,'raw_choices':groups[key]})
for choice in choices:
 choice['orbit_index']=index[tuple(tuple(x) for x in choice.pop('canonical_key'))]
out={'status':'PRODUCER_EXACT_MARKED_GEOMETRY_ONLY','Z0':Z,'raw_unordered_choices':50,'canonical_marked_classes':len(rows),'rows':rows,'choices':choices,'star_Q6_closed':False,'A_mixed_opening_interface_proved':False}
(P/'TWELVE_STAR_B_profile.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'canonical_classes':len(rows),'rows':rows},indent=2))
