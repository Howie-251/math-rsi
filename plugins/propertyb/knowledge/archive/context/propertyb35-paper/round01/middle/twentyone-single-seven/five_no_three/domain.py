"""Five actual unit8 neighbors of degree7 center on21 points/M35, no neighbor codegree3.
Shared four-view recovery, true neighbor-S5 action fixing center. Bounded10s domain pilot.
When pool s>=7, deleting an endpoint of its at-most-one codegree3 pair supplies at least6 such points.
"""
from pathlib import Path
from itertools import product,permutations
import json,time,sys
HERE=Path(__file__).parent;sys.dont_write_bytecode=True;start=time.time();src=HERE.parent;dom=json.loads((src/'FOUR_DOMAIN.json').read_text());res={r['id'] for r in json.loads((src/'FOUR_REMAINDERS.json').read_text())['cases'] if max(r['neighbor_codegrees'])<=2}
def key(ns,s):return tuple(ns.get(t,ns.get(str(t),0)) for t in range(1<<s))
views=[r for r in dom['labelled'] if r['orbit'] in res];allowed={key(r['counts'],5) for r in views};groups={}
for r in views:
 nn=key(r['counts'],5);base=tuple(nn[t]+nn[t|16] for t in range(16));prom=tuple(nn[t|16] for t in range(16));groups.setdefault(base,[]).append((prom,r['orbit']))
seen={};orbits=[];labelled=[];counts=dict(view_pairs=0,intersection_candidates=0,pair_capacity_pass=0,all_four_neighbor_views_pass=0);orders=[[0]+[i for i in range(1,4) if i!=j]+[4,5] for j in range(1,4)];complete=True
projection_maps=[[sum(1<<i for i,j in enumerate(order) if t>>j&1) for t in range(64)] for order in orders]
permutation_maps=[(p,[(t&1)|sum(1<<(p[i]+1) for i in range(5) if t>>(i+1)&1) for t in range(64)]) for p in permutations(range(5))]
for old,vv in groups.items():
 for (a,ida),(b,idb) in product(vv,repeat=2):
  counts['view_pairs']+=1;ranges=[]
  for t in range(16):
   cap=0 if t==15 else 1 if t.bit_count()==3 else 35;ranges.append(range(max(0,a[t]+b[t]-old[t]),min(a[t],b[t],cap)+1))
  if any(not r for r in ranges):continue
  for qq in product(*ranges[1:]):
   counts['intersection_candidates']+=1
   if sum(qq)>2:continue
   for q0 in ranges[0]:
    q=(q0,*qq)
    if not 1<=sum(q)<=2:continue
    counts['pair_capacity_pass']+=1;ns={}
    for t in range(16):ns[t]=old[t]-a[t]-b[t]+q[t];ns[t|16]=a[t]-q[t];ns[t|32]=b[t]-q[t];ns[t|48]=q[t]
    passed=True
    for projection in projection_maps:
     vv0=[0]*32
     for t,n in ns.items():vv0[projection[t]]+=n
     if tuple(vv0) not in allowed:passed=False;break
    if not passed:continue
    counts['all_four_neighbor_views_pass']+=1;kk=key(ns,6)
    if kk not in seen:
     idx=len(orbits);orbits.append(dict(id=idx,degrees=[7]+[8]*5,counts=ns,old_counts=old,promoted4=a,promoted5=b,intersection=q,seed_four_neighbor_ids=[ida,idb],labelled_count=0))
     for p,mp in permutation_maps:
      moved=[0]*64
      for t,n in ns.items():moved[mp[t]]=n
      seen[tuple(moved)]=(idx,p)
    idx,p=seen[kk];orbits[idx]['labelled_count']+=1;labelled.append(dict(counts=ns,orbit=idx,from_representative_neighbor_permutation=p))
  if time.time()-start>10:complete=False;break
 if not complete:break
result=dict(scope=__doc__,complete=complete,source_four_orbits=len(res),source_labelled=len(views),common_groups=len(groups),counters=counts,labelled_count=len(labelled),orbit_count=len(orbits),orbits=orbits,labelled=labelled,elapsed_seconds=time.time()-start);(HERE/'DOMAIN.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items() if k not in ('orbits','labelled')})
