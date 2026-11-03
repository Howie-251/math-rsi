#!/usr/bin/env python3
"""Test necessary same-fiber coverage around one saved external C5."""
import itertools
import json
from pathlib import Path
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (30, 31))
START = time.process_time()
HERE = Path(__file__).resolve().parent
params = json.loads((HERE.parent / "f5_full_d20_D3/PARAMETERS.json").read_text())
C, T, DIR, INV = (params[k] for k in ("controller", "matrices", "directions", "inverse_ports"))
I = [[int(i == j) for j in range(3)] for i in range(3)]
V = [(i % 5, i // 5 % 5, i // 25) for i in range(125)]
FULL = (1 << 125) - 1
CYCLE = [0, 20, 28, 22, 9]


def mv(m, x):
    return tuple(sum(a * b for a, b in zip(row, x)) % 5 for row in m)


def mm(m, n):
    return [[sum(m[i][k] * n[k][j] for k in range(3)) % 5 for j in range(3)] for i in range(3)]


def code(x):
    return x[0] + 5 * x[1] + 25 * x[2]


def triangle(a, b):
    return bool(set(C[a]) & set(C[b]))


def analyze_root(root):
    paths = []

    def visit(a, vertices, ports):
        if a == root:
            paths.append((vertices, ports))
        if len(ports) < 4:
            for p, b in enumerate(C[a]):
                visit(b, vertices + [b], ports + [p])

    visit(root, [root], [])
    records = []
    external = set()
    for vertices, ports in paths:
        matrix, columns = I, []
        edges = [tuple(sorted(edge)) for edge in zip(vertices, vertices[1:])]
        for p in ports:
            matrix = mm(T[p], matrix)
            columns = [mv(T[p], column) for column in columns] + [tuple(DIR[INV[p]])]
        if len(ports) in (2, 4):
            assert matrix == I
            external |= {edge for edge in edges if not triangle(*edge)}
        records.append(dict(vertices=vertices, ports=ports, edges=edges, matrix=matrix, columns=columns))
    external = sorted(external)
    closed3 = [row for row in records if len(row["ports"]) == 3]
    assert len(closed3) == 2
    forward, reverse = closed3
    H, Hinv = forward["matrix"], reverse["matrix"]
    assert mm(H, Hinv) == I
    L = [[(H[i][j] - I[i][j]) % 5 for j in range(3)] for i in range(3)]
    shifts = sorted(set(mv(L, x) for x in V))
    negative_inverse = {x: tuple(-v % 5 for v in mv(Hinv, x)) for x in V}
    all_G = 0
    for choices in itertools.product(itertools.combinations(range(5), 3), repeat=3):
        signed = [values if a < b else tuple(-v % 5 for v in values)
                  for a, b, values in zip(forward["vertices"], forward["vertices"][1:], choices)]
        Z = {tuple(sum(t * col[i] for t, col in zip(values, forward["columns"])) % 5 for i in range(3))
             for values in itertools.product(*signed)}
        assert len(Z) == 27
        G = FULL
        for h in shifts:
            positive = {tuple((a + b) % 5 for a, b in zip(z, h)) for z in Z}
            image = positive | {negative_inverse[z] for z in positive}
            G &= sum(1 << code(x) for x in image)
        all_G |= G
    # all_G is a relaxation: different points may use different triangle
    # triples. Passing it is not asserted sufficient for any actual graph.
    masks_by_shape = []
    external_root_edges = [edge for edge in external if root in edge]
    assert len(external_root_edges) == 2
    root_indices = [external.index(edge) for edge in external_root_edges]
    for shape in itertools.product((1, 2), repeat=len(external)):
        widths = dict(zip(external, shape))
        B = 1
        for row in records:
            if len(row["ports"]) not in (2, 4):
                continue
            columns, coefficients = [], []
            for edge in dict.fromkeys(row["edges"]):
                indices = [i for i, value in enumerate(row["edges"]) if value == edge]
                column = row["columns"][indices[0]]
                assert all(row["columns"][i] == column for i in indices)
                columns.append(column)
                coefficients.append(range(5) if edge not in widths or len(indices) == 4
                                    else (0, widths[edge], -widths[edge]))
            for values in itertools.product(*coefficients):
                point = tuple(sum(t * column[i] for t, column in zip(values, columns)) % 5 for i in range(3))
                B |= 1 << code(point)
        masks_by_shape.append(dict(shape=shape, backtrack_size=B.bit_count(),
                                   relaxed_pass=(B | all_G) == FULL,
                                   root_gaps=[shape[i] for i in root_indices]))
    feasible = [row for row in masks_by_shape if row["relaxed_pass"]]
    detail = dict(root=root, closed_words=records, external_edges=external,
                  root_external_edges=external_root_edges, holonomy=H, holonomy_image_size=len(shifts),
                  union_universal_triangle_codes=[x for x in range(125) if all_G >> x & 1],
                  shape_cases=masks_by_shape)
    (HERE / f"CYCLE_ROOT_{root}.json").write_text(json.dumps(detail, separators=(",", ":")) + "\n")
    return dict(root=root, closed_word_counts={str(k): sum(len(row["ports"]) == k for row in records) for k in range(5)},
                holonomy_image_size=len(shifts), shape_cases=len(masks_by_shape),
                relaxed_feasible=len(feasible), root_external_edges=external_root_edges,
                allowed_root_gaps=sorted(set(tuple(row["root_gaps"]) for row in feasible)))


rows = [analyze_root(root) for root in CYCLE]
all_opposite = all(row["allowed_root_gaps"] == [(1, 2), (2, 1)] for row in rows)
result = dict(status="ODD_EXTERNAL_CYCLE_OBSTRUCTION_SUPPORTED" if all_opposite else "ODD_CYCLE_PREDICTION_NOT_SUPPORTED",
              cycle=CYCLE, roots=rows, all_vertices_require_opposite_external_gap_shapes=all_opposite,
              expanded_graphs=0, graph_BFS=0, solver_calls=0, CPU_seconds=time.process_time()-START)
(HERE / "CYCLE_RESULT.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
