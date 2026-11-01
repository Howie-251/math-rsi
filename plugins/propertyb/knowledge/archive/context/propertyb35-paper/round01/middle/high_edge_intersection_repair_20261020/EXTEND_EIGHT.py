"""Actual centre-x star expansion of only the eight failed p-quad profiles."""
from pathlib import Path
from itertools import product
import sys,json,time
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb35-paper/round01/middle'),str(ROOT/'context/propertyb34/round01/high-math')]
from subset_position_dp import SubsetEngine
from pilot import json_value
st=time.process_time();data=json.loads((HERE/'RESULT.json').read_text());out=[]
def partitions(xs):
 if not xs:yield [];return
 x=xs[0]
 for pp in partitions(xs[1:]):
  yield [[x]]+pp
  for j in range(len(pp)):yield pp[:j]+[[x]+pp[j]]+pp[j+1:]
for sid in data['p_nonstrict_ids']:
 r=data['p_cases'][sid];ns={int(t):n for t,n in r['counts'].items()};ds=r['degrees']
 for extra in ([False,True] if 8 in ds else [False]):
  selected=list(range(4))+([1] if extra else [])
  hs=set()
  for pp in partitions(selected):
   if any(len(set(b))<len(b) for b in pp):continue
   hh=[0]*16
   for b in pp:hh[sum(1<<i for i in b)]+=1
   hh[0]=6-len(pp)
   if hh[0]<0 or any(hh[t]>ns.get(t,0) for t in range(16)):continue
   assert hh[15]<=1
   hs.add(tuple(hh))
  for hh in sorted(hs):
   nn={}
   for t,n in ns.items():
    if n-hh[t]:nn[t<<1]=n-hh[t]
    if hh[t]:nn[(t<<1)|1]=hh[t]
   if hh[0] and 0 not in ns:raise AssertionError
   assert sum(nn.values())==35
   assert all(sum(n for t,n in nn.items() if t>>i&1)==d for i,d in enumerate([6]+ds))
   e=SubsetEngine(21,5,nn);z=e.verify(e.solve())
   out.append(dict(source_id=sid,eight_is_nonunit=extra,center_counts=list(hh),counts=nn,positions=z['positions'],bound=z['bound'],strict=z['bound']<1))
   assert time.process_time()-st<40
 print(sid,'total',len(out),'nonstrict',sum(not z['strict'] for z in out),flush=True)
assert {r['source_id'] for r in out}==set(data['p_nonstrict_ids'])
result=dict(complete=True,cases=out,nonstrict_ids=[i for i,z in enumerate(out) if not z['strict']],cpu_seconds=time.process_time()-st)
(HERE/'EXTENDED.json').write_text(json.dumps(json_value(result),indent=2)+'\n')
print('cpu',time.process_time()-st)
