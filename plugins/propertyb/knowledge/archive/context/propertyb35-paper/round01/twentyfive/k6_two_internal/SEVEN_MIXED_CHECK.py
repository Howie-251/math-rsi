"""Exact branch arithmetic and three actual star count callers for the seven-mixed lemma."""
from fractions import Fraction as Q
from pathlib import Path
from itertools import combinations
import json
P=Path(__file__).resolve().parent;p=Q(7,16);w=[Q(1,2)**j*p**(4-j) for j in range(4)]
chord=[w[0]+Q(j,3)*(w[3]-w[0])-w[j] for j in range(4)];assert all(v>=0 for v in chord)
bad=21*w[0]+6*(w[3]-w[0]);assert bad==Q(57519,65536)<1 and 21*p**4==Q(50421,65536)<1
branches=[]
for b in range(5):
 for cand,badmax,label in [(27,b,'three_disjoint'),(9,b,'four_with_intersection'),(81,4*b+21-b,'four_disjoint')]:
  assert cand>badmax;branches.append(dict(b=b,candidates=cand,bad_upper=badmax,case=label))
source=json.loads((P/'STAR_RESIDUALS.json').read_text());covered=[];excluded=[]
for r in source['records']:
 if r['positive_four']==6:
  assert r['positive_triple']==1 and r['negative_triple']==0 and r['negative_four']==21
  assert all(r['P_degrees'][i]==8 for i in r['blue']);covered.append(dict(nine=r['nine'],star_center=r['star_center'],blue=r['blue']))
 else:
  assert r['positive_four']==7 and r['positive_triple']==1 and r['negative_four']==20
  excluded.append(dict(nine=r['nine'],star_center=r['star_center'],blue=r['blue'],reason='eight positives exceeds this theorem'))
assert len(covered)==3 and len(excluded)==1
out=dict(passed=True,scope=__doc__,chord_slacks=[str(v) for v in chord],union_bound_no_triple=str(21*p**4),union_bound_one_positive_triple=str(bad),numeric_branches=branches,covered_star_callers=covered,excluded_star_caller=excluded)
(P/'SEVEN_MIXED_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='numeric_branches'},indent=2))
