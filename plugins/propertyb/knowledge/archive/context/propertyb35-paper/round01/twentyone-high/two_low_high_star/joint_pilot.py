"""Bounded exact repaired joint-layout diagnostic for the three-unpaired double-star residuals."""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from unpaired_three import serial

def main():
 st=time.time();src=json.loads((HERE/'UNPAIRED_THREE_DP.json').read_text())['cases'];chosen=[]
 for c in (1,2):
  for ds in [(8,8,8),(8,8,9),(8,9,9),(9,9,9)]:
   rr=[r for r in src if r['center_codegree']==c and tuple(r['degrees'][2:])==ds and not r['strict']];chosen.append(max(rr,key=lambda r:Q(r['bound'])))
 eng=Engine(21,5);out=[]
 for r in chosen:
  z=solve_profile(eng,dict(r,graph='doubleunit',group=r['id']),permutation_limit=120);z['source_id']=r['id'];out.append(z);print(r['center_codegree'],r['degrees'][2:],r['id'],r['bound'],'->',z.get('bound',z.get('status')),'seconds',time.time()-st,flush=True)
  (HERE/'JOINT_PILOT.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=False,selected_ids=[r['id'] for r in chosen],results=out,elapsed_seconds=time.time()-st)),indent=2)+'\n')
  if time.time()-st>55:break
if __name__=='__main__':main()
