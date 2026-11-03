"""Root-owned entry point. Compilation and native child share one CPU budget."""
from pathlib import Path
import argparse
import json
import resource
import subprocess
import time

OUT = Path(__file__).resolve().parent


def cpu():
    child = resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time() + child.ru_utime + child.ru_stime


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--onecoeff', nargs=4, type=int)
    args = parser.parse_args()
    start = cpu()
    prediction = json.loads((OUT / 'PREDICTION.json').read_text())
    assert prediction['frozen_before_experiment']
    subprocess.run(['g++', '-O3', '-std=c++17', '-DNDEBUG', str(OUT / 'scan.cpp'),
                    '-o', str(OUT / 'scan')], check=True)
    compile_cpu = cpu() - start
    remaining = 60.0 - compile_cpu - 0.75
    if remaining <= 0:
        result = {'status': 'COMPILE_BUDGET_UNKNOWN', 'complete_space': False,
                  'compile_CPU_seconds': compile_cpu, 'evaluated_candidates': 0}
        (OUT / 'terminal.json').write_text(json.dumps(result, indent=2) + '\n')
        return
    command = [str(OUT / 'scan'), '--out', str(OUT), '--budget', str(remaining)]
    if args.onecoeff:
        command += ['--onecoeff'] + [str(x) for x in args.onecoeff]
    result = subprocess.run(command, text=True, capture_output=True)
    (OUT / 'run.stdout').write_text(result.stdout)
    (OUT / 'run.stderr').write_text(result.stderr)
    timing = {'compile_CPU_seconds': compile_cpu, 'native_budget_CPU_seconds': remaining,
              'total_parent_and_child_CPU_seconds': cpu() - start, 'returncode': result.returncode}
    (OUT / 'run_timing.json').write_text(json.dumps(timing, indent=2) + '\n')
    print(result.stdout, end='')
    print(json.dumps(timing))
    result.check_returncode()


if __name__ == '__main__':
    main()
