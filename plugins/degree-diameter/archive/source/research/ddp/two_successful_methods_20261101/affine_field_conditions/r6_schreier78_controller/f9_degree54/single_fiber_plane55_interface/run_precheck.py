#!/usr/bin/env python3
"""One explicit transverse-plane pin interface; no graph/BFS/solver run."""
import time
START = time.process_time()
import csv
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent
P = json.loads((SOURCE / 'PARAMETERS.json').read_text())
BUDGET = 15.0

def add(a, b):
    return (a % 3 + b % 3) % 3 + 3 * ((a // 3 + b // 3) % 3)

def neg(a):
    return (-a % 3) + 3 * ((-(a // 3)) % 3)

def mul(a, b):
    return (a % 3 * (b % 3) - (a // 3) * (b // 3)) % 3 + 3 * ((a % 3 * (b // 3) + (a // 3) * (b % 3)) % 3)

def dot(a, b):
    x = 0
    for u, v in zip(a, b):
        x = add(x, mul(u, v))
    return x

def act(m, v):
    return tuple(dot(row, v) for row in m)

def sub(a, b):
    return tuple(add(x, neg(y)) for x, y in zip(a, b))

def encode(v):
    return v[0] + 9 * v[1] + 81 * v[2]

eta = 4
normal = (neg(eta), 0, 1)
squares = sorted({mul(a, a) for a in range(9)})
assert eta not in squares
assert all(mul(a, b) == P['field']['multiplication'][a][b] for a in range(9) for b in range(9))
directions = [tuple(v) for v in P['directions']]
pairings = [dot(normal, ell) for ell in directions]
assert all(pairings)
lines = [{tuple(mul(t, c) for c in ell) for t in range(9)} for ell in directions]
assert all(len(line) == 9 for line in lines)
centers = [(a, b, mul(eta, a)) for a in range(9) for b in range(9)]
assert len(set(centers)) == 81
assert all(dot(normal, x) == 0 for x in centers)
assert all(set(centers).intersection(line) == {(0, 0, 0)} for line in lines)
controller = P['controller']
dart_chart = P['dart_chart_index']
reverse = P['inverse_ports']
matrices = P['matrices']
neighbor_layers = controller[0]
assert len(set(neighbor_layers)) == 6 and 0 not in neighbor_layers
basis = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
for p, v in enumerate(neighbor_layers):
    q = reverse[p]
    m, r = matrices[dart_chart[0][p]], matrices[dart_chart[v][q]]
    assert controller[v][q] == 0
    assert act(m, directions[p]) == directions[q]
    assert all(act(r, act(m, e)) == e and act(m, act(r, e)) == e for e in basis)

all_rows = []
pin_sets = []
port_pins = [set() for _ in range(6)]
for j, x in enumerate(centers):
    pins = set()
    for p, v in enumerate(neighbor_layers):
        q = reverse[p]
        image = act(matrices[dart_chart[0][p]], x)
        for t in range(9):
            y = tuple(add(c, mul(t, e)) for c, e in zip(image, directions[q]))
            pin = 729 * v + encode(y)
            assert pin not in pins
            pins.add(pin)
            port_pins[p].add(pin)
            all_rows.append((j, encode(x), p, t, pin))
    assert len(pins) == 54
    pin_sets.append(pins)
counter = Counter(row[-1] for row in all_rows)
assert len(counter) == 4374 and max(counter.values()) == 1
for p, v in enumerate(neighbor_layers):
    assert port_pins[p] == {729 * v + x for x in range(729)}
pair_count = 0
for i in range(81):
    for j in range(i):
        criterion = any(sub(centers[i], centers[j]) in line for line in lines)
        assert (bool(pin_sets[i].intersection(pin_sets[j]))) == criterion
        assert not criterion
        pair_count += 1
assert pair_count == 3240

with (HERE / 'CENTER_SEQUENCE.csv').open('w', newline='') as f:
    out = csv.writer(f)
    out.writerow(['j', 'a', 'b', 'x0', 'x1', 'x2', 'old_label', 'proposed_new_label'])
    for j, x in enumerate(centers):
        out.writerow([j, j // 9, j % 9, *x, encode(x), 56862 + j])
with (HERE / 'PINS.csv').open('w', newline='') as f:
    out = csv.writer(f)
    out.writerow(['j', 'center_old_label', 'port', 'noise_code', 'pin_old_label'])
    out.writerows(all_rows)

parameters = {
    'source': '../PARAMETERS.json',
    'source_vertices': 56862, 'source_edges': 1535274, 'source_degree': 54,
    'field': 'GF3[w]/(w^2+1)', 'field_encoding': 'a+3b means a+bw',
    'source_controller_vertex': 0, 'eta': eta, 'eta_meaning': '1+w',
    'normal': list(normal), 'normal_direction_pairings': pairings,
    'plane': 'W={(a,b,4*a): a,b inGF9}; multiplication is GF9, not integer',
    'center_sequence': 'j=9*a+b, a outer0..8, b inner0..8',
    'center_source_label': 'a+9*b+81*GF9mul(4,a)',
    'proposed_new_label': '56862+j',
    'centers': [list(x) for x in centers],
    'center_old_labels': [encode(x) for x in centers],
    'pin_rule': 'immutable source fullN54, using exact source dart matrices and9noise values per6ports',
    'neighbor_controller_layers': neighbor_layers,
    'pins': 'PINS.csv', 'ordered_centers': 'CENTER_SEQUENCE.csv',
    'proposed_target': {'Delta': 55, 'D': 3, 'vertices': 56943, 'edges': 1539648},
    'predicted_degree_histogram': {'54': 52569, '55': 4374},
    'new_new_edges': 0,
    'source_induced_graph_unchanged': True,
    'single_fiber_capacity_upper': 81,
    'whole_source_capacity_optimality_claimed': False,
    'complete_extension_graph_generated': False,
    'public_gate_complete_here': False,
    'source_edge_file_read': False,
}
(HERE / 'PARAMETERS.json').write_text(json.dumps(parameters, ensure_ascii=False, indent=2) + '\n')
result = {
    'status': 'PASS_TRANSVERSE_PLANE_FULL_NEIGHBORHOOD_PACKING_INTERFACE_ONLY',
    'eta_is_nonsquare': True, 'field_squares': squares,
    'normal': list(normal), 'normal_direction_pairings': pairings,
    'centers': 81, 'source_neighbors_each': 54,
    'pairwise_common_neighborhood_tests': pair_count,
    'pairs_with_common_neighbor': 0,
    'pin_occurrences': len(all_rows), 'distinct_old_pins': len(counter),
    'max_old_pin_load': max(counter.values()),
    'neighbor_controller_layers': neighbor_layers,
    'pins_per_neighbor_fiber': [len(x) for x in port_pins],
    'all_six_neighbor_fibers_fully_partitioned': True,
    'predicted_target': parameters['proposed_target'],
    'predicted_degree_histogram': parameters['predicted_degree_histogram'],
    'all_prefix_D3': 'Analytic immutable-fullN clone proof in PROOF.md; only original source interior vertices, no future clones',
    'single_fiber_fullN_upper': 81,
    'source_edgefile_reads': 0, 'full_graphs_generated': 0,
    'BFS_Lean_solver_calls': 0, 'new_graph_counted': False,
    'field_controller_other_planes_searched': 0,
    'next': 'Return exact interface for separate root public55 gate; no generation in this scope',
}
(HERE / 'RESULT.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
cpu = time.process_time() - START
assert cpu < BUDGET
terminal = {
    'status': result['status'], 'returncode': 0,
    'total_CPU_seconds': cpu, 'CPU_budget_seconds': BUDGET,
    'single_worker': True, 'all_children_terminal': True,
    'compile_runs': 0, 'BFS_Lean_solver_runs': 0,
    'source_edgefile_reads': 0, 'complete_graphs_generated': 0,
    'measurement_boundary': 'One Python process: imports, literal source parameter read, finite interface checks, CSV/JSON writes; no interactive authoring time',
}
(HERE / 'TERMINAL.json').write_text(json.dumps(terminal, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'result': result, 'terminal': terminal}, ensure_ascii=False))
