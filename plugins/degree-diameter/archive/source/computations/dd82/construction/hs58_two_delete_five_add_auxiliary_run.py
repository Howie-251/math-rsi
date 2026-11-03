#!/usr/bin/env python3
"""Compile, then perform one complete H(8,10) screen with a 10-CPU-second cap."""
from pathlib import Path
import json
import os
import resource
import time

HERE=Path(__file__).resolve().parent
OUT=HERE/'hs58_two_delete_five_add_auxiliary_run'
OUT.mkdir(exist_ok=True)

def invoke(command, cpu_limits, memory):
    start=time.monotonic()
    pid=os.fork()
    if pid==0:
        if hasattr(os,'sched_getaffinity'):
            os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
        resource.setrlimit(resource.RLIMIT_CPU,cpu_limits)
        resource.setrlimit(resource.RLIMIT_AS,(memory,memory))
        os.execvp(command[0],command)
    _,status,usage=os.wait4(pid,0)
    return {'command':command,'cpu_limits_seconds':cpu_limits,'threads':1,
            'exit_code':os.waitstatus_to_exitcode(status),
            'user_cpu_seconds':usage.ru_utime,'system_cpu_seconds':usage.ru_stime,
            'total_cpu_seconds':usage.ru_utime+usage.ru_stime,
            'wall_seconds':time.monotonic()-start,'maximum_resident_kib':usage.ru_maxrss}

compile_report=invoke(['g++','-O3','-std=c++17',str(HERE/'hs58_two_delete_five_add_auxiliary.cpp'),
                       '-o',str(HERE/'hs58_two_delete_five_add_auxiliary.bin')],(30,31),2*1024**3)
(OUT/'compilation.json').write_text(json.dumps(compile_report,indent=2)+'\n')
if compile_report['exit_code']:
    raise SystemExit(compile_report['exit_code'])
report=invoke([str(HERE/'hs58_two_delete_five_add_auxiliary.bin'),str(OUT/'enumeration')],(10,11),1024**3)
report['internal_cpu_stop_seconds']=9.8
(OUT/'resources.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
if report['exit_code']:
    raise SystemExit(report['exit_code'])
