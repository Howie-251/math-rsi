"""An explicit obstruction to nine unit locks, not to Property B."""
from itertools import combinations
from pathlib import Path
import json
import random

vertices=list(range(25))
point=lambda x,y:5*x+y
lines=[frozenset(point(x,y) for y in range(5)) for x in range(5)]
lines += [frozenset(point(x,(a*x+b)%5) for x in range(5))
          for a in range(5) for b in range(5)]
parabolas=[frozenset(point(x,(x*x+c)%5) for x in range(5)) for c in range(5)]
edges=lines+parabolas
assert len(set(edges))==35 and all(len(e)==5 for e in edges)
assert all(sum(x in e for e in edges)==7 for x in vertices)
group=lambda p: ((p%5)-(p//5)**2)%5
for x,y in combinations(vertices,2):
    assert sum(x in e and y in e for e in edges)==1+(group(x)==group(y))
# One point from each group is unit; two from the same group are nonunit.
unit_witness=list(range(5))
assert len(set(group(x) for x in unit_witness))==5
rng=random.Random(20261015)
for attempt in range(10000):
    red={x for x in vertices if rng.randrange(2)}
    if all(0<len(e&red)<5 for e in edges):
        break
else:
    raise RuntimeError('No coloring found within the diagnostic budget')
result=dict(point_encoding='5*x+y, x,y in F5',
            edges=[sorted(e) for e in edges],
            lines=30,extra_parabolas=5,regular_degree=7,
            nonunit_graph='five disjoint K5, each lambda=2; all other lambda=1',
            maximum_unit_set=5,unit_set_witness=unit_witness,
            proper_coloring_red=sorted(red),
            per_edge_red_count=[len(e&red) for e in edges],
            coloring_attempts=attempt+1,
            scope='A verified counterexample to a universal nine-unit-lock selection at M35,v25. It is colorable; not a counterexample to m(5)>=36.')
Path(__file__).with_name('AFFINE_PLANE_OBSTRUCTION.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='edges'},indent=2))
