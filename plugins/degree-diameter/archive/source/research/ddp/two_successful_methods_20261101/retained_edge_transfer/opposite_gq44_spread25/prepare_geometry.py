#!/usr/bin/env python3
"""One fixed GF4/GF16 symplectic GQ(4,4) geometry; no graph/BFS/solver."""
import itertools
import json
from pathlib import Path
import resource
import time

OUT = Path(__file__).resolve().parent
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
START = time.process_time()

def write(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2) + '\n')

def m4(a, b):
    product = 0
    for i in range(2):
        if (b >> i) & 1:
            product ^= a << i
    if product & 4:
        product ^= 7
    return product

M4 = [[m4(a, b) for b in range(4)] for a in range(4)]
I4 = [None] + [next(b for b in range(1, 4) if M4[a][b] == 1) for a in range(1, 4)]

def m16(a, b):
    a0, a1 = a % 4, a // 4
    b0, b1 = b % 4, b // 4
    c0 = M4[a0][b0] ^ M4[2][M4[a1][b1]]
    c1 = M4[a0][b1] ^ M4[a1][b0] ^ M4[a1][b1]
    return c0 + 4 * c1

M16 = [[m16(a, b) for b in range(16)] for a in range(16)]
I16 = [None] + [next(b for b in range(1, 16) if M16[a][b] == 1) for a in range(1, 16)]

def power16(a, exponent):
    value = 1
    for _ in range(exponent):
        value = M16[value][a]
    return value

field_checks = {}
for q, table in ((4, M4), (16, M16)):
    assert all(table[a][b] == table[b][a] for a in range(q) for b in range(q))
    assert all(table[a][1] == a and table[a][0] == 0 for a in range(q))
    assert all(table[table[a][b]][c] == table[a][table[b][c]]
               and table[a][b ^ c] == (table[a][b] ^ table[a][c])
               for a in range(q) for b in range(q) for c in range(q))
    field_checks[f'GF{q}_field_laws'] = True
