#!/usr/bin/env python3
"""Independent scalar arithmetic only; no H or signed-layout generation."""
from fractions import Fraction
from math import comb
from pathlib import Path
import json

rows = []
def bound(R, W):
    return (174 - R * (24 - R) + W) // 2
assert bound(12, 0) == 15
assert bound(8, 0) == 23 < 24
rows.append(dict(case='two_four',R=8,private_lower=24,E_upper=23))
for u, expected in ((1,21),(2,19),(3,17)):
    R=8+u
    got=bound(R,u*(4-u))
    assert got == expected
    protected=23 if u==1 else 20
    assert protected > got
    rows.append(dict(case='two_three',u=u,R=R,private_lower=protected,E_upper=got))
for u,v,expected,protected in ((1,1,20,22),(1,2,19,21)):
    R=8+u+v
    got=bound(R,u*(4-u)+v*(4-v))
    assert got==expected and protected>got
    rows.append(dict(case='two_two_imbalanced',u=u,v=v,R=R,private_lower=protected,E_upper=got))
assert bound(12,6)==18 and 3*3 > (18-16)*3
assert bound(12,8)==19
surplus=[dict(E=e,delta=174-2*e-(144-8)) for e in range(16,20)]
assert [x['delta'] for x in surplus]==[6,4,2,0]
p=Fraction(comb(12,5)+comb(13,5),comb(25,5))
assert p==Fraction(9,230)
assert 35*p==Fraction(63,46)
assert 70-2/p==Fraction(170,9)
assert 19*p-2*(35*p-1)==Fraction(1,230)
assert Fraction(comb(25,12),230) == 22610
# Separate globally minimum-blue unique-low-source experiment: only scalar equations.
rigid=set()
for r in (3,4,5):
  for rB in range(r): # at least one six lies on the red source
    for eB in range(r+1):
      for z in range(4):
        for n2 in range(6):
          for n3 in range(12):
            if 3*z+2*n2+n3==6+rB-eB and n2+n3>=10:
              rigid.add((r,rB,eB,z,n2,n3))
assert rigid=={(5,4,0,0,0,10)}
out=dict(status='PASS',scope='scalar identities and inequalities only',normal_form_rows=rows,
         balanced_surplus=surplus,balanced_single_edge_probability=str(p),
         unique_low_probability_lower_at_L19=str(19*p-2*(35*p-1)),
         unique_low_count_lower_at_L19=22610,
         unique_low_source_b13_rigid=sorted(rigid))
path=Path(__file__).with_name('NORMAL_FORM_SCALARS.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
