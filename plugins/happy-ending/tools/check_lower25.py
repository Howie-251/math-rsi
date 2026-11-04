#!/usr/bin/env python3
"""Recompute a 25-vertex abstract witness; Python stdlib, no SAT libraries.

Paths use vertex count and require each consecutive triple to have its color.
The state (start, penultimate, last) stores a bitset of ALL attainable lengths,
not a solver assignment or an auxiliary predicate from the archived encoder.
Only the supplied TSV is read. All output goes to the explicitly supplied file.
"""

import argparse
import csv
import itertools
import json
import platform
import sys
import time
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def verify(path):
    n = 25
    vertices = range(1, n + 1)
    colors = {}
    with path.open(newline="") as stream:
        rows = csv.DictReader(stream, delimiter="\t")
        require(rows.fieldnames == ["i", "j", "k", "red_true_blue_false"], "Unexpected TSV header")
        for row in rows:
            require(None not in row and None not in row.values(), "Malformed TSV row")
            triple = tuple(int(row[key]) for key in ("i", "j", "k"))
            require(1 <= triple[0] < triple[1] < triple[2] <= n, "Vertex outside ordered triple domain")
            require(triple not in colors, "Duplicate triple")
            require(row["red_true_blue_false"] in ("0", "1"), "Non-Boolean color")
            colors[triple] = int(row["red_true_blue_false"])
    expected = set(itertools.combinations(vertices, 3))
    require(set(colors) == expected, "Missing or extraneous triples")

    packet_violations = []
    packet_count = 0
    for four in itertools.combinations(vertices, 4):
        packet_count += 1
        packet = [colors[triple] for triple in itertools.combinations(four, 3)]
        changes = sum(packet[i] != packet[i + 1] for i in range(3))
        if changes > 1:
            packet_violations.append(list(four))

    # For each color, all_lengths[s,u,v] has bit d set iff there is a
    # d-vertex path starting at s and ending with (u,v). Base paths have two
    # vertices and no triples. Every longer path has a unique final triple
    # (k,u,v) and a prefix ending with (k,u), giving the recurrence below.
    terminal_max = {color: {} for color in (0, 1)}
    outer_lengths = {color: {} for color in (0, 1)}
    state_counts = {}
    for color in (0, 1):
        all_lengths = {}
        outer = {pair: 0 for pair in itertools.combinations(vertices, 2)}
        for last in range(2, n + 1):
            for penult in range(1, last):
                maximum = 0
                for start in range(1, penult + 1):
                    mask = (1 << 2) if start == penult else 0
                    for predecessor in range(start, penult):
                        if colors[predecessor, penult, last] == color:
                            mask |= all_lengths.get((start, predecessor, penult), 0) << 1
                    all_lengths[start, penult, last] = mask
                    outer[start, last] |= mask
                    maximum = max(maximum, mask.bit_length() - 1)
                terminal_max[color][penult, last] = maximum
        outer_lengths[color] = outer
        state_counts[str(color)] = len(all_lengths)

    weak_violations = []
    outer_pair_checks = []
    # Check the full definition d_blue + d_red = 7+2, with d>=2.
    # No signotope path-shortening lemma is needed: all exact lengths were
    # computed from the raw consecutive-triple definition above.
    for start, end in itertools.combinations(vertices, 2):
        blue = outer_lengths[0][start, end]
        red = outer_lengths[1][start, end]
        length_pairs = [[d, 9 - d] for d in range(2, 8)
                        if blue & (1 << d) and red & (1 << (9 - d))]
        if length_pairs:
            weak_violations.append({"endpoints": [start, end], "length_pairs": length_pairs})
        outer_pair_checks.append({"endpoints": [start, end],
                                  "maximum_blue_vertices": blue.bit_length() - 1,
                                  "maximum_red_vertices": red.bit_length() - 1})

    # Build actual downsets as sets of cells, independently of archived
    # height-table enumeration, state variables, or occupancy auxiliaries.
    box = tuple(itertools.product(range(1, 4), range(1, 5)))
    catalog = set()
    for mask in range(1 << len(box)):
        cells = frozenset(cell for index, cell in enumerate(box) if mask & (1 << index))
        if all((a, b) in cells for x, y in cells for a in range(1, x + 1) for b in range(1, y + 1)):
            catalog.add(cells)

    def ordinary(cells):
        width = max((x for x, _ in cells), default=0)
        height = max((y for _, y in cells), default=0)
        return width + height <= 6

    normal = {cells for cells in catalog if ordinary(cells)}
    exceptional = catalog - normal
    states = []
    for last in vertices:
        cells = set()
        for penult in range(1, last):
            blue = terminal_max[0][penult, last] - 1
            red = terminal_max[1][penult, last] - 1
            cells.update(itertools.product(range(1, blue + 1), range(1, red + 1)))
        states.append(frozenset(cells))
    occupied = set(states)
    e = len(occupied & exceptional)
    m = len(normal - occupied)
    maxima = {str(color): max(terminal_max[color].values()) for color in (0, 1)}
    checks = {
        "all_2300_triples_present_once": len(colors) == 2300,
        "all_12650_packets_legal": packet_count == 12650 and not packet_violations,
        "maximum_blue_path_is_4": maxima["0"] == 4,
        "maximum_red_path_is_5": maxima["1"] == 5,
        "all_300_outer_pairs_weak7_free": len(outer_pair_checks) == 300 and not weak_violations,
        "downset_catalog_35_ordinary25_exceptional10": (len(catalog), len(normal), len(exceptional)) == (35, 25, 10),
        "all_actual_states_in_catalog": occupied <= catalog,
        "25_states_distinct": len(occupied) == n,
        "e_equals_9": e == 9,
        "m_equals_9": m == 9,
        "state_count_identity": n == 25 + e - m,
    }
    return {
        "schema": "happy_ending_lower25_independent_stdlib_v1",
        "input": str(path.resolve()),
        "color_semantics": "0=blue, 1=red; paths counted by vertices",
        "method": "all attainable path lengths indexed by start/penultimate/last; explicit set-of-cells downsets and exhaustive 4096-subset ideal catalog",
        "pass": all(checks.values()), "checks": checks,
        "triple_count": len(colors), "packet_count": packet_count,
        "packet_violations": packet_violations,
        "maximum_blue_path_vertices": maxima["0"],
        "maximum_red_path_vertices": maxima["1"],
        "outer_pair_count": len(outer_pair_checks),
        "weak_7_violations": weak_violations,
        "path_dp_state_counts_by_color": state_counts,
        "catalog_count": len(catalog), "ordinary_count": len(normal), "exceptional_count": len(exceptional),
        "occupied_state_count": len(occupied), "e": e, "m": m,
        "states_column_heights": [[sum((x, y) in cells for y in range(1, 5)) for x in range(1, 4)] for cells in states],
        "all_outer_pair_maxima": outer_pair_checks,
        "solver_invocations": 0,
        "scope": "fresh exact verification of one 25-vertex abstract coloring; proves lower25 only, not upper25, coordinate realizability, or the later ES(7) upper bound",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("color_tsv", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    result = verify(args.color_tsv)
    result["elapsed_seconds"] = time.perf_counter() - start
    result["execution_platform"] = platform.platform()
    result["python_version"] = sys.version.split()[0]
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: value for key, value in result.items() if key not in ("all_outer_pair_maxima", "states_column_heights")}, indent=2))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
