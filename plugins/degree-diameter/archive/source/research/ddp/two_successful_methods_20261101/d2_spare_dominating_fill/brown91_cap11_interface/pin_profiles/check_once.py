import itertools
import json
import resource
import time
from collections import Counter
from pathlib import Path

resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
started = time.process_time()
root = Path(__file__).resolve().parent
assert (root / 'PRED.json').exists()

def add(x, y):
    return (x % 3 + y % 3) % 3 + 3 * ((x // 3 + y // 3) % 3)

def mul(x, y):
    a, b, c, d = x % 3, x // 3, y % 3, y // 3
    return (a * c + 2 * b * d) % 3 + 3 * ((a * d + b * c) % 3)

products = [[mul(x, y) for y in range(9)] for x in range(9)]
inverses = [0] + [next(y for y in range(1, 9) if products[x][y] == 1) for x in range(1, 9)]
points = [(1, a, b) for a in range(9) for b in range(9)]
points += [(0, 1, a) for a in range(9)] + [(0, 0, 1)]
assert len(points) == 91 and len(set(points)) == 91

def dot(p, q):
    return add(add(products[p[0]][q[0]], products[p[1]][q[1]]), products[p[2]][q[2]])

lines = [[j for j, q in enumerate(points) if dot(p, q) == 0] for p in points]
assert all(len(line) == 10 for line in lines)
absolute = {i for i, p in enumerate(points) if dot(p, p) == 0}
types = []
for i, line in enumerate(lines):
    count = len(absolute.intersection(line))
    if i in absolute:
        assert count == 1
        types.append('A')
    else:
        assert count in (0, 2)
        types.append('I' if count == 0 else 'E')
assert Counter(types) == {'A': 10, 'I': 36, 'E': 45}

neighbor_profiles = Counter()
closed = []
for i, line in enumerate(lines):
    old_neighbors = [j for j in line if j != i]
    typ = Counter(types[j] for j in old_neighbors)
    key = (types[i], typ['A'], typ['I'], typ['E'])
    neighbor_profiles[key] += 1
    closed.append(sum(1 << j for j in set(line) | {i}))
assert neighbor_profiles == {('A', 0, 0, 9): 10, ('I', 0, 5, 5): 36, ('E', 2, 4, 4): 45}

profiles = {}
tested = 0
for pole, line in enumerate(lines):
    line_kind = {'A': 'tangent', 'I': 'external', 'E': 'secant'}[types[pole]]
    for size in range(1, 10):
        for pins in itertools.combinations(line, size):
            tested += 1
            cover = 0
            counts = Counter(types[p] for p in pins)
            for p in pins:
                cover |= closed[p]
            ncover = cover.bit_count()
            key = (line_kind, size, counts['A'], counts['I'], counts['E'], ncover)
            if key not in profiles:
                profiles[key] = {'line_type': line_kind, 'size': size, 'A': counts['A'], 'I': counts['I'], 'E': counts['E'], 'closed_coverage': ncover, 'line_subset_instances': 0, 'representative_pole': pole, 'representative_pins': list(pins)}
            profiles[key]['line_subset_instances'] += 1
            if line_kind == 'tangent' and pole not in pins:
                assert counts['A'] == counts['I'] == 0
                assert ncover == 10 * size + 1
            elif line_kind == 'tangent':
                assert ncover == 9 * size + 1
            else:
                assert ncover <= 10 * size + 1 - max(0, 2 * size - 10)

assert tested == 91 * (2 ** 10 - 2)
max_by_size = {s: max(v['closed_coverage'] for v in profiles.values() if v['size'] == s) for s in range(1, 10)}
assert max_by_size == {s: 10 * s + 1 for s in range(1, 10)}
result = {
    'status': 'PASS_FIXED_GF9_COLLINEAR_PIN_PROFILE_PREDICTIONS',
    'field': 'GF3[w]/(w^2+1)',
    'field_encoding': 'a+3b for a+bw',
    'projective_points': 91,
    'point_type_counts': dict(Counter(types)),
    'line_subset_instances_tested': tested,
    'unique_profiles': len(profiles),
    'max_closed_coverage_by_size': max_by_size,
    'neighbor_type_profiles': [{'point_type': k[0], 'A': k[1], 'I': k[2], 'E': k[3], 'vertices': v} for k, v in sorted(neighbor_profiles.items())],
    'finite_CPU_seconds': time.process_time() - started,
    'CPU_budget_seconds': 5,
    'workers': 1,
    'source_edgelists_generated': 0,
    'target_graphs_generated': 0,
    'BFS_solver_Lean': 0,
    'multiplicity_scope': 'Pairs (projective line, pin subset); singleton subsets occur on10lines, larger subsets on1line.',
    'classic_geometry_not_counted_as_new_graph': True
}
(root / 'GEOMETRY.json').write_text(json.dumps({'points': points, 'polar_lines': lines, 'point_types': types, 'field_multiplication': products, 'field_inverses': inverses}, indent=2) + '\n')
(root / 'PROFILES.json').write_text(json.dumps(sorted(profiles.values(), key=lambda p: (p['line_type'], p['size'], p['A'], p['I'], p['E'], p['closed_coverage'])), indent=2) + '\n')
(root / 'RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result))
