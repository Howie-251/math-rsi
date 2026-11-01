from pathlib import Path
import sys,json,time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(ROOT/'context/propertyb34/round01/high-math')]
from probe import *
from subset_position_dp import SubsetEngine
HERE=Path(__file__).resolve().parent;start=time.time();out=[]
for a in range(1,8):
 r=calc(23,(7,7),(a,),0,(11,12));z=SubsetEngine(23,2,r['counts']).solve();r=calc(23,(7,7),(a,),0,z['positions']);out.append(r);print('double',a,r['bound'],r['pos'])
(HERE/'DOUBLES.json').write_text(json.dumps(json_value({'cases':out}),indent=2));out=[]
for ls in product(range(1,4),repeat=3):
 for t in range(min(ls)+1):
  r=calc(23,(7,7,7),ls,t,(10,11,12))
  if not r:continue
  z=SubsetEngine(23,3,r['counts']).solve();r=calc(23,(7,7,7),ls,t,z['positions']);assert r['bound']==z['bound'];out.append(r)
(HERE/'TRIPLES.json').write_text(json.dumps(json_value({'cases':out}),indent=2));print('triples strict',sum(r['bound']<1 for r in out),'/',len(out),'seconds',time.time()-start)
