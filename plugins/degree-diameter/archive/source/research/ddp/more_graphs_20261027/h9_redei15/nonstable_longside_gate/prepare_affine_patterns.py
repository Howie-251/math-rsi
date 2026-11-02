"""The one frozen affine9 pattern family; no planes, degrees or coverage."""
from pathlib import Path
from itertools import product
import importlib.util
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (3, 3))
P = Path(__file__).resolve().parent
ROOT = Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math')
geometry = ROOT / 'research/ddp/global_coverage_20261027/h9_quadric_line_signature/geometry.py'
spec = importlib.util.spec_from_file_location('existing_affine9_field', geometry)
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)
ADD, MUL = g.ADD, g.MUL


def power(x, n):
    value = 1
    for _ in range(n):
        value = MUL[value][x]
    return value


matrices = sorted(
    t for t in product(range(3), repeat=4)
    if (t[0] * t[3] - t[1] * t[2]) % 3
    and next(x for x in t if x) == 1
)
assert len(matrices) == 24 and len(set(matrices)) == 24
points = [(x, MUL[6][power(x, 5)]) for x in range(9)]
patterns = {}
raw = 0
for ai, (a00, a01, a10, a11) in enumerate(matrices):
    linear = [(ADD[MUL[a00][x]][MUL[a01][y]],
               ADD[MUL[a10][x]][MUL[a11][y]]) for x, y in points]
    for r in range(1, 9):
        scaled = [(MUL[r][u], MUL[r][v]) for u, v in linear]
        for a in range(9):
            for b in range(9):
                ids = sorted(ADD[a][u] + 9 * ADD[b][v] for u, v in scaled)
                assert len(set(ids)) == 9
                mask = sum(1 << j for j in ids)
                raw += 1
                if mask not in patterns:
                    patterns[mask] = {
                        'pattern_index': len(patterns), 'grid_indices9': ids,
                        'witness': [ai, r, a, b], 'multiplicity': 1,
                        'mask_words_u64_decimal': [str(mask & ((1 << 64) - 1)), str(mask >> 64)],
                    }
                else:
                    patterns[mask]['multiplicity'] += 1
assert raw == 15552
records = list(patterns.values())
assert sum(r['multiplicity'] for r in records) == raw
assert [r['witness'] for r in records] == sorted(r['witness'] for r in records)
result = {
    'status': 'COMPLETE_FROZEN15552_AFFINE9_PARAMETERS_EXACT_MASK_DEDUP',
    'field_encoding': 'a+3*b for a+b*t, t^2=-1 overF3; use existing geometry.py.',
    'field_geometry_API': str(geometry.relative_to(ROOT)),
    'A24': [[[a, b], [c, d]] for a, b, c, d in matrices],
    'A24_flat': [list(a) for a in matrices],
    'matrix_order': 'Lexicographic flattened entries; invertible overF3; first nonzero entry1.',
    'source_graph_points': [[x, power(x, 5)] for x in range(9)],
    'transformed_source_points_after_Y6': [list(p) for p in points],
    'formula': 'u=a+r*(A00*x+A01*6*x^5); v=b+r*(A10*x+A11*6*x^5), all operations inF9.',
    'grid_index': 'u+9*v',
    'raw_parameter_count': raw,
    'unique_pattern_count': len(records),
    'record_order': 'First lexicographic witness[Aindex,r,a,b]; Aindex is0-based.',
    'grid_indices_order': 'Ascending grid index; represents the exact9-point set.',
    'records': records,
    'CPU_seconds_checkpoint': time.process_time(),
    'planes': 0, 'degree_tests': 0, 'BFS': 0, 'R4': 0, 'graphs': 0, 'solver_calls': 0,
}
(P / 'AFFINE_PATTERNS.json').write_text(json.dumps(result, indent=2) + '\n')
with (P / 'affine_patterns.txt').open('w') as f:
    f.write(str(len(records)) + '\n')
    for rec in records:
        values = [*rec['mask_words_u64_decimal'], rec['multiplicity'],
                  *rec['witness'], *rec['grid_indices9']]
        f.write(' '.join(map(str, values)) + '\n')
print(json.dumps({k: result[k] for k in ('status', 'raw_parameter_count',
                                       'unique_pattern_count', 'CPU_seconds_checkpoint')}), flush=True)
