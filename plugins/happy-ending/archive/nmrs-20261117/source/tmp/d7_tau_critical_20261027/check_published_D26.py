"""Our independent exact-integer geometry/color calibration; never author code."""
from itertools import combinations
from pathlib import Path
import hashlib
import json
import platform
import resource
import sys
import time

HERE = Path(__file__).resolve().parent
PRIOR = HERE.parent / 'd7_global_critical_20261027'
sys.path.insert(0, str(PRIOR))
from semantic_check import analyze, transversals


def sha(path):
    with path.open('rb') as stream: return hashlib.file_digest(stream, 'sha256').hexdigest()


def save(name, data):
    with (HERE / name).open('x') as out: json.dump(data, out, indent=2)


def main():
    assert platform.system() == 'Linux'
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3,) * 2)
    start = time.monotonic()
    witness = HERE / 'residual_26_points.json'
    author = HERE / 'check_residual_lower.py'
    expected = 'fcb21099d32753fef183b1759c02c296d8fb0d5539d0312180ed77c082484158'
    assert sha(witness) == expected
    assert sha(author) == '832f33cdaf08146f36fdfb836125abbb657f18fafcc1eb57693168e47901b447'
    raw = json.loads(witness.read_text())
    points = raw['points']
    assert len(points) == 26
    assert all(len(p) == 3 and all(type(v) is int for v in p) and p[2] > 0 for p in points)
    assert all(p[0] * q[2] < q[0] * p[2] for p, q in zip(points, points[1:]))
    colors, determinants = {}, {}
    for t in combinations(range(26), 3):
        a, b, c = [points[v] for v in t]
        det = (a[0] * (b[1] * c[2] - b[2] * c[1])
               - a[1] * (b[0] * c[2] - b[2] * c[0])
               + a[2] * (b[0] * c[1] - b[1] * c[0]))
        assert det != 0, 'collinear triple'
        colors[t], determinants[t] = det > 0, det
    save('published_D26_colors.json', {'n': 26, 'points': points,
        'red_iff': 'positive exact integer homogeneous determinant in supplied increasing-x order',
        'source_sha256': expected,
        'colors': [{'triple': t, 'red': colors[t], 'determinant': determinants[t]} for t in colors]})
    checked = analyze(colors, 26)
    checked.pop('_endpoints')
    save('published_D26_semantics.json', checked)
    report = {'schema': 'published_geometric_D26_independent_semantic_transversal_v1',
              'status': 'D7_VALID' if checked['D7_valid'] else 'D7_INVALID',
              'source_bindings': {str(p): sha(p) for p in (witness, author, Path(__file__), PRIOR / 'semantic_check.py')},
              'semantic_result': checked, 'solver_invocations': 0,
              'downloaded_author_code_executed': False,
              'independent_mathematical_review': False, 'production_acceptance': False}
    if checked['D7_valid']:
        report['red6_transversals'] = transversals(colors, 26)
        report['all_red6'] = [[v for v in range(26) if mask >> v & 1]
                             for mask in report['red6_transversals']['red6_masks']]
        report['tau5_counterexample'] = report['red6_transversals'].get('tau') == 5
    report['elapsed_seconds'] = time.monotonic() - start
    save('published_D26_calibration_result.json', report)
    print(json.dumps({'status': report['status'], 'maxR': len(checked['longest_red']),
                      'maxB': len(checked['longest_blue']), 'sameendsum': checked['max_same_endpoint_sum'],
                      'EndR5': checked['EndR5'], 'SrcB4': checked['SrcB4'],
                      'red6_count': report.get('red6_transversals', {}).get('red6_count'),
                      'tau': report.get('red6_transversals', {}).get('tau'),
                      'minimum_count': report.get('red6_transversals', {}).get('minimum_count'),
                      'tau5_counterexample': report.get('tau5_counterexample'),
                      'elapsed_seconds': report['elapsed_seconds']}, indent=2))


if __name__ == '__main__': main()
