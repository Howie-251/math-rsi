"""All actual three degree8 unit neighbours, after strict codegree>=4 pairs."""
from pathlib import Path
import sys,json,time
from itertools import product
P=Path(__file__).resolve();ROOT=P.parents[4];HERE=P.parent
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'context/propertyb35-paper/round01/middle'),str(ROOT/'context/propertyb35-paper/round01/middle/twentytwo'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from star_pilot import parts,recover
from multilock import json_value
start=time.process_time();out=[]
for ps in product(range(1,4),repeat=3):
 for part in parts(3):
  for t in range(min(ps)+1):
   ns=recover(6,[8]*3,ps,part,{7:t})
   if ns is None:continue
   eng=SubsetEngine(22,4,ns);r=eng.verify(eng.solve());r.update(neighbor_degrees=[8]*3,center_partition=part,neighbor_codegrees=ps,triple=t,strict=r['bound']<1,source_id=len(out));r.pop('rows',None);out.append(r)
print('complete',len(out),'strict',sum(r['strict'] for r in out),'cpu',time.process_time()-start,flush=True)
(HERE/'EIGHT_THREE.json').write_text(json.dumps(json_value(dict(cases=out,cpu_seconds=time.process_time()-start)),indent=2)+'\n')
