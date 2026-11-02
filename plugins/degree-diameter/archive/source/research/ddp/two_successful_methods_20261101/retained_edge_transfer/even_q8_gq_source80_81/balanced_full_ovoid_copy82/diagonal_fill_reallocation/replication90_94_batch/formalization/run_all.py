from pathlib import Path
import json,os,subprocess,sys
D=Path(__file__).resolve().parent
for mod in json.loads((D/'PREPARATION_RESULT.json').read_text())['modules']:
    checkpoint=json.loads((D/'CHECKPOINT.json').read_text())if(D/'CHECKPOINT.json').exists()else{}
    if mod in checkpoint.get('completed',[]):continue
    print('COMPILING '+mod,flush=True)
    result=subprocess.run([sys.executable,str(D/'compile.py'),mod])
    if result.returncode:raise SystemExit(result.returncode)
checkpoint=json.loads((D/'CHECKPOINT.json').read_text())
print(json.dumps(dict(status='ALL_EIGHT_NEW_MODULES_KERNEL_PASS_EXTERNAL_BINDING_PENDING',
    CPU_seconds=checkpoint['CPU_seconds'],completed=checkpoint['completed'])),flush=True)
