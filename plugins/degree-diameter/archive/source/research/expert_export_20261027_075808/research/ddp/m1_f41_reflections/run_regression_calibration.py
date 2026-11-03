"""Prescribed tiny regression, saved-graph negative control, bounded speed pilot."""
import json
import resource
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EXE = HERE / 'search_reflections'


def run(args, prefix):
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    proc = subprocess.run([str(EXE), *map(str, args)], capture_output=True, text=True, check=True)
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    Path(str(prefix) + '.log').write_text(proc.stdout + proc.stderr)
    return after.ru_utime + after.ru_stime - before.ru_utime - before.ru_stime


expected = json.loads((HERE / 'regression_expected.json').read_text())
checks = []
total_cpu = 0.0
for idx, row in enumerate(expected['counts']):
    skeleton = HERE / f'regression_{idx}.skeletons.txt'
    skeleton.write_text(f"1\n{row['beta']} {row['sigma']} {row['tau']}\n")
    prefix = HERE / f'regression_{idx}'
    used = run([row['kind'], 5, 4, 2, skeleton, 5, prefix, 0, 0, 1], prefix)
    total_cpu += used
    got = json.loads(Path(str(prefix) + '.summary.json').read_text())
    assert got['raw_visited'] == row['raw_assignments']
    assert got['legal_fully_scored'] == row['legal_assignments']
    assert got['illegal_rejected'] == row['illegal_assignments']
    assert got['score_histogram'] == row['two_root_missing_histogram']
    assert got['diameter_histogram'] == row['diameter_histogram']
    checks.append({'case': idx, 'raw': got['raw_visited'], 'legal': got['legal_fully_scored'], 'exact_histogram_match': True, 'child_cpu_seconds': used})

prefix = HERE / 'regression_saved_f41'
used = run(['check', 41, 8, 3, 3, 5, 11, 29, 49, 275, prefix], prefix)
total_cpu += used
old = ROOT / 'computations/ddp/m1/d5_quotient/faithful/p41_m8_r3.search.best.edges'
def edges(path):
    lines = path.read_text().splitlines()
    return tuple(map(int, lines[0].split())), {tuple(sorted(map(int, line.split()))) for line in lines[1:]}
assert edges(Path(str(prefix) + '.edges')) == edges(old)
got = json.loads(Path(str(prefix) + '.json').read_text())
assert got['root_missing'] == [11, 14] and got['missing_sum'] == 25
checks.append({'case': 'saved_f41_negative', 'exact_edge_set_match': True, 'root_missing': got['root_missing'], 'child_cpu_seconds': used})

pilots = []
for kind in ['mixed', 'both']:
    prefix = HERE / f'calibration_{kind}'
    used = run([kind, 41, 8, 3, HERE / f'{kind}_skeletons.txt', 10, prefix, 100000, 0, 0], prefix)
    total_cpu += used
    got = json.loads(Path(str(prefix) + '.summary.json').read_text())
    assert got['raw_visited'] == 100000
    metadata = json.loads((HERE / 'profile_metadata.json').read_text())['branches'][kind]
    estimate = used / got['legal_fully_scored'] * metadata['legal_assignment_count_without_additional_symmetry']
    pilots.append({'branch': kind, 'raw': got['raw_visited'], 'legal': got['legal_fully_scored'], 'minimum_missing_seen': got['minimum_missing_seen'], 'child_cpu_seconds': used, 'estimated_full_branch_cpu_seconds': estimate})

result = {'status': 'REGRESSION_PASSED_CALIBRATION_COMPLETE', 'regression_checks': checks, 'pilots': pilots, 'total_child_cpu_seconds': total_cpu, 'production_estimate_cpu_seconds': sum(p['estimated_full_branch_cpu_seconds'] for p in pilots), 'raw_production_assignments': 14059884, 'legal_expected': 13740658}
(HERE / 'regression_calibration.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
