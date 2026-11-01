#!/usr/bin/env python3
"""Exact budget arithmetic only: no hypergraph, layout or catalogue search."""
from fractions import Fraction
from math import ceil, comb
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
rows = []
for M in range(35, 40):
    maximum = max(v for v in range(2, 50) if v * ceil((v - 1) / 4) <= 5 * M)
    for v in range(24, 28):
        a = ceil((v - 1) / 4)
        excess = 5 * M - v * a
        row = {
            "M": M, "target_lower_bound": M + 1, "v": v,
            "minimum_degree": a, "degree_excess_over_minimum": excess,
            "pair_excess": 10 * M - comb(v, 2),
            "excluded_by_integer_degree_bound": excess < 0,
            "global_max_v_from_degree_bound": maximum,
        }
        if v in (24, 25):
            C = 8 * v - 5 * M
            row["twice_six_count_plus_seven_count_at_least"] = C
            row["degree_6_7_matching_locks_guaranteed"] = max(0, ceil(C / 3))
        elif excess >= 0:
            low = max(0, v - excess)
            epsilon = 4 * 7 - (v - 1)
            row["seven_degree_count_at_least"] = low
            row["seven_degree_matching_locks_guaranteed"] = ceil(low / 2)
            row["seven_degree_unit_locks_greedy"] = ceil(low / (epsilon + 1))
        rows.append(row)

fractions = {
    "v27_M38_unit_locks": Fraction(26**2, 26 + 2 * 23),
    "v26_M37_one_high_unit_locks": Fraction(25**2, 25 + 2 * 30),
    "v26_M37_two_high_unit_locks": Fraction(24**2, 24 + 2 * 34),
    "v26_M37_three_high_small_internal_unit_locks": Fraction(23**2, 23 + 2 * 26),
    "v27_M39_one_high_unit_locks": Fraction(26**2, 26 + 2 * 13),
}
assert ceil(fractions["v27_M38_unit_locks"]) == 10
assert ceil(fractions["v26_M37_one_high_unit_locks"]) == 8
assert ceil(fractions["v26_M37_two_high_unit_locks"]) == 7
assert ceil(fractions["v26_M37_three_high_small_internal_unit_locks"]) == 8
assert ceil(fractions["v27_M39_one_high_unit_locks"]) == 13

# Coefficients of high-trace masses t3,t4,t5 for ten unit degree-seven locks.
# Elimination is a symbolic linear identity; coefficient checks do not assert
# any chosen trace inventory can be realized by a hypergraph.
for a, b, c in [(0,0,0),(1,0,0),(0,1,0),(0,0,1)]:
    t2 = 45 - 3*a - 6*b - 10*c
    t1 = -20 + 3*a + 8*b + 15*c
    t0 = 13 - a - 3*b - 6*c
    t = [t0,t1,t2,a,b,c]
    assert sum(t) == 38
    assert sum(j*t[j] for j in range(6)) == 70
    assert sum(comb(j,2)*t[j] for j in range(6)) == 45

low_table = []
for r in range(7):
    t = max(0,25-2*r)
    low_table.append({"six_count":r,"seven_count_at_least":t,
        "unit_locks_guaranteed":r+ceil(t/5),
        "matching_locks_guaranteed":max(r,ceil((25+r)/3))})

result = {
    "date":"2026-10-15",
    "scope":"24..27 vertices, 35..39 edges, pair-covering simple 5-uniform hypergraphs",
    "status":"paper structural lemmas proved as stated; no new Property B theorem",
    "lean_ran":False,
    "hypergraph_or_layout_search_ran":False,
    "cross_model_review_of_this_report":"not yet performed",
    "arithmetic":"PASS",
    "parameter_rows":rows,
    "v25_M35_low_count_table":low_table,
    "exact_independence_bounds":{
        k:{"fraction":str(v),"ceil":ceil(v)} for k,v in fractions.items()
    },
    "paper_results":[
        "M35,v25 universally has nine degree6/7 matching locks",
        "M38,v27 has ten pairwise-unit degree7 locks",
        "M38,v27 different edges intersect in at most three vertices",
        "M38,v27 degree7 link has exactly the two stated multiplicity-defect patterns",
        "actual singleton-slot collision inequality for arbitrary q",
        "actual deletion-projection trace-moment identity for arbitrary h",
    ],
    "unresolved":[
        "new-parameter probability strictness",
        "complete actual local input coverage for new locked configurations",
        "all vertex-count branches and original target assembly",
        "independent mathematical review of the new paper lemmas",
    ],
    "old_lean_checkpoint":"context/propertyb34/round02/twentyfour/PAUSE_CHECKPOINT_20261015.md",
}
(ROOT / "SUMMARY.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print("Exact budget/moment arithmetic PASS; SUMMARY.json written. No Lean or search run.")
