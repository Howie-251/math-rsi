"""Six nontrivial eight-lock pilots (111,211-empty,211-nonempty per type).
The entire local domain is precomputed; this script does not enumerate H.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent;root=P.parents[3];sys.dont_write_bytecode=True
sys.path[:0]=[str(root/'context/propertyb34/round01/high-math'),str(root/'computations'),str(root/'computations/propertyb33/round01')]
from subset_position_dp import SubsetEngine
from multilock import json_value
st=time.perf_counter();domain=json.loads((P/'GROUP5_THREE_EXTERNAL_STARS_DOMAIN.json').read_text());out=[]
for f in domain['results']:
 T=min(f['by_trace'],key=lambda z:(z['total'],z['T']))['T'];zs=[z for z in f['cases'] if z['T']==T]
 for label,predicate in [('111',lambda z:z['mode']=='111'),('211-empty',lambda z:z['mode']=='211' and z['U']==0),('211-nonempty',lambda z:z['mode']=='211' and z['U']!=0)]:
  zz=next(z for z in zs if predicate(z));ns={int(t):c for t,c in zz['counts'].items()};t0=time.perf_counter();eng=SubsetEngine(25,8,ns);w=eng.verify(eng.solve());out.append(dict(pilot_class=label,id=zz['id'],T=T,mode=zz['mode'],partitions=zz['partitions'],U=zz['U'],seconds=time.perf_counter()-t0,**w));print(zz['id'],label,w['bound'],out[-1]['seconds'],flush=True)
summary=dict(scope=__doc__,cases=len(out),strict=sum(z['bound']<1 for z in out),elapsed_seconds=time.perf_counter()-st)
(P/'GROUP5_THREE_EXTERNAL_STARS_PILOT.json').write_text(json.dumps(json_value(dict(summary=summary,results=out)),indent=2)+'\n');print(json.dumps(summary,indent=2))
