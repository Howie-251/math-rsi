"""Finite binomial/Bonferroni arithmetic and five sparse graph shapes, no set-family enumeration."""
from pathlib import Path
from itertools import combinations
from math import comb
from fractions import Fraction
import json,time
P=Path(__file__).resolve().parent;st=time.process_time()
def C(n,k):return comb(n,k) if 0<=k<=n else 0
D=C(17,10);single=C(13,6);blue=C(13,10)
assert (D,single,blue)==(19448,1716,286)
pair={j:C(9+j,2+j) for j in range(4)};assert list(pair.values())==[36,120,330,792]
triple={k:C(8+k,1+k) for k in range(4)};assert list(triple.values())==[8,36,120,330]
bare=8*single+24*blue;assert bare==20592 and bare-D==1144
# Forest branches: pairgraph rank>=4 follows fromsupport<=17 andsupport>=4percomponent.
forest3=pair[3]+3*pair[1]+3*pair[0]
forest2=3*pair[2]+pair[1]+3*pair[0]
assert (forest3,forest2)==(1260,1218)
shapes={'empty':[],'one_edge':[(0,1)],'two_matching':[(0,1),(2,3)],'two_wedge':[(0,1),(1,2)],'triangle':[(0,1),(1,2),(0,2)]}
rows=[]
for name,edges in shapes.items():
 E={frozenset(e) for e in edges};hist=[0]*4
 for T in combinations(range(8),3):
  k=sum(frozenset(e) in E for e in combinations(T,2));hist[k]+=1
 tsum=sum(hist[k]*triple[k] for k in range(4));a2=len(E)
 pairsum=28*36+84*15+126*a2;net=pairsum-tsum;bad=bare-net
 assert net>1144 and bad<D
 rows.append({'shape':name,'a2':a2,'triple_k_histogram':hist,'triple_sum_upper':tsum,'pair_sum_lower':pairsum,'deduction_lower':net,'all_bad_upper':bad,'success_lower':D-bad})
assert [r['triple_sum_upper'] for r in rows]==[448,616,784,840,1190]
assert min(r['deduction_lower'] for r in rows)==1456
# Direct verification of third-order Bonferroni: at any sample withm active red events,
# m-C(m,2)+C(m,3) is at least unionindicator, m=0..8.
bonf=[m-C(m,2)+C(m,3) for m in range(9)]
assert all(z>=int(m>0) for m,z in enumerate(bonf))
# Verify no union-size bound monotonicity reversal, u=0..17.
counts=[C(17-u,10-u) for u in range(18)]
assert all(counts[u]>=counts[u+1] for u in range(17))
out={'status':'PASS_SCALARS_AND_SPARSE_SHAPE_COUNTS','scope':__doc__,'D':D,'red_single':single,'blue_single':blue,'bare_all_bad_upper':bare,'needed_deduction_strictly_above':bare-D,'pair_joint_by_intersection':pair,'triple_upper_by_two_intersection_edges':triple,'forest_branches':[{'case':'hasintersection3','deduction':forest3,'bad_upper':bare-forest3,'success_lower':D-bare+forest3},{'case':'intersection_atleast2graph_rank>=3','deduction':forest2,'bad_upper':bare-forest2,'success_lower':D-bare+forest2}],'bonferroni_branches':rows,'third_order_pointwise_counts':bonf,'universal_all_bad_upper':bare-forest2,'universal_success_lower':D-bare+forest2,'cpu_seconds':time.process_time()-st}
assert out['universal_all_bad_upper']==19374 and out['universal_success_lower']==74
(P/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ('bonferroni_branches','third_order_pointwise_counts')})
