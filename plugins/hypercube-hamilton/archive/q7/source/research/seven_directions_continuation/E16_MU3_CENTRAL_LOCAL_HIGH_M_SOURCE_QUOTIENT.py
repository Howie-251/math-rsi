"""Quotient the fixed high-m source rows by the exact common receiver stabilizer."""

from collections import Counter
from itertools import permutations, product
import json
from pathlib import Path
from time import process_time

from E16_MU3_CENTRAL_LOCAL_HIGH_M_BASE import minority_sets
from E16_MU3_CENTRAL_LOCAL_HIGH_M_POLYNOMIAL import (
    CPU_LIMIT, POOL_COUNT, QUALIFIED_LIMIT, STATE_LIMIT, coefficients, verify,
)
from E16_MU3_CENTRAL_LOCAL_RECEIVER import AXES
from E16_MU3_ROUTE_SCALAR import remaining_columns
from E16_MU3_ROUTE_SCALAR_TRANSPOSE import transposed_hits


def root_stabilizer(h):
    root = (1 << h) - 1
    for left, right in product(permutations(range(h)), permutations(range(h, 6))):
        order = left + right
        permuted = tuple(sum(1 << target for axis, target in zip(AXES, order) if point & axis)
                         for point in range(64))
        for shift in (0, root):
            yield order, shift, tuple(point ^ shift for point in permuted)


def move(points, action):
    return tuple(sorted(action[point] for point in points))


def verify_row_transport(row, target, order, shift, action):
    assert move(row["U_pool"], action) == tuple(target["U_pool"])
    for source_axis, target_axis in enumerate(order):
        values = row["allowed_a"][source_axis]
        if shift & AXES[target_axis]:
            values = sorted(3 - value for value in values)
        assert values == target["allowed_a"][target_axis]


def run():
    started = process_time()

    def check_cpu():
        if process_time() - started > CPU_LIMIT:
            raise TimeoutError("high-m common source quotient exceeded its CPU limit")

    data_path = Path(__file__).with_name("E16_MU3_CENTRAL_LOCAL_HIGH_M_BASE.json")
    sources = json.loads(data_path.read_text())["valid_source_rows"]
    assert len(sources) == POOL_COUNT
    index_of = {(row["h"], tuple(row["W"]), tuple(row["Y"])): index
                for index, row in enumerate(sources)}
    assert len(index_of) == len(sources)
    groups = {h: tuple(root_stabilizer(h)) for h in sorted({row["h"] for row in sources})}
    receiver_groups = {}
    representatives = set()
    transports = []
    for index, row in enumerate(sources):
        check_cpu()
        h, W, Y = row["h"], tuple(row["W"]), tuple(row["Y"])
        if (h, W) not in receiver_groups:
            receiver_groups[h, W] = tuple((order, shift, action) for order, shift, action in groups[h]
                                           if move(W, action) == W)
        canonical, order, shift, action = min((move(Y, action), order, shift, action)
                                              for order, shift, action in receiver_groups[h, W])
        target_index = index_of[h, W, canonical]
        verify_row_transport(row, sources[target_index], order, shift, action)
        representatives.add(target_index)
        transports.append({"source_row": index, "representative_row": target_index,
                           "axis_destination": order, "xor_after_permutation": shift})

    counts_by_h_m = Counter()
    preflight = {}
    states = 0
    for index in sorted(representatives):
        check_cpu()
        row = sources[index]
        allowed = tuple(set(values) for values in row["allowed_a"])
        terms = coefficients(row["U_pool"])
        states += sum(len(degree) for degree in terms)
        assert states <= STATE_LIMIT
        count = sum(ways for signature, ways in terms[3].items()
                    if all(load in alphabet for load, alphabet in zip(signature, allowed)))
        preflight[index] = count
        counts_by_h_m[row["h"], row["m"]] += count
    qualified = sum(preflight.values())
    residual = {row for row in remaining_columns(3, 2) if not transposed_hits(3, 2, row)}
    base = []
    if qualified <= QUALIFIED_LIMIT:
        for index, expected in preflight.items():
            check_cpu()
            row = sources[index]
            h, m, W, Y = (row[key] for key in ("h", "m", "W", "Y"))
            before = len(base)
            allowed = tuple(set(values) for values in row["allowed_a"])
            for U in minority_sets(row["U_pool"], allowed):
                if len(base) == QUALIFIED_LIMIT:
                    raise RuntimeError("high-m quotient base reached its fixed cap")
                verify(h, m, W, Y, U, residual)
                base.append({"h": h, "m": m, "W": W, "Y": Y, "U": U})
            assert len(base) - before == expected
        assert len(base) == qualified
    check_cpu()
    return {
        "source_rows": len(sources),
        "representative_source_rows": len(representatives),
        "representative_source_rows_with_completions": sum(count > 0 for count in preflight.values()),
        "coalesced_states": states,
        "qualified": qualified,
        "qualified_h_m": [[h, m, count] for (h, m), count in sorted(counts_by_h_m.items())],
        "source_row_transports": transports,
        "representative_rows_and_completion_counts": sorted(preflight.items()),
        "base_generated": qualified <= QUALIFIED_LIMIT,
        "base": base,
        "cpu_seconds": process_time() - started,
    }


if __name__ == "__main__":
    print(json.dumps(run(), separators=(",", ":")))
