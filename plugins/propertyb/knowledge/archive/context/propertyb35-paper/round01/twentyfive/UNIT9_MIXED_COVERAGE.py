"""Reconcile the q2 DP list with exactly the affine residual masks.
Evaluate saved affine models only; no repeated probability calculation.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter()
x=json.loads((P/'UNIT9_MIXED_AFFINE.json').read_text());d=json.loads((P/'UNIT9_MIXED_Q2_COMPLETE.json').read_text())
actual={(z['base'],z['low_mask']):z for z in d['cases']}
assert len(actual)==len(d['cases'])==144
expected={(f['base'],mask) for f in x['families'] if f['feasible'] for c in f['cases'] if c['q']==2 for mask in c.get('residual_colors',[])}
assert set(actual)==expected
count=0;maximum=Q();worst=None
for f in x['families']:
 if not f['feasible']:continue
 for c in f['cases']:
  if c['q']!=2:continue
  constants=[Q(a) for a in c['layout_constants']]
  for low in combinations(f['eligible'],2):
   mask=sum(1<<i for i in low);key=f['base'],mask
   if key in actual:
    z=actual[key];value=Q(z['bound'])
    ns={**{int(t):1 for t in f['full']},**{1<<i:a-int(i in low) for i,a in enumerate(f['single_high']) if a-int(i in low)},0:c['empty']}
    ns={str(t):a for t,a in ns.items() if a}
    assert ns==z['counts']
   else:
    value=min(a+sum(Q(lay['slopes'][i]) for i in low) for a,lay in zip(constants,f['layouts']))
   assert value<1
   if value>maximum:maximum=value;worst=dict(base=f['base'],low_mask=mask,value=str(value),method='DP' if key in actual else 'affine')
   count+=1
assert count==7663
out=dict(scope=__doc__,q2=dict(complete=True,feasible_colors=count,affine_colors=count-144,dp_colors=144,all_dp_inventory_bindings_equal=True,global_maximum=str(maximum),worst=worst),closed_q=[0,1,2],remaining_q={str(q):x['summary'][str(q)]['residual_colors'] for q in range(3,10)},elapsed_seconds=time.perf_counter()-st)
(P/'UNIT9_MIXED_COVERAGE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
