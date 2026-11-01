"""Independent edge-by-edge generation of the narrow M2=7,8 domain."""
from itertools import combinations
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
PAIRS = tuple(combinations(range(5), 2))
vector, degree = [0]*10, [0]*5
domain = set()

def generate(index, matching):
    if index == len(PAIRS):
        if matching in (7, 8):
            domain.add(tuple(vector))
        return
    u, v = PAIRS[index]
    previous_disjoint = sum(vector[j] for j in range(index)
                            if u not in PAIRS[j] and v not in PAIRS[j])
    for value in range(min(4-degree[u], 4-degree[v])+1):
        new_matching = matching + value*previous_disjoint
        if new_matching > 8:
            break
        vector[index] = value
        degree[u] += value
        degree[v] += value
        generate(index+1, new_matching)
        degree[u] -= value
        degree[v] -= value
    vector[index] = 0

generate(0, 0)
saved = json.loads((HERE/'REPLAY.json').read_text())['new_M2_7_8']
rows = {tuple(row['edge_vector']): row for row in saved['all_labeled_vectors']}
assert domain == set(rows)
counts, minima = {7: 0, 8: 0}, {7: 999, 8: 999}
for g in domain:
    deg = [sum(g[j] for j, pair in enumerate(PAIRS) if v in pair) for v in range(5)]
    twice_C3 = 0
    for i, j in combinations(range(10), 2):
        if set(PAIRS[i]) & set(PAIRS[j]):
            continue
        w = next(v for v in range(5) if v not in PAIRS[i]+PAIRS[j])
        twice_C3 += g[i]*g[j]*(8-deg[w])
    assert twice_C3 % 2 == 0
    c3 = twice_C3//2
    row = rows[g]
    assert c3 == row['C3_direct'] == row['C3_IE']
    m2 = row['M2']
    counts[m2] += 1
    minima[m2] = min(minima[m2], c3)
assert counts == {7: 1020, 8: 1395} and minima == {7: 18, 8: 21}
result = {'status': 'PASS', 'scope': 'Complete edge-domain equality with the independent forward-star domain; exact C3 matching formula versus direct/IE on all labels.',
          'labeled_counts': counts, 'C3_minima': minima}
(HERE/'EDGE_DOMAIN_CHECK.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
