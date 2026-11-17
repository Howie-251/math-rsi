"""Bounded S6 preflight of a=1 large-face supports, including the five-point branch."""

from collections import Counter
from itertools import combinations
import json
from math import comb
from pathlib import Path
import sys
from time import perf_counter

sys.dont_write_bytecode = True

from MU0_A0_BASIS_PREFLIGHT import (
    QUADRUPLE, TRIPLES, UNITS, coordinate_maps, graph_orbits, loads, permute,
)


FIVE_POINTS = tuple(sorted(63 ^ unit for unit in UNITS))
PAIR_LIMIT = 100_000
WALL_SECONDS = 55


class BudgetReached(Exception):
    """Preserve the checked prefix on a preflight budget exit."""


def survives(L, V, even_load):
    if not all((x ^ y).bit_count() != 5 for x in L for y in V):
        return False
    return all(
        x + y <= 4 or (x, y) in ((2, 3), (3, 2))
        for x, y in zip(even_load, loads(V))
    )


def preflight():
    start = perf_counter()
    report = {
        "scope": "Necessary a=1 large-face geometries; small face and original matching unexamined.",
        "status": "RUNNING",
        "candidate_pair_budget": PAIR_LIMIT,
        "internal_wall_budget_seconds": WALL_SECONDS,
        "candidate_pairs": 0,
        "templates": {},
        "representatives": [],
    }

    def check_budget():
        if report["candidate_pairs"] >= PAIR_LIMIT:
            raise BudgetReached("PAIR_LIMIT")
        if perf_counter() - start >= WALL_SECONDS:
            raise BudgetReached("WALL_LIMIT")

    # The two seven-edge rows have the same first graph set, but separate partner scopes.
    templates = (
        ("zero_six_edges", 6, True, False, False, range(1, 6)),
        ("seven_edges", 7, False, False, False, range(1, 5)),
        ("seven_edges_and_V_five_point", 7, False, False, True, range(3)),
        ("zero_five_edges_four", 5, True, True, False, (3, 4)),
    )
    try:
        maps = coordinate_maps()
        four_stabilizer = tuple(mapping for mapping in maps
                                if mapping[QUADRUPLE] == QUADRUPLE)
        assert len(maps) == 720 and len(four_stabilizer) == 48
        for label, edges, zero, four, five, triple_sizes in templates:
            group = four_stabilizer if four else maps
            mark_orbit_size = 15 if four else 1
            marks = ((0,) if zero else ()) + ((QUADRUPLE,) if four else ())
            summary = {
                "first_graph_labels_with_fixed_marks": comb(15, edges),
                "first_graph_orbits_seen": 0,
                "raw_partner_bound_at_first_representatives": 0,
                "partner_bound_after_cross_distance": 0,
                "candidate_pairs": 0,
                "valid_pairs_at_first_representatives": 0,
                "valid_labeled_pairs": 0,
                "pair_orbits": 0,
                "pair_orbits_by_triple_count": Counter(),
            }
            report["templates"][label] = summary
            for graph, graph_orbit_size, stabilizer in graph_orbits(edges, group, check_budget):
                summary["first_graph_orbits_seen"] += 1
                L = tuple(sorted(graph + marks))
                even_load = loads(L)
                assert len(L) == 7
                units = tuple(u for u in UNITS if not four or u & QUADRUPLE)
                triples = tuple(t for t in TRIPLES if all(t & e for e in graph)
                                and (not four or (t & QUADRUPLE).bit_count() >= 2))
                fifth = tuple((v,) for v in FIVE_POINTS
                              if all(v & e == e for e in graph)) if five else ((),)
                first_weight = graph_orbit_size * mark_orbit_size
                for t in triple_sizes:
                    u = 7 - t - int(five)
                    summary["raw_partner_bound_at_first_representatives"] += (
                        comb(6, u) * comb(20, t) * (6 if five else 1)
                    )
                    summary["partner_bound_after_cross_distance"] += (
                        comb(len(units), u) * comb(len(triples), t) * len(fifth)
                    )
                    for fifth_point in fifth:
                        for unit_subset in combinations(units, u):
                            for triple_subset in combinations(triples, t):
                                check_budget()
                                summary["candidate_pairs"] += 1
                                report["candidate_pairs"] += 1
                                V = tuple(sorted(unit_subset + triple_subset + fifth_point))
                                if not survives(L, V, even_load):
                                    continue
                                summary["valid_pairs_at_first_representatives"] += 1
                                summary["valid_labeled_pairs"] += first_weight
                                partner_orbit = {permute(V, mapping) for mapping in stabilizer}
                                if V != min(partner_orbit):
                                    continue
                                assert len(stabilizer) % len(partner_orbit) == 0
                                summary["pair_orbits"] += 1
                                summary["pair_orbits_by_triple_count"][t] += 1
                                report["representatives"].append({
                                    "template": label,
                                    "L": L,
                                    "V": V,
                                    "orbit_multiplicity": first_weight * len(partner_orbit),
                                })
            assert summary["candidate_pairs"] == summary["partner_bound_after_cross_distance"]
            assert summary["valid_labeled_pairs"] == sum(
                row["orbit_multiplicity"] for row in report["representatives"]
                if row["template"] == label
            )
        report["status"] = "COMPLETE"
    except BudgetReached as error:
        report["status"] = str(error)
    report["stored_representatives"] = len(report["representatives"])
    report["wall_seconds"] = perf_counter() - start
    return report


if __name__ == "__main__":
    result = preflight()
    output_path = Path(__file__).with_suffix(".json")
    output_path.write_text(json.dumps(result, separators=(",", ":")) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "representatives"}))
