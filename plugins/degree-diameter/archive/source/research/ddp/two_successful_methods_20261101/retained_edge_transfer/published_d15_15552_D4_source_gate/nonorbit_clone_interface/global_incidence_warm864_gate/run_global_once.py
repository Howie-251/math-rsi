"""One conditional warm-start MIP; never starts on import or without authorization."""
import argparse
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
CAP = 90.0


def save(name, value):
    p = HERE / name
    q = p.with_suffix(p.suffix + '.tmp')
    q.write_text(json.dumps(value, indent=2, allow_nan=False) + '\n')
    q.replace(p)


def main():
    started = time.process_time()
    ap = argparse.ArgumentParser()
    ap.add_argument('--root-authorized', action='store_true', required=True)
    ap.add_argument('--prior-total-cpu', type=float, required=True,
                    help='All prior D4case CPU, including local/postprocess/API/prep')
    args = ap.parse_args()
    prior = args.prior_total_cpu
    local_path = HERE.parent / 'append_oneout_twoin_gate/RESULT.json'
    local = json.loads(local_path.read_text())
    if not (local['status'] == 'COMPLETE_NO_APPEND_OR_ONE_OUT_TWO_IN_FIXED864_BINARY_CLONE_SCOPE'
            and local['full_domain_complete'] and not local['append_hit']):
        raise RuntimeError('Actual local complete NO required; root conditional run not satisfied')
    if (HERE / 'ATTEMPT.json').exists():
        raise RuntimeError('This one-shot attempt already exists; no automatic restart')
    # Two CPU seconds remain reserved for reporting/export after a hard child limit.
    hard = min(80, math.floor(CAP - prior - 2.0))
    time_limit = min(60.0, hard - 4.0)
    if hard < 6 or time_limit <= 0:
        raise RuntimeError('Insufficient cumulative CPU remains; do not start')
    packet = dict(status='ONE_SHOT_STARTING', driver_pid=os.getpid(), running=True,
                  prior_total_CPU_seconds=prior, cumulative_CPU_cap_seconds=CAP,
                  child_hard_CPU_seconds=hard, solver_time_limit_seconds=time_limit,
                  local_NO_receipt=str(local_path), root_authorized=True,
                  LP_MIP_run_count_planned=1)
    save('ATTEMPT.json', packet)
    save('HANDLE.json', packet)
    env = dict(os.environ)
    for k in ['OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
              'NUMEXPR_NUM_THREADS']:
        env[k] = '1'
    cmd = [sys.executable, '-u', str(HERE/'global_child.py'),
           '--hard-cpu', str(hard), '--time-limit', str(time_limit)]
    with (HERE/'GLOBAL_STDOUT.log').open('w') as out, (HERE/'GLOBAL_STDERR.log').open('w') as err:
        child = subprocess.Popen(cmd, stdout=out, stderr=err, env=env)
        packet.update(status='CHILD_ACTIVE', child_pid=child.pid, command=cmd)
        save('HANDLE.json', packet)
        _, status, usage = os.wait4(child.pid, 0)
        child.returncode = os.waitstatus_to_exitcode(status)
    child_cpu = usage.ru_utime + usage.ru_stime
    parent_cpu = time.process_time() - started
    total = prior + child_cpu + parent_cpu
    terminal = dict(status='CHILD_COMPLETE_CHECK_RAW_RESULT' if child.returncode == 0
                    else 'UNKNOWN_CHILD_FAILURE_NO_RESTART', running=False,
                    driver_pid=os.getpid(), child_pid=child.pid,
                    child_exit_code=child.returncode,
                    prior_total_CPU_seconds=prior, actual_child_CPU_seconds=child_cpu,
                    actual_driver_CPU_seconds=parent_cpu,
                    cumulative_CPU_seconds=total, cumulative_CPU_cap_seconds=CAP,
                    all_processes_terminal=True, retries=0,
                    old_source_BFS_field_Lean_ARIS_runs=0,
                    new_graph_parameter_Lean_count=[0, 0, 0])
    result_path = HERE/'RESULT.json'
    if result_path.exists():
        result = json.loads(result_path.read_text())
        terminal['status'] = result['status']
        terminal['best_count'] = result.get('best_count')
        terminal['candidate_generated'] = result.get('candidate_generated', False)
    else:
        save('RESULT.json', terminal)
    save('TERMINAL.json', terminal)
    save('HANDLE.json', terminal)
    print(json.dumps(terminal, allow_nan=False), flush=True)


if __name__ == '__main__':
    main()
