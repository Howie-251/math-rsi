"""One exact completion of the saved seed3 F5, never an automatic prefix ladder."""
import argparse
import importlib.util
import json
from pathlib import Path
import signal
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
spec = importlib.util.spec_from_file_location('joint_tail_bounded_process',
    ROOT / 'computations/dd82/n61/adjacent_double_full61_run/runner.py')
process = importlib.util.module_from_spec(spec)
spec.loader.exec_module(process)


def save(path, data):
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(data, indent=2) + '\n')
    tmp.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'solve'))
    parser.add_argument('--cpu', type=int, default=1)
    args = parser.parse_args()

    def bounded(command, log, cpu, wall):
        return process.bounded(command, HERE / log, cpu, wall, args.cpu, cap_files=True)

    if args.action == 'prepare':
        assert not (HERE / 'preparation_process.json').exists()
        result = bounded([sys.executable, str(HERE / 'encode.py'), 'prepare'], 'prepare.log', 20, 30)
        result['status'] = 'PREPARED_NOT_RUN' if result['exit_code'] == 0 else 'PREPARATION_FAILED'
        save(HERE / 'preparation_process.json', result)
    else:
        assert not any((HERE / name).exists() for name in ('launch.json', 'solver.log', 'result.json'))
        encoding = json.loads((HERE / 'encoding.json').read_text())
        assert encoding['status'] == 'PREPARED_NOT_RUN'
        command = [str(process.SOLVER), '-t', '28', str(HERE / 'input.cnf')]
        save(HERE / 'launch.json', dict(command=command, scope=encoding['scope'],
             seed=3, fixed_prefix_rounds=5, solver_calls=1, automatic_restarts=0,
             proof_logging=False, cpu_budget_seconds=30, wall_budget_seconds=45,
             cpu_affinity=[args.cpu], memory_limit_bytes=process.MEMORY_BYTES,
             per_file_limit_bytes=process.OUTPUT_BYTES))
        result = bounded(command, 'solver.log', 30, 45)
        status = {10: 'SAT_PENDING_DECODE', 20: 'RAW_UNSAT_UNCERTIFIED', 0: 'UNKNOWN',
                  -signal.SIGXFSZ: 'OUTPUT_LIMIT_UNKNOWN', -signal.SIGXCPU: 'CPU_LIMIT_UNKNOWN',
                  -signal.SIGKILL: 'KILLED_UNKNOWN'}.get(result['exit_code'], 'PROCESS_FAILURE_UNKNOWN')
        if result['wall_timeout']:
            status = 'WALL_LIMIT_UNKNOWN'
        result.update(status=status, seed=3, fixed_prefix_rounds=5, n=58,
                      scope=encoding['scope'], variables=encoding['variables'],
                      clauses=encoding['clauses'], solver_calls=1, proof_logging=False,
                      proof_checked=False, target_graph_verified=False)
        save(HERE / 'result.json', result)
        if status == 'SAT_PENDING_DECODE':
            decoded = bounded([sys.executable, str(HERE / 'encode.py'), 'decode'], 'decode.log', 10, 15)
            result['decode_process'] = decoded
            result['status'] = 'SAT_PENDING_INDEPENDENT_BFS' if decoded['exit_code'] == 0 else 'SAT_DECODE_FAILED'
            if decoded['exit_code'] == 0:
                checked = bounded([sys.executable,
                    str(ROOT / 'computations/dd82/construction/verify_hs_candidate.py'),
                    str(HERE / 'candidate.json')], 'independent_bfs.log', 10, 15)
                result['independent_bfs_process'] = checked
                if checked['exit_code'] == 0:
                    graph = json.loads((HERE / 'candidate.verification.json').read_text())
                    result['independent_graph_check'] = graph
                    valid = (graph['valid_target'] and graph['n'] == 58 and graph['edges'] == 232
                             and graph['degrees'] == [8] * 58 and graph['bad_pair_count'] == 0)
                    result['target_graph_verified'] = valid
                    result['status'] = 'VERIFIED_TARGET_GRAPH' if valid else 'SAT_GRAPH_CHECK_FAILED'
                else:
                    result['status'] = 'SAT_CHECK_PROCESS_FAILED'
        result['mathematical_conclusion'] = (
            'Explicit target independently BFS verified; formal final acceptance remains.'
            if result['target_graph_verified'] else
            'No accepted target or certified fixed-prefix exclusion from this profile.')
        save(HERE / 'result.json', result)
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
