"""Count the two failed-receiver branches after the 140-row filter."""

from collections import Counter, defaultdict
from hashlib import sha256
from math import comb
from pathlib import Path
from time import process_time
import json


HERE = Path(__file__).resolve().parent
CPU_LIMIT = 10
CANDIDATE_LIMIT = 10000
SOURCE_LIMIT = 1145
AXES = tuple(1 << i for i in range(6))
EVEN = tuple(v for v in range(64) if v.bit_count() % 2 == 0)
PACKED = {v: sum(bool(v & bit) << (2 * i) for i, bit in enumerate(AXES)) for v in EVEN}

INPUTS = {
    "bridge_diagnostic_2026_11_15/THREE_BRIDGE_RECEIVER_CAPACITY.json": None,
    "R7_E16_MU3_CENTRAL_LOWM_PREFLIGHT_COUNT.json":
        "59ae221dc88eb374927c390cee705165171a1e569a694ac9d88d8f27b2a0516f",
    "R7_E16_MU3_CENTRAL_AFTER_R41_SCALAR_NOTE.json":
        "0623c86fec679e7e2b2e1fa06205a64d5605a20deaed43c9ce3afa30c3439dac",
}


def load_inputs():
    data = []
    actual_hashes = {}
    for name, expected in INPUTS.items():
        raw = (HERE.parent / name).read_bytes()
        actual = sha256(raw).hexdigest()
        assert expected is None or expected == actual
        data.append(json.loads(raw))
        actual_hashes[name] = actual

    capacity, preflight, scalar = data
    before = sorted(
        (a, b, row["c"], row["d"])
        for row in preflight["allowed_a_b_gap"]
        for a, b, _ in row["rows"]
    )
    serialized = json.dumps(before, separators=(",", ":")).encode()
    assert len(before) == 156 and sha256(serialized).hexdigest() == scalar["rows_before_sha256"]
    removed = set(map(tuple, scalar["removed_columns_abcd"]))
    assert len(removed) == 16 and removed <= set(before)
    after = set(before) - removed
    assert len(after) == 140
    assert after == {(3-a, 6-b, 5-c, 2-d) for a, b, c, d in after}
    allowed = defaultdict(set)
    for a, b, c, d in after:
        allowed[c, d, b].add(a)
    exceptions = capacity["capacity_does_not_rule_out_receiver_failure"]
    return exceptions, allowed, actual_hashes


def column_load(points):
    return tuple(sum(bool(p & bit) for p in points) for bit in AXES)


def sources(pool, allowed_loads, started):
    """Generate accepted six-sets using coordinatewise suffix bounds."""
    suffix = [column_load(pool[i:]) for i in range(len(pool) + 1)]

    def visit(start, chosen, loads):
        if process_time() - started >= CPU_LIMIT:
            raise TimeoutError("CPU limit reached during source generation")
        need = 6 - len(chosen)
        remaining = len(pool) - start
        if remaining < need:
            return
        for have, ones, permitted in zip(loads, suffix[start], allowed_loads):
            low = have + max(0, need - (remaining - ones))
            high = have + min(need, ones)
            if not any(low <= b <= high for b in permitted):
                return
        if need == 0:
            yield chosen, loads
            return
        for i in range(start, len(pool) - need + 1):
            v = pool[i]
            new_loads = tuple(load + bool(v & bit) for load, bit in zip(loads, AXES))
            yield from visit(i + 1, chosen + (v,), new_loads)

    yield from visit(0, (), (0,) * 6)


def donor_pool(source, roots):
    excluded = set(roots) | {y ^ bit for y in source for bit in AXES}
    return tuple(v for v in EVEN if v not in excluded)


def degree_three_coefficients(pool):
    # Base 4 keeps the six exponents independent through degree three.
    terms = [Counter({0: 1}), Counter(), Counter(), Counter()]
    for v in pool:
        monomial = PACKED[v]
        for degree in (3, 2, 1):
            for previous, count in terms[degree - 1].items():
                terms[degree][previous + monomial] += count
    assert sum(terms[3].values()) == comb(len(pool), 3)
    return terms[3]


def missing_pair_orbit(x, y):
    # For W2, permute high axes 3, 4, 5 and interchange the two points.
    # Axis 2 stays fixed by W2.
    below = tuple(sorted(((x >> 2) & 1, (y >> 2) & 1)))
    upper = (x >> 3, y >> 3)
    if below[0] != below[1] and x & 4:
        upper = upper[::-1]
    weights = tuple(v.bit_count() for v in upper)
    if below[0] == below[1]:
        weights = tuple(sorted(weights))
    return below, weights, (upper[0] & upper[1]).bit_count()


