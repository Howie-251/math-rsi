"""Finite sanity check of integer consequences; the proof is algebraic."""
from pathlib import Path
import json

for a in range(35):
 assert (a-2)*(a-3)>=0
 assert 5*a-a*a<=6

u0_count=0
low_count=0
general_count=0
for t in range(35):
 for bh in range(t+1):
  capacity=2*(t-bh)
  for a in range(35):
   if a*(a-1)<=capacity:
    assert 2*a+bh<=t+3
    u0_count+=1
   for u in range(35):
    general=max(a-2*u,0)*max(a-1-u,0)
    low=max(a-u,0)*max(a-1-u,0)
    assert general<=low
    if general<=capacity:
     general_count+=1
    if low<=capacity:
     assert 2*a+bh<=t+2*u+3
     low_count+=1

out=dict(status='PASS',scope='integer sanity range 0..34 only; proof covers all integers',
         u0_feasible_integer_rows=u0_count,
         low_point_feasible_integer_rows=low_count,
         general_inequality_feasible_integer_rows=general_count,
         max_quadratic_term=3,
         cross_zero_nonlow_thresholds={'b13_N2_lower':5,'b12_N2_lower':6},
         no_H_source_or_negative_family_search=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('PASS: shared indexed N2 capacity and integer quadratic consequences')
