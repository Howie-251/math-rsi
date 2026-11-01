"""Complete local promotion of six unit degree-six locks by one unit degree-seven lock."""
from pathlib import Path
import sys,json,time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4];OLD=ROOT/'context/propertyb34-hour1-20261013/high-math'
sys.path[:0]=[str(Path(__file__).parent),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from multilock import json_value

def extensions(ns,s=6,degree=7):
 full=(1<<s)-1;blocks=sorted(t for t,n in ns.items() if t and n>0 and t.bit_count()<5)
 def rec(left,chosen):
  if not left:
   nc=ns.copy()
   for t in chosen:nc[t]-=1;nc[t|(1<<s)]=1
   nc[1<<s]=degree-len(chosen);nc[0]-=nc[1<<s]
   if min(nc.values())>=0:yield {t:n for t,n in nc.items() if n}
   return
  bit=left&-left
  for t in blocks:
   if t&bit and t&left==t:yield from rec(left^t,chosen+[t])
 yield from rec(full,[])

if __name__=='__main__':
 source=json.loads((OLD/'MIXED_SIX_v24_low6_badnone.json').read_text())['results'];out=[];start=time.perf_counter()
 for x in source:
  if x['group'] not in (1,3,5,8):continue
  ns={int(t):n for t,n in x['counts'].items()};cases=[]
  for j,nc in enumerate(extensions(ns)):
   eng=SubsetEngine(24,7,nc);z=eng.verify(eng.solve());z['id']=j;cases.append(z)
  out.append(dict(group=x['group'],cases=cases));print(x['group'],len(cases),sum(z['bound']<1 for z in cases),'max',max(z['bound'] for z in cases),time.perf_counter()-start,flush=True)
  Path(__file__).with_name('SIX_LOW_EXTENSION.json').write_text(json.dumps(json_value(dict(scope=__doc__,elapsed=time.perf_counter()-start,results=out)),indent=2)+'\n')
