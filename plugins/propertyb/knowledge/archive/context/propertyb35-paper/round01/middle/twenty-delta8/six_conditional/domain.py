"""Conditional r8>=6 only. Six distinct actual8 vertices, all six five-views in the same49 residual relation.
Join two five-views over the same exact four-point inventory. True old-slot capacities, new pair1..3,
full-six trace0 (5-uniform), every new full-five exact trace<=1 (simple), and four new five-view checks.
No existence of a sixth8 is asserted for r8=5.
"""
from pathlib import Path
from itertools import product,permutations
import json,time,sys
HERE=Path(__file__).parent;sys.dont_write_bytecode=True;start=time.time();src=HERE.parent/'five_join';dom=json.loads((src/'DOMAIN.json').read_text());res={r['id'] for r in json.loads((src/'FIVE_REMAINDERS.json').read_text())['cases']}
def key(ns,s):return tuple(ns.get(t,ns.get(str(t),0)) for t in range(1<<s))
views=[r for r in dom['labelled'] if r['orbit'] in res];allowed5={key(r['counts'],5) for r in views};groups={}
for r in views:
 nn=key(r['counts'],5);base=tuple(nn[t]+nn[t|16] for t in range(16));prom=tuple(nn[t|16] for t in range(16));groups.setdefault(base,[]).append((prom,r['orbit']))
seen={};orbits=[];labelled=[];counts=dict(view_pairs=0,intersection_candidates=0,pair_capacity_pass=0,all_five_pass=0);neworders=[[i for i in range(4) if i!=j]+[4,5] for j in range(4)];complete=True
for old,vv in groups.items():
 for (a,ida),(b,idb) in product(vv,repeat=2):
  counts['view_pairs']+=1;ranges=[]
  for t in range(16):
   cap=0 if t==15 else 1 if t.bit_count()==3 else 35;ranges.append(range(max(0,a[t]+b[t]-old[t]),min(a[t],b[t],cap)+1))
  if any(not r for r in ranges):continue
  for qq in product(*ranges[1:]):
   counts['intersection_candidates']+=1
   if sum(qq)>3:continue
   for q0 in ranges[0]:
    q=(q0,*qq)
    if not 1<=sum(q)<=3:continue
    counts['pair_capacity_pass']+=1;ns={}
    for t in range(16):ns[t]=old[t]-a[t]-b[t]+q[t];ns[t|16]=a[t]-q[t];ns[t|32]=b[t]-q[t];ns[t|48]=q[t]
    passed=True
    for order in neworders:
     proj=[0]*32
     for t,n in ns.items():proj[sum(1<<i for i,j in enumerate(order) if t>>j&1)]+=n
     if tuple(proj) not in allowed5:passed=False;break
    if not passed:continue
    counts['all_five_pass']+=1;kk=key(ns,6)
    if kk in seen:idx,perm=seen[kk]
    else:
     idx=len(orbits);orbits.append(dict(id=idx,degrees=[8]*6,counts=ns,old_four_counts=old,promoted4=a,promoted5=b,intersection=q,seed_five_ids=[ida,idb],labelled_count=0))
     for perm in permutations(range(6)):
      moved={sum(1<<perm[i] for i in range(6) if t>>i&1):n for t,n in ns.items()};seen[key(moved,6)]=(idx,perm)
     idx,perm=seen[kk]
    orbits[idx]['labelled_count']+=1;labelled.append(dict(counts=ns,orbit=idx,from_representative_permutation=perm))
  if time.time()-start>25:complete=False;break
 if not complete:break
result=dict(scope=__doc__,complete=complete,five_residual_orbits=len(res),five_residual_labelled=len(views),common_four_groups=len(groups),counters=counts,labelled_count=len(labelled),orbit_count=len(orbits),orbits=orbits,labelled=labelled,elapsed_seconds=time.time()-start)
(HERE/'DOMAIN.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items() if k not in ('orbits','labelled')})
