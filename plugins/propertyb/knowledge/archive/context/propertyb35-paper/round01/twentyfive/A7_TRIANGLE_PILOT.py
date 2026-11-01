"""Fifteen bounded triangle-anomaly pilots, not an all7907 probability table.
For each rooted seven-core and codegree2/3/4, select one maximum-empty input.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent;root=P.parents[3];sys.dont_write_bytecode=True
sys.path[:0]=[str(root/'context/propertyb34/round01/high-math'),str(root/'computations'),str(root/'computations/propertyb33/round01')]
from subset_position_dp import SubsetEngine
from multilock import json_value
src=json.loads((P/'A7_TRIANGLE_DOMAIN.json').read_text());st=time.perf_counter();out=[]
for f in src['results']:
 for lam in [2,3,4]:
  zz=max((z for z in f['cases'] if z['codegree']==lam),key=lambda z:z['counts'].get('0',0));ns={int(t):c for t,c in zz['counts'].items()};tm=time.perf_counter();eng=SubsetEngine(25,9,ns);w=eng.verify(eng.solve());out.append(dict(base=f['base'],partner=f['partner'],codegree=lam,P=zz['P'],Q=zz['Q'],joint=zz['joint'],seconds=time.perf_counter()-tm,**w));print(f['base'],f['partner'],lam,w['bound'],out[-1]['seconds'],flush=True)
summary=dict(scope=__doc__,cases=len(out),strict=sum(z['bound']<1 for z in out),maximum=max(z['bound'] for z in out),elapsed_seconds=time.perf_counter()-st)
(P/'A7_TRIANGLE_PILOT.json').write_text(json.dumps(json_value(dict(summary=summary,results=out)),indent=2)+'\n');print(json.dumps(json_value(summary),indent=2))