def count_exception(template, allowed, started, tally):
    w = tuple(template["W"])
    roots = tuple(template["receiver_minority_roots"])
    fixed = tuple(map(tuple, template["g0_bits"]))
    pool = tuple(
        v for v in range(64)
        if v.bit_count() % 2 and v not in w
        and all((v >> axis) & 1 == bit for axis, bit in fixed)
    )
    assert list(pool) == template["available_odd_vertices"]
    cd = tuple(zip(column_load(w), column_load(roots)))
    projected = tuple(
        tuple(b for b in range(7) if (c, d, b) in allowed)
        for c, d in cd
    )
    assert projected == tuple(map(tuple, template["allowed_bit1_source_loads_b"]))

    positive_sources = 0
    total = 0
    first_positive = None
    fiber_stats = defaultdict(Counter)
    pool_profile = Counter()
    source_multiplicities = Counter()
    example_missing_orbits = []
    per_load = Counter()
    per_fixed_axis_load = Counter()
    for y, b in sources(pool, projected, started):
        tally["sources"] += 1
        if tally["sources"] > SOURCE_LIMIT:
            raise RuntimeError("Source cap reached")
        allowed_a = tuple(allowed[c, d, value] for value, (c, d) in zip(b, cd))
        available = donor_pool(y, roots)
        fibers = tuple(sum(v & 3 == t for v in available) for t in range(4))
        pool_profile[fibers] += 1
        missing = tuple(sorted(set(pool) - set(y))) if len(pool) == 8 else ()
        if missing:
            assert fibers == (7, 2, 2, 0)
        valid = 0
        for packed, multiplicity in degree_three_coefficients(available).items():
            a = tuple((packed >> (2 * i)) & 3 for i in range(6))
            if all(value in permitted for value, permitted in zip(a, allowed_a)):
                valid += multiplicity
                per_fixed_axis_load[a[:len(fixed)]] += multiplicity
        by_low_source_load = fiber_stats[b[:2]]
        by_low_source_load["projected_sources"] += 1
        by_low_source_load["nonzero_sources"] += bool(valid)
        by_low_source_load["admissible_completion_count"] += valid
        source_multiplicities[valid] += 1
        if valid:
            positive_sources += 1
            total += valid
            per_load[b] += valid
            if first_positive is None:
                first_positive = {"Y": y, "b": b, "donor_pool": available, "count": valid}
        if missing:
            example_missing_orbits.append({
                "Y": y, "excluded_pair": missing, "excluded_pair_distance": (missing[0] ^ missing[1]).bit_count(),
                "excluded_pair_orbit": missing_pair_orbit(*missing), "count": valid,
            })

    projected_count = sum(source_multiplicities.values())
    assert projected_count == template["subsets_counted_after_projection"]
    return {
        "W": w, "receiver_minority_roots": roots, "F_fixed": fixed,
        "source_pool": pool,
        "projected_sources": projected_count,
        "sources_with_nonzero_completion": positive_sources,
        "total_admissible_completions": total,
        "maximum_completions_for_one_source": max(source_multiplicities),
        "first_positive_source": first_positive,
        "completion_multiplicity_histogram_count_to_sources": sorted(source_multiplicities.items()),
        "source_fiber_stats_by_b0_b1": sorted(fiber_stats.items()),
        "pool_profile_fiber_order_00_01_10_11": sorted(pool_profile.items()),
        "completions_by_a_on_F_fixed_axes": sorted(per_fixed_axis_load.items()),
        "completions_by_b": sorted(per_load.items()),
        "W2_sources_by_excluded_pair": example_missing_orbits,
    }


def main():
    started = process_time()
    exceptions, allowed, hashes = load_inputs()
    unfiltered = sum(comb(len(row["available_odd_vertices"]), 6) for row in exceptions)
    assert unfiltered <= CANDIDATE_LIMIT
    tally = {"sources": 0}
    result = [count_exception(template, allowed, started, tally) for template in exceptions]
    assert tally["sources"] == SOURCE_LIMIT
    elapsed = process_time() - started
    assert elapsed < CPU_LIMIT
    output = {
        "input_SHA256": hashes,
        "scope": "Independent hole geometry and 140 necessary scalar rows. Coefficients only for U.",
        "axis_encoding": "Bit 0 has weight 1. Fiber labels print bit 1 followed by bit 0.",
        "full_Y_cap": SOURCE_LIMIT, "full_Y_generated": tally["sources"],
        "candidate_cap": CANDIDATE_LIMIT, "unfiltered_source_space": unfiltered,
        "full_U_generated": 0, "full_hole_geometries_generated": 0,
        "original_matchings_enumerated": 0, "solver_calls": 0,
        "combined_admissible_completion_count": sum(r["total_admissible_completions"] for r in result),
        "exceptions": result, "CPU_limit_seconds": CPU_LIMIT, "CPU_seconds": elapsed,
    }
    (HERE / "EXCEPTION_PREFLIGHT.json").write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps([
        {key: row[key] for key in (
            "W", "projected_sources", "sources_with_nonzero_completion",
            "total_admissible_completions", "maximum_completions_for_one_source",
            "first_positive_source", "source_fiber_stats_by_b0_b1",
            "completions_by_a_on_F_fixed_axes",
        )} for row in result
    ], indent=2))
    print(f"CPU: {elapsed:.3f} sec")


if __name__ == "__main__":
    main()
