"""Actual marked T37 orbit profile of conservative348283 twelve-hole remainder."""
from pathlib import Path
from itertools import permutations,combinations
from collections import Counter,defaultdict
import json,struct,hashlib
P=Path(__file__).resolve().parent
rows=json.loads((P/'Q5_T37_INDEPENDENT_geometry.json').read_text())['rows']
maps=[tuple(sum(((x>>p[i])&1)<<i for i in range(5)) for x in range(32)) for p in permutations(range(5))]
odd=[x for x in range(32) if x.bit_count()%2];oi={x:i for i,x in enumerate(odd)}
def key(M,J,U):return sum(1<<x for x in M)|(sum(1<<oi[x] for x in J)<<32)|(sum(1<<oi[x] for x in U)<<48)
lookup={}
for row in rows:
 for shift in row['minority']:
  for m in maps:
   k=key([m[x^shift] for x in row['minority']],[m[x^shift] for x in row['majority']],[m[x^shift] for x in row['omitted']])
   assert k not in lookup or lookup[k]==row['index'];lookup[k]=row['index']
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
counts=Counter();targetcounts=defaultdict(Counter);reports=[];witness=bytearray();hashes={}
for v in (1,7,31):
 for free in (False,True):
  name=f"HIGHER_Q5_FULL_reuse_remaining_h12_v{v}_{'free' if free else 'covered'}.bin";raw=(P/name).read_bytes();hashes[name]=hashlib.sha256(raw).hexdigest();withT37=0
  for off in range(0,len(raw),11):
   Z=raw[off:off+5];W=raw[off+5:off+11];seen={}
   for d in range(6):
    za=[x for x in Z if (x>>d&1)==(v>>d&1)];wa=[x for x in W if (x>>d&1)==(v>>d&1)]
    if (len(za),len(wa))==(2,1):pool=za;minor=[x for x in Z if x not in za];major=[x for x in W if x not in wa]
    elif (len(za),len(wa))==(0,3):pool=[x for x in wa if x!=(1<<d) and (not free or x!=v)];minor=[x for x in W if x not in wa];major=[x for x in Z if x not in za]
    else:continue
    for S in combinations(pool,2):
     M=[project(x,d) for x in minor];U=[project(x,d) for x in S];J=[project(x,d) for x in major]+U;shift=min(M)
     k=key([x^shift for x in M],[x^shift for x in J],[x^shift for x in U]);assert k in lookup
     i=lookup[k]
     if i not in seen:seen[i]=(d,S)
   if seen:withT37+=1
   for i,(d,S) in seen.items():
    counts[i]+=1;targetcounts[i][f'{v}_{int(free)}']+=1
    witness.extend(struct.pack('<BBIBBQ',v,int(free),off//11,i,d,sum(1<<x for x in S)))
  reports.append({'v':v,'free_target':free,'input':len(raw)//11,'has_T37_projection':withT37,'without_T37_projection':len(raw)//11-withT37})
(P/'HIGHER_Q5_FULL_T37_projection_witnesses.bin').write_bytes(witness)
out={'status':'PRODUCER_GEOMETRY_PROFILE_ONLY_NO_LOCAL_RANK_ACCEPTANCE','input':348283,'lookup_entries':len(lookup),'reports':reports,'orbit_counts':[{'index':i,'actual_records':counts[i],'targets':dict(targetcounts[i])} for i in sorted(counts,key=lambda j:(-counts[j],j))],
 'input_hashes':hashes,'witness_record_bytes':16,'witness_records':len(witness)//16,'full_twelve_hole_proved':False,'full_P6_proved':False}
(P/'HIGHER_Q5_FULL_T37_profile.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('input_hashes','orbit_counts')},indent=2));print('top',out['orbit_counts'][:12])
