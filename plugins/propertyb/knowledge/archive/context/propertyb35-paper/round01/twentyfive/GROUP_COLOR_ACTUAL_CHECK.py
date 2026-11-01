"""Actual affine-plane-plus-parabolas example: every group-symmetric first-moment orbit.
This hypergraph is explicitly colorable; the obstruction concerns one proof method.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from itertools import combinations_with_replacement,permutations
from math import comb
import json,time
P=Path(__file__).resolve().parent;R=P.parents[3];st=time.perf_counter()
source=R/'context/propertyb36-40-diagnosis-20261015/high-structure/AFFINE_PLANE_OBSTRUCTION.json'
data=json.loads(source.read_text());edges=[set(e) for e in data['edges']]
assert len(edges)==len({tuple(sorted(e)) for e in edges})==35
assert all(len(e)==5 for e in edges)
pointgroup={p:((p%5)-(p//5)**2)%5 for p in range(25)}
groups=[sorted(p for p in range(25) if pointgroup[p]==j) for j in range(5)]
assert all(len(g)==5 for g in groups)
assert all(sum(p in e for e in edges)==7 for p in range(25))
parts=Counter(tuple(sorted([sum(pointgroup[p]==j for p in e) for j in range(5)],reverse=True)) for e in edges)
assert parts==Counter({(1,1,1,1,1):5,(2,2,1,0,0):25,(5,0,0,0,0):5})
results=[]
for r in combinations_with_replacement(range(6),5):
 ps=sorted(set(permutations(r)));total=Q()
 for composition,n in parts.items():
  prob=Q()
  for assigned in ps:
   red=blue=Q(1)
   for ri,t in zip(assigned,composition):
    red*=Q(comb(ri,t) if ri>=t else 0,comb(5,t))
    blue*=Q(comb(5-ri,t) if 5-ri>=t else 0,comb(5,t))
   prob+=red+blue
  total+=n*prob/len(ps)
 results.append(dict(red_counts=list(r),expected_monochromatic_edges=str(total)))
minimum=min(Q(z['expected_monochromatic_edges']) for z in results)
best=[z['red_counts'] for z in results if Q(z['expected_monochromatic_edges'])==minimum]
# Independently retain and verify the documented proper coloring of this same H.
red=set([3,9,11,13,15,16,17,18,21,22,23]);edge_red_counts=[len(e&red) for e in edges]
assert all(1<=n<=4 for n in edge_red_counts)
out=dict(scope=__doc__,source=str(source.relative_to(R)),point_group_formula='(y-x^2) mod 5, with point=5*x+y',groups=groups,actual_group_composition_counts=[dict(composition=list(c),count=n) for c,n in sorted(parts.items())],orbits=len(results),minimum_expectation=str(minimum),all_minimizing_orbits=best,all_orbits_expectation_at_least_one=minimum>=1,known_proper_coloring_verified=True,known_red_set=sorted(red),proper_coloring_red_counts_by_group=[len(set(g)&red) for g in groups],expectations=results,elapsed_seconds=time.perf_counter()-st)
(P/'GROUP_COLOR_ACTUAL_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='expectations'},indent=2))
