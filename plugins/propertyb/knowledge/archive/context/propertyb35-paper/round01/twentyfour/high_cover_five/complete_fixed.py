"""Complete all81 actual degree-preserving high-cover orbits, reuse16 fixed pilots."""
from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
HERE=Path(__file__).parent;ROOT=HERE.parents[4];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from multilock import json_value
st=time.time();rs=json.loads((HERE/'DOMAIN.json').read_text())['orbits'];cache={r['id']:r for r in json.loads((HERE/'PILOT.json').read_text())['cases']};out=[]
for r in rs:
 if r['id'] in cache:z=cache[r['id']];z['bound']=Q(z['bound'])
 else:en=SubsetEngine(24,5,r['counts']);z=en.verify(en.solve());z.update(r);z['strict']=z['bound']<1
 # Raw ABC at exactly these positions is a separate, valid (weaker) bound.
 z['raw_ABC_bound']=sum(min(Q(row['A']),Q(row['B']),Q(row['C'])) for row in z['rows']);out.append(z)
(HERE/'FIXED.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,pilot_reused=len(cache),cases=out,fixed_strict=sum(r['strict'] for r in out),raw_ABC_strict=sum(r['raw_ABC_bound']<1 for r in out),max_bound=max(r['bound'] for r in out),max_raw_ABC_bound=max(r['raw_ABC_bound'] for r in out),elapsed_seconds=time.time()-st)),indent=2)+'\n');print('fixed',sum(r['strict'] for r in out),'of',len(out),'max',max(r['bound'] for r in out),'rawABCstrict',sum(r['raw_ABC_bound']<1 for r in out),'rawmax',max(r['raw_ABC_bound'] for r in out),'seconds',time.time()-st)
