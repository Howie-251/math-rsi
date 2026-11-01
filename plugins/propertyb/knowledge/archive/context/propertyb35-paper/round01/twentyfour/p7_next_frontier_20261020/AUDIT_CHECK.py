"""Independent scalar/interface checks; no hypergraph or source-domain search."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json

directory = Path(__file__).parent
margins = []
for groups in product(range(2, 5), repeat=4):
    if max(groups) == 2:
        continue
    candidates = 1
    for size in groups:
        candidates *= size
    margin = candidates - 4 * max(groups) + 3 - Fraction(3, 2) * sum(groups)
    assert margin > 0
    margins.append(margin)
assert len(margins) == 80 and min(margins) == Fraction(3, 2)

profiles = {tuple(sorted(h)) for h in product(range(3), repeat=5) if sum(h) >= 8}
assert profiles == {(1, 1, 2, 2, 2), (0, 2, 2, 2, 2),
                    (1, 2, 2, 2, 2), (2, 2, 2, 2, 2)}
tails = {(a, b, c) for a, b, c in product(range(6), repeat=3)
         if a >= 1 and b >= 1 and a + b + c == 5
         and a + c <= 3 and b + c <= 3}
assert tails == {(2, 3, 0), (3, 2, 0), (2, 2, 1)}
for a, b, c in tails:
    assert (7 - a - b) + (4 - a - c) == 6 - a
    assert 0 <= a <= 3

pair_calls = []
for high_frequency, minimum_j_degree in [(4, 1), (3, 2)]:
    upper = min(8 - high_frequency, 15 - 3 * high_frequency)
    for degree in range(minimum_j_degree, upper + 1):
        m = 13 - high_frequency - degree
        t, b = 5 - degree, 25 - m
        gate = "eight_4T_17B" if m == 8 else "at_most_seven_4T_35B"
        if m == 8:
            assert t <= 4 and b <= 17
        else:
            assert m <= 7 and t <= 4 and b <= 35
        pair_calls.append(dict(h=high_frequency, s=degree, m=m, t=t, b=b, gate=gate))

out = dict(status="PASS", scope="local scalar and gate-interface arithmetic only",
           ordered_four_group_size_tuples=len(margins),
           minimum_margin=str(min(margins)),
           C_frequency_profiles=sorted(profiles), J_tails=sorted(tails),
           pair_calls=pair_calls)
(directory / "AUDIT_CHECK.json").write_text(json.dumps(out, indent=2) + "\n")
print({k: out[k] for k in ("status", "ordered_four_group_size_tuples", "minimum_margin")})
