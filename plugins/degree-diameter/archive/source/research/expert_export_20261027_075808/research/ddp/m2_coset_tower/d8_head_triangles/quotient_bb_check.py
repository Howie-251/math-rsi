"""Complete small quotient BB check; no full tower graphs or candidate search."""
import itertools
import json
from collections import Counter
from pathlib import Path
from time import process_time

started = process_time()
OUT = Path(__file__).parent
N = 126
POW = [pow(3, j, 7) for j in range(6)]


def enc(v, w, j):
    return v % 7 + 7 * (w % 3) + 21 * (j % 6)


def dec(g):
    return (g % 7, g // 7 % 3, g // 21)


def multiply(g, h):
    v, w, j = dec(g)
    z, t, ell = dec(h)
    return enc(v + POW[j] * z, w + t, j + ell)


TABLE = [[multiply(g, h) for h in range(N)] for g in range(N)]
INV = [enc(-POW[(-dec(g)[2]) % 6] * dec(g)[0], -dec(g)[1], -dec(g)[2])
       for g in range(N)]
assert all(TABLE[g][INV[g]] == TABLE[INV[g]][g] == 0 for g in range(N))
K = [enc(0, 0, j) for j in range(6)]
ZK = {enc(0, w, j) for w in (1, 2) for j in range(6)}


def internal_patterns():
    for j in range(6):
        for t in range(1, 7):
            p = enc(0, 0, j)
            yield "pair_A_involution_B", {"pair_index": j, "t": t}, [p, INV[p], enc(t, 0, 3)]
    for j in range(6):
        for t in range(1, 7):
            p = enc(t, 0, j)
            yield "pair_B_involution_A", {"pair_index": j, "t": t}, [p, INV[p], enc(0, 0, 3)]
    for branch in ("involutions_2A_1B", "involutions_1A_1B_zero"):
        for t in range(1, 7):
            yield branch, {"t": t}, [enc(0, 0, 3), enc(0, 0, 3), enc(t, 0, 3)]
    for t1, t2 in itertools.combinations_with_replacement(range(1, 7), 2):
        yield "involutions_1A_2B", {"t1": t1, "t2": t2}, [enc(0, 0, 3), enc(t1, 0, 3), enc(t2, 0, 3)]


cache = {}


def score(projected_generators):
    key = tuple(sorted(set(projected_generators)))
    if key in cache:
        return cache[key]
    assert {INV[g] for g in key} == set(key)
    visited = {0}
    frontier = {0}
    for _ in range(3):
        frontier = {TABLE[g][s] for g in frontier for s in key} - visited
        visited |= frontier
    w1 = set(key) | {0}
    # Direct projected exact BB formula: W3 union K W1 union W1 K union ZK.
    covered = visited | ZK
    covered |= {TABLE[k][s] for k in K for s in w1}
    covered |= {TABLE[s][k] for k in K for s in w1}
    # Check the proposed six-mask implementation against that group-set formula.
    masks = [set() for _ in range(6)]
    for word in visited:
        v, w, j = dec(word)
        masks[j].add((v, w))
    for j in range(6):
        masks[j] |= {(0, 1), (0, 2)}
        for s in w1:
            v, w, js = dec(s)
            masks[j].add((v, w))
            masks[j].add((POW[(j - js) % 6] * v % 7, w))
    assert covered == {enc(v, w, j) for j in range(6) for v, w in masks[j]}
    by_j = [21 - len(mask) for mask in masks]
    answer = (N - len(covered), by_j, tuple(g for g in range(N) if g not in covered))
    cache[key] = answer
    return answer


branches = {}
rows = []
allowed = []
minimum = N
best_patterns = []
for ja in range(6):
    for jb in range(6):
        cross_a = enc(0, 1, ja)
        cross_b = enc(1, 1, jb)
        cross = [cross_a, INV[cross_a], cross_b, INV[cross_b]]
        for branch, parameters, internal in internal_patterns():
            generators = cross + internal
            miss, by_j, missing = score(generators)
            row = {"pattern_index": len(rows), "branch": branch, "cross_a_index": ja,
                   "cross_b_index": jb, **parameters, "missing_BB": miss,
                   "missing_by_index": by_j}
            rows.append(row)
            info = branches.setdefault(branch, {"completed_patterns": 0, "BB_pass": 0,
                                               "min_missing": N, "histogram": Counter()})
            info["completed_patterns"] += 1
            info["BB_pass"] += miss == 0
            info["min_missing"] = min(info["min_missing"], miss)
            info["histogram"][miss] += 1
            if miss == 0:
                allowed.append({**row, "projected_generators_with_multiplicity": [dec(g) for g in generators]})
            if miss < minimum:
                minimum = miss
                best_patterns = []
            if miss == minimum:
                best_patterns.append({**row, "projected_generators_with_multiplicity": [dec(g) for g in generators],
                                      "missing_targets": [dec(g) for g in missing]})

assert len(rows) == 3780
assert [branches[b]["completed_patterns"] for b in branches] == [1296, 1296, 216, 216, 756]
for branch in branches.values():
    branch["histogram"] = dict(sorted(branch["histogram"].items()))
allowed_sets = sorted({tuple(sorted(set(map(tuple, row["projected_generators_with_multiplicity"]))))
                       for row in allowed})
summary = {
    "status": "COMPLETE_QUOTIENT_BB_CHECK",
    "quotient_order": N,
    "full_block_targets_per_quotient_target": 7,
    "patterns_completed": len(rows),
    "distinct_projected_generator_sets": len(cache),
    "quotient_BB_pass_patterns": len(allowed),
    "distinct_quotient_BB_pass_generator_sets": len(allowed_sets),
    "min_quotient_missing_BB": minimum,
    "implied_uniform_original_missing_BB_lower_bound": 7 * minimum,
    "branches": branches,
    "best_pattern_count": len(best_patterns),
    "best_patterns": best_patterns,
    "allowed_patterns": allowed,
    "allowed_projected_generator_sets": allowed_sets,
    "full_tower_graphs_generated": 0,
    "full_tower_BFS_runs": 0,
    "cpu_seconds": process_time() - started,
}
(OUT / "QUOTIENT_BB_CHECK.json").write_text(json.dumps(summary, indent=2) + "\n")
(OUT / "quotient_bb_patterns.jsonl").write_text("".join(json.dumps(row) + "\n" for row in rows))
print(json.dumps({key: value for key, value in summary.items()
                  if key not in ("best_patterns", "allowed_patterns")}, indent=2))
