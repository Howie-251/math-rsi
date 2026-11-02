"""Prepare or run one bounded no-proof complete variable-deletion graph profile."""
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
        result = bounded([sys.executable, str(HERE / 'encode.py'), 'prepare', '--n', str(args.n)],
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
            decoded = bounded([sys.executable, str(HERE / 'encode.py'), 'decode', '--n', str(args.n)],
                              'decode.log', 15, 20)
            result['decode_process'] = decoded
            result['status'] = ('SAT_PENDING_INDEPENDENT_GRAPH_CHECK' if decoded['exit_code'] == 0
                                else 'SAT_DECODE_CHECK_FAILED')
            if decoded['exit_code'] == 0:
                check = bounded([sys.executable, str(parent.ROOT / 'computations/dd82/construction/verify_hs_candidate.py'),
                                 str(out / 'candidate.json')], 'independent_bfs.log', 10, 15)
                result['independent_bfs_process'] = check
                if check['exit_code'] == 0:
                    verified = json.loads((out / 'candidate.verification.json').read_text())
                    result['independent_graph_check'] = verified
                    valid = (verified['valid_target'] and verified['n'] == args.n
                             and verified['edges'] == 4 * args.n
                             and verified['degrees'] == [8] * args.n
                             and verified['bad_pair_count'] == 0)
                    result['status'] = 'VERIFIED_TARGET_GRAPH' if valid else 'SAT_GRAPH_CHECK_FAILED'
                    result['complete_graph_constructed'] = valid
                else:
                    result['status'] = 'SAT_GRAPH_CHECK_PROCESS_FAILED' 
        result['mathematical_conclusion'] = (
            'Explicit target graph independently verified from its saved edge list; formal acceptance remains.'
            if result['status'] == 'VERIFIED_TARGET_GRAPH' else
            'No accepted target or certified exclusion; preserve exact result and scope.')
        save(out / 'result.json', result)
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
