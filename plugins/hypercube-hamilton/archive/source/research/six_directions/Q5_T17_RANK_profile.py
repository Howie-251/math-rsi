"""Producer-only complete actual T17 projection profile; no transfer claim."""
from pathlib import Path
from itertools import permutations,combinations
from functools import lru_cache
from collections import defaultdict,Counter
import hashlib,json,sys
R=Path(__file__).resolve().parent
CANDIDATE='--candidate' in sys.argv
PRE='Q5_T17_RANK_candidate' if CANDIDATE else 'Q5_T17_RANK'
MAPS=[tuple(sum(((x>>j)&1)<<p[j] for j in range(5)) for x in range(32)) for p in permutations(range(5))]
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
@lru_cache(None)
def canon(major,omitted):
 return min((tuple(sorted(m[x] for x in major)),tuple(sorted(m[x] for x in omitted))) for m in MAPS)
coverage=defaultdict(set);witnesses=defaultdict(dict);counts=Counter();inputs={}
for v in (1,7,31):
 n=f'Q5_T26_RANK_batch_remaining_v{v}.bin' if CANDIDATE else f'ten_covered_q5_and_t63_remaining_v{v}.bin';raw=(R/n).read_bytes();assert len(raw)%9==0
 inputs[n]={'records':len(raw)//9,'sha256':hashlib.sha256(raw).hexdigest()}
 for i in range(0,len(raw),9):
  z=set(raw[i:i+4]);w=set(raw[i+4:i+9]);seen=set()
  for d in range(6):
   side=lambda x:((x^v)>>d)&1==0
   za={x for x in z if side(x)};wa={x for x in w if side(x)}
   if (len(za),len(wa))==(3,1):sources=[tuple(sorted(za))];minor=next(iter(z-za));included=w-wa
   elif (len(za),len(wa))==(0,4):sources=combinations(sorted(wa-{1<<d}),3);minor=next(iter(w-wa));included=z-za
   else:continue
   for s in sources:
    omitted=tuple(sorted(project((x^(1<<d))^minor,d) for x in s))
    major=tuple(sorted({project(x^minor,d) for x in included}|set(omitted)))
    assert len(major)==7 and len(set(omitted))==3 and all(x.bit_count()%2 for x in major)
    assert all(x.bit_count()!=1 for x in major if x not in omitted)
    key=canon(major,omitted);counts[key]+=1;coverage[key].add((v,i//9))
    witnesses[key].setdefault((v,i//9),{'v':v,'input_index':i//9,'outer_cut':d,'row':[len(za),len(wa)],'sources':list(s),'minority':minor,'local_minority':0,'majority':major,'omitted':omitted})
rows=[]
for j,(key,domain) in enumerate(sorted(coverage.items(),key=lambda x:(-len(x[1]),x[0])),1):
 major,omit=key;remaining_neighbors={1,2,4,8,16}-set(omit)
 forced=sorted(remaining_neighbors) if len(remaining_neighbors)==2 else None
 rows.append({'id':j,'minority':[0],'majority':major,'omitted':omit,'coverage':len(domain),
              'targets':dict(Counter(v for v,i in domain)),'projections':counts[key],
              'omitted_neighbors_of_minority':sum(x.bit_count()==1 for x in omit),
              'forced_cherry_pair':forced,'full_rank_obstructed_by_triangle':forced is not None})
out={'status':'PRODUCER_PROFILE','input_records':sum(a['records'] for a in inputs.values()),'inputs':inputs,
     'marked_orbits':len(rows),'orbits_without_forced_cherry':sum(not a['full_rank_obstructed_by_triangle'] for a in rows),
     'records_admitting_T17_projection':len(set().union(*coverage.values())) if coverage else 0,'rows':rows}
(R/(PRE+'_profile.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
if rows:
 preferred=next((a for a in rows if not a['full_rank_obstructed_by_triangle']),rows[0]);key=(tuple(preferred['majority']),tuple(preferred['omitted']))
 (R/(PRE+'_first_config.txt')).write_text(' '.join(map(str,[0,*key[0],*key[1]]))+'\n')
 (R/(PRE+'_first_coverage.json')).write_text(json.dumps({'status':'PRODUCER_ONLY_LOCAL_RANK_AND_Q6_APPLICATION_UNPROVED','orbit':preferred,'witnesses':list(witnesses[key].values()),'inputs':inputs,'full_P6_proved':False},indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2));print(json.dumps(rows[:12],indent=2))
