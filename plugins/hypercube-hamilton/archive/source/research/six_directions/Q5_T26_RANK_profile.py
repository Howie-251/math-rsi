"""Producer profile of actual T26 projections in accepted ten-hole residuals."""
from pathlib import Path
from itertools import permutations,combinations
from functools import lru_cache
from collections import Counter,defaultdict
import json
P=Path(__file__).resolve().parent
PERM=[tuple(sum(((x>>p[i])&1)<<i for i in range(5)) for x in range(32)) for p in permutations(range(5))]
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
@lru_cache(None)
def canonical(minor,major,omit):
 target=3 if (minor[0]^minor[1]).bit_count()==2 else 15
 out=[]
 for shift in minor:
  delta=minor[0]^minor[1]
  for m in PERM:
   if m[delta]!=target:continue
   out.append((tuple(sorted(m[x^shift] for x in minor)),tuple(sorted(m[x^shift] for x in major)),tuple(sorted(m[x^shift] for x in omit))))
 return min(out)
coverage=defaultdict(set);counts=Counter();targetcounts=defaultdict(Counter)
FIRST=((0,3),(1,4,14,22,28,31),(1,4));first_witness={}
for v in (1,7,31):
 raw=(P/f'ten_covered_after_full_A8_v{v}.bin').read_bytes()
 for k in range(0,len(raw),9):
  Z=set(raw[k:k+4]);W=set(raw[k+4:k+9]);seen=set()
  for d in range(6):
   A={x for x in range(64) if (x>>d&1)==(v>>d&1)};za=Z&A;wa=W&A
   if (len(za),len(wa))==(2,1):sources=[tuple(za)];base_minor=Z-A;base_major=W-A
   elif (len(za),len(wa))==(0,3):sources=list(combinations(wa-{1<<d},2));base_minor=W-A;base_major=Z-A
   else:continue
   for source in sources:
    U={project(x^(1<<d),d) for x in source};M={project(x,d) for x in base_minor};J={project(x,d) for x in base_major}|U
    assert len(M)==2 and len(J)==6 and len(U)==2
    key=canonical(tuple(sorted(M)),tuple(sorted(J)),tuple(sorted(U)))
    if key==FIRST and (v,k//9) not in first_witness:
     first_witness[v,k//9]={'v':v,'input_index':k//9,'cut':d,'row':[len(za),len(wa)],'bridge_sources':list(source),'local_minority':sorted(M),'local_majority':sorted(J),'local_omitted':sorted(U)}
    seen.add(key);counts[key]+=1
  for key in seen:coverage[key].add((v,k//9));targetcounts[key][v]+=1
rows=[]
for key,domain in sorted(coverage.items(),key=lambda item:(-len(item[1]),item[0])):
 rows.append({'minority':key[0],'majority':key[1],'omitted':key[2],'covered_Q6_records':len(domain),'targets':dict(targetcounts[key]),'projections':counts[key]})
(P/'Q5_T26_RANK_profile.json').write_text(json.dumps({'status':'PRODUCER_ONLY','marked_orbits':len(rows),'rows':rows},indent=2)+'\n')
print(json.dumps(rows[:5],indent=2))
reports=[]
for v in (1,7,31):
 raw=(P/f'ten_covered_after_full_A8_v{v}.bin').read_bytes();rec=[raw[i:i+9] for i in range(0,len(raw),9)]
 indices={i for vv,i in first_witness if vv==v};remaining=b''.join(r for i,r in enumerate(rec) if i not in indices)
 (P/f'Q5_T26_RANK_first_remaining_v{v}.bin').write_bytes(remaining)
 conditional=(P/f'ten_covered_t63_complete_split_remaining_v{v}.bin').read_bytes();conditional_set={conditional[i:i+9] for i in range(0,len(conditional),9)}
 net=sum(rec[i] in conditional_set for i in indices)
 reports.append({'v':v,'input':len(rec),'first_orbit_covered':len(indices),'remaining':len(remaining)//9,'net_in_conditional_T63_remainder':net})
out={'status':'PRODUCER_ONLY_PENDING_RANK_AND_APPLICATION_REVIEW','orbit':{'minority':FIRST[0],'majority':FIRST[1],'omitted':FIRST[2]},'reports':reports,'witnesses':list(first_witness.values()),'full_ten_hole_proved':False,'full_P6_proved':False}
(P/'Q5_T26_RANK_first_coverage.json').write_text(json.dumps(out,indent=2)+'\n')
print('FIRST COVERAGE',json.dumps(reports))
