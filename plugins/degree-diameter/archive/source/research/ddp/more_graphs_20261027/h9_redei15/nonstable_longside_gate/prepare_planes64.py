"""Select cached planes and generate their line-anchored affine81 coordinates.

Only finite-field algebra; no graph, degree filtering, projectivities or coverage.
"""
from pathlib import Path
from collections import Counter
import importlib.util
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (14, 14))
ROOT = Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math')
OUT = Path(__file__).resolve().parent
OLD = OUT.parents[1] / 'h9_baer_nonstable_global_pool'
COORDS = ROOT / 'research/ddp/global_coverage_20261027/h9_quadric_line_signature/point_coords.u8.bin'
GEOMETRY = COORDS.parent / 'geometry.py'


def save(name, obj):
    (OUT / name).write_text(json.dumps(obj, indent=2) + '\n')


save('PLANES64_PREDICTION.json', {
    'status': 'FROZEN_BEFORE_PLANE_SELECTION_AND_AFFINE_COORDINATES',
    'question': 'The64 eligible rational lines each have exactly6 cached nonstable generatorplanes; each intersects its Frobenius conjugate in that same line.',
    'expected_planes': 384,
    'input': 'eligible_lines_d12.json on actual42402/245937',
    'method': 'Filter existing21840 cached planes, then rank/quadric checks and affine81 point-ID lookup.',
    'output': 'NONSTABLE_PLANES64.json',
    'CPU_budget_seconds': 15,
    'worker_hard_CPU_seconds': 14,
    'BFS': 0, 'R4': 0, 'projectivities': 0, 'graphs': 0, 'solver_calls': 0,
})

