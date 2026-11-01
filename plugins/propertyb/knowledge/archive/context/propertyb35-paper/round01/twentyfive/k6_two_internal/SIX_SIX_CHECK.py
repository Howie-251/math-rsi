"""Exact arithmetic checks; the theorem's domain coverage is analytic."""
from fractions import Fraction as F
import json
from pathlib import Path

p, q = F(7, 16), F(1, 4)
a3, a4 = (p**3-q**3)/3, (p**4-q**4)/4
low = 6*q**3 + 35*q**4 + 18*a3 + 42*a4
assert low == F(128821, 131072) < 1
# Independently optimize all integer budget allocations, instead of assuming
# that triples receive the budget first.
allocation_max = max(6*q**3 + 35*q**4 + j3*a3 + j4*a4
                     for j3 in range(19) for j4 in range(141)
                     if j3+j4 <= 60)
assert allocation_max == low
remaining = []
for r in range(2):
    for b in range(2-r):
        four_candidate_bad = 4*r + (2-r) + b
        five_candidate_bad = 16*r + 4*(2-r) + 4*b + (35-b)
        assert four_candidate_bad <= 5 < 9
        assert five_candidate_bad <= 55 < 108
        remaining.append({"r": r, "b": b,
                          "four_candidate_bad": four_candidate_bad,
                          "five_candidate_bad": five_candidate_bad})
assert 6*4+4 == 28 < 64
assert 3 < 16 and 4 < 16 and 1 < 3 and 1 < 4
caller = []
for s in range(7):
    m = 6-s
    row = {"q_degree": 8, "q_internal_degree": 2,
           "q_pair_trace_degree": s, "positive_four_sets": m,
           "negative_triples": 6-s, "negative_four_sets": 27-m}
    assert 0 <= m <= 6 and row["negative_triples"] <= 6
    assert row["negative_four_sets"] <= 35
    assert 2+s+m == 8
    caller.append(row)
result = {"scope": "Fraction and finite count checks for an analytic signed-set lemma; no H enumeration.",
          "low_occurrence_bound": str(low),
          "independent_integer_allocation_max": str(allocation_max),
          "remaining_negative_budgets": remaining,
          "actual_pure_pair_caller_counts": caller, "status": "PASS"}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
