"""Bounded semantics/preparation or the single epsilon=0 full61 discovery call."""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import signal
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('full61_resource_limits',
    HERE.parent/'adjacent_double_full61_run'/'runner.py')
process = importlib.util.module_from_spec(spec)
spec.loader.exec_module(process)


def save(name, value):
    (HERE/name).write_text(json.dumps(value, indent=2)+'\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('sanity', 'prepare', 'solve'))
    parser.add_argument('--cpu', type=int, default=min(os.sched_getaffinity(0)))
    args = parser.parse_args()

    def bounded(command, logfile, cpu=30, wall=45):
        return process.bounded(command, HERE/logfile, cpu, wall, args.cpu, cap_files=True)

    if args.action in ('sanity', 'prepare'):
        target = 'sanity.py' if args.action == 'sanity' else 'encode.py'
        command = [sys.executable, '-B', str(HERE/target)]
        if args.action == 'prepare':
            assert not (HERE/'preparation_process.json').exists()
            assert json.loads((HERE/'sanity.json').read_text())['status'] == 'PASSED'
            command.append('prepare')
        result = bounded(command, args.action+'.log')
        result.update(status='PASSED' if result['exit_code'] == 0 else 'FAILED', solver_calls=0)
        save('sanity_process.json' if args.action == 'sanity' else 'preparation_process.json', result)
    else:
        assert not any((HERE/name).exists() for name in ('launch.json', 'solver.log', 'result.json'))
        assert json.loads((HERE/'sanity.json').read_text())['status'] == 'PASSED'
        enc = json.loads((HERE/'encoding.json').read_text())
        assert enc['status'] == 'PREPARED_NOT_RUN' and enc['covered_original_pairs'] == 1830
        command = [str(process.SOLVER), '-t', '88', str(HERE/'input.cnf')]
        save('launch.json', dict(command=command, scope=enc['scope'], solver_calls=1,
             automatic_restarts=0, proof_logging=False, solver_soft_wall_seconds=88,
             cpu_budget_seconds=90, wall_budget_seconds=120, threads=1,
             memory_limit_bytes=process.MEMORY_BYTES, output_limit_bytes=process.OUTPUT_BYTES))
        result = bounded(command, 'solver.log', 90, 120)
        status = {10: 'SAT_PENDING_DECODE', 20: 'RAW_UNSAT_UNCERTIFIED', 0: 'UNKNOWN',
                  -signal.SIGXCPU: 'CPU_LIMIT_UNKNOWN', -signal.SIGXFSZ: 'OUTPUT_LIMIT_UNKNOWN',
                  -signal.SIGKILL: 'KILLED_UNKNOWN'}.get(result['exit_code'], 'PROCESS_FAILURE_UNKNOWN')
        if result['wall_timeout']:
            status = 'WALL_LIMIT_UNKNOWN'
        result.update(status=status, variables=enc['variables'], clauses=enc['clauses'],
                      scope=enc['scope'], proof_logging=False, proof_checked=False,
                      solver_calls=1, target61_verified=False, epsilon1_excluded=False)
        save('result.json', result)
        if status == 'SAT_PENDING_DECODE':
            result['decode'] = bounded([sys.executable, '-B', str(HERE/'encode.py'), 'decode'], 'decode.log')
            if result['decode']['exit_code'] == 0:
                result['independent_check'] = bounded([sys.executable, '-B', str(HERE/'check.py')], 'check.log')
                if result['independent_check']['exit_code'] == 0:
                    checked = json.loads((HERE/'candidate_check.json').read_text())
                    result['target61_verified'] = checked['target61_verified']
                result['status'] = 'VERIFIED_ORDER61_TARGET' if result['target61_verified'] else 'CANDIDATE_CHECK_FAILED'
            else:
                result['status'] = 'MODEL_DECODE_FAILED'
        result['mathematical_conclusion'] = (
            'Actual61 graph independently checked by BFS and complete model obligations'
            if result['target61_verified'] else
            'No accepted graph or certified exclusion; epsilon=1 remains outside this input')
        save('result.json', result)
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
