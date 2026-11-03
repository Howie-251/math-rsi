"""Read-only independent checks of the small Brown families and n63 data.

Writes no source data and performs no completion/profile enumeration.
"""
import itertools
import json
import math
import os
from pathlib import Path
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
started = time.monotonic()
root = Path(__file__).resolve().parents[3]
data = root / 'computations/dd82/construction'

raw = [tuple(map(int, line.split())) for line in (data / 'brown57.edges').read_text().splitlines()]
assert raw[0] == (57, 224)
edges = set(raw[1:])
assert len(edges) == len(raw) - 1 == 224
assert all(0 <= u < v < 57 for u, v in edges)
neighbors = {v: set() for v in range(57)}
for u, v in edges:
    neighbors[u].add(v)
    neighbors[v].add(u)
assert all(len(neighbors[v]) in (7, 8) for v in neighbors)
C = {v for v in neighbors if len(neighbors[v]) == 7}
I = {v for v in neighbors if v not in C and neighbors[v].isdisjoint(C)}
E = set(neighbors) - C - I
assert tuple(map(len, (C, I, E))) == (8, 21, 28)
assert all(neighbors[v] <= E for v in C)
assert all(len(neighbors[v] & C) == 2 and len(neighbors[v] & I) == 3 for v in E)
assert all(len(neighbors[v] & I) == 4 for v in I)
triangles = {frozenset((u, v, w)) for u, v in edges for w in neighbors[u] & neighbors[v]}
III = sorted([t for t in triangles if t <= I], key=lambda t: sorted(t))
IEE = [t for t in triangles if len(t & I) == 1 and len(t & E) == 2]
assert len(III) == 14 and len(IEE) == 42 and len(triangles) == 56
assert all(sum(v in t for t in III) == 2 and sum(v in t for t in IEE) == 2 for v in I)
for u, v in edges:
    containing = [t for t in triangles if {u, v} <= t]
    if u in C or v in C:
        assert len(containing) == 0
    else:
        assert len(containing) == 1
        assert (containing[0] <= I) == (u in I and v in I)

stored = json.loads((data / 'brown_r9_eight_iii_facts.json').read_text())
assert stored['III_triangles'] == [sorted(t) for t in III]
stored_records = {tuple(r['triangle_indices']): r for r in stored['records']}
assert len(stored_records) == len(stored['records'])
full_families, twenty_families, alternatives = [], [], 0
coverage_histograms = {}
for size in (6, 7, 8, 9):
    histogram = {}
    for indices in itertools.combinations(range(14), size):
        family = [III[i] for i in indices]
        union = set().union(*family)
        histogram[len(union)] = histogram.get(len(union), 0) + 1
        if size != 8 or len(union) < 20:
            continue
        R = {v for v in I if sum(v in t for t in family) == 2}
        if len(union) == 21:
            assert len(R) == 3 and frozenset(R) in family
            full_families.append(indices)
            continue
        assert len(union) == 20 and len(R) == 4
        missing, = I - union
        isolated = [t for t in family if t.isdisjoint(R)]
        assert len(isolated) == 2 and isolated[0].isdisjoint(isolated[1])
        Z = set().union(*isolated)
        cross = {(min(u, v), max(u, v)) for u in isolated[0] for v in isolated[1]
                 if v in neighbors[u]}
        assert len(Z) == 6 and len(cross) == 1
        induced = {e for e in edges if set(e) <= Z}
        assert len(induced) == 7
        assert all(neighbors[v].isdisjoint(Z) for v in R)
        assert all(len(neighbors[v] & Z) <= 1 for v in I - Z - {missing})
        allowed_EE = {tuple(sorted(t & E)) for t in IEE if missing in t}
        assert len(allowed_EE) == 2
        assert all(neighbors[v].isdisjoint(Z) for edge in allowed_EE for v in edge)
        r = stored_records[indices]
        assert r['missing_I'] == missing and r['repeated_I'] == sorted(R)
        assert {tuple(t) for t in r['isolated_triangles']} == {tuple(sorted(t)) for t in isolated}
        assert tuple(sorted(r['cross_edge'])) in cross
        assert {tuple(sorted(e)) for e in r['allowed_extra_EE_edges']} == allowed_EE
        twenty_families.append(indices)
        alternatives += len(allowed_EE)
    coverage_histograms[str(size)] = {str(k): v for k, v in sorted(histogram.items())}
