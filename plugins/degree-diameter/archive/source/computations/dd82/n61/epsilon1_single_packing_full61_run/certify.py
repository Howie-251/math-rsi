"""One separately justified LRAT production and exact saved-input check."""
import argparse
import json
import os
from pathlib import Path
import signal
import runner

HERE = Path(__file__).resolve().parent
OUT = HERE / 'certification'


def save(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2) + '\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cpu', type=int, default=min(os.sched_getaffinity(0)))
    args = parser.parse_args()
    original = json.loads((HERE / 'result.json').read_text())
    assert original['status'] == 'RAW_UNSAT_UNCERTIFIED' and original['exit_code'] == 20
    OUT.mkdir(exist_ok=True)
    assert not any((OUT / name).exists() for name in ('launch.json', 'solver.log', 'proof.lrat', 'result.json'))

    def bounded(command, filename, cpu, wall):
        return runner.process.bounded(command, OUT / filename, cpu, wall, args.cpu, cap_files=True)

    command = [str(runner.process.SOLVER), '--lrat', '-t', '48',
               str(HERE / 'input.cnf'), str(OUT / 'proof.lrat')]
    save('launch.json', dict(command=command, source_input=str(HERE / 'input.cnf'),
        purpose='Separate certification of actual RAW UNSAT; unchanged saved CNF',
        certification_solver_calls=1, original_discovery_solver_calls=1, automatic_restarts=0,
        solver_cpu_budget_seconds=50, solver_wall_budget_seconds=70,
        checker_cpu_budget_seconds=30, checker_wall_budget_seconds=45,
        maximum_child_cpu_seconds=80, maximum_child_wall_seconds=115,
        threads=1, memory_limit_bytes=runner.process.MEMORY_BYTES,
        per_file_limit_bytes=runner.process.OUTPUT_BYTES, proof_logging=True))
    result = bounded(command, 'solver.log', 50, 70)
    status = {20: 'RAW_UNSAT_WITH_PROOF', 10: 'UNEXPECTED_SAT_REQUIRES_INVESTIGATION',
              0: 'CERTIFICATION_UNKNOWN', -signal.SIGXFSZ: 'OUTPUT_LIMIT_UNKNOWN',
              -signal.SIGXCPU: 'CPU_LIMIT_UNKNOWN', -signal.SIGKILL: 'KILLED_UNKNOWN'
              }.get(result['exit_code'], 'PROCESS_FAILURE_UNKNOWN')
    if result['wall_timeout']:
        status = 'WALL_LIMIT_UNKNOWN'
    result.update(status=status, source_input=str(HERE / 'input.cnf'), scope=original['scope'],
                  proof_checked=False, certification_solver_calls=1, original_discovery_solver_calls=1,
                  proof_bytes=(OUT / 'proof.lrat').stat().st_size if (OUT / 'proof.lrat').exists() else 0)
    save('result.json', result)
    print(json.dumps(result, indent=2), flush=True)
    if status == 'RAW_UNSAT_WITH_PROOF' and result['proof_bytes'] > 0:
        checked = bounded([str(runner.process.CHECKER), '--no-trim',
                           str(HERE / 'input.cnf'), str(OUT / 'proof.lrat')],
                          'certificate_check.log', 30, 45)
        verified_line = any(line.strip() == 's VERIFIED'
                            for line in (OUT / 'certificate_check.log').open())
        verified = checked['exit_code'] == 20 and not checked['wall_timeout'] and verified_line
        checked.update(verified=verified, scope='Exact unchanged epsilon1_single_packing_full61 input.cnf')
        save('certificate_check.json', checked)
        result.update(certificate_check=checked, proof_checked=verified,
                      status='CHECKED_UNSAT_CNF' if verified else 'RAW_UNSAT_CHECK_NOT_VERIFIED')
    result['mathematical_conclusion'] = (
        'Exact saved CNF certified UNSAT; epsilon=1 graph-to-CNF bridge separately documented and reviewed. Other order61 branches remain outside scope.'
        if result['proof_checked'] else 'No checked exclusion from this certification attempt.')
    save('result.json', result)
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
