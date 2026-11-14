"""Count scalar-valid high-m completions before enumerating qualifying triples."""

from collections import Counter
import json
from math import comb
from pathlib import Path
from time import process_time

from E16_MU3_CENTRAL_LOCAL_HIGH_M_BASE import minority_sets
from E16_MU3_CENTRAL_LOCAL_RECEIVER import AXES, USEFUL
from E16_MU3_ROUTE_SCALAR import remaining_columns
from E16_MU3_ROUTE_SCALAR_TRANSPOSE import transposed_hits


CPU_LIMIT = 10
QUALIFIED_LIMIT = 5_000
POOL_COUNT = 234
STATE_LIMIT = POOL_COUNT * 697


def coefficients(pool):
    """Multiply one point factor at a time, keeping degrees zero through three."""
    terms = [Counter({(0,) * 6: 1}), Counter(), Counter(), Counter()]
    for point in pool:
        bits = tuple(bool(point & axis) for axis in AXES)
        for degree in (3, 2, 1):
            for counts, ways in terms[degree - 1].items():
                updated = tuple(count + bit for count, bit in zip(counts, bits))
                terms[degree][updated] += ways
    assert all(sum(terms[degree].values()) == comb(len(pool), degree) for degree in range(4))
    return terms


def verify(h, m, W, Y, U, residual):
    S = (0, (1 << h) - 1)
    assert all(len(set(group)) == size for group, size in zip((U, Y, W, S), (3, 6, 5, 2)))
    assert all(point.bit_count() % 2 == parity
               for group, parity in zip((U, Y, W, S), (0, 1, 1, 0)) for point in group)
    assert set(U).isdisjoint(S) and set(Y).isdisjoint(W)
    assert all((u ^ y).bit_count() != 1 for u in U for y in Y)
    assert all((s ^ w).bit_count() != 1 for s in S for w in W)
    columns = [tuple(sum(bool(point & axis) for point in group) for group in (U, Y, W, S))
               for axis in AXES]
    assert all(column in residual for column in columns)
    assert min(3, *(abs(a + c - b - d) for a, b, c, d in columns)) == 3
    assert sum((c, d) in USEFUL for _, _, c, d in columns) == m


def run():
    started = process_time()

    def check_cpu():
        if process_time() - started > CPU_LIMIT:
            raise TimeoutError("high-m polynomial base exceeded its CPU limit")

    source_path = Path(__file__).with_name("E16_MU3_CENTRAL_LOCAL_HIGH_M_BASE.json")
    sources = json.loads(source_path.read_text())["valid_source_rows"]
    assert len(sources) == POOL_COUNT
    counts_by_h_m = Counter()
    states = 0
    preflight = []
    for row in sources:
        check_cpu()
        pool = row["U_pool"]
        assert len(set(pool)) == len(pool) <= 16
        allowed = tuple(set(values) for values in row["allowed_a"])
        terms = coefficients(pool)
        states += sum(len(degree) for degree in terms)
        assert states <= STATE_LIMIT
        count = sum(ways for signature, ways in terms[3].items()
                    if all(load in alphabet for load, alphabet in zip(signature, allowed)))
        counts_by_h_m[row["h"], row["m"]] += count
        preflight.append(count)
    qualified = sum(preflight)
    preflight_elapsed = process_time() - started
    residual = {row for row in remaining_columns(3, 2) if not transposed_hits(3, 2, row)}
    base = []
    if qualified <= QUALIFIED_LIMIT:
        for row, expected in zip(sources, preflight):
            check_cpu()
            h, m, W, Y = (row[key] for key in ("h", "m", "W", "Y"))
            before = len(base)
            for U in minority_sets(row["U_pool"], tuple(set(values) for values in row["allowed_a"])):
                if len(base) == QUALIFIED_LIMIT:
                    raise RuntimeError("high-m qualified base reached its fixed cap")
                verify(h, m, W, Y, U, residual)
                base.append({"h": h, "m": m, "W": W, "Y": Y, "U": U})
            assert len(base) - before == expected
        assert len(base) == qualified
    check_cpu()
    return {
        "qualified": qualified,
        "qualified_h_m": [[h, m, count] for (h, m), count in sorted(counts_by_h_m.items())],
        "source_rows_with_completions": sum(count > 0 for count in preflight),
        "preflight_per_source_row": preflight,
        "coalesced_states": states,
        "preflight_cpu_seconds": preflight_elapsed,
        "cpu_seconds": process_time() - started,
        "base_generated": qualified <= QUALIFIED_LIMIT,
        "base": base,
    }


if __name__ == "__main__":
    print(json.dumps(run(), separators=(",", ":")))
