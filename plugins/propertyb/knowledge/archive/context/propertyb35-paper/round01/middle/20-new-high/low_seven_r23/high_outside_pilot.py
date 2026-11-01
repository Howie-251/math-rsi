"""Bounded actual structural pilot:7/b pairs and7/7/b triples, b10..15, low/high codegrees1/2.
Records exact fixed and repaired joint certificates; failure is only a boundary of this inequality.
"""
from pathlib import Path
from itertools import product
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[5];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
start=time.time();pairs=[];triples=[]
for b,c in product(range(10,16),(1,2)):
 ns={0:28-b+c,1:7-c,2:b-c,3:c};eng=SubsetEngine(20,2,ns);z=eng.verify(eng.solve());z.update(degrees=[7,b],codegree=c);z['strict']=z['bound']<1;pairs.append(z)
 print('pair',b,c,z['bound'],flush=True)
eng3=Engine(20,3)
for b,c,a,d in product(range(10,16),(1,2,3),(1,2),(1,2)):
 for t in range(min(c,a,d)+1):
  ns={0:21-b+c+a+d-t,1:7-c-a+t,2:7-c-d+t,4:b-a-d+t,3:c-t,5:a-t,6:d-t,7:t}
  if min(ns.values())<0:continue
  eng=SubsetEngine(20,3,ns);z=eng.verify(eng.solve());z.update(degrees=[7,7,b],codegrees=[c,a,d],triple=t);z['strict']=z['bound']<1
  if not z['strict']:
   jj=solve_profile(eng3,dict(z,graph='r2high',group=len(triples)),permutation_limit=6);z['joint']=jj;z['strict']=Q(jj.get('bound','2'))<1
  triples.append(z)
(HERE/'HIGH_OUTSIDE_PILOT.json').write_text(json.dumps(json_value(dict(scope=__doc__,pairs=pairs,triples=triples,elapsed_seconds=time.time()-start)),indent=2)+'\n')
print('pairs',len(pairs),'strict',sum(z['strict'] for z in pairs),'triples',len(triples),'strict',sum(z['strict'] for z in triples),'seconds',time.time()-start,flush=True)
