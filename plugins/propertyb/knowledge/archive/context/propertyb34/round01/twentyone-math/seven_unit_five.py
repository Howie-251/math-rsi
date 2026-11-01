from pathlib import Path
import sys,time,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(ROOT/'context/propertyb34/round01/high-math')]
from five_general import *
from subset_position_dp import SubsetEngine
start=time.time();out=[];ds=(7,8,8,8,8);ls=(1,1,1,1,2,2,2,2,2,2)
forbid=[m for m in range(32) if m.bit_count()>=4 and m&1]
for idx,ns in enumerate(profiles(5,ds,ls,forbid)):
 if not sum(c for m,c in ns.items() if m&7==7):continue
 z=SubsetEngine(21,5,ns).solve();r=calc_counts(21,ds,ns,z['positions']);assert z['bound']==r['bound'];out.append(r)
 if len(out)%25==0:print('done',len(out),'strict',sum(t['bound']<1 for t in out),'sec',time.time()-start,flush=True)
 if time.time()-start>60:break
Path(__file__).with_name('SEVEN_UNIT_FIVE.json').write_text(json.dumps(json_value(dict(cases=out,seconds=time.time()-start)),indent=2))
print('strict',sum(r['bound']<1 for r in out),'/',len(out),'seconds',time.time()-start)
