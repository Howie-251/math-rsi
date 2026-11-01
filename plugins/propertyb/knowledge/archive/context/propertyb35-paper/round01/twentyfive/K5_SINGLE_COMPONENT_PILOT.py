"""Small seven-lock profile for one real K5 component, no external groups.
Each chosen trace is sampled at its minimum and maximum feasible codegree.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent;root=P.parents[3];sys.dont_write_bytecode=True
sys.path[:0]=[str(root/'context/propertyb34/round01/high-math'),str(root/'computations'),str(root/'computations/propertyb33/round01')]
from subset_position_dp import SubsetEngine
from multilock import json_value
src=json.loads((P/'K5_SINGLE_COMPONENT_DOMAIN.json').read_text());st=time.perf_counter();out=[]
for f in src['results']:
 zs=f['cases'];chosen=[]
 for z in [min(zs,key=lambda z:z['codegree']),max(zs,key=lambda z:z['codegree'])]:
  if z not in chosen:chosen.append(z)
 for zz in chosen:
  tm=time.perf_counter();ns={int(t):c for t,c in zz['counts'].items()};eng=SubsetEngine(25,7,ns);w=eng.verify(eng.solve());out.append(dict(id=f['id'],T=zz['T'],P=zz['P'],Q=zz['Q'],joint=zz['joint'],codegree=zz['codegree'],seconds=time.perf_counter()-tm,**w));print(f['id'],zz['T'],zz['codegree'],w['bound'],out[-1]['seconds'],flush=True)
summary=dict(scope=__doc__,cases=len(out),strict=sum(z['bound']<1 for z in out),elapsed_seconds=time.perf_counter()-st)
(P/'K5_SINGLE_COMPONENT_PILOT.json').write_text(json.dumps(json_value(dict(summary=summary,results=out)),indent=2)+'\n');print(json.dumps(summary,indent=2))
