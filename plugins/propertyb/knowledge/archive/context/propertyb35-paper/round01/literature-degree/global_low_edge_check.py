"""Tiny integer/Fraction replay. No hypergraph or edge-layout enumeration."""
from fractions import Fraction as F
from pathlib import Path
from math import comb
import json
H=Path(__file__).parent
maxima={}
for d in (1,2,3):
 vals=[(d*(21-a)+b*(b-d)+c*(c-d),(a,b,c,d)) for a in range(d,12) for b in range(d,a+1) for c in range(d,b+1) if a+b+c+d<=14]
 maxima[str(d)]=max(vals)
 assert maxima[str(d)][0]<59
classes=[(1,0,4,6),(1,3,1,3),(1,4,0,1),(0,3,2,25)]
point_deg={'v':sum(v*w for v,a,b,w in classes),'A':str(F(sum(a*w for v,a,b,w in classes),11)),'B':str(F(sum(b*w for v,a,b,w in classes),11))}
pair_deg={'vA':str(F(sum(v*a*w for v,a,b,w in classes),11)),'vB':str(F(sum(v*b*w for v,a,b,w in classes),11)),'AA':str(F(sum(comb(a,2)*w for v,a,b,w in classes),55)),'BB':str(F(sum(comb(b,2)*w for v,a,b,w in classes),55)),'AB':str(F(sum(a*b*w for v,a,b,w in classes),121))}
assert all(F(q)>=1 for q in pair_deg.values())
assert all(F(w,comb(11,a)*comb(11,b))<1 for v,a,b,w in classes)
assert sum(w for v,a,b,w in classes)==35
assert sum((3*v+a)*w for v,a,b,w in classes)==118
n21=[str(F((a+8)*(7-a)-4*a,27-a)) for a in (1,2,3)]
assert all(F(z)<2 for z in n21)
assert all(F((a+7)*(14-a)-4*a,28-a)<4 for a in range(1,11))
assert all(F((a+7)*(7-a)-4*a,28-a)<2 for a in range(1,4))
assert max(((a+7)*(28-a)-4*a)//(28-a) for a in range(1,25))==17
out={'result':'PASS','scope':'Only integer moment constants and an explicit fractional four-class boundary; no H enumeration','n22_d_branch_relaxed_maxima':maxima,'n21_d8_avoid_maximum_bounds':n21,'fractional_n23_boundary':{'classes':classes,'point_degrees':point_deg,'pair_degrees':pair_deg,'all_edge_excess_at_least':3},'n23_low_edge_degree_patterns':[[7,7,7,7,7],[7,7,7,7,8],[7,7,7,7,9],[7,7,7,8,8],[7,7,7,7,10],[7,7,7,8,9],[7,7,8,8,8]]}
(H/'GLOBAL_LOW_EDGE_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS: degree-moment constants and four-class rational boundary')
