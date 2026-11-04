"""Producer exact union coverage and forced-OB projection witnesses."""
from pathlib import Path
from itertools import permutations,combinations
from functools import lru_cache
from collections import Counter
import json,hashlib
R=Path(__file__).resolve().parent
unforced=json.loads((R/'Q5_T17_RANK_batch_summary.json').read_text())['orbits']
forced=json.loads((R/'Q5_T17_RANK_forced_summary.json').read_text())['orbits']
lookup={};forcedlookup={}
for a in unforced:
 assert a['full_rank'];g=a['marked_geometry'];lookup[(tuple(g['majority']),tuple(g['omitted']))]=a['id']
for a in forced:
 assert a['full_reduced_rank'];g=a['marked_geometry'];forcedlookup[(tuple(g['majority']),tuple(g['omitted']))]=(a['id'],g['forced_cherry_pair'])
perms=list(permutations(range(5)));maps=[tuple(sum(((x>>j)&1)<<p[j] for j in range(5)) for x in range(32)) for p in perms]
@lru_cache(None)
def canonical(major,om):
 return min((tuple(sorted(m[x] for x in major)),tuple(sorted(m[x] for x in om)),i) for i,m in enumerate(maps))
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
def lift(x,d):return (x&((1<<d)-1))|((x>>d)<<(d+1))
accepted_review=json.loads((R/'Q5_T26_RANK_BATCH_REVIEW.json').read_text());assert accepted_review['verdict']=='PASS'
reports=[];witnesses=[];conditional=[];used=Counter();inputhash={}
for v in (1,7,31):
 n=f'Q5_T26_RANK_BATCH_REVIEW_remaining_v{v}.bin';raw=(R/n).read_bytes()
 assert raw==(R/f'Q5_T26_RANK_batch_remaining_v{v}.bin').read_bytes()
 inputhash[n]=hashlib.sha256(raw).hexdigest();keep=[];covered=0;forced_only=0
 for i in range(0,len(raw),9):
  z=set(raw[i:i+4]);w=set(raw[i+4:i+9]);assert v not in w
  choices=[];fchoices=[]
  for d in range(6):
   side=lambda x:((x^v)>>d)&1==0
   za={x for x in z if side(x)};wa={x for x in w if side(x)}
   if (len(za),len(wa))==(3,1):sources=[tuple(sorted(za))];minor=next(iter(z-za));inc=w-wa
   elif (len(za),len(wa))==(0,4):sources=list(combinations(sorted(wa-{1<<d}),3));minor=next(iter(w-wa));inc=z-za
   else:continue
   for s in sources:
    om=tuple(sorted(project((x^(1<<d))^minor,d) for x in s));major=tuple(sorted({project(x^minor,d) for x in inc}|set(om)));a,b,pi=canonical(major,om);key=(a,b)
    base={'v':v,'input_index':i//9,'Z':sorted(z),'W':sorted(w),'cut':d,'source_triple':s,'minority':minor,'normalized_majority':major,'normalized_omitted':om,'permutation':perms[pi]}
    if key in lookup:choices.append({**base,'orbit_id':lookup[key]})
    if key in forcedlookup:
     oid,pq=forcedlookup[key];inverse={y:x for x,y in enumerate(maps[pi])}
     actual=sorted(lift(inverse[q],d)^minor for q in pq)
     assert all(not side(x) for x in actual) and (actual[0]^actual[1]).bit_count()%2==0
     assert not set(actual)&(z|w)
     fchoices.append({**base,'orbit_id':oid,'canonical_forced_pair':pq,'actual_B_forced_pair':actual,'global_root_in_OB_pair':0 in actual})
  if choices:
   chosen=choices[0];witnesses.append(chosen);used[chosen['orbit_id']]+=1;covered+=1
  else:
   keep.append(raw[i:i+9])
   if fchoices:conditional.append({'v':v,'input_index':i//9,'choices':fchoices});forced_only+=1
 remaining=b''.join(keep);dest=f'Q5_T17_RANK_batch_remaining_v{v}.bin';(R/dest).write_bytes(remaining)
 reports.append({'v':v,'input':len(raw)//9,'unforced_orbit_union_covered':covered,'remaining':len(keep),'remaining_with_forced_T17_choice':forced_only,'remaining_file':dest,'remaining_sha256':hashlib.sha256(remaining).hexdigest()})
out={'status':'PRODUCER_UNION_PENDING_LOCAL_BATCH_REVIEW','accepted_input_review_sha256':hashlib.sha256((R/'Q5_T26_RANK_BATCH_REVIEW.json').read_bytes()).hexdigest(),'input_hashes':inputhash,'reports':reports,'selected_orbit_counts':dict(used),'total_covered':len(witnesses),'total_remaining':sum(a['remaining'] for a in reports),'forced_only_geometry_records':len(conditional),'full_P6_proved':False}
(R/'Q5_T17_RANK_batch_coverage.json').write_text(json.dumps(out,indent=2)+'\n')
(R/'Q5_T17_RANK_batch_projection_witnesses.json').write_text(json.dumps(witnesses,indent=2)+'\n')
(R/'Q5_T17_RANK_forced_projection_witnesses.json').write_text(json.dumps(conditional,indent=2)+'\n')
print(json.dumps(out,indent=2))
