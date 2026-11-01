"""Actual five degree8 vertices, guaranteed by total175/min8. Join two surviving four8 views
on the same exact three-point old inventory; true old-slot capacities, pair34=1..3,
full-five trace<=1, and all three new four-views simultaneously in the same residual relation.
Exclude only the separately proved all-pair2/no-triple core.
"""
from pathlib import Path
from itertools import product,combinations,permutations
import json,time,sys
HERE=Path(__file__).parent;sys.dont_write_bytecode=True;start=time.time();src=HERE.parent/'four_projection';four=json.loads((src/'DOMAIN.json').read_text());res={r['id'] for r in json.loads((src/'FOUR_REMAINDERS.json').read_text())['cases']}
def key(ns,s):return tuple(ns.get(t,ns.get(str(t),0)) for t in range(1<<s))
views=[r for r in four['labelled'] if r['orbit'] in res];allowed4={key(r['counts'],4) for r in views};groups={}
for r in views:
 nn=key(r['counts'],4);base=tuple(nn[t]+nn[t|8] for t in range(8));prom=tuple(nn[t|8] for t in range(8));groups.setdefault(base,[]).append((prom,r['orbit']))
core=tuple(15 if t==0 else 2 if t.bit_count()==2 else 0 for t in range(32));seen={};orbits=[];labelled=[];counts=dict(view_pairs=0,intersection_candidates=0,pair_capacity_pass=0,all_four_pass=0,proved_core_excluded=0);newprojs=[(0,1,3,4),(0,2,3,4),(1,2,3,4)]
for old,vv in groups.items():
 for (a,ida),(b,idb) in product(vv,repeat=2):
  counts['view_pairs']+=1;ranges=[range(max(0,a[t]+b[t]-old[t]),min(a[t],b[t],1 if t==7 else 35)+1) for t in range(8)]
  for qq in product(*ranges[1:]):
   counts['intersection_candidates']+=1
   if sum(qq)>3:continue
   for q0 in ranges[0]:
    q=(q0,*qq)
    if not 1<=sum(q)<=3:continue
    counts['pair_capacity_pass']+=1;ns={}
    for t in range(8):ns[t]=old[t]-a[t]-b[t]+q[t];ns[t|8]=a[t]-q[t];ns[t|16]=b[t]-q[t];ns[t|24]=q[t]
    passed=True
    for order in newprojs:
     proj=[0]*16
     for t,n in ns.items():proj[sum(1<<i for i,j in enumerate(order) if t>>j&1)]+=n
     if tuple(proj) not in allowed4:passed=False;break
    if not passed:continue
    counts['all_four_pass']+=1;kk=key(ns,5)
    if kk==core:counts['proved_core_excluded']+=1;continue
    if kk in seen:idx,perm=seen[kk]
    else:
     idx=len(orbits);orbits.append(dict(id=idx,degrees=[8]*5,counts=ns,old_three_counts=old,promoted3=a,promoted4=b,intersection=q,seed_four_ids=[ida,idb],labelled_count=0))
     for perm in permutations(range(5)):
      moved={sum(1<<perm[i] for i in range(5) if t>>i&1):n for t,n in ns.items()};seen[key(moved,5)]=(idx,perm)
     idx,perm=seen[kk]
    orbits[idx]['labelled_count']+=1;labelled.append(dict(counts=ns,orbit=idx,from_representative_permutation=perm))
result=dict(scope=__doc__,four_residual_orbits=len(res),four_residual_labelled=len(views),common_three_groups=len(groups),counters=counts,labelled_count=len(labelled),orbit_count=len(orbits),orbits=orbits,labelled=labelled,elapsed_seconds=time.time()-start)
(HERE/'DOMAIN.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items() if k not in ('orbits','labelled')})
