#!/usr/bin/env python3
"""Run the one bounded mixed-copy experiment and always save its terminal."""
import json
import os
from pathlib import Path
import resource
import subprocess
import sys
import time

base = Path(__file__).resolve().parent
assert not (base/'MILP_TERMINAL.json').exists(), 'This one-shot budget was already used.'
assert (base/'G0_INPUT.npz').exists(), 'Wait for the actual base preparation.'
started = time.monotonic()
before = resource.getrusage(resource.RUSAGE_CHILDREN)
with (base/'milp_once.log').open('w') as log:
    child = subprocess.Popen([sys.executable,str(base/'solver_once.py')],
        stdout=log,stderr=subprocess.STDOUT,cwd=base)
    (base/'MILP_HANDLE.json').write_text(json.dumps({'status':'RUNNING',
        'supervisor_pid':os.getpid(),'child_pid':child.pid,
        'total_CPU_budget_seconds':120,'solver_time_limit_seconds':90,
        'single_worker':True,'start_UTC':time.strftime('%Y-%m-%d %H:%M:%S UTC',time.gmtime()),
        'no_timer_restart':True},indent=2)+'\n')
    code = child.wait()
after = resource.getrusage(resource.RUSAGE_CHILDREN)
used = after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
p = base/'SCIPY_MILP_RESULT.json'
result = json.loads(p.read_text()) if p.exists() else {}
terminal = {'status':result.get('status','UNKNOWN_CHILD_TERMINATED_WITHOUT_FEASIBLE_PINS'),
    'exit_code':code,'child_CPU_seconds':used,'wall_seconds':time.monotonic()-started,
    'total_CPU_budget_seconds':120,'solver_time_limit_seconds':90,
    'all_processes_terminal':True,'single_worker':True,'one_milp_attempt':True,
    'feasible_pins_saved':result.get('feasible_integer_pins_saved',False),
    'strict_infeasibility_proof_claimed':False,'portfolio_parameter_Lean_increment':[0,0,0],
    'source_BFS_field_old_Lean_paid_review_runs':0,'automatic_next_pattern':False}
(base/'MILP_TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
(base/'MILP_HANDLE.json').write_text(json.dumps({'status':'TERMINAL',
    'supervisor_pid':os.getpid(),'child_pid':child.pid,'running':False,
    'terminal':'MILP_TERMINAL.json','exit_code':code},indent=2)+'\n')
print(json.dumps(terminal))
