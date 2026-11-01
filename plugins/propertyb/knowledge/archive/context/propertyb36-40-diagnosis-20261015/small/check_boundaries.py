"""Exact counting formulas for the 36--40 diagnostic; no hypergraph search."""
from fractions import Fraction
from math import comb
from pathlib import Path
import json

def C(n, k):
    return comb(n, k) if 0 <= k <= n else 0

def pair_probability(v, t):
    a = v // 2
    u = 10 - t
    numerator = C(v-u, a-u) + C(v-u, a)
    if t == 0:
        numerator += 2*C(v-10, a-5)
    return Fraction(numerator, C(v, a))

budgets = []
for M in range(35, 40):
    vmax = max(v for v in range(9, 100) if v*((v+2)//4) <= 5*M)
    balanced = []
    for v in range(9, 28):
        a = v//2
        p = Fraction(C(a, 5)+C(v-a, 5), C(v, 5))
        balanced.append(dict(v=v, p=str(p), union=str(M*p)))
    budgets.append(dict(target_lower_bound=M+1, edge_budget=M, degree_sum=5*M,
                        max_pair_covered_vertices=vmax, remaining_window=[17,vmax],
                        balanced=balanced))
pair_probs = {str(v): {str(t): str(pair_probability(v,t)) for t in range(5)}
              for v in (15,16,17,18)}
result = dict(method='exact binomial arithmetic; not enumeration of hypergraphs',
              budgets=budgets, pair_monochromatic_intersection_by_edge_intersection=pair_probs,
              max_one_pair_17_18=str(max(pair_probability(18,t) for t in range(5))),
              one_pair_best_35=str(Fraction(35,34)-max(pair_probability(18,t) for t in range(5))))
Path(__file__).with_name('EXACT_BOUNDARIES.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='budgets'},indent=2))
