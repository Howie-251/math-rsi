"""Count exact three-point completions for central s=2 receivers with a strong column."""

from collections import Counter
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
from time import process_time

from R7_E16_MU3_CENTRAL_S2_PREFLIGHT import AXES, ODD, STRONG, read_inputs, shapes
from R7_E16_MU3_CENTRAL_S3_PREFLIGHT import coefficients, move, root_stabilizer, source_data, verify_transport


CPU_LIMIT = 30
COMPUTE_LIMIT = 29
MAX_FIBER_CHOICES = 25000
MAX_SOURCES = 4491
MAX_RELAXED_PAIRS = 64438
COARSE_INPUT = Path(__file__).with_name("R7_E16_MU3_CENTRAL_S2_PREFLIGHT.json")


def run(start):
    templates, allowed, projection = read_inputs()
    selected = [t for t in templates if any(t[4][i] in STRONG for i in t[5])]
    assert Counter(t[0] for t in selected) == {2: 72, 4: 4}
    groups = {h: tuple(root_stabilizer(h)) for h in (2, 4)}
    coarse = json.loads(COARSE_INPUT.read_bytes())
    assert coarse["status"] == "complete"
    bounds = {(row["h"], tuple(row["W"])): row for row in coarse["templates"] if row["strong_columns"]}
    assert len(bounds) == len(selected)
    assert sum(r["fiber_choices"] for r in bounds.values()) <= MAX_FIBER_CHOICES
    assert sum(r["projected_Y"] for r in bounds.values()) == MAX_SOURCES
    assert sum(r["relaxed_pairs"] for r in bounds.values()) == MAX_RELAXED_PAIRS
    rows = []
    for h, s, w, m, loads, sparse in selected:
        if process_time() - start >= COMPUTE_LIMIT:
            break
        expected = bounds[h, w]
        mask = sum(AXES[i] for i in sparse)
        candidates = 0
        sources = {}
        projected = tuple(projection[load] for load in loads)
        for values in product(*(projected[i] for i in sparse)):
            assert sum(value in (1, 5) for value in values) <= 1
            occupied = sum(AXES[i] for i, value in zip(sparse, values) if value in (5, 6))
            for _, pattern in shapes(values, sparse):
                fibers = [tuple(v for v in ODD if v not in w and ((v ^ occupied) & mask) == j)
                          for j, _ in pattern]
                assert all(len(fiber) <= 8 for fiber in fibers)
                for groups_of_points in product(*(combinations(fiber, size)
                                                  for fiber, (_, size) in zip(fibers, pattern))):
                    y = tuple(sorted(v for part in groups_of_points for v in part))
                    candidates += 1
                    b = tuple(sum(bool(v & bit) for v in y) for bit in AXES)
                    assert tuple(b[i] for i in sparse) == values
                    if all(bi in permit for bi, permit in zip(b, projected)):
                        assert y not in sources
                        sources[y] = source_data(s, y, loads, allowed)
        assert candidates == expected["fiber_choices"] and len(sources) == expected["projected_Y"]

        stabilizer = tuple((order, shift, action) for order, shift, action in groups[h] if move(w, action) == w)
        assert all(move(s, action) == s for _, _, action in stabilizer)
        counts = Counter(raw_choices=candidates, labeled_Y=len(sources), source_orbits=0, source_orbits_with_U=0,
                         root_exchange_transports=0, exact_U_on_source_reps=0, exact_labeled_Y_U=0)
        seen = set()
        reps = []
        for y, data in sorted(sources.items()):
            if y in seen:
                continue
            orbit = {move(y, action) for _, _, action in stabilizer}
            assert y == min(orbit) and orbit <= sources.keys() and not seen.intersection(orbit)
            seen.update(orbit)
            transport = []
            for member in sorted(orbit):
                order, shift, action = next(g for g in stabilizer if move(member, g[2]) == y)
                verify_transport(sources[member], data, order, shift, action)
                counts["root_exchange_transports"] += bool(shift)
                transport.append(dict(Y=member, axis_destination=order, xor_after_permutation=shift))
            b, pool, permits = data
            exact = sum(count for load, count in coefficients(pool)[3].items()
                        if all(a in permit for a, permit in zip(load, permits)))
            counts["source_orbits"] += 1
            counts["source_orbits_with_U"] += bool(exact)
            counts["exact_U_on_source_reps"] += exact
            counts["exact_labeled_Y_U"] += len(orbit) * exact
            reps.append(dict(Y=y, b_loads=b, U_pool=pool, allowed_a=permits, exact_U=exact,
                             source_orbit_size=len(orbit), source_transport=transport))
        assert seen == sources.keys() and counts["exact_labeled_Y_U"] <= expected["relaxed_pairs"]
        rows.append(dict(h=h, m=m, s=2, S=s, W=w, loads_c_d=loads, sparse_axes=sparse,
                         strong_columns=expected["strong_columns"],
                         receiver_stabilizer_size=len(stabilizer), counts=counts, source_representatives=reps))

    totals = Counter()
    by_h = {2: Counter(), 4: Counter()}
    for row in rows:
        totals.update(row["counts"])
        by_h[row["h"]].update(row["counts"])
    assert totals["raw_choices"] <= MAX_FIBER_CHOICES and totals["labeled_Y"] <= MAX_SOURCES
    assert totals["exact_labeled_Y_U"] <= MAX_RELAXED_PAIRS
    status = "complete" if len(rows) == len(selected) else "stopped_cpu_limit"
    if status == "complete":
        assert totals["raw_choices"] == 22336 and totals["labeled_Y"] == MAX_SOURCES
    return dict(
        status=status, template_count=len(rows), expected_templates=len(selected), rows=rows, totals=totals,
        counts_by_h=by_h,
        scope="Necessary-domain preflight for the 76 h=2 or 4, s=2 receivers with at least one strong constant column. Proposed structural theorem has s>=2 and at least one strong constant column, with accepted s>=3 and h=6 imported.",
        coarse_preflight_sha256=sha256(COARSE_INPUT.read_bytes()).hexdigest(),
        fiber_choice_cap=MAX_FIBER_CHOICES, projected_Y_cap=MAX_SOURCES, relaxed_pair_cap=MAX_RELAXED_PAIRS,
        cpu_seconds_before_write=process_time()-start, cpu_limit_seconds=CPU_LIMIT,
        compute_cutoff_cpu_seconds=COMPUTE_LIMIT, complete_Y_generated=totals["raw_choices"], complete_U_generated=0,
        complete_geometries_generated=0, plan_searches=0, original_matchings_enumerated=0,
        solver_calls=0, rank_runs=0,
    )


if __name__ == "__main__":
    result = run(process_time())
    with Path(__file__).with_suffix(".json").open("x", encoding="utf-8", newline="\n") as out:
        json.dump(result, out, indent=2)
        out.write("\n")
    print(json.dumps({key: value for key, value in result.items() if key != "rows"}))
