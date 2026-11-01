from pathlib import Path
import sys,time,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(ROOT/'context/propertyb34/round01/high-math')]
from probe import *
from subset_position_dp import SubsetEngine
start=time.time();out=[]
for ds in [(7,7,7),(7,7,8),(7,8,8)]:
 cases=[]
 for a,b,c in product(range(1,5),repeat=3):
  if ds==(7,8,8) and (a,b)!=(1,1):continue
  for t in range(min(a,b,c)+1):
   r=calc(21,ds,(a,b,c),t,(9,10,11))
   if r is None:continue
   z=SubsetEngine(21,3,r['counts']).solve();r=calc(21,ds,(a,b,c),t,z['positions']);assert r['bound']==z['bound'];cases.append(r);out.append(r)
 fail=[r for r in cases if r['bound']>=1];print(ds,'strict',len(cases)-len(fail),'/',len(cases),'residual',[(r['ls'],r['t'],str(r['bound'])) for r in fail],flush=True)
Path(__file__).with_name('SEVEN_TRIPLES.json').write_text(json.dumps(json_value(dict(cases=out,seconds=time.time()-start)),indent=2))
print('seconds',time.time()-start)
