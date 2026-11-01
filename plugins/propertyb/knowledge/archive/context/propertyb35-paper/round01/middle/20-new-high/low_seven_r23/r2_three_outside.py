"""Two sevens and three actual8/9 outsiders y,z,w: low-excess(y)<=1, low-excess(z),low-excess(w)<=2.
Join two surviving four-lock views over the same exact {low1,low2,y} inventory.
True old-slot capacities, codegree(z,w)1..4, simple full-five trace<=1.
"""
from pathlib import Path
from itertools import product,permutations
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[5];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
start=time.time();dom=json.loads((HERE/'R2_TWO_DOMAIN.json').read_text());dp=json.loads((HERE/'R2_TWO_DP.json').read_text())['cases'];joints={r['source_id']:r for r in json.loads((HERE/'R2_TWO_JOINT.json').read_text())['results']}
res={r['id'] for r in dp if not r['strict'] and Q(joints[r['id']].get('bound','2'))>=1};groups={}
for row in dom['labelled']:
 if row['orbit'] not in res:continue
 ns={int(t):n for t,n in row['counts'].items()};base=tuple(ns.get(t,0)+ns.get(t|8,0) for t in range(8));dy=row['degrees'][2];dz=row['degrees'][3];a=tuple(ns.get(t|8,0) for t in range(8));groups.setdefault((dy,base),[]).append((dz,a,row['orbit']))
seen={};orbits=[];labelled=[]
for (dy,base),views in groups.items():
 for da,a,ida in views:
  for db,b,idb in views:
   if da>db:continue
   ranges=[range(max(0,a[t]+b[t]-base[t]),min(a[t],b[t],1 if t==7 else 35)+1) for t in range(8)]
   for qq in product(*ranges[1:]):
    if sum(qq)>4:continue
    for q0 in ranges[0]:
     q=(q0,*qq);co=sum(q)
     if not 1<=co<=4:continue
     ns={}
     for t in range(8):
      for mask,n in ((t,base[t]-a[t]-b[t]+q[t]),(t|8,a[t]-q[t]),(t|16,b[t]-q[t]),(t|24,q[t])):
       if n:ns[mask]=n
     key=(dy,da,db,tuple(ns.get(t,0) for t in range(32)))
     if key in seen:idx,perm,swap=seen[key]
     else:
      idx=len(orbits);orbits.append(dict(id=idx,degrees=[7,7,dy,da,db],counts=ns,base_counts=base,promoted_z=a,promoted_w=b,both=q,new_outside_codegree=co,view_ids=[ida,idb],labelled_count=0))
      for perm in permutations(range(2)):
       for swap in range(2 if da==db else 1):
        def move(t):return sum(1<<perm[i] for i in range(2) if t>>i&1)|(t&4)|((((t&8)<<1)|((t&16)>>1)) if swap else(t&24))
        moved={move(t):n for t,n in ns.items()};seen[(dy,da,db,tuple(moved.get(t,0) for t in range(32)))]=(idx,perm,swap)
      idx,perm,swap=seen[key]
     orbits[idx]['labelled_count']+=1;labelled.append(dict(counts=ns,degrees=[7,7,dy,da,db],orbit=idx,from_representative_low_permutation=perm,from_representative_last_outside_swap=swap,view_ids=[ida,idb]))
result=dict(scope=__doc__,four_lock_residues=sorted(res),labelled_count=len(labelled),orbit_count=len(orbits),orbits=orbits,labelled=labelled,elapsed_seconds=time.time()-start)
(HERE/'R2_THREE_DOMAIN.json').write_text(json.dumps(json_value(result),indent=2)+'\n');print('domain',len(labelled),'orbits',len(orbits),'seconds',time.time()-start,flush=True)
if len(orbits)>3000:
 print('domain exceeds small pilot budget; no DP',flush=True);sys.exit(0)
out=[]
for r in orbits:
 eng=SubsetEngine(20,5,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;out.append(z)
 if len(out) in (10,100,500,1000):print('dp progress',len(out),'strict',sum(r['strict'] for r in out),'seconds',time.time()-start,flush=True)
 if time.time()-start>65:break
(HERE/'R2_THREE_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(orbits),cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('dp',len(out),'strict',sum(r['strict'] for r in out),'seconds',time.time()-start,flush=True)
joints=[];eng5=Engine(20,5)
for r in out:
 if r['strict']:continue
 z=solve_profile(eng5,dict(r,graph='r2three',group=r['id']),permutation_limit=120);z['source_id']=r['id'];joints.append(z)
 print('joint',r['id'],r['degrees'],r['bound'],'->',z.get('bound',z.get('status')),flush=True)
 if time.time()-start>80:break
(HERE/'R2_THREE_JOINT.json').write_text(json.dumps(json_value(dict(scope=__doc__,results=joints,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('joint strict',sum(Q(z.get('bound','2'))<1 for z in joints),'of',len(joints),'seconds',time.time()-start,flush=True)
