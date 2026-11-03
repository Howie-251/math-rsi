"""Small group/module arithmetic only: no generating-set or graph search."""
import json
from collections import Counter
from itertools import combinations
from math import comb
from pathlib import Path
from time import process_time

started = process_time()


def mul(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 8:
            a ^= 11
    return result


def power(a, n):
    result = 1
    while n:
        if n & 1:
            result = mul(result, a)
        a = mul(a, a)
        n >>= 1
    return result


def act(mask, permutation):
    result = 0
    for x in range(8):
        if mask >> x & 1:
            result |= 1 << permutation[x]
    return result


def syndrome(mask):
    result = 0
    for x in range(8):
        if mask >> x & 1:
            result ^= x
    return result


def label(mask):
    weight = mask.bit_count()
    if weight == 0:
        return "zero"
    if weight == 8:
        return "all_one"
    if weight in (2, 6):
        return f"weight{weight}"
    assert weight == 4
    return "affine_plane4" if syndrome(mask) == 0 else "nonplane4"


A = [mask for mask in range(256) if mask.bit_count() % 2 == 0]
K = [(a, b) for a in range(1, 8) for b in range(8)]
permutations = {(a, b): tuple(mul(a, x) ^ b for x in range(8)) for a, b in K}
permutation_to_k = {p: k for k, p in permutations.items()}
assert len(permutation_to_k) == 56
H = {(a, 0) for a in range(1, 8)}
korbits = []
unseen = set(A)
while unseen:
    root = min(unseen)
    orbit = sorted({act(root, p) for p in permutations.values()})
    assert len({label(v) for v in orbit}) == 1
    korbits.append({"label": label(root), "size": len(orbit), "members": orbit})
    unseen.difference_update(orbit)
assert sorted(o["size"] for o in korbits) == [1, 1, 14, 28, 28, 56]


def inverse(g):
    v, a, b = g
    ai = power(a, 6)
    bi = mul(ai, b)
    return act(v, permutations[(ai, bi)]), ai, bi


counts = {name: Counter() for name in [o["label"] for o in korbits]}
z_involutions = []
z_pairs = []
for v in A:
    for a, b in K:
        g = (v, a, b)
        gi = inverse(g)
        assert inverse(gi) == g
        row = counts[label(v)]
        row["elements"] += 1
        if g == (0, 1, 0):
            row["identity"] += 1
        elif gi == g:
            row["involutions"] += 1
            if v == 255:
                z_involutions.append(g)
        elif g < gi:
            row["inverse_pairs"] += 1
            if v == 255:
                z_pairs.append((g, gi))
expected = {
    "zero": (7, 24), "all_one": (8, 24), "affine_plane4": (56, 364),
    "weight2": (56, 756), "weight6": (56, 756), "nonplane4": (56, 1540),
}
assert {key: (row["involutions"], row["inverse_pairs"]) for key, row in counts.items()} == expected

C = [v for v in A if syndrome(v) == 0]
assert len(C) == 16
for a, b in K:
    for v in A:
        assert syndrome(act(v, permutations[(a, b)])) == mul(a, syndrome(v))
fixed_vectors = [v for v in A if all(act(v, p) == v for p in permutations.values())]
assert fixed_vectors == [0, 255]
basis = {}
for v in A:
    for p in permutations.values():
        w = v ^ act(v, p)
        while w:
            pivot = w.bit_length() - 1
            if pivot in basis:
                w ^= basis[pivot]
            else:
                basis[pivot] = w
                break
assert len(basis) == 7
horbits = []
unseen = set(A)
while unseen:
    root = min(unseen)
    orbit = sorted({act(root, permutations[h]) for h in H})
    horbits.append({"label": label(root), "size": len(orbit), "members": orbit})
    unseen.difference_update(orbit)
assert len(horbits) == 20

normalizers = [tuple(mul(a, power(x, 1 << e)) for x in range(8)) for a in range(1, 8) for e in range(3)]
assert len(set(normalizers)) == 21
conjugations = []
for p in normalizers:
    pinv = [0] * 8
    for x, y in enumerate(p):
        pinv[y] = x
    table = {}
    for k, kp in permutations.items():
        conjugate = tuple(p[kp[pinv[x]]] for x in range(8))
        table[k] = permutation_to_k[conjugate]
    assert {table[h] for h in H} == H
    conjugations.append((p, table))


def conjugate_element(g, automorphism):
    v, a, b = g
    p, table = automorphism
    return (act(v, p),) + table[(a, b)]


anchor_orbits = []
for component_kind, components in [("involution", z_involutions), ("inverse_pair", z_pairs)]:
    unseen = set(components)
    while unseen:
        root = min(unseen)
        if component_kind == "involution":
            orbit = {conjugate_element(root, c) for c in conjugations}
        else:
            orbit = {tuple(sorted(conjugate_element(g, c) for g in root)) for c in conjugations}
        anchor_orbits.append({"kind": component_kind, "size": len(orbit), "representative": root})
        unseen.difference_update(orbit)
assert sorted((o["kind"], o["size"]) for o in anchor_orbits) == [("inverse_pair", 3), ("inverse_pair", 21), ("involution", 1), ("involution", 7)]


def meeting_count(total, required_class_sizes, number):
    answer = 0
    for bits in range(1 << len(required_class_sizes)):
        removed = sum(size for j, size in enumerate(required_class_sizes) if bits >> j & 1)
        answer += (-1 if bits.bit_count() % 2 else 1) * comb(total - removed, number)
    return answer


other_pair_counts = [364, 756, 756, 1540]
pair_product_sum = sum(x * y for x, y in combinations(other_pair_counts, 2))
normalized_two_pair = 2 * 56**2 * pair_product_sum + 2 * 56**3 * sum(other_pair_counts)
normalized_one_pair = 2 * (sum(other_pair_counts) * meeting_count(238, [56] * 3, 4) + 48 * 56**4) + 2 * meeting_count(239, [56] * 4, 5)
normalized_zero_pair = 2 * meeting_count(238, [56] * 4, 6)
I_nonzero = [8, 56, 56, 56, 56]
P_nonzero = [24, 364, 756, 756, 1540]
raw_zero_pair = meeting_count(239, I_nonzero, 7)
raw_one_pair = 24 * meeting_count(239, I_nonzero, 5)
for j, pair_count in enumerate(P_nonzero):
    raw_one_pair += pair_count * meeting_count(239, I_nonzero[:j] + I_nonzero[j + 1:], 5)
raw_two_pair = 0
for pair_indices in combinations(range(5), 2):
    value = 1
    for j in range(5):
        value *= P_nonzero[j] if j in pair_indices else I_nonzero[j]
    raw_two_pair += value
result = {
    "status": "STRUCTURE_SCOPE_ARITHMETIC_COMPLETE_NO_GENERATOR_SET_SEARCH",
    "field_polynomial_binary": 11,
    "K_coordinates": "(a,b): x -> a*x+b over F8",
    "G_coordinates": "(even_mask,a,b)",
    "mask_bits": "field point x is bit x",
    "A_order": 128, "K_order": 56, "H_order": 7,
    "K_orbits_on_A": korbits,
    "element_counts": {key: dict(value) for key, value in counts.items()},
    "total_nonidentity_involutions": sum(row["involutions"] for row in counts.values()),
    "total_inverse_pairs": sum(row["inverse_pairs"] for row in counts.values()),
    "fixed_vectors": fixed_vectors,
    "code_C": C,
    "commutator_module_rank": len(basis),
    "H_orbits": horbits,
    "allowed_normalizer_order": 21,
    "all_one_component_normalizer_orbits": anchor_orbits,
    "HH_pass_raw_unordered_sets_by_pair_count": {0: raw_zero_pair, 1: raw_one_pair, 2: raw_two_pair, 3: 0},
    "HH_pass_anchored_inputs_with_possible_duplicates": {0: normalized_zero_pair, 1: normalized_one_pair, 2: normalized_two_pair, 3: 0},
    "cpu_seconds": process_time() - started,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({key: result[key] for key in ["status", "element_counts", "total_nonidentity_involutions", "total_inverse_pairs", "all_one_component_normalizer_orbits", "HH_pass_raw_unordered_sets_by_pair_count", "HH_pass_anchored_inputs_with_possible_duplicates", "cpu_seconds"]}, indent=2))
