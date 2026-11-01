"""Six nontrivial actual-group trace representatives, exact five-lock DP.
No extrapolation from tested representatives to the 27-orbit domain.
"""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,time
P=Path(__file__).resolve().parent;R=P.parents[3];S=R/'context/propertyb34/round01/high-math'
sys.dont_write_bytecode=True
sys.path[:0]=[str(S),str(R/'computations'),str(R/'computations/propertyb33/round01')]
from subset_position_dp import SubsetEngine
from multilock import json_value
st=time.perf_counter();src=json.loads((P/'GROUP5_CATALOGUE.json').read_text());ids=[0,7,14,18,23,25];out=[]
for i in ids:
 r=src['representatives'][i];ns={int(t):c for t,c in r['counts'].items()};start=time.perf_counter()
 eng=SubsetEngine(25,5,ns);z=eng.verify(eng.solve())
 out.append(dict(id=i,**z,elapsed_seconds=time.perf_counter()-start))
 print(i,z['bound'],float(z['bound']),time.perf_counter()-start,flush=True)
summary=dict(scope=__doc__,selected_ids=ids,catalogue_orbits=src['orbits'],tested=6,strict=sum(r['bound']<1 for r in out),minimum=min(r['bound'] for r in out),maximum=max(r['bound'] for r in out),elapsed_seconds=time.perf_counter()-st)
(P/'GROUP5_PILOT.json').write_text(json.dumps(json_value(dict(summary=summary,results=out)),indent=2)+'\n');print(json.dumps(json_value(summary),indent=2))
