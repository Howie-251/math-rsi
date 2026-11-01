from itertools import permutations,product
from pathlib import Path
import json
D=Path(__file__).parent
quad=[m for m in range(128) if m.bit_count()==4]
tri=[m for m in range(128) if m.bit_count()==3]
jobs=[]
for case,missing in enumerate(((3,5),(3,12))):
 def move(m,p):return sum(1<<p[v] for v in range(7) if m>>v&1)
 group=[p for p in permutations(range(7)) if {move(m,p) for m in missing}==set(missing)]
 assert len(group)==48
 full=set(product(quad,tri));seen=set()
 for key in sorted(full):
  if key in seen:continue
  orbit={(move(key[0],p),move(key[1],p)) for p in group}
  assert min(orbit)==key and orbit<=full
  jobs.append(dict(id=len(jobs),case=case,quad=key[0],triple=key[1],orbit_size=len(orbit)))
  seen|=orbit
 assert seen==full and sum(j['orbit_size'] for j in jobs if j['case']==case)==1225
(D/'JOBS.json').write_text(json.dumps(jobs,indent=2)+'\n')
(D/'JOBS.tsv').write_text(''.join(f"{j['id']} {j['case']} {j['quad']} {j['triple']} {j['orbit_size']}\n" for j in jobs))
print({'jobs':len(jobs),'cases':[sum(j['case']==c for j in jobs) for c in (0,1)]})
