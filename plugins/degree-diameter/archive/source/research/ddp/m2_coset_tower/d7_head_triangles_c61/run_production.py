from pathlib import Path
import json, math, os, resource, subprocess, time

HERE = Path(__file__).resolve().parent
prep = json.loads((HERE / 'prepare.terminal.json').read_text())
assert prep['status'] == 'PREPARED_AND_PREFLIGHT_MATCHED'
assert prep['actual_original_BB_scope'] == 1944000
assert not (HERE / 'production.terminal.json').exists(), 'No automatic restart'
prior = prep['CPU_seconds']
remaining = 90 - prior - 1
assert remaining > 0

def cpu():
    a = resource.getrusage(resource.RUSAGE_SELF)
    b = resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime + a.ru_stime + b.ru_utime + b.ru_stime

def cap():
    limit = math.ceil(remaining)
    resource.setrlimit(resource.RLIMIT_CPU, (limit, limit))

start, wall = cpu(), time.monotonic()
args = [str(HERE / 'production'), 'run', str(HERE), str(remaining)]
with (HERE / 'production.log').open('w') as log:
    process = subprocess.Popen(args, stdout=log, stderr=subprocess.STDOUT, preexec_fn=cap)
    run = {
        'status': 'RUNNING', 'pid': process.pid, 'driver_pid': os.getpid(),
        'worker_count': 1, 'new_cursor': 0, 'actual_original_BB_scope': 1944000,
        'prior_CPU_seconds': prior, 'process_CPU_budget_seconds': remaining,
        'cumulative_CPU_budget_seconds': 90, 'command': args,
    }
    (HERE / 'production.run.json').write_text(json.dumps(run, indent=2) + '\n')
    print(json.dumps(run), flush=True)
    code = process.wait()
assert code == 0, f'Process exit {code}; do not restart automatically'
terminal = json.loads((HERE / 'production.terminal.json').read_text())
elapsed = cpu() - start
run.update(status=terminal['status'], exit_code=code, running=False,
           next_cursor=terminal['next_cursor'])
(HERE / 'production.run.json').write_text(json.dumps(run, indent=2) + '\n')
summary = {
    'status': terminal['status'], 'raw_HH_scope': 729000000,
    'normalized_scope': 24300000, 'safe_sign_scope': 12960000,
    'formal_word_pass_scope': 1944000,
    'actual_original_BB_evaluated': terminal['counts']['original_BB_evaluated'],
    'actual_BB_pass': terminal['counts']['BB_pass'],
    'preparation_compile_preflight_CPU_seconds': prior,
    'production_driver_CPU_seconds': elapsed, 'cumulative_CPU_seconds': prior + elapsed,
    'CPU_budget_seconds': 90, 'wall_seconds': time.monotonic() - wall,
    'worker_count': 1, 'restarts': 0,
    'independent_final': 'parent-owned; pending for the sole final saved graph',
    'root_statistics_population': 'actual BB survivors only',
    'one_minBB_fallback_scored': terminal['one_minBB_fallback_scored'],
    'preflight_cached_as_cursor0': True,
}
(HERE / 'production.summary.json').write_text(json.dumps(summary, indent=2) + '\n')
(HERE / 'terminal.json').write_text(json.dumps({
    'status': terminal['status'], 'summary': summary,
    'details': 'production.terminal.json',
}, indent=2) + '\n')
print(json.dumps(summary, indent=2), flush=True)
print(json.dumps(terminal['counts'], indent=2), flush=True)
