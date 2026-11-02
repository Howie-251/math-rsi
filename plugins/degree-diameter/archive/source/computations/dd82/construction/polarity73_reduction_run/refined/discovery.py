"""Prepare or run one bounded no-proof refined-screen discovery profile."""
import argparse
import importlib.util
import json
from pathlib import Path
import signal
import sys

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('saved_polarity_runner', HERE.parent / 'runner.py')
parent = importlib.util.module_from_spec(spec)
spec.loader.exec_module(parent)
process, save = parent.process, parent.save


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'solve'))
    parser.add_argument('--n', type=int, choices=(58, 59), required=True)
    parser.add_argument('--cpu', type=int, required=True)
    args = parser.parse_args()
    out = HERE / f'n{args.n}'
    out.mkdir(exist_ok=True)

    def bounded(command, log, cpu, wall):
        return process.bounded(command, out / log, cpu, wall, args.cpu, cap_files=True)

    if args.action == 'prepare':
        assert not (out / 'preparation_process.json').exists()
        result = bounded([sys.executable, str(HERE / 'screen.py'), 'prepare', '--n', str(args.n)],
                         'prepare.log', 20, 30)
        result.update(status='PREPARED_NOT_RUN' if result['exit_code'] == 0 else 'PREPARATION_FAILED',
                      solver_calls=0)
        save(out / 'preparation_process.json', result)
    else:
        assert not any((out / name).exists() for name in ('launch.json', 'solver.log', 'result.json'))
        encoding = json.loads((out / 'encoding.json').read_text())
        assert encoding['status'] == 'PREPARED_NOT_RUN' and encoding['n'] == args.n
        command = [str(process.SOLVER), '-t', '28', str(out / 'input.cnf')]
        save(out / 'launch.json', dict(status='LAUNCHED', purpose='candidate_discovery',
             command=command, scope=encoding['scope'], cpu_affinity=[args.cpu],
             proof_logging=False, solver_calls=1, automatic_restarts=0,
             solver_cpu_limit_seconds=30, solver_wall_limit_seconds=45,
             memory_limit_bytes=process.MEMORY_BYTES, per_file_limit_bytes=process.OUTPUT_BYTES))
        result = bounded(command, 'solver.log', 30, 45)
        status = {10: 'SAT_PENDING_DECODE', 20: 'RAW_UNSAT_UNCERTIFIED', 0: 'UNKNOWN',
                  -signal.SIGXFSZ: 'OUTPUT_LIMIT_UNKNOWN', -signal.SIGXCPU: 'CPU_LIMIT_UNKNOWN',
                  -signal.SIGKILL: 'KILLED_UNKNOWN'}.get(result['exit_code'], 'PROCESS_FAILURE_UNKNOWN')
        if result['wall_timeout']:
            status = 'WALL_LIMIT_UNKNOWN'
        result.update(status=status, n=args.n, scope=encoding['scope'],
                      variables=encoding['variables'], clauses=encoding['clauses'],
                      solver_calls=1, proof_logging=False, proof_checked=False,
                      complete_graph_constructed=False, purpose='candidate_discovery')
        save(out / 'result.json', result)
        if status == 'SAT_PENDING_DECODE':
            decoded = bounded([sys.executable, str(HERE / 'screen.py'), 'decode', '--n', str(args.n)],
                              'decode.log', 15, 20)
            result['decode_process'] = decoded
            result['status'] = ('REFINED_SCREEN_SAT_CHECKED' if decoded['exit_code'] == 0
                                else 'SAT_DECODE_CHECK_FAILED')
        result['mathematical_conclusion'] = (
            'Necessary screen model only; saved deletion set needs complete graph completion.'
            if result['status'] == 'REFINED_SCREEN_SAT_CHECKED' else
            'No accepted target or certified exclusion; preserve exact result and scope.')
        save(out / 'result.json', result)
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
