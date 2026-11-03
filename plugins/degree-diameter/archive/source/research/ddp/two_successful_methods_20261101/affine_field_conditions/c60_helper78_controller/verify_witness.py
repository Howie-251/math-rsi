#!/usr/bin/env python3
"""Independent literal 78-controller verification, used only after SAT."""
import collections
import itertools
import json
from pathlib import Path
import resource
import time

START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
HERE = Path(__file__).resolve().parent
source = json.loads((HERE.parent.parent / 'f7_c60_d35/PARAMETERS.json').read_text())
source_edges = {tuple(sorted((u, v))) for u, ns in enumerate(source['controller']) for v in ns}
lines = (HERE / 'controller78.literal.edges').read_text().splitlines()
edges = [tuple(map(int, line.split())) for line in lines if line and not line.startswith('#')]
assert len(edges) == len(set(edges)) == 234
adj = [set() for _ in range(78)]
for u, v in edges:
    assert 0 <= u < v < 78
    adj[u].add(v)
    adj[v].add(u)
assert all(len(ns) == 6 for ns in adj)
assert {(u, v) for u, v in edges if v < 60} == source_edges
cliques = [list(range(0, 3)), list(range(3, 6)), list(range(6, 10)),
           list(range(10, 14)), list(range(14, 18))]
helper_edges = {(60 + i, 60 + j) for c in cliques for i, j in itertools.combinations(c, 2)}
assert {(u, v) for u, v in edges if u >= 60} == helper_edges
colors = []
for v in range(60):
    hs = adj[v] - set(range(60))
    assert len(hs) == 1
    colors.append(next(iter(hs)) - 60)
assert [colors.count(i) for i in range(18)] == [4] * 6 + [3] * 12
partition = json.loads((HERE / 'PIN_PARTITION.json').read_text())
assert partition['old_vertex_color'] == colors

# Direct all 216 walks from each root, independently of any SAT variables.
routes = []
counts = []
for root in range(78):
    targets = {}
    multiplicity = collections.Counter()
    walked = 0
    for a in sorted(adj[root]):
        for b in sorted(adj[a]):
            for c in sorted(adj[b]):
                walked += 1
                multiplicity[c] += 1
                targets.setdefault(c, [root, a, b, c])
    assert walked == 216
    assert len(targets) == 78, (root, sorted(set(range(78)) - set(targets)))
    routes.append([targets[target] for target in range(78)])
    counts.append([multiplicity[target] for target in range(78)])
ports = [sorted(ns) for ns in adj]
reverse = [[ports[v].index(u) for v in ports[u]] for u in range(78)]
for u in range(78):
    for p, v in enumerate(ports[u]):
        assert ports[v][reverse[u][p]] == u
dart_edges = [{'u': u, 'v': v, 'port_u': ports[u].index(v), 'port_v': ports[v].index(u)}
              for u, v in edges]
data = {'neighbor_by_local_port': ports, 'reverse_port': reverse,
        'undirected_edges_with_two_dart_ports': dart_edges,
        'chart_assignment': 'Use separately verified arbitrary-dart cross-port extension; no 1-factorization assumed.'}
(HERE / 'CONTROLLER_PORT_TABLE.json').write_text(json.dumps(data, indent=2) + '\n')
(HERE / 'ALL_6084_THREE_WALK_WITNESSES.json').write_text(json.dumps(routes) + '\n')
(HERE / 'ALL_6084_THREE_WALK_COUNTS.json').write_text(json.dumps(counts) + '\n')
result = {'status': 'PASS', 'vertices': 78, 'edges': 234,
          'simple': True, 'degree_histogram': {'6': 78},
          'old_induced_edges_exactly_preserved': 150,
          'helper_induced_edges': 24, 'pin_edges': 60,
          'pin_loads': [colors.count(i) for i in range(18)],
          'three_step_walks_per_root': 216, 'all_walks_enumerated': 78 * 216,
          'ordered_pairs_covered': 78 * 78, 'A_cubed_strictly_positive': True,
          'minimum_three_walk_multiplicity': min(map(min, counts)),
          'every_vertex_in_triangle': all(counts[v][v] > 0 for v in range(78)),
          'exact_diameter': 3, 'non_D2_reason': 'Moore bound 1+6+6*5=37 < 78',
          'dart_ports_each_vertex_exactly_0_through_5': True,
          'fiber_generated': False, 'old_fiber_BFS_calls': 0,
          'CPU_seconds': time.process_time() - START}
(HERE / 'VERIFIED.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
