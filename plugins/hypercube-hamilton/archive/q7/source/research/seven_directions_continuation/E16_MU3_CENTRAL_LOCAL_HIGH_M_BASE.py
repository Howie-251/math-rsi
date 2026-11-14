"""Build the bounded high-m (3,6)/(5,2) equality base for the scalar residual."""

from collections import Counter, defaultdict
from itertools import product
import json
from math import comb
from pathlib import Path
from time import process_time

from E16_MU3_CENTRAL_LOCAL_RECEIVER import AXES, USEFUL
from E16_MU3_ROUTE_SCALAR import remaining_columns
from E16_MU3_ROUTE_SCALAR_TRANSPOSE import transposed_hits


CPU_LIMIT = 10
SOURCE_LIMIT = 900
MINORITY_COMBINATION_LIMIT = 15_000
BASE_LIMIT = 3_000


def source_sets(loads):
    """Enumerate the capacity equality fibers with a parity-odd source."""
    useful = tuple((axis, pair) for axis, pair in zip(AXES, loads) if pair in USEFUL)
    assert len(useful) in (4, 5) and all(d == 1 for _, (_, d) in useful)
    mask = sum(axis for axis, _ in useful)
    flip = sum(axis for axis, (c, _) in useful if c == 2)
    odd_fibers = defaultdict(list)
    for point in range(64):
        if point.bit_count() % 2:
            odd_fibers[(point ^ flip) & mask].append(point)
    for units in product(*(odd_fibers[axis] for axis, _ in useful)):
        yield tuple(sorted((*odd_fibers[0], *units)))


def minority_pool(root, source, allowed_a):
    pool = tuple(point for point in range(64) if point.bit_count() % 2 == 0
                 and point not in (0, root)
                 and all((point ^ y).bit_count() != 1 for y in source))
    while len(pool) >= 3:
        permitted = []
        for axis, alphabet in zip(AXES, allowed_a):
            ones = sum(bool(point & axis) for point in pool)
            feasible = alphabet & set(range(max(0, 3 - len(pool) + ones), min(3, ones) + 1))
            if not feasible:
                return ()
            permitted.append(feasible)
        required_ones = sum(axis for axis, feasible in zip(AXES, permitted) if feasible == {3})
        required_zeros = sum(axis for axis, feasible in zip(AXES, permitted) if feasible == {0})
        reduced = tuple(point for point in pool if point & required_ones == required_ones
                        and not point & required_zeros)
        if reduced == pool:
            return pool
        pool = reduced
    return pool


def minority_sets(pool, allowed_a):
    """Extend a partial triple only if the remaining pool can meet every column."""
    suffix_ones = [(0,) * 6] * (len(pool) + 1)
    for index in reversed(range(len(pool))):
        suffix_ones[index] = tuple(count + bool(pool[index] & axis)
                                   for count, axis in zip(suffix_ones[index + 1], AXES))

    def visit(start, chosen, counts):
        need = 3 - len(chosen)
        left = len(pool) - start
        if left < need:
            return
        for count, ones, alphabet in zip(counts, suffix_ones[start], allowed_a):
            low, high = count + max(0, need - left + ones), count + min(need, ones)
            if alphabet.isdisjoint(range(low, high + 1)):
                return
        if not need:
            yield chosen
            return
        for index in range(start, len(pool) - need + 1):
            point = pool[index]
            updated = tuple(count + bool(point & axis) for count, axis in zip(counts, AXES))
            yield from visit(index + 1, (*chosen, point), updated)

    yield from visit(0, (), (0,) * 6)


def run():
    started = process_time()

    def check_cpu():
        if process_time() - started > CPU_LIMIT:
            raise TimeoutError("high-m equality base exceeded the CPU limit")

    data = json.loads(Path(__file__).with_name("E16_MU3_CENTRAL_LOCAL_RECEIVER.json").read_text())
    assert data["source_base_upper_bound_m_ge_4"] == SOURCE_LIMIT
    alphabet = defaultdict(set)
    for row in remaining_columns(3, 2):
        if not transposed_hits(3, 2, row):
            a, b, c, d = row
            alphabet[b, c, d].add(a)
    counters = Counter()
    valid_sources = []
    for entry in data["receivers"]:
        if not entry["source_bound"]:
            continue
        h, m, receiver = entry["h"], entry["m"], tuple(entry["W"])
        root = (1 << h) - 1
        loads = tuple(map(tuple, entry["loads_c_d"]))
        for source in source_sets(loads):
            check_cpu()
            counters["source_sets_generated"] += 1
            if counters["source_sets_generated"] > SOURCE_LIMIT:
                raise RuntimeError("high-m source generation exceeded its fixed cap")
            assert len(source) == len(set(source)) == 6
            if not set(source).isdisjoint(receiver):
                continue
            counters["disjoint_source_sets"] += 1
            allowed_a = tuple(alphabet[sum(bool(y & axis) for y in source), c, d]
                              for axis, (c, d) in zip(AXES, loads))
            if not all(allowed_a):
                continue
            counters["scalar_valid_source_sets"] += 1
            pool = minority_pool(root, source, allowed_a)
            valid_sources.append((h, m, receiver, source, allowed_a, pool))
    assert counters["source_sets_generated"] == SOURCE_LIMIT
    combinations_bound = sum(comb(len(pool), 3) for _, _, _, _, _, pool in valid_sources)
    records = []
    if combinations_bound <= MINORITY_COMBINATION_LIMIT:
        for h, m, receiver, source, allowed_a, pool in valid_sources:
            check_cpu()
            for minority in minority_sets(pool, allowed_a):
                if len(records) == BASE_LIMIT:
                    raise RuntimeError("high-m accepted base reached its fixed cap")
                records.append({"h": h, "m": m, "W": receiver, "Y": source, "U": minority})
    check_cpu()
    return {
        "counts": dict(counters),
        "sum_choose_pool_3": combinations_bound,
        "max_pool": max(len(pool) for _, _, _, _, _, pool in valid_sources),
        "pool_size_counts": dict(sorted(Counter(len(pool) for _, _, _, _, _, pool in valid_sources).items())),
        "valid_source_rows": [
            {"h": h, "m": m, "W": receiver, "Y": source,
             "allowed_a": [sorted(values) for values in allowed_a], "U_pool": pool}
            for h, m, receiver, source, allowed_a, pool in valid_sources
        ],
        "minority_base_generated": combinations_bound <= MINORITY_COMBINATION_LIMIT,
        "base_size": len(records),
        "base_counts_h_m": [[h, m, count] for (h, m), count in sorted(
            Counter((record["h"], record["m"]) for record in records).items())],
        "base": records,
        "cpu_seconds": process_time() - started,
    }


if __name__ == "__main__":
    print(json.dumps(run(), separators=(",", ":")))
