"""Small actual a7=1 domains: x6, p7 with center codegree1/2, and two unit8/9."""
from pathlib import Path
from itertools import combinations,product
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[5];BASE=HERE.parents[1]
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(BASE/'two_low_high_star')]
from subset_position_dp import SubsetEngine
from unpaired_three import serial
def recover(inc):
 ns={A:sum((-1)**(B.bit_count()-A.bit_count())*v for B,v in inc.items() if B&A==A) for A in range(16)}
 return ns if min(ns.values())>=0 else None
def main():
 st=time.time();gunit=json.loads((HERE.parent/'UNIT7_GATES.json').read_text())['cases'];gnon=json.loads((HERE/'NONUNIT7_GATES.json').read_text())['cases'];gp=json.loads((BASE/'UNIT_PAIRS.json').read_text())['cases'];opts={}
 for r in gunit+gnon+gp:
  if not r['strict']:opts.setdefault((tuple(r['degrees']),tuple(r['codegrees'][:2])),set()).add((r['codegrees'][2],r['triple']))
 out=[];labelled=[];seen={}
 for a in (1,2):
  for b,c in ((8,8),(8,9),(9,9)):
   start=len(out);nlabels=0
   for (cpz,tpz),(cpw,tpw),(czw,tzw) in product(opts[((6,7,b),(a,1))],opts[((6,7,c),(a,1))],opts[((6,b,c),(1,1))]):
    if b==c and (cpz,tpz)>(cpw,tpw):continue
    for tpzw in range(min(cpz,cpw,czw)+1):
     for q in range(min(tpz,tpw,tzw,tpzw)+1):
      inc={0:35,1:6,2:7,4:b,8:c,3:a,5:1,9:1,6:cpz,10:cpw,12:czw,7:tpz,11:tpw,13:tzw,14:tpzw,15:q};ns=recover(inc)
      if ns is None:continue
      k=tuple(ns.values())
      if k in seen:continue
      oid=len(out);eng=SubsetEngine(21,4,ns);z=eng.verify(eng.solve());z.update(id=oid,degrees=[6,7,b,c],center_seven_codegree=a,counts=ns,strict=z['bound']<1);out.append(z);seen[k]=oid
      if b==c:
       def swap(m):return (m&3)|((m&4)<<1)|((m&8)>>1)
       seen[tuple({swap(m):v for m,v in ns.items()}.get(t,0) for t in range(16))]=oid
   rr=out[start:];print(a,b,c,'orbits',len(rr),'strict',sum(r['strict'] for r in rr),'max',max((r['bound'] for r in rr),default=None),flush=True)
 (HERE/'FOUR_DP.json').write_text(json.dumps(serial(dict(scope=__doc__,complete_representative_domain=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st,flush=True)
if __name__=='__main__':main()
