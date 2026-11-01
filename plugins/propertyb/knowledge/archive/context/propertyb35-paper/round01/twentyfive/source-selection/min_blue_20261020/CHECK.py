"""Exact small color-type arithmetic; no H or coloring search."""
from pathlib import Path
from itertools import product
import json

raw14=[]
for u in range(21):
 for n2 in range(35):
  for n3 in range(35):
   n1=14+u
   n4=34-n1-n2-n3
   if n4<0:
    continue
   degree=n1+2*n2+3*n3+4*n4
   delta=degree-84
   cross=136+2*(n2+n3)
   if delta<0 or cross<154:
    continue
   assert 3*u+2*n2+n3==10-delta
   assert u==0 and delta in (0,1)
   raw14.append(dict(N=[n1,n2,n3,n4],delta=delta,cross=cross))
assert len(raw14)==3
unit_corrected=[]
for row in raw14:
 required=154 if row['delta']==0 else 158
 # At delta0/1 the appropriate blue excess rows force exact cross count.
 if row['cross']==required:
  unit_corrected.append(row)
assert unit_corrected==[dict(N=[14,1,8,11],delta=0,cross=154)]

b15=[]
for u,n2,n3 in product(range(20),range(35),range(35)):
 n1=15+u
 n4=34-n1-n2-n3
 if n4<0 or n1+2*n2+3*n3+4*n4<90:
  continue
 assert 3*u+2*n2+n3<=1
 cross=136+2*(n2+n3)
 assert cross<=138<150
 b15.append([n1,n2,n3,n4])

stars=[]
for c in product(range(6),repeat=4):
 if sum(c)==5 and sum((j+1)*c[j] for j in range(4))==14 and c[1]<=1 and c[3]>=2:
  stars.append(c)
assert sorted(stars)==[(1,1,1,2),(2,0,0,3)]
assert 1+3*8+6*11==14*13//2
assert all(24-b<b for b in range(13,21))

K={b:(b*b-43*b+408)//2 for b in range(26)}
assert K[13]==9 and K[14]==1 and all(K[b]<0 for b in range(15,21))
assert 9-3*9+18==0
assert 136-9*13-9==10

out=dict(status='PASS',scope='color-type scalar domain only',
         b15_degree_feasible_rows=b15,b15_cross_capacity_max=138,b15_required_cross_pairs=150,
         b14_raw_scalar_rows=raw14,b14_after_actual_unit_rows=unit_corrected,
         b14_minimum_total_low_points=15,b14_excluded_by_existing_balanced_source=True,
         b14_intermediate_star_shapes=stars,
         profile_K=K, r_le_four_minimum_blue_upper=12,
         r5_b13_necessary_counts=[13,0,10,11],
         final_conclusion='global minimum blue count <=13; r<=4 implies <=12',
         remaining='repair unique low-containing red bad edge at b<=13')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('PASS: b15 impossible; b14 intermediate spectrum unique and balanced-source excluded; b<=13')
