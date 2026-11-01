"""Local scalar and swap truth-table check; no hypergraph/coloring search."""
from pathlib import Path
from itertools import product
import json

swap_rows=[]
for j,has_h,has_y in product(range(1,5),(0,1),(0,1)):
 if has_h>5-j or has_y>j:
  continue
 # h has no N4 private; y's only N1 private contains both h and y.
 if j==4 and has_h:
  continue
 if j==1 and has_y and not has_h:
  continue
 after=j+has_h-has_y
 assert 1<=after<=4
 swap_rows.append(dict(old_blue_count=j,contains_h=has_h,contains_y=has_y,
                       new_blue_count=after))

# No N2 exists in the new general color-profile argument.
for row in swap_rows:
 if row['old_blue_count'] in (3,4):
  assert row['new_blue_count']>=2

general_h=[]
for a,c in product(range(14),range(5)):
 if a+3*c==13 and a+c>=6:
  assert (a+c)%2==1 and a+c>=7 and a>=4
  assert 13-(a-1)<=10<13
  general_h.append(dict(a=a,c=c,degree=a+c,new_N1=14-a))

local_h=[]
for n1,n3 in product(range(14),range(5)):
 if n1+3*n3!=13:
  continue
 assert n1>0
 degree=n1+n3
 if 7<=degree<=12:
  local_h.append(dict(n1=n1,n3=n3,degree=degree))
assert [row['degree'] for row in local_h]==[7,9,11]

cuts=[]
for h,y in product((7,9,11),(6,7)):
 new_cut=4*(h-6)+4*(y-6)
 assert new_cut>=4
 cuts.append(dict(h_degree=h,y_degree=y,new_cut_excess=new_cut))

assert 13+10+11==34 and 4*(13+11)+6*10==13*12
out=dict(status='PASS',scope='swap truth table and local scalar rows only',
         swap_rows=swap_rows,possible_local_h_rows=local_h,new_cut_rows=cuts,
         general_profile_h_rows=general_h,
         general_profile_exclusion='any global minblue13 source has N!=(13,0,10,11)',
         minimum_positive_new_cut_excess=min(row['new_cut_excess'] for row in cuts),
         conclusion='r5 global minimum blue count <=12',
         not_a_coloring_proof_for_H=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('PASS:',len(swap_rows),'proper-edge swap rows;',len(local_h),'local h rows; new cut >=4')
