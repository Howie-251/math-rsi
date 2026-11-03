"""One single-core, bounded, sequential complete-family batch; no continuation."""
import json
import math
import resource
import subprocess
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
previous = json.loads((HERE / 'regression_calibration.json').read_text())['total_child_cpu_seconds']
# Reserve one CPU second for wrapper and bookkeeping, in addition to actual calibration.
budget = 299.0 - previous
used = 0.0
records = []
start = time.monotonic()
metadata = json.loads((HERE / 'profile_metadata.json').read_text())
for kind in ['mixed', 'both']:
    remaining = budget - used
    if remaining < 2:
        break
    prefix = HERE / f'complete_{kind}'
    command = [str(HERE / 'search_reflections'), kind, '41', '8', '3', str(HERE / f'{kind}_skeletons.txt'), str(remaining - 0.5), str(prefix), '0', '1', '0']
    def cpu_limit():
        cap = math.ceil(remaining)
        resource.setrlimit(resource.RLIMIT_CPU, (cap, cap + 1))
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    wall = time.monotonic()
    with Path(str(prefix) + '.log').open('w') as log:
        child = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT, preexec_fn=cpu_limit)
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    cpu = after.ru_utime + after.ru_stime - before.ru_utime - before.ru_stime
    used += cpu
    summary_path = Path(str(prefix) + '.summary.json')
    summary = json.loads(summary_path.read_text()) if summary_path.exists() else None
    record = {'branch': kind, 'command': command, 'exit_code': child.returncode, 'cpu_seconds': cpu, 'wall_seconds': time.monotonic() - wall, 'summary': summary}
    records.append(record)
    (HERE / 'production_process.json').write_text(json.dumps({'status': 'RUNNING' if kind == 'mixed' else 'FINISHED', 'prior_calibration_cpu_seconds': previous, 'production_cpu_seconds': used, 'cumulative_search_cpu_seconds': previous + used, 'wall_seconds': time.monotonic()-start, 'records': records}, indent=2) + '\n')
    print(json.dumps({'branch': kind, 'exit_code': child.returncode, 'cpu_seconds': cpu, 'status': summary and summary['status'], 'minimum_missing': summary and summary['minimum_missing_seen']}, ensure_ascii=False), flush=True)
    if child.returncode or summary['status'] != 'COMPLETE_NO_SOLUTION':
        break
    assert summary['raw_visited'] == metadata['branches'][kind]['raw_assignment_count']
    assert summary['legal_fully_scored'] == metadata['branches'][kind]['legal_assignment_count_without_additional_symmetry']

terminal = 'COMPLETE_NO_SOLUTION' if len(records)==2 and all(r['summary'] and r['summary']['status']=='COMPLETE_NO_SOLUTION' for r in records) else 'CANDIDATE_COVERED' if any(r['summary'] and r['summary']['status']=='CANDIDATE_COVERED' for r in records) else 'INCOMPLETE_STOPPED'
result = {'status': terminal, 'prior_calibration_cpu_seconds': previous, 'production_cpu_seconds': used, 'cumulative_search_cpu_seconds': previous + used, 'wall_seconds': time.monotonic()-start, 'records': records}
(HERE / 'production_process.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'terminal': terminal, 'cumulative_search_cpu_seconds': previous+used, 'wall_seconds': time.monotonic()-start}), flush=True)
