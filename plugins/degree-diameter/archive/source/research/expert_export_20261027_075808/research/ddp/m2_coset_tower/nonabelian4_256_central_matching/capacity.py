"""One symbolic short-walk pass over exactly22 fixed deletion choices; no graph/BFS."""
from pathlib import Path
from collections import Counter
from itertools import product
import json
import time

HERE = Path(__file__).resolve().parent
assert not (HERE / 'CAPACITY.json').exists(), 'This fixed22-case scope is already recorded.'
started = time.process_time()
base = json.loads((HERE.parent / 'nonabelian4_256_search' / 'best.json').read_text())
source_path = HERE.parent / 'nonabelian4_256_central_lift' / 'quotient_descent' / 'best_projection.json'
source = json.loads(source_path.read_text())
U, V, Q = base['edge_u'], base['edge_v'], source['projection']
free = base['free_edge_indices']
bit = {e: 1 << i for i, e in enumerate(free)}
classes = {}
for e, pair in enumerate(zip(U, V)):
    classes.setdefault(pair, []).append(e)
opposite_classes = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
deletions = [(a, b) for first, second in opposite_classes for a, b in product(classes[first], classes[second])]
assert len(deletions) == 22


def mul(g, h):
    x, s = g % 32, g // 32
    y, t = h % 32, h // 32
    return (x + (-1 if s else 1) * y + 16 * s * t) % 32 + 32 * (s ^ t)


def inverse(g):
    x, s = g % 32, g // 32
    return (x + 16) % 32 + 32 if s else (-x) % 32


def matrix_mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


records = []
for cursor, removed in enumerate(deletions):
    darts = [[] for _ in range(4)]
    adjacency = [[0] * 4 for _ in range(4)]
    for e, (u, v, q) in enumerate(zip(U, V, Q)):
        if e in removed:
            continue
        g = q % 16 + 32 * (q // 16)
        darts[u].append((v, 2 * e, g, bit.get(e, 0)))
        darts[v].append((u, 2 * e + 1, inverse(g), bit.get(e, 0)))
        adjacency[u][v] += 1
        adjacency[v][u] += 1
    assert all(len(row) == 7 for row in darts)
    a2 = matrix_mul(adjacency, adjacency)
    a3 = matrix_mul(a2, adjacency)
    capacity_formula = [[a3[i][j] + 2*a2[i][j] - 11*adjacency[i][j] - 12*(i == j)
                         for j in range(4)] for i in range(4)]
    measured_capacity, root_records = [], []
    for root in range(4):
        # Retain real edge IDs; no merging of projected parallel darts.
        paths = [(root, 0, 0, -1, 0, ())]
        for length in range(3):
            current = [p for p in paths if p[4] == length]
            for end, g, mask, last, _, word in current:
                for target, dart, h, b in darts[end]:
                    if last >= 0 and dart == (last ^ 1):
                        continue
                    paths.append((target, mul(g, h), mask ^ b, dart, length + 1, word + (dart,)))
        assert Counter(p[4] for p in paths) == {0: 1, 1: 7, 2: 42, 3: 252}
        formal = [set() for _ in range(4)]
        forms = [set() for _ in range(128)]
        cross_le2_targets = set()
        for end, g, mask, last, length, word in paths:
            # Abstract reduced cross word and central parity: upper capacity only.
            formal[end].add((word, 0))
            q = g % 16 + 16 * (g // 32)
            slot = 32 * end + q
            constant = (g % 32) // 16
            forms[slot].add((mask, constant))
            if length <= 2:
                formal[end].add((word, 1))
                forms[slot].add((mask, constant ^ 1))
                cross_le2_targets.add(slot)
        upper = [len(s) for s in formal]
        assert upper == capacity_formula[root] and sum(upper) == 352
        measured_capacity.append(upper)
        empty = [slot for slot, f in enumerate(forms) if not f]
        singleton = [slot for slot, f in enumerate(forms) if len(f) == 1]
        automatic = [slot for slot, f in enumerate(forms)
                     if any((mask, constant ^ 1) in f for mask, constant in f)]
        assert root * 32 in cross_le2_targets and root * 32 in automatic
        root_records.append({
            'root_orbit': root, 'cross_walk_counts_by_length': [1, 7, 42, 252],
            'quotient_empty_slots': empty, 'quotient_missing_count': len(empty),
            'singleton_central_form_slots': singleton,
            'cross_length_at_most2_quotient_target_count': len(cross_le2_targets),
            'automatically_two_lift_covered_slot_count': len(automatic),
            'central_form_cardinality_histogram': dict(sorted(Counter(map(len, forms)).items())),
        })
    records.append({
        'cursor': cursor, 'removed_edge_ids': list(removed),
        'removed_endpoint_classes': [[U[e], V[e]] for e in removed],
        'cross_multiplicity_matrix': adjacency,
        'abstract_central_commutation_capacity_matrix': measured_capacity,
        'capacity_matrix_minimum': min(map(min, measured_capacity)),
        'root_records': root_records,
        'sum_quotient_missing': sum(r['quotient_missing_count'] for r in root_records),
        'necessary_quotient_coverage_pass': all(r['quotient_missing_count'] == 0 for r in root_records),
    })
report = {
    'status': 'COMPLETE_FIXED22_SYMBOLIC_CHECK', 'source_projection_file': str(source_path),
    'source_projection': Q, 'edge_u': U, 'edge_v': V,
    'center': [16, 0], 'internal_matchings': 4, 'degree_per_internal_matching': 1,
    'new_cross_base_edge_count': 14, 'internal_lift_edge_count': 128,
    'total_lift_edges': 1024, 'vertices': 256, 'degree': 8,
    'scope_count': 22, 'records': records,
    'quotient_pass_count': sum(r['necessary_quotient_coverage_pass'] for r in records),
    'quotient_missing_sum_minimum': min(r['sum_quotient_missing'] for r in records),
    'quotient_missing_sum_maximum': max(r['sum_quotient_missing'] for r in records),
    'actual_center_assignments': 0, 'actual_graphs': 0, 'BFS_roots': 0,
    'CPU_seconds': time.process_time() - started,
}
(HERE / 'CAPACITY.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({k: v for k, v in report.items() if k not in ['records', 'edge_u', 'edge_v', 'source_projection']}))
