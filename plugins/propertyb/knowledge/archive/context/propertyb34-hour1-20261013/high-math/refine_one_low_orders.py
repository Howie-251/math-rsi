from pathlib import Path
from fractions import Fraction
from itertools import permutations
import sys,json,time
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).parent))
from fast_position_dp import Engine
from mixed_six import trans
from multilock import json_value,Profile,rows,total_bound
from pure_quota import certificate
from independent_structure_bounds import independent_rows
start=time.perf_counter();eng=Engine(24,6);print('init',time.perf_counter()-start,flush=True);out=[]
src=json.loads(Path(__file__).with_name('MIXED_SIX_v24_low1_bad6.json').read_text())
for x in src['results']:
 if Fraction(x['bound'])<1:continue
 ns={int(t):n for t,n in x['counts'].items()};seen=set();best=None
 for perm in permutations(range(6)):
  counts={trans(t,perm):n for t,n in ns.items()};key=tuple(sorted(counts.items()))
  if key in seen:continue
  seen.add(key);z=eng.solve(counts)
  if best is None or z['bound']<best['bound']:best=dict(relabeling=perm,counts=counts,**z)
  if z['bound']<1:break
 pos=best['positions'];p=Profile(24,5,pos,best['counts']);cs=[certificate(p,i) for i in range(6)];rs=rows(p,deductions={pos[i]:cs[i]['loss'] for i in range(6)});assert total_bound(rs)==best['bound']
 stubs=[frozenset(i+1 for i in range(6) if t&(1<<i)) for t,n in p.counts.items() for _ in range(n)];ir=independent_rows(24,pos,stubs);assert all(all(a[k]==b[k] for k in ('A','B','C')) for a,b in zip(rs,ir))
 out.append(dict(group=x['group'],orders=len(seen),old_bound=x['bound'],certificates=cs,rows=rs,independent_ABC=True,**best));print(x['group'],best['bound'],best['positions'],len(seen),'sec',time.perf_counter()-start,flush=True)
 Path(__file__).with_name('ONE_LOW_ALL_ORDERS.json').write_text(json.dumps(json_value(dict(elapsed=time.perf_counter()-start,results=out)),indent=2)+'\n')
