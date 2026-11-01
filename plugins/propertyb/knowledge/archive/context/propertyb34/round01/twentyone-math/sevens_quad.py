from pathlib import Path
import sys,time,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(ROOT/'context/propertyb34/round01/high-math')]
from quad_general import *
from subset_position_dp import SubsetEngine
start=time.time();out=[]
for ds in [(6,7,7,7),(6,7,7,8)]:
 for mode in ['A','B']:
  lss=[(1,1,1,2,2,2)] if mode=='A' and ds[-1]==7 else [(2,2,2,1,1,1)] if ds[-1]==7 else [(1,1,1,2,b,c) if mode=='A' else (2,2,1,1,b,c) for b,c in product([1,2],repeat=2)]
  for ls in lss:
   for ns,q,ts in profiles(ds,ls):
    if ds[-1]==7:
     if mode=='A' and q!=1:continue
     if mode=='B' and (q or any(ts[:3])):continue
    else:
     if q:continue
     if mode=='A' and (ts[0]!=1 or ts[1] or ts[2]):continue
     if mode=='B' and ts[0]:continue
    z=SubsetEngine(21,4,ns).solve();p=Profile(21,5,z['positions'],ns);cs=[certificate(p,i) for i in range(4)];rs=rows(p,deductions={p.positions[i]:cs[i]['loss'] for i in range(4)})
    r=dict(v=21,ds=ds,ls=ls,mode=mode,q=q,t3=ts,counts=ns,pos=z['positions'],cs=cs,rows=rs,bound=total_bound(rs));assert z['bound']==r['bound'];out.append(r)
    print(ds,mode,ls,ts,q,r['bound'],flush=True)
Path(__file__).with_name('SEVENS_QUAD.json').write_text(json.dumps(json_value(dict(cases=out,seconds=time.time()-start)),indent=2))
print('strict',sum(r['bound']<1 for r in out),'/',len(out),'seconds',time.time()-start)
