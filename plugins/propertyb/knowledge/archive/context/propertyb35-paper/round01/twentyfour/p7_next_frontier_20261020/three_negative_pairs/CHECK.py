"""Scalar checks only: indexed q_x, forbidden-set sizes, and actual J totals."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json

directory = Path(__file__).parent
disjoint = []
for q in range(4):
    b3 = Fraction(24) + Fraction(10, 3) * q
    b4 = Fraction(128) + Fraction(40, 3) * q
    assert b3 < 64 and b4 < 256
    disjoint.append(dict(pair_indices=q, three_group_bound=str(b3),
                         four_group_bound=str(b4)))

rows = []
for q_x in range(4):
    for f_size in range(q_x + 1):
        for alpha, beta in product(range(f_size + 1), repeat=2):
            # alpha,beta are removals from two original four-sets.
            a, b = 4 - alpha, 4 - beta
            candidates = a * b
            block_bound = 8 - 2 * q_x
            rescue = None
            if q_x <= 1:
                assert candidates > block_bound
            elif q_x == 2 and candidates <= block_bound:
                assert (f_size, alpha, beta, candidates) == (2, 2, 2, 4)
                assert (5 - q_x) < candidates  # A third active N2 is necessary.
                assert 1 + 4 < 9
                rescue = "F_two_common_points_and_active_third_pair"
            elif q_x == 3 and candidates <= block_bound:
                assert alpha + beta >= 5
                assert alpha + beta - f_size >= 2
                assert 4 < 9
                rescue = "F_at_least_two_common_points_all_N2_contain_x"
            rows.append(dict(q_x=q_x, distinct_forbidden_points=f_size,
                             removals=[alpha, beta], candidates=candidates,
                             block_bound=block_bound, rescue=rescue))

inventory = []
for r in range(4):
    n2, n1 = 17 - 2 * r, 17 + r
    assert 1 + n1 + n2 + r == 35
    assert 5 + n1 + 2 * n2 + 3 * r == 56
    upper, actual = 26 - 3 * r, 2 * n2
    assert actual - upper == 8 - r > 0
    inventory.append(dict(r=r, n1=n1, n2=n2, J_degree_upper=upper,
                          actual_J_degree=actual, gap=actual-upper,
                          new_whole_inventory=(r == 3)))

out = dict(status="PASS", scope="scalar bounds only; no set-system or H search",
           disjoint_group_bounds=disjoint,
           forbidden_size_rows=rows,
           forbidden_size_row_count=len(rows),
           inventory=inventory)
(directory / "CHECK.json").write_text(json.dumps(out, indent=2) + "\n")
print(dict(status="PASS", forbidden_size_rows=len(rows),
           disjoint_maximum_bounds=["34", "168"],
           inventory_gaps=[row["gap"] for row in inventory]))
