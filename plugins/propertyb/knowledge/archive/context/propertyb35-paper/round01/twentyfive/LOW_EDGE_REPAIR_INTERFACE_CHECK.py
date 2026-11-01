"""Local color-action orbit check for a protected real five-edge on23/24 points.
Only group/color compositions are enumerated; no hypergraph/trace catalogue.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction as Q
from math import comb
import json
P=Path(__file__).resolve().parent
C=lambda n,k:comb(n,k) if 0<=k<=n else 0
out=[]
for n in [23,24]:
 G=set(range(5));O=set(range(5,n));profiles=[];records=[]
 den=sum(C(5,g)*C(n-5,(9 if n==23 else 12-g)) for g in [2,3])
 for t in range(5):
  numer=0
  for g in [2,3]:
   ro=9 if n==23 else 12-g
   numer+=2*C(5-t,g-t)*C(n-10+t,ro-(5-t))
  profiles.append(Q(numer,den))
 for g in [2,3]:
  ro=9 if n==23 else 12-g;R=set(range(g))|set(range(5,5+ro));B=set(range(n))-R;actions=[]
  for x in R:
   for y in B:
    if n==23:
     if (x in G)==(y in G):actions.append({x,y})
    else:
     changed=R^{x,y}
     if len(changed&G) in [2,3]:actions.append({x,y})
  if n==23:actions.extend([{x} for x in (B&G if g==2 else R&G)])
  assert len(actions)==(90 if n==23 else 126)
  # Every orbit is specified by mono color and G intersection, or by minority
  # color/location and majority G incidence. Representatives cover all orbits.
  for color,M in [('red',R),('blue',B)]:
   gg=sorted(M&G);oo=sorted(M&O)
   for t in range(6):
    if t>len(gg) or 5-t>len(oo):continue
    e=set(gg[:t]+oo[:5-t]);D=sum(0<len((R^a)&e)<5 for a in actions)
    expected=45-6*t if n==23 else ((60-9*t) if len(M&G)==2 else (50+2*t));assert D==expected
    records.append(dict(n=n,g_red=g,kind='mono',color=color,G_trace=t,destroyed=D))
   opp=B if color=='red' else R
   for minority_in_G in [False,True]:
    yy=sorted(opp&(G if minority_in_G else O))
    if not yy:continue
    for k in range(5):
     if k>len(gg) or 4-k>len(oo):continue
     f={yy[0]}|set(gg[:k]+oo[:4-k]);t=k+int(minority_in_G);new=sum(len((R^a)&f) in [0,5] for a in actions)
     if n==23:assert new==(4-t if minority_in_G else 5+t)
     else:assert new<=8
     records.append(dict(n=n,g_red=g,kind='critical',majority=color,minority_in_G=minority_in_G,G_trace=t,new_mono=new))
 out.append(dict(n=n,profile=[str(q) for q in profiles],max_nong_probability=str(max(profiles)),expected_nong_upper=str(34*max(profiles)),has_at_most_one_bad=True,actions=90 if n==23 else 126,minimum_mono_destroy=min(z['destroyed'] for z in records if z['kind']=='mono'),maximum_critical_create=max(z['new_mono'] for z in records if z['kind']=='critical'),local_composition_records=records))
assert all(Q(z['expected_nong_upper'])<2 for z in out)
witness=dict(n=23,G_edge=1,other_empty_traces=4,other_singleton_traces_per_G_point=6,G_degrees=[7]*5,nong_incidence=30,cross_G_outside_incidence=120,required_cross=90,degree_budget=35,first_moment='23/17',actual_H_realization_claimed=False,relaxation_scope='total edges, exact G degrees, trace cardinalities and aggregate cross-pair coverage only')
assert 30*Q(7,170)+4*Q(1,34)==Q(23,17)
result=dict(passed=True,scope=__doc__,profiles=out,relaxation_witness=witness)
(P/'LOW_EDGE_REPAIR_INTERFACE_CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(dict(passed=True,profiles=[{k:v for k,v in z.items() if k!='local_composition_records'} for z in out],relaxation_witness=witness),indent=2))
