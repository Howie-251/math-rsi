"""Tiny scalar/type checks; no hypergraph or negative-family enumeration."""
import itertools
import json
import time
from pathlib import Path

start = time.process_time()
rows = {}
for u, t in [(1, 2), (2, 1), (3, 0), (0, 3)]:
    out = []
    for a in range(36):
        for bh in range(t + 1):
            for n3 in range(36):
                d = a + bh + n3
                if d < 6 or a + 2 * bh + 3 * n3 != 12:
                    continue
                # Cross-unit: a distinct blue neighbors; >u ensures unique one.
                if a > u and a - 1 > t - bh:
                    continue
                if max(0, a - u) * max(0, a - 1) > 2 * (t - bh):
                    continue
                out.append([a, bh, n3, d])
    rows[f"u{u}_t{t}"] = out
assert rows == {
    "u1_t2": [[3, 0, 3, 6]],
    "u2_t1": [],
    "u3_t0": [[3, 0, 3, 6]],
    "u0_t3": [[2, 2, 2, 6], [3, 0, 3, 6]],
}

code_max = 0
for subset in range(1 << 8):
    words = [i for i in range(8) if subset >> i & 1]
    if all((i ^ j).bit_count() >= 2 for i, j in itertools.combinations(words, 2)):
        code_max = max(code_max, len(words))
assert code_max == 4

# Source edge has red h, blue y. Each proper 5-edge may contain neither,
# either, or both. Only missing N4_h and unique N1_y can create a bad edge.
edge_types = []
for H in (0, 1):
    for Y in (0, 1):
        for blue_other in range(5 - H - Y + 1):
            initial_blue = Y + blue_other
            if not 1 <= initial_blue <= 4:
                continue
            final_blue = H + blue_other
            if final_blue == 0:
                assert Y == 1 and H == 0 and initial_blue == 1
            if final_blue == 5:
                assert H == 1 and Y == 0 and initial_blue == 4
            edge_types.append([H, Y, blue_other, initial_blue, final_blue])
assert len(edge_types) == 16

result = {
    "status": "PASS",
    "scalar_rows": rows,
    "binary_length3_distance2_max": code_max,
    "proper_edge_swap_types": edge_types,
    "scope": "Four scalar endpoints, 256 length-three codes, 16 edge color types only",
    "cpu_seconds": time.process_time() - start,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, ensure_ascii=False))
