"""Shared actual bad-pair layouts for exactly four selected low-star residual inventories."""
from pathlib import Path
import sys,json,time
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
from fractions import Fraction as Q

def main():
 st=time.time();src=json.loads((HERE/'STAR_LOW_DP.json').read_text())['cases'];need=[(i,r) for i,r in enumerate(src) if not r['strict'] and tuple(r['neighbor_degrees']) in [(5,8,8),(6,7,8)]];out=[];eng=Engine(21,4)
 for i,r in need:
  z=solve_profile(eng,dict(r,graph='low_unit_star',group=i),permutation_limit=24);z['source_id']=i;out.append(z)
  print(i,r['neighbor_degrees'],r['bound'],'->',z.get('bound',z.get('status')),z.get('LP_bound'),flush=True)
 (HERE/'JOINT_LOW.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(need),need_count=len(need),results=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st)
if __name__=='__main__':main()
