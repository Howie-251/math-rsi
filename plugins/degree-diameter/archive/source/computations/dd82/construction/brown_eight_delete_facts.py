"""Check only the concrete Brown premises used in the eight-deletion proof."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json

base = Path(__file__).parent
lines = (base / 'brown57.edges').read_text().splitlines()
assert list(map(int, lines[0].split())) == [57, 224]
edges = {tuple(map(int, row.split())) for row in lines[1:]}
g = [set() for _ in range(57)]
for u, v in edges:
    g[u].add(v)
    g[v].add(u)
C = {v for v in range(57) if len(g[v]) == 7}
I = {v for v in range(57) if len(g[v]) == 8 and not g[v] & C}
E = set(range(57)) - C - I
assert (len(C), len(I), len(E)) == (8, 21, 28)
assert all(g[c] <= E for c in C)
assert all(len(g[e] & C) == 2 and len(g[e] & I) == 3 for e in E)
assert all(len(g[i] & I) == 4 for i in I)
triangles = [frozenset((u, v, w)) for u, v, w in combinations(range(57), 3)
             if v in g[u] and w in g[u] and w in g[v]]
iii = [t for t in triangles if t <= I]
iee = [t for t in triangles if len(t & I) == 1 and len(t & E) == 2]
assert len(iii) == 14 and len(iee) == 42 and len(triangles) == 56
assert all(sum(i in t for t in iii) == 2 and sum(i in t for t in iee) == 2 for i in I)
edge_types = Counter()
for u, v in edges:
    t = next(label for label, S, T in [('II', I, I), ('CE', C, E), ('IE', I, E), ('EE', E, E)]
             if (u in S and v in T) or (u in T and v in S))
    containing = [z for z in triangles if {u, v} <= z]
    assert len(containing) == (0 if t == 'CE' else 1)
    if containing:
        assert (containing[0] <= I) == (t == 'II')
    edge_types[t] += 1
result = dict(status='PASS', scope='Finite Brown graph premises only; no extension search or general order58 exclusion',
              class_sizes=dict(C=8,I=21,E=28), edge_types=dict(edge_types),
              triangles=dict(III=14,IEE=42), E_neighbors_in_C=2, E_neighbors_in_I=3,
              I_neighbors_in_I=4, III_triangles_per_I=2, IEE_triangles_per_I=2)
(base / 'brown_eight_delete_facts.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))
