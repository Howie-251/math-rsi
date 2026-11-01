from pathlib import Path
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[3]
sys.dont_write_bytecode=True
sys.path[:0]=[str(HERE),str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
from fractions import Fraction as Q
start=time.time();out=[]
source=json.loads((HERE/'UNIT_TWO.json').read_text())['cases'];needed=[(i,r) for i,r in enumerate(source) if not r['strict'] and r['degrees'][1:]==[8,8]]
eng=Engine(20,3)
for i,r in needed:
 z=solve_profile(eng,dict(r,graph='two8',group=i),permutation_limit=6);z['source_id']=i;out.append(z);print('two8',i,z.get('bound',z.get('status')),time.time()-start,flush=True)
(HERE/'JOINT_TWO8.json').write_text(json.dumps(json_value(dict(results=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
source=json.loads((HERE/'UNIT_THREE.json').read_text())['cases'];needed=[(i,r) for i,r in enumerate(source) if not r['strict'] and r['neighbor_degrees']==[8,9,9]]
eng=Engine(20,4);out=[]
for i,r in needed:
 z=solve_profile(eng,dict(r,graph='899',group=i),permutation_limit=24);z['source_id']=i;out.append(z);print('899',i,z.get('bound',z.get('status')),time.time()-start,flush=True)
 (HERE/'JOINT_899.json').write_text(json.dumps(json_value(dict(results=out,need_count=len(needed),complete=len(out)==len(needed),elapsed_seconds=time.time()-start)),indent=2)+'\n')
 if time.time()-start>100:break
