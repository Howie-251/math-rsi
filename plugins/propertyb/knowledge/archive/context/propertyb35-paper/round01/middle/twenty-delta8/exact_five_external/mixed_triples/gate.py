"""Fresh (8,8,9) mixed triple gate, conditional external9 chosen with S<=8.
Low pair c=1..3, high-low a,b>=1 and a+b<=5 (remaining3 lows each>=1).
Modulo ONLY interchange of the two8 points. Inclusive triple0..min(c,a,b), all exact slots nonnegative.
"""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[6];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
start=time.time();out=[];eng3=Engine(20,3)
for c in range(1,4):
 for a in range(1,5):
  for b in range(a,5):
   if a+b>5:continue
   for t in range(min(c,a,b)+1):
    ns={7:t,3:c-t,5:a-t,6:b-t,1:8-c-a+t,2:8-c-b+t,4:9-a-b+t,0:10+c+a+b-t}
    if min(ns.values())<0:continue
    en=SubsetEngine(20,3,ns);z=en.verify(en.solve());z.update(id=len(out),degrees=[8,8,9],codegrees=[c,a,b],triple=t,strict=z['bound']<1)
    if not z['strict']:
     z['joint']=solve_profile(eng3,dict(z,graph='889fresh',group=len(out)),permutation_limit=6);z['strict']=Q(z['joint'].get('bound','2'))<1
    out.append(z);print(z['id'],c,a,b,t,z['bound'],z.get('joint',{}).get('bound'),z['strict'],flush=True)
result=dict(scope=__doc__,complete=True,cases=out,fixed_strict=sum(Q(z['bound'])<1 for z in out),after_joint_strict=sum(z['strict'] for z in out),elapsed_seconds=time.time()-start)
(HERE/'GATE.json').write_text(json.dumps(json_value(result),indent=2)+'\n');print('complete',len(out),'fixed',result['fixed_strict'],'afterjoint',result['after_joint_strict'],'seconds',time.time()-start)
