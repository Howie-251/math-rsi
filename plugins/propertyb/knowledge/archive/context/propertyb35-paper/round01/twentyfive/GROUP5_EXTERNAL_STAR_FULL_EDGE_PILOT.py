"""One additional full-group-edge inventory with a four-point proper trace.
It is the only full-G representative containing such a trace (id25).
"""
from pathlib import Path
from collections import Counter
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent;root=P.parents[3];sys.dont_write_bytecode=True
sys.path[:0]=[str(root/'context/propertyb34/round01/high-math'),str(root/'computations'),str(root/'computations/propertyb33/round01')]
from subset_position_dp import SubsetEngine
from multilock import json_value
st=time.perf_counter();d=json.loads((P/'GROUP5_CATALOGUE.json').read_text());mu={int(t):c for t,c in d['representatives'][25]['counts'].items()};part=[1,30]
ns=Counter(mu)
for t in part:ns[t]-=1;ns[t|32]+=1
ns[0]-=5;ns[32]+=5;ns={t:c for t,c in ns.items() if c};eng=SubsetEngine(25,6,ns);z=eng.verify(eng.solve())
raw=sum(min(r['A'],r['B'],r['C']) for r in z['rows'])
out=dict(scope=__doc__,id=25,partition=part,required_four_trace=30,no_quota_bound_at_same_layout=raw,elapsed_seconds=time.perf_counter()-st,**z)
(P/'GROUP5_EXTERNAL_STAR_FULL_EDGE_PILOT.json').write_text(json.dumps(json_value(out),indent=2)+'\n');print(z['bound'],raw,z['positions'],z['certificates'])
