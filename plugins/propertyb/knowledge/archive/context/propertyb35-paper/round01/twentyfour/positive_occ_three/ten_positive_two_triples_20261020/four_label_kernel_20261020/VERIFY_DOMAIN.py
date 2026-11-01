"""Cartesian-product second domain check, separate from recursive PROFILE.py."""
from pathlib import Path
from itertools import combinations,permutations,product
import json,time

HERE=Path(__file__).resolve().parent;EDGES=tuple(combinations(range(4),2))
start=time.process_time();d=json.loads((HERE/'PROFILE.json').read_text());checks=[]
# Derive ALL capacity cells directly from the mathematical parameters, rather
# than allowing an omitted job to disappear from both sides of the replay.
expected_cells={(n,tuple(sorted(cap))) for n in range(3)
                for cap in product(range(4-n,5),repeat=4)
                if sum(cap)>=(16,13,10)[n]}
actual_cells={(job['n'],tuple(job['capacities'])) for job in d['jobs']}
assert len(expected_cells)==len(actual_cells)==len(d['jobs'])==18
assert actual_cells==expected_cells
assert {(r['n'],tuple(r['capacities'])) for r in d['representatives']}==expected_cells
for job in d['jobs']:
 n=job['n'];cap=tuple(job['capacities'])
 reps=[r for r in d['representatives'] if r['n']==n and tuple(r['capacities'])==cap]
 permutations_cap=[p for p in permutations(range(4)) if all(cap[p[i]]==cap[i] for i in range(4))]
 transported=set()
 for r in reps:
  orbit=set()
  for p in permutations_cap:
   out=[0]*6
   for (a,b),m in zip(EDGES,r['graph']):out[EDGES.index(tuple(sorted((p[a],p[b]))))]=m
   orbit.add(tuple(out))
  assert len(orbit)==r['orbit_size'] and not transported&orbit
  transported.update(orbit)
 direct=set()
 for vec in product(*(range(min(cap[a],cap[b])+1) for a,b in EDGES)):
  degree=[0]*4
  for (a,b),m in zip(EDGES,vec):degree[a]+=m;degree[b]+=m
  if all(degree[i]<=cap[i] for i in range(4)) and sum(cap)-sum(vec)<=16-n:direct.add(vec)
 assert direct==transported and len(direct)==job['labelled']
 checks.append(dict(n=n,capacities=cap,labelled=len(direct),orbits=len(reps),same_full_labelled_set=True))
out=dict(pass_all=True,all_mathematically_defined_capacity_cells_checked=True,
         capacity_cells=len(expected_cells),jobs=checks,labelled=sum(r['labelled'] for r in checks),
         orbits=sum(r['orbits'] for r in checks),process_seconds=time.process_time()-start)
assert (out['labelled'],out['orbits'])==(5573,1333)
(HERE/'DOMAIN_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS',out['labelled'],out['orbits'],'CPU',out['process_seconds'])
