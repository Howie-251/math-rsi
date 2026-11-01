"""One raw fixed-layout witness for every436 feasible one-six/eight-unit input.
Nine new layouts are transported only by color-preserving canonical maps.
No new trace family, degree marking, or ninth lock is added.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent;root=P.parents[3];sys.path[:0]=[str(root/'context/propertyb34/round01/high-math'),str(root/'computations')];sys.dont_write_bytecode=True
from unit_catalogue import canonical
from bare_layout import BareLayout
from multilock import json_value
st=time.perf_counter();screen=json.loads((P/'MIXED_ONE_SIX_UNIT8_SCREEN.json').read_text());pilot=json.loads((P/'MIXED_ONE_SIX_UNIT8_PILOT.json').read_text());assert screen['summary']['screen_complete'];cache={}
for z in pilot['results']:
 ns={int(t):n for t,n in z['counts'].items()};large=[t for t in ns if t.bit_count()>=3];key,m=canonical(large,8,extra=[int(i==z['low']) for i in range(8)],with_perm=True);cp=[0]*8
 for i,j in enumerate(m):cp[j]=z['positions'][i]
 cache[(key,m[z['low']])]=(cp,Q(z['raw_ABC_bound']))
results=[]
for z in screen['results']:
 ns={int(t):n for t,n in z['counts'].items()}
 if Q(z['bound'])<1:pos=z['positions'];source='consecutive_then_low_mark_transport'
 else:
  large=[t for t in ns if t.bit_count()>=3];key,m=canonical(large,8,extra=[int(i==z['low']) for i in range(8)],with_perm=True);cp,expected=cache[(key,m[z['low']])];pos=[cp[m[i]] for i in range(8)];assert BareLayout(25,pos).bound(ns)==expected;source='nine_residual_orbit_layouts'
 bound=BareLayout(25,pos).bound(ns);assert bound<1;results.append(dict(base=z['base'],low=z['low'],counts=ns,positions=pos,raw_ABC_bound=bound,source=source))
summary=dict(scope=__doc__,complete=True,cases=len(results),all_raw_strict=True,maximum_raw=max(z['raw_ABC_bound'] for z in results),elapsed_seconds=time.perf_counter()-st)
(P/'MIXED_ONE_SIX_UNIT8_CERTIFICATE.json').write_text(json.dumps(json_value(dict(summary=summary,results=results)),indent=2)+'\n');print(json.dumps(json_value(summary),indent=2))
