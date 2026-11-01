from pathlib import Path
import sys,json,time
from fractions import Fraction as Q
P=Path(__file__).resolve();ROOT=P.parents[4];HERE=P.parent
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math'),str(ROOT/'computations')]
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
source=json.loads((HERE/'EIGHT_THREE.json').read_text())['cases'];eng=Engine(22,4);start=time.process_time();out=[]
for r in source:
 if r['strict']:continue
 z=solve_profile(eng,dict(r,graph='three8',group=r['source_id']),permutation_limit=24);z['source_id']=r['source_id'];out.append(z)
 if len(out)%20==0:print(len(out),'strict',sum(Q(z.get('bound','2'))<1 for z in out),'cpu',time.process_time()-start,flush=True)
 if time.process_time()-start>40:break
print('complete',len(out),'strict',sum(Q(z.get('bound','2'))<1 for z in out),'cpu',time.process_time()-start,flush=True)
(HERE/'EIGHT_THREE_JOINT.json').write_text(json.dumps(json_value(dict(results=out,complete=len(out)==sum(not r['strict'] for r in source),cpu_seconds=time.process_time()-start)),indent=2)+'\n')