assert coverage_histograms == stored['coverage_histograms']
assert len(full_families) == stored['eight_III_full_cover_families'] == 14
assert len(twenty_families) == stored['eight_III_twenty_cover_families'] == 42
assert alternatives == stored['EE_alternatives'] == 84
assert set(stored_records) == set(twenty_families)

# Independently reconstruct cyclotomic polynomials by exact monic division;
# verify every supplied Laurent lift, norm, square bracket and residue field.
def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def quotient(p, divisor):
    a = p[:]
    q = [0] * (len(a) - len(divisor) + 1)
    for shift in reversed(range(len(q))):
        q[shift] = a[shift + len(divisor) - 1]
        for j in range(len(divisor)):
            a[shift + j] -= q[shift] * divisor[j]
    assert not any(a)
    return trim(q)

table = json.loads((data / 'n63_cyclotomic_norms.json').read_text())
rows = table['rows']
assert [r['order'] for r in rows] == list(range(1, 64))
assert table['checked_rows'] == 63 and table['nonsquare_rows'] == 62
phi = {}
exceptions = []
expected_md = ['| conductor ell | degree | modulus | norm residue |', '|---:|---:|---:|---:|']
for row in rows:
    ell = row['order']
    poly = [-1] + [0] * (ell - 1) + [1]
    for proper in range(1, ell):
        if ell % proper == 0:
            poly = quotient(poly, phi[proper])
    phi[ell] = poly
    c = row['real_cyclotomic_coefficients']
    d = len(c) - 1
    assert d == row['degree'] and c[-1] == 1
    if ell > 2:
        lift = [0] * (2*d + 1)
        for j, coefficient in enumerate(c):
            for k in range(j + 1):
                lift[d-j+2*k] += coefficient * math.comb(j, k)
        assert lift == poly
        assert 2*d == sum(math.gcd(k, ell) == 1 for k in range(1, ell + 1))
    else:
        assert c == ([-2, 1] if ell == 1 else [2, 1])
    norm = sum(cj * (-29)**j * (-4)**d // 4**j for j, cj in enumerate(c))
    assert norm == row['discriminant_norm']
    floor = math.isqrt(norm)
    assert floor == row['sqrt_floor']
    if row['exception']:
        assert ell == 3 and c == [1, 1] and norm == 25
        exceptions.append(ell)
        expected_md.append(f'| {ell} | {d} | exception | 25 = 5² |')
    else:
        assert floor**2 < norm < (floor+1)**2
        m = row['modulus']
        squares = sorted({j*j % m for j in range(m)})
        assert squares == row['square_residues']
        assert norm % m == row['norm_residue'] and norm % m not in squares
        expected_md.append(f'| {ell} | {d} | {m} | {norm % m} |')
assert exceptions == [3]
assert (data / 'n63_cyclotomic_norms.table.md').read_text().splitlines() == expected_md

print(json.dumps({
    'status': 'PASS',
    'cpu_limit_seconds': 30,
    'cpu_count': len(os.sched_getaffinity(0)),
    'elapsed_seconds': round(time.monotonic() - started, 6),
    'brown': {'vertices': 57, 'edges': 224, 'class_sizes': [8, 21, 28],
              'triangle_counts': [14, 42], 'all_family_subsets': math.comb(14, 8),
              'full_cover_families': len(full_families),
              'twenty_cover_families': len(twenty_families),
              'EE_alternatives': alternatives,
              'stored_records_and_histograms_match': True,
              'six_family_predicates': 'all independently verified'},
    'n63': {'coefficient_rows': 63, 'Laurent_lifts': 61,
            'exact_norms': 63, 'nonsquare_rows': 62, 'exception': exceptions,
            'markdown_table_matches': True},
    'excluded_work': ['six-million Brown profile', 'added-edge completions',
                      'Lean build', 'hashes'],
}, indent=2))
