from pathlib import Path
import sys,time,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4];sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math')]
from probe import *
start=time.time();out=[]
for ds in [(6,6,6),(6,6,7),(6,6,8),(6,7,7),(6,7,8)]:
 rr=[]
 for a,b,c in product(range(1,5),repeat=3):
  if a+b>6:continue
  if ds[1]==6 and a+c>6:continue
  if ds[2]==6 and b+c>6:continue
  for t in range(min(a,b,c)+1):
   r=best(21,ds,(a,b,c),t)
   if r:rr.append(r);out.append(r)
 fail=[r for r in rr if r['bound']>=1]
 print(ds,'total',len(rr),'fail',len(fail),'residual',[(r['ls'],r['t'],str(r['bound'])) for r in fail],flush=True)
 if time.time()-start>60:break
Path(__file__).with_name('TRIPLE_LOW.json').write_text(json.dumps(json_value(dict(cases=out,seconds=time.time()-start)),indent=2))
print('seconds',time.time()-start)
