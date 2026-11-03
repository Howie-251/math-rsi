#!/usr/bin/env python3
"""Exact local route algebra; no graph construction or graph BFS."""
import itertools
import json
from pathlib import Path
import resource
import time

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[3]
resource.setrlimit(resource.RLIMIT_CPU, (30, 31))
START = time.process_time()
P = json.loads((HERE.parent / "f5_full_d20_D3/PARAMETERS.json").read_text())
C, T, DIR, INV = (P[k] for k in ("controller", "matrices", "directions", "inverse_ports"))
I = [[int(i == j) for j in range(3)] for i in range(3)]
V = list(itertools.product(range(5), repeat=3))


def add(x, y):
    return tuple((a + b) % 5 for a, b in zip(x, y))


def scale(t, x):
    return tuple(t * a % 5 for a in x)


def mv(m, x):
    return tuple(sum(a * b for a, b in zip(row, x)) % 5 for row in m)


def mm(m, n):
    return [[sum(m[i][k] * n[k][j] for k in range(3)) % 5 for j in range(3)] for i in range(3)]


def rank(columns):
    a = [list(row) for row in zip(*columns)]
    r = 0
    for col in range(len(columns)):
        pivot = next((i for i in range(r, 3) if a[i][col] % 5), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        mult = pow(a[r][col] % 5, -1, 5)
        a[r] = [z * mult % 5 for z in a[r]]
        for i in range(3):
            if i != r:
                q = a[i][col]
                a[i] = [(x - q * y) % 5 for x, y in zip(a[i], a[r])]
        r += 1
        if r == 3:
            break
    return r


def code(x):
    return x[0] + 5 * x[1] + 25 * x[2]


def is_triangle(a, p):
    b = C[a][p]
    return bool(set(C[a]) & set(C[b]))


words = []


def visit(a, vertices, ports):
    if a == 0:
        words.append((vertices, ports))
    if len(ports) == 4:
        return
    for p, b in enumerate(C[a]):
        visit(b, vertices + [b], ports + [p])


visit(0, [0], [])
records = []
external = set()
for vertices, ports in words:
    matrix = I
    columns = []
    for p in ports:
        matrix = mm(T[p], matrix)
        columns = [mv(T[p], v) for v in columns] + [tuple(DIR[INV[p]])]
    edges = [tuple(sorted(pair)) for pair in zip(vertices, vertices[1:])]
    if len(ports) in (2, 4):
        assert matrix == I
        for a, p in zip(vertices, ports):
            if not is_triangle(a, p):
                external.add(tuple(sorted((a, C[a][p]))))
    records.append(dict(vertices=vertices, ports=ports, edges=edges, matrix=matrix,
                        columns=columns, noise_rank=rank(columns) if columns else 0,
                        nonbacktracking=all(ports[k + 1] != INV[ports[k]] for k in range(len(ports) - 1))))

external = sorted(external)
triangle_words = [r for r in records if len(r["ports"]) == 3]
assert len(triangle_words) == 2
assert mm(triangle_words[0]["matrix"], triangle_words[1]["matrix"]) == I
H = triangle_words[0]["matrix"]
HminusI = [[(H[i][j] - I[i][j]) % 5 for j in range(3)] for i in range(3)]
holonomy_rank = rank(list(zip(*HminusI)))


def backtracks(shapes):
    # A closed tree walk of length <=4 is either two successive reversals,
    # or outer edge / inner reversal / reversed outer edge. Difference
    # coefficients for its one or two edge pairs are independent.
    reached = {(0, 0, 0)}
    for r in records:
        if len(r["ports"]) not in (2, 4):
            continue
        pair_columns = []
        coefficients = []
        for edge in dict.fromkeys(tuple(e) for e in r["edges"]):
            indices = [i for i, e in enumerate(r["edges"]) if tuple(e) == edge]
            # At most two undirected edges; each forward/reverse pair has
            # equal transported direction, so its signed values form A-A.
            v = r["columns"][indices[0]]
            assert all(tuple(r["columns"][i]) == tuple(v) for i in indices)
            pair_columns.append(v)
            # Four traversals of the same edge give (A-A)+(A-A)=F5,
            # including when A has two elements. Two traversals give A-A.
            coefficients.append(range(5) if edge not in shapes or len(indices) == 4
                                else (0, shapes[edge], -shapes[edge]))
        for values in itertools.product(*coefficients):
            out = (0, 0, 0)
            for t, v in zip(values, pair_columns):
                out = add(out, scale(t, v))
            reached.add(out)
    return reached


# Check the precise saved representative using the actual signed sets,
# enumerating only its 35 return words, never an expanded graph.
old_case = json.loads((HERE.parent / "f5_triangle_noise_d10_D4/CASES.jsonl").read_text().splitlines()[0])
actual = {(0, 0, 0)}
representative_words = []
for r in records:
    choices = []
    for a, b, p in zip(r["vertices"], r["vertices"][1:], r["ports"]):
        values = old_case["A2" if is_triangle(a, p) else "A0"]
        choices.append(values if a < b else [(-t) % 5 for t in values])
    image = set()
    for coefficients in itertools.product(*choices):
        out = (0, 0, 0)
        for t, v in zip(coefficients, r["columns"]):
            out = add(out, scale(t, v))
        image.add(out)
    actual |= image
    representative_words.append(dict(ports=r["ports"], image_codes=sorted(map(code, image))))
missing = sorted(code(x) for x in V if x not in actual)
assert missing[0] == old_case["first_missing"] == 6

shapes_rows = []
for shape in itertools.product((1, 2), repeat=len(external)):
    reached = backtracks(dict(zip(external, shape)))
    shapes_rows.append(dict(shape=shape, backtrack_union_size=len(reached),
                            missing_codes=sorted(code(x) for x in V if x not in reached)))

result = dict(status="EXACT_LOCAL_ROUTE_DIAGNOSIS_COMPLETE", root_controller=0,
              closed_word_counts={str(length): sum(len(r["ports"]) == length for r in records) for length in range(5)},
              all_length4_backtracking=all(not r["nonbacktracking"] for r in records if len(r["ports"]) == 4),
              holonomy=H, rank_H_minus_I=holonomy_rank, external_edges=external,
              shape_cases=len(shapes_rows), full_backtrack_union_cases=sum(not r["missing_codes"] for r in shapes_rows),
              backtrack_union_sizes=sorted(set(r["backtrack_union_size"] for r in shapes_rows)),
              saved_representative_same_fiber_reached=len(actual), saved_representative_missing_codes=missing,
              graphs_generated=0, graph_BFS=0, solver_calls=0, CPU_seconds=time.process_time()-START)
(HERE / "CONTROLLER_RETURN_WORDS.json").write_text(json.dumps(records, indent=2) + "\n")
(HERE / "LOCAL_SHAPE_CASES.json").write_text(json.dumps(shapes_rows, indent=2) + "\n")
(HERE / "REPRESENTATIVE_WORD_IMAGES.json").write_text(json.dumps(representative_words, indent=2) + "\n")
(HERE / "RESULT.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result))
