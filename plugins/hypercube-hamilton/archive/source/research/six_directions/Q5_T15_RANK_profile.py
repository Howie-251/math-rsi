"""Actual T15 marked orbits in the producer4096 remainder, prioritizing no-T17."""
from pathlib import Path
from itertools import permutations,combinations
from functools import lru_cache
from collections import defaultdict,Counter
import json
P=Path(__file__).resolve().parent
PERM=[tuple(sum(((x>>p[i])&1)<<i for i in range(5)) for x in range(32)) for p in permutations(range(5))]
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
@lru_cache(None)
def canon(minor,major,omit):
 return min((tuple(sorted(m[x^minor] for x in major)),tuple(sorted(m[x^minor] for x in omit))) for m in PERM)
coverage=defaultdict(set);hard=defaultdict(set);witnesses=[];allrecords=[]
for v in (1,7,31):
 raw=(P/f'Q5_T26_RANK_batch_remaining_v{v}.bin').read_bytes()
 for off in range(0,len(raw),9):
  Z=set(raw[off:off+4]);W=set(raw[off+4:off+9]);rid=len(allrecords)
  counts=[(sum((x>>d&1)==(v>>d&1) for x in Z),sum((x>>d&1)==(v>>d&1) for x in W)) for d in range(6)]
  noT17=not any(ab in ((3,1),(0,4)) for ab in counts)
  allrecords.append({'v':v,'input_index':off//9,'record':list(raw[off:off+9]),'no_T17_cut':noT17})
  seen={}
  for d,(a,b) in enumerate(counts):
   A={x for x in range(64) if (x>>d&1)==(v>>d&1)};za=Z&A;wa=W&A
   if (a,b)==(3,2):sources=combinations(za,2);minor=Z-A;major=W-A
   elif (a,b)==(1,4):sources=combinations(wa-{1<<d},2);minor=W-A;major=Z-A
   else:continue
   assert len(minor)==1
   for S in sources:
    U=tuple(sorted(project(x^(1<<d),d) for x in S));M=project(next(iter(minor)),d);J=tuple(sorted([project(x,d) for x in major]+list(U)))
    assert len(J)==5 and len(set(J))==5 and M not in J
    key=canon(M,J,U)
    if key not in seen:seen[key]={'cut':d,'row':[a,b],'sources':list(S),'minority':M,'majority':J,'omitted':U}
  for key,w in seen.items():
   coverage[key].add(rid)
   if noT17:hard[key].add(rid)
   witnesses.append({'record_id':rid,'canonical_majority':key[0],'canonical_omitted':key[1],**w})
assert len(allrecords)==4096 and sum(r['no_T17_cut'] for r in allrecords)==462
rows=[]
for key in sorted(coverage,key=lambda k:(-len(hard[k]),-len(coverage[k]),k)):
 rows.append({'minority':[0],'majority':key[0],'omitted':key[1],'covered_records':len(coverage[key]),'no_T17_records':len(hard[key])})
out={'status':'PRODUCER_PROFILE_ONLY','input_records':4096,'no_T17_records':462,'actual_T15_marked_orbits':len(rows),'rows':rows,'records':allrecords,'witnesses':witnesses}
(P/'Q5_T15_RANK_profile.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('records','witnesses')},indent=2))
