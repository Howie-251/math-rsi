import hashlib
import itertools
import json
from collections import Counter, deque
from pathlib import Path


HERE = Path(__file__).resolve().parent
GEOMETRY = HERE / "geometry.json"
OBSTRUCTIONS = HERE / "zero_delta_obstructions.json"
RESULT = HERE / "Q6_A8_FULL_REVIEW_check.json"
VERTICES = tuple(range(64))
EVEN_NONZERO = tuple(v for v in VERTICES if v and v.bit_count() % 2 == 0)
ODD = tuple(v for v in VERTICES if v.bit_count() % 2 == 1)
GATE_ORDER = ("delta_2", "delta_3", "delta_1", "delta_4", "delta_0_k_3")


def swap_coordinate_bits(vertex, axis):
    left = (vertex >> axis) & 1
    right = (vertex >> (axis + 1)) & 1
    return vertex ^ ((3 << axis) if left != right else 0)


GENERATORS = tuple(
    tuple(swap_coordinate_bits(v, axis) for v in VERTICES)
    for axis in range(5)
)


def orbit(start):
    """Orbit of a tuple of ordered vertex sets under adjacent coordinate swaps."""
    found = {start}
    pending = deque([start])
    while pending:
        current = pending.popleft()
        for perm in GENERATORS:
            moved = tuple(tuple(sorted(perm[v] for v in group)) for group in current)
            if moved not in found:
                found.add(moved)
                pending.append(moved)
    return found


def axis_profile(minority, other_majority):
    for axis in range(6):
        bit = 1 << axis
        k = sum((v & bit) == 0 for v in minority)
        majority_in_a = 1 + sum((v & bit) == 0 for v in other_majority)
        yield majority_in_a - k, k


def applicable_gates(minority, other_majority):
    flags = set()
    for delta, k in axis_profile(minority, other_majority):
        if 1 <= delta <= 4:
            flags.add(f"delta_{delta}")
        if (delta, k) == (0, 3):
            flags.add("delta_0_k_3")
    return flags


def independent_census():
    all_minority = {(triple,) for triple in itertools.combinations(ODD, 3)}
    remainder = set(all_minority)
    canonical_count = normalized_count = 0
    orbit_sizes = []
    max_majority_options = 0
    residual_seeds = set()
    residual_counts = Counter()
    any_normalized, any_canonical = Counter(), Counter()
    first_normalized, first_canonical = Counter(), Counter()
    while remainder:
        representative = min(remainder)
        pat = orbit(representative)
        assert pat <= remainder
        remainder -= pat
        weight = len(pat)
        orbit_sizes.append(weight)
        minority, = representative
        options = tuple(
            v for v in EVEN_NONZERO
            if all((v ^ h).bit_count() != 1 for h in minority)
        )
        max_majority_options = max(max_majority_options, len(options))
        for other_majority in itertools.combinations(options, 4):
            normalized_count += weight
            canonical_count += 1
            gates = applicable_gates(minority, other_majority)
            any_normalized.update({name: weight for name in gates})
            any_canonical.update(gates)
            first = next((name for name in GATE_ORDER if name in gates), "remaining")
            first_normalized[first] += weight
            first_canonical[first] += 1
            if first == "remaining":
                residual_seeds.add((minority, other_majority))
                residual_counts["normalized"] += weight
                residual_counts["with_canonical_minority"] += 1

    # Quotient the marked geometries under simultaneous coordinate swaps.
    remaining_seeds = set(residual_seeds)
    residual_orbits = {}
    while remaining_seeds:
        seed = min(remaining_seeds)
        full_orbit = orbit(seed)
        assert all(not applicable_gates(*point) for point in full_orbit)
        hits = full_orbit & remaining_seeds
        assert hits
        remaining_seeds -= hits
        representative = min(full_orbit)
        assert representative not in residual_orbits
        residual_orbits[representative] = len(full_orbit)
    assert sum(residual_orbits.values()) == residual_counts["normalized"]
    assert sum(orbit_sizes) == len(all_minority)

    return {
        "minority_triples": len(all_minority),
        "minority_orbits": len(orbit_sizes),
        "max_majority_options": max_majority_options,
        "short_independent_with_canonical_minority": canonical_count,
        "normalized_short_independent": normalized_count,
        "any_gate_normalized": dict(any_normalized),
        "any_gate_with_canonical_minority": dict(any_canonical),
        "first_gate_normalized": dict(first_normalized),
        "first_gate_with_canonical_minority": dict(first_canonical),
        "residual_counts": dict(residual_counts),
        "residual_orbits": residual_orbits,
    }


