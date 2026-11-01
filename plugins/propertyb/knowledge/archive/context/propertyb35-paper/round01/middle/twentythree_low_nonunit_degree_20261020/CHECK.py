"""Exact23-point anchor counts and seven-red-foursets-on18 forest/Bonferroni scalars."""
from pathlib import Path
from math import comb
from itertools import combinations
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.process_time()
def C(n,r):return comb(n,r) if 0<=r<=n else 0
D=C(18,11);R=C(14,7);B=C(14,11);E0=C(13,6)+C(13,11)
weights=[C(10+j,3+j) for j in range(4)]
assert (D,R,B,E0)==(31824,3432,364,1794)
assert weights==[120,330,792,1716]
def parts(n,k,lo=1):
 if not k:
  if n==0:yield ()
  return
 for a in range(lo,n+1):
  for rest in parts(n-a,k-1,a):yield (a,)+rest
linear_cases=[]
for c in (3,4):
 for sizes in parts(7,c):
  lower=sum(4*s-C(s,2) for s in sizes)
  linear_cases.append(dict(components=c,sizes=sizes,union_lower=lower,not_ruled_out=lower<=18))
assert [tuple(x['sizes']) for x in linear_cases if x['not_ruled_out']]==[(1,1,5)]
forest={'at_most_two_components':5*weights[1]+weights[0], 'three_components_with_pair2':weights[2]+3*weights[1]+2*weights[0], 'four_components_with_pair2':weights[2]+2*weights[1]+3*weights[0]}
assert forest==dict(at_most_two_components=1770,three_components_with_pair2=2022,four_components_with_pair2=1812)
# Exact fixed special family: K5 edges as ten points, two independent foursets.
pairs=list(combinations(range(5),2));A=[frozenset(i for i,p in enumerate(pairs) if v in p) for v in range(5)]+[frozenset(range(10,14)),frozenset(range(14,18))]
assert len(set(A))==7 and all(len(a)==4 for a in A)
byorder={}
for k in range(1,8):
 byorder[k]=sum(C(18-len(frozenset().union(*(A[i] for i in ids))),11-len(frozenset().union(*(A[i] for i in ids)))) for ids in combinations(range(7),k))
assert byorder=={1:24024,2:4620,3:380,4:40,5:8,6:0,7:0}
exact_red_union=sum((-1)**(k+1)*v for k,v in byorder.items())
assert exact_red_union==19752
bonferroni_deduction=byorder[2]-byorder[3];assert bonferroni_deduction==4240
minimum_red_deduction=min(*forest.values(),bonferroni_deduction);assert minimum_red_deduction==1770
cases={}
cases['q0']=6*R+28*B
cases['q1_disjoint_c0to5_max']=5*R+28*B+E0
cases['q1_disjoint_c6']=6*R+27*B+E0-5*weights[0]
cases['q1_overlap_common_degree_le9_c0to6_max']=6*R+27*B
cases['q1_overlap_common_degree_le9_c7']=7*R+26*B-minimum_red_deduction
high=[]
for j in (2,3,4):
 a=(33-8*j)//(5-j);value=a*R+(33-a)*B+C(13+j,11)
 assert (j,a,value) in [(2,5,28717),(3,4,28652),(4,1,27456)]
 cases['q1_overlap_all_common_degree_ge10_j'+str(j)]=value
 high.append(dict(intersection=j,anchor_attachment_max=a,exceptional_blue_count=C(13+j,11),bad_bound=value))
assert all(v<D for v in cases.values())
out=dict(status='PASS',scope=__doc__,sample_count=D,red_single=R,blue_single=B,empty_five=E0,red_pair_by_intersection=weights,linear_component_cases=linear_cases,forest_deductions=forest,special_7family=[sorted(a) for a in A],special_IE_order_sums=byorder,special_exact_red_union=exact_red_union,special_third_Bonferroni_deduction=bonferroni_deduction,universal_seven_red_deduction=minimum_red_deduction,actual_H_bad_bounds=cases,high_common_degree_cases=high,maximum_bad_bound=max(cases.values()),minimum_success_samples=D-max(cases.values()),cpu_seconds=time.process_time()-st)
(P/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
