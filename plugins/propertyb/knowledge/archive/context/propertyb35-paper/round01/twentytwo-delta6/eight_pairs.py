from pathlib import Path
import sys,json,time
P=Path(__file__).resolve();ROOT=P.parents[4];HERE=P.parent
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'context/propertyb35-paper/round01/middle'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from pilot import triple
from multilock import json_value
start=time.process_time();out=[]
for a,b in [(6,6),(6,7),(6,8),(7,7),(7,8),(8,8)]:
 for c in range(1,min(a,b)+1):
  for t in (0,1):
   ns=triple(22,[6,a,b],(1,1,c),t)
   if min(ns.values())<0:continue
   eng=SubsetEngine(22,3,ns);r=eng.verify(eng.solve());r.update(degrees=[6,a,b],codegrees=[1,1,c],triple=t,strict=r['bound']<1);r.pop('rows',None);out.append(r)
print([(r['degrees'],r['codegrees'][-1],r['triple'],str(r['bound']))for r in out],flush=True)
(HERE/'EIGHT_PAIRS.json').write_text(json.dumps(json_value(dict(cases=out,cpu_seconds=time.process_time()-start)),indent=2)+'\n')
