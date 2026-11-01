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
for d in [6,7,8]:
 local=[]
 for part in parts(4):
  for vals in product((0,1),repeat=5):
   ts=vals[:4];q=vals[4]
   if q>min(ts):continue
   ns=recover(6,[d]*4,[1]*6,part,dict(zip((7,11,13,14,15),vals)))
   if ns is None:continue
   eng=SubsetEngine(22,5,ns);z=eng.verify(eng.solve());z.update(neighbor_degrees=[d]*4,center_partition=part,high=dict(zip((7,11,13,14,15),vals)),strict=z['bound']<1);z.pop('rows',None);local.append(z)
 out.extend(local);print(d,len(local),sum(z['strict'] for z in local),'minmax',min(str(z['bound']) for z in local),max(str(z['bound']) for z in local),'cpu',time.process_time()-start,flush=True)
(HERE/'FOUR_UNITS.json').write_text(json.dumps(json_value(dict(cases=out,cpu_seconds=time.process_time()-start)),indent=2)+'\n')
