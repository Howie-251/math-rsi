"""Exactly 66 normalized F25 coset-tower generators, full BFS for each graph."""
import json
import time
from collections import Counter, deque
from pathlib import Path

START = time.process_time()
OUT = Path(__file__).resolve().parent
(OUT / 'candidates').mkdir(exist_ok=True)
BUDGET = 30.0

def add(x, y):
    return (x % 5 + y % 5) % 5 + 5 * ((x // 5 + y // 5) % 5)

def neg(x):
    return (-x % 5) % 5 + 5 * ((-(x // 5)) % 5)

def mul(x, y):
    a, b, c, d = x % 5, x // 5, y % 5, y // 5
    return (a * c + 2 * b * d) % 5 + 5 * ((a * d + b * c) % 5)

def power(x, k):
    out = 1
    for _ in range(k):
        out = mul(out, x)
    return out

order12 = [x for x in range(1, 25) if power(x, 12) == 1 and power(x, 6) != 1 and power(x, 4) != 1]
r = order12[0]
rp = [power(r, k) for k in range(12)]
assert r == 6 and len(set(rp)) == 12 and rp[6] == 4
outside = sorted(set(range(1, 25)) - set(rp))
assert len(outside) == 12

def inverse(element):
    x, k = element
    return neg(mul(rp[-k % 12], x)), -k % 12

def product(g, h):
    x, k = g
    y, ell = h
    return add(x, mul(rp[k], y)), (k + ell) % 12

def leaf(x, k): return 12 * x + k
def block(x, j): return 300 + 4 * x + j
def head(x): return 400 + x

involution = (1, 6)
assert inverse(involution) == involution
raw = [(x, k) for x in outside for k in range(12) if k != 6]
assert len(raw) == 132
assert all(inverse(a) in raw and inverse(a) != a and product(a, inverse(a)) == (0, 0) for a in raw)
representatives = [a for a in raw if a < inverse(a)]
assert len(representatives) == 66
assert {a for rep in representatives for a in (rep, inverse(rep))} == set(raw)
metadata = {
    'field': 'F5[u]/(u^2-2)', 'field_encoding': 'a+5*b encodes a+b*u',
    'action_element_encoding': r, 'action_element_coefficients': [1, 1],
    'action_order': 12, 'action_powers': rp, 'other_nonzero_multiplicative_orbit': outside,
    'involution': involution, 'raw_pair_elements': 132, 'inverse_pair_representatives': representatives,
    'candidate_count': 66, 'labels': {'leaf': '12*enc(x)+k', 'block': '300+4*enc(x)+j', 'head': '400+enc(x)'},
    'representative_roots': [0, 300, 400], 'bfs_roots_per_candidate': 425,
    'cpu_budget_seconds': BUDGET,
}
(OUT / 'definition.json').write_text(json.dumps(metadata, indent=2) + '\n')

def generate(a):
    S = (involution, a, inverse(a))
    assert len(set(S)) == 3 and (0, 0) not in S and set(map(inverse, S)) == set(S)
    edges = set()
    for x in range(25):
        for k in range(12):
            u = leaf(x, k)
            for s in S:
                y, ell = product((x, k), s)
                edges.add(tuple(sorted((u, leaf(y, ell)))))
            edges.add((u, block(x, k % 4)))
        for j in range(4):
            edges.add((block(x, j), head(x)))
    edges = sorted(edges)
    assert len(edges) == 850 and all(u != v for u, v in edges)
    adj = [[] for _ in range(425)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    assert all(len(neighbors) == 4 for neighbors in adj)
    return edges, adj

def write_edges(path, edges):
    with path.open('w') as out:
        out.write('425 850\n')
        for u, v in edges:
            out.write(f'{u} {v}\n')

def evaluate(adj):
    all_hist = Counter()
    spectra = {}
    ordered_bad = 0
    max_distance = 0
    for root in range(425):
        dist = [-1] * 425
        dist[root] = 0
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if dist[v] < 0:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        assert -1 not in dist
        counts = Counter(dist)
        all_hist.update(counts)
        ordered_bad += sum(count for distance, count in counts.items() if distance > 5)
        max_distance = max(max_distance, max(counts))
        orbit = 'leaf' if root < 300 else 'block' if root < 400 else 'head'
        if orbit not in spectra:
            spectra[orbit] = {'root': root, 'distance_histogram': dict(sorted(counts.items())),
                              'missing_within_five': sum(count for d, count in counts.items() if d > 5)}
        else:
            assert dict(counts) == spectra[orbit]['distance_histogram']
    assert ordered_bad % 2 == 0
    weighted = 300 * spectra['leaf']['missing_within_five'] + 100 * spectra['block']['missing_within_five'] + 25 * spectra['head']['missing_within_five']
    assert weighted == ordered_bad
    return {'diameter': max_distance, 'bad_unordered_pairs': ordered_bad // 2,
            'ordered_distance_histogram': dict(sorted(all_hist.items())), 'three_orbit_roots': spectra,
            'all_roots_checked': 425, 'all_roots_within_each_type_have_identical_spectrum': True}

results = []
best = None
found = False
with (OUT / 'candidate_results.jsonl').open('w') as records:
    for index, a in enumerate(representatives):
        if time.process_time() - START > BUDGET - 1.0:
            break
        edges, adj = generate(a)
        path = OUT / 'candidates' / f'candidate_{index:02d}.edges'
        write_edges(path, edges)
        result = {'index': index, 'a': a, 'a_inverse': inverse(a), 'involution': involution,
                  'edge_file': str(path.relative_to(OUT)), **evaluate(adj)}
        records.write(json.dumps(result) + '\n')
        records.flush()
        results.append(result)
        if best is None or result['bad_unordered_pairs'] < best['bad_unordered_pairs']:
            best = result
            write_edges(OUT / 'best.edges', edges)
            (OUT / 'best.json').write_text(json.dumps(best, indent=2) + '\n')
            print('BEST', json.dumps({'index': index, 'a': a, 'bad_pairs': best['bad_unordered_pairs'], 'diameter': best['diameter'], 'cpu_seconds': time.process_time() - START}), flush=True)
        if result['bad_unordered_pairs'] == 0:
            found = True
            break
summary = {
    'status': 'FOUND_D5_CANDIDATE' if found else 'COMPLETE_NO_SOLUTION' if len(results) == 66 else 'CPU_BUDGET_EXHAUSTED_PARTIAL',
    'candidate_count': 66, 'evaluated_candidates': len(results), 'next_candidate_index': len(results),
    'all_roots_per_candidate': 425, 'total_bfs_roots': 425 * len(results),
    'best_candidate_index': best['index'], 'best_bad_unordered_pairs': best['bad_unordered_pairs'],
    'best_diameter': best['diameter'], 'score_histogram': dict(sorted(Counter(r['bad_unordered_pairs'] for r in results).items())),
    'diameter_histogram': dict(sorted(Counter(r['diameter'] for r in results).items())),
    'cpu_budget_seconds': BUDGET, 'cpu_seconds': time.process_time() - START,
    'scope': 'Only the selected order-12 action and exactly the normalized one-inverse-pair plus one-involution generator family. No three-involution case, extra parameter or random search.',
}
(OUT / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
print('TERMINAL', json.dumps(summary), flush=True)
