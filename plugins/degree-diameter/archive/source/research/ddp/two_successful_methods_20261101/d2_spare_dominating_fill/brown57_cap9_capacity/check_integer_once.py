#!/usr/bin/env python3
"""One small arithmetic check; no graph data, search, or external packages."""
import json
from pathlib import Path
import resource
import time

out_dir = Path(__file__).resolve().parent
start_cpu = time.process_time()
start_wall = time.monotonic()

assert 8 * 2 + 49 == 65

def polynomial(h):
    return 57 * h * h - 1170 * h + 4225

assert polynomial(16) == 97
assert polynomial(17) - polynomial(16) == 711
assert 114 * 16 - 1113 == 711
# The forward difference 114*h-1113 grows strictly with h. Thus this
# base case proves that the polynomial is positive for every integer h>=16.

def balanced_square_sum(h, B):
    q, r = divmod(B, h)
    return (h - r) * q * q + r * (q + 1) * (q + 1)

rows = []
for h in range(15, 21):
    # A scalar relaxation over total pin counts, not helper-graph enumeration.
    values = [
        (18 * B - balanced_square_sum(h, B), B,
         balanced_square_sum(h, B))
        for B in range(min(65, 9 * h) + 1)
    ]
    upper, B, Q = max(values)
    rows.append({
        "h": h, "old_targets_required": 57 * h,
        "max_scalar_capacity": upper, "maximizing_B": B,
        "balanced_square_sum_at_B": Q,
        "capacity_minus_required": upper - 57 * h,
        "quadratic_polynomial": polynomial(h),
    })
assert rows[0]["capacity_minus_required"] == 30
assert rows[1]["max_scalar_capacity"] == 905
assert rows[1]["capacity_minus_required"] == -7
assert all(row["capacity_minus_required"] < 0 for row in rows[1:])
assert 57 + 15 == 72
assert 74 - 57 == 17
assert 75 - 57 == 18

usage = resource.getrusage(resource.RUSAGE_SELF)
result = {
    "status": "PASS_ARITHMETIC_CHECK",
    "source_data_read": False,
    "P_at_16": polynomial(16),
    "P_forward_difference": "114*h-1113",
    "P_forward_difference_at_16": 711,
    "rows": rows,
    "interpretation": "The relaxation excludes every h>=16. Its pass at h=15 is not an existence claim.",
    "arithmetic_CPU_seconds": time.process_time() - start_cpu,
    "process_CPU_seconds_through_check": usage.ru_utime + usage.ru_stime,
    "wall_seconds_through_check": time.monotonic() - start_wall,
    "workers": 1,
    "graph_generation": 0, "BFS": 0, "solver": 0, "Lean": 0,
    "helper_graphs_enumerated": 0, "new_primary_search": 0,
}
(out_dir / "INTEGER_CHECK.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
