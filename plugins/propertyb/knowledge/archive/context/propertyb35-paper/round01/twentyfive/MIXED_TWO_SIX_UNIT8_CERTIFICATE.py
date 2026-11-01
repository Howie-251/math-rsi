"""Concrete raw layout for every1566 feasible two-low eight-unit input.
Transport preserves the unordered pair of degree-six labels exactly.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent;root=P.parents[3];sys.dont_write_bytecode=True;sys.path[:0]=[str(root/'context/propertyb34/round01/high-math'),str(root/'computations')]
from unit_catalogue import canonical
from bare_layout import BareLayout
from multilock import json_value
st=time.perf_counter();screen=json.loads((P/'MIXED_TWO_SIX_UNIT8_SCREEN.json').read_text());pilot=json.loads((P/'MIXED_TWO_SIX_UNIT8_PILOT.json').read_text());cache={}
for z in pilot['results']:
 ns={int(t):n for t,n in z['counts'].items()};large=[t for t in ns if t.bit_count()>=3];key,m=canonical(large,8,extra=[int(i in z['low']) for i in range(8)],with_perm=True);lowmask=sum(1<<m[i] for i in z['low']);cp=[0]*8
 for i,j in enumerate(m):cp[j]=z['positions'][i]
 cache[(key,lowmask)]=(cp,Q(z['raw_ABC_bound']))
results=[]
for z in screen['results']:
 ns={int(t):n for t,n in z['counts'].items()}
 if Q(z['raw_ABC_bound'])<1:pos=z['positions'];source='fixed_screen_then_low_set_transport'
 else:
  key,m=canonical([t for t in ns if t.bit_count()>=3],8,extra=[int(i in z['low']) for i in range(8)],with_perm=True);cp,expected=cache[(key,sum(1<<m[i] for i in z['low']))];pos=[cp[m[i]] for i in range(8)];assert BareLayout(25,pos).bound(ns)==expected;source='35_residual_colored_orbit_layouts'
 bound=BareLayout(25,pos).bound(ns);assert bound<1;results.append(dict(base=z['base'],low=z['low'],counts=ns,positions=pos,raw_ABC_bound=bound,source=source))
summary=dict(scope=__doc__,complete=True,cases=len(results),all_raw_strict=True,maximum_raw=max(z['raw_ABC_bound'] for z in results),elapsed_seconds=time.perf_counter()-st)
(P/'MIXED_TWO_SIX_UNIT8_CERTIFICATE.json').write_text(json.dumps(json_value(dict(summary=summary,results=results)),indent=2)+'\n');print(json.dumps(json_value(summary),indent=2))
