"""Deterministic check of the explicit 44-negative signed counterexample.

The 8192 subsets are used only for this one counterexample, never to prove
the positive theorem. The theorem's small scalar identities are also checked.
"""
from itertools import combinations, product
from math import prod
from pathlib import Path
import json

names = ['e01','e02','e12','a1','a2','b1','b2','c1','c2','d1','d2','d3','d4']
P = [set(z) for z in [('e01','e02','a1','a2'),('e01','e12','b1','b2'),
                     ('e02','e12','c1','c2'),('d1','d2','d3','d4')]]
core = sorted(set.union(*P[:3]))
K = [set(z) for z in combinations(core,2) if all(set(z)&A for A in P[:3])]
assert len(K)==9
N = [z|{d} for z in K for d in sorted(P[3])]
N += [set(z) for z in product(('a1','a2'),('b1','b2'),('c1','c2'))]
assert len(N)==len({tuple(sorted(z)) for z in N})==44
assert len(names)==13 and all(len(A)==4 for A in P) and all(len(F)==3 for F in N)

pm = [sum(1<<names.index(v) for v in A) for A in P]
nm = [sum(1<<names.index(v) for v in F) for F in N]
positive_transversals = 0
blocked_transversals = 0
repairs = []
for R in range(1<<13):
    if not all(R&A for A in pm):
        continue
    positive_transversals += 1
    if any(R&F==F for F in nm):
        blocked_transversals += 1
    else:
        repairs.append(R)
assert not repairs and positive_transversals==blocked_transversals

star = []
for r in product(range(5),repeat=3):
    if tuple(sorted(r,reverse=True)) != r or not 1<=sum(r)<=4:
        continue
    c3=64-prod(4-x for x in r)
    c4=(4-sum(r))*prod(4-x for x in r)
    margin = c3-43 if c3>43 else c4-4*(43-c3)
    assert margin>0
    star.append(dict(weights=r,C3=c3,C4=c4,strict_margin=margin))
triangle=[]
for a,b,c in product(range(1,5),repeat=3):
    if not a<=b<=c or max(a+b,a+c,b+c)>4:
        continue
    c3=4*(4*(a+b+c)-(a*b+a*c+b*c))
    margin = 32-4*(43-c3) if (a,b,c)==(1,1,1) else c3-43
    assert margin>0
    triangle.append(dict(weights=[a,b,c],C3=c3,strict_margin=margin))
assert len(star)==10 and len(triangle)==5

out=dict(status='PASS',scope='one explicit signed counterexample plus scalar identities',
         vertices=names,total_indexed_occurrence={v:sum(v in A for A in P+N) for v in names},positive_sets=[sorted(A) for A in P],
         core_two_point_transversals=[sorted(A) for A in K],
         negative_sets=[sorted(F) for F in N],subsets_checked=1<<13,
         positive_transversals=positive_transversals,
         blocked_transversals=blocked_transversals,repair_count=0,
         star_scalar_rows=star,triangle_scalar_rows=triangle,
         minimum_star_strict_margin=min(z['strict_margin'] for z in star),
         minimum_triangle_strict_margin=min(z['strict_margin'] for z in triangle),
         not_a_property_B_hypergraph_counterexample=True)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(f'PASS: 8192 subsets, {positive_transversals} positive transversals all blocked; '
      f'{len(star)} star and {len(triangle)} triangle scalar rows strict')
