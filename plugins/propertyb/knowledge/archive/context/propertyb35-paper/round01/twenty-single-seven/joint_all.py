from pathlib import Path
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[3]
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
from fractions import Fraction as Q
start=time.time();source=json.loads((HERE/'UNIT_THREE.json').read_text())['cases'];needed=[(i,r) for i,r in enumerate(source) if not r['strict']];eng=Engine(20,4);out=[]
for i,r in needed:
 z=solve_profile(eng,dict(r,graph='three',group=i),permutation_limit=24);z['source_id']=i;out.append(z)
 if len(out)%30==0:print('three',len(out),'strict',sum(Q(z.get('bound','2'))<1 for z in out),'sec',time.time()-start,flush=True)
(HERE/'JOINT_THREE_ALL.json').write_text(json.dumps(json_value(dict(results=out,complete=len(out)==len(needed),elapsed_seconds=time.time()-start)),indent=2)+'\n')
source=json.loads((HERE/'UNIT_FOUR_DP.json').read_text())['cases'];needed=[(i,r) for i,r in enumerate(source) if not r['strict'] and r['neighbor_degrees']==[9]*4];eng=Engine(20,5);out=[]
for i,r in needed:
 z=solve_profile(eng,dict(r,graph='four9',group=i),permutation_limit=120);z['source_id']=i;out.append(z)
 if len(out)%20==0:print('four9',len(out),'strict',sum(Q(z.get('bound','2'))<1 for z in out),'sec',time.time()-start,flush=True)
 (HERE/'JOINT_FOUR9.json').write_text(json.dumps(json_value(dict(results=out,complete=len(out)==len(needed),need_count=len(needed),elapsed_seconds=time.time()-start)),indent=2)+'\n')
 if time.time()-start>120:break
