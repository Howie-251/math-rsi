"""Third unit degree-seven extension; simultaneous two-high projection constraints."""
from pathlib import Path
from itertools import permutations
from fractions import Fraction
import sys,json,time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent
sys.path[:0]=[str(HERE),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from six_low_extension import extensions
from multilock import json_value
PP=list(permutations(range(6)))

def canonical8(ns):
 best=None
 for p in PP:
  for swap in (False,True):
   def tr(t):
    h=(((t&64)<<1)|((t&128)>>1)) if swap else (t&192)
    return h|sum(1<<p[i] for i in range(6) if t&(1<<i))
   key=tuple(sorted((tr(t),n) for t,n in ns.items() if n))
   if best is None or key<best:best=key
 return best

def remove_high(ns,i):
 out={}
 for t,n in ns.items():
  u=(t&((1<<i)-1))|((t>>(i+1))<<i);out[u]=out.get(u,0)+n
 return out

if __name__=='__main__':
 source=json.loads((HERE/'SIX_TWO_HIGH_JOINT.json').read_text())['results'];bad=[x for x in source if Fraction(x['bound'])>=1]
 keys={canonical8({int(t):n for t,n in x['counts'].items()}):x for x in bad}
 out=[];start=time.perf_counter()
 for bid,(key,x) in enumerate(keys.items()):
  ns={int(t):n for t,n in x['counts'].items()};cases=[];covered=0;total=0
  for j,nc in enumerate(extensions(ns,8,7)):
   total+=1
   if any(canonical8(remove_high(nc,i)) not in keys for i in (6,7)):
    covered+=1;continue
   eng=SubsetEngine(24,9,nc);z=eng.verify(eng.solve());z['id']=j;cases.append(z)
  out.append(dict(base=bid,source_graph=x['graph'],source_group=x['group'],counts=ns,complete_extensions=total,covered_by_other_projection=covered,cases=cases))
  print(bid,'total',total,'covered',covered,'remaining',len(cases),'strict',sum(z['bound']<1 for z in cases),'sec',time.perf_counter()-start,flush=True)
  (HERE/'SIX_LOW_THREE_HIGH.json').write_text(json.dumps(json_value(dict(scope=__doc__,base_orbits=len(keys),elapsed=time.perf_counter()-start,complete=len(out)==len(keys),results=out)),indent=2)+'\n')
