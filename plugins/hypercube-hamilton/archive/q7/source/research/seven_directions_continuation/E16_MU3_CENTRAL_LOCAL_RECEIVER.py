"""Inventory the local receiver face of the E16 (3,6)/(5,2) scalar residual."""

from collections import Counter
from itertools import combinations
import json
from math import comb
from time import process_time

from E16_MU3_ROUTE_SCALAR import remaining_columns
from E16_MU3_ROUTE_SCALAR_TRANSPOSE import transposed_hits


CPU_LIMIT = 20
LABELED_LIMIT = 57_342
AXES = tuple(1 << i for i in range(6))
USEFUL = {(2, 0), (2, 1), (3, 1), (3, 2)}
FORCES_ZERO_SPARSE_LOAD = {(2, 0), (3, 2)}


def source_projection():
    rows = [row for row in remaining_columns(3, 2) if not transposed_hits(3, 2, row)]
    assert len(rows) == 166
    allowed = {pair: set() for pair in ((c, d) for c in range(6) for d in range(3))}
    for _, b, c, d in rows:
        allowed[c, d].add(b)
    assert {pair for pair, loads in allowed.items() if loads <= {0, 1, 5, 6}} == USEFUL
    assert {pair for pair, loads in allowed.items() if loads <= {0, 6}} == FORCES_ZERO_SPARSE_LOAD
    return allowed


def generators(h):
    """Generate the stabilizer of the unordered even root pair {0, 2**h-1}."""
    root = (1 << h) - 1
    yield tuple(point ^ root for point in range(64))
    for index in range(5):
        if index == h - 1:
            continue
        axis = 1 << index
        yield tuple(point ^ (3 * axis) if ((point ^ (point >> 1)) & axis) else point
                    for point in range(64))


def receiver_orbits(pool, h, check_budget):
    actions = tuple(generators(h))
    visited = set()
    for receiver in combinations(pool, 5):
        check_budget()
        if receiver in visited:
            continue
        orbit = {receiver}
        frontier = [receiver]
        for current in frontier:
            for action in actions:
                target = tuple(sorted(action[point] for point in current))
                if target not in orbit:
                    orbit.add(target)
                    frontier.append(target)
        assert receiver == min(orbit) and orbit.isdisjoint(visited)
        visited.update(orbit)
        yield receiver, len(orbit)
    assert len(visited) == comb(len(pool), 5)


def source_bound(loads, allowed):
    """Upper bound for odd six-point source sets, from scalar projections alone."""
    useful = [pair for pair in loads if pair in USEFUL]
    m = len(useful)
    if m < 4:
        return None
    if any(pair in FORCES_ZERO_SPARSE_LOAD for pair in useful):
        return 0
    # Flip the c=2 axes so their sparse bit 0 becomes 1.
    offset_is_odd = sum(pair == (2, 1) for pair in useful) % 2
    if m == 6:
        return int(not offset_is_odd)
    if m == 5:
        remaining = next(pair for pair in loads if pair not in USEFUL)
        required_b = 5 if offset_is_odd else 1
        return int(required_b in allowed[remaining])
    return 16


def summarize():
    start = process_time()
    examined = 0

    def check_budget():
        nonlocal examined
        examined += 1
        if examined > LABELED_LIMIT or process_time() - start > CPU_LIMIT:
            raise TimeoutError("local receiver inventory exceeded its bound")

    allowed = source_projection()
    orbits_by_h_m = Counter()
    labeled_by_h_m = Counter()
    bounds_by_h_m = Counter()
    records = []
    for h, pool_size in ((2, 22), (4, 20), (6, 20)):
        root = (1 << h) - 1
        pool = tuple(point for point in range(64) if point.bit_count() >= 3
                     and point.bit_count() % 2 and (point ^ root).bit_count() >= 3)
        assert len(pool) == pool_size
        for receiver, orbit_size in receiver_orbits(pool, h, check_budget):
            loads = tuple((sum(bool(point & axis) for point in receiver), int(bool(root & axis)))
                          for axis in AXES)
            m = sum(pair in USEFUL for pair in loads)
            bound = source_bound(loads, allowed)
            orbits_by_h_m[h, m] += 1
            labeled_by_h_m[h, m] += orbit_size
            bounds_by_h_m[h, m, bound] += 1
            records.append({"h": h, "W": receiver, "labeled_orbit_size": orbit_size,
                            "loads_c_d": loads, "m": m, "source_bound": bound})
    assert examined == sum(labeled_by_h_m.values()) == LABELED_LIMIT
    elapsed = process_time() - start
    if elapsed > CPU_LIMIT:
        raise TimeoutError("local receiver inventory exceeded its CPU bound")
    return {
        "b_by_d_c": [[sorted(allowed[c, d]) for c in range(6)] for d in range(3)],
        "h_m_orbit_labeled": [[h, m, count, labeled_by_h_m[h, m]]
                              for (h, m), count in sorted(orbits_by_h_m.items())],
        "h_m_source_bound_orbits": [[h, m, bound, count]
                                     for (h, m, bound), count in sorted(bounds_by_h_m.items())],
        "source_base_upper_bound_m_ge_4": sum(record["source_bound"] or 0 for record in records),
        "cpu_seconds": elapsed,
        "receivers": records,
    }


if __name__ == "__main__":
    print(json.dumps(summarize(), separators=(",", ":")))
