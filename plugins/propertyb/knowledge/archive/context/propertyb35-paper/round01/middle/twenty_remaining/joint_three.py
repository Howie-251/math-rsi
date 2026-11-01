"""Shared actual bad-slot vectors across layouts for the remaining fixed440-star domain.
Exact repaired rational duals; numerical LP proposes, no float acceptance.
"""
from pathlib import Path
import sys
HERE=Path(__file__).parent;ROOT=HERE.parents[4]
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
from fractions import Fraction as Q
import json,time
start=time.time();eng=Engine(20,4);old=json.loads((HERE/'STAR_THREE_REFINED.json').read_text())['cases']
need=sorted([(i,r) for i,r in enumerate(old) if not r['strict']],key=lambda z:Q(z[1]['bound']));out=[]
for i,r in need:
 w=dict(r,graph='star3',group=i);z=solve_profile(eng,w,permutation_limit=24);z['source_id']=i;out.append(z)
 print(i,r['neighbor_degrees'],r['bound'],'->',z.get('bound',z.get('status')),z.get('LP_bound'),len(z.get('layouts',[])),flush=True)
 (HERE/'STAR_THREE_JOINT.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(need),need_count=len(need),results=out,elapsed_seconds=time.time()-start)),indent=2)+'\n')
 if time.time()-start>75:break
print('processed',len(out),'strict',sum(Q(z.get('bound','2'))<1 for z in out),'seconds',time.time()-start)
