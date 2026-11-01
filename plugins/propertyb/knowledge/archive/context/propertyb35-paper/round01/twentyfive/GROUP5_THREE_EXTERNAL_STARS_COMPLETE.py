"""Complete selected-singleton eight-lock domain: 8+9=17 cases.
Six pilot layouts are reused and independently verified on their inputs.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent;root=P.parents[3];sys.dont_write_bytecode=True
sys.path[:0]=[str(root/'context/propertyb34/round01/high-math'),str(root/'computations'),str(root/'computations/propertyb33/round01')]
from subset_position_dp import SubsetEngine
from multilock import json_value
st=time.perf_counter();domain=json.loads((P/'GROUP5_THREE_EXTERNAL_STARS_DOMAIN.json').read_text());pilot=json.loads((P/'GROUP5_THREE_EXTERNAL_STARS_PILOT.json').read_text());out=[];families=[]
def key(z):return z['id'],z['T'],z['mode'],tuple(tuple(p) for p in z['partitions']),z['U']
cache={key(z):z for z in pilot['results']}
for f in domain['results']:
 T=min(f['by_trace'],key=lambda z:(z['total'],z['T']))['T'];zs=[z for z in f['cases'] if z['T']==T]
 for zz in zs:
  ns={int(t):c for t,c in zz['counts'].items()};eng=SubsetEngine(25,8,ns)
  if key(zz) in cache:z=dict(bound=Q(cache[key(zz)]['bound']),positions=cache[key(zz)]['positions'],counts=ns)
  else:z=eng.solve()
  w=eng.verify(z);out.append(dict(id=zz['id'],T=T,mode=zz['mode'],partitions=zz['partitions'],U=zz['U'],**w))
 ff=[z for z in out if z['id']==f['id']];families.append(dict(id=f['id'],T=T,cases=len(ff),strict=sum(z['bound']<1 for z in ff),maximum=max(z['bound'] for z in ff)))
summary=dict(scope=__doc__,cases=len(out),strict=sum(z['bound']<1 for z in out),elapsed_seconds=time.perf_counter()-st)
(P/'GROUP5_THREE_EXTERNAL_STARS_COMPLETE.json').write_text(json.dumps(json_value(dict(summary=summary,families=families,results=out)),indent=2)+'\n');print(json.dumps(json_value(dict(summary=summary,families=families)),indent=2))
