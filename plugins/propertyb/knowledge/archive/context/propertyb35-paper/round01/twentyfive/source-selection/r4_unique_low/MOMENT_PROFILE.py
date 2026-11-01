"""One actual r4/no-three-low H: exact balanced third monochromatic moment.
No hypergraph or coloring-space search. Sum only its 6545 edge triples.
"""
from itertools import combinations,product
from fractions import Fraction
from math import comb
from pathlib import Path
from collections import Counter
import json,time
D=Path(__file__).resolve().parent;t0=time.process_time()
V=set(range(25)); low={0,6,14,19}
E=[]
for x in range(5):E.append(frozenset(5*x+y for y in range(5)))
for m in range(5):
 for b in range(5):E.append(frozenset(5*x+(m*x+b)%5 for x in range(5)))
hub=1;rest=sorted(V-low-{hub})
extras=[frozenset([hub]+rest[4*j:4*j+4]) for j in range(5)]
assert len(rest)==20 and not set(E)&set(extras) and len(set(extras))==5
E+=extras;assert len(E)==35 and len(set(E))==35
freq={x:sum(x in e for e in E) for x in V}
assert {x for x in V if freq[x]==6}==low
assert all(sum(x in e and y in e for e in E)>=1 for x,y in combinations(V,2))
assert all(len(e&low)<=2 for e in E)
L=sum(bool(e&low) for e in E);assert L==18
N=comb(25,12)
def joint(edges):
 comps=[]
 for e in edges:
  merged=set(e);keep=[]
  for C in comps:
   if C&e:merged|=C
   else:keep.append(C)
  # Three original edges suffice, but merge transitively explicitly.
  changed=True
  while changed:
   changed=False;left=[]
   for C in keep:
    if C&merged:merged|=C;changed=True
    else:left.append(C)
   keep=left
  comps=keep+[merged]
 sizes=tuple(sorted(map(len,comps)));free=25-sum(sizes);ways=0
 for colors in product((0,1),repeat=len(sizes)):
  red=sum(s*c for s,c in zip(sizes,colors));n=12-red
  if 0<=n<=free:ways+=comb(free,n)
 return ways,sizes
hist=Counter();num=0
for es in combinations(E,3):
 ways,sizes=joint(es);num+=ways;hist[(sizes,ways)]+=1
third=Fraction(num,N);lower=third/12;gap=Fraction(8,230)
low_indices=[j for j,e in enumerate(E) if e&low]
pair_num=0; pair_hist=Counter()
for j in low_indices:
 for k,f in enumerate(E):
  if j==k:continue
  w,sz=joint([E[j],f]);pair_num+=w;pair_hist[(len(E[j]&f),w)]+=1
pair_moment=Fraction(pair_num,N);bonf=Fraction(18*9,230)-pair_moment
p=Fraction(comb(12,5)+comb(13,5),comb(25,5));assert p==Fraction(9,230)
pt=[Fraction(w,N) for w in [13430,2380,8568,27132,77520]]
coeff={t:pt[t]+(t-1)*pt[0]-t*pt[1] for t in (2,3,4)}
mu=max(coeff[t]/comb(t,2) for t in (2,3,4));assert mu==Fraction(91,26220)
general_margin=18*p-(612*pt[0]+524*(pt[1]-pt[0])+68*mu)
assert general_margin==Fraction(58,45885)>0
hub_rows=[]
for t in range(3):
 TT=532-4*t;KK=72-4*t;bound=612*pt[0]+TT*(pt[1]-pt[0])+KK*mu
 margin=18*p-bound;assert margin>0
 hub_rows.append(dict(hub_double_low_incidence=t,T=TT,K2_upper=KK,pair_union_bound=str(bound),unique_low_margin=str(margin)))
tv={v:sum(v in e and len(e&low)==2 for e in E) for v in V-low}
assert sum(tv.values())==18 and max(tv.values())<=2
actualT=sum(t*c for (t,w),c in pair_hist.items())
assert actualT==532-sum((freq[v]-7)*tv[v] for v in V-low)

# Exhaustive scalar states verify the proposed pointwise inequality with U flag.
for X in range(1,10):
 for Y in range(0,min(X,L)+1):
  U=int(X==1 and Y==1)
  assert Y<=2*(X-1)+U-max(0,X-2)
  assert max(0,X-2)>=Fraction(comb(X,3),12)
out=dict(scope=__doc__,status='PASS',low=sorted(low),edges=[sorted(e) for e in E],
 degrees={str(x):freq[x] for x in V},low_incident_edges=L,
 balanced_denominator=N,mono_probability=str(p),base_gap=str(-gap),
 expected_choose_X_3=str(third),proposed_third_moment_contribution=str(lower),
 expected_Y_Xminus1=str(pair_moment),direct_targeted_bonferroni=str(bonf),
 low_other_oriented_pair_histogram=[dict(intersection=t,joint_colorings=w,count=c) for (t,w),c in sorted(pair_hist.items())],
 required_positive_contribution=str(gap),third_moment_sufficient=lower>gap,
 exact_pair_probability_by_intersection=[str(q) for q in pt],
 higher_intersection_unit_pair_cost=str(mu),
 general_K2_at_most_68_margin=str(general_margin),hub_coupled_budget=hub_rows,
 triangle_histogram=[dict(component_union_sizes=list(s),joint_colorings=w,count=c) for (s,w),c in sorted(hist.items())],
 cpu_seconds=time.process_time()-t0)
(D/'MOMENT_PROFILE.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('edges','degrees','triangle_histogram')},indent=2))
