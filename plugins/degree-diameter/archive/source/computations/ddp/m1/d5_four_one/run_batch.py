"""Exactly the four approved 4+1 instances, one CPU, 120 s total."""
from pathlib import Path
import datetime
import json
import os
import resource
import subprocess
import time

ROOT = Path(__file__).resolve().parent
EXE = ROOT / 'search_4plus1'
cases = json.loads((ROOT / 'batch.json').read_text())
started = time.monotonic()
completed = []
(ROOT / 'batch_process.json').write_text(json.dumps({
    'pid': os.getpid(), 'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'single_cpu_sequential': True, 'total_seconds_limit': 120,
    'case_count': len(cases),
}, indent=2) + '\n')
for case in cases:
    stem = f"p{case['p']}_m{case['m']}_r{case['r']}"
    remaining = 120 - (time.monotonic() - started)
    if remaining <= 0:
        break
    command = [str(EXE), str(case['p']), str(case['m']), str(case['r']),
               str(ROOT / (stem + '.skeletons.txt')), str(remaining), str(ROOT / (stem + '.search'))]
    print('START', stem, 'remaining', round(remaining, 3), flush=True)
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    with (ROOT / (stem + '.search.log')).open('w') as log:
        process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT)
        (ROOT / 'batch_current.json').write_text(json.dumps({'stem': stem, 'pid': process.pid, 'argv': command}, indent=2) + '\n')
        code = process.wait()
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    if code:
        raise RuntimeError(f'{stem} exit {code}')
    result = json.loads((ROOT / (stem + '.search.summary.json')).read_text())
    result['child_cpu_seconds'] = after.ru_utime + after.ru_stime - before.ru_utime - before.ru_stime
    result['stem'] = stem
    completed.append(result)
    (ROOT / 'batch_results.json').write_text(json.dumps({
        'wall_seconds': time.monotonic() - started,
        'child_cpu_seconds': sum(x['child_cpu_seconds'] for x in completed),
        'cases_completed': len(completed), 'cases': completed,
    }, indent=2) + '\n')
    print('TERMINAL', stem, result['status'], 'minimum', result['minimum_missing_seen'],
          'cpu', round(result['child_cpu_seconds'], 3), flush=True)
print('BATCH_TERMINAL', len(completed), 'wall', round(time.monotonic() - started, 3), flush=True)
