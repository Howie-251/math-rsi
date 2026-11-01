"""Exact illustrations of the candidate additive gain; not a proof by sampling."""
import json
from fractions import Fraction
from math import factorial, isqrt
from pathlib import Path

rows = []
for k, b, n in [(17, 3, 5), (32, 4, 5), (64, 5, 6), (128, 5, 10), (256, 6, 9)]:
    # exp(b) exceeds this finite positive sum; hence log(k) < b.
    exp_lower = sum((Fraction(b) ** j / factorial(j) for j in range(n + 1)), Fraction())
    assert exp_lower > k
    root = isqrt(2 ** k)
    assert root * root <= 2 ** k < (root + 1) ** 2
    rows.append({
        "k": k,
        "log_upper": b,
        "exp_partial_terms_through": n,
        "exp_partial_sum": str(exp_lower),
        "floor_sqrt_2k": root,
        "certified_increment_lower": root // (8 * (1 + b)),
    })

path = Path(__file__).with_name("CONSERVATIVE_GAIN_EXAMPLES.json")
saved = json.loads(path.read_text())
assert saved["rows"] == rows
print(f"PASS: {len(rows)} exact integer/rational illustrations; B_RS itself not computed")
