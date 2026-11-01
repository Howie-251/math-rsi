from pathlib import Path
import sys,json,time
from itertools import combinations,product
from fractions import Fraction as Q
P=Path(__file__).resolve();ROOT=P.parents[4];HERE=P.parent
sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'context/propertyb35-paper/round01/middle'),str(ROOT/'context/propertyb35-paper/round01/middle/twentytwo'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from pilot import triple,double
from star_pilot import parts,recover
from multilock import json_value
start=time.process_time();out=[]
# Complete low pair domain: centre has only three units of excess.
for a in (6,7,8):
 for c in range(1,5):
  if c>a:continue
  ns=double(22,6,a,c);eng=SubsetEngine(22,2,ns);r=eng.verify(eng.solve());r.update(degrees=[6,a],codegree=c,strict=r['bound']<1);r.pop('rows',None);out.append(r)
(HERE/'PAIRS.json').write_text(json.dumps(json_value(dict(cases=out,cpu_seconds=time.process_time()-start)),indent=2)+'\n')
print('pairs',[(r['degrees'],r['codegree'],str(r['bound'])) for r in out],flush=True)
# All pairwise-unit three-neighbour profiles for low uniform and mixed pools.
records=[]
for ds in [(6,6,6),(6,6,7),(6,6,8),(6,7,7),(6,7,8),(6,8,8),(7,7,7),(7,7,8),(7,8,8),(8,8,8)]:
 local=[]
 for partition in parts(3):
  for t in (0,1):
   ns=recover(6,ds,(1,1,1),partition,{7:t})
   if ns is None:continue
   eng=SubsetEngine(22,4,ns);r=eng.verify(eng.solve());r.update(neighbor_degrees=ds,center_partition=partition,triple=t,strict=r['bound']<1);r.pop('rows',None);local.append(r)
 records.extend(local);print('unitstar',ds,'strict',sum(r['strict'] for r in local),'/',len(local),'max',max(str(r['bound']) for r in local),'cpu',time.process_time()-start,flush=True)
 if time.process_time()-start>50:break
(HERE/'UNIT_STAR_THREE.json').write_text(json.dumps(json_value(dict(cases=records,cpu_seconds=time.process_time()-start)),indent=2)+'\n')
