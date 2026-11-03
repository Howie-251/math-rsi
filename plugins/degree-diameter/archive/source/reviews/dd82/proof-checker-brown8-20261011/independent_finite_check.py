"""Read-only, small exact audit of the concrete Brown premises (no search for G)."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import time

started = time.monotonic()
root = Path(__file__).resolve().parents[3]
rows = [tuple(map(int, row.split())) for row in
        (root / 'computations/dd82/construction/brown57.edges').read_text().splitlines()]
assert rows[0] == (57, 224)
old_edges = rows[1:]
assert len(old_edges) == len(set(old_edges)) == 224
assert all(0 <= u < v < 57 for u, v in old_edges)
edge_set = set(old_edges)
points = [(1, a, b) for a in range(7) for b in range(7)]
points += [(0, 1, a) for a in range(7)] + [(0, 0, 1)]
coordinate_edges = {(u, v) for u, v in combinations(range(57), 2)
                    if sum(points[u][k] * points[v][k] for k in range(3)) % 7 == 0}
assert coordinate_edges == edge_set
adj = [set() for _ in points]
for u, v in old_edges:
    adj[u].add(v)
    adj[v].add(u)
assert Counter(map(len, adj)) == {7: 8, 8: 49}
assert all(v in adj[u] or adj[u] & adj[v] for u, v in combinations(range(57), 2))
C = {v for v in range(57) if len(adj[v]) == 7}
I = {v for v in range(57) if v not in C and not adj[v] & C}
E = set(range(57)) - C - I
assert (len(C), len(I), len(E)) == (8, 21, 28)
assert all(adj[c] <= E for c in C)
assert all(len(adj[e] & C) == 2 and len(adj[e] & I) == 3 for e in E)
assert all(len(adj[i] & I) == 4 for i in I)
triangles = [frozenset((u, v, w)) for u, v, w in combinations(range(57), 3)
             if (u, v) in edge_set and (u, w) in edge_set and (v, w) in edge_set]
iii = [t for t in triangles if t <= I]
iee = [t for t in triangles if len(t & I) == 1 and len(t & E) == 2]
assert (len(triangles), len(iii), len(iee)) == (56, 14, 42)
assert all(sum(i in t for t in iii) == 2 and sum(i in t for t in iee) == 2 for i in I)
types = Counter()
for u, v in old_edges:
    kind = ''.join(sorted('C' if z in C else 'I' if z in I else 'E' for z in (u, v)))
    assert kind in ('CE', 'EI', 'EE', 'II')
    containing = [t for t in triangles if u in t and v in t]
    assert len(containing) == (0 if kind == 'CE' else 1)
    if containing:
        assert (containing[0] <= I) == (kind == 'II')
    types[kind] += 1

# Red-team the only triangle-cover reductions; all sets, no symmetry quotient.
cover_stats = Counter()
for count, minimum_coverage in ((7, 20), (8, 21)):
    for chosen in combinations(iii, count):
        multiplicity = Counter(v for triangle in chosen for v in triangle)
        if len(multiplicity) < minimum_coverage:
            continue
        cover_stats[f'{count}_triangles_cover_{len(multiplicity)}'] += 1
        assert max(multiplicity.values()) <= 2
        repeats = sum(m == 2 for m in multiplicity.values())
        assert repeats == 3 * count - len(multiplicity)
        if count == 7:
            assert repeats <= 1
        else:
            assert repeats == 3

# Independent integer checks of the relaxed resource bounds in C, D, E.
maxima = {}
for case in ('C', 'D', 'E'):
    values = []
    for j in range(9):
        for e in range(9 - j):
            if e > (2 if case == 'E' else 1):
                continue
            for sigma in range((2 if case == 'D' else 1) + 1):
                needed = j if case == 'C' else max(0, j - e)
                if sigma < needed:
                    continue
                if case == 'C':
                    values.append(4*j + 3*e + sigma - needed)
                elif case == 'D':
                    for epsilon in range(2):
                        if j == 0 and epsilon:
                            continue
                        values.append(4*j + 2*e + epsilon - needed)
                else:
                    values.append(4*j + 3*e - needed)
    maxima[case] = max(values)
assert maxima == {'C': 7, 'D': 13, 'E': 17}

result = {
    'status': 'PASS',
    'scope': 'Concrete Brown premises and tiny triangle-subset / integer-bound checks only',
    'source_files_modified': False,
    'n': 57, 'm': 224,
    'coordinate_edge_list_match': True,
    'all_pairs_distance_at_most_two': True,
    'degree_counts': dict(Counter(map(len, adj))),
    'class_sizes': {'C': len(C), 'I': len(I), 'E': len(E)},
    'triangles': {'III': len(iii), 'IEE': len(iee)},
    'edge_types': dict(types),
    'triangle_cover_statistics': dict(cover_stats),
    'relaxed_coverage_maxima': maxima,
    'elapsed_seconds': time.monotonic() - started,
    'cpu_processes': 1,
    'not_an_extension_search': True,
}
print(json.dumps(result, indent=2))
