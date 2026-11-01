"""Recompute the 19/20-vertex global-pair refinement at exactly 33 edges.

This checks arithmetic and both formulas; it does not build a new Lean theorem.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations"))
from multilock import Profile, rows, total_bound, json_value


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


out = []
for v in (19, 20):
    excess = 33 * comb(5, 2) - comb(v, 2)
    bad_unordered = (excess + 5) // 6
    cap = 33 * 32 - 2 * bad_unordered
    result_rows = rows(Profile(v, 5, (), {0: 33}), pair_caps={(0, 0): cap})
    independent_rows = []
    for k in range(1, v + 1):
        a = F(33 * 5 * choose(k - 1, 4), v * comb(v - 1, 4))
        b = F(33 * 5 * choose(v - k, 4), v * comb(v - 1, 4))
        c = F(cap * choose(k - 1, 4) * choose(v - k, 4),
              v * comb(v - 1, 4) * comb(v - 5, 4))
        observed = result_rows[k - 1]
        assert (a, b, c) == (observed['A'], observed['B'], observed['C'])
        independent_rows.append(min(a, b, c))
    bound = total_bound(result_rows)
    assert sum(independent_rows, F(0)) == bound
    out.append({
        'vertices': v, 'edges': 33,
        'vertex_pairs': comb(v, 2),
        'vertex_pair_incidence_sum': 330,
        'sum_choose_codegree_2_lower': excess,
        'bad_unordered_edge_pairs_lower': bad_unordered,
        'single_intersection_ordered_edge_pairs_cap': cap,
        'bound': bound, 'one_minus_bound': 1 - bound,
        'independent_closed_formula_agrees': True,
        'position_rows': result_rows,
    })
assert [case['bound'] for case in out] == [F(228291, 230945), F(4599, 4420)]
print(json.dumps(json_value({
    'scope': 'Exact arithmetic plus recorded mathematical deduction; no new Lean build',
    'cases': out,
}), ensure_ascii=False, indent=2))
