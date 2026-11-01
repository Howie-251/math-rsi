"""Only finite integer degree/color budgets from the accompanying proofs.
No H, negative-layout, source-edge, or coloring enumeration.
"""
from pathlib import Path
import json
P=Path(__file__).resolve().parent
# Continuous consequence of the exact private-edge packing rows.
packing={M:{b:b*b-64*b+652+4*(5*M-168) for b in range(4,20)} for M in (34,35)}
assert all(packing[35][b]<0 for b in range(14,20))
assert all(packing[34][b]<0 for b in range(13,20))
patterns=[]
for e in (0,1):
 for z in range(8):
  for a in range(8):
   for c in range(8):
    if 3*z+2*a+c!=6-e or a+c<4:continue
    assert z==0
    patterns.append({'blue_excess':e,'N1':13,'N2':a,'N3':c,'N4':21-a-c,'cross_pair_surplus':5-2*e-2*a})
assert len(patterns)==5
# Bound c_p from the other five red-exterior points and all five G rows.
bounds=[]
for e in (0,1):
 for t in range(2,8-e):
  low=12-(4*(7-e-t))//3
  if (e==0 and t>=6):assert low>=11 and 7+t-low<=2
  if (e==1 and t>=4):assert low>=10 and 7+t-low<=1
  bounds.append({'blue_excess':e,'red_point_excess':t,'minimum_private_count':low,'nonprivate_edges_at_most':7+t-low})
assert next(r for r in bounds if r['blue_excess']==0 and r['red_point_excess']==5)['minimum_private_count']==10

def partitions(total,length,maximum):
 if length==0:
  if total==0:yield ()
  return
 for x in range(min(total,maximum),-1,-1):
  for rest in partitions(total-x,length-1,x):yield (x,)+rest
partitions_by_e={}
for e in (0,1):
 out=[]
 for T in partitions(7-e,6,4-e):
  caps=[5+t+t//3 for t in T]
  if 15+sum(caps)<52:continue
  out.append({'red_excess_partition':T,'red_private_capacity':sum(caps),'minimum_G_private_incidence':52-sum(caps)})
 partitions_by_e[e]=out
assert [tuple(r['red_excess_partition']) for r in partitions_by_e[1]]==[(3,3,0,0,0,0),(3,2,1,0,0,0),(3,1,1,1,0,0)]
out={'status':'PASS_SCALARS_ONLY','packing_polynomial':packing,'b13_color_patterns':patterns,'red_point_private_lower_bounds':bounds,'remaining_b13_red_excess_partitions':partitions_by_e,'scope':__doc__}
(P/'SCALARS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('packing_polynomial','red_point_private_lower_bounds')},indent=2))
