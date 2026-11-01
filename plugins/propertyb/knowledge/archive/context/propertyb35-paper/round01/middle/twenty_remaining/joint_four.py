"""One finite shared-bad-slot joint pass on the164 DP-residual four-neighbour profiles."""
from pathlib import Path
import sys,json,time
from fractions import Fraction as Q
HERE=Path(__file__).parent;ROOT=HERE.parents[4];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
start=time.time();eng=Engine(20,5);old=json.loads((HERE/'STAR_FOUR_DP.json').read_text())['cases'];need=[r for r in old if not r['strict']];out=[]
for n,r in enumerate(need):
 w=dict(r,graph='star4',group=r['source_id']);z=solve_profile(eng,w,permutation_limit=120);z['source_id']=r['source_id'];out.append(z)
 print(n,r['source_id'],r['neighbor_degrees'],r['bound'],'->',z.get('bound',z.get('status')),len(z.get('layouts',[])),flush=True)
 if n%10==9 or len(out)==len(need) or time.time()-start>70:
  (HERE/'STAR_FOUR_JOINT.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(need),need_count=len(need),results=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
 if time.time()-start>70:break
print('processed',len(out),'strict',sum(Q(z.get('bound','2'))<1 for z in out),'seconds',time.time()-start)
