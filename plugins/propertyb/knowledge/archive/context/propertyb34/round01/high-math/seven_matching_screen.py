"""Bound the complete homogeneous-matching seven-lock domain, with replay."""
from pathlib import Path
from fractions import Fraction
from itertools import combinations
import sys,json,time
sys.dont_write_bytecode=True
HERE=Path(__file__).parent;sys.path.insert(0,str(HERE))
from bare_layout import BareLayout
from subset_position_dp import SubsetEngine
from independent_structure_bounds import independent_rows
from multilock import json_value

if __name__=='__main__':
 budget=float(sys.argv[1]) if len(sys.argv)>1 else 900
 src=json.loads((HERE/'SEVEN_HOMOGENEOUS_MATCHING.json').read_text())['profiles']
 poses=[tuple(range(a,a+7)) for a in (9,8,10,11,18)]
 poses += [(a,19,20,21,22,23,24) for a in (10,11,12)]
 poses += [(10,11,20,21,22,23,24),(11,20,12,21,22,23,24),(11,21,12,22,13,23,24)]
 layouts=[BareLayout(24,p) for p in poses];out=[];start=time.perf_counter();dp=0
 target=HERE/'SEVEN_HOMOGENEOUS_MATCHING_BOUNDS.json'
 if target.exists():
  saved=json.loads(target.read_text());out=[z for z in saved['results'] if z['low_count']<=3]
  for z in out:z['bound']=Fraction(z['bound'])
 done={z['group'] for z in out};required=sum(x['low_count']<=3 for x in src)
 old=json.loads((HERE/'SEVEN_MATCHING_QMAX0_BOUNDS.json').read_text())['results']
 old={tuple(sorted((int(t),n) for t,n in x['counts'].items())):x for x in old}
 for j,x in enumerate(src):
  if x['low_count']>3 or j in done:continue
  ns={int(t):n for t,n in x['counts'].items()};key=tuple(sorted(ns.items()));z=None
  if x['low_count']==0:
   a=old[key];z={k:v for k,v in a.items() if k not in ('rows','certificates','group')};z['bound']=Fraction(z['bound']);z['method']='q0_complete_replay'
  else:
   for e in layouts:
    b=e.bound(ns)
    if b>=1:continue
    stubs=[frozenset(i+1 for i in range(7) if t&(1<<i)) for t,c in ns.items() for _ in range(c)]
    rr=independent_rows(24,e.pos,stubs);b2,own=e.bound(ns,True)
    assert b==b2==sum((r['bound'] for r in rr),Fraction())
    assert own==[(r['A'],r['B'],r['C']) for r in rr]
    z=dict(bound=b,positions=e.pos,counts=ns,method='bare',independent_ABC=True);break
  if z is None:
   dp+=1;e=SubsetEngine(24,7,ns);z=e.verify(e.solve());z['method']='full_subset_dp'
   if z['bound']<1:z.pop('rows');z.pop('certificates')
  z.update(group=j,low_count=x['low_count'],matching_size=x['matching_size'],catalogue_id=x['catalogue_id']);out.append(z)
  if len(out)%500==0:print(len(out),'strict',sum(z['bound']<1 for z in out),'DP',dp,'elapsed',time.perf_counter()-start,flush=True)
  if len(out)%500==0 or len(out)==required or time.perf_counter()-start>budget:
   target.write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==required,low_count_limit=3,catalogue_size=required,elapsed=time.perf_counter()-start,dp_calls=dp,results=out)),indent=2)+'\n')
  if time.perf_counter()-start>budget:print('BUDGET_STOP',flush=True);break
