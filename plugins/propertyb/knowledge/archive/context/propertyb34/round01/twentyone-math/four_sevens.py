from pathlib import Path
import sys,time,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(ROOT/'context/propertyb34/round01/high-math')]
from quad_general import *
from subset_position_dp import SubsetEngine
start=time.time();out=[];ds=(7,7,7,7)
for ls in product((1,2),repeat=6):
 for ns,q,ts in profiles(ds,ls):
  z=SubsetEngine(21,4,ns).solve();p=Profile(21,5,z['positions'],ns);cs=[certificate(p,i) for i in range(4)];rs=rows(p,deductions={p.positions[i]:cs[i]['loss'] for i in range(4)})
  r=dict(v=21,ds=ds,ls=ls,q=q,t3=ts,counts=ns,pos=z['positions'],cs=cs,rows=rs,bound=total_bound(rs));assert z['bound']==r['bound'];out.append(r)
Path(__file__).with_name('FOUR_SEVENS.json').write_text(json.dumps(json_value(dict(cases=out,seconds=time.time()-start)),indent=2))
print('strict',sum(r['bound']<1 for r in out),'/',len(out),'seconds',time.time()-start)
