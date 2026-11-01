"""Complete q=5 catalogue: cheap exact bare layouts first, subset DP only on residues."""
from pathlib import Path
from fractions import Fraction
import sys,json,time
sys.dont_write_bytecode=True
HERE=Path(__file__).parent;sys.path.insert(0,str(HERE))
from bare_layout import BareLayout
from subset_position_dp import SubsetEngine
from independent_structure_bounds import independent_rows
from multilock import json_value

if __name__=='__main__':
 budget=float(sys.argv[1]) if len(sys.argv)>1 else 300
 src=json.loads((HERE/'V25_NINE_Q5_CATALOGUE.json').read_text())['results'];layouts=[BareLayout(25,tuple(range(a,a+9))) for a in (9,8,10,11,17)]
 out=[];start=time.perf_counter();dp=0
 for x in src:
  ns={int(t):n for t,n in x['counts'].items()};z=None
  for e in layouts:
   b=e.bound(ns)
   if b>=1:continue
   stubs=[frozenset(i+1 for i in range(9) if t&(1<<i)) for t,c in ns.items() for _ in range(c)]
   rr=independent_rows(25,e.pos,stubs);b2,own=e.bound(ns,True)
   assert b==b2==sum((r['bound'] for r in rr),Fraction())
   assert own==[(r['A'],r['B'],r['C']) for r in rr]
   z=dict(bound=b,positions=e.pos,counts=ns,method='bare',independent_ABC=True);break
  if z is None:
   dp+=1;e=SubsetEngine(25,9,ns);z=e.verify(e.solve());z['method']='full_subset_dp'
   if z['bound']<1:z.pop('rows');z.pop('certificates')
  z.update(id=x['id'],large_blocks=x['large_blocks']);out.append(z)
  if len(out)%500==0:print(len(out),'strict',sum(z['bound']<1 for z in out),'DP',dp,'elapsed',time.perf_counter()-start,flush=True)
  if len(out)%500==0 or len(out)==len(src) or time.perf_counter()-start>budget:
   (HERE/'V25_NINE_Q5_BOUNDS.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(src),catalogue_size=len(src),elapsed=time.perf_counter()-start,dp_calls=dp,results=out)),indent=2)+'\n')
  if time.perf_counter()-start>budget:print('BUDGET_STOP',flush=True);break
