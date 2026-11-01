"""Full position/order exact DP and one bounded joint pass on70 true S4 orbits."""
from pathlib import Path
import sys,json,time
from fractions import Fraction as Q
HERE=Path(__file__).parent;ROOT=HERE.parents[4];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
source=json.loads((HERE/'FOUR_SEVENS_DOMAIN.json').read_text())['orbits'];start=time.time();out=[]
for r in source:
 eng=SubsetEngine(20,4,r['counts']);z=eng.solve();z=eng.verify(z);z.update(r);z['strict']=z['bound']<1;out.append(z)
 print(r['id'],z['bound'],flush=True)
(HERE/'FOUR_SEVENS_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
print('DP',len(out),'strict',sum(z['strict'] for z in out),'seconds',time.time()-start,flush=True)
joints=[];eng=Engine(20,4)
for r in out:
 if r['strict']:continue
 w=dict(r,graph='four7',group=r['id']);z=solve_profile(eng,w,permutation_limit=24);z['source_id']=r['id'];joints.append(z)
 print('joint',r['id'],r['bound'],'->',z.get('bound',z.get('status')),len(z.get('layouts',[])),flush=True)
(HERE/'FOUR_SEVENS_JOINT.json').write_text(json.dumps(json_value(dict(scope=__doc__,results=joints,elapsed_seconds=time.time()-start)),indent=2)+'\n')
print('jointed',len(joints),'strict',sum(Q(z.get('bound','2'))<1 for z in joints),'seconds',time.time()-start)
