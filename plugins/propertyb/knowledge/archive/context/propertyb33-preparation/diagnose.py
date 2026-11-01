"""Small exact-arithmetic diagnostics for the proposed 33-edge problem.

No hypergraph search and no new theorem claim. Imports the existing arithmetic
engine without modifying its source or creating bytecode beside it.
Run: python3 context/propertyb33-preparation/diagnose.py
"""
from fractions import Fraction
from math import comb
from pathlib import Path
import json
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations"))
from multilock import Profile, rows, total_bound, link_certificate, link_q_lower


def profile_result(name, profile, centers=()):
    certificates = []
    for j in centers:
        degree = sum(c for t, c in profile.counts.items() if t & (1 << j))
        certificates.append(link_certificate(
            profile, j, link_q_lower(profile.v, profile.n, degree)
        ))
    deductions = {c["position"]: c["deduction"] for c in certificates}
    return {
        "name": name,
        "v": profile.v,
        "uniformity": profile.n,
        "positions": profile.positions,
        "counts_by_mask": profile.counts,
        "edge_count": sum(profile.counts.values()),
        "base_bound": str(total_bound(rows(profile))),
        "corrected_bound": str(total_bound(rows(profile, deductions=deductions))),
        "link_deductions": [
            {"center": c["center"], "position": c["position"],
             "q_lower": c["q_lower"], "deduction": str(c["deduction"])}
            for c in certificates
        ],
    }


balanced = {
    v: str(Fraction(33 * (comb(v // 2, 5) + comb(v - v // 2, 5)), comb(v, 5)))
    for v in range(9, 19)
}
assert all(Fraction(q) < 1 for q in balanced.values())
assert balanced[18] == "33/34"

cases = [profile_result("v19_no_locks", Profile(19, 5, (), {0: 33}))]
for degree in (5, 6, 7):
    cases.append(profile_result(
        f"v21_degree_{degree}",
        Profile(21, 5, (11,), {0: 33 - degree, 1: degree}), (0,)
    ))
cases.append(profile_result(
    "v23_degrees_6_6_codegree_1",
    Profile(23, 5, (11, 12), {0: 22, 1: 5, 2: 5, 3: 1}), (0, 1)
))
assert [c["corrected_bound"] for c in cases] == [
    "1239/1235", "4242/4199", "651/646", "4305/4199", "60951/58786"
]

result = {
    "scope": "33-edge arithmetic diagnostics; not a proof or a counterexample",
    "balanced_coloring_union_bounds": balanced,
    "integer_degree_obstruction_at_26": {
        "pair_count_lower": comb(26, 2), "pair_incidence_budget": 33 * comb(5, 2),
        "minimum_degree": (26 - 1 + 3) // 4,
        "total_degree_lower": 26 * ((26 - 1 + 3) // 4),
        "total_degree_budget": 5 * 33,
    },
    "six_degree_vertex_budget_lower_bounds": {
        v: max(0, 7 * v - 5 * 33) for v in (23, 24, 25)
    },
    "profiles": cases,
}
print(json.dumps(result, ensure_ascii=False, indent=2))
