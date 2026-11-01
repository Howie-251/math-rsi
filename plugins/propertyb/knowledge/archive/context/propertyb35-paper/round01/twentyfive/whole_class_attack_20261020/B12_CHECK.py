"""Exact role arithmetic for B12_TRANSFER; not an enumeration of H."""
from itertools import combinations
import json
from pathlib import Path
from time import process_time

start = process_time()
baseline, survivors = [], []
for ell in (2, 3):
    for c in range(1, 7):
        for extra in (0, 1):
            high = 1 + c + extra - ell
            if high < 0 or 3 * high > 2 * c:
                continue
            row = [ell, c, extra, high]
            baseline.append(row)
            if extra == 0:
                if high < 2:
                    continue
                price = 3 * high + 2 if ell == 2 else 5 * high
            else:
                price = 3 * high if ell == 2 else 5 * high
            if price <= 2 * c:
                survivors.append(row)
assert survivors == [[3, 1, 1, 0]]

# Role 0 is the unique double owner, 1..9 are single owners.
owner_subsets = [set(t) for size in (1, 2)
                 for t in combinations(range(1, 10), size)]
trials = valid = 0
for pair in combinations(range(10), 2):
    outside = set(pair)
    for first in owner_subsets:
        for second in owner_subsets:
            trials += 1
            if first & second or not (first <= outside and second <= outside):
                continue
            valid += 1
            assert len(first) == len(second) == 1 and 0 not in outside
assert trials == 91125 and valid == 72

result = {
    "status": "PASS",
    "scope": "25 vertices, b12/u0/N2=3 selected unique-low-bad-edge source",
    "whole_twentyfive_branch_claimed": False,
    "review_independence": "same-family",
    "acceptance_status": "provisional",
    "baseline_role_rows": baseline,
    "price_survivors": survivors,
    "owner_role_trials": trials,
    "owner_valid_projections": valid,
    "all_owner_projections_force": ["both P sets singletons", "z not in X"],
    "new_probability_layouts": 0,
    "hypergraphs_enumerated": 0,
    "cpu_seconds": process_time() - start,
}
Path(__file__).with_name("B12_RESULT.json").write_text(
    json.dumps(result, indent=2) + "\n"
)
print(json.dumps(result))
