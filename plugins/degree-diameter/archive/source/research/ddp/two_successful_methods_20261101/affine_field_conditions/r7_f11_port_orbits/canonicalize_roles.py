"""Rename the two already checked cross-port pairs; no orbit enumeration."""
import copy
import json
from pathlib import Path
from time import process_time, perf_counter

start, wall = process_time(), perf_counter()
root = Path(__file__).resolve().parent
old = root / 'initial_role_order'
old.mkdir(exist_ok=True)
for name in ['PARAMETERS.json', 'CHART_CHECKS.json', 'RESULT.json', 'TERMINAL.json']:
    assert not (old / name).exists(), 'This one-time relabeling already ran.'
    (old / name).write_bytes((root / name).read_bytes())
P = json.loads((old / 'PARAMETERS.json').read_text())
C = json.loads((old / 'CHART_CHECKS.json').read_text())
R = json.loads((old / 'RESULT.json').read_text())
T = json.loads((old / 'TERMINAL.json').read_text())
perm = [2, 3, 0, 1, 4, 5, 6]  # new port -> old port, also its inverse
rev = P['reverse_ports']
assert all(perm[perm[i]] == i and perm[rev[i]] == rev[perm[i]] for i in range(7))
rename = {
    'cross_0_1_forward': 'cross_2_3_forward',
    'cross_0_1_reverse': 'cross_2_3_reverse',
    'cross_2_3_forward': 'cross_0_1_forward',
    'cross_2_3_reverse': 'cross_0_1_reverse',
}
port_fields = ['selected_role_order_ids', 'selected_role_order_points',
               'port_orbit_ids', 'port_orbit_sizes', 'directions', 'H',
               'H_inverse', 'puncture_B_ids']
for key in port_fields:
    P[key] = [P[key][i] for i in perm]
for pair in P['allowed_source_target_pairs']:
    pair['source_port'] = perm[pair['source_port']]
    pair['target_port'] = perm[pair['target_port']]
P['allowed_source_target_pairs'].sort(key=lambda r: (r['source_port'], r['target_port']))
for chart in P['actual_charts']:
    chart['chart_id'] = rename.get(chart['chart_id'], chart['chart_id'])
    chart['source_port'] = perm[chart['source_port']]
    chart['target_port'] = perm[chart['target_port']]
    if 'forward_chart' in chart:
        chart['forward_chart'] = rename.get(chart['forward_chart'], chart['forward_chart'])
for row in C:
    row['chart_id'] = rename.get(row['chart_id'], row['chart_id'])
    row['turn_determinants'] = sorted([perm[s], perm[t], d] for s, t, d in row['turn_determinants'])
    for plane in row['planes']:
        plane['other_port'] = perm[plane['other_port']]
    row['planes'].sort(key=lambda r: (r['family'], r['other_port']))
P['actual_charts'].sort(key=lambda r: r['chart_id'])
C.sort(key=lambda r: r['chart_id'])
P['selection_rule'] = ('First lexicographic seven-set with a compatible reverse-port assignment. '
    'Its actual profile is two264 plus five330. The final port order swaps the two '
    'already checked cross-pairs so that the multiplicity-two type comes first; '
    'initial_role_order preserves the original finite run.')
P['role_names'] = ['a+', 'a-', 'b+', 'b-', 's', 't', 'r']
P['controller_interface'] = {
    'reverse_ports': rev,
    'type_preserving_required': True,
    'implemented_directed_port_pairs': [[i, rev[i]] for i in range(7)],
    'self_port_orientation_charts': {str(i): [f'self_{i}_plus', f'self_{i}_minus'] for i in (4, 5, 6)},
    'special_ports': [0, 1],
    'special_edges_must_form_spanning_2factor': True,
    'arbitrary_sorted_neighbor_port_labels_supported': False,
    'self_port_matrix_involutivity_assumed': False,
}
P['allowed_pairs_scope'] = ('29 orbit-compatible ordered pairs are recorded, but actual matrices '
    'and rank/pencil checks are supplied only for the fixed reverse-port pairs and self orientations.')

# Only recheck the transported 360 tiny determinants and ten literal inverses.
# No PGL group or subset classification is repeated.
def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) % 11 for j in range(3)] for i in range(3)]
def mv(A, v):
    return [sum(a * b for a, b in zip(row, v)) % 11 for row in A]
def det(a, b, c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])) % 11
I = [[1,0,0],[0,1,0],[0,0,1]]
checks = {c['chart_id']: c for c in C}
for chart in P['actual_charts']:
    a, b, A, B = chart['source_port'], chart['target_port'], chart['matrix'], chart['literal_inverse']
    assert mm(A, B) == I == mm(B, A)
    assert mv(A, P['directions'][a]) == P['directions'][b]
    assert mv(B, P['directions'][b]) == P['directions'][a]
    for s, t, d in checks[chart['chart_id']]['turn_determinants']:
        assert s != a and t != b
        assert d == det(P['directions'][b], mv(A, P['directions'][s]), P['directions'][t]) != 0
    assert checks[chart['chart_id']]['adjacent_union'] == 1331
assert P['selected_role_order_points'] == [1, 4, 'inf', 0, 2, 3, 5]
assert P['port_orbit_sizes'] == [264, 264, 330, 330, 330, 330, 330]
R['selected_ports'] = P['selected_role_order_points']
R['port_orbit_sizes'] = P['port_orbit_sizes']
R['role_relabeling'] = {'new_to_initial': perm, 'commutes_with_reverse_ports': True,
                       'PGL_or_subset_enumeration_repeated': False, 'new_charts_added': 0}
cpu, elapsed = process_time() - start, perf_counter() - wall
R['initial_experiment_CPU_seconds'] = R['CPU_seconds']
R['role_relabeling_CPU_seconds'] = cpu
R['CPU_seconds'] += cpu
R['wall_seconds'] += elapsed
T.update({'status': R['status'], 'running': False, 'active_processes': [],
          'CPU_seconds': R['CPU_seconds'], 'role_relabeling_CPU_seconds': cpu})
relabel = {'new_to_initial_ports': perm, 'commutes_with_reverse_ports': True,
           'unchanged_raw_point_set': P['selected_raw_points'],
           'unchanged_actual_matrix_multiset': True, 'new_charts': 0,
           'original_classification_repeated': False,
           'transported_NB_determinants_directly_rechecked': 360,
           'literal_two_sided_inverses_directly_rechecked': 10,
           'adjacent_plane_union_certificates_transported_by_bijection': 10,
           'CPU_seconds': cpu}
for name, value in [('PARAMETERS.json', P), ('CHART_CHECKS.json', C),
                    ('RESULT.json', R), ('TERMINAL.json', T), ('ROLE_RELABEL_CHECK.json', relabel)]:
    (root / name).write_text(json.dumps(value, indent=2) + '\n')
print(json.dumps({'ports': R['selected_ports'], 'types': R['port_orbit_sizes'],
                  'total_CPU_seconds': R['CPU_seconds'], 'status': R['status']}))
