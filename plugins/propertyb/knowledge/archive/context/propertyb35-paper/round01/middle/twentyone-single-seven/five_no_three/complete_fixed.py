"""Complete330 fixed certificates, reusing18 pilots; no new joint search in this pass."""
from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
HERE=Path(__file__).parent;ROOT=HERE.parents[5];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from multilock import json_value
st=time.time();dom=json.loads((HERE/'DOMAIN.json').read_text());cache={r['id']:r for r in json.loads((HERE/'PILOT.json').read_text())['cases']};out=[]
for r in dom['orbits']:
 if r['id'] in cache:z=cache[r['id']];z['bound']=Q(z['bound'])
 else:en=SubsetEngine(21,6,r['counts']);z=en.verify(en.solve());z.update(r);z['strict']=z['bound']<1
 out.append(z)
(HERE/'DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,pilot_reused=len(cache),cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');res=[r for r in out if not r['strict']];(HERE/'REMAINDERS.json').write_text(json.dumps(json_value(dict(count=len(res),cases=res)),indent=2)+'\n');print('fixed',sum(r['strict'] for r in out),'res',len(res),'seconds',time.time()-st)
