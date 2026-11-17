"""Independent standard-library certificate checker; never imports the producer.

Coordinate orbits use the multiset of six 3-bit column patterns, with the two
unmarked majority rows interchangeable. No coordinate permutations are used.
Run: python verify_q7_initial.py
"""
from pathlib import Path
from collections import Counter, defaultdict
from itertools import combinations
from math import factorial, prod
from hashlib import sha256
import json

ROOT = Path(__file__).resolve().parent


def read(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def edge(u, v):
    return tuple(sorted((u, v)))


def short(u, v):
    return (u ^ v).bit_count() == 1


def matching_holes(n, pairs):
    endpoints = [v for pair in pairs for v in pair]
    assert all(len(pair) == 2 for pair in pairs)
    assert all(type(v) is int and 0 <= v < 2**n for v in endpoints)
    assert len(endpoints) == len(set(endpoints))
    return set(range(2**n)) - set(endpoints)


def patterns(z, a, b):
    count = Counter(4*((z >> j) & 1) + 2*((a >> j) & 1) + ((b >> j) & 1)
                    for j in range(6))
    return tuple(count[k] for k in range(8))


def signature(z, a, b):
    return min(patterns(z, a, b), patterns(z, b, a))


def good_directions(z, a, b):
    return [j for j in range(6) if (z >> j) & 1 and ((a ^ b) >> j) & 1]


def block_test(z, a, b):
    directions = good_directions(z, a, b)
    mask = sum(1 << j for j in directions)
    counts = Counter(v & mask for v in range(64) if v not in (0, z, a, b))
    return any(c % 2 for c in counts.values())


def main():
    witness = read("Q7_ROOTED_WITNESS.json")
    pairs, root = witness["matching"], witness["root"]
    holes = matching_holes(7, pairs)
    assert root == 0 and root in holes
    assert all(short(*p) for p in pairs)
    assert len(pairs) == witness["size"] == 47
    assert sorted(holes) == witness["holes"] and len(holes) == 34
    # A matching is inclusion-maximal on Q7-root iff its other holes
    # induce no cube edge. Test all hole pairs, independent of cube generation.
    assert all(not short(u, v) for u, v in combinations(holes - {root}, 2))

    geometry = read("Q6_A4_GEOMETRY.json")
    odd = [v for v in range(64) if v.bit_count() % 2]
    nonadj = [v for v in odd if v.bit_count() != 1]
    groups = defaultdict(list)
    total_normalized = augmentation_closed = 0
    for a, b in combinations(odd, 2):
        for z in odd:
            if z in (a, b):
                continue
            total_normalized += 1
            if short(0, a) or short(0, b):
                augmentation_closed += 1
            else:
                groups[signature(z, a, b)].append((z, a, b))
    assert total_normalized == 14880 and augmentation_closed == 5130
    assert len(nonadj) == 26 and len(groups) == 52
    assert sum(map(len, groups.values())) == geometry["domain_count"] == 9750
    assert geometry["orbit_count"] == 52 and geometry["minority_hole"] == 0
    indexed = {}
    checked_orbits = []
    for i, orbit in enumerate(geometry["orbits"]):
        z, a, b = orbit["representative"]
        key = signature(z, a, b)
        assert key not in indexed
        indexed[key] = i
        members = groups[key]
        assert (z, a, b) == min(members)
        count = patterns(z, a, b)
        # S6 orbit-stabilizer, quotienting the unmarked row exchange only
        # when that exchange already fixes the column multiplicities.
        orbit_size = factorial(6) // prod(factorial(c) for c in count)
        if count == patterns(z, b, a):
            orbit_size //= 2
        assert orbit_size == len(members) == orbit["size"]
        good = good_directions(z, a, b)
        assert good == orbit["good_directions"]
        assert orbit["z_weight"] == z.bit_count()
        assert orbit["span"] == (z | a | b).bit_count()
        forced = block_test(z, a, b)
        assert forced == orbit["crossing_forced_by_odd_block"]
        assert all(block_test(*m) == forced for m in members)
        checked_orbits.append({"index": i, "signature": key, "size": orbit_size,
                               "forced": forced, "good_count": len(good)})
    assert set(indexed) == set(groups)
    forced_orbits = [o for o in checked_orbits if o["forced"]]
    forced_geometries = sum(o["size"] for o in forced_orbits)
    assert len(forced_orbits) == geometry["universally_closed_orbits_by_positive_cut"] == 18
    assert forced_geometries == geometry["universally_closed_geometries_by_positive_cut"] == 3540
    no_good = sum(not o["good_count"] for o in checked_orbits)
    zero_possible = sum(bool(o["good_count"]) and not o["forced"] for o in checked_orbits)
    assert no_good == 12 and zero_possible == 22
    remaining_file_checked = False
    if (ROOT / "Q6_A4_REMAINING.json").exists():
        remaining = read("Q6_A4_REMAINING.json")
        expected = {i: o for i, o in enumerate(geometry["orbits"])
                    if not o["crossing_forced_by_odd_block"]}
        assert len(remaining) == 34
        assert {r["orbit_index"] for r in remaining} == set(expected)
        for row in remaining:
            original = expected[row["orbit_index"]]
            assert all(row[k] == v for k, v in original.items())
            assert row["kind"] == ("all_good_crossings_zero" if original["good_directions"]
                                    else "no_good_direction")
        remaining_file_checked = True

    pilot = read("Q6_A4_PILOT.json")
    families = Counter()
    per_orbit = Counter()
    case_results = []
    for i, case in enumerate(pilot["cases"]):
        assert case["status"] == "FOUND"
        pairs, z, cycle = case["matching"], case["forbidden"], case["cycle"]
        holes = matching_holes(6, pairs)
        assert len(pairs) == 30 and holes == set(case["holes"])
        assert len(holes) == 4 and 0 in holes and z in holes and z != 0
        others = holes - {0, z}
        assert all(v.bit_count() % 2 for v in holes - {0})
        a, b = sorted(others)
        assert a in nonadj and b in nonadj
        orbit_id = case["orbit"]
        assert indexed[signature(z, a, b)] == orbit_id
        assert [z, a, b] == geometry["orbits"][orbit_id]["representative"]
        assert all(type(v) is int for v in cycle)
        assert len(cycle) == len(set(cycle)) == 63
        assert set(cycle) == set(range(64)) - {z}
        ce = {edge(cycle[k], cycle[(k+1) % 63]) for k in range(63)}
        required = {edge(*p) for p in pairs}
        assert len(ce) == 63 and required <= ce
        assert all(short(*p) for p in ce - required)
        kind = case["kind"]
        assert kind in ("uniform", "parity_mixed", "half_layer", "zero_good_crossings")
        if kind == "parity_mixed":
            assert sum(not (u.bit_count() % 2 or v.bit_count() % 2) for u, v in pairs) == 1
            assert not any(u.bit_count() % 2 and v.bit_count() % 2 for u, v in pairs)
        elif kind == "half_layer":
            # Independently allow either half-layer parity rather than the
            # producer's selected parity convention.
            assert any({edge(v, v ^ (1 << j)) for v in range(64)
                        if not ((v >> j) & 1) and v.bit_count() % 2 == p} <= required
                       for j in range(6) for p in range(2))
        elif kind == "zero_good_crossings":
            good = good_directions(z, a, b)
            assert good and not block_test(z, a, b)
            assert all(not (((u ^ v) >> j) & 1) for u, v in pairs for j in good)
        families[kind] += 1
        per_orbit[orbit_id] += 1
        case_results.append({"index": i, "orbit": orbit_id, "kind": kind,
                             "matching_and_cycle_valid": True,
                             "new_short_edges": len(ce - required)})
    assert len(case_results) == 157 and pilot["summary"] == {"FOUND": 157}
    assert families == {"uniform": 52, "parity_mixed": 52, "half_layer": 31, "zero_good_crossings": 22}
    assert set(per_orbit) == set(range(52)) and min(per_orbit.values()) >= 2
    # Check uniqueness of the advertised orbit/family grid.
    assert len({(c["orbit"], c["kind"]) for c in pilot["cases"]}) == 157
    files = ["PROOF_PACKAGE.md", "Q7_ROOTED_WITNESS.json", "Q6_A4_GEOMETRY.json",
             "Q6_A4_PILOT.json", "q7_initial_probe.py", "verify_q7_initial.py"]
    if remaining_file_checked:
        files.append("Q6_A4_REMAINING.json")
    hashes = {n: sha256((ROOT/n).read_bytes()).hexdigest() for n in files}
    result = {"status": "PASS", "checker": "independent standard-library implementation",
              "producer_imported_or_executed": False, "coordinate_permutations_enumerated": False,
              "hashes": hashes, "rooted_witness": {"edges": 47, "holes": 34, "maximal_after_root_deletion": True},
              "geometry": {"normalized": total_normalized, "augmentation_closed": augmentation_closed,
                           "remaining": 9750, "orbits": 52, "forced_orbits": 18,
                           "forced_geometries": 3540, "all_closed_geometries": 8670,
                           "remaining_orbits": 34, "remaining_geometries": 6210,
                           "no_good_orbits": no_good, "zero_good_crossings_possible_orbits": zero_possible},
              "families": dict(families), "all_157_cycles_valid": True,
              "remaining_file_exact_complement_checked": remaining_file_checked,
              "universal_matching_enumeration": False, "orbits": checked_orbits,
              "cases": case_results}
    (ROOT/"verify_q7_initial_summary.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k not in ("hashes", "orbits", "cases")}, indent=2))


if __name__ == "__main__":
    main()
