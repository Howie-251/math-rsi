from pathlib import Path
import sys,time,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(ROOT/'context/propertyb34/round01/high-math')]
from five_general import *
from subset_position_dp import SubsetEngine
HERE=Path(__file__).resolve().parent;start=time.time();out=[];ds=(7,7,8,8,8);complete=True
for a,b in product([1,2],[1,2]):
 ls=(a,1,1,1,b,b,b,2,2,2)
 forbid=[m for m in range(32) if (m&29)==29 or b==1 and (m&30)==30]
 for ns in profiles(5,ds,ls,forbid):
  z=SubsetEngine(21,5,ns).solve();r=calc_counts(21,ds,ns,z['positions']);assert z['bound']==r['bound'];r['ls']=ls;out.append(r)
  if time.time()-start>90:complete=False;break
 print(a,b,'done',len(out),'strict',sum(z['bound']<1 for z in out),'seconds',time.time()-start,flush=True)
 if not complete:break
(HERE/'TWO_SEVEN_THREE_EIGHT.json').write_text(json.dumps(json_value(dict(cases=out,complete=complete,seconds=time.time()-start)),indent=2))
