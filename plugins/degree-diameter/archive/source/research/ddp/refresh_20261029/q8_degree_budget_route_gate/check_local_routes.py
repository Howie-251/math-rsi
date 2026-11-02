#!/usr/bin/env python3
"""Only word types and the nine two-flip Q3 words; no graph search or BFS."""
import itertools
import json
import time
from collections import Counter
from pathlib import Path

started = time.process_time()
all_types = sorted(
    "".join(word)
    for length in range(1, 4)
    for word in itertools.product("IE", repeat=length)
    if "E" in word
)
first_exit = {
    0: {"E": 1, "EI": 3, "EE": 1, "EII": 3,
        "EIE": 6, "EEI": 3, "EEE": 1},
    1: {"IE": 6, "IEI": 18, "IEE": 6},
    2: {"IIE": 6},
}
partition = [word for group in first_exit.values() for word in group]
assert sorted(partition) == all_types and len(set(partition)) == 11
for initial_i, group in first_exit.items():
    assert all(word.index("E") == initial_i for word in group)

two_flip_endpoints = Counter(a ^ b for a in (1, 2, 4) for b in (1, 2, 4))
assert two_flip_endpoints == {0: 3, 3: 2, 5: 2, 6: 2}
group_bounds_at_s_one = [sum(first_exit[k].values()) for k in range(3)]
assert group_bounds_at_s_one == [18, 30, 6]
outside_bounds = {str(s): 18 * s + 36 for s in (0, 1)}
assert outside_bounds == {"0": 36, "1": 54}
assert all(bound < 56 for bound in outside_bounds.values())

result = {
    "status": "LOCAL_IDENTITIES_CONFIRMED",
    "word_types": all_types,
    "first_exit_word_bounds": first_exit,
    "first_exit_bounds_at_extra_degree_one": group_bounds_at_s_one,
    "ordered_two_cube_flip_endpoint_multiplicities": dict(two_flip_endpoints),
    "required_outside_vertices": 56,
    "outside_bounds_by_root_extra_degree": outside_bounds,
    "full_graphs_generated": 0,
    "bfs_runs": 0,
    "solver_calls": 0,
    "cpu_seconds": time.process_time() - started,
}
path = Path(__file__).with_name("LOCAL_CHECK.json")
path.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, separators=(",", ":")))
