from pathlib import Path
import sys,json,time
from fractions import Fraction as Q
P=Path(__file__).resolve();ROOT=P.parents[4];HERE=P.parent
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math'),str(ROOT/'computations')]
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
pairs=json.loads((HERE/'PAIRS.json').read_text())['cases'];three=json.loads((HERE/'UNIT_STAR_THREE.json').read_text())['cases'];four=json.loads((HERE/'FOUR_UNITS.json').read_text())['cases']
selected=[r for r in pairs if r['degrees'][:]==[6,6] and r['codegree']==4 or r['degrees'][:]==[6,7] and r['codegree']==4]
selected += [r for r in three if r['neighbor_degrees']==[6,6,6] and len(r['center_partition'])==3 and r['triple']==0 or r['neighbor_degrees']==[8,8,8] and len(r['center_partition'])==1]
selected += [r for r in four if r['neighbor_degrees'] in [[6]*4,[7]*4] and len(r['center_partition'])==4 and all(v==0 for v in r['high'].values())]
start=time.process_time();out=[]
for i,r in enumerate(selected):
 s=len(r['positions']);eng=Engine(22,s);z=solve_profile(eng,dict(r,graph='n22d6pilot',group=i),permutation_limit=120);z['source']=r;out.append(z)
 print(i,r.get('degrees',r.get('neighbor_degrees')),r['bound'],'->',z.get('bound',z.get('status')),'cpu',time.process_time()-start,flush=True)
(HERE/'JOINT_PILOT.json').write_text(json.dumps(json_value(dict(results=out,cpu_seconds=time.process_time()-start)),indent=2)+'\n')