spec = importlib.util.spec_from_file_location('existing_h9_quadric_geometry', GEOMETRY)
geom = importlib.util.module_from_spec(spec)
spec.loader.exec_module(geom)
A, M, INV = geom.ADD, geom.MUL, geom.INV
NEG = [(3 - x % 3) % 3 + 3 * ((3 - x // 3) % 3) for x in range(9)]
SUB = [[A[x][NEG[y]] for y in range(9)] for x in range(9)]
FROB = [M[M[x][x]][x] for x in range(9)]


def rref(rows):
    rows = [list(r) for r in rows]
    rank = 0
    for col in range(7):
        pivot = next((j for j in range(rank, len(rows)) if rows[j][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = INV[rows[rank][col]]
        rows[rank] = [M[scale][x] for x in rows[rank]]
        for j in range(len(rows)):
            if j != rank and rows[j][col]:
                factor = rows[j][col]
                rows[j] = [SUB[x][M[factor][y]] for x, y in zip(rows[j], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return tuple(tuple(r) for r in rows[:rank])


def polar(x, y):
    # Polarization of x0*x4+x1*x5+x2*x6-x3^2 in characteristic3.
    value = M[x[3]][y[3]]
    for j in range(3):
        value = A[value][M[x[j]][y[j + 4]]]
        value = A[value][M[x[j + 4]][y[j]]]
    return value


gate = json.loads((OUT / 'eligible_lines_d12.json').read_text())
assert (gate['source_n'], gate['source_m'], gate['degree_cap']) == (42402, 245937, 12)
eligible = {r['line_index']: r for r in gate['records']}
assert len(eligible) == 64
lines = {r['line_index']: r for r in json.loads((OLD / 'F3_lines.json').read_text())['records']}
cached = json.loads((OLD / 'nonstable_planes.json').read_text())['records']
assert len(cached) == 21840
selected = [r for r in cached if r['F3line_index'] in eligible]
assert len(selected) == 384
counts = Counter(r['F3line_index'] for r in selected)
assert set(counts) == set(eligible) and set(counts.values()) == {6}

rawcoords = COORDS.read_bytes()
assert len(rawcoords) == 66430 * 7
coordinate_to_id = {tuple(rawcoords[7 * i:7 * i + 7]): i for i in range(66430)}
assert len(coordinate_to_id) == 66430
records = []
keys = set()
local_index = Counter()
for rec in sorted(selected, key=lambda r: (r['F3line_index'], r['plane_index'])):
    li = rec['F3line_index']
    line = eligible[li]
    e0, e1 = [tuple(r) for r in line['RREF_basis']]
    assert [list(e0), list(e1)] == lines[li]['RREF_basis']
    assert all(x < 3 for row in (e0, e1) for x in row)
    ell = rref([e0, e1])
    assert len(ell) == 2
    basis = tuple(tuple(r) for r in rec['RREF_basis'])
    assert rref(basis) == basis and len(basis) == 3
    assert len(rref(list(basis) + [e0, e1])) == 3
    assert all(geom.on_quadric(row) for row in basis)
    assert all(polar(basis[i], basis[j]) == 0 for i in range(3) for j in range(i + 1, 3))
    conjugate = rref([[FROB[x] for x in row] for row in basis])
    assert len(conjugate) == 3 and conjugate != basis
    assert len(rref(list(basis) + list(conjugate))) == 4
    assert len(rref(list(conjugate) + [e0, e1])) == 3
    # Both planes contain ell and their vector intersection has dimension2.
    w = next(row for row in basis if len(rref([e0, e1, row])) == 3)
    lineids = set(lines[li]['Q9point_ids10'])
    offgrid = [None] * 81
    for v in range(9):
        for u in range(9):
            point = geom.normalize(tuple(A[A[w[j]][M[u][e0[j]]]][M[v][e1[j]]] for j in range(7)))
            assert geom.on_quadric(point)
            rawid = coordinate_to_id[point]
            assert rawid not in lineids
            offgrid[u + 9 * v] = rawid
    assert len(set(offgrid)) == 81 and len(set(offgrid) | lineids) == 91
    assert basis not in keys
    keys.add(basis)
    records.append({
        'line_index': li,
        'line_RREF_basis': [list(e0), list(e1)],
        'line_basis_e0_e1': [list(e0), list(e1)],
        'plane_index': rec['plane_index'],
        'local_plane_index': local_index[li],
        'RREF_basis': [list(r) for r in basis],
        'complement_w': list(w),
        'basis_e0_e1_w': [list(e0), list(e1), list(w)],
        'offgrid_point_ids81': offgrid,
        'Q9_line_point_ids10': sorted(lineids),
        'longside_nonF3_point_ids6': line['raw_nonF3_points6'],
        'longside_whole_class_pins': line['whole_class_pins'],
        'frobenius_conjugate_RREF_basis': [list(r) for r in conjugate],
        'algebra_checks': {'vector_rank': 3, 'totally_singular': True,
                           'union_with_conjugate_rank': 4, 'intersection_vector_dim': 2,
                           'intersection_equals_input_line': True, 'affine_offgrid_unique': 81},
    })
    local_index[li] += 1

by_key = {tuple(tuple(r) for r in x['RREF_basis']): x['plane_index'] for x in records}
for rec in records:
    key = tuple(tuple(r) for r in rec['frobenius_conjugate_RREF_basis'])
    rec['frobenius_partner_plane_index'] = by_key[key]
    assert rec['frobenius_partner_plane_index'] != rec['plane_index']

result = {
    'status': 'COMPLETE64_LINES384_NONSTABLE_PLANES_AFFINE81_ALGEBRA_CHECKED',
    'source_n': 42402, 'source_m': 245937, 'degree_cap': 12,
    'line_count': 64, 'planes_per_line': 6, 'plane_count': len(records),
    'distinct_plane_count': len(keys), 'affine_points_per_plane': 81,
    'affine_point_ID_entries': len(records) * 81,
    'coordinate_cache': str(COORDS.relative_to(ROOT)),
    'plane_cache': str((OLD / 'nonstable_planes.json').relative_to(ROOT)),
    'line_cache': str((OLD / 'F3_lines.json').relative_to(ROOT)),
    'field_geometry_API': str(GEOMETRY.relative_to(ROOT)),
    'field_encoding': 'a+3*b encodes a+b*t; t^2=-1 overF3.',
    'field_ADD': A, 'field_MUL': M, 'field_FROB3': FROB,
    'offgrid_schema': 'index=u+9*v, rawID of normalized(w+u*e0+v*e1); u,v=0..8.',
    'nonstable_planes_reenumerated': False, 'old21840_plane_coordinates_reused': True,
    'source_BFS': 0, 'R4': 0, 'projectivities': 0, 'degree_pool_tests': 0,
    'candidate_graphs': 0, 'solver_calls': 0,
    'CPU_seconds': time.process_time(),
    'records': records,
}
save('NONSTABLE_PLANES64.json', result)
summary = {k: v for k, v in result.items() if k not in ('records', 'field_ADD', 'field_MUL')}
summary['result_file'] = 'NONSTABLE_PLANES64.json'
save('PLANES64_RESULT.json', summary)
print(json.dumps(summary), flush=True)
