#!/usr/bin/env python3
"""The sole bounded general-bridge run; persist measured process resources."""
from pathlib import Path
import json
import os
import resource
import time

HERE = Path(__file__).resolve().parent
OUT = HERE/'d1_general_bridge_run'
command = [str(HERE/'d1_general_bridge_search.bin'), str(OUT/'inputs.txt'), str(OUT/'search')]
start = time.monotonic()
pid = os.fork()
if pid == 0:
    if hasattr(os, 'sched_getaffinity'):
        os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_CPU, (10, 11))
    resource.setrlimit(resource.RLIMIT_AS, (2*1024**3, 2*1024**3))
    os.execv(command[0], command)
_, status, usage = os.wait4(pid, 0)
report = {'command': command, 'internal_cpu_stop_seconds': 9.8,
          'cpu_limits_seconds': [10, 11], 'threads': 1,
          'exit_code': os.waitstatus_to_exitcode(status),
          'user_cpu_seconds': usage.ru_utime, 'system_cpu_seconds': usage.ru_stime,
          'total_cpu_seconds': usage.ru_utime+usage.ru_stime,
          'wall_seconds': time.monotonic()-start, 'maximum_resident_kib': usage.ru_maxrss}
(OUT/'resources.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
if report['exit_code']:
    raise SystemExit(report['exit_code'])
