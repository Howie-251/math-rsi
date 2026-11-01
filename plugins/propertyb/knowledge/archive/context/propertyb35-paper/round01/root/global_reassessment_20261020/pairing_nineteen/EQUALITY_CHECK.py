"""Small exact check of one 16-event partition; no H search or optimization."""
import itertools
import json
import time
from collections import Counter
from pathlib import Path

t0 = time.process_time()
base = [((0, 1, 2), (0, 0, 0)), ((0, 1, 3), (0, 1, 0)),
        ((0, 2, 3), (0, 1, 1)), ((1, 2, 3), (0, 1, 0))]
events = []
for branch, (support, pattern) in enumerate(base):
    for a, b in itertools.product(range(2), repeat=2):
        support5 = support + (4 + 2 * branch, 5 + 2 * branch)
        pattern5 = pattern + (a, b)
        flip = a ^ b
        edge = tuple(sorted(2 * i + (s ^ flip) for i, s in zip(support5, pattern5)))
        events.append({'support': support5, 'pattern': pattern5, 'edge': edge})

hist = Counter()
for z in itertools.product(range(2), repeat=12):
    hits = sum(len({z[i] ^ s for i, s in zip(e['support'], e['pattern'])}) == 1
               for e in events)
    hist[hits] += 1
assert hist == {1: 4096}

coeff = {2: Counter(), 4: Counter()}
for e in events:
    for size in (2, 4):
        for js in itertools.combinations(range(5), size):
            key = tuple(e['support'][j] for j in js)
            coeff[size][key] += (-1) ** sum(e['pattern'][j] for j in js)
assert all(v == 0 for c in coeff.values() for v in c.values())
degree = Counter(v for e in events for v in e['edge'])
assert Counter(degree.values()) == {6: 8, 2: 16}
support_degree = Counter(i for e in events for i in e['support'])
assert Counter(support_degree.values()) == {12: 4, 4: 8}
covered = set(p for e in events for p in itertools.combinations(e['edge'], 2))
assert len(covered) == 136
assert sum(max(0, 7 - degree[v]) for v in range(24)) == 88
common = set.intersection(*(set(e['support']) for e in events))
assert not common
actual_intersections = Counter(len(set(e['edge']) & set(f['edge']))
                               for e, f in itertools.combinations(events, 2))
assert min(actual_intersections) >= 1
for i, j in itertools.combinations(range(12), 2):
    n = [0, 0]
    for e in events:
        if i in e['support'] and j in e['support']:
            si = e['pattern'][e['support'].index(i)]
            sj = e['pattern'][e['support'].index(j)]
            n[si ^ sj] += 1
    assert n[0] == n[1]

result = {
    'status': 'PASS', 'scope': 'one explicit 16-event partition, not a 35-edge H',
    'events': events, 'assignments_checked': 4096,
    'event_hit_histogram': dict(hist), 'common_support': sorted(common),
    'point_degree_histogram': dict(Counter(degree.values())),
    'component_occurrence_histogram': dict(Counter(support_degree.values())),
    'point_pairs_covered_by_U': len(covered), 'point_pairs_uncovered': 276 - len(covered),
    'minimum_degree_completion_incidence_deficit': 88,
    'available_hit_edge_incidence': 95,
    'pairwise_actual_intersection_histogram': dict(actual_intersections),
    'all_quadratic_and_quartic_coefficients_zero': True,
    'cpu_seconds': time.process_time() - t0,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'events'}, indent=2))
