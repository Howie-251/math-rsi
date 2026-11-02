import json,subprocess,sys
from pathlib import Path
D=Path(__file__).resolve().parent
mods=['OppositeGQ44SpreadInputInterface','OppositeGQ44SpreadInputRow00','OppositeGQ44SpreadInputRow84'];out=[]
for m in mods:
 p=subprocess.run([sys.executable,str(D/'compile.py'),m,'115'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
 r=json.loads((D/f'{m}_RESULT.json').read_text());print(json.dumps(r),flush=True);out.append(r)
 if r['exit_code']!=0:print(p.stdout,flush=True);raise SystemExit(1)
(D/'FIRST_LAST_ROW_MEASUREMENT.json').write_text(json.dumps({'status':'PASS','receipts':out,'remaining_batch_started':False},indent=2)+'\n')
