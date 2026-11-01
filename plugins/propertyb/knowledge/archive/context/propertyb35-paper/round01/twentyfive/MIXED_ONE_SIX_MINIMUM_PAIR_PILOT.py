"""At most two residual examples per root; no per-input large DP sweep.
The exact worst old-layout residual and one first residual are profiled.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent;root=P.parents[3];sys.dont_write_bytecode=True;sys.path[:0]=[str(root/'context/propertyb34/round01/high-math'),str(root/'computations'),str(root/'computations/propertyb33/round01')]
from subset_position_dp import SubsetEngine
from multilock import json_value
st=time.perf_counter();dom=json.loads((P/'MIXED_ONE_SIX_MINIMUM_PAIRS.json').read_text());scr=json.loads((P/'MIXED_ONE_SIX_MINIMUM_PAIR_SCREEN.json').read_text());records=[]
for f in dom['results']:
 s=next(z for z in scr['results'] if (z['base'],z['partner'])==(f['base'],f['partner']));rr=s['residual'];inds=sorted({rr[0]['case_index'],max(rr,key=lambda z:Q(z['minimum_raw']))['case_index']})
 for idx in inds:
  z=f['cases'][idx];ns={int(t):n for t,n in z['counts'].items()};tm=time.perf_counter();eng=SubsetEngine(25,9,ns);w=eng.verify(eng.solve());raw=sum(min(r['A'],r['B'],r['C']) for r in w['rows']);records.append(dict(base=f['base'],partner=f['partner'],case_index=idx,raw_ABC_bound=raw,seconds=time.perf_counter()-tm,**w));print(f['base'],f['partner'],idx,w['bound'],raw,flush=True)
out=dict(scope=__doc__,cases=len(records),strict=sum(z['bound']<1 for z in records),raw_strict=sum(z['raw_ABC_bound']<1 for z in records),results=records,elapsed_seconds=time.perf_counter()-st)
(P/'MIXED_ONE_SIX_MINIMUM_PAIR_PILOT.json').write_text(json.dumps(json_value(out),indent=2)+'\n');print('seconds',out['elapsed_seconds'])
