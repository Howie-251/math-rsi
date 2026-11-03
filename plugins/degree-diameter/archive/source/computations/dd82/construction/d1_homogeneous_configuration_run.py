#!/usr/bin/env python3
"""Run the homogeneous-family search once, with a 10-second internal CPU cap."""
from pathlib import Path
import json, os, resource, time

HERE = Path(__file__).resolve().parent
OUT = HERE / 'd1_homogeneous_configuration_run'

def main():
    OUT.mkdir(exist_ok=True)
    command = [str(HERE / 'd1_homogeneous_configuration_search.bin'),
               str(OUT / 'inputs.txt'), str(OUT / 'search')]
    start = time.monotonic()
    pid = os.fork()
    if pid == 0:
        resource.setrlimit(resource.RLIMIT_CPU, (11, 12))
        resource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))
        os.execv(command[0], command)
    _, status, usage = os.wait4(pid, 0)
    report = {
        'command': command, 'internal_cpu_cap_seconds': 10,
        'hard_cpu_limits_seconds': [11, 12], 'threads': 1,
        'address_space_limit_bytes': 4 * 1024**3,
        'exit_code': os.waitstatus_to_exitcode(status),
        'user_cpu_seconds': usage.ru_utime, 'system_cpu_seconds': usage.ru_stime,
        'total_cpu_seconds': usage.ru_utime + usage.ru_stime,
        'wall_seconds': time.monotonic() - start,
        'maximum_resident_kib': usage.ru_maxrss,
    }
    (OUT / 'resources.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))
    if report['exit_code'] != 0:
        raise SystemExit(report['exit_code'])

if __name__ == '__main__':
    main()
