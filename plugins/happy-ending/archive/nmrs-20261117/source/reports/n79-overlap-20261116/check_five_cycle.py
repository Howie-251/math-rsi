#!/usr/bin/env python3
"""Exact replay of the c=5 five-cycle hole conditions; stdlib only.

Prepared on 2026-11-16 and NOT EXECUTED during preparation. Run on Linux:
    python3 -B reports/n79-overlap-20261116/check_five_cycle.py
    python3 -B reports/n79-overlap-20261116/check_five_cycle.py --w 3 4

No input files, solver, network, or random choices are used. JSON is written
to stdout. A surviving hole set satisfies only the stated necessary tests;
it is not an actual signotope construction. Zero survivors excludes only
the selected c=5 domain under these necessary conditions. The optional
15-layer red matching-rank conditions are NOT implemented.
"""

import argparse
import itertools
import json
import math
import sys


LABELS = frozenset(range(1, 7))
UNIVERSE = frozenset(itertools.combinations(range(1, 9), 3))
EARLY_FORBIDDEN = frozenset(((1, 2), (1, 3)))
LATE_FORBIDDEN = frozenset(((5, 6), (4, 6)))


def require(condition, message):
    """Keep exact self-checks enabled even under python -O."""
    if not condition:
        raise RuntimeError(message)


def edge(a, b):
    require(a != b, "A graph edge must have distinct endpoints")
    return tuple(sorted((a, b)))


def encode(heights):
    require(len(heights) == 3, "Expected three columns")
    require(5 >= heights[0] >= heights[1] >= heights[2] >= 0,
            "Invalid 3x5 ideal heights: {!r}".format(heights))
    state = tuple(sorted(heights[i] + 3 - i for i in range(3)))
    require(len(set(state)) == 3 and state in UNIVERSE,
            "Ideal encoding failed")
    return state


def all_rows():
    """All 41 east/south/diagonal 3x5 rows, with parameters retained."""
    rows = []
    for q1 in range(1, 6):
        for q2 in range(1, q1 + 1):
            for p1 in (q1, q1 + 1):
                for p2 in (q2, q2 + 1):
                    if p1 > 5 or p2 > q1:
                        continue
                    require(5 >= p1 >= p2 >= 1, "Invalid start heights")
                    start = (p1 - 1, p2 - 1, 0)
                    end = (5, q1, q2)
                    blue = [encode(start)]
                    for column in range(3):
                        heights = tuple(end[i] if i <= column else start[i]
                                        for i in range(3))
                        blue.append(encode(heights))
                    red = [encode(start)]
                    for h in range(1, 6):
                        heights = tuple(max(start[i], min(end[i], h))
                                        for i in range(3))
                        red.append(encode(heights))
                    support = frozenset(blue + red)
                    require(len(set(blue)) == 4, "Blue chain must have 4 states")
                    require(len(set(red)) == 6, "Red chain must have 6 states")
                    require(set(blue) & set(red) == {encode(start), encode(end)},
                            "The two chains must share exactly their endpoints")
                    require(len(support) == 8, "Every row must have 8 states")
                    rows.append({"q": (q1, q2), "p": (p1, p2),
                                 "support": support,
                                 "ordinary": (p1 == q1 and p2 == q2)})
    require(len(rows) == 41, "Delannoy D(2,4) must be 41")
    require(sum(row["ordinary"] for row in rows) == 15,
            "There must be 15 ordinary rows")
    require(len({row["support"] for row in rows}) == 41,
            "Delannoy row supports must be distinct")
    return rows


def five_cycles(vertices):
    """Exactly 12 labelled undirected Hamilton cycles on five vertices."""
    vertices = tuple(sorted(vertices))
    require(len(vertices) == 5, "Expected five noncentral vertices")
    cycles = []
    for tail in itertools.permutations(vertices[1:]):
        # Fix the least vertex first, and retain one of the two directions.
        if tail[0] >= tail[-1]:
            continue
        order = (vertices[0],) + tail
        cycle = frozenset(edge(order[i], order[(i + 1) % 5])
                          for i in range(5))
        require(len(cycle) == 5, "A five-cycle must have five edges")
        require(all(sum(v in e for e in cycle) == 2 for v in vertices),
                "A five-cycle must be two-regular")
        cycles.append(cycle)
    require(len(cycles) == len(set(cycles)) == 12,
            "Cycle catalogue must have exactly 12 distinct members")
    return cycles


def make_candidate(w, cycle, first_private):
    """Translate one ordered (w,P,F,G) into its 16 missing W states."""
    vertices = LABELS - {w}
    noncentral_edges = frozenset(itertools.combinations(sorted(vertices), 2))
    private_support = (frozenset(edge(w, v) for v in vertices)
                       | (noncentral_edges - cycle))
    first_private = frozenset(first_private)
    last_private = private_support - first_private
    require(len(private_support) == 10, "Private support must have ten edges")
    require(len(first_private) == len(last_private) == 5,
            "F and G must each have five edges")
    require(first_private.isdisjoint(last_private), "F and G must be disjoint")
    red_triples = frozenset(tuple(sorted(vertices - set(e))) for e in cycle)
    require(len(red_triples) == 5, "There must be five red internal holes")
    blue_hole = tuple(sorted((1, 8, w + 1)))
    red_holes = frozenset(tuple(j + 1 for j in triple) for triple in red_triples)
    first_holes = frozenset(tuple(sorted((1, i + 1, j + 1)))
                            for i, j in first_private)
    last_holes = frozenset(tuple(sorted((8, i + 1, j + 1)))
                           for i, j in last_private)
    holes = frozenset({blue_hole}) | red_holes | first_holes | last_holes
    require(len(holes) == 16 and holes <= UNIVERSE,
            "Candidate must give exactly 16 valid, distinct missing states")
    return {"cycle": cycle, "F": first_private, "G": last_private,
            "red_triples": red_triples, "holes": holes}


