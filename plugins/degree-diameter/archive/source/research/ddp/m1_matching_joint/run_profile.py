from pathlib import Path
import json
import os
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[2]
os.chdir(PROJECT)
cpp = [json.loads(line) for line in (HERE / 'regression_upto5.seed_scores.jsonl').read_text().splitlines()]
independent = json.loads((HERE / 'lower_bound_upto5_ten_check.json').read_text())['candidate_results']
assert len(cpp) == len(independent) == 10
for a, b in zip(cpp, independent):
    assert a['seed'] == b['candidate']
    assert a['old_old'] == b['lower_bound_old_old']
    assert a['new_old'] == [b['lower_bound_new_u'], b['lower_bound_new_v']]
    assert a['lower_bound'] == b['lower_bound_total']

command = [str(HERE / 'search'),
           'research/ddp/m1_d7d5_source/baseline_normalized.edges',
           'research/ddp/m1_matching_augmentation/baseline.distances.u8',
           str(HERE / 'critical_upto5_pairs.txt'), str(HERE / 'seeds.txt'),
           str(HERE / 'profile'), '120']

def one_cpu():
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})

start = time.monotonic()
usage_before = resource.getrusage(resource.RUSAGE_CHILDREN)
with (HERE / 'profile.log').open('w') as log:
    process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, preexec_fn=one_cpu)
    (HERE / 'process.json').write_text(json.dumps({'pid': process.pid, 'command': command,
        'cpu_budget_seconds': 120, 'one_cpu': True, 'started_unix': time.time()}, indent=2) + '\n')
    print(f'launched pid {process.pid}', flush=True)
    code = process.wait()
usage_after = resource.getrusage(resource.RUSAGE_CHILDREN)
result = {'returncode': code, 'wall_seconds': time.monotonic() - start,
          'cpu_seconds': usage_after.ru_utime + usage_after.ru_stime - usage_before.ru_utime - usage_before.ru_stime}
(HERE / 'process_terminal.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result), flush=True)
