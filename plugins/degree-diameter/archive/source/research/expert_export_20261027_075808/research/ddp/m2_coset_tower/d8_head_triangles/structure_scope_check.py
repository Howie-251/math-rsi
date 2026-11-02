"""Small group/normalization arithmetic only; no generating-set or graph search."""
import json
import math
from pathlib import Path
from time import process_time

started = process_time()
MOD = 7
C = 3
K = [(b, j) for j in range(6) for b in range(7)]
V = [(u, v) for u in range(7) for v in range(7)]


def kmul(k, l):
    b, j = k
    d, ell = l
    return ((b + pow(C, 4 * j, MOD) * d) % MOD, (j + ell) % 6)


def kinv(k):
    b, j = k
    return ((-pow(C, (-4 * j) % 6, MOD) * b) % MOD, -j % 6)


def act(k, x):
    b, j = k
    u, v = x
    return ((pow(C, 5 * j, MOD) * u + b * pow(C, j, MOD) * v) % MOD,
            pow(C, j, MOD) * v % MOD)


def mul(g, h):
    u, v, b, j = g
    z, t, d, ell = h
    y = act((b, j), (z, t))
    k = kmul((b, j), (d, ell))
    return ((u + y[0]) % MOD, (v + y[1]) % MOD, *k)


def inv(g):
    u, v, b, j = g
    k = kinv((b, j))
    return (*act(k, (-u, -v)), *k)


def color(x):
    u, v = x[:2]
    return "O42" if v else ("O6" if u else "zero")


def t_act(t, x):
    p, q, r = t
    u, v = x
    return ((p * u + q * v) % MOD, r * v % MOD)


def conjugate_k(t, k):
    p, q, r = t
    b, j = k
    rinv = pow(r, -1, MOD)
    return ((rinv * (p * b + q * (1 - pow(C, 4 * j, MOD)))) % MOD, j)


assert {pow(C, j, MOD) for j in range(6)} == set(range(1, 7))
for k in K:
    assert kmul(k, kinv(k)) == kmul(kinv(k), k) == (0, 0)
    for ell in K:
        for x in ((1, 0), (0, 1)):
            assert act(kmul(k, ell), x) == act(k, act(ell, x))

orbits = []
unseen = set(V)
while unseen:
    x = min(unseen)
    orbit = {act(k, x) for k in K}
    orbits.append({"representative": x, "size": len(orbit), "color": color(x)})
    unseen -= orbit
assert sorted(o["size"] for o in orbits) == [1, 6, 42]

identity = (0, 0, 0, 0)
involutions = []
pairs = []
counts = {name: {"involutions": 0, "inverse_pairs": 0} for name in ("zero", "O6", "O42")}
for u, v in V:
    for b, j in K:
        g = (u, v, b, j)
        gi = inv(g)
        assert mul(g, gi) == mul(gi, g) == identity
        assert color(g) == color(gi)
        if g == identity:
            continue
        if g == gi:
            involutions.append(g)
            counts[color(g)]["involutions"] += 1
        elif g < gi:
            pairs.append((g, gi))
            counts[color(g)]["inverse_pairs"] += 1
assert len(involutions) == 49 and len(pairs) == 1004
assert set(involutions) == {(u, v, 0, 3) for u, v in V}
assert counts == {
    "zero": {"involutions": 1, "inverse_pairs": 20},
    "O6": {"involutions": 6, "inverse_pairs": 123},
    "O42": {"involutions": 42, "inverse_pairs": 861},
}

borel = [(p, q, r) for p in range(1, 7) for q in range(7) for r in range(1, 7)]
for t in borel:
    for k in K:
        ck = conjugate_k(t, k)
        assert ck in K
        if k[1] == 0:
            assert ck[1] == 0
        for x in ((1, 0), (0, 1)):
            assert t_act(t, act(k, x)) == act(ck, t_act(t, x))
normalization_cases = 0
for alpha in range(1, 7):
    for beta in range(7):
        for gamma in range(1, 7):
            t = (pow(alpha, -1, MOD), -beta * pow(alpha * gamma % MOD, -1, MOD) % MOD,
                 pow(gamma, -1, MOD))
            assert t_act(t, (alpha, 0)) == (1, 0)
            assert t_act(t, (beta, gamma)) == (0, 1)
            # This also checks uniqueness in the complete 252-element Borel group.
            assert sum(t_act(z, (alpha, 0)) == (1, 0) and
                       t_act(z, (beta, gamma)) == (0, 1) for z in borel) == 1
            normalization_cases += 1

internal_pair_involution = 123 * 42 + 861 * 6
internal_three_involutions = math.comb(49, 3) - math.comb(43, 3) - math.comb(7, 3)
assert (internal_pair_involution, internal_three_involutions) == (10332, 6048)
normalized_pair_involution = 42 ** 2 * internal_pair_involution
normalized_three_involutions = 42 ** 2 * internal_three_involutions
normalized_total = normalized_pair_involution + normalized_three_involutions
assert normalized_total == 28894320
raw_hh_total = (6 * 42) * (42 * 42) * (internal_pair_involution + internal_three_involutions)
assert raw_hh_total == 252 * normalized_total

result = {
    "status": "COMPLETE_SMALL_ARITHMETIC_ONLY",
    "candidate_generating_sets_enumerated": 0,
    "candidate_graphs_generated": 0,
    "K_order": 42,
    "H_order": 7,
    "G0_order": 2058,
    "G_order": 6174,
    "tower_vertices": {"leaves": 6174, "blocks": 882, "heads": 147, "total": 7203},
    "degree": 8,
    "K_orbits_on_F7_squared": orbits,
    "G0_inverse_component_counts": counts,
    "G0_involutions": 49,
    "G0_noninvolution_inverse_pairs": 1004,
    "full_G_involutions": 49,
    "full_G_noninvolution_inverse_pairs": 3062,
    "Borel_order": len(borel),
    "joint_vector_normalizations_checked": normalization_cases,
    "internal_pair_involution": internal_pair_involution,
    "internal_three_involutions": internal_three_involutions,
    "normalized_pair_involution_inputs": normalized_pair_involution,
    "normalized_three_involution_inputs": normalized_three_involutions,
    "normalized_HH_inputs": normalized_total,
    "raw_HH_generating_sets": raw_hh_total,
    "cpu_seconds": process_time() - started,
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
