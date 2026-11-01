"""M35 v20 r7=3 then2: true low inventory + actual bounded-excess8/9 outsider.
Small exact pair-low-outsider projections and all three-low base inventories.
"""
from pathlib import Path
from itertools import combinations,permutations,product
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[5];sys.dont_write_bytecode=True
sys.path[:0]=[str(HERE.parents[1]),str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from pilot import triple
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
start=time.time();projections=[];eng3=Engine(20,3)
for c in (1,2,3):
 for d in (8,9):
  for a,b in product(range(1,4),repeat=2):
   for t in range(min(c,a,b)+1):
    ns=triple(20,[7,7,d],(c,a,b),t)
    if min(ns.values())<0:continue
    eng=SubsetEngine(20,3,ns);z=eng.verify(eng.solve());z.update(low_codegree=c,degree=d,cross=(a,b),triple=t,source_id=len(projections),strict=z['bound']<1)
    if not z['strict']:
     j=solve_profile(eng3,dict(z,graph='low23proj',group=z['source_id']),permutation_limit=6);z['joint']=j;z['strict']=Q(j.get('bound','2'))<1
    projections.append(z)
(HERE/'PROJECTIONS.json').write_text(json.dumps(json_value(dict(scope=__doc__,cases=projections,elapsed_seconds=time.time()-start)),indent=2)+'\n')
print('projections',len(projections),'strict',sum(z['strict'] for z in projections),'seconds',time.time()-start,flush=True)
base=[];seen=set()
for cs in product((1,2),repeat=3):
 for t in range(min(cs)+1):
  ns=triple(20,[7]*3,cs,t);key=tuple(ns.get(i,0) for i in range(8))
  if key in seen:continue
  for p in permutations(range(3)):
   moved={sum(1<<p[i] for i in range(3) if m>>i&1):n for m,n in ns.items()};seen.add(tuple(moved.get(i,0) for i in range(8)))
  eng=SubsetEngine(20,3,ns);z=eng.verify(eng.solve());z.update(codegrees=cs,triple=t,id=len(base),strict=z['bound']<1)
  if not z['strict']:
   j=solve_profile(eng3,dict(z,graph='low3base',group=z['id']),permutation_limit=6);z['joint']=j;z['strict']=Q(j.get('bound','2'))<1
  base.append(z)
(HERE/'THREE_LOW_BASE.json').write_text(json.dumps(json_value(dict(scope=__doc__,cases=base,elapsed_seconds=time.time()-start)),indent=2)+'\n')
print('three-low bases',len(base),'strict',sum(z['strict'] for z in base),'seconds',time.time()-start)
