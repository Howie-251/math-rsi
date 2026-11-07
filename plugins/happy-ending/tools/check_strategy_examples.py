#!/usr/bin/env python3
"""Check two fixed small strategy counterexamples, not an ES upper bound.

Enumerates every increasing vertex subset as a path; uses only consecutive
triples, not SAT predicates or a path-shortening lemma. Python standard library.
"""
import argparse
import itertools
import json
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def inspect(n, red):
    vertices = tuple(range(1, n + 1))
    colors = {t: bool(red(t)) for t in itertools.combinations(vertices, 3)}
    packets = 0
    for four in itertools.combinations(vertices, 4):
        packet = [colors[t] for t in itertools.combinations(four, 3)]
        require(sum(a != b for a, b in zip(packet, packet[1:])) <= 1,
                f"Invalid packet: {four}")
        packets += 1
    paths = {False: [], True: []}
    for size in range(2, n + 1):
        for seq in itertools.combinations(vertices, size):
            triples = list(zip(seq, seq[1:], seq[2:]))
            for color in paths:
                if all(colors[t] == color for t in triples):
                    paths[color].append(seq)
    longest = {str(int(c)): max(map(len, ps)) for c, ps in paths.items()}
    endpoints = {c: {} for c in paths}
    for c, ps in paths.items():
        for seq in ps:
            pair = (seq[0], seq[-1])
            endpoints[c][pair] = max(endpoints[c].get(pair, 0), len(seq))
    weak_max = max(endpoints[False][pair] + endpoints[True][pair]
                   for pair in endpoints[False])
    require(weak_max < 9, "Unexpected weak7")
    return paths, {"n": n, "triples": len(colors), "packets": packets,
                   "increasing_subsets_checked": 2**n - n - 1,
                   "maximum_vertices_blue_red": longest,
                   "maximum_same_endpoint_length_sum": weak_max}


def check_common_root():
    # L={1..5}, z=6, R={7..11}; red exactly in either closed half.
    paths, report = inspect(11, lambda t: max(t) <= 6 or min(t) >= 6)
    r6 = [p for p in paths[True] if len(p) == 6]
    sources, ends = {p[0] for p in r6}, {p[-1] for p in r6}
    require(sources == {1, 6} and ends == {6, 11}, "R6 roles differ")
    core = set(range(2, 6)) | set(range(7, 11))
    r5 = [p for p in paths[True] if len(p) == 5]
    require(not any(set(p) <= core for p in r5), "Core has R5")
    require(all(any(set(p) <= core | {x} for p in r5) for x in {1, 6, 11}),
            "Missing private supply")
    require(not any(p[0] < 6 < p[-1] for p in r5), "Cross-side R5 exists")
    roles = sources | ends
    enhanced_ends = {p[-1] for p in r6 if p[-1] == 6 and p[-2] in roles}
    enhanced_sources = {p[0] for p in r6 if p[0] == 6 and p[1] in roles}
    require(not enhanced_ends and not enhanced_sources, "Unexpected effective root")
    report.update({"core": sorted(core), "R6_sources": sorted(sources),
                   "R6_ends": sorted(ends), "private_R5_for_all_external_points": True,
                   "strict_cross_side_R5": False, "effective_root_at_6": False})
    return report


def check_joint_insertion():
    blocks = [set(range(1, 5)), set(range(4, 8)), set(range(7, 11))]
    paths, report = inspect(10, lambda t: not any(set(t) <= b for b in blocks))
    require(max(map(len, paths[False])) < 5, "Unexpected B5")
    require(max(map(len, paths[True])) < 7, "Unexpected R7")
    b4 = [p for p in paths[False] if len(p) == 4]
    r6 = [p for p in paths[True] if len(p) == 6]
    canonical_a = set(range(1, 11)) - {p[-1] for p in b4}
    canonical_b = set(range(1, 11)) - {p[0] for p in r6}
    require(canonical_a == {1, 2, 3, 5, 6, 8, 9}, "Canonical A differs")
    require({7, 10} <= canonical_b - canonical_a, "Insertion points not in B minus A")
    require(all(not any(set(p) <= canonical_a | {x} for p in b4) for x in (7, 10)),
            "Single insertion already fails")
    joint = [list(p) for p in b4 if set(p) <= canonical_a | {7, 10}]
    require([7, 8, 9, 10] in joint, "Missing joint obstruction")
    report.update({"canonical_A": sorted(canonical_a), "canonical_B": sorted(canonical_b),
                   "single_insertions_B4_free": [7, 10], "joint_B4_witnesses": joint})
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = {"scope": "two fixed abstract strategy counterexamples; no universal upper-bound proof",
              "common_root_11": check_common_root(), "canonical_joint_10": check_joint_insertion()}
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print("PASS: two fixed counterexamples; no full-proof acceptance")


if __name__ == "__main__":
    main()
