"""One worker; stop on first failure, preserving every receipt."""
import json
import subprocess
import sys
import time
from pathlib import Path

D = Path(__file__).resolve().parent
start = time.monotonic()
modules = ['OppositeGQ77SpreadIncidenceData']
modules += [f'OppositeGQ77SpreadIncidenceChunk{k}' for k in range(8)]
modules += ['OppositeGQ77SpreadIncidence', 'OppositeGQ77SpreadInputInterface']
modules += ['OppositeGQ77SpreadInputRow000', 'OppositeGQ77SpreadInputRow399']

def cpu():
    paths = list(D.glob('*_RESULT.json')) + list((D / 'build_history').glob('*_RESULT.json'))
    return sum(json.loads(p.read_text()).get('CPU_seconds', 0) for p in paths
               if 'module' in json.loads(p.read_text()))

state = {'status': 'RUNNING', 'workers': 1, 'modules': modules,
         'prep_CPU_budget': 600, 'probe_rows_each_CPU_limit': 115,
         'completed': [], 'failure': None}
for mod in modules:
    receipt = D / f'{mod}_RESULT.json'
    if receipt.exists() and json.loads(receipt.read_text())['exit_code'] == 0:
        state['completed'].append(mod)
        continue
    # Reserve a full 115 CPU allocation; probes are separately measured.
    if cpu() + 115 > (830 if 'InputRow' in mod else 600):
        state['status'] = 'STOP_PHASE_BUDGET'
        break
    state['current_module'] = mod
    state['all_CPU'] = cpu()
    (D / 'PREPARATION_HANDLE.json').write_text(json.dumps(state, indent=2)+'\n')
    with (D / f'{mod}_driver.log').open('w') as log:
        subprocess.run([sys.executable, str(D / 'compile.py'), mod, '115'], stdout=log, stderr=log)
    result = json.loads(receipt.read_text())
    print(json.dumps(result), flush=True)
    if result['exit_code'] != 0:
        state['failure'] = result
        state['status'] = 'STOP_MODULE_FAILURE'
        break
    state['completed'].append(mod)
else:
    state['status'] = 'COMPLETE_PREPARATION_AND_TWO_PROBES'
state['all_CPU'] = cpu()
state['elapsed_wall'] = time.monotonic()-start
(D / 'PREPARATION_RESULT.json').write_text(json.dumps(state, indent=2)+'\n')
(D / 'PREPARATION_HANDLE.json').write_text(json.dumps(state, indent=2)+'\n')
print(json.dumps(state), flush=True)
