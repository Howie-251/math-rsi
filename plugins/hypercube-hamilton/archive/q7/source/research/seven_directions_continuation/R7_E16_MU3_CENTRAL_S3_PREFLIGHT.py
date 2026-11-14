"""Bound and count central s=3 sources using the 140-row residual alphabet."""

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations, product
import json
from math import comb, prod
from pathlib import Path
from time import process_time

from E16_MU3_CENTRAL_LOCAL_HIGH_M_POLYNOMIAL import coefficients
from E16_MU3_CENTRAL_LOCAL_HIGH_M_SOURCE_QUOTIENT import move, root_stabilizer
from E16_MU3_CENTRAL_LOCAL_RECEIVER import AXES, USEFUL


HERE = Path(__file__).resolve().parent
TEMPLATES = "R7_E16_MU3_CENTRAL_LOWM_PREFLIGHT_COUNT.json"
SCALAR = "R7_E16_MU3_CENTRAL_AFTER_R41_SCALAR_NOTE.json"
REVIEW = "R41_FULL_REVIEW.json"
INPUTS = {
    TEMPLATES: "59ae221dc88eb374927c390cee705165171a1e569a694ac9d88d8f27b2a0516f",
    SCALAR: "0623c86fec679e7e2b2e1fa06205a64d5605a20deaed43c9ce3afa30c3439dac",
    REVIEW: "3bbd1bae12da13e05fae0ea651e1fed4cdf97372dd99b7062bb424db06489f55",
}
FIBER_LIMIT = 200_000
CPU_LIMIT = 30
COMPUTE_LIMIT = 29
ODD = tuple(v for v in range(64) if v.bit_count() % 2)
EVEN = tuple(v for v in range(64) if not v.bit_count() % 2)
NEIGHBORS = {v: {v ^ axis for axis in AXES} for v in ODD}


def load_inputs():
    payloads = {}
    for name, expected in INPUTS.items():
        raw = (HERE / name).read_bytes()
        assert sha256(raw).hexdigest() == expected
        payloads[name] = json.loads(raw)
    old, scalar, review = (payloads[name] for name in (TEMPLATES, SCALAR, REVIEW))
    assert review["verdict"] == "PASS" and review["full_R41_proved"]
    before = sorted((a, b, entry["c"], entry["d"]) for entry in old["allowed_a_b_gap"]
                    for a, b, _ in entry["rows"])
    assert len(before) == 156
    assert sha256(json.dumps(before, separators=(",", ":")).encode()).hexdigest() == scalar["rows_before_sha256"]
    removed = set(map(tuple, scalar["removed_columns_abcd"]))
    assert removed == {row for row in before if (row[1] + row[3], row[0] + row[2])
                       in {(1, 4), (4, 1), (4, 7), (7, 4)}}
    after = set(before) - removed
    assert len(after) == 140
    assert after == {(3 - a, 6 - b, 5 - c, 2 - d) for a, b, c, d in after}
    alphabet = defaultdict(set)
    for a, b, c, d in after:
        alphabet[c, d, b].add(a)
    projection = {key: tuple(sorted(b for c, d, b in alphabet if (c, d) == key))
                  for key in {(c, d) for c, d, _ in alphabet}}
    assert projection == {(e["c"], e["d"]): tuple(e["b_after"]) for e in scalar["b_projections_by_cd"]}
    templates = []
    for row in old["rows"]:
        h, m, w = row["h"], row["m"], tuple(row["W"])
        if h not in (2, 4) or m > 2:
            continue
        s = (0, (1 << h) - 1)
        loads = tuple((sum(bool(v & bit) for v in w), sum(bool(v & bit) for v in s)) for bit in AXES)
        assert loads == tuple(map(tuple, row["loads_c_d"]))
        assert m == sum(load in USEFUL for load in loads)
        sparse = tuple(i for i, (c, d) in enumerate(loads) if c - d in (1, 2))
        if len(sparse) == 3:
            assert m == 2
            templates.append((h, s, w, loads, sparse))
    assert Counter(t[0] for t in templates) == {2: 32, 4: 2}
    assert len({(h, w) for h, _, w, _, _ in templates}) == len(templates)
    return templates, alphabet, projection


