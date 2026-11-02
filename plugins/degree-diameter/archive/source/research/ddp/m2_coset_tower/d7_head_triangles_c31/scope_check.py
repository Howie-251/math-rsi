"""c31 HH scope arithmetic only; no generating-set enumeration or graph work."""
import json
import math
from pathlib import Path
from time import process_time

started = process_time()
HERE = Path(__file__).parent
P, R, K_ORDER, H_ORDER = 31, 3, 30, 6
powers = [pow(R, j, P) for j in range(K_ORDER)]
assert set(powers) == set(range(1, P))


def enc(x, w, j):
    return x % P + P * (w % 3) + 3 * P * (j % K_ORDER)


def dec(g):
    return g % P, g // P % 3, g // (3 * P)


def inv(g):
    x, w, j = dec(g)
    return enc(-powers[-j % K_ORDER] * x, -w, -j)


def multiply(g, h):
    x, w, j = dec(g)
    y, v, k = dec(h)
    return enc(x + powers[j] * y, w + v, j + k)


invol = {"zero": [], "nonzero": []}
pairs = {"zero": [], "nonzero": []}
for x in range(P):
    for j in range(K_ORDER):
        g = enc(x, 0, j)
        gi = inv(g)
        assert multiply(g, gi) == multiply(gi, g) == 0 and inv(gi) == g
        if g == 0:
            continue
        color = "zero" if x == 0 else "nonzero"
        assert (dec(gi)[0] == 0) == (x == 0)
        if g == gi:
            assert j == 15
            invol[color].append(g)
        elif g < gi:
            pairs[color].append((g, gi))
assert [len(invol[k]) for k in invol] == [1, 30]
assert [len(pairs[k]) for k in pairs] == [14, 435]

branches = [
    {"t": 1, "internal_pairs": 2, "internal_involutions": 0,
     "HH_internal_choices": math.comb(449, 2) - math.comb(14, 2)},
    {"t": 1, "internal_pairs": 1, "internal_involutions": 2,
     "HH_internal_choices": 449 * math.comb(31, 2)},
    {"t": 1, "internal_pairs": 0, "internal_involutions": 4,
     "HH_internal_choices": math.comb(31, 4)},
    {"t": 2, "internal_pairs": 1, "internal_involutions": 0,
     "HH_internal_choices": 435},
    {"t": 2, "internal_pairs": 0, "internal_involutions": 2,
     "HH_internal_choices": math.comb(31, 2)},
]
for row in branches:
    row["normalized_cross_marked_choices"] = 30 if row["t"] == 1 else 30 * 929
    row["normalized_marked_inputs"] = row["HH_internal_choices"] * row["normalized_cross_marked_choices"]
t1 = sum(row["normalized_marked_inputs"] for row in branches if row["t"] == 1)
t2 = sum(row["normalized_marked_inputs"] for row in branches if row["t"] == 2)
assert (t1, t2, t1 + t2) == (10222050, 25083000, 35305050)

# Optional central inversion plus field scaling: after reorienting the marked
# inverse pair to w=1, its exponent is -j. This checks all 30 anchor exponents.
for j in range(30):
    scale = -powers[j] % P
    transformed_anchor = enc(scale, -1, j)
    assert inv(transformed_anchor) == enc(1, 1, -j)
    assert (-powers[-j % 30] * scale) % P == 1
representatives = list(range(16))
assert {min(j, -j % 30) for j in range(30)} == set(representatives)

output = {
    "status": "COMPLETE_HH_MARKED_SCOPE_ARITHMETIC_ONLY",
    "p": 31, "primitive_root": 3, "degree": 7, "n": 3348,
    "K_order": 30, "H_order": 6, "H_exponent_generator": 5,
    "layer_sizes": {"leaves": 2790, "blocks": 465, "heads": 93},
    "group_encoding": "x+31*w+93*j",
    "G0_order": 930,
    "G0_involution_counts": {key: len(value) for key, value in invol.items()},
    "G0_inverse_pair_counts": {key: len(value) for key, value in pairs.items()},
    "w1_representatives_total": 930,
    "w1_nonzero_field_representatives": 900,
    "w1_zero_field_representatives": 30,
    "HH_allowed_t": [1, 2],
    "HH_excluded_t": {"0": "no nonzero-field coverage in w=1,2", "3": "no internal nonzero-field element"},
    "branches": branches,
    "t1_normalized_inputs": t1,
    "t2_normalized_marked_inputs": t2,
    "total_normalized_marked_inputs": t1 + t2,
    "t2_same_unmarked_set_may_have_multiple_markings": True,
    "optional_anchor_inversion_representatives": representatives,
    "optional_anchor_inversion_fixed_exponents": [0, 15],
    "optional_safe_16_slice_counts_not_used_in_main_scope": {
        "t1": 16 * (t1 // 30), "t2": 16 * (t2 // 30), "total": 16 * ((t1 + t2) // 30)},
    "unconditional_division_by_two_claimed": False,
    "complete_generating_sets_enumerated": 0,
    "graphs_generated": 0, "BFS_runs": 0,
    "cpu_seconds": process_time() - started,
}
(HERE / "SCOPE.json").write_text(json.dumps(output, indent=2) + "\n")
print(json.dumps(output, indent=2))
