"""Count the central s=2 receiver families without constructing sources or completions."""

from collections import Counter, defaultdict
from functools import cache
from hashlib import sha256
from itertools import product
import json
from math import comb, prod
from pathlib import Path
from time import process_time

from E16_MU3_CENTRAL_LOCAL_HIGH_M_POLYNOMIAL import coefficients
from R7_E16_MU3_CENTRAL_S3_PREFLIGHT import AXES, EVEN, INPUTS as SCALAR_INPUTS, ODD, USEFUL


HERE = Path(__file__).resolve().parent
RECEIVERS = "E16_MU3_CENTRAL_LOCAL_RECEIVER.json"
SCALAR = "R7_E16_MU3_CENTRAL_AFTER_R41_SCALAR_NOTE.json"
LOW_M = "R7_E16_MU3_CENTRAL_LOWM_PREFLIGHT_COUNT.json"
S3_REVIEW = "R7_E16_MU3_CENTRAL_S3_REVIEW.json"
INPUTS = {
    **SCALAR_INPUTS,
    RECEIVERS: "076bb20f38a17688bed5c247950addaeb95b6a1aae86de4babbbc13c035e75b0",
    S3_REVIEW: "bbbad5bdd633a02a105d8e9c598cb66d89811a0f27bb069d55e5eb01ec6b4750",
}
STRONG = {(2, 0), (3, 2)}
HALF_SPARSE = {(1, 1), (4, 1)}
CPU_LIMIT = 25
COMPUTE_LIMIT = 24
NEIGHBORS = {u: frozenset(u ^ axis for axis in AXES) for u in EVEN}
PACKED = {point: sum(1 << (3 * i) for i, bit in enumerate(AXES) if point & bit) for point in ODD}
SHAPES = ("zero6", "zero5_unit", "zero4_two_units", "zero5_pair")
COUNT_KEYS = ("fiber_choices", "projected_Y", "relaxed_pairs", "modes", "positive_modes")


def accepted_central_s3_cuts(colors):
    """Return (outer, receiver_side, majority_parity, sparse_axes) for physical hole sets."""
    if tuple(map(len, colors)) != (8, 8):
        return ()
    gaps = tuple(sum(v >> i & 1 for v in colors[0]) - sum(v >> i & 1 for v in colors[1])
                 for i in range(7))
    if min(map(abs, gaps)) != 3:
        return ()

    witnesses = []
    for outer, gap in enumerate(gaps):
        if abs(gap) != 3:
            continue
        for receiver_side in (0, 1):
            halves = tuple(tuple(v for v in points if (v >> outer & 1) == receiver_side)
                           for points in colors)
            counts = tuple(map(len, halves))
            if counts not in ((5, 2), (2, 5)):
                continue
            majority_parity = counts.index(5)
            major, minor = halves[majority_parity], halves[1 - majority_parity]
            sparse = tuple(i for i in range(7) if i != outer
                           and sum(v >> i & 1 for v in major) - sum(v >> i & 1 for v in minor) in (1, 2))
            if len(sparse) >= 3:
                witnesses.append((outer, receiver_side, majority_parity, sparse))
    return tuple(witnesses)


