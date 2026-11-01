"""Independent direct bit-mask replay of the balanced unique-edge swap bound.

No hypergraphs are enumerated: one ordered pair of 5-sets per intersection
type is checked against all balanced colorings and the designated swaps.
"""
from itertools import combinations
from math import comb
from fractions import Fraction
from pathlib import Path
import json

N = 18
K = 5
B = N // 2
FULL = (1 << N) - 1
E = (1 << K) - 1


def mono(edge, red):
    return edge & red in (0, edge)


def direct(t):
    g = sum(1 << i for i in list(range(t)) + list(range(K, 2 * K - t)))
    counts = {"new_red": 0, "new_blue": 0}
    for extra in combinations(range(K, N), B - K):
        red = E | sum(1 << i for i in extra)
        if mono(g, red):
            continue
        blue = [i for i in range(N) if not (red >> i) & 1]
        for x in range(K):
            for y in blue:
                after = red ^ (1 << x) ^ (1 << y)
                assert not mono(E, after)
                if g & after == g:
                    counts["new_red"] += 1
                elif g & after == 0:
                    counts["new_blue"] += 1
    # Complementation gives a disjoint, equally sized class with E blue.
    return {**counts, "both_colors_total": 2 * sum(counts.values())}


def safecomb(n, r):
    return comb(n, r) if 0 <= r <= n else 0


def formula(t):
    same = (K - t) ** 2 * safecomb(N - 2*K + t, B - 2*K + t + 1)
    other = (B - K + 1) * safecomb(N - 2*K + 1, B - K) if t == 1 else 0
    return 2 * (same + other)


rows = []
for t in range(K):
    d = direct(t)
    f = formula(t)
    assert d["both_colors_total"] == f
    rows.append({"intersection": t, **d, "formula": f})
colors = comb(N, B)
per_edge = 2 * comb(N - K, B - K)
swap_degree = K * B
max_coeff = max(r["formula"] for r in rows)
budgets = []
for m in range(1, 40):
    unique_lower = 2 * colors - m * per_edge
    lhs = swap_degree * unique_lower
    rhs = m * (m - 1) * max_coeff
    budgets.append({"m": m, "unique_lower": unique_lower, "lhs": lhs,
                    "rhs": rhs, "strict_contradiction": lhs > rhs})
out = {"n": N, "k": K, "balanced_colorings": colors,
       "bad_colorings_per_edge": per_edge, "swaps_per_unique_coloring": swap_degree,
       "ordered_pair_rows": rows, "max_pair_coefficient": max_coeff,
       "largest_m_certified": max(r["m"] for r in budgets if r["strict_contradiction"]),
       "budgets": budgets}
Path(__file__).with_name("UNIQUE_SWAP_REPLAY.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({k:v for k,v in out.items() if k != "budgets"}, indent=2))
