"""One tiny PG2(F9) seed/orbit check; no source graph or degree pool."""
from pathlib import Path
from collections import Counter
import importlib.util
import itertools
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
start = time.process_time()
P = Path(__file__).resolve().parent
ROOT = P.parents[4]
assert json.loads((P / 'PREDICTION.json').read_text())['frozen_before_numeric_seed_or_orbit_check']
old = json.loads((P.parent / 'pool/orbit.json').read_text())
shape = json.loads((P.parent / 'SHAPE.json').read_text())
spec = importlib.util.spec_from_file_location('h9_geometry', ROOT / 'research/ddp/global_coverage_20261027/h9_quadric_line_signature/geometry.py')
geom = importlib.util.module_from_spec(spec)
spec.loader.exec_module(geom)
ADD, MUL, INV, norm = geom.ADD, geom.MUL, geom.INV, geom.normalize
NEG = [MUL[2][a] for a in range(9)]
coeff = [tuple(v) for v in old['coefficient_points_PG2F9']]
idx = {v: i for i, v in enumerate(coeff)}
perms = old['generator_permutations']

def power(a, k):
    out = 1
    for _ in range(k):
        out = MUL[out][a]
    return out

def add3(a, b, c):
    return ADD[ADD[a][b]][c]

def dot(a, b):
    return add3(*(MUL[x][y] for x, y in zip(a, b)))

def cross(a, b):
    return norm(tuple(ADD[MUL[a[i]][b[j]]][NEG[MUL[a[j]][b[i]]]]
                      for i, j in [(1, 2), (2, 0), (0, 1)]))

def frob(p):
    return norm(tuple(power(a, 3) for a in p))

mu4 = sorted({MUL[a][a] for a in range(1, 9)})
assert mu4 == [1, 2, 3, 6]
units = [tuple(int(i == j) for i in range(3)) for j in range(3)]
Bplus = set(units)
for i, j in itertools.combinations(range(3), 2):
    for t in mu4:
        p = [0, 0, 0]
        p[i], p[j] = 1, t
        Bplus.add(norm(p))
R = [[1, 0, 0], [0, 1, 1], [0, 3, 6]]
# Its lower-right determinant is 6-3=3, a nonzero field element.
detR = ADD[MUL[1][6]][NEG[MUL[1][3]]]
assert detR != 0
Btw = {norm(tuple(dot(row, p) for row in R)) for p in Bplus}
assert len(Bplus) == len(Btw) == 15

def inspect(points):
    incidence = [[p for p in sorted(points) if dot(line, p) == 0] for line in coeff]
    counts = [len(pts) for pts in incidence]
    six = [coeff[i] for i, n in enumerate(counts) if n == 6]
    triangle = sorted({cross(a, b) for a, b in itertools.combinations(six, 2)})
    fixed = sorted(p for p in points if frob(p) == p)
    pairs = []
    seen = set(fixed)
    for p in sorted(points):
        if p not in seen:
            q = frob(p)
            assert q in points and q != p and frob(q) == p
            pairs.append([list(p), list(q)])
            seen.update([p, q])
    tangents = {str(list(p)): [list(coeff[i]) for i, pts in enumerate(incidence) if pts == [p]]
                for p in sorted(points)}
    return {
        'raw_points': [list(p) for p in sorted(points)],
        'point_count': len(points),
        'Frobenius_stable': {frob(p) for p in points} == points,
        'fixed_points': [list(p) for p in fixed],
        'fixed_point_count': len(fixed),
        'conjugate_pairs': pairs,
        'conjugate_pair_count': len(pairs),
        'fully_unsplit_pin_count': len(fixed) + len(pairs),
        'all91_lines_blocked': min(counts) >= 1,
        'minimal_blocking': all(tangents.values()),
        'line_intersection_histogram': dict(sorted(Counter(counts).items())),
        'six_secant_covectors': [list(v) for v in six],
        'triangle_vertices': [list(v) for v in triangle],
        'triangle_fixed_vertices': [list(p) for p in triangle if frob(p) == p],
        'triangle_fixed_vertex_count': sum(frob(p) == p for p in triangle),
        'tangent_witnesses': tangents,
    }

