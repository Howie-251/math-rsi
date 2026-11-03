"""Bounded independent exact checks for the read-only paper audit."""
import itertools
import json
import math
from pathlib import Path
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
start = time.process_time()
ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent


def multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def determinant(a):
    a = [row[:] for row in a]
    previous = sign = 1
    for k in range(len(a) - 1):
        if a[k][k] == 0:
            j = next(j for j in range(k + 1, len(a)) if a[j][k])
            a[k], a[j] = a[j], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, len(a)):
            for j in range(k + 1, len(a)):
                value = a[i][j] * pivot - a[i][k] * a[k][j]
                assert value % previous == 0
                a[i][j] = value // previous
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


data = json.loads((ROOT / 'computations/dd82/construction/n63_cyclotomic_norms.json').read_text())
rows = data['rows']
assert [r['order'] for r in rows] == list(range(1, 64))
assert data['checked_rows'] == 63 and data['nonsquare_rows'] == 62
lifted = {1: [-1, 1], 2: [1, 1]}
for r in rows:
    ell, d, c = r['order'], r['degree'], r['real_cyclotomic_coefficients']
    assert len(c) == d + 1 and c[-1] == 1
    if ell >= 3:
        assert 2 * d == sum(math.gcd(ell, j) == 1 for j in range(1, ell + 1))
        lift = [0] * (2 * d + 1)
        for j, value in enumerate(c):
            for k in range(j + 1):
                lift[d + j - 2 * k] += value * math.comb(j, k)
        lifted[ell] = lift
    else:
        assert c == ([-2, 1] if ell == 1 else [2, 1])
    # Independently compute the norm as det(29 I + 4 M_mu), not by evaluation.
    matrix = [[29 * (i == j) for j in range(d)] for i in range(d)]
    for j in range(d - 1):
        matrix[j + 1][j] += 4
    for i in range(d):
        matrix[i][d - 1] -= 4 * c[i]
    norm = determinant(matrix)
    assert norm == r['discriminant_norm']
    k = r['sqrt_floor']
    assert k == math.isqrt(norm)
    assert r['exception'] == (ell == 3)
    if ell == 3:
        assert c == [1, 1] and norm == 25
    else:
        assert k * k < norm < (k + 1) * (k + 1)
        m = r['modulus']
        squares = sorted({i * i % m for i in range(m)})
        assert squares == r['square_residues']
        assert norm % m == r['norm_residue'] and norm % m not in squares

# Divisor products characterize cyclotomic polynomials; avoid the source generator.
for ell in range(1, 64):
    product = [1]
    for divisor in range(1, ell + 1):
        if ell % divisor == 0:
            product = multiply(product, lifted[divisor])
    assert product == [-1] + [0] * (ell - 1) + [1]
table = (ROOT / 'computations/dd82/construction/n63_cyclotomic_norms.table.md').read_text().splitlines()[2:]
assert len(table) == 63
for r, line in zip(rows, table):
    values = [p.strip() for p in line.split('|')[1:-1]]
    assert values[:2] == [str(r['order']), str(r['degree'])]
    assert values[2:] == (['exception', '25 = 5²'] if r['exception'] else [str(r['modulus']), str(r['norm_residue'])])


def matmul(a, b):
    return [[sum(x * y for x, y in zip(row, column)) for column in zip(*b)] for row in a]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def graph_checks(a):
    n = len(a)
    triangles = [p for p in itertools.combinations(range(n), 3) if all(a[u][v] for u, v in itertools.combinations(p, 2))]
    degrees = [sum(row) for row in a]
    a2 = matmul(a, a)
    a3 = matmul(a2, a)
    a5 = matmul(a3, a2)
    # Count genuine five-cycles once: smallest vertex first, second < last.
    cycles = sum(all(a[p[i]][p[(i + 1) % 5]] for i in range(5))
                 for p in itertools.permutations(range(n), 5)
                 if p[0] == min(p) and p[1] < p[-1])
    correction = 10 * sum(sum(degrees[v] for v in t) - 3 for t in triangles)
    assert trace(a5) == 10 * cycles + correction
    return trace(a5)


