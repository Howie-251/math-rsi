"""All 144 q2 affine residues: exact arbitrary-layout DP and independent witness replay."""
from pathlib import Path
import sys,json,time
P=Path(__file__).resolve().parent;R=P.parents[3];S=R/'context/propertyb34/round01/high-math'
sys.dont_write_bytecode=True
sys.path[:0]=[str(S),str(R/'computations'),str(R/'computations/propertyb33/round01')]
from subset_position_dp import SubsetEngine
from multilock import json_value
from fractions import Fraction as Q
src=json.loads((P/'UNIT9_MIXED_AFFINE.json').read_text());st=time.perf_counter();out=[]
previous=json.loads((P/'UNIT9_MIXED_Q2_PILOT.json').read_text())['cases']
cache={(z['base'],z['low_mask']):z for z in previous}
for f in src['families']:
 if not f['feasible']:continue
 for c in f['cases']:
  if c['q']!=2:continue
  for mask in c.get('residual_colors',[]):
   ns={**{int(t):1 for t in f['full']},**{1<<i:a-int(bool(mask>>i&1)) for i,a in enumerate(f['single_high']) if a-int(bool(mask>>i&1))},0:c['empty']}
   start=time.perf_counter()
   if (f['base'],mask) in cache:
    out.append(cache[f['base'],mask]);continue
   eng=SubsetEngine(25,9,ns);z=eng.solve();z=eng.verify(z)
   out.append(dict(base=f['base'],low_mask=mask,dp_seconds=time.perf_counter()-start,**z))
   if len(out)%20==0:print('processed',len(out),'elapsed',time.perf_counter()-st,flush=True)
res=dict(scope=__doc__,complete_q2=len(out)==144,strict=sum(Q(z['bound'])<1 for z in out),residual=sum(Q(z['bound'])>=1 for z in out),maximum=max(Q(z['bound']) for z in out),cases=out,elapsed_seconds=time.perf_counter()-st)
(P/'UNIT9_MIXED_Q2_COMPLETE.json').write_text(json.dumps(json_value(res),indent=2)+'\n')
print(json.dumps(json_value({k:v for k,v in res.items() if k!='cases'}),indent=2))
