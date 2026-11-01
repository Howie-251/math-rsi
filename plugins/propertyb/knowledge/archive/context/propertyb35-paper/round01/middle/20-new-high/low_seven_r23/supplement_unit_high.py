"""Complete newly bounded actual unit-high degrees16..19 under the 83-profile degree budget.
Only eight7/7/b triples: low codegree2, cross1/1, inclusive triple0/1.
"""
from pathlib import Path
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[5];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations'),str(HERE)]
from subset_position_dp import SubsetEngine
from multilock import json_value
from replay_r3 import fixed
start=time.time();out=[]
for b in range(16,20):
 for t in (0,1):
  ns={0:25-b-t,1:4+t,2:4+t,4:b-2+t,3:2-t,5:1-t,6:1-t,7:t};eng=SubsetEngine(20,3,ns);z=eng.verify(eng.solve());z.update(degrees=[7,7,b],codegrees=[2,1,1],triple=t);assert fixed(json_value(z))==z['bound']<1;out.append(z)
(HERE/'C2_HIGH_UNIT_16_19.json').write_text(json.dumps(json_value(dict(status='PASS',scope=__doc__,cases=out,all_fixed_strict=True,max_bound=max(r['bound'] for r in out),elapsed_seconds=time.time()-start)),indent=2)+'\n');print('all eight strict max',max(r['bound'] for r in out),'seconds',time.time()-start)
