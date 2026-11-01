"""Exactly two sevens: actual low pair c1..3 and two real8/9 outsiders with w(y)<=1,w(z)<=2.
Shared old two-low inventory, low/high projections, true old-slot four-way capacities, pair(y,z)1..4.
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
start=time.time();proj=json.loads((HERE/'PROJECTIONS.json').read_text())['cases'];lookup={(r['low_codegree'],r['degree'],*r['cross'],r['triple']):r['strict'] for r in proj}
views={};viewrows=[]
for c in (1,2,3):
 n=(21+c,7-c,7-c,c)
 for budget in (1,2):
  rows=[]
  for a1,a2,a3 in product(*(range(min(n[t],3)+1) for t in (1,2,3))):
   lam=[a1+a3,a2+a3]
   if min(lam)<1 or max(lam)>3 or sum(lam)-2>budget:continue
   for d in (8,9):
    if lookup[(c,d,*lam,a3)]:continue
    a0=d-a1-a2-a3
    if not 0<=a0<=n[0]:continue
    rows.append((d,(a0,a1,a2,a3)))
  views[(c,budget)]=rows
  viewrows.append(dict(low_codegree=c,budget=budget,rows=rows))
seen={};orbits=[];labelled=[]
for c in (1,2,3):
 n=(21+c,7-c,7-c,c)
 for da,a in views[(c,1)]:
  for db,b in views[(c,2)]:
   ranges=[range(max(0,a[t]+b[t]-n[t]),min(a[t],b[t])+1) for t in range(4)]
   for q in product(*ranges):
    if not 1<=sum(q)<=4:continue
    ns={}
    for t in range(4):
     for mask,v in ((t,n[t]-a[t]-b[t]+q[t]),(t|4,a[t]-q[t]),(t|8,b[t]-q[t]),(t|12,q[t])):
      if v:ns[mask]=v
    key=(da,db,tuple(ns.get(t,0) for t in range(16)))
    if key in seen:idx,perm,swap=seen[key]
    else:
     idx=len(orbits);orbits.append(dict(id=idx,degrees=[7,7,da,db],counts=ns,low_codegree=c,base_counts=n,promoted_y=a,promoted_z=b,both=q,labelled_count=0))
     for perm in permutations(range(2)):
      for swap in range(2 if da==db else 1):
       def move(t):return sum(1<<perm[i] for i in range(2) if t>>i&1)|((((t&4)<<1)|((t&8)>>1)) if swap else (t&12))
       moved={move(t):v for t,v in ns.items()};seen[(da,db,tuple(moved.get(t,0) for t in range(16)))]=(idx,perm,swap)
     idx,perm,swap=seen[key]
    orbits[idx]['labelled_count']+=1;labelled.append(dict(counts=ns,degrees=[7,7,da,db],orbit=idx,from_representative_low_permutation=perm,from_representative_outside_swap=swap))
(HERE/'R2_TWO_DOMAIN.json').write_text(json.dumps(json_value(dict(scope=__doc__,views=viewrows,labelled_count=len(labelled),orbit_count=len(orbits),orbits=orbits,labelled=labelled,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('domain',len(labelled),'orbits',len(orbits),'seconds',time.time()-start,flush=True)
out=[]
for r in orbits:
 eng=SubsetEngine(20,4,r['counts']);z=eng.verify(eng.solve());z.update(r);z['strict']=z['bound']<1;out.append(z)
 if time.time()-start>60:break
(HERE/'R2_TWO_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(orbits),cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('dp',len(out),'strict',sum(r['strict'] for r in out),'seconds',time.time()-start,flush=True)
joints=[];eng4=Engine(20,4)
for r in out:
 if r['strict']:continue
 z=solve_profile(eng4,dict(r,graph='r2two',group=r['id']),permutation_limit=24);z['source_id']=r['id'];joints.append(z)
 print('joint',r['id'],r['degrees'],r['bound'],'->',z.get('bound',z.get('status')),flush=True)
 if time.time()-start>110:break
(HERE/'R2_TWO_JOINT.json').write_text(json.dumps(json_value(dict(scope=__doc__,results=joints,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('joint strict',sum(Q(z.get('bound','2'))<1 for z in joints),'of',len(joints),'seconds',time.time()-start,flush=True)
