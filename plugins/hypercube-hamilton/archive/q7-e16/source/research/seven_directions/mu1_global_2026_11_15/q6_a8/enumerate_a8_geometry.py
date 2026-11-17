"""Exhaust normalized Q6 A8 hole geometries for the stated coordinate gates."""

from collections import Counter
from itertools import combinations, permutations
import json
from math import comb


DIMENSION = 6
GROUP_SIZE = 720
FIRST_GATES = ("delta_2", "delta_3", "delta_1")
ALL_GATES = (*FIRST_GATES, "delta_4", "delta_0_k_3")
VERTICES = range(1 << DIMENSION)
ODD = [vertex for vertex in VERTICES if vertex.bit_count() % 2]
NONZERO_EVEN = [
    vertex for vertex in VERTICES if vertex and vertex.bit_count() % 2 == 0
]


def coordinate_permutations():
    for permutation in permutations(range(DIMENSION)):
        yield tuple(
            sum(1 << target for source, target in enumerate(permutation)
                if vertex & (1 << source))
            for vertex in VERTICES
        )


def relabel(vertices, permutation):
    return tuple(sorted(permutation[vertex] for vertex in vertices))


def zero_counts(vertices):
    return tuple(
        sum(not vertex & (1 << axis) for vertex in vertices)
        for axis in range(DIMENSION)
    )


def classify(delta, minority_count):
    gates = [f"delta_{value}" for value in (2, 3, 1, 4) if value in delta]
    if (0, 3) in zip(delta, minority_count):
        gates.append("delta_0_k_3")
    return gates


def exhaust():
    permutations_by_vertex = tuple(coordinate_permutations())
    assert len(set(permutations_by_vertex)) == GROUP_SIZE
    unseen_triples = set(combinations(ODD, 3))
    row_totals = Counter()
    normalized_totals = Counter()
    gate_incidence = Counter()
    normalized_gate_incidence = Counter()
    triple_rows = []
    remaining = []
    residual_profiles = Counter()
    minority_triples = 0

    while unseen_triples:
        minority = min(unseen_triples)
        orbit = {
            relabel(minority, permutation)
            for permutation in permutations_by_vertex
        }
        assert orbit <= unseen_triples
        unseen_triples.difference_update(orbit)
        stabilizer = [
            permutation for permutation in permutations_by_vertex
            if relabel(minority, permutation) == minority
        ]
        assert len(orbit) * len(stabilizer) == GROUP_SIZE

        allowed = [
            vertex for vertex in NONZERO_EVEN
            if all((vertex ^ hole).bit_count() != 1 for hole in minority)
        ]
        minority_count = zero_counts(minority)
        base_remaining = 0
        leftover = set()
        for other_majority in combinations(allowed, 4):
            major_zero = zero_counts(other_majority)
            delta = tuple(
                1 + majority - minority
                for majority, minority in zip(major_zero, minority_count)
            )
            gates = classify(delta, minority_count)
            gate_incidence.update(gates)
            for gate in gates:
                normalized_gate_incidence[gate] += len(orbit)
            first_gate = next(iter(gates), "remaining")
            row_totals[first_gate] += 1
            normalized_totals[first_gate] += len(orbit)
            if not any(gate in FIRST_GATES for gate in gates):
                base_remaining += 1
            if not gates:
                leftover.add(other_majority)

        triple_rows.append({
            "minority": minority,
            "minority_multiplicity": len(orbit),
            "allowed_majority": len(allowed),
            "majority_quadruples": comb(len(allowed), 4),
            "after_delta_1_2_3": base_remaining,
            "after_all_gates": len(leftover),
        })
        minority_triples += len(orbit)
        while leftover:
            other_majority = min(leftover)
            majority_orbit = {
                relabel(other_majority, permutation)
                for permutation in stabilizer
            }
            assert majority_orbit <= leftover
            leftover.difference_update(majority_orbit)
            orbit_size = len(orbit) * len(majority_orbit)
            assert GROUP_SIZE % orbit_size == 0
            delta = tuple(
                1 + majority - minority
                for majority, minority in zip(
                    zero_counts(other_majority), minority_count
                )
            )
            zero_k2_axes = [
                axis for axis, key in enumerate(zip(delta, minority_count))
                if key == (0, 2)
            ]
            remaining.append({
                "minority": minority,
                "other_majority": other_majority,
                "orbit_multiplicity": orbit_size,
                "delta": delta,
                "k": minority_count,
                "delta_0_k_2_axes": zero_k2_axes,
            })
            residual_profiles[tuple(sorted(zip(delta, minority_count)))] += 1

    assert minority_triples == comb(len(ODD), 3)
    assert sum(row_totals.values()) == sum(
        row["majority_quadruples"] for row in triple_rows
    )
    assert sum(normalized_totals.values()) == sum(
        row["minority_multiplicity"] * row["majority_quadruples"]
        for row in triple_rows
    )
    assert normalized_totals["remaining"] == sum(
        record["orbit_multiplicity"] for record in remaining
    )
    normalized_unfiltered = minority_triples * comb(len(NONZERO_EVEN), 4)
    domains = {
        "normalized_unfiltered": normalized_unfiltered,
        "normalized_failed_short_independence": (
            normalized_unfiltered - sum(normalized_totals.values())
        ),
        "normalized_short_independent": sum(normalized_totals.values()),
        "minority_triples": minority_triples,
        "minority_orbits": len(triple_rows),
        "short_independent_with_canonical_minority": sum(row_totals.values()),
        "after_delta_1_2_3_with_canonical_minority": sum(
            row_totals[key] for key in ("delta_4", "delta_0_k_3", "remaining")
        ),
        "after_delta_1_2_3_normalized": sum(
            normalized_totals[key] for key in ("delta_4", "delta_0_k_3", "remaining")
        ),
        "after_all_gates": {
            "with_canonical_minority": row_totals["remaining"],
            "normalized": normalized_totals["remaining"],
            "full_s6_orbits": len(remaining),
        },
    }
    return {
        "convention": (
            "Vertices are decimal bitmasks. z=0, majority is even, "
            "minority is odd. Axis indices are 0..5, least significant first. "
            "Both delta and k are counted in the axis-zero face containing z. "
            "Orbit multiplicities count distinct z=0 geometries under S6."
        ),
        "scope": (
            "Geometry and candidate gate counts only. Coordinate matching "
            "constructions and original matching realizability are untested."
        ),
        "domains": domains,
        "gate_order": ALL_GATES,
        "first_gate_with_canonical_minority": row_totals,
        "first_gate_normalized": normalized_totals,
        "any_gate_with_canonical_minority": gate_incidence,
        "any_gate_normalized": normalized_gate_incidence,
        "minority_orbit_profiles": triple_rows,
        "residual_axis_profiles": [
            {"sorted_delta_k_pairs": profile, "full_s6_orbits": count}
            for profile, count in sorted(residual_profiles.items())
        ],
        "residual_list_complete": len(remaining) <= 1000,
        "residual_geometries": remaining if len(remaining) <= 1000 else remaining[:20],
    }


if __name__ == "__main__":
    print(json.dumps(exhaust(), separators=(",", ":"), sort_keys=True))
