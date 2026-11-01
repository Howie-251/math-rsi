from pathlib import Path
import sys,json,time
P=Path(__file__).resolve();ROOT=P.parents[4];HERE=P.parent
sys.dont_write_bytecode=True;sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'context/propertyb35-paper/round01/middle'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from pilot import double
from multilock import json_value
start=time.process_time();out=[]
for c in (2,3,4):
 for d in range(6,36):
  ns=double(22,6,d,c)
  if min(ns.values())<0:continue
  eng=SubsetEngine(22,2,ns);r=eng.verify(eng.solve());r.update(degrees=[6,d],codegree=c,strict=r['bound']<1);r.pop('rows',None);out.append(r)
 print('c',c,'unresolved_degrees',[r['degrees'][1]for r in out if r['codegree']==c and not r['strict']],flush=True)
(HERE/'NONUNIT_PAIRS.json').write_text(json.dumps(json_value(dict(cases=out,cpu_seconds=time.process_time()-start)),indent=2)+'\n')
