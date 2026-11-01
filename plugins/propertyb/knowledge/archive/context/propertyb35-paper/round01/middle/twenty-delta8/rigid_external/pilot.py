"""Conditional rigid8^5 9^15 graph: all low pairs inclusive2, no >=3 low edge.
Choose actual nine-degree y with mixed incidence r<=4, hence r3/4; weighted K5 p_ij0..2, min degree>=1.
Expand the same twenty low-pair edges and fifteen empty-low edges into six locks.
"""
from pathlib import Path
from itertools import product,combinations,permutations
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[5];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
start=time.time();pairs=list(combinations(range(5),2));masks=[sum(1<<i for i in S) for S in pairs];seen={};orbits=[];labelled=[]
for pp in product(range(3),repeat=10):
 r=sum(pp)
 if r not in (3,4):continue
 lam=[sum(p for S,p in zip(pairs,pp) if i in S) for i in range(5)]
 if min(lam)<1:continue
 ns={0:6+r,32:9-r}
 for m,p in zip(masks,pp):ns[m]=2-p;ns[m|32]=p
 key=tuple(ns.get(t,0) for t in range(64))
 if key in seen:idx,perm=seen[key]
 else:
  idx=len(orbits);orbits.append(dict(id=idx,degrees=[8,8,8,8,8,9],counts=ns,weighted_pairs=pp,y_low_codegrees=lam,mixed_incidence=r,labelled_count=0))
  for perm in permutations(range(5)):
   def move(t):return(t&32)|sum(1<<perm[i] for i in range(5) if t>>i&1)
   moved={move(t):v for t,v in ns.items()};seen[tuple(moved.get(t,0) for t in range(64))]=(idx,perm)
  idx,perm=seen[key]
 orbits[idx]['labelled_count']+=1;labelled.append(dict(counts=ns,orbit=idx,from_representative_low_permutation=perm))
(HERE/'DOMAIN.json').write_text(json.dumps(json_value(dict(scope=__doc__,labelled_count=len(labelled),orbit_count=len(orbits),orbits=orbits,labelled=labelled,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('domain',len(labelled),'orbits',len(orbits),'seconds',time.time()-start,flush=True)
out=[]
for rr in orbits:
 eng=SubsetEngine(20,6,rr['counts']);z=eng.verify(eng.solve());z.update(rr);z['strict']=z['bound']<1;out.append(z);print('dp',rr['id'],rr['mixed_incidence'],rr['y_low_codegrees'],z['bound'],flush=True)
(HERE/'DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('dp strict',sum(r['strict'] for r in out),'seconds',time.time()-start,flush=True)
joints=[];eng6=Engine(20,6)
for rr in out:
 if rr['strict']:continue
 z=solve_profile(eng6,dict(rr,graph='d8rigid',group=rr['id']),permutation_limit=720);z['source_id']=rr['id'];joints.append(z);print('joint',rr['id'],z.get('bound',z.get('status')),flush=True)
 if time.time()-start>60:break
(HERE/'JOINT.json').write_text(json.dumps(json_value(dict(scope=__doc__,results=joints,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('joint strict',sum(Q(z.get('bound','2'))<1 for z in joints),'of',len(joints),'seconds',time.time()-start,flush=True)
