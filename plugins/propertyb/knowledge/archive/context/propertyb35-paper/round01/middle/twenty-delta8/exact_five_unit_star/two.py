"""Center8, actual unit neighbors8/9. Reuse old888 and newly certified889 triples;
only the eight genuinely new899 triple profiles are solved. Common partition is retained.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction as Q
import json,sys,time
HERE=Path(__file__).parent;ROOT=HERE.parents[5];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb35-paper/round01/twenty-single-seven'),str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from pilot import parts,recover
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
start=time.time();old=json.loads((HERE.parents[1]/'20-new-high/DIAGNOSIS.json').read_text())['triples'];mixed=json.loads((HERE.parent/'exact_five_external/mixed_triples/GENERAL_GATE.json').read_text())['cases'];out=[]
for a,b in ((8,8),(8,9),(9,9)):
 for c in range(1,5 if a==b==9 else 4):
  for part in parts(2):
   t=int(len(part)==1);ns=recover(8,(a,b),(c,),part,{})
   if a==b==8:z=dict(next(r for r in old if r['degrees']==[8,8,8] and r['codegrees']==[1,1,c] and r['triple']==t));source='old888'
   elif a==8:z=dict(next(r for r in mixed if r['codegrees']==[1,1,c] and r['triple']==t));source='mixed889'
   else:
    en=SubsetEngine(20,3,ns);z=en.verify(en.solve());z['strict']=z['bound']<1;source='fresh899'
    if not z['strict']:z['joint']=solve_profile(Engine(20,3),dict(z,graph='unit899',group=len(out)),permutation_limit=6);z['strict']=Q(z['joint'].get('bound','2'))<1
   assert all(ns.get(t,0)==z['counts'].get(t,z['counts'].get(str(t),0)) for t in range(8))
   z.update(id=len(out),neighbor_degrees=[a,b],neighbor_codegree=c,partition=part,counts=ns,source=source);out.append(z)
 print(a,b,'cases',sum(r['neighbor_degrees']==[a,b] for r in out),'res',[(r['neighbor_codegree'],r['partition']) for r in out if r['neighbor_degrees']==[a,b] and not r['strict']],flush=True)
(HERE/'UNIT_TWO.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('seconds',time.time()-start)
