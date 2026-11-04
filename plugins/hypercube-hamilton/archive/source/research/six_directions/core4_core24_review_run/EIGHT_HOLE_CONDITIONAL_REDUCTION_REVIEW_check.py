"""Reviewer-owned deterministic checker; run with D:\\anaconda\\python.exe.

The C++ geometry pass enumerates unordered subsets by set bits, computes
all six face intersections as bit masks and tests the algebraic three-row
families. It never calls the producer's implementation.
"""
from pathlib import Path
import hashlib
import json
import subprocess

BASE = Path(__file__).resolve().parent
STEM = 'EIGHT_HOLE_CONDITIONAL_REDUCTION_REVIEW_check'

def digest(path):
    return 'sha256:' + hashlib.sha256(path.read_bytes()).hexdigest()

subprocess.run([r'D:\mingw64\bin\g++.exe', '-O3', '-std=c++17',
                str(BASE / (STEM + '.cpp')), '-o', str(BASE / (STEM + '.exe'))], check=True)
geometry = json.loads(subprocess.check_output([str(BASE / (STEM + '.exe'))], text=True))
assert [(r['target'], r['total'], r['bad']) for r in geometry] == [(7, 1300674, 0), (31, 1287690, 0)]
producer = json.loads((BASE / 'eight_hole_conditional_reduction_check.json').read_text(encoding='utf-8-sig'))
assert hashlib.sha256((BASE / 'eight_hole_free_cut_census.cpp').read_bytes()).hexdigest() == producer['source_sha256']
assert sum(r['total'] for r in geometry) == producer['free_geometries_checked']
assert producer['census_output'] == [f"v={r['target']} total={r['total']} bad={r['bad']}" for r in geometry]

good = {(a, b) for a in range(4) for b in range(5)
        if (b == a + 1 and a <= 2) or (b == a and a >= 1) or (b == a + 2 and a <= 2)}
bad = {(0, 0), (0, 3), (0, 4), (1, 0), (1, 4), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2), (3, 4)}
assert len(good) == 9 and good.isdisjoint(bad)
assert good | bad == {(a, b) for a in range(4) for b in range(5)}

example = producer['covered_residual_example']
z, w, root, target = set(example['Z']), set(example['W']), example['root'], example['target']
assert root == 0 and z == {6, 17, 53} and w == {11, 35, 41, 47} and target == 4
pc = int.bit_count
assert len(z) == 3 and len(w) == 4 and all(pc(x) % 2 == 0 for x in z)
assert all(pc(x) % 2 == 1 for x in w) and pc(target) % 2 == 1 and target not in w
assert all(pc(a ^ b) != 1 for a in z for b in w)
matching = example['matching']
ends = [x for edge in matching for x in edge]
assert len(matching) == 28 and len(ends) == len(set(ends)) == 56
assert all(0 <= x < 64 for x in ends)
assert all(pc(a ^ b) == 1 for a, b in matching)
assert set(range(64)) - set(ends) == {root} | z | w
assert target in ends
rows = [[sum(((x ^ target) & (1 << i)) == 0 for x in group) for group in (z, w)] for i in range(6)]
assert rows == example['cut_rows']
assert all(tuple(r) in bad for r in rows)
directions = sorted({(a ^ b).bit_length() - 1 for a, b in matching})
assert directions == list(range(6))

# Local symbolic bookkeeping: finite integer checks independent of matchings.
bookkeeping = []
for a, b in sorted(good):
    for delta in (0, 1):
        bridge = 'none' if b == a + 1 else ('even' if b == a else 'odd')
        local_A = (a + 1, a + 1) if bridge != 'even' else (a, a)
        # All A calls have two to six balanced holes.
        assert local_A[0] == local_A[1] and 1 <= local_A[0] <= 3
        if bridge == 'none':
            closed_B = (3 - a, 3 - a)
        elif bridge == 'even':
            closed_B = (3 - a, 5 - a)
        else:
            closed_B = (4 - a, 2 - a)
        assert min(closed_B) >= 0 and 2 <= sum(closed_B) <= 6
        assert abs(closed_B[0] - closed_B[1]) in (0, 2)
        bookkeeping.append({'a': a, 'b': b, 'delta': delta, 'bridge': bridge,
                            'A_holes': local_A, 'nonterminal_B_holes': closed_B})

inputs = ['EIGHT_HOLE_CONDITIONAL_REDUCTION_DRAFT.md', 'eight_hole_free_cut_census.cpp',
          'eight_hole_conditional_reduction_check.json']
result = {
    'status': 'PASS',
    'scope': 'finite_geometry_table_partition_and_concrete_residual_witness_only',
    'geometry': geometry,
    'total_geometries': sum(r['total'] for r in geometry),
    'good_rows': sorted(good), 'bad_rows': sorted(bad),
    'covered_witness': {'valid_short_matching': True, 'exact_holes': True,
                         'target_covered': True, 'nonroot_independent': True,
                         'all_cuts_bad': True, 'directions': directions, 'cut_rows': rows},
    'symbolic_branch_bookkeeping': bookkeeping,
    'audited_input_hashes': {name: digest(BASE / name) for name in inputs},
    'checker_hashes': {STEM + ext: digest(BASE / (STEM + ext)) for ext in ('.cpp', '.py')},
    'limitation': 'No Hamilton path, no A6 theorem and no R8-covered theorem is established by this checker.'
}
(BASE / (STEM + '.json')).write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'status': result['status'], 'geometry': geometry, 'covered_witness': result['covered_witness']}))
