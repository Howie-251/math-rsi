"""Complete second unit-high extension for five lows with one internal exceptional pair."""
from pathlib import Path
from itertools import permutations
from fractions import Fraction
import sys,json,time
sys.dont_write_bytecode=True
HERE=Path(__file__).parent;sys.path.insert(0,str(HERE))
from six_low_extension import extensions
from subset_position_dp import SubsetEngine
from multilock import json_value

def canonical(ns,low=5):
 return min(tuple(sorted(((t&~((1<<low)-1))|sum(1<<p[i] for i in range(low) if t&(1<<i)),n) for t,n in ns.items())) for p in permutations(range(low)))

def drop_x(ns):
 out={}
 for t,n in ns.items():u=(t&31)|((t&64)>>1);out[u]=out.get(u,0)+n
 return out

if __name__=='__main__':
 source=json.loads((HERE/'MIXED_SIX_JOINT.json').read_text())['sources'];b=next(g for g in source if g['source']=='MIXED_SIX_v24_low5_bad3.json');bad=[x for x in b['results'] if Fraction(x['bound'])>=1];keys={canonical({int(t):n for t,n in x['counts'].items()}) for x in bad};start=time.perf_counter();out=[]
 for x in bad:
  ns={int(t):n for t,n in x['counts'].items()};total=covered=0;cases=[]
  for j,nc in enumerate(extensions(ns,6,7)):
   total+=1
   if canonical(drop_x(nc)) not in keys:covered+=1;continue
   e=SubsetEngine(24,7,nc);z=e.verify(e.solve());z['id']=j;cases.append(z)
  out.append(dict(group=x['group'],counts=ns,total=total,covered_by_other_projection=covered,cases=cases));print(x['group'],total,covered,len(cases),sum(z['bound']<1 for z in cases),time.perf_counter()-start,flush=True)
  (HERE/'FIVE_LOW_ONE_BAD_EXTENSION.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(bad),elapsed=time.perf_counter()-start,results=out)),indent=2)+'\n')