tw = inspect(Btw)
plus = inspect(Bplus)
old_inspect = inspect({tuple(p) for p in shape['raw_points']})
assert tw['Frobenius_stable'] and tw['fixed_point_count'] == 5 and tw['conjugate_pair_count'] == 5
assert tw['all91_lines_blocked'] and tw['minimal_blocking']
assert tw['line_intersection_histogram'] == {1: 60, 2: 12, 3: 16, 6: 3}
assert tw['triangle_fixed_vertex_count'] == 1
assert old_inspect['triangle_fixed_vertex_count'] == 3
assert plus['fixed_point_count'] == 9 and plus['conjugate_pair_count'] == 3

initial = sum(1 << idx[p] for p in Btw)
orbit, parents, generators = [initial], [-1], [-1]
which = {initial: 0}
members = []
for at, mask in enumerate(orbit):
    ids = [j for j in range(91) if (mask >> j) & 1]
    members.append(ids)
    for gi, perm in enumerate(perms):
        image = sum(1 << perm[j] for j in ids)
        if image not in which:
            which[image] = len(orbit)
            orbit.append(image)
            parents.append(at)
            generators.append(gi)
old_masks = {int(lo) + (int(hi) << 64) for lo, hi in old['mask_words_u64_decimal']}
intersection = sorted(set(orbit) & old_masks)
assert len(orbit) == 702 and not intersection
fixed_ids = {j for j, p in enumerate(coeff) if frob(p) == p}
assert all(len(ids) == 15 and sum(j in fixed_ids for j in ids) == 5 for ids in members)
orbit_out = {
    'status': 'COMPLETE_TWISTED_REDEI15_PGL3F3_MASK_ORBIT',
    'orbit_size': len(orbit), 'group': 'PGL3(F3)', 'group_order': 5616,
    'mask_stabilizer_order': 5616 // len(orbit),
    'raw_points_per_set': 15, 'Frobenius_fixed_points_per_set': 5,
    'fully_unsplit_pins_per_set': 10,
    'coefficient_points_PG2F9': old['coefficient_points_PG2F9'],
    'generator_matrices': old['generator_matrices'],
    'generator_permutations': perms,
    'parent': parents, 'generator': generators,
    'point_indices15': members,
    'mask_words_u64_decimal': [[str(m & ((1 << 64) - 1)), str(m >> 64)] for m in orbit],
    'old702_orbit_intersection_size': len(intersection),
    'F9_field_check': 'Existing h9 geometry.py ADD/MUL/INV reused directly; u=3, u^2=2.',
    'generator_proof': old['generator_proof'],
    'CPU_seconds': time.process_time() - start,
}
(P / 'orbit.json').write_text(json.dumps(orbit_out, ensure_ascii=False, indent=2) + '\n')
result = {
    'status': 'COMPLETE_NEW_STABLE_TRIANGLE_REAL_FORM',
    'prediction_status': 'SUPPORTED',
    'mu4': mu4, 'R_rows': R, 'R_determinant': detR,
    'twisted_seed': tw,
    'Bplus_control_only': plus,
    'old_seed_triangle_vertices': old_inspect['triangle_vertices'],
    'old_seed_triangle_fixed_vertex_count': old_inspect['triangle_fixed_vertex_count'],
    'new_orbit_size': len(orbit), 'old_orbit_size': len(old_masks),
    'old_new_exact_mask_intersection_size': len(intersection),
    'mask_stabilizer_order': 5616 // len(orbit),
    'source_pools_generated': 0, 'R4_runs': 0, 'graph_or_solver_runs': 0,
    'CPU_seconds': time.process_time() - start,
    'scope': 'Only the 91-point coefficient plane, the explicit projectivity seed, and its PGL3(F3) mask orbit; no source-level coverage claim.',
}
(P / 'RESULT.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: result[k] for k in ['status', 'new_orbit_size', 'old_new_exact_mask_intersection_size', 'CPU_seconds']}))
