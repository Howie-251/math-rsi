"""Actual accepted 41236-domain projection witnesses, then greedy rank-orbit cover."""
from pathlib import Path
from itertools import combinations,permutations
from functools import lru_cache
from collections import Counter
import json,hashlib
P=Path(__file__).resolve().parent
profile=json.loads((P/'Q5_T26_RANK_profile.json').read_text())['rows']
keys={(tuple(r['minority']),tuple(r['majority']),tuple(r['omitted'])):i for i,r in enumerate(profile)}
PERM=[tuple(sum(((x>>p[i])&1)<<i for i in range(5)) for x in range(32)) for p in permutations(range(5))]
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
@lru_cache(None)
def canonical(M,J,U):
 target=3 if (M[0]^M[1]).bit_count()==2 else 15;answers=[]
 for shift in M:
  for m in PERM:
   if m[M[0]^M[1]]==target:answers.append((tuple(sorted(m[x^shift] for x in M)),tuple(sorted(m[x^shift] for x in J)),tuple(sorted(m[x^shift] for x in U))))
 return min(answers)
records=[];by_orbit={i:set() for i in range(len(profile))};inputs={}
for v in (1,7,31):
 name=f'ten_covered_q5_and_t63_remaining_v{v}.bin';raw=(P/name).read_bytes();inputs[name]=hashlib.sha256(raw).hexdigest()
 for off in range(0,len(raw),9):
  Z=set(raw[off:off+4]);W=set(raw[off+4:off+9]);witness={}
  for d in range(6):
   A={x for x in range(64) if (x>>d&1)==(v>>d&1)};za=Z&A;wa=W&A
   if (len(za),len(wa))==(2,1):sources=[tuple(za)];minor=Z-A;major=W-A
   elif (len(za),len(wa))==(0,3):sources=combinations(wa-{1<<d},2);minor=W-A;major=Z-A
   else:continue
   for S in sources:
    U=tuple(sorted(project(x^(1<<d),d) for x in S));M=tuple(sorted(project(x,d) for x in minor));J=tuple(sorted([project(x,d) for x in major]+list(U)))
    key=canonical(M,J,U);i=keys[key]
    if i not in witness:witness[i]={'cut':d,'row':[len(za),len(wa)],'sources':list(S),'local_minority':M,'local_majority':J,'local_omitted':U}
  rid=len(records)
  records.append({'v':v,'input_index':off//9,'record':list(raw[off:off+9]),'witnesses':witness})
  for i in witness:by_orbit[i].add(rid)
assert len(records)==41236
out={'status':'PRODUCER_ACTUAL_DOMAIN_PROJECTIONS','inputs':inputs,'input_count':41236,'records':records,
 'orbit_domain_sizes':{i:len(s) for i,s in by_orbit.items()}}
(P/'Q5_T26_RANK_batch_projection_witnesses.json').write_text(json.dumps(out,indent=2)+'\n')
summary=json.loads((P/'Q5_T26_RANK_batch_summary.json').read_text())
good={r['orbit_index'] for r in summary['reports'] if r['full_rank']};covered=set();greedy=[]
while good:
 i=max(good,key=lambda j:(len(by_orbit[j]-covered),-j));new=by_orbit[i]-covered
 if not new:break
 counts=Counter(records[k]['v'] for k in new);greedy.append({'orbit_index':i,'newly_covered':len(new),'targets':dict(counts)});covered|=new;good.remove(i)
reports=[]
for v in (1,7,31):
 original=[r for r in records if r['v']==v];remaining=[r for k,r in enumerate(records) if r['v']==v and k not in covered]
 raw=bytes(x for r in remaining for x in r['record']);name=f'Q5_T26_RANK_batch_remaining_v{v}.bin';(P/name).write_bytes(raw)
 reports.append({'v':v,'input':len(original),'newly_covered':len(original)-len(remaining),'remaining':len(remaining),'remaining_file':name,'remaining_sha256':hashlib.sha256(raw).hexdigest()})
result={'status':'PRODUCER_ONLY_PENDING_INDEPENDENT_RANK_AND_TRANSFER_REVIEW','input_count':41236,
 'newly_covered':len(covered),'remaining':41236-len(covered),'completed_rank_orbits':summary['completed_orbits'],
 'rank_full_orbits':summary['full_rank_orbits'],'greedy':greedy,'reports':reports,'full_T26_proved':False,'full_P6_proved':False}
(P/'Q5_T26_RANK_batch_coverage.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
