"""Only small scalar bounds and five C-point frequencies, not H/set searches."""
from itertools import product
from pathlib import Path
import json

assert 16 > 4
assert 3 * 3 * 4 > 35
assert 4 ** 3 > 4 * 4 + 35
rows = []
for h in product(range(3), repeat=5):
    H_C = sum(h)
    if H_C < 4:
        continue
    x2 = h.count(2)
    C_J_upper = sum({0: 3, 1: 1, 2: 0}[a] for a in h)
    assert C_J_upper == 15 - 2 * H_C + x2
    D_J_upper = 4 + H_C
    upper = C_J_upper + D_J_upper
    assert H_C - x2 >= (H_C + 1) // 2 >= 2
    assert upper <= 17 < 18
    rows.append(dict(h=list(h), H_C=H_C, x2=x2,
                     J_total_upper=upper, gap=18-upper))
assert rows
out = dict(status="PASS", scope="scalar/local-frequency checks only",
           candidate_margins=dict(two_disjoint=16-4,
                                  star_rescue=36-35,
                                  three_disjoint=64-51),
           frequency_rows=len(rows), max_J_degree_upper=max(r["J_total_upper"] for r in rows),
           minimum_J_gap=min(r["gap"] for r in rows), rows=rows)
(Path(__file__).parent / "CHECK_R4.json").write_text(json.dumps(out, indent=2) + "\n")
print({k: out[k] for k in ("status", "frequency_rows", "max_J_degree_upper", "minimum_J_gap")})