def read_inputs():
    data = {}
    for name, digest in INPUTS.items():
        raw = (HERE / name).read_bytes()
        assert sha256(raw).hexdigest() == digest
        data[name] = json.loads(raw)
    assert data[S3_REVIEW]["verdict"] == "PASS" and data[S3_REVIEW]["central_s_ge3_proved"]
    assert data["R41_FULL_REVIEW.json"]["verdict"] == "PASS"
    old, scalar = data[LOW_M], data[SCALAR]
    before = sorted((a, b, row["c"], row["d"]) for row in old["allowed_a_b_gap"] for a, b, _ in row["rows"])
    assert len(before) == 156
    assert sha256(json.dumps(before, separators=(",", ":")).encode()).hexdigest() == scalar["rows_before_sha256"]
    removed = {row for row in before if (row[1] + row[3], row[0] + row[2])
               in {(1, 4), (4, 1), (4, 7), (7, 4)}}
    assert removed == set(map(tuple, scalar["removed_columns_abcd"])) and len(removed) == 16
    after = set(before) - removed
    assert len(after) == 140
    assert after == {(3 - a, 6 - b, 5 - c, 2 - d) for a, b, c, d in after}
    allowed = defaultdict(set)
    for a, b, c, d in after:
        allowed[c, d, b].add(a)
    projection = {(row["c"], row["d"]): tuple(row["b_after"]) for row in scalar["b_projections_by_cd"]}
    assert {(c, d, b) for (c, d), values in projection.items() for b in values} == allowed.keys()
    assert all(projection[load] == (0, 6) for load in STRONG)

    receivers = data[RECEIVERS]["receivers"]
    assert len(receivers) == len({(row["h"], tuple(row["W"])) for row in receivers}) == 704
    templates = []
    for row in receivers:
        h, w = row["h"], tuple(row["W"])
        if h not in (2, 4):
            continue
        s = (0, (1 << h) - 1)
        loads = tuple((sum(bool(v & bit) for v in w), sum(bool(v & bit) for v in s)) for bit in AXES)
        assert loads == tuple(map(tuple, row["loads_c_d"]))
        assert row["m"] == sum(load in USEFUL for load in loads)
        sparse = tuple(i for i, (c, d) in enumerate(loads) if c - d in (1, 2))
        if len(sparse) == 2:
            templates.append((h, s, w, row["m"], loads, sparse))
    assert Counter((h, m) for h, _, _, m, _, _ in templates) == {(2, 1): 16, (2, 2): 139, (4, 2): 52}
    return templates, allowed, projection


@cache
def point_coefficients(fiber, size):
    terms = [Counter({0: 1})] + [Counter() for _ in range(size)]
    for point in fiber:
        for degree in range(size, 0, -1):
            for load, count in terms[degree - 1].items():
                terms[degree][load + PACKED[point]] += count
    assert sum(terms[size].values()) == comb(len(fiber), size)
    return terms[size]


def source_coefficients(groups):
    total = Counter({0: 1})
    for fiber, size in groups:
        terms = point_coefficients(fiber, size)
        updated = Counter()
        for p, count in total.items():
            for q, ways in terms.items():
                updated[p + q] += count * ways
        total = updated
    return total


@cache
def completion_masks(pool):
    """Give each unit of a three-point coefficient one bit in the scalar filter."""
    by_axis = [[0] * 4 for _ in AXES]
    offset = 0
    for load, count in coefficients(pool)[3].items():
        segment = ((1 << count) - 1) << offset
        for i, value in enumerate(load):
            by_axis[i][value] |= segment
        offset += count
    masks = tuple(tuple(sum(counts[a] for a in range(4) if subset >> a & 1)
                        for subset in range(16)) for counts in by_axis)
    return (1 << offset) - 1, masks


def shapes(sparse_b, sparse):
    active = tuple(AXES[i] for i, b in zip(sparse, sparse_b) if b in (1, 5))
    if len(active) == 0:
        return (("zero6", ((0, 6),)),)
    if len(active) == 1:
        return (("zero5_unit", ((0, 5), (active[0], 1))),)
    first, second = active
    return (("zero4_two_units", ((0, 4), (first, 1), (second, 1))),
            ("zero5_pair", ((0, 5), (first | second, 1))))


