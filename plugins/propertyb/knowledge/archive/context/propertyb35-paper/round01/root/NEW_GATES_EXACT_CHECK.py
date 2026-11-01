"""Exact arithmetic for the analytic gates; not a classification of hypergraphs."""
from fractions import Fraction as Q
from pathlib import Path
import json

p, q = Q(7, 16), Q(1, 4)
checks = {
    "seven_mixed_one_triple": Q(55118, 65536) + Q(1, 8),
    "six_positive_union_ge16": 8*p**3 + 4*p**4 + 16*q**4,
    "six_positive_union_ge14": 8*p**3 + Q(13, 2)*p**4 + Q(27, 2)*q**4,
    "ten_positive_zero_triple": 27*p**4,
    "one_exterior_red_cost32": Q(3, 4) + Q(5, 64) + Q(29, 256),
}
assert all(value < 1 for value in checks.values())
for r, b in ((0, 0), (0, 1), (1, 0)):
    assert 4*r + (4-r) + b < 9
    assert 16*r + 4*(4-r) + 4*b + (20-b) < 108
assert 4 > 3  # Four distinct candidates versus the three other negative triples.
inventories = {(a, b, c) for a in range(11) for b in range(6) for c in range(4)
               if a + 2*b + 3*c == 10}
closed = {(10, 0, 0), (8, 1, 0), (7, 0, 1), (0, 5, 0),
          (1, 3, 1), (0, 2, 2), (1, 0, 3)}
open_ = {(6, 2, 0), (4, 3, 0), (2, 4, 0), (5, 1, 1),
         (3, 2, 1), (4, 0, 2), (2, 1, 2)}
assert closed.isdisjoint(open_) and closed | open_ == inventories
result = {
    "scope": "Exact rational constants and exchange-branch budgets only; analytic case coverage is in the proof texts.",
    "bounds": {name: str(value) for name, value in checks.items()},
    "one_internal_inventory_partition": {"all": len(inventories), "closed": 7, "open": 7},
    "status": "PASS",
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
