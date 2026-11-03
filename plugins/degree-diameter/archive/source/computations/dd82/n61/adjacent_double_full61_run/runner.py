"""Root-launched bounded prepare, one solve, or separate certificate check.

Source delivery is unexecuted. A solve action permits at most 50 CPU/70 wall
seconds for CaDiCaL, followed only on SAT by 5/10 decoding and 5/10 independent
BFS. Thus the sum of child budgets is at most 60 CPU/90 wall seconds.
No restart or automatic certificate-check job is launched.
"""
import argparse
import json
import os
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOLVER = ROOT / '.tools/lean-4.24.0-linux/bin/cadical'
CHECKER = ROOT / '.tools/dd82-lrat-check/lrat-trim-rel-0.2.0/lrat-trim'
BFS = ROOT / 'computations/dd82/construction/verify_hs_candidate.py'
MEMORY_BYTES = 4 * 1024**3
OUTPUT_BYTES = 256 * 1024**2


def save(path, data):
    path.write_text(json.dumps(data, indent=2) + '\n')


def bounded(command, logfile, cpu_seconds, wall_seconds, cpu, cap_files=False):
    assert cpu in os.sched_getaffinity(0)

    def limits():
        os.sched_setaffinity(0, {cpu})
        resource.setrlimit(resource.RLIMIT_CPU, (cpu_seconds, cpu_seconds))
        resource.setrlimit(resource.RLIMIT_AS, (MEMORY_BYTES, MEMORY_BYTES))
        if cap_files:
            resource.setrlimit(resource.RLIMIT_FSIZE, (OUTPUT_BYTES, OUTPUT_BYTES))

    before, started = resource.getrusage(resource.RUSAGE_CHILDREN), time.monotonic()
    timed_out = False
    with logfile.open('w') as stream:
        process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT, preexec_fn=limits)
        try:
            rc = process.wait(timeout=wall_seconds)
        except subprocess.TimeoutExpired:
            timed_out = True
            process.kill()
            rc = process.wait()
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    return dict(command=command, exit_code=rc, wall_timeout=timed_out,
                termination_signal=signal.Signals(-rc).name if rc < 0 else None,
                cpu_seconds=after.ru_utime + after.ru_stime - before.ru_utime - before.ru_stime,
                wall_seconds=time.monotonic() - started, cpu_budget_seconds=cpu_seconds,
                wall_budget_seconds=wall_seconds, cpu_affinity=[cpu], threads=1,
                memory_limit_bytes=MEMORY_BYTES, per_file_limit_bytes=OUTPUT_BYTES if cap_files else None)


def prepare(cpu):
    assert not (HERE / 'preparation_process.json').exists(), 'Preserve the prior preparation attempt'
    result = bounded([sys.executable, str(HERE / 'encode.py'), 'prepare'],
                     HERE / 'prepare.log', 20, 30, cpu)
    result['status'] = 'PREPARED_NOT_RUN' if result['exit_code'] == 0 else 'PREPARATION_FAILED'
    result['solver_calls'] = 0
    save(HERE / 'preparation_process.json', result)
    print(json.dumps(result, indent=2), flush=True)


