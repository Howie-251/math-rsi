"""Bounded S6 census of the a=1 large-face support templates."""

from collections import Counter
from itertools import combinations, permutations
import json
from math import comb
from pathlib import Path
from time import perf_counter


DIMENSION = 6
GROUP_SIZE = 720
PAIR_LIMIT = 100_000
INTERNAL_SECONDS = 55
UNITS = tuple(1 << axis for axis in range(DIMENSION))
EDGES = tuple(sorted(a | b for a, b in combinations(UNITS, 2)))
TRIPLES = tuple(sorted(a | b | c for a, b, c in combinations(UNITS, 3)))


class BudgetReached(Exception):
    pass


def coordinate_maps():
    return tuple(
        tuple(
            sum(1 << new_axis for axis, new_axis in enumerate(permutation)
                if v & (1 << axis))
            for v in range(1 << DIMENSION)
        )
        for permutation in permutations(range(DIMENSION))
    )


def relabel(points, index):
    return tuple(sorted(index[v] for v in points))


def loads(points):
    return tuple(sum(bool(v & unit) for v in points) for unit in UNITS)


def valid_pair(even, odd):
    return (
        all((e ^ o).bit_count() != 5 for e in even for o in odd)
        and all(x + y < 4 or (x, y) == (2, 2)
                for x, y in zip(loads(even), loads(odd)))
    )


def graph_classes(edge_count, maps, check_budget):
    unseen = set(combinations(EDGES, edge_count))
    while unseen:
        check_budget()
        graph = min(unseen)
        orbit = {relabel(graph, index) for index in maps}
        assert orbit <= unseen
        unseen.difference_update(orbit)
        stabilizer = tuple(index for index in maps if relabel(graph, index) == graph)
        assert len(stabilizer) * len(orbit) == GROUP_SIZE
        yield graph, stabilizer, len(orbit)


def preflight(start):
    report = {
        "scope": (
            "Large-face supports only after the proved weight constraints. "
            "E: L even = 0 plus six edges, V odd. "
            "O1: V even = 0 plus five edges, L odd. "
            "O2: V even = bipartite six-cycle, two cases for odd L. "
            "S6 acts simultaneously on both supports. "
            "No small-face completions or prescribed matchings."
        ),
        "status": "RUNNING",
        "candidate_pair_limit": PAIR_LIMIT,
        "internal_wall_limit_seconds": INTERNAL_SECONDS,
        "candidate_pairs": 0,
        "families": {},
        "representatives": [],
    }

    def check_budget():
        if report["candidate_pairs"] >= PAIR_LIMIT:
            raise BudgetReached("PAIR_LIMIT")
        if perf_counter() - start >= INTERNAL_SECONDS:
            raise BudgetReached("WALL_LIMIT")

    def record(family, L, V, multiplicity):
        report["representatives"].append({
            "family": family,
            "L": L,
            "V": V,
            "s6_multiplicity": multiplicity,
        })

    try:
        maps = coordinate_maps()
        for name, edge_count, odd_size, triple_counts in (
            ("E", 6, 6, (0, 1, 2, 3)),
            ("O1", 5, 7, (1, 2)),
        ):
            summary = {
                "labeled_first_graphs": comb(len(EDGES), edge_count),
                "first_graph_orbits_seen": 0,
                "first_graph_orbits_with_max_degree_at_most_three": 0,
                "raw_partner_pairs_upper_bound": 0,
                "partner_pairs_upper_bound_after_triangle_cover": 0,
                "candidate_pairs": 0,
                "valid_pairs_at_canonical_first_graphs": 0,
                "valid_pairs_at_labeled_first_graphs": 0,
                "pair_orbits": 0,
                "pair_orbits_by_triple_count": Counter(),
            }
            report["families"][name] = summary
            for graph, stabilizer, graph_multiplicity in graph_classes(
                edge_count, maps, check_budget
            ):
                summary["first_graph_orbits_seen"] += 1
                summary["raw_partner_pairs_upper_bound"] += sum(
                    comb(len(UNITS), odd_size - t) * comb(len(TRIPLES), t)
                    for t in triple_counts
                )
                if max(loads(graph)) > 3:
                    continue
                summary["first_graph_orbits_with_max_degree_at_most_three"] += 1
                even = (0, *graph)
                cover_triples = tuple(t for t in TRIPLES if all(t & e for e in graph))
                for t in triple_counts:
                    summary["partner_pairs_upper_bound_after_triangle_cover"] += (
                        comb(len(UNITS), odd_size - t) * comb(len(cover_triples), t)
                    )
                    valid = set()
                    for units in combinations(UNITS, odd_size - t):
                        for triples in combinations(cover_triples, t):
                            check_budget()
                            report["candidate_pairs"] += 1
                            summary["candidate_pairs"] += 1
                            odd = tuple(sorted(units + triples))
                            if valid_pair(even, odd):
                                valid.add(odd)
                                summary["valid_pairs_at_canonical_first_graphs"] += 1
                                summary["valid_pairs_at_labeled_first_graphs"] += graph_multiplicity
                                # Record each representative at its first encounter so a budget
                                # hit retains a genuine, independently usable prefix.
                                orbit = {relabel(odd, index) for index in stabilizer}
                                if odd != min(orbit):
                                    continue
                                assert len(stabilizer) % len(orbit) == 0
                                L, V = (even, odd) if name == "E" else (odd, even)
                                record(name, L, V, graph_multiplicity * len(orbit))
                                summary["pair_orbits"] += 1
                                summary["pair_orbits_by_triple_count"][t] += 1
                    # Symmetry maps valid partners to valid partners with the same t.
                    assert all(relabel(odd, index) in valid
                               for odd in valid for index in stabilizer)

        bipartite_cycle = (9, 12, 17, 18, 34, 36)
        for suffix, L in (
            ("O2_s1", tuple(sorted((*UNITS, 7)))),
            ("O2_s2", tuple(sorted((*UNITS[:-1], 7, 56)))),
        ):
            check_budget()
            assert valid_pair(bipartite_cycle, L)
            report["candidate_pairs"] += 1
            orbit = {
                (relabel(L, index), relabel(bipartite_cycle, index))
                for index in maps
            }
            record(suffix, L, bipartite_cycle, len(orbit))
            report["families"][suffix] = {
                "candidate_pairs": 1,
                "pair_orbits": 1,
                "labeled_pairs": len(orbit),
            }

        for family in ("E", "O1"):
            summary = report["families"][family]
            assert summary["candidate_pairs"] == summary["partner_pairs_upper_bound_after_triangle_cover"]
            assert summary["valid_pairs_at_labeled_first_graphs"] == sum(
                row["s6_multiplicity"] for row in report["representatives"]
                if row["family"] == family
            )
        report["status"] = "COMPLETE"
    except BudgetReached as error:
        report["status"] = str(error)
    report["total_s6_representatives"] = len(report["representatives"])
    report["elapsed_seconds"] = perf_counter() - start
    return report


if __name__ == "__main__":
    start = perf_counter()
    report = preflight(start)
    output = Path(__file__).with_name("STRUCTURE_BASIS_PREFLIGHT.json")
    output.write_text(json.dumps(report, separators=(",", ":")) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key != "representatives"}))