walk_cases = 0
for n in range(1, 6):
    edges = list(itertools.combinations(range(n), 2))
    for mask in range(1 << len(edges)):
        a = [[0] * n for _ in range(n)]
        for k, (u, v) in enumerate(edges):
            if mask >> k & 1:
                a[u][v] = a[v][u] = 1
        graph_checks(a)
        walk_cases += 1

# Check fifth-trace coefficients on an 8-regular 59-vertex graph.  This graph
# does not have diameter two, so this checks algebra only, not a counterexample.
n = 59
a = [[int((j - i) % n in {1, 2, 3, 4, 55, 56, 57, 58}) for j in range(n)] for i in range(n)]
a2 = matmul(a, a)
a3 = matmul(a2, a)
a4 = matmul(a2, a2)
a5 = matmul(a3, a2)
b = [[a2[i][j] + a[i][j] - 7 * (i == j) - 1 for j in range(n)] for i in range(n)]
b2 = matmul(b, b)
s = trace(b2)
w = trace(matmul(a, b2))
t = trace(a3) // 6
assert trace(a4) == 126 * n + s - 12 * t
assert trace(a5) == 428 * n + w - 2 * s + 102 * t
assert (209 * 59) % 5 == 1 and (418 * 59) % 10 == 2

cycle_checks = {}
for ell in (5, 7, 8, 9):
    neighbors = [{(i - 2) % ell, (i + 2) % ell} for i in range(ell)]
    common = [len(neighbors[0] & neighbors[j]) for j in range(ell)]
    cycle_checks[str(ell)] = {'internal_common_neighbors_from_zero': common}
assert cycle_checks['5']['internal_common_neighbors_from_zero'][1] == 1
assert cycle_checks['7']['internal_common_neighbors_from_zero'][1] == 0
assert cycle_checks['7']['internal_common_neighbors_from_zero'][3] == 1
assert cycle_checks['8']['internal_common_neighbors_from_zero'][4] == 2
assert all(cycle_checks['8']['internal_common_neighbors_from_zero'][j] == 0 for j in (1, 3, 5, 7))
assert cycle_checks['9']['internal_common_neighbors_from_zero'][1] == 0
assert cycle_checks['9']['internal_common_neighbors_from_zero'][3] == 0
assert cycle_checks['9']['internal_common_neighbors_from_zero'][4:6] == [1, 1]

# Exhaust the 512 subsets, only to check C9's elementary local case split.
allowed = []
for mask in range(1 << 9):
    subset = {i for i in range(9) if mask >> i & 1}
    if all(sum(j in subset for j in ((i - 1) % 9, (i + 1) % 9)) == 1 for i in subset) and all((i + 2) % 9 not in subset for i in subset):
        allowed.append(subset)
orbits = {frozenset((sign * i + shift) % 9 for i in (0, 1, 4, 5)) for sign in (-1, 1) for shift in range(9)}
assert all(len(s) in (0, 2, 4) for s in allowed)
assert {frozenset(s) for s in allowed if len(s) == 4} == orbits
cycle_checks['9']['external_subset_size_counts'] = {str(k): sum(len(s) == k for s in allowed) for k in (0, 2, 4)}

result = {
    'status': 'PASS',
    'norm_rows_checked': 63,
    'nonsquare_rows': 62,
    'exception': [3],
    'norm_method': 'Bareiss determinant of multiplication by 29+4mu',
    'cyclotomic_method': 'all divisor products equal t^ell-1',
    'source_generator_imported_or_run': False,
    'closed_walk_graphs_checked': walk_cases,
    'closed_walk_scope': 'all labeled simple graphs of orders 1 through 5; general degree correction',
    'regular_trace_check': {'n': 59, 'degree': 8, 'triangles': t, 's': s, 'w': w, 'trace_A5': trace(a5)},
    'cycle_checks': cycle_checks,
    'cpu_limit_seconds': 60,
    'cpu_seconds': round(time.process_time() - start, 6),
}
(OUT / 'audit_checks.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