def fiber_jobs(w, sparse, choices):
    axes = tuple(AXES[i] for i in sparse)
    mask = sum(axes)
    for sparse_b in product(*(choices[i] for i in sparse)):
        assert all(b in (0, 1, 5, 6) for b in sparse_b)
        majority = sum(bit for bit, b in zip(axes, sparse_b) if b in (5, 6))
        active = tuple(bit for bit, b in zip(axes, sparse_b) if b in (1, 5))
        fibers = defaultdict(list)
        for point in ODD:
            if point not in w:
                fibers[(point ^ majority) & mask].append(point)
        assert len(fibers[0]) <= 4
        patterns = []
        if len(active) == 2:
            patterns.append(("four_zero_two_units", 4, active))
        if len(active) == 3:
            patterns.append(("three_zero_three_units", 3, active))
            patterns.extend(("four_zero_unit_pair", 4, (bit, mask ^ bit)) for bit in active)
        for mode, zero, supports in patterns:
            upper = comb(len(fibers[0]), zero) * prod(len(fibers[bit]) for bit in supports)
            yield sparse_b, mode, zero, supports, fibers, upper


def source_data(s, y, loads, alphabet):
    forbidden = set(s).union(*(NEIGHBORS[v] for v in y))
    pool = tuple(v for v in EVEN if v not in forbidden)
    b = tuple(sum(bool(v & bit) for v in y) for bit in AXES)
    allowed = tuple(tuple(sorted(alphabet[c, d, bi])) for (c, d), bi in zip(loads, b))
    return b, pool, allowed


def verify_transport(source, target, order, shift, action):
    b, pool, allowed = source
    target_b, target_pool, target_allowed = target
    assert move(pool, action) == target_pool
    for i, j in enumerate(order):
        flipped = bool(shift & AXES[j])
        assert (6 - b[i] if flipped else b[i]) == target_b[j]
        values = tuple(sorted(3 - a for a in allowed[i])) if flipped else allowed[i]
        assert values == target_allowed[j]