def solve(cpu, seconds, wall_seconds):
    assert 3 <= seconds <= 50 and 5 <= wall_seconds <= 70
    assert not (HERE / 'launch.json').exists(), 'Only one bounded solver attempt in this directory'
    assert not (HERE / 'proof.lrat').exists() and not (HERE / 'solver.log').exists()
    enc = json.loads((HERE / 'encoding.json').read_text())
    assert enc['status'] == 'PREPARED_NOT_RUN' and enc['primary_edge_variables'] == 1830
    assert os.access(SOLVER, os.X_OK)
    command = [str(SOLVER), '--lrat', '-t', str(seconds - 2),
               str(HERE / 'input.cnf'), str(HERE / 'proof.lrat')]
    save(HERE / 'launch.json', dict(status='LAUNCHED', command=command, scope=enc['scope'],
         cpu_affinity=[cpu], solver_calls=1, solver_os_cpu_limit_seconds=seconds,
         solver_soft_time_seconds=seconds - 2, solver_wall_limit_seconds=wall_seconds,
         maximum_child_cpu_seconds=seconds + 10, maximum_child_wall_seconds=wall_seconds + 20,
         memory_limit_bytes=MEMORY_BYTES, proof_and_log_per_file_limit_bytes=OUTPUT_BYTES,
         retained_internal_solver_state=False, automatic_restarts=0, certificate_check_automatic=False))
    result = bounded(command, HERE / 'solver.log', seconds, wall_seconds, cpu, cap_files=True)
    rc = result['exit_code']
    status = {10: 'SAT_CANDIDATE', 20: 'RAW_UNSAT', 0: 'UNKNOWN',
              -signal.SIGXFSZ: 'OUTPUT_LIMIT_UNKNOWN', -signal.SIGXCPU: 'CPU_LIMIT_UNKNOWN',
              -signal.SIGKILL: 'KILLED_UNKNOWN'}.get(rc, 'PROCESS_FAILURE_UNKNOWN')
    if result['wall_timeout']:
        status = 'WALL_LIMIT_UNKNOWN'
    result.update(status=status, scope=enc['scope'], solver_calls=1,
                  variables=enc['variables'], clauses=enc['clauses'], proof_checked=False,
                  proof_bytes=(HERE / 'proof.lrat').stat().st_size if (HERE / 'proof.lrat').exists() else 0,
                  retained_internal_solver_state=False,
                  mathematical_conclusion='None until model acceptance or certificate and scope checks')
    save(HERE / 'result.json', result)
    print(json.dumps(result, indent=2), flush=True)

    if status == 'SAT_CANDIDATE':
        result['decode_process'] = bounded([sys.executable, str(HERE / 'encode.py'), 'decode'],
                                           HERE / 'decode.log', 5, 10, cpu)
        if result['decode_process']['exit_code'] != 0:
            result['status'] = 'SAT_MODEL_OR_DECODE_CHECK_FAILED'
        else:
            result['independent_bfs_process'] = bounded(
                [sys.executable, str(BFS), str(HERE / 'candidate.json')],
                HERE / 'independent_bfs.log', 5, 10, cpu)
            if result['independent_bfs_process']['exit_code'] != 0:
                result['status'] = 'SAT_INDEPENDENT_CHECK_FAILED'
            else:
                checked = json.loads((HERE / 'candidate.verification.json').read_text())
                result['independent_graph_check'] = checked
                valid = (checked['valid_target'] and checked['n'] == 61 and checked['edges'] == 244
                         and checked['degrees'] == [8] * 61 and checked['bad_pair_count'] == 0
                         and checked['diameter'] is not None and checked['diameter'] <= 2)
                result['status'] = 'VERIFIED_ORDER61_TARGET' if valid else 'SAT_FAILED_TARGET_CHECK'
        result['mathematical_conclusion'] = ('An explicit independently BFS-verified order61 graph was found'
            if result['status'] == 'VERIFIED_ORDER61_TARGET' else 'No accepted graph; retain the model and inspect actual checks')
    elif status == 'RAW_UNSAT':
        result['mathematical_conclusion'] = 'No exclusion yet: exact-input LRAT certificate verification is pending'
    else:
        result['mathematical_conclusion'] = 'UNKNOWN or process failure does not exclude the adjacent-double-defect branch'
    save(HERE / 'result.json', result)
    print(json.dumps(result, indent=2), flush=True)


def check(cpu):
    """A separate root-launched job, only for the actual saved RAW_UNSAT proof."""
    assert not (HERE / 'certificate_check.json').exists(), 'Preserve the previous certificate-check result'
    result = json.loads((HERE / 'result.json').read_text())
    assert result['status'] == 'RAW_UNSAT' and result['exit_code'] == 20
    assert os.access(CHECKER, os.X_OK) and (HERE / 'proof.lrat').stat().st_size > 0
    command = [str(CHECKER), '--no-trim', str(HERE / 'input.cnf'), str(HERE / 'proof.lrat')]
    checked = bounded(command, HERE / 'certificate_check.log', 50, 70, cpu)
    verified_line = any(line.strip() == 's VERIFIED' for line in (HERE / 'certificate_check.log').open())
    verified = checked['exit_code'] == 20 and not checked['wall_timeout'] and verified_line
    checked.update(verified=verified, scope='Exact saved input.cnf only; mathematical reduction review remains separate')
    save(HERE / 'certificate_check.json', checked)
    result.update(proof_checked=verified, certificate_check=checked,
                  status='CHECKED_UNSAT_TEMPLATE' if verified else 'RAW_UNSAT')
    result['mathematical_conclusion'] = (
        'The saved full61 template CNF is certified UNSAT; applying this to every adjacent-double-defect graph also requires the documented reduction and source review'
        if verified else 'No checked exclusion: certificate check did not verify')
    save(HERE / 'result.json', result)
    print(json.dumps(checked, indent=2), flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'solve', 'check'))
    parser.add_argument('--cpu', type=int, default=1)
    parser.add_argument('--solver-cpu', type=int, default=50)
    parser.add_argument('--solver-wall', type=int, default=70)
    args = parser.parse_args()
    if args.action == 'prepare':
        prepare(args.cpu)
    elif args.action == 'solve':
        solve(args.cpu, args.solver_cpu, args.solver_wall)
    else:
        check(args.cpu)