def count_template(template, allowed, projection):
    h, roots, w, m, loads, sparse = template
    projected = tuple(projection[load] for load in loads)
    mask = sum(AXES[i] for i in sparse)
    summary = {name: Counter(fiber_choices=0, projected_Y=0, relaxed_pairs=0, modes=0, positive_modes=0)
               for name in SHAPES}
    filters = tuple({b: sum(1 << a for a in allowed[c, d, b]) for b in choices}
                    for (c, d), choices in zip(loads, projected))
    for sparse_b in product(*(projected[i] for i in sparse)):
        assert all(b in (0, 1, 5, 6) for b in sparse_b)
        majority = sum(AXES[i] for i, b in zip(sparse, sparse_b) if b in (5, 6))
        fibers = {j: tuple(v for v in ODD if v not in w and ((v ^ majority) & mask) == j)
                  for j in (0, *(AXES[i] for i in sparse), mask)}
        assert all(len(fiber) <= 8 for fiber in fibers.values()) and sum(map(len, fibers.values())) == 27
        for name, pattern in shapes(sparse_b, sparse):
            counts = summary[name]
            groups = tuple((fibers[j], size) for j, size in pattern)
            bound = prod(comb(len(fiber), size) for fiber, size in groups)
            counts["modes"] += 1
            counts["positive_modes"] += bool(bound)
            counts["fiber_choices"] += bound
            if not bound:
                continue

            pool = tuple(u for u in EVEN if u not in roots
                         and all(len(fiber) - len(NEIGHBORS[u].intersection(fiber)) >= size
                                 for fiber, size in groups))
            full, masks = completion_masks(pool)
            terms = source_coefficients(groups)
            assert sum(terms.values()) == bound
            for packed, n_y in terms.items():
                b = tuple(packed >> (3 * i) & 7 for i in range(6))
                assert tuple(b[i] for i in sparse) == sparse_b
                permitted = tuple(f.get(bi, 0) for f, bi in zip(filters, b))
                if not all(permitted):
                    continue
                counts["projected_Y"] += n_y
                matched = full
                for i, subset in enumerate(permitted):
                    matched &= masks[i][subset]
                counts["relaxed_pairs"] += n_y * matched.bit_count()

    total = {key: sum(counts[key] for counts in summary.values()) for key in COUNT_KEYS}
    return dict(h=h, S=roots, W=w, m=m, s=2, loads_c_d=loads, sparse_axes=sparse,
                strong_columns=sum(load in STRONG for load in loads),
                half_sparse_columns=sum(load in HALF_SPARSE for load in loads), by_shape=summary, **total)


def aggregate(rows):
    counts = {key: sum(row[key] for row in rows) for key in COUNT_KEYS}
    by_shape = {name: {key: sum(row["by_shape"][name][key] for row in rows) for key in COUNT_KEYS}
                for name in SHAPES}
    return dict(templates=len(rows), **counts, by_shape=by_shape)


def run(start):
    templates, allowed, projection = read_inputs()
    rows = []
    for template in templates:
        if process_time() - start >= COMPUTE_LIMIT:
            break
        rows.append(count_template(template, allowed, projection))
    buckets = defaultdict(list)
    for row in rows:
        key = row["h"], row["m"], row["strong_columns"], row["half_sparse_columns"]
        buckets[key].append(row)
    cohorts = {"all_s2": rows,
               "h4_all_s2": [row for row in rows if row["h"] == 4],
               "at_least_one_strong": [row for row in rows if row["strong_columns"]],
               "two_strong": [row for row in rows if row["strong_columns"] == 2],
               "h4_at_least_one_strong": [row for row in rows if row["h"] == 4 and row["strong_columns"]],
               "h4_two_strong": [row for row in rows if row["h"] == 4 and row["strong_columns"] == 2]}
    return dict(
        status="complete" if len(rows) == len(templates) else "stopped_cpu_limit",
        scope="Necessary-domain local counts for all h=2 or 4, s=2 receivers; no joint all-axis peeling yet.",
        inputs_sha256=INPUTS, necessary_scalar_rows=140, expected_templates=len(templates),
        cohorts={name: aggregate(group) for name, group in cohorts.items()},
        buckets=[dict(h=h, m=m, strong_columns=strong, half_sparse_columns=half, **aggregate(group))
                 for (h, m, strong, half), group in sorted(buckets.items())],
        templates=rows, cpu_seconds_before_write=process_time()-start, cpu_limit_seconds=CPU_LIMIT,
        compute_cutoff_cpu_seconds=COMPUTE_LIMIT, complete_Y_generated=0, complete_U_generated=0,
        complete_geometries_generated=0, plan_searches=0, original_matchings_enumerated=0,
        solver_calls=0, rank_runs=0,
    )


if __name__ == "__main__":
    result = run(process_time())
    with Path(__file__).with_suffix(".json").open("x", encoding="utf-8", newline="\n") as out:
        json.dump(result, out, indent=2)
        out.write("\n")
    print(json.dumps({key: result[key] for key in ("status", "cpu_seconds_before_write", "cohorts")}))
