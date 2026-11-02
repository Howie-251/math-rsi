#!/usr/bin/env python3
"""One bounded binding check. No lifted graph, BFS, field or matrix search."""
import itertools
import json
import os
import resource
import time
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
start = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (5, 5))

def save(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2) + '\n')

save('HANDLE.json', {'pid': os.getpid(), 'status': 'RUNNING', 'CPU_limit': 5})
source = ROOT / 'research/ddp/refresh_20261029/f5_full_d20_D3/PARAMETERS.json'
data = json.loads(source.read_text())
C, T, L, inv = (data[k] for k in ['controller', 'matrices', 'directions', 'inverse_ports'])
cached = json.loads((ROOT / 'research/ddp/breadth_20261027_wave4/mizuno_d3_source/controller_structure.json').read_text())
q = data['field']
assert q == 5 and len(C) == 30
assert all(len(row) == 4 and len(set(row)) == 4 and u not in row for u, row in enumerate(C))
assert all(C[C[u][p]][inv[p]] == u for u in range(30) for p in range(4))

def mv(A, x):
    return [sum(a * b for a, b in zip(row, x)) % q for row in A]

def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) % q for j in range(3)] for i in range(3)]

def determinant(a, b, c):
    return (a[0] * (b[1]*c[2]-b[2]*c[1])
            - b[0] * (a[1]*c[2]-a[2]*c[1])
            + c[0] * (a[1]*b[2]-a[2]*b[1])) % q

def projective(v):
    pivot = next(x for x in v if x)
    return tuple(x * pow(pivot, -1, q) % q for x in v)

def quotient_point(v, line):
    pivot = next(i for i, x in enumerate(line) if x)
    scale = v[pivot] * pow(line[pivot], -1, q) % q
    return projective([(v[i] - scale * line[i]) % q for i in range(3) if i != pivot])

assert all(determinant(*(L[i] for i in triple)) for triple in itertools.combinations(range(4), 3))
I = [[int(i == j) for j in range(3)] for i in range(3)]
port_records = []
for p in range(4):
    r = inv[p]
    assert mm(T[r], T[p]) == I and mv(T[p], L[p]) == L[r]
    source_triple = {i: quotient_point(mv(T[p], L[i]), L[r]) for i in range(4) if i != p}
    target_triple = {j: quotient_point(L[j], L[r]) for j in range(4) if j != r}
    A, B = set(source_triple.values()), set(target_triple.values())
    assert len(A) == len(B) == 3
    turns = []
    for i, j in itertools.product(source_triple, target_triple):
        d = determinant(mv(T[p], L[i]), L[r], L[j])
        equal = source_triple[i] == target_triple[j]
        assert (d == 0) == equal
        turns.append({'source_port': i, 'target_port': j, 'det_mod5': d, 'quotient_points_equal': equal})
    k = len(A & B)
    assert k == 0 and len(A | B) == q + 1
    port_records.append({'port': p, 'inverse_port': r,
        'quotient_coordinate_rule': 'Eliminate first nonzero coordinate of reverse direction, then normalize remaining pair.',
        'source_triple': source_triple, 'target_triple': target_triple,
        'intersection_size': k, 'distinct_pencil_planes': 6-k,
        'pencil_union_size_by_formula': q + (6-k)*(q*q-q),
        'turns': turns, 'actual_inverse_and_direction_binding': True})
save('FOUR_PORT_PROJECTIVE_TRIPLES.json', {'field': 5, 'ports': port_records})

pair_records = []
kind_counts = Counter()
external = []
for u in range(30):
    words = [[] for _ in range(30)]
    for length in range(4):
        for ports in itertools.product(range(4), repeat=length):
            path = [u]
            for p in ports:
                path.append(C[path[-1]][p])
            if length == 0:
                kind = 'empty'
            elif length == 1:
                kind = 'direct'
            elif length == 2:
                kind = 'two_backtrack' if path[0] == path[2] else 'NB2'
            else:
                pre, post = path[0] == path[2], path[1] == path[3]
                kind = ('common_line_backtrack' if pre and post else
                        'pre_backtrack' if pre else 'post_backtrack' if post else 'NB3')
            words[path[-1]].append({'ports': ports, 'vertices': path, 'kind': kind})
    for v, W in enumerate(words):
        counts = Counter(w['kind'] for w in W)
        assert counts['NB3'] == cached['NB3_counts'][u][v]
        common = sorted(set(C[u]) & set(C[v]))
        if u == v:
            pair_type = 'same_layer'
            assert counts['NB3'] == 2 and counts['two_backtrack'] == 4
        elif v in C[u]:
            pair_type = 'triangle_adjacent' if common else 'external_adjacent'
            assert counts['NB3'] == 0
            assert counts['direct'] == counts['common_line_backtrack'] == 1
            assert counts['pre_backtrack'] == counts['post_backtrack'] == 3
            assert counts['NB2'] == (1 if common else 0)
            if not common:
                external.append([u, v])
        else:
            pair_type = 'nonadjacent'
            assert counts['NB3'] >= 1
        # Two distinct length-two paths would supply a controller four-cycle.
        if u != v:
            assert len(common) <= 1
        kind_counts[pair_type] += 1
        pair_records.append({'source': u, 'target': v, 'type': pair_type,
            'route_counts': dict(counts), 'all_length_at_most3_port_words': W})
assert [0, 20] in external and len(external) == 60
save('ALL_CONTROLLER_ROUTE_CLASSES.json', {'scope': 'All 900 ordered controller pairs, all port words of lengths 0 through 3.',
    'class_counts': dict(kind_counts), 'external_directed_edges': external, 'pairs': pair_records})
save('EXTERNAL_EDGE_0_20.json', next(row for row in pair_records if row['source'] == 0 and row['target'] == 20))
elapsed = time.process_time() - start
result = {'status': 'PREDICTION_SUPPORTED_BINDING_COMPLETE', 'pid': os.getpid(),
    'controller_ordered_pairs': 900, 'controller_port_words_including_empty': 30*(1+4+16+64),
    'route_class_counts': dict(kind_counts), 'external_directed_edges': 60,
    'external_routes_each': {'direct': 1, 'NB2': 0, 'NB3': 0, 'pre_backtrack': 3, 'post_backtrack': 3, 'common_line_backtrack': 1},
    'four_ports_intersection_sizes': [r['intersection_size'] for r in port_records],
    'central_turn_bindings': 36, 'new_full_fiber_pencil_point_enumerations': 0,
    'field_values_tested': [5], 'matrix_search': False, 'source_graph_BFS': False,
    'lifted_graphs_generated': 0, 'controller_BFS': False,
    'CPU_seconds': elapsed, 'budget_seconds': 5,
    'general_q_result_basis': 'Symbolic derivation, not finite-field enumeration.',
    'pending': []}
save('RESULT.json', result)
save('HANDLE.json', {'pid': os.getpid(), 'status': 'TERMINAL', 'return_code': 0, 'CPU_seconds': elapsed})
print(json.dumps(result), flush=True)
