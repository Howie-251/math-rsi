"""Bounded preflight of a=0 large-face supports, using the refined templates."""

from collections import Counter
from itertools import combinations, permutations
import json
from math import comb
from pathlib import Path
from time import perf_counter


UNITS = tuple(1 << j for j in range(6))
EDGES = tuple(sorted(a | b for a, b in combinations(UNITS, 2)))
TRIPLES = tuple(sorted(a | b | c for a, b, c in combinations(UNITS, 3)))
QUADRUPLE = 15
PAIR_LIMIT = 100_000
INTERNAL_WALL_SECONDS = 55


class PreflightLimit(Exception):
    pass


def permute(points, mapping):
    return tuple(sorted(mapping[v] for v in points))


def loads(points):
    return tuple(sum(bool(v & unit) for v in points) for unit in UNITS)


def coordinate_maps():
    return tuple(
        tuple(
            sum(1 << destination for source, destination in enumerate(places)
                if vertex & (1 << source))
            for vertex in range(64)
        )
        for places in permutations(range(6))
    )


def graph_orbits(edge_count, maps, check_budget):
    unseen = set(combinations(EDGES, edge_count))
    while unseen:
        check_budget()
        graph = min(unseen)
        orbit = {permute(graph, mapping) for mapping in maps}
        assert orbit <= unseen
        unseen.difference_update(orbit)
        stabilizer = tuple(mapping for mapping in maps if permute(graph, mapping) == graph)
        assert len(orbit) * len(stabilizer) == len(maps)
        yield graph, len(orbit), stabilizer


def permitted(even, odd, even_load):
    return all(
        (e ^ o).bit_count() != 5 for e in even for o in odd
    ) and all(
        x + y <= 5 or (x, y) == (3, 3)
        for x, y in zip(even_load, loads(odd))
    )


def preflight():
    start = perf_counter()
    report = {
        "scope": (
            "Necessary large-face support pairs for a=0, before joint gates "
            "on other axes. Common S6 only; no prescribed matching work."
        ),
        "status": "RUNNING",
        "pair_budget": PAIR_LIMIT,
        "internal_wall_budget_seconds": INTERNAL_WALL_SECONDS,
        "candidate_pairs_checked": 0,
        "templates": {},
        "representatives": [],
    }

    def check_budget():
        if report["candidate_pairs_checked"] >= PAIR_LIMIT:
            raise PreflightLimit("PAIR_LIMIT")
        if perf_counter() - start >= INTERNAL_WALL_SECONDS:
            raise PreflightLimit("WALL_LIMIT")

    templates = (
        ("zero_seven_edges", 7, True, False, range(2, 7)),
        ("eight_edges", 8, False, False, range(2, 6)),
        ("zero_six_edges_four", 6, True, True, range(4, 6)),
    )
    try:
        maps = coordinate_maps()
        four_stabilizer = tuple(mapping for mapping in maps
                                if mapping[QUADRUPLE] == QUADRUPLE)
        assert len(maps) == 720 and len(four_stabilizer) == 48
        for family, edge_count, has_zero, has_four, triple_sizes in templates:
            check_budget()
            group = four_stabilizer if has_four else maps
            four_multiplicity = 15 if has_four else 1
            marked = ((0,) if has_zero else ()) + ((QUADRUPLE,) if has_four else ())
            summary = {
                "first_graph_labels_with_fixed_marks": comb(15, edge_count),
                "first_graph_classes_seen": 0,
                "first_graph_classes_with_degree_at_most_three": 0,
                "partner_choices_upper_bound_after_short_distance": 0,
                "candidate_pairs": 0,
                "valid_pairs_at_first_representatives": 0,
                "valid_pairs_at_labeled_first_groups": 0,
                "pair_orbits": 0,
                "pair_orbits_by_triple_count": Counter(),
            }
            report["templates"][family] = summary
            for graph, first_orbit, stabilizer in graph_orbits(
                edge_count, group, check_budget
            ):
                summary["first_graph_classes_seen"] += 1
                if max(loads(graph)) > 3:
                    continue
                summary["first_graph_classes_with_degree_at_most_three"] += 1
                L = tuple(sorted(marked + graph))
                even_load = loads(L)
                assert len(L) == 8
                # Crossing distance five excludes a disjoint graph edge and triple.
                units = tuple(u for u in UNITS if not has_four or u & QUADRUPLE)
                triples = tuple(t for t in TRIPLES if all(t & edge for edge in graph)
                                and (not has_four or (t & QUADRUPLE).bit_count() >= 2))
                for count in triple_sizes:
                    number = comb(len(units), 8 - count) * comb(len(triples), count)
                    summary["partner_choices_upper_bound_after_short_distance"] += number
                    for singletons in combinations(units, 8 - count):
                        for supports in combinations(triples, count):
                            check_budget()
                            report["candidate_pairs_checked"] += 1
                            summary["candidate_pairs"] += 1
                            V = tuple(sorted(singletons + supports))
                            if not permitted(L, V, even_load):
                                continue
                            summary["valid_pairs_at_first_representatives"] += 1
                            graph_weight = first_orbit * four_multiplicity
                            summary["valid_pairs_at_labeled_first_groups"] += graph_weight
                            partners = {permute(V, mapping) for mapping in stabilizer}
                            if V != min(partners):
                                continue
                            assert len(stabilizer) % len(partners) == 0
                            summary["pair_orbits"] += 1
                            summary["pair_orbits_by_triple_count"][count] += 1
                            report["representatives"].append({
                                "template": family,
                                "L": L,
                                "V": V,
                                "orbit_multiplicity": graph_weight * len(partners),
                            })
            assert summary["candidate_pairs"] == summary["partner_choices_upper_bound_after_short_distance"]
            assert summary["valid_pairs_at_labeled_first_groups"] == sum(
                row["orbit_multiplicity"] for row in report["representatives"]
                if row["template"] == family
            )
        report["status"] = "COMPLETE"
    except PreflightLimit as error:
        report["status"] = str(error)
    report["stored_representatives"] = len(report["representatives"])
    report["wall_seconds"] = perf_counter() - start
    return report


if __name__ == "__main__":
    report = preflight()
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(report, separators=(",", ":")) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key != "representatives"}))
