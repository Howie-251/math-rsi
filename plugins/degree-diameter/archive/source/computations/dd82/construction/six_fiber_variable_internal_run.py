#!/usr/bin/env python3
"""One ten-CPU-second quotient enumeration; no graph/SAT search."""
from pathlib import Path
import json, os, resource, time

HERE = Path(__file__).resolve().parent
OUT = HERE / 'six_fiber_variable_internal_run'

def main():
    OUT.mkdir(exist_ok=True)
    assert not (OUT / 'search.json').exists(), 'Do not repeat an unchanged enumeration'
    command = [str(HERE / 'six_fiber_variable_internal_search.bin'), str(OUT / 'search')]
    started = time.monotonic()
    cpu = min(os.sched_getaffinity(0))
    pid = os.fork()
    if pid == 0:
        os.sched_setaffinity(0, {cpu})
        resource.setrlimit(resource.RLIMIT_CPU, (11, 12))
        resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
        os.execv(command[0], command)
    _, status, usage = os.wait4(pid, 0)
    report = {
        'command': command, 'internal_cpu_cap_seconds': 10,
        'hard_cpu_limits_seconds': [11, 12], 'threads': 1,
        'pinned_cpu': cpu, 'address_space_limit_bytes': 1024**3,
        'exit_code': os.waitstatus_to_exitcode(status),
        'user_cpu_seconds': usage.ru_utime, 'system_cpu_seconds': usage.ru_stime,
        'total_cpu_seconds': usage.ru_utime + usage.ru_stime,
        'wall_seconds': time.monotonic() - started,
        'maximum_resident_kib': usage.ru_maxrss,
    }
    (OUT / 'resources.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
    if report['exit_code'] != 0:
        raise SystemExit(report['exit_code'])

if __name__ == '__main__':
    main()
