import json
import os
from pathlib import Path
import resource
import subprocess
import sys
import time

ROOT = Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math')
FORMAL = ROOT / 'formal'
OUT = Path(__file__).resolve().parent
MODULE = 'DegreeDiameter.Portfolio.OppositeGQ35SpreadLowerGeneric'
SOURCE = 'DegreeDiameter/Portfolio/OppositeGQ35SpreadLowerGeneric.lean'
OUTPUT = '.lake/build/lib/lean/DegreeDiameter/Portfolio/OppositeGQ35SpreadLowerGeneric.olean'
attempt = int(sys.argv[1]) if len(sys.argv) > 1 else 1
base = json.loads((ROOT / 'research/ddp/refresh_20261029/f5_full_d20_D3/FORMAL_ENV_COMMAND.json').read_text())
env = dict(os.environ)
env['LEAN_PATH'] = base['LEAN_PATH']
env['LEAN_NUM_THREADS'] = '1'
command = [str(ROOT / '.tools/lean-4.24.0-linux/bin/lean'), '-j1', '-o', OUTPUT, SOURCE]
log_path = OUT / f'attempt_{attempt:02d}.log'
started = time.monotonic()

def limits():
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))

with log_path.open('w') as log:
    result = subprocess.run(command, cwd=FORMAL, env=env, stdout=log, stderr=log, preexec_fn=limits)
usage = resource.getrusage(resource.RUSAGE_CHILDREN)
receipt = dict(module=MODULE, source=str(FORMAL / SOURCE), command=command,
               cwd=str(FORMAL), LEAN_PATH=env['LEAN_PATH'], LEAN_NUM_THREADS='1',
               exit_code=result.returncode, CPU_seconds=usage.ru_utime + usage.ru_stime,
               wall_seconds=time.monotonic() - started, CPU_budget_seconds=60,
               log=str(log_path), attempt=attempt, concrete_graph_claim=False)
(OUT / f'attempt_{attempt:02d}.json').write_text(json.dumps(receipt, indent=2) + '\n')
(OUT / 'COMPILE_RESULT.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt))
print(log_path.read_text())
raise SystemExit(result.returncode)
