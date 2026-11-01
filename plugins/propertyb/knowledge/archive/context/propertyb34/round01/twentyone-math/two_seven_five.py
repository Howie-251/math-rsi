from pathlib import Path
import sys,time,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(ROOT/'context/propertyb34/round01/high-math')]
from five_general import *
from subset_position_dp import SubsetEngine
start=time.time();out=[];ds=(6,7,7,8,8)
for b in [1,2]:
 ls=(1,1,1,1,2,1,1,1,1,b)
 forbid=[m for m in range(32) if m.bit_count()>=3 and (m&7).bit_count()>=2 and m!=7]
 for ns in profiles(5,ds,ls,forbid):
  if ns.get(7,0)!=1:continue
  z=SubsetEngine(21,5,ns).solve();r=calc_counts(21,ds,ns,z['positions']);assert z['bound']==r['bound'];r['ls']=ls;out.append(r);print(b,{m:c for m,c in ns.items() if m.bit_count()>=3 and c},r['bound'],flush=True)
Path(__file__).with_name('TWO_SEVEN_FIVE.json').write_text(json.dumps(json_value(dict(cases=out,seconds=time.time()-start)),indent=2))
print('strict',sum(r['bound']<1 for r in out),'/',len(out),'seconds',time.time()-start)