def signature_classes(minority, other_majority):
    axes = tuple(
        j for j, profile in enumerate(axis_profile(minority, other_majority))
        if profile == (0, 2)
    )
    holes = {0, *minority, *other_majority}
    slices = {}
    mirrors = {}
    for j in axes:
        b = 1 << j
        mirrors[j] = {h ^ b for h in minority if (h & b) == 0}
        assert len(mirrors[j]) == 2 and not (mirrors[j] & holes)
        slices[j] = {v for v in VERTICES if (v & b)} - mirrors[j]
    signs = {}
    for v in VERTICES:
        if v not in holes:
            s = sum(1 << j for j in axes if v in slices[j])
            signs.setdefault(s, []).append(v)
    return axes, mirrors, signs


def independent_fiber(minority, other_majority):
    axes, mirrors, signs = signature_classes(minority, other_majority)
    signature = min(s for s, vertices in signs.items() if len(vertices) % 2 == 1)
    return {
        "minority": minority,
        "other_majority": other_majority,
        "axes": axes,
        "mirrors": {j: sorted(pair) for j, pair in mirrors.items()},
        "odd_signature": signature,
        "covered_vertices": signs[signature],
    }


def main():
    computed = independent_census()
    patterns = computed.pop("residual_orbits")
    fibers = []
    for h, multiplicity in sorted(patterns.items()):
        entry = independent_fiber(*h)
        entry["orbit_multiplicity"] = multiplicity
        fibers.append(entry)

    # Read producer output only after constructing the complete independent result.
    producer_bytes = GEOMETRY.read_bytes()
    producer = json.loads(producer_bytes)
    for key in (
        "minority_triples",
        "minority_orbits",
        "short_independent_with_canonical_minority",
        "normalized_short_independent",
    ):
        assert computed[key] == producer["domains"][key], key
    for key in (
        "any_gate_normalized",
        "any_gate_with_canonical_minority",
        "first_gate_normalized",
        "first_gate_with_canonical_minority",
    ):
        assert computed[key] == producer[key], key
    assert set(producer["domains"]["after_all_gates"]) == {
        "normalized", "with_canonical_minority", "full_s6_orbits"
    }
    assert {**computed["residual_counts"], "full_s6_orbits": len(patterns)} == (
        producer["domains"]["after_all_gates"]
    )
    producer_patterns = {}
    for row in producer["residual_geometries"]:
        pattern = (tuple(row["minority"]), tuple(row["other_majority"]))
        full_orbit = orbit(pattern)
        representative = min(full_orbit)
        assert representative not in producer_patterns
        assert len(full_orbit) == row["orbit_multiplicity"]
        producer_patterns[representative] = row["orbit_multiplicity"]
    assert patterns == producer_patterns
    obstruction_bytes = OBSTRUCTIONS.read_bytes()
    author_fibers = json.loads(obstruction_bytes)
    assert len(author_fibers) == len(patterns)
    author_patterns = set()
    for author in author_fibers:
        point = (tuple(author["minority"]), tuple(author["other_majority"]))
        author_patterns.add(min(orbit(point)))
        axes, mirrors, signs = signature_classes(*point)
        assert set(author["odd_signature"]) <= set(axes)
        assert author["mirrors_by_axis"] == {str(j): sorted(pair) for j, pair in mirrors.items()}
        signature = sum(1 << j for j in author["odd_signature"])
        assert author["odd_covered_vertices"] == signs[signature]
        assert len(signs[signature]) % 2 == 1
    assert author_patterns == set(patterns)
    record = {
        "verdict": "PASS",
        "scope": "Independently exhausts marked hole geometries; checks all seven odd fibers. No prescribed matchings enumerated.",
        "producer_sha256": hashlib.sha256(producer_bytes).hexdigest(),
        "producer_obstructions_sha256": hashlib.sha256(obstruction_bytes).hexdigest(),
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        **computed,
        "residual_orbits": fibers,
    }
    RESULT.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(
        f"PASS: {computed['minority_orbits']} minority orbits, "
        f"{computed['short_independent_with_canonical_minority']} canonical-minority "
        f"inputs, {computed['normalized_short_independent']} normalized inputs, "
        f"{len(fibers)} residual orbits with odd fibers"
    )


if __name__ == "__main__":
    main()
