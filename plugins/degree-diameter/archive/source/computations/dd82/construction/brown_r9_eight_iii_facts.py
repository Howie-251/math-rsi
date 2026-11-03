"""Small exact family facts for r9 with eight distinct destroyed III triangles.

This reads the complete Brown edge list. It checks triangle families, not
edge-choice completions or candidate order-58 graphs. No solver is used.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json

root = Path(__file__).parent
rows = [tuple(map(int, line.split()))
        for line in (root / 'brown57.edges').read_text().splitlines()]
n, edge_count = rows[0]
assert n == 57 and edge_count == 224 and len(rows[1:]) == edge_count
adj = [set() for _ in range(n)]
for u, v in rows[1:]:
    adj[u].add(v)
    adj[v].add(u)
C = {v for v in range(n) if len(adj[v]) == 7}
I = {v for v in range(n) if v not in C and not adj[v] & C}
E = set(range(n)) - C - I
triangles = [set(t) for t in combinations(sorted(I), 3)
             if t[1] in adj[t[0]] and t[2] in adj[t[0]]
             and t[2] in adj[t[1]]]
assert len(triangles) == 14
assert all(sum(v in t for t in triangles) == 2 for v in I)

histograms = {}
for count in (6, 7, 8, 9):
    histogram = Counter(len(set().union(*(triangles[k] for k in ix)))
                        for ix in combinations(range(14), count))
    histograms[str(count)] = dict(sorted(histogram.items()))

records = []
full_cover_count = 0
ee_alternatives = 0
for ix in combinations(range(14), 8):
    incidence = Counter(v for k in ix for v in triangles[k])
    repeated = {v for v, count in incidence.items() if count == 2}
    if len(incidence) == 21:
        full_cover_count += 1
        assert len(repeated) == 3
        centers = [k for k in ix if triangles[k] == repeated]
        assert len(centers) == 1
        # One deletion in this central triangle can hit at most two R points.
        continue
    if len(incidence) != 20:
        continue
    missing = next(iter(I - set(incidence)))
    assert len(repeated) == 4
    isolated = [triangles[k] for k in ix if not triangles[k] & repeated]
    assert len(isolated) == 2
    Z = isolated[0] | isolated[1]
    assert len(Z) == 6
    cross = [(u, v) for u in isolated[0] for v in isolated[1]
             if v in adj[u]]
    assert len(cross) == 1
    assert all(not adj[v] & Z for v in repeated)
    assert all(len(adj[v] & Z) <= 1 for v in I - Z - {missing})
    ee = [(u, v) for u, v in rows[1:]
          if u in E and v in E and missing in adj[u] & adj[v]]
    assert len(ee) == 2
    for u, v in ee:
        assert not (adj[u] | adj[v]) & Z
        ee_alternatives += 1
    records.append({
        'triangle_indices': list(ix),
        'missing_I': missing,
        'repeated_I': sorted(repeated),
        'isolated_triangles': [sorted(t) for t in isolated],
        'cross_edge': list(cross[0]),
        'allowed_extra_EE_edges': [list(e) for e in ee],
    })
assert full_cover_count == 14 and len(records) == 42 and ee_alternatives == 84
payload = {
    'status': 'EXACT_FAMILY_FACTS_FOR_EIGHT_III_PLUS_ONE_EE_ONLY',
    'scope': 'Necessary finite facts; no full r9 or arbitrary order-58 exclusion.',
    'III_triangles': [sorted(t) for t in triangles],
    'coverage_histograms': histograms,
    'eight_III_full_cover_families': full_cover_count,
    'eight_III_twenty_cover_families': len(records),
    'EE_alternatives': ee_alternatives,
    'records': records,
}
(root / 'brown_r9_eight_iii_facts.json').write_text(json.dumps(payload, indent=2) + '\n')
print(json.dumps({'full_cover_families': full_cover_count,
                  'twenty_cover_families': len(records),
                  'EE_alternatives': ee_alternatives,
                  'all_assertions_passed': True}))
