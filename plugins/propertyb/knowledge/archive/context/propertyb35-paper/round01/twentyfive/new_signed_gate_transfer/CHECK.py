"""Fixed actual-H and rational checks; no q3 DP or layout search."""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
raw = json.loads((HERE.parent / 'MIXED_THREE_SIX_UNIT8_REALIZATION.json').read_text())
H = list(map(frozenset, raw['edges']))
V = set(raw['points'])
K = {0, 1, 2}
G = next(e for e in H if K <= e)
W = V-G
H0 = [e for e in H if not e & K]
degree = Counter(x for e in H for x in e)
assert len(H) == 35 and len(H0) == 19
for g in K:
    assert degree[g] == 6
    assert all(sum({g, x} <= e for e in H) == 1 for x in V-{g})
    blocks = [e-{g} for e in H if g in e and e != G]
    assert len(blocks) == 5 and all(len(A) == 4 for A in blocks)
    assert set().union(*blocks) == W
    assert sum(map(len, blocks)) == len(W)
parallel = [frozenset(range(5*i, 5*i+5)) for i in range(1, 5)]
assert all(e in H and not e & G for e in parallel)
assert all(not e & f for e, f in combinations(parallel, 2))

# One fixed source-color example: only H0 must initially be proper.  This is
# an illustration of a valid monotone signed interface, not a universal caller.
g = 2
red_nonlow = {3, 4, 9, 10, 15, 24}
blue_nonlow = V-K-red_nonlow
assert all(e & red_nonlow and e & blue_nonlow for e in H0)
positive = [e-{g} for e in H if e != G and e & K == {g}
            and e-{g} <= blue_nonlow]
U = set().union(*positive)
negative_all = [e & blue_nonlow for e in H if g not in e]
assert all(negative_all)
active_negative = [B for B in negative_all if B <= U]
occ = Counter(x for A in positive+active_negative for x in A)
assert positive == [frozenset({7, 12, 17, 22})]
assert not active_negative and max(occ.values()) == 1

# Cost budget <=32: optimize its integer singleton count independently.
cost_max = max(F(n1, 4)+F(n2, 16)+F(n3, 64)+F(29, 256)
               for n1 in range(4) for n2 in range(9) for n3 in range(33)
               if 9*n1+4*n2+n3 <= 32)
assert cost_max == F(241, 256) < 1
result = {
    'scope': 'One frozen actual H and finite signed-count arithmetic; no whole-H enumeration.',
    'G': sorted(G), 'lows': sorted(K), 'zero_low_edge_count': len(H0),
    'disjoint_zero_G_edges': [sorted(e) for e in parallel],
    'forced_minimum_red_exterior_in_any_proper_H_minus_G': 4,
    'fixed_H0_proper_example': {
        'blue_low': g, 'red_lows': sorted(K-{g}),
        'initial_red_nonlow': sorted(red_nonlow),
        'positive_four_sets': [sorted(A) for A in positive],
        'active_negative_count': len(active_negative),
        'active_max_signed_occurrence': max(occ.values()),
        'scope': 'A colorable example with an elementary one-point repair, not new branch coverage.',
    },
    'one_red_cost32_union_bound': str(cost_max), 'status': 'PASS',
}
(HERE/'CHECK.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
