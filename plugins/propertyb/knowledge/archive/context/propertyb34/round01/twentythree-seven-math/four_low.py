from pathlib import Path
import sys,time,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(ROOT/'context/propertyb34/round01/high-math')]
from quad_general import *
from subset_position_dp import SubsetEngine
HERE=Path(__file__).resolve().parent;start=time.time();out=[];seen=set();ds=(7,)*4;scanned=0;complete=True
maps=[{t:sum(1<<p[i] for i in range(4) if t&(1<<i)) for t in range(16)} for p in permutations(range(4))]
for ls in product((1,2,3),repeat=6):
 for ns,q,ts in profiles(ds,ls):
  scanned+=1;key=min(tuple(sorted((mp[t],c) for t,c in ns.items() if c)) for mp in maps)
  if key in seen:continue
  seen.add(key);z=SubsetEngine(23,4,ns).solve();p=Profile(23,5,z['positions'],ns);cs=[certificate(p,i) for i in range(4)];rs=rows(p,deductions={p.positions[i]:cs[i]['loss'] for i in range(4)})
  r=dict(v=23,ds=ds,ls=ls,q=q,t3=ts,counts=ns,pos=z['positions'],cs=cs,rows=rs,bound=total_bound(rs));assert z['bound']==r['bound'];out.append(r)
  if len(out)%200==0:print('done',len(out),'strict',sum(z['bound']<1 for z in out),'scanned',scanned,'seconds',time.time()-start,flush=True)
  if time.time()-start>90:complete=False;break
 if not complete:break
(HERE/'FOUR_LOW.json').write_text(json.dumps(json_value(dict(cases=out,scanned=scanned,complete=complete,seconds=time.time()-start)),indent=2))
print('strict',sum(r['bound']<1 for r in out),'/',len(out),'scanned',scanned,'complete',complete,'seconds',time.time()-start)
