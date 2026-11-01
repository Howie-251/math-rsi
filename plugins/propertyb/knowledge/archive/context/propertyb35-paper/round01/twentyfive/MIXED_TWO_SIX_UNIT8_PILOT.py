"""Only35 residual low-set-preserving eight-lock orbits, no new point.
This tests a conditional eight-unit two-six gate, not existence of eight locks.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent;root=P.parents[3];sys.dont_write_bytecode=True
sys.path[:0]=[str(root/'context/propertyb34/round01/high-math'),str(root/'computations'),str(root/'computations/propertyb33/round01')]
from subset_position_dp import SubsetEngine
from multilock import json_value
src=json.loads((P/'MIXED_TWO_SIX_UNIT8_SCREEN.json').read_text());st=time.perf_counter();out=[]
for orb in src['residual_orbits']:
 z=next(z for z in src['results'] if z['base']==orb['base'] and z['low']==orb['low'] and z['canonical_large']==orb['canonical_large']);ns={int(t):n for t,n in z['counts'].items()};tm=time.perf_counter();eng=SubsetEngine(25,8,ns);w=eng.verify(eng.solve());raw=sum(min(r['A'],r['B'],r['C']) for r in w['rows']);out.append(dict(base=z['base'],low=z['low'],low_orbit=orb['low_labels'],canonical_large=orb['canonical_large'],canonical_lowmask=z['canonical_lowmask'],raw_ABC_bound=raw,seconds=time.perf_counter()-tm,**w));print(z['base'],z['low'],w['bound'],raw,flush=True)
summary=dict(scope=__doc__,cases=len(out),strict=sum(z['bound']<1 for z in out),raw_strict=sum(z['raw_ABC_bound']<1 for z in out),maximum=max(z['bound'] for z in out),elapsed_seconds=time.perf_counter()-st)
(P/'MIXED_TWO_SIX_UNIT8_PILOT.json').write_text(json.dumps(json_value(dict(summary=summary,results=out)),indent=2)+'\n');print(json.dumps(json_value(summary),indent=2))
