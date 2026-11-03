"""Two fixed parameter arithmetic checks; zero graph/candidate evaluations."""
import itertools
import json
from pathlib import Path
from time import process_time

HERE = Path(__file__).parent
started = process_time()


def check_group(q, r, c):
    m = q - 1
    power = [pow(c, j, q) for j in range(m)]
    assert len(set(power)) == m
    kvals = [(b, j) for j in range(m) for b in range(q)]

    def kmul(k, ell):
        b, j = k
        d, t = ell
        return ((b + power[((r - 1) * j) % m] * d) % q, (j + t) % m)

    def action(k, x):
        b, j = k
        u, v = x
        return ((power[r * j % m] * u + b * power[j] * v) % q, power[j] * v % q)

    def enc(u, v, b, j):
        # Full G encoding, with w=0 here: u+q*v+q^2*w+3*q^2*(b+q*j).
        return u + q * v + 3 * q * q * (b + q * j)

    def dec(g):
        x, k = g % (3 * q * q), g // (3 * q * q)
        return x % q, x // q % q, k % q, k // q

    def inverse(g):
        u, v, b, j = dec(g)
        ji = -j % m
        bi = -power[(r - 1) * ji % m] * b % q
        y = action((bi, ji), (-u, -v))
        return enc(*y, bi, ji)

    def color(g):
        u, v, _, _ = dec(g)
        return "offaxis" if v else ("axis" if u else "zero")

    for k in kvals:
        for ell in kvals:
            for x in ((1, 0), (0, 1)):
                assert action(kmul(k, ell), x) == action(k, action(ell, x))
    unseen = {(u, v) for u in range(q) for v in range(q)}
    orbit_sizes = []
    while unseen:
        x = min(unseen)
        orbit = {action(k, x) for k in kvals}
        orbit_sizes.append(len(orbit))
        unseen -= orbit
    assert sorted(orbit_sizes) == [1, q - 1, q * (q - 1)]

    involutions = {s: [] for s in ("zero", "axis", "offaxis")}
    pairs = {s: [] for s in involutions}
    for u in range(q):
        for v in range(q):
            for b, j in kvals:
                g = enc(u, v, b, j)
                gi = inverse(g)
                assert inverse(gi) == g
                ui, vi, bi, ji = dec(gi)
                y = action((b, j), (ui, vi))
                assert ((u + y[0]) % q, (v + y[1]) % q) == (0, 0)
                assert kmul((b, j), (bi, ji)) == (0, 0)
                if g == 0:
                    continue
                assert color(g) == color(gi)
                if g == gi:
                    assert (b, j) == (0, m // 2)
                    involutions[color(g)].append(g)
                elif g < gi:
                    pairs[color(g)].append((g, gi))
    for table in (involutions, pairs):
        for values in table.values():
            values.sort()
    result = {
        "q": q, "r": r, "c": c, "K_order": q * m, "H_order": q,
        "K_is_abelian": all(kmul(k, ell) == kmul(ell, k) for k in kvals for ell in kvals),
        "field_orbit_sizes": sorted(orbit_sizes),
        "G0_order": q ** 3 * m,
        "G0_involution_counts": {k: len(v) for k, v in involutions.items()},
        "G0_inverse_pair_counts": {k: len(v) for k, v in pairs.items()},
        "G0_involutions_total": sum(map(len, involutions.values())),
        "G0_inverse_pairs_total": sum(map(len, pairs.values())),
        "layers": {"leaf": 3 * q ** 3 * m, "block": 3 * q * q * m, "head": 3 * q * q},
        "n": 3 * q ** 4, "degree": q + 1,
    }
    return result, involutions, pairs, dec


r1, involutions, pairs, dec = check_group(7, 1, 3)
assert r1["G0_inverse_pair_counts"] == {"zero": 20, "axis": 123, "offaxis": 861}
q11, _, _, _ = check_group(11, 3, 2)
assert q11["G0_inverse_pair_counts"] == {"zero": 54, "axis": 545, "offaxis": 5995}
assert q11["G0_involutions_total"] == 121 and q11["G0_inverse_pairs_total"] == 6594

internal = [[], [], [], [], []]
for p in pairs["axis"]:
    for t in involutions["offaxis"]:
        internal[0].append((*p, t))
for p in pairs["offaxis"]:
    for t in involutions["axis"]:
        internal[1].append((*p, t))
for a, b in itertools.combinations(involutions["axis"], 2):
    for c in involutions["offaxis"]:
        internal[2].append((a, b, c))
for a in involutions["axis"]:
    for b, c in itertools.combinations(involutions["offaxis"], 2):
        internal[3].append((a, b, c))
for a in involutions["axis"]:
    for b in involutions["offaxis"]:
        for c in involutions["zero"]:
            internal[4].append((a, b, c))
assert list(map(len, internal)) == [5166, 5166, 630, 5166, 252]
assert len({tuple(sorted(s)) for branch in internal for s in branch}) == 16380

allowed_data = json.loads((HERE / "QUOTIENT_BB_ALLOWED.json").read_text())
allowed = set(map(tuple, allowed_data["allowed_unique_projected_S"]))
assert len(allowed) == 16


def qenc(v, w, j):
    return v % 7 + 7 * (w % 3) + 21 * (j % 6)


def qinv(g):
    v, w, j = g % 7, g // 7 % 3, g // 21
    return qenc(-pow(3, -j % 6, 7) * v, -w, -j)


cross = []
for ja in range(6):
    for jb in range(6):
        a, b = qenc(0, 1, ja), qenc(1, 1, jb)
        cross.append({a, qinv(a), b, qinv(b)})
branch_counts = []
for branch_id, options in enumerate(internal):
    hits = 0
    for s in options:
        projected = {qenc(dec(g)[1], 0, dec(g)[3]) for g in s}
        for cs in cross:
            hits += tuple(sorted(projected | cs)) in allowed
    branch_counts.append({"branch": branch_id, "actual_internal_options": len(options),
                          "completed_projection_keys": 36 * len(options), "passing_projection_keys": hits,
                          "passing_full_normalized_inputs": 49 * hits})
assert [row["passing_full_normalized_inputs"] for row in branch_counts] == [28812, 86436, 0, 115248, 0]
r1["newly_generated_internal_options"] = 16380
r1["completed_projection_keys"] = 589680
r1["allowed_unique_projected_S_count"] = 16
r1["branches"] = branch_counts
r1["passing_full_normalized_inputs"] = sum(row["passing_full_normalized_inputs"] for row in branch_counts)
r1["old_r5_internal_indices_reused"] = False
result = {
    "status": "COMPLETE_PARAMETER_ARITHMETIC_ONLY",
    "q7_r1": r1,
    "q11_r3": q11,
    "q11_allowed_nonzero_w_inverse_pair_counts_from_HH": [2, 3, 4],
    "q11_two_cross_pair_internal_patterns": ["3 pairs + 1 involution", "2 pairs + 3 involutions",
                                              "1 pair + 5 involutions", "7 involutions"],
    "candidate_graphs_generated": 0,
    "original_BB_evaluations": 0,
    "BFS_runs": 0,
    "q11_generating_sets_enumerated": 0,
    "cpu_seconds": process_time() - started,
}
(HERE / "HEAD_TRIANGLE_PARAMETER_EXTENSION.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