assert all((M4[x][x] ^ x ^ 2) != 0 for x in range(4))
assert M16[4][4] == (4 ^ 2)
TRACE = [a ^ power16(a, 4) for a in range(16)]
assert TRACE == [a // 4 for a in range(16)]
field_checks.update(beta_polynomial_irreducible_over_GF4=True,
                    beta_squared_equals_beta_plus_w=True,
                    relative_trace_equals_beta_coefficient=True)

VECTORS = list(itertools.product(range(4), repeat=4))
def normalize(x):
    first = next(a for a in x if a != 0)
    return tuple(M4[I4[first]][a] for a in x)

def form(x, y):
    xu, xv = x[0] + 4*x[1], x[2] + 4*x[3]
    yu, yv = y[0] + 4*y[1], y[2] + 4*y[3]
    return TRACE[M16[xu][yv] ^ M16[xv][yu]]

POINTS = sorted({normalize(v) for v in VECTORS if any(v)})
P_ID = {p: i for i, p in enumerate(POINTS)}
assert len(POINTS) == 85
BASIS = [tuple(int(i == j) for j in range(4)) for i in range(4)]
assert all(form(x, x) == 0 for x in VECTORS)
assert all(any(form(x, e) for e in BASIS) for x in VECTORS if any(x))
# Each argument is GF4 linear: evaluate all vectors against basis combinations.
assert all(form(x, y) == form(y, x) for x in VECTORS for y in BASIS)
assert all(form(x, tuple(M4[c][z] for z in y)) == M4[c][form(x, y)]
           for x in VECTORS for y in BASIS for c in range(4))
assert all(form(x, tuple(a ^ b for a, b in zip(y, z))) == (form(x, y) ^ form(x, z))
           for x in VECTORS for y in BASIS for z in BASIS)

LINE_ORIGINS = {}
for i, x in enumerate(POINTS):
    for j in range(i+1, len(POINTS)):
        y = POINTS[j]
        if form(x, y) != 0:
            continue
        line = tuple(sorted({P_ID[normalize(tuple(M4[a][xx] ^ M4[b][yy]
                            for xx, yy in zip(x, y)))]
                            for a in range(4) for b in range(4) if a or b}))
        assert len(line) == 5
        LINE_ORIGINS.setdefault(line, [i, j])
LINES = sorted(LINE_ORIGINS)
assert len(LINES) == 85
L_ID = {l: i for i, l in enumerate(LINES)}
POINT_LINES = [[l for l, pts in enumerate(LINES) if p in pts] for p in range(85)]
assert all(len(ls) == 5 for ls in POINT_LINES)
PAIR_LINE = {}
for l, pts in enumerate(LINES):
    for p, q in itertools.combinations(pts, 2):
        assert (p, q) not in PAIR_LINE
        PAIR_LINE[p, q] = l
        assert form(POINTS[p], POINTS[q]) == 0
assert all(((p,q) in PAIR_LINE) == (form(POINTS[p], POINTS[q]) == 0)
           for p in range(85) for q in range(p+1,85))
assert all(len(set(LINES[l]) & set(LINES[m])) <= 1
           for l in range(85) for m in range(l+1,85))

PROJECTION = [[None]*85 for _ in range(85)]
WITNESSES = []
for p in range(85):
    for l, pts in enumerate(LINES):
        if p in pts:
            continue
        projections = [q for q in pts if form(POINTS[p], POINTS[q]) == 0]
        assert len(projections) == 1
        q = projections[0]
        n = PAIR_LINE[tuple(sorted((p,q)))]
        PROJECTION[p][l] = q
        WITNESSES.append([p,l,q,n])
assert len(WITNESSES) == 6800

SPREAD = []
for a in range(16):
    points = set()
    for u in range(1,16):
        v = M16[a][u]
        points.add(P_ID[normalize((u%4,u//4,v%4,v//4))])
    line = tuple(sorted(points))
    assert len(line) == 5 and line in L_ID
    SPREAD.append({'index': a, 'slope_code': a, 'slope_pair': [a%4,a//4],
                   'line_id': L_ID[line], 'points': list(line)})
line = tuple(sorted({P_ID[normalize((0,0,v%4,v//4))] for v in range(1,16)}))
assert len(line) == 5 and line in L_ID
SPREAD.append({'index': 16, 'slope_code': 'infinity', 'line_id': L_ID[line], 'points': list(line)})
assert len({item['line_id'] for item in SPREAD}) == 17
assert sorted(p for item in SPREAD for p in item['points']) == list(range(85))
CPU = time.process_time() - START

write('FIELD_TABLES.json', {
    'GF4': {'definition': 'F2[w]/(w^2+w+1)', 'encoding': '0,1,2=w,3=w+1',
            'addition': [[a^b for b in range(4)] for a in range(4)],
            'multiplication': M4, 'inverse_nonzero': I4[1:]},
    'GF16': {'definition': 'GF4[beta]/(beta^2+beta+w)',
             'encoding': 'u0+4*u1 represents u0+u1*beta',
             'elements': [[a%4,a//4] for a in range(16)],
             'addition': [[a^b for b in range(16)] for a in range(16)],
             'multiplication': M16, 'inverse_nonzero': I16[1:],
             'trace_GF16_to_GF4': TRACE,
             'primitive_element_codes': [a for a in range(1,16) if len({power16(a,k) for k in range(15)})==15]},
    'checks': field_checks})
write('PARAMETERS.json', {
    'stage': 'GEOMETRY_READY_ONLY_NO_SOURCE_GRAPH',
    'GF4': 'F2[w]/(w^2+w+1); addition XOR; code2=w, not Zmod4',
    'GF16': 'GF4[beta]/(beta^2+beta+w); code u0+4*u1',
    'point_coordinates': '(u0,u1,v0,v1), with u=u0+u1*beta, v=v0+v1*beta',
    'point_normalization': 'multiply by GF4 inverse of first nonzero coordinate; lexicographic sorted tuple IDs',
    'points': [list(p) for p in POINTS],
    'alternating_form': 'Trace_GF16/GF4(u*v_prime+v*u_prime), Trace(a0+a1*beta)=a1',
    'line_label_rule': 'lexicographic sorted five-point-ID tuples',
    'lines': [{'line': i, 'points': list(l), 'generating_point_pair': LINE_ORIGINS[l]}
              for i,l in enumerate(LINES)],
    'point_incident_lines': POINT_LINES,
    'spread': SPREAD,
    'spread_line_labels': [item['line_id'] for item in SPREAD],
    'point_spread_owner': [next(item['index'] for item in SPREAD if p in item['points']) for p in range(85)],
    'old_vertex_label_prediction': '85*point+line',
    'old_adjacency_prediction': 'distinct (p,l),(q,m), with p in m and q in l',
    'new_vertex_label_prediction': '7225+spread_index, slopes0..15 then infinity',
    'new_pins_prediction': 'all old flags(p,l) with p on spread line and p on l',
    'scope': 'One fixed GF4 balanced GQ and one GF16 slope spread; no complete graph yet'})
write('PROJECTION_WITNESSES.json', {
    'columns': ['point_p', 'nonincident_line_l', 'unique_collinear_point_q_on_l', 'joining_line_pq'],
    'rows': WITNESSES,
    'point_line_projection_table': PROJECTION,
    'incident_entries': None})
result = {'status': 'PASS_GEOMETRY_READY_AWAIT_ROOT_GRAPH_RELEASE',
          'points': 85, 'lines': 85, 'points_per_line': 5, 'lines_per_point': 5,
          'incidences': 425, 'nonincident_point_line_pairs': 6800,
          'unique_projection_checks': 6800, 'spread_lines': 17,
          'spread_line_labels': [item['line_id'] for item in SPREAD],
          'spread_partitions_points': True, 'field_checks': field_checks,
          'alternating_form_checked': True, 'nondegenerate_form_checked': True,
          'point_pair_maximum_common_lines': 1, 'line_pair_maximum_common_points': 1,
          'all_collinear_pairs_match_B_zero': True, 'CPU_seconds': CPU,
          'worker_count': 1, 'solver_calls': 0, 'BFS_calls': 0,
          'complete_source_graph_generated': False, 'candidate_graph_generated': False}
write('GQ_AXIOM_CHECK.json', result)
write('GEOMETRY_STATE.json', result)
print(json.dumps(result, indent=2))
