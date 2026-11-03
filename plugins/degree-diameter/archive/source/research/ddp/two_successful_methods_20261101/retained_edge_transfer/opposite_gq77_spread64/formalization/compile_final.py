import json
import subprocess
import sys
from pathlib import Path

D = Path(__file__).resolve().parent
for i in range(400):
    r = json.loads((D/f'OppositeGQ77SpreadInputRow{i:03}_RESULT.json').read_text())
    assert r['exit_code'] == 0, (i,r)

def cpu():
    paths = list(D.glob('*_RESULT.json'))+list((D/'build_history').glob('*_RESULT.json'))
    return sum(x['CPU_seconds'] for p in paths if 'module' in (x:=json.loads(p.read_text())))

for mod in ['OppositeGQ77SpreadInputs','OppositeGQ77SpreadExact','OppositeGQ77SpreadAudit']:
    old = D/f'{mod}_RESULT.json'
    if old.exists() and json.loads(old.read_text())['exit_code'] == 0:
        continue
    assert cpu()+115 <= 15000, cpu()
    with (D/f'{mod}_driver.log').open('w') as log:
        subprocess.run([sys.executable,str(D/'compile.py'),mod,'115'],stdout=log,stderr=log)
    r = json.loads(old.read_text())
    print(json.dumps(r),flush=True)
    if r['exit_code'] != 0:
        sys.exit(1)
print(json.dumps({'status':'FINAL_ASSEMBLY_EXACT_AND_SEPARATE_IMPORT_AUDIT_PASS','all_CPU':cpu()}),flush=True)
