"""Bounded S6 preflight of a=2 large-face support pairs."""

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


PAIR_LIMIT = 100_000
WALL_SECONDS = 55


class BudgetReached(Exception):
    """Stop with the prefix of representatives already checked."""


def survives(L, V, loads_L):
    return all(
        (x ^ y).bit_count() != 5 for x in L for y in V
    ) and all(
        x + y <= 3 or (x, y) == (2, 2)
        for x, y in zip(loads_L, loads(V))
    )


def preflight():
    start = perf_counter()
    report = {
        "scope": "Necessary a=2 large-face support pairs only; small face and actual matching not generated.",
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

    templates = (
        ("zero_five_edges", 5, (0,), (0, 1, 2, 3)),
        ("six_edges", 6, (), (0, 1, 2)),
        ("zero_four_edges_four", 4, (0, QUADRUPLE), (2,)),
    )
    try:
        maps = coordinate_maps()
        four_stabilizer = tuple(mapping for mapping in maps
                                if mapping[QUADRUPLE] == QUADRUPLE)
        assert len(maps) == 720 and len(four_stabilizer) == 48
        for label, edge_count, marks, triple_sizes in templates:
            marked = QUADRUPLE in marks
            group = four_stabilizer if marked else maps
            mark_weight = 15 if marked else 1
            summary = {
                "first_graph_labels_with_fixed_marks": comb(15, edge_count),
                "first_graph_orbits_seen": 0,
                "first_group_orbits_with_load_at_most_three": 0,
                "raw_partner_bound_at_first_representatives": 0,
                "partner_bound_after_cross_distance": 0,
                "candidate_pairs": 0,
                "valid_pairs_at_first_representatives": 0,
                "valid_labeled_pairs": 0,
                "pair_orbits": 0,
                "pair_orbits_by_triple_count": Counter(),
            }
            report["templates"][label] = summary
            for graph, graph_weight, stabilizer in graph_orbits(edge_count, group, check_budget):
                summary["first_graph_orbits_seen"] += 1
                summary["raw_partner_bound_at_first_representatives"] += sum(
                    comb(6, 6 - t) * comb(20, t) for t in triple_sizes
                )
                L = tuple(sorted(graph + marks))
                loads_L = loads(L)
                assert len(L) == 6
                if max(loads_L) > 3:
                    continue
                summary["first_group_orbits_with_load_at_most_three"] += 1
                units = tuple(u for u in UNITS if not marked or u & QUADRUPLE)
                triples = tuple(t for t in TRIPLES if all(t & e for e in graph)
                                and (not marked or (t & QUADRUPLE).bit_count() >= 2))
                first_weight = graph_weight * mark_weight
                for t in triple_sizes:
                    u = 6 - t
                    summary["partner_bound_after_cross_distance"] += (
                        comb(len(units), u) * comb(len(triples), t)
                    )
                    for selected_units in combinations(units, u):
                        for selected_triples in combinations(triples, t):
                            check_budget()
                            summary["candidate_pairs"] += 1
                            report["candidate_pairs"] += 1
                            V = tuple(sorted(selected_units + selected_triples))
                            if not survives(L, V, loads_L):
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
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(result, separators=(",", ":")) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "representatives"}))
