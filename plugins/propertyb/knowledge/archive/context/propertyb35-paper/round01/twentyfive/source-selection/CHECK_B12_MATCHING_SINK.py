"""Bounded scalar audit of the matching-sink proof; no H/source enumeration."""
from itertools import product
from pathlib import Path
import json
import time

start = time.process_time()
owner_rows = []
for a, b, n3, k, in_g in product(range(13), range(7), range(5), range(4), (0, 1)):
    if a + 2*b + 3*n3 + 4*k != 12:
        continue
    degree = a + b + n3 + k + in_g
    if degree < 6:
        continue
    owner_rows.append([a,b,n3,k,in_g,degree])
    assert k <= 2
    if k == 2:
        assert n3 == 0 and b <= 1
        if b == 1:
            assert in_g == 1 and degree == 6 and a == 2

blue_y_rows = []
for n3, n4 in product(range(7), repeat=2):
    if 1+1+n3+n4 == 6 and 4+3+2*n3+n4 == 13:
        blue_y_rows.append([1,1,n3,n4])
assert blue_y_rows == [[1,1,2,2]]

owner_distributions = {}
for s in (1,2,3):
    # Each non-sink owns one or two of the same 12 original N4 indices.
    solutions = [[single,double] for single in range(14) for double in range(14)
                 if single+double == 13-s and single+2*double == 12]
    assert solutions == [[14-2*s,s-1]]
    owner_distributions[str(s)] = solutions[0]

two_sink_swaps = []
for y in (0,1):
    # Counts for old double p and two single Xi owners. Owner x_y loses
    # the y-N4; both Xi gain an N4 from their own hi-N3.
    before = [2,1,1]
    after = [1, 1+(y != 0), 1+(y != 1)]
    assert sum(before) == sum(after) == 4
    assert after.count(2) == 1
    assert after[y+1] == 1 and after[2-y] == 2
    two_sink_swaps.append({"y": y, "before": before, "after": after})

result = {
    "status": "PASS",
    "owner_scalar_rows": owner_rows,
    "blue_private_neighbor_type": blue_y_rows,
    "owner_single_double_counts": owner_distributions,
    "two_sink_swap_counts": two_sink_swaps,
    "s1_incidence": {"required": 4, "single_owner_capacity": 2},
    "s2_N3_edges": {"required": 8, "available": 7},
    "s3_red_N3_incidence": {"required": 18, "available": 14},
    "cpu_seconds": time.process_time()-start,
    "scope": "Owner scalar equations and indexed count changes only; no hypergraph enumeration",
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k != 'owner_scalar_rows'}))
