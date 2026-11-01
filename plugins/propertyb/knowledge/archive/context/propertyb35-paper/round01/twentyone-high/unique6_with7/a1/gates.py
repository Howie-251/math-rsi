"""Bounded a7=1 pilot: degree7 nonunit-to-center2 and one actual unit8/9."""
from pathlib import Path
from fractions import Fraction
import json,sys,time
HERE=Path(__file__).parent;ROOT=HERE.parents[5]
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(HERE.parents[1]/'two_low_high_star')]
from subset_position_dp import SubsetEngine
from unpaired_three import serial
def main():
 st=time.time();out=[]
 for d in (8,9):
  for c in range(1,8):
   for t in (0,1):
    inc={0:35,1:6,2:7,4:d,3:2,5:1,6:c,7:t};ns={A:sum((-1)**(B.bit_count()-A.bit_count())*v for B,v in inc.items() if B&A==A) for A in range(8)}
    if min(ns.values())<0:continue
    eng=SubsetEngine(21,3,ns);z=eng.verify(eng.solve());z.update(id=len(out),degrees=[6,7,d],codegrees=[2,1,c],triple=t,counts=ns,strict=z['bound']<1);out.append(z)
  rr=[r for r in out if r['degrees'][-1]==d];print(d,len(rr),'strict',sum(r['strict'] for r in rr),'res',[(r['codegrees'][2],r['triple'],str(r['bound'])) for r in rr if not r['strict']],flush=True)
 (HERE/'NONUNIT7_GATES.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st)
if __name__=='__main__':main()
