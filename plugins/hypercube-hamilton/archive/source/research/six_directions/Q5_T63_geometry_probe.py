"""Hole-only geometry census for a strict positive-crossing split criterion."""
from pathlib import Path
from itertools import combinations,permutations
from collections import Counter
import json,hashlib
P=Path(__file__).resolve().parent
EVEN=[x for x in range(32) if x.bit_count()%2==0]
maps=[]
for perm in permutations(range(5)):
 m=[sum(((x>>perm[i])&1)<<i for i in range(5)) for x in range(32)]
 for shift in EVEN:maps.append([y^shift for y in m])
domain={(h,u) for h in combinations(EVEN,6) for u in combinations(h,3)}
assert len(domain)==160160
def classification(h,u):
 good=[]
 for i in range(5):
  a=sum(not(x&(1<<i)) for x in h);b=sum(not(x&(1<<i)) for x in u)
  if (a,b) in ((2,1),(4,2)):good.append(i)
 mask=sum(1<<i for i in good)
 cells=Counter(x&mask for x in h)
 return good,[{'cell':c,'holes':sorted(x for x in h if x&mask==c)} for c,n in sorted(cells.items()) if n%2]
unseen=set(domain);rows=[];totals=Counter();good_hist=Counter()
while unseen:
 h,u=min(unseen)
 orbit={(tuple(sorted(m[x] for x in h)),tuple(sorted(m[x] for x in u))) for m in maps}
 assert orbit<=unseen
 unseen-=orbit
 good,odd=classification(h,u)
 status='all_matchings_by_odd_common_cell' if odd else 'positive_crossing_cut_only' if good else 'no_2_4_split'
 totals[status]+=len(orbit);good_hist[len(good)]+=len(orbit)
 # Criterion invariance under every automorphism in this orbit.
 assert all(bool(classification(h1,u1)[1])==bool(odd) for h1,u1 in orbit)
 rows.append({'holes':list(h),'omitted':list(u),'orbit_size':len(orbit),
  'good_cut_indices':good,'odd_common_cells':odd,'status':status})
out={'scope':'Q5 six same-parity holes, three specified omitted holes; geometry-only sufficient split census, not full T63 proof',
 'status':'PRODUCER_GEOMETRY_ONLY_PENDING_INDEPENDENT_REVIEW','even_parity_marked_geometries':160160,
 'automorphism_group_size':1920,'orbits':len(rows),'counts':dict(totals),'good_cut_count_histogram':dict(good_hist),
 'rows':rows,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'full_T63_proved':False,'full_P6_proved':False}
(P/'Q5_T63_geometry_probe.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
