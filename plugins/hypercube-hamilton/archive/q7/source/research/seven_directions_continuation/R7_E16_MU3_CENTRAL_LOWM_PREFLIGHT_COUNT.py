"""Bound central low-m sources by coefficients and sparse-fiber capacity."""

from collections import Counter, defaultdict
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
from math import comb
from pathlib import Path
from time import process_time

import numpy as np

from E16_MU3_CENTRAL_LOCAL_RECEIVER import AXES, USEFUL
from E16_MU3_ROUTE_SCALAR import remaining_columns
from E16_MU3_ROUTE_SCALAR_TRANSPOSE import transposed_hits


CPU_LIMIT = 20
HERE = Path(__file__).resolve().parent
ODD = tuple(v for v in range(64) if v.bit_count() % 2)
EVEN = tuple(v for v in range(64) if v.bit_count() % 2 == 0)
NEIGHBORS = {v: {v ^ bit for bit in AXES} for v in range(64)}


def check_budget(start):
    if process_time() - start >= CPU_LIMIT:
        raise TimeoutError("central low-m source preflight exceeded its CPU limit")


def tables():
    old = [row for row in remaining_columns(3, 2) if not transposed_hits(3, 2, row)]
    limited = defaultdict(list)
    for a, b, c, d in old:
        if abs(a + c - b - d) <= 6:
            limited[c, d].append((a, b, abs(a + c - b - d)))
    assert len(old) == 166
    assert {(b, c, d) for _, b, c, d in old} == {
        (b, c, d) for (c, d), rows in limited.items() for _, b, _ in rows
    }
    return old, limited


def key(point, base):
    return sum(base ** i for i, bit in enumerate(AXES) if point & bit)


def polynomial(pool, degree):
    base = degree + 1
    coefficients = np.zeros((base, base ** 6), dtype=np.int32)
    coefficients[0, 0] = 1
    for index, point in enumerate(pool, 1):
        shift = key(point, base)
        for k in range(min(index, degree), 0, -1):
            coefficients[k, shift:] += coefficients[k - 1, :base ** 6 - shift]
    assert coefficients[degree].sum() == comb(len(pool), degree)
    return coefficients


def source_coefficients(full, w):
    # Divide by the five factors for excluded points, degree by degree.
    coefficients = full.copy()
    for point in w:
        shift = key(point, 7)
        for k in range(1, 7):
            coefficients[k, shift:] -= coefficients[k - 1, :7 ** 6 - shift]
    result = coefficients[6].reshape((7,) * 6, order="F")
    assert result.sum() == comb(27, 6) and result.min() >= 0
    return result


@lru_cache(maxsize=512)
def minority_coefficients(pool):
    return polynomial(pool, 3)[3].reshape((4,) * 6, order="F")


def shrink_minority(pool, columns):
    while len(pool) >= 3:
        forced = []
        for bit, rows in zip(AXES, columns):
            ones = sum(bool(v & bit) for v in pool)
            lower, upper = max(0, 3 - len(pool) + ones), min(3, ones)
            allowed = {a for a, _, _ in rows if lower <= a <= upper}
            if not allowed:
                return ()
            if allowed == {0} or allowed == {3}:
                forced.append((bit, 3 in allowed))
        new = tuple(v for v in pool if all(bool(v & bit) == value for bit, value in forced))
        if new == pool:
            return pool
        pool = new
    return ()


def coupled_counts(coefficients, columns, pool, max_gap):
    weights = minority_coefficients(pool)
    for rows in columns:
        matrix = np.zeros((4, len(rows)), dtype=np.int32)
        for j, choices in enumerate(rows):
            for a, gap in choices:
                if gap <= max_gap:
                    matrix[a, j] = 1
        weights = np.tensordot(weights, matrix, axes=(0, 0))
    assert weights.shape == coefficients.shape
    return int(coefficients[weights > 0].sum()), int(np.sum(coefficients * weights, dtype=np.int64))


