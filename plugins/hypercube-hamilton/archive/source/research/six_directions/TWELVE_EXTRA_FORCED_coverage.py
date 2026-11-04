"""Candidate single-forced-cherry local classifications on frozen37405 actual records."""
from pathlib import Path
from itertools import combinations,permutations
from collections import Counter
import json,struct,hashlib
P=Path(__file__).resolve().parent
summary=json.loads((P/'TWELVE_EXTRA_FORCED_summary.json').read_text())
assert summary['count']==len(summary['reports'])==15
assert json.loads((P/'HIGHER_FORCED_CHERRY_REVIEW.json').read_text())['verdict']=='PASS'
maps=[tuple(sum(((x>>p[i])&1)<<i for i in range(5)) for x in range(32)) for p in permutations(range(5))]
def masks(M,J,U):return sum(1<<x for x in M),sum(1<<x for x in J),sum(1<<x for x in U)
lookup={};geometry={}
for r in summary['reports']:
 assert r['rank']==1024 and r['reduced_endpoints']==22 and r['covered_endpoints']==24
 g=r['geometry'];i=r['index'];assert g['type']=='T17';geometry[i]=g
 R=r['forced_pair'];h=r['forced_hole']
 assert len(R)==2 and set(R)=={h^(1<<d) for d in range(5)}-set(g['omitted'])
 for anchor in g['minority']:
  for tr in maps:
   key=masks([tr[x^anchor] for x in g['minority']],[tr[x^anchor] for x in g['majority']],[tr[x^anchor] for x in g['omitted']])
   value=(i,sum(1<<tr[x^anchor] for x in R))
   assert key not in lookup or lookup[key]==value
   lookup[key]=value
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
witness=bytearray();reports=[];inputhashes={};firstcounts=Counter()
for v in (1,7,31):
 name=f'TWELVE_EXTRA_TYPES_positive_remaining_v{v}.bin';raw=(P/name).read_bytes();inputhashes[name]=hashlib.sha256(raw).hexdigest()
 remaining=bytearray();covered=0
 for off in range(0,len(raw),11):
  Z=raw[off:off+5];W=raw[off+5:off+11];found=None
  for d in range(6):
   za=[x for x in Z if (x>>d&1)==(v>>d&1)];wa=[x for x in W if (x>>d&1)==(v>>d&1)];s=len(za)+1-len(wa)
   if s>=3:
    if not wa:continue
    pool=za;minor=[x for x in Z if x not in za];major=[x for x in W if x not in wa]
   elif s<=-3:
    s=-s;pool=[x for x in wa if x!=(1<<d)];minor=[x for x in W if x not in wa];major=[x for x in Z if x not in za]
   else:continue
   if (len(minor),len(major)+s,s) != (1,7,3):continue
   for S in combinations(pool,s):
    M=[project(x,d) for x in minor];U=[project(x,d) for x in S];J=[project(x,d) for x in major]+U;anchor=min(M)
    key=masks([x^anchor for x in M],[x^anchor for x in J],[x^anchor for x in U])
    candidate=lookup.get(key)
    if candidate is None:continue
    index,normR=candidate;actualR=sum(1<<(x^anchor) for x in range(32) if normR>>x&1)
    assert actualR.bit_count()==2 and not actualR&(masks(M,J,U)[0]|masks(M,J,U)[1])
    if (v>>d&1) and actualR&1:continue
    found=(index,d,sum(1<<x for x in S),*masks(M,J,U),actualR);break
   if found:break
  if found:
   covered+=1;index,d,S,M,J,U,R=found;firstcounts[index]+=1
   witness.extend(struct.pack('<BIHBQIIII',v,off//11,index,d,S,M,J,U,R))
  else:remaining.extend(raw[off:off+11])
 output=f'TWELVE_EXTRA_FORCED_safe_remaining_v{v}.bin';(P/output).write_bytes(remaining)
 reports.append({'v':v,'input':len(raw)//11,'safe_covered':covered,'remaining':len(remaining)//11,'remaining_file':output,'remaining_sha256':hashlib.sha256(remaining).hexdigest()})
 print(reports[-1],flush=True)
(P/'TWELVE_EXTRA_FORCED_safe_witnesses.bin').write_bytes(witness)
out={'status':'PRODUCER_CONDITIONAL_LOCAL_CLASSES_AND_APPLICATION_PENDING_REVIEW','input':1281,'conditional_local_classes':15,'safe_covered':sum(r['safe_covered'] for r in reports),'remaining':sum(r['remaining'] for r in reports),'generic_forced_transfer_import_PASS':True,'local_conditional_certificates_not_yet_accepted':True,'reports':reports,'first_witness_indices':dict(firstcounts),'witness_record_bytes':32,'input_hashes':inputhashes,'full_twelve_hole_proved':False,'full_P6_proved':False}
assert len(witness)==out['safe_covered']*32
(P/'TWELVE_EXTRA_FORCED_coverage.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('reports','input_hashes')},indent=2))
