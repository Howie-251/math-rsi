"""Complete bounded 135-case seven-lock domains for one real K5 component.
The full-G inventory23 has no three-point trace; its selected two-point domain
is retained even when non-strict. No complete H or eight-lock domain is searched.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent;root=P.parents[3];sys.dont_write_bytecode=True
sys.path[:0]=[str(root/'context/propertyb34/round01/high-math'),str(root/'computations'),str(root/'computations/propertyb33/round01')]
from subset_position_dp import SubsetEngine
from multilock import json_value
src=json.loads((P/'K5_SINGLE_COMPONENT_DOMAIN.json').read_text());pilot=json.loads((P/'K5_SINGLE_COMPONENT_PILOT.json').read_text());st=time.perf_counter();out=[];families=[]
def key(z):return z['id'],z['T'],tuple(z['P']),tuple(z['Q']),tuple(sorted((int(t),c) for t,c in z['joint'].items()))
cache={key(z):z for z in pilot['results']}
for f in src['results']:
 for zz in f['cases']:
  ns={int(t):c for t,c in zz['counts'].items()};eng=SubsetEngine(25,7,ns)
  if key(zz) in cache:z=dict(bound=Q(cache[key(zz)]['bound']),positions=cache[key(zz)]['positions'],counts=ns)
  else:z=eng.solve()
  w=eng.verify(z);out.append(dict(id=f['id'],T=zz['T'],P=zz['P'],Q=zz['Q'],joint=zz['joint'],codegree=zz['codegree'],**w))
 zz=[z for z in out if z['id']==f['id']];families.append(dict(id=f['id'],T=f['chosen_T'],cases=len(zz),strict=sum(z['bound']<1 for z in zz),maximum=max(z['bound'] for z in zz)));print(f['id'],len(zz),families[-1]['strict'],families[-1]['maximum'],flush=True)
summary=dict(scope=__doc__,cases=len(out),strict=sum(z['bound']<1 for z in out),elapsed_seconds=time.perf_counter()-st)
(P/'K5_SINGLE_COMPONENT_COMPLETE.json').write_text(json.dumps(json_value(dict(summary=summary,families=families,results=out)),indent=2)+'\n');print(json.dumps(summary,indent=2))
