"""Compile and run the specifically requested small semantics; no production."""
import json
from pathlib import Path
import resource
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent


def measured(command, stdout_path, stderr_path):
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    start = time.monotonic()
    with stdout_path.open('w') as stdout, stderr_path.open('w') as stderr:
        result = subprocess.run(command, cwd=ROOT, stdout=stdout, stderr=stderr, check=True)
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    return dict(command=command, exit_code=result.returncode,
                child_cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
                wall_seconds=time.monotonic()-start)


def main():
    steps = []
    steps.append(measured(['g++', '-std=c++17', '-O3', '-Wall', '-Wextra', 'enumerate.cpp', '-o', 'enumerate'],
                          ROOT/'compile.stdout', ROOT/'compile.stderr'))
    steps.append(measured([str(ROOT/'enumerate'), '--sanity'], ROOT/'sanity_cpp.json', ROOT/'sanity_cpp.stderr'))
    steps.append(measured([sys.executable, str(ROOT/'check.py'), 'sanity'], ROOT/'sanity_check.json', ROOT/'sanity_check.stderr'))
    record = dict(status='PASS', production_executed=False, steps=steps)
    (ROOT/'preparation_timing.json').write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps(record, indent=2))


if __name__ == '__main__':
    main()
