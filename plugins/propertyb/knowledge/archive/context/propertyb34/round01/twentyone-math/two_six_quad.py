from pathlib import Path
import sys,time,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'context/propertyb34-hour1-20261013/low-math'))
from quad_general import *
from twentyone_five import dual
start=time.time();out=[]
for a,b in product((1,2),repeat=2):
 ls=(a,1,1,1,1,b)
 for ns,q,ts in profiles((6,6,8,8),ls):
  if q or ts[0] or ts[1]:continue
  opts=[]
  for k in [9,8,10,7,11]:
   for pos in permutations(range(k,k+4)):
    p=Profile(21,5,pos,ns);cs=[dual(p,i) for i in range(4)];rs=rows(p,deductions={pos[i]:cs[i]['loss'] for i in range(4)})
    r=dict(v=21,ds=(6,6,8,8),ls=ls,q=q,t3=ts,counts=ns,pos=pos,cs=cs,rows=rs,bound=total_bound(rs));opts.append(r)
    if r['bound']<1:break
   if opts[-1]['bound']<1:break
  r=min(opts,key=lambda z:z['bound']);out.append(r);print(ls,ts,r['bound'],float(r['bound']),flush=True)
Path(__file__).with_name('TWO_SIX_QUAD.json').write_text(json.dumps(json_value(dict(cases=out,seconds=time.time()-start)),indent=2))
print('strict',sum(r['bound']<1 for r in out),'/',len(out),'seconds',time.time()-start)
