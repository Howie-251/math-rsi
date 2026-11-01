from itertools import permutations, combinations_with_replacement
from pathlib import Path
import json
D=Path(__file__).parent
quad=[m for m in range(128) if m.bit_count()==4]
jobs=[]
for case,missing in enumerate(((3,5),(3,12))):
 def move(m,p):return sum(1<<p[v] for v in range(7) if m>>v&1)
 group=[p for p in permutations(range(7)) if {move(m,p) for m in missing}==set(missing)]
 assert len(group)==48
 full=set(combinations_with_replacement(quad,2)); seen=set(); local=[]
 for key in sorted(full):
  if key in seen:continue
  orbit={tuple(sorted(move(m,p) for m in key)) for p in group}
  assert orbit<=full
  rep=min(orbit);assert rep==key
  seen|=orbit
  jobs.append(dict(id=len(jobs),case=case,quads=list(rep),orbit_size=len(orbit),group_order=len(group)))
 assert seen==full and sum(x['orbit_size'] for x in jobs if x['case']==case)==630
(D/'JOBS.json').write_text(json.dumps(jobs,indent=2)+'\n')
(D/'JOBS.tsv').write_text(''.join(f"{j['id']} {j['case']} {j['quads'][0]} {j['quads'][1]} {j['orbit_size']}\n" for j in jobs))
print({'jobs':len(jobs),'cases':[sum(j['case']==c for j in jobs) for c in (0,1)]})
