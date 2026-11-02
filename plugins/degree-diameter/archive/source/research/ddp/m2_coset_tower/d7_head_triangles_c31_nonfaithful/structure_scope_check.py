"""Order-15 action on the fixed c31 triangle tower: arithmetic only, no graphs."""
import json
from collections import Counter
from pathlib import Path
from time import process_time

started = process_time()
HERE = Path(__file__).parent
P, R, M = 31, 9, 30
powers = [pow(R, j, P) for j in range(M)]
Q = set(powers)
N = set(range(1, P)) - Q
assert len(Q) == len(N) == 15 and pow(R, 15, P) == 1
assert all(pow(R, j, P) != 1 for j in range(1, 15))
assert P - 1 in N
assert {(-x) % P for x in Q} == N


def enc(x, w, j):
    return x % P + P * (w % 3) + 3 * P * (j % M)


def dec(g):
    return g % P, g // P % 3, g // (3 * P)


def inverse(g):
    x, w, j = dec(g)
    return enc(-powers[-j % M] * x, -w, -j)


def multiply(g, h):
    x, w, j = dec(g)
    y, v, k = dec(h)
    return enc(x + powers[j] * y, w + v, j + k)


def color(x):
    return "zero" if x == 0 else ("Q" if x in Q else "N")


involutions = []
pairs = {"zero": [], "nonzero_both_colors": []}
for x in range(P):
    for j in range(M):
        g = enc(x, 0, j)
        gi = inverse(g)
        assert multiply(g, gi) == multiply(gi, g) == 0 and inverse(gi) == g
        if g == 0:
            continue
        xi = dec(gi)[0]
        if x:
            assert {color(x), color(xi)} == {"Q", "N"}
        if g == gi:
            involutions.append(g)
        elif g < gi:
            pairs["zero" if x == 0 else "nonzero_both_colors"].append((g, gi))
assert involutions == [enc(0, 0, 15)]
assert [len(v) for v in pairs.values()] == [14, 450]

z = enc(0, 0, 15)
H_exponents = [(5 * j) % 30 for j in range(6)]
assert 15 in H_exponents
for g in range(2790):
    zg = multiply(z, g)
    assert zg == multiply(g, z) and zg != g
    x, w, j = dec(g)
    xz, wz, jz = dec(zg)
    assert (xz, wz, jz % 5) == (x, w, j % 5)
    assert (xz, wz) == (x, w)

normalizations = 0
for x in range(1, P):
    for y in range(1, P):
        if color(x) == color(y):
            continue
        assert y * pow(x, -1, P) % P in N
        normalizations += 1
assert normalizations == 450
count = 30 * 15 * 30 * 450
assert count == 6075000

def quotient_code(g):
    x, w, j = dec(g)
    return x + P * w + 3 * P * (j % 15)


quotient_pairs = {"zero": set(), "nonzero": set()}
for x in range(P):
    for j in range(15):
        g = enc(x, 0, j)
        a, b = quotient_code(g), quotient_code(inverse(g))
        if a:
            assert a != b
            quotient_pairs["zero" if x == 0 else "nonzero"].add(tuple(sorted((a, b))))
assert [len(value) for value in quotient_pairs.values()] == [7, 225]
nonzero_pair_fibers = Counter(tuple(sorted((quotient_code(g), quotient_code(h))))
                             for g, h in pairs["nonzero_both_colors"])
assert len(nonzero_pair_fibers) == 225 and set(nonzero_pair_fibers.values()) == {2}
quotient_keys = 15 * 15 * 15 * 225
reduced_quotient_keys = 8 * 15 * 15 * 225
assert quotient_keys == 759375 and quotient_keys * 8 == count
assert reduced_quotient_keys == 405000 and reduced_quotient_keys * 8 == 3240000
assert {min(j, -j % 15) for j in range(15)} == set(range(8))
result = {
    "status": "COMPLETE_NONFAITHFUL_C31_SCOPE_ARITHMETIC_ONLY",
    "p": 31, "action_root": 9, "action_order": 15,
    "K_order": 30, "H_order": 6, "K_over_H_order": 5,
    "H_exponents": H_exponents,
    "H_action_image_order": len({powers[j] for j in H_exponents}),
    "nonzero_K_orbits": {"Q": sorted(Q), "N": sorted(N)},
    "inverse_swaps_nonzero_colors": True,
    "G0_order": 930,
    "G0_nonidentity_involutions": len(involutions),
    "G0_involution_coordinates": [dec(g) for g in involutions],
    "G0_inverse_pairs": 464,
    "G0_zero_inverse_pairs": len(pairs["zero"]),
    "G0_nonzero_inverse_pairs": len(pairs["nonzero_both_colors"]),
    "HH_forced_cross_inverse_pairs": 2,
    "HH_forced_internal_nonzero_inverse_pairs": 1,
    "normalized_marked_inputs": count,
    "count_factors": {"marked_anchor_index": 30, "second_w1_field_values": 15,
                      "second_w1_index": 30, "internal_nonzero_inverse_pairs": 450},
    "central_kernel_element": [0, 0, 15],
    "original_layers": {"leaves": 2790, "blocks": 465, "heads": 93},
    "original_n": 3348, "original_degree": 7,
    "central_quotient_layers": {"leaves": 1395, "blocks": 465, "heads": 93},
    "central_quotient_vertex_count": 1953,
    "central_quotient_G0_order": 465,
    "central_quotient_G0_nonidentity_involutions": 0,
    "central_quotient_G0_inverse_pairs": {"zero": 7, "nonzero": 225},
    "normalized_quotient_keys": quotient_keys,
    "independent_component_lifts_per_quotient_key": 8,
    "all_nonzero_internal_quotient_pairs_have_exactly_two_original_pair_lifts": True,
    "optional_quotient_anchor_inversion_representatives": list(range(8)),
    "optional_quotient_anchor_inversion_fixed_exponents": [0],
    "optional_reduced_quotient_keys": reduced_quotient_keys,
    "optional_reduced_original_lifted_inputs": reduced_quotient_keys * 8,
    "central_quotient_distances_exact_if_an_endpoint_is_block_or_head": True,
    "central_quotient_LL_distance_is_minimum_over_two_leaf_lifts": True,
    "old_one_inverse_pair_capacity_lemma_applicable": False,
    "complete_generating_sets_enumerated": 0,
    "graphs_generated": 0, "BFS_runs": 0,
    "cpu_seconds": process_time() - started,
}
(HERE / "STRUCTURE_SCOPE.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