def run(start):
    def check():
        if process_time() - start >= COMPUTE_LIMIT:
            raise TimeoutError("central s=3 preflight CPU limit")

    templates, alphabet, projection = load_inputs()
    schedules = []
    results = []
    for h, s, w, loads, sparse in templates:
        choices = tuple(projection[load] for load in loads)
        jobs = tuple(fiber_jobs(w, sparse, choices))
        bounds = Counter()
        for _, mode, _, _, _, upper in jobs:
            bounds[mode] += upper
        schedules.append((choices, jobs))
        results.append(dict(h=h, S=s, W=w, m=2, s=3, loads_c_d=loads, sparse_axes=sparse,
                            sparse_allowed_b=[choices[i] for i in sparse], fiber_bound=sum(bounds.values()),
                            fiber_bounds_by_mode=bounds, zero_bound_modes=sum(not job[-1] for job in jobs),
                            positive_bound_modes=sum(bool(job[-1]) for job in jobs), complete=False,
                            counts=Counter(), source_representatives=[]))
    bound = sum(row["fiber_bound"] for row in results)
    status = "stopped_fiber_bound" if bound > FIBER_LIMIT else "complete"
    missing = None
    if bound <= FIBER_LIMIT:
        groups = {h: tuple(root_stabilizer(h)) for h in (2, 4)}
        try:
            for row, (choices, jobs) in zip(results, schedules):
                check()
                h, s, w, loads, sparse = (row[key] for key in ("h", "S", "W", "loads_c_d", "sparse_axes"))
                stats = row["counts"]
                sources = set()
                for sparse_b, mode, zero, supports, fibers, upper in jobs:
                    check()
                    visited = 0
                    for points in product(combinations(fibers[0], zero), *(fibers[key] for key in supports)):
                        y = tuple(sorted(points[0] + points[1:]))
                        assert len(set(y)) == 6
                        b = tuple(sum(bool(v & bit) for v in y) for bit in AXES)
                        assert tuple(b[i] for i in sparse) == sparse_b
                        visited += 1
                        if all(bi in allowed for bi, allowed in zip(b, choices)):
                            assert y not in sources
                            sources.add(y)
                    stats["raw_choices"] += visited
                    if visited != upper:
                        missing = dict(h=h, W=w, sparse_b=sparse_b, mode=mode, support=supports,
                                       expected=upper, visited=visited)
                        raise ValueError("fiber mode count mismatch")
                assert stats["raw_choices"] == row["fiber_bound"]
                stats["labeled_Y"] = len(sources)
                stabilizer = tuple((order, shift, action) for order, shift, action in groups[h]
                                   if move(w, action) == w)
                assert all(move(s, action) == s for _, _, action in stabilizer)
                row["receiver_stabilizer_size"] = len(stabilizer)
                row["receiver_stabilizer_root_exchange_count"] = sum(bool(shift) for _, shift, _ in stabilizer)
                geometry = {y: source_data(s, y, loads, alphabet) for y in sources}
                seen = set()
                for y in sorted(sources):
                    if y in seen:
                        continue
                    check()
                    orbit = {move(y, action) for _, _, action in stabilizer}
                    assert y == min(orbit) and orbit <= sources and not seen.intersection(orbit)
                    seen.update(orbit)
                    transport = []
                    for member in sorted(orbit):
                        order, shift, action = next(g for g in stabilizer if move(member, g[2]) == y)
                        verify_transport(geometry[member], geometry[y], order, shift, action)
                        transport.append(dict(Y=member, axis_destination=order, xor_after_permutation=shift))
                    b, pool, allowed = geometry[y]
                    exact = sum(n for a, n in coefficients(pool)[3].items()
                                if all(value in permit for value, permit in zip(a, allowed)))
                    assert exact <= comb(len(pool), 3)
                    stats["source_orbits"] += 1
                    stats["source_orbits_with_U"] += bool(exact)
                    stats["labeled_Y_with_U"] += len(orbit) * bool(exact)
                    stats["exact_U_on_source_reps"] += exact
                    stats["exact_labeled_Y_U"] += len(orbit) * exact
                    row["source_representatives"].append(dict(Y=y, b_loads=b, U_pool=pool, allowed_a=allowed,
                                                               exact_U=exact, source_orbit_size=len(orbit),
                                                               source_transport=transport))
                assert seen == sources
                row["complete"] = True
        except TimeoutError:
            status = "stopped_cpu_limit"
        except ValueError:
            if missing is None:
                raise
            status = "first_missing_mode"

    totals = Counter()
    grouped = defaultdict(Counter)
    for row in results:
        totals.update(row["counts"])
        grouped[row["h"]].update(row["counts"])
    return dict(status=status, inputs_sha256=INPUTS, fiber_bound=bound, fiber_limit=FIBER_LIMIT,
                first_missing_mode=missing, rows=results, totals=totals, counts_by_h=grouped,
                cpu_seconds_before_write=process_time() - start, cpu_limit_seconds=CPU_LIMIT,
                compute_cutoff_cpu_seconds=COMPUTE_LIMIT, complete_Y_generated=totals["raw_choices"],
                complete_U_generated=0, complete_geometries_generated=0, plan_searches=0,
                original_matchings_enumerated=0, solver_calls=0, rank_runs=0)


if __name__ == "__main__":
    result = run(process_time())
    with Path(__file__).with_suffix(".json").open("x", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(result, separators=(",", ":")) + "\n")
    print(json.dumps({key: value for key, value in result.items() if key != "rows"}))