def candidate_catalogue(rows):
    """Build the whole 18144-member domain, even for a selected-w run."""
    catalogue = {}
    all_pairs = set()
    ordinary = [row["support"] for row in rows if row["ordinary"]]
    for w in sorted(LABELS):
        candidates = []
        vertices = LABELS - {w}
        for cycle in five_cycles(vertices):
            private_support = (frozenset(edge(w, v) for v in vertices)
                               | (frozenset(itertools.combinations(
                                   sorted(vertices), 2)) - cycle))
            splits = list(itertools.combinations(sorted(private_support), 5))
            require(len(splits) == math.comb(10, 5) == 252,
                    "Each cycle must have 252 ordered F/G splits")
            for first_private in splits:
                candidate = make_candidate(w, cycle, first_private)
                key = (w, cycle, candidate["F"])
                require(key not in all_pairs, "Duplicate domain member")
                all_pairs.add(key)
                require(all(len(candidate["holes"] & support) == 2
                            for support in ordinary),
                        "The c=5 construction must hit each ordinary row twice")
                candidates.append(candidate)
        require(len(candidates) == 12 * 252 == 3024,
                "Each center must have exactly 3024 raw candidates")
        catalogue[w] = candidates
    require(sum(map(len, catalogue.values())) == len(all_pairs) == 18144,
            "Full domain must be 6 * 12 * 252 = 18144")
    return catalogue


def serialize_survivor(candidate):
    return {"P_cycle_edges": sorted(candidate["cycle"]),
            "F_first_private_edges": sorted(candidate["F"]),
            "G_last_private_edges": sorted(candidate["G"]),
            "red_internal_triples": sorted(candidate["red_triples"]),
            "missing_W": sorted(candidate["holes"])}


def check_center(w, candidates, rows):
    raw_count = len(candidates)
    candidates = [candidate for candidate in candidates
                  if candidate["F"].isdisjoint(EARLY_FORBIDDEN)]
    after_first = len(candidates)
    candidates = [candidate for candidate in candidates
                  if candidate["G"].isdisjoint(LATE_FORBIDDEN)]
    after_last = len(candidates)
    stages = []
    for index, row in enumerate(rows):
        before = len(candidates)
        candidates = [candidate for candidate in candidates
                      if len(candidate["holes"] & row["support"]) >= 2]
        stages.append({"row_index": index, "q": row["q"], "p": row["p"],
                       "ordinary": row["ordinary"],
                       "eight_states_W": sorted(row["support"]),
                       "survivors": len(candidates),
                       "rejected_at_this_stage": before - len(candidates)})
    # Replay surviving members against the full conjunction, independently of
    # the destructive filtering order used for the per-stage counters.
    for candidate in candidates:
        require(candidate["F"].isdisjoint(EARLY_FORBIDDEN)
                and candidate["G"].isdisjoint(LATE_FORBIDDEN)
                and all(len(candidate["holes"] & row["support"]) >= 2
                        for row in rows), "Survivor replay failed")
    return {"w": w, "raw": raw_count,
            "after_F_excludes_12_13": after_first,
            "after_G_excludes_56_46": after_last,
            "Delannoy_stages": stages, "survivors": len(candidates),
            "first_survivor": (serialize_survivor(candidates[0])
                               if candidates else None)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--w", type=int, nargs="+", choices=range(1, 7),
                        default=list(range(1, 7)),
                        help="Centers to check; default: all six, or use --w 3 4")
    args = parser.parse_args()
    if not sys.platform.startswith("linux"):
        parser.error("Scientific replay is restricted to the Linux execution target")
    require(len(UNIVERSE) == 56, "3x5 universe must contain 56 states")
    require(encode((0, 0, 0)) == (1, 2, 3), "Empty ideal encoding mismatch")
    require(encode((1, 0, 0)) == (1, 2, 4), "Singleton ideal encoding mismatch")
    require(encode((5, 5, 4)) == (5, 7, 8), "Penultimate encoding mismatch")
    require(encode((5, 5, 5)) == (6, 7, 8), "Full ideal encoding mismatch")
    rows = all_rows()
    catalogue = candidate_catalogue(rows)
    selected = sorted(set(args.w))
    result = {"schema": "c5_five_cycle_delannoy_exact_v1",
              "scope": "Necessary hole-set conditions only; no signotope realization",
              "selected_w": selected, "complete_c5_domain_checked": selected == list(range(1, 7)),
              "self_checks": {"universe_states": 56, "Delannoy_rows": 41,
                              "ordinary_rows": 15, "states_per_row": 8,
                              "centers": 6, "cycles_per_center": 12,
                              "splits_per_cycle": 252, "raw_domain": 18144},
              "extra_red_matching_rank_constraints": "not_implemented",
              "by_center": [check_center(w, catalogue[w], rows) for w in selected]}
    result["selected_survivors"] = sum(item["survivors"] for item in result["by_center"])
    json.dump(result, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