def analyze_template(entry, full, alphabet):
    h, m = entry["h"], entry["m"]
    w = tuple(entry["W"])
    s = (0, (1 << h) - 1)
    y_pool = tuple(v for v in ODD if v not in w)
    u_pool = tuple(v for v in EVEN if v not in s)
    loads = tuple(map(tuple, entry["loads_c_d"]))
    assert loads == tuple((sum(bool(v & bit) for v in w), int(bool(s[1] & bit))) for bit in AXES)
    sparse_axes = tuple(i for i, load in enumerate(loads) if load in USEFUL)
    assert len(sparse_axes) == m
    choices = tuple(tuple(sorted({b for _, b, _ in alphabet[load]})) for load in loads)
    source_tensor = source_coefficients(full, w)
    source_projection_count = int(source_tensor[np.ix_(*choices)].sum())
    counts = Counter()
    sparse_cases = []
    for sparse_values in product(*(choices[i] for i in sparse_axes)):
        columns = list(choices)
        for i, value in zip(sparse_axes, sparse_values):
            columns[i] = (value,)
        coeffs = source_tensor[np.ix_(*columns)]
        sources = int(coeffs.sum())
        if not sources:
            continue
        counts["nonempty_source_patterns"] += 1
        # At most k sources have a nonzero sparse projection after flipping the
        # majority bits to zero. All other sources lie in the zero fiber.
        mask = sum(AXES[i] for i in sparse_axes)
        majority = sum(AXES[i] for i, b in zip(sparse_axes, sparse_values) if b >= 5)
        k = sum(b in (1, 5) for b in sparse_values)
        zero_fiber = {v for v in y_pool if v & mask == majority}
        assert len(zero_fiber) >= 6 - k
        if len(zero_fiber) == 6 - k:
            counts["source_patterns_filling_zero_fiber"] += 1
        constant = sum(AXES[i] for i, b in zip(sparse_axes, sparse_values) if b in (0, 6))
        # Each U candidate must leave enough room for Y in its zero fiber.
        candidate_u = tuple(v for v in u_pool if len(zero_fiber - NEIGHBORS[v]) >= 6 - k)
        relations = [tuple(row for row in alphabet[load] if row[1] in values)
                     for load, values in zip(loads, columns)]
        candidate_u = shrink_minority(candidate_u, relations)
        if len(candidate_u) < 3:
            counts["minority_capacity_empty_patterns"] += 1
            continue
        row_alphabets = [tuple(tuple((a, gap) for a, b, gap in rows if b == value)
                               for value in values)
                         for rows, values in zip(relations, columns)]
        y_count, pair_count = coupled_counts(coeffs, row_alphabets, candidate_u, 6)
        _, pair_without_six = coupled_counts(coeffs, row_alphabets, candidate_u, 5)
        assert pair_without_six <= pair_count and y_count <= sources
        if not pair_count:
            counts["joint_load_empty_patterns"] += 1
            continue
        counts["source_upper_bound"] += y_count
        counts["pair_upper_bound"] += pair_count
        counts["pair_upper_bound_no_gap_six"] += pair_without_six
        sparse_cases.append(dict(b=sparse_values, constant_mask=constant, zero_fiber_size=len(zero_fiber),
                                 zero_fiber_minimum=6-k, U_pool_size=len(candidate_u),
                                 source_upper_bound=y_count, pair_upper_bound=pair_count,
                                 pair_upper_bound_no_gap_six=pair_without_six))
    return dict(h=h, m=m, W=w, loads_c_d=loads, b_projection=choices, sparse_axes=sparse_axes,
                source_projection_count=source_projection_count, **{
                    field: counts[field] for field in (
                        "source_upper_bound", "pair_upper_bound", "pair_upper_bound_no_gap_six",
                        "nonempty_source_patterns", "source_patterns_filling_zero_fiber",
                        "minority_capacity_empty_patterns",
                        "joint_load_empty_patterns",
                    )
                }, sparse_cases=sparse_cases)


def run():
    start = process_time()
    payload = (HERE / "E16_MU3_CENTRAL_LOCAL_RECEIVER.json").read_bytes()
    templates = [r for r in json.loads(payload)["receivers"] if r["m"] <= 3]
    assert Counter(r["h"] for r in templates) == {2: 407, 4: 148, 6: 7}
    old, alphabet = tables()
    full = polynomial(ODD, 6)
    groups = defaultdict(Counter)
    rows = []
    for entry in templates:
        check_budget(start)
        result = analyze_template(entry, full, alphabet)
        rows.append(result)
        stats = groups[result["h"], result["m"]]
        stats["templates"] += 1
        stats["nonempty_templates"] += int(result["pair_upper_bound"] > 0)
        stats["nonempty_templates_no_gap_six"] += int(result["pair_upper_bound_no_gap_six"] > 0)
        for field in ("source_projection_count", "source_upper_bound", "pair_upper_bound",
                      "pair_upper_bound_no_gap_six", "source_patterns_filling_zero_fiber"):
            stats[field] += result[field]
    check_budget(start)
    return dict(receiver_template_sha256=sha256(payload).hexdigest(), templates=len(templates),
                scalar_rows_before=Counter(abs(a+c-b-d) for a,b,c,d in old),
                scalar_rows_after=sum(map(len, alphabet.values())),
                allowed_a_b_gap=[dict(c=c, d=d, rows=values) for (c,d), values in sorted(alphabet.items())],
                grouped=[dict(h=h, m=m, **stats) for (h,m), stats in sorted(groups.items())],
                rows=rows, cpu_seconds=process_time()-start, cpu_limit_seconds=CPU_LIMIT,
                complete_Y_generated=0, complete_U_generated=0, plans=0,
                original_matchings_enumerated=0, solver_calls=0, rank_runs=0)


if __name__ == "__main__":
    start = process_time()
    result = run()
    output = json.dumps(result, separators=(",", ":"))
    check_budget(start)
    with Path(__file__).with_suffix(".json").open("x", encoding="utf-8", newline="\n") as file:
        file.write(output + "\n")
    print(json.dumps({key: value for key, value in result.items() if key not in ("rows", "allowed_a_b_gap")},
                     indent=2))
