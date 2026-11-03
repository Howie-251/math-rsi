"""One independent quotient BFS for the terminal saved best-BB parameters."""
import json
import time
from collections import Counter, deque
from pathlib import Path

START = time.process_time()
OUT = Path(__file__).resolve().parent
source = OUT / 'frontend.best_BB.json'
saved = json.loads(source.read_text())
S = set(map(tuple, saved['quotient_S_coordinates']))

def mul(a, b):
    result = 0
    while b:
        if b & 1:
            result ^= a
        b >>= 1
        a <<= 1
        if a & 64:
            a ^= 0x43
    return result

power = [1]
for _ in range(1, 21):
    power.append(mul(power[-1], 8))
assert len(set(power)) == 21 and mul(power[-1], 8) == 1
assert {(mul(power[-i % 21], x), -i % 21) for x, i in S} == S
edges = set()
for i in range(21):
    for x in range(64):
        u = x + 64 * i
        for y, j in S:
            v = (x ^ mul(power[i], y)) + 64 * ((i + j) % 21)
            if u != v:
                edges.add(tuple(sorted((u, v))))
        edges.add((u, 1344 + x + 64 * (i % 7)))
for b in range(7):
    for x in range(64):
        edges.add((1344 + x + 64 * b, 1792 + x))
adj = [set() for _ in range(1856)]
for u, v in edges:
    adj[u].add(v)
    adj[v].add(u)
distance = [-1] * 1856
distance[1344] = 0
queue = deque([1344])
while queue:
    u = queue.popleft()
    for v in adj[u]:
        if distance[v] < 0:
            distance[v] = distance[u] + 1
            queue.append(v)
assert -1 not in distance
actual_masks = [sum(1 << x for x in range(64) if distance[1344 + x + 64 * b] <= 5) for b in range(7)]
mismatches = []
for b in range(7):
    for x in range(64):
        predicted = bool(saved['BB_masks'][b] & (1 << x))
        actual = distance[1344 + x + 64 * b] <= 5
        if predicted != actual:
            mismatches.append({'x': x, 'b': b, 'saved_mask_reachable': predicted,
                               'BFS_distance': distance[1344 + x + 64 * b]})
missing = [1344 + x + 64 * b for b in range(7) for x in range(64)
           if distance[1344 + x + 64 * b] > 5]
assert len(missing) == saved['BB_missing'] == 18
assert actual_masks == saved['BB_masks'] and not mismatches
result = {
    'status': 'COMPLETE_ONE_SAVED_BEST_POINTWISE_BB_CHECK', 'source_parameters': source.name,
    'candidate_cursor': saved['candidate_cursor'], 'quotient_generators': sorted(S),
    'vertices': 1856, 'edges': len(edges), 'degree_histogram': dict(sorted(Counter(map(len, adj)).items())),
    'block_root': 1344, 'block_targets_checked': 448,
    'saved_BB_masks': saved['BB_masks'], 'BFS_BB_masks': actual_masks,
    'all_masks_and_all_block_targets_exactly_match': True, 'mismatches': mismatches,
    'BB_missing': len(missing), 'missing_block_labels': missing,
    'block_target_distances_in_label_order': distance[1344:1792],
    'block_root_missing_by_layer': {'leaf': sum(d > 5 for d in distance[:1344]),
                                    'block': len(missing), 'head': sum(d > 5 for d in distance[1792:])},
    'cpu_seconds': time.process_time() - START,
    'scope': 'Only one terminal saved quotient parameter object was expanded; one block-root BFS, no batch repeat or C42 lift search.',
}
(OUT / 'frontend.best_BB.independent_check.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'block_target_distances_in_label_order'}, indent=2))
