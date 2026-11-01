"""Exact repaired joint witnesses for the two complete c1 entry domains."""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from unpaired_three import serial

def main():
 st=time.time()
 for tag,s in [('C1_FOUR',6),('C1_8810',5)]:
  rr=json.loads((HERE/f'{tag}_DP.json').read_text())['cases'];eng=Engine(21,s);out=[]
  for r in rr:
   if r['strict']:continue
   z=solve_profile(eng,dict(r,graph=tag,group=r['id']),permutation_limit=120);z['source_id']=r['id'];out.append(z);print(tag,r['id'],r['bound'],'->',z.get('bound',z.get('status')),flush=True)
  (HERE/f'{tag}_JOINT.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,results=out)),indent=2)+'\n')
 print('seconds',time.time()-st,flush=True)
if __name__=='__main__':main()
