"""Two small positive-only diagnostic witnesses; no negative-layout search."""
from itertools import combinations
from fractions import Fraction as F
from pathlib import Path
import json

# Ten four-sets on18 points, all four three-stars meet the same positive label.
sets=[set() for _ in range(10)]
for point,triple in enumerate(((0,1,2),(0,3,4),(0,5,6),(0,7,8))):
 for i in triple:sets[i].add(point)
edges=[(i,i+1) for i in range(1,8)]+[(8,1)]+[(i,9) for i in (1,3,5,7)]+[(2,4),(6,8)]
for point,(a,b) in enumerate(edges,4):sets[a].add(point);sets[b].add(point)
assert all(len(s)==4 for s in sets)
U=set().union(*sets);assert len(U)==18
stars={p:tuple(i for i,s in enumerate(sets) if p in s) for p in U}
three=[s for s in stars.values() if len(s)==3]
assert len(three)==4 and all(set(a)&set(b) for a,b in combinations(three,2))

# A seven-label graph with E12 and no four-point transversal.
seven=[set() for _ in range(7)];point=0
for labels in ((0,1,2),(3,4,5)):
 for a,b in combinations(labels,2):
  for _ in range(2):seven[a].add(point);seven[b].add(point);point+=1
for _ in range(4):seven[6].add(point);point+=1
V=set().union(*seven)
counts={k:sum(all(set(s)&a for a in seven) for s in combinations(V,k)) for k in (3,4,5)}
assert len(V)==16 and counts=={3:0,4:0,5:576}
out=dict(pass_all=True,low_occurrence_bound=str(2*F(7,16)**3+18*F(7,16)**4),
         ten_positive_intersecting_three_stars=dict(sets=[sorted(s) for s in sets],
                    three_stars=three,variables=len(U),max_positive_occurrence=max(map(len,stars.values()))),
         seven_label_short_candidate_obstruction=dict(sets=[sorted(s) for s in seven],
                    E=12,union=len(V),transversal_counts=counts),
         negative_constraints_constructed=False,
         not_a_signed_counterexample=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('ten_positive_intersecting_three_stars','seven_label_short_candidate_obstruction')},indent=2))
