from pathlib import Path
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[3]
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
from fractions import Fraction as Q
start=time.time();source=json.loads((HERE/'EIGHT_FIVE_DP.json').read_text())['cases'];needed=[(i,r) for i,r in enumerate(source) if not r['strict']];eng=Engine(20,6);out=[]
for i,r in needed:
 z=solve_profile(eng,dict(r,graph='eightfive',group=i),permutation_limit=120);z['source_id']=i;out.append(z)
 if len(out)%10==0:print('four',len(out),'strict',sum(Q(z.get('bound','2'))<1 for z in out),'sec',time.time()-start,flush=True)
 if len(out)%10==0 or len(out)==len(needed):(HERE/'JOINT_EIGHT_FIVE.json').write_text(json.dumps(json_value(dict(results=out,complete=len(out)==len(needed),need_count=len(needed),elapsed_seconds=time.time()-start)),indent=2)+'\n')
 if time.time()-start>120:break
