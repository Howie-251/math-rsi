"""Exact repaired all-avoided-quota joint refinement of complete677 necessary triples."""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;BASE=HERE.parent;ROOT=HERE.parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math'),str(BASE/'two_low_high_star')]
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from unpaired_three import serial
st=time.time();src=json.loads((HERE/'ALL677_DP.json').read_text())['cases'];eng=Engine(21,3);out=[]
for r in src:
 if r['strict']:continue
 z=solve_profile(eng,dict(r,counts={m:n for m,n in r['counts'].items() if n},graph='ALL677',group=r['id']),permutation_limit=120);z['source_id']=r['id'];out.append(z);print(r['id'],r['codegrees'],r['triple'],r['bound'],'->',z.get('bound',z.get('status')),flush=True)
(HERE/'ALL677_JOINT.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,results=out,elapsed_seconds=time.time()-st)),indent=2)+'\n')
