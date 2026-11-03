#!/usr/bin/env python3
import json
import os
from pathlib import Path
import resource
import subprocess
import sys
import time
base=Path(__file__).resolve().parent
assert not (base/'COLOR_TERMINAL.json').exists(),'One batch already used.'
assert (base/'G0_INPUT.npz').exists(),'Wait for actual base preparation.'
before=resource.getrusage(resource.RUSAGE_CHILDREN);started=time.monotonic()
with (base/'color_once.log').open('w') as log:
    child=subprocess.Popen([sys.executable,str(base/'color_once.py')],stdout=log,stderr=subprocess.STDOUT,cwd=base)
    (base/'COLOR_HANDLE.json').write_text(json.dumps({'status':'RUNNING','supervisor_pid':os.getpid(),
        'child_pid':child.pid,'total_CPU_budget':60,'solver_time_limit':45,
        'workers':1,'no_seed_timer_pattern_restart':True},indent=2)+'\n')
    code=child.wait()
after=resource.getrusage(resource.RUSAGE_CHILDREN)
used=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
p=base/'COLOR_RESULT.json';r=json.loads(p.read_text()) if p.exists() else {}
terminal={'status':r.get('status','UNKNOWN_CHILD_ENDED_WITHOUT_INTEGER_PINS'),'exit_code':code,
    'child_CPU_seconds':used,'wall_seconds':time.monotonic()-started,'total_CPU_budget':60,
    'solver_time_limit':45,'all_processes_terminal':True,'workers':1,
    'integer_pins_saved':r.get('integer_pins_saved',False),'new_graph_accepted':False,
    'no_seed_timer_pattern_restart':True,'portfolio_parameter_Lean_increment':[0,0,0]}
(base/'COLOR_TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
(base/'COLOR_HANDLE.json').write_text(json.dumps({'status':'TERMINAL','running':False,
    'child_pid':child.pid,'exit_code':code,'terminal':'COLOR_TERMINAL.json'},indent=2)+'\n')
print(json.dumps(terminal))
