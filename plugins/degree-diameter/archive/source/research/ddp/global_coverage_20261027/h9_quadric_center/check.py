"""One fixed P_center coordinate test; no incidence graph, routes, BFS or new graph."""
from pathlib import Path
from array import array
import importlib.util
import json
import resource
import sys
import time

sys.dont_write_bytecode = True
resource.setrlimit(resource.RLIMIT_CPU, (29, 30))
START = time.process_time()
OUT = Path(__file__).resolve().parent
SOURCE = OUT.parent / 'h9_quadric_line_signature'
assert json.loads((OUT / 'PREDICTION.json').read_text())['prediction_id'] == 'P_center'
spec = importlib.util.spec_from_file_location('h9_geometry', SOURCE / 'geometry.py')
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)
add, mul, inv = g.ADD, g.MUL, g.INV
neg = [(-a % 3) % 3 + 3 * ((-(a // 3)) % 3) for a in range(9)]
sub = [[add[a][neg[b]] for b in range(9)] for a in range(9)]
cube = [mul[mul[a][a]][a] for a in range(9)]
EQ = [((1, 2), (3, 4)), ((5, 4), (3, 2)), ((2, 0), (3, 5)),
      ((6, 5), (3, 0)), ((0, 1), (3, 6)), ((4, 6), (3, 1))]


def flatplane_center_rows(x):
    rows = []
    for (a, b), (c, d) in EQ:
        row = [0] * 7
        row[b] = add[row[b]][x[a]]
        row[a] = sub[row[a]][x[b]]
        row[d] = sub[row[d]][x[c]]
        row[c] = add[row[c]][x[d]]
        rows.append(row)
    # Polar of Q=x0*x4+x1*x5+x2*x6-x3^2; -2=1 in characteristic3.
    rows.append([x[4], x[5], x[6], x[3], x[0], x[1], x[2]])
    return rows


def kernel(rows):
    a = [list(r) for r in rows]
    pivots = []
    for col in range(7):
        pivot = next((r for r in range(len(pivots), len(a)) if a[r][col]), None)
        if pivot is None:
            continue
        r = len(pivots)
        a[r], a[pivot] = a[pivot], a[r]
        scale = inv[a[r][col]]
        a[r] = [mul[scale][v] for v in a[r]]
        for i in range(len(a)):
            if i == r or not a[i][col]:
                continue
            factor = a[i][col]
            a[i] = [sub[v][mul[factor][w]] for v, w in zip(a[i], a[r])]
        pivots.append(col)
    free = [c for c in range(7) if c not in pivots]
    basis = []
    for c in free:
        v = [0] * 7
        v[c] = 1
        for r, pc in enumerate(pivots):
            v[pc] = neg[a[r][c]]
        assert all(not dot(row, v) for row in rows)
        basis.append(v)
    return basis


def dot(x, y):
    value = 0
    for a, b in zip(x, y):
        value = add[value][mul[a][b]]
    return value


def is_h9_line(x, z):
    def grass(a, b):
        return sub[mul[x[a]][z[b]]][mul[x[b]][z[a]]]
    return all(grass(a, b) == grass(c, d) for (a, b), (c, d) in EQ)


e = [tuple(int(i == j) for i in range(7)) for j in range(7)]
fixtures = []
for name, x, z, expected_dim, expected_center in [
        ('H9_line_e0_e5', e[0], e[5], 2, None),
        ('external_Qline_e5_e6', e[5], e[6], 1, e[0])]:
    basis = kernel(flatplane_center_rows(x) + flatplane_center_rows(z))
    assert len(basis) == expected_dim
    if expected_center is not None:
        assert g.normalize(basis[0]) == expected_center
    fixtures.append({'name': name, 'basis_points': [list(x), list(z)],
                     'is_H9_line': is_h9_line(x, z), 'kernel_dimension': len(basis),
                     'kernel_basis': basis, 'expected_dimension': expected_dim,
                     'expected_center': list(expected_center) if expected_center else None})

coordinate_bytes = (SOURCE / 'point_coords.u8.bin').read_bytes()
point_to_core = array('H')
point_to_core.frombytes((SOURCE / 'point_to_core.u16.bin').read_bytes())
assert len(coordinate_bytes) == 7 * len(point_to_core) == 7 * 66430
point_index = {tuple(coordinate_bytes[7*i:7*i+7]): i for i in range(66430)}
source = json.loads((SOURCE / 'RESULT.json').read_text())
assert len(source['records']) == 675
records = []
first_center_failure = first_anchor_failure = None
for row in source['records']:
    if time.process_time() - START > 27:
        break
    w = row['witness']
    x, z = w['original_point_coordinates'][:2]
    assert not is_h9_line(x, z)
    rows = flatplane_center_rows(x) + flatplane_center_rows(z)
    basis = kernel(rows)
    out = {'vertex': row['vertex'], 'image_size': w['image_size'],
           'line_basis_original_labels': w['original_point_labels'][:2],
           'line_basis_coordinates': [x, z], 'kernel_dimension': len(basis),
           'kernel_basis': basis, 'extra_core_anchors': w['extra_anchors']}
    if len(basis) == 1:
        y = g.normalize(basis[0])
        singular = g.on_quadric(y)
        out['center_coordinates'] = list(y)
        out['center_singular'] = singular
        if singular:
            phi_y = tuple(cube[t] for t in y)
            yp, phip = point_index[y], point_index[phi_y]
            fiber = sorted({point_to_core[yp], point_to_core[phip]})
            anchors = set(w['extra_anchors'])
            out.update(center_original_label=yp,
                       phi_center_original_label=phip,
                       phi_center_coordinates=list(phi_y),
                       center_fold_phi_fiber=fiber,
                       anchor_subset_of_center_fold_phi_fiber=anchors <= set(fiber),
                       anchors_outside_center_fold_phi_fiber=sorted(anchors - set(fiber)),
                       center_original_point_on_selected_line=yp in w['original_point_labels'])
            if w['image_size'] == 10 and not anchors <= set(fiber) and first_anchor_failure is None:
                first_anchor_failure = out
    if len(basis) != 1 or not out.get('center_singular', False):
        if first_center_failure is None:
            first_center_failure = out
    records.append(out)


def histogram(values):
    result = {}
    for value in values:
        k = str(value)
        result[k] = result.get(k, 0) + 1
    return result

complete = len(records) == 675
image10 = [r for r in records if r['image_size'] == 10]
image7 = [r for r in records if r['image_size'] == 7]
result = {
    'prediction_id': 'P_center',
    'status': ('UNKNOWN_CPU_LIMIT' if not complete else
               'REFUTED' if first_center_failure is not None or first_anchor_failure is not None else 'SUPPORTED'),
    'fixed_selected_lines': 675, 'tested_selected_lines': len(records),
    'kernel_dimension_histogram': histogram(r['kernel_dimension'] for r in records),
    'singular_centers': sum(r.get('center_singular', False) for r in records),
    'centers_on_selected_lines': sum(r.get('center_original_point_on_selected_line', False) for r in records),
    'first_center_failure': first_center_failure,
    'image10': {'tested': len(image10),
                'anchor_subset_pass': sum(r.get('anchor_subset_of_center_fold_phi_fiber', False) for r in image10),
                'anchor_subset_fail': sum(not r.get('anchor_subset_of_center_fold_phi_fiber', False) for r in image10),
                'anchor_count_histogram': histogram(len(r['extra_core_anchors']) for r in image10),
                'center_fold_phi_fiber_size_histogram': histogram(len(r.get('center_fold_phi_fiber', [])) for r in image10)},
    'first_image10_anchor_failure': first_anchor_failure,
    'image7_descriptive_only': {'tested': len(image7),
                'anchor_subset_pass': sum(r.get('anchor_subset_of_center_fold_phi_fiber', False) for r in image7),
                'anchor_subset_fail': sum(not r.get('anchor_subset_of_center_fold_phi_fiber', False) for r in image7),
                'anchor_count_histogram': histogram(len(r['extra_core_anchors']) for r in image7),
                'center_fold_phi_fiber_size_histogram': histogram(len(r.get('center_fold_phi_fiber', [])) for r in image7)},
    'fixtures': fixtures, 'records': records,
    'input_selected_witnesses_changed': False,
    'H9_incidence_generated': False, 'BFS_performed': False,
    'new_graphs_generated': 0, 'pins_optimized': False, 'new_lower_bounds': 0,
    'CPU_seconds': time.process_time() - START,
    'pending': [] if complete else ['unprocessed_fixed_selected_lines'],
}
(OUT / 'RESULT.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'records'}, ensure_ascii=False, indent=2))
