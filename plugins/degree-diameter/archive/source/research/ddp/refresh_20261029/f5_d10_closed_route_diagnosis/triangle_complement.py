#!/usr/bin/env python3
"""Check the five actual holonomy shifts against local backtrack masks."""
import itertools
import json
from pathlib import Path
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (30, 31))
START = time.process_time()
HERE = Path(__file__).resolve().parent
params = json.loads((HERE.parent / "f5_full_d20_D3/PARAMETERS.json").read_text())
words = json.loads((HERE / "CONTROLLER_RETURN_WORDS.json").read_text())
shapes = json.loads((HERE / "LOCAL_SHAPE_CASES.json").read_text())
triangles = [r for r in words if len(r["ports"]) == 3]
forward, reverse = triangles
H, Hinv = forward["matrix"], reverse["matrix"]
I = [[int(i == j) for j in range(3)] for i in range(3)]
L = [[(H[i][j] - I[i][j]) % 5 for j in range(3)] for i in range(3)]
vectors = [(i % 5, i // 5 % 5, i // 25) for i in range(125)]


def add(x, y):
    return tuple((a + b) % 5 for a, b in zip(x, y))


def mv(m, x):
    return tuple(sum(a * b for a, b in zip(row, x)) % 5 for row in m)


def code(x):
    return x[0] + 5 * x[1] + 25 * x[2]


shifts = sorted(set(mv(L, x) for x in vectors))
assert len(shifts) == 5
negative_inverse = {x: tuple(-v % 5 for v in mv(Hinv, x)) for x in vectors}
FULL = (1 << 125) - 1
for row in shapes:
    row["missing_mask"] = sum(1 << x for x in row["missing_codes"])
    row["triangle_choices_pass"] = 0
subsets = list(itertools.combinations(range(5), 3))
triangle_rows = []
for choices in itertools.product(subsets, repeat=3):
    signed = [values if a < b else tuple(-v % 5 for v in values)
              for a, b, values in zip(forward["vertices"], forward["vertices"][1:], choices)]
    Z = set()
    for values in itertools.product(*signed):
        out = [sum(t * column[i] for t, column in zip(values, forward["columns"])) % 5
               for i in range(3)]
        Z.add(tuple(out))
    assert len(Z) == 27
    universal = FULL
    for h in shifts:
        positive = {add(z, h) for z in Z}
        image = positive | {negative_inverse[z] for z in positive}
        universal &= sum(1 << code(x) for x in image)
    passing = []
    for index, row in enumerate(shapes):
        if not (row["missing_mask"] & ~universal):
            row["triangle_choices_pass"] += 1
            row.setdefault("first_triangle_choices", choices)
            passing.append(index)
    triangle_rows.append(dict(choices=choices, universal_triangle_codes=[i for i in range(125) if universal >> i & 1],
                              passing_shapes=passing))

valid = [row for row in shapes if row["triangle_choices_pass"]]
for row in shapes:
    del row["missing_mask"]
result = dict(status="COMPLETE_ROOT0_ALL_SOURCE_LOCAL_SHAPE_TEST", holonomy_shifts=shifts,
              external_shape_cases=len(shapes), triangle_choices=len(triangle_rows),
              local_combinations_tested=len(shapes) * len(triangle_rows),
              feasible_external_shapes=len(valid),
              all_feasible_shapes_require_different_root_external_gaps=all(row["shape"][0] != row["shape"][1] for row in valid),
              feasible_shapes_with_nonfull_backtrack_union=sum(row["backtrack_union_size"] < 125 for row in valid),
              universal_triangle_sizes=sorted(set(len(row["universal_triangle_codes"]) for row in triangle_rows)),
              feasible_shapes_summary=[dict(shape=row["shape"], triangle_choices=row["triangle_choices_pass"],
                                             backtrack_size=row["backtrack_union_size"]) for row in valid],
              new_graphs=0, BFS=0, solver_calls=0, CPU_seconds=time.process_time()-START)
(HERE / "ALL_TRIANGLE_LOCAL_CASES.json").write_text(json.dumps(triangle_rows, separators=(",", ":")) + "\n")
(HERE / "COMPLEMENT_SHAPES.json").write_text(json.dumps(shapes, indent=2) + "\n")
(HERE / "COMPLEMENT_RESULT.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
