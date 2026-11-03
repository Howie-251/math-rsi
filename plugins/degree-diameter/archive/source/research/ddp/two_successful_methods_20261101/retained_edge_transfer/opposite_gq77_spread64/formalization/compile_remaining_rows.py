"""Run only after the first and last actual rows pass their bounded probes."""
import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

D = Path(__file__).resolve().parent
start = time.monotonic()
ticks = os.sysconf('SC_CLK_TCK')
def atomic_json(path,value):
    tmp=path.with_name(path.name+f'.{os.getpid()}.tmp')
    tmp.write_text(json.dumps(value,indent=2)+'\n')
    tmp.replace(path)

def all_cpu():
    paths = list(D.glob('*_RESULT.json')) + list((D/'build_history').glob('*_RESULT.json'))
    total = 0
    for p in paths:
        x = json.loads(p.read_text())
        if 'module' in x:
            total += x.get('CPU_seconds', 0)
    return total

probes = [json.loads((D/f'OppositeGQ77SpreadInputRow{i:03}_RESULT.json').read_text()) for i in [0,399]]
assert all(p['exit_code'] == 0 and p['CPU_seconds'] < 115 for p in probes)
base = all_cpu()
rows = list(range(1,399))
passed = [i for i in rows if (p:=D/f'OppositeGQ77SpreadInputRow{i:03}_RESULT.json').exists()
          and json.loads(p.read_text())['exit_code']==0]
todo = [i for i in rows if i not in passed]
estimate = base + len(todo)*max(p['CPU_seconds'] for p in probes)*1.5 + 200
assert estimate < 15000, ('probe extrapolation exceeds authorized budget', estimate)
state = {'status':'RUNNING', 'driver_pid':os.getpid(), 'workers':8,
         'expected_rows':rows, 'completed':passed.copy(), 'already_PASS_rows_at_start':passed.copy(),
         'new_rows_to_dispatch_at_start':todo.copy(), 'per_module_CPU_limit':115,
         'total_CPU_limit_including_all_attempts':15000, 'assembly_reserve':200,
         'all_prior_CPU':base, 'probe_results':probes,
         'conservative_probe_extrapolation_CPU':estimate,
         'stop_conditions':['first failure stops dispatch',
                            '14800 completed plus active CPU stops and terminates active workers',
                            'no unchanged PASS module is recompiled', 'no automatic restart']}
active = {}
stop = False

def snapshot():
    running = []
    used = 0
    for i,p in active.items():
        pid = None
        h = D/f'OppositeGQ77SpreadInputRow{i:03}_HANDLE.json'
        if h.exists():
            r = json.loads(h.read_text())
            pid = r.get('pid') if r.get('status') == 'RUNNING' else None
        if pid:
            try:
                fields = Path(f'/proc/{pid}/stat').read_text().split()
                used += (int(fields[13])+int(fields[14]))/ticks
            except FileNotFoundError:
                pass
        running.append({'row':i, 'wrapper_pid':p.pid, 'compiler_pid':pid})
    state.update(active=running, completed_attempts_CPU=all_cpu(), active_CPU=used,
                 elapsed_wall=time.monotonic()-start)
    atomic_json(D/'INPUT_BATCH_HANDLE.json',state)
    return state['completed_attempts_CPU']+used

while todo or active:
    while todo and len(active) < 8 and not stop:
        if all_cpu()+115*(len(active)+1) > 14800:
            stop = True
            state['status'] = 'STOP_ALLOCATION_BUDGET'
            break
        i = todo.pop(0)
        mod = f'OppositeGQ77SpreadInputRow{i:03}'
        receipt = D/f'{mod}_RESULT.json'
        if receipt.exists() and json.loads(receipt.read_text())['exit_code'] == 0:
            state['completed'].append(i)
            continue
        with (D/f'{mod}_driver.log').open('w') as log:
            active[i] = subprocess.Popen([sys.executable,str(D/'compile.py'),mod,'115'],stdout=log,stderr=log)
    for i,p in list(active.items()):
        if p.poll() is None:
            continue
        r = json.loads((D/f'OppositeGQ77SpreadInputRow{i:03}_RESULT.json').read_text())
        if r['exit_code'] == 0:
            state['completed'].append(i)
        else:
            state['failure'] = r
            state['status'] = 'STOP_MODULE_FAILURE'
            stop = True
        del active[i]
        if len(state['completed']) % 25 == 0:
            print(json.dumps({'completed':len(state['completed']), 'all_CPU':all_cpu()}), flush=True)
    if snapshot() >= 14800 and not stop:
        stop = True
        state['status'] = 'STOP_AGGREGATE_CPU_LIMIT'
        for x in state['active']:
            if x['compiler_pid']:
                os.kill(x['compiler_pid'],signal.SIGTERM)
    if stop and not active:
        break
    time.sleep(.5)
if not stop:
    state['status'] = 'COMPLETE_ALL398_REMAINING_ROWS'
state.update(unstarted_rows=todo, all_attempts_CPU=all_cpu(), elapsed_wall=time.monotonic()-start)
atomic_json(D/'INPUT_BATCH_RESULT.json',state)
atomic_json(D/'INPUT_BATCH_HANDLE.json',state)
print(json.dumps({k:v for k,v in state.items() if k not in ['expected_rows','completed','already_PASS_rows_at_start','new_rows_to_dispatch_at_start']},indent=2),flush=True)
