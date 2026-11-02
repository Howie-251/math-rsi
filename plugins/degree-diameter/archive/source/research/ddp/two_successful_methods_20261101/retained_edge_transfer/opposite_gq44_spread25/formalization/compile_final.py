import json,subprocess,sys
from pathlib import Path
D=Path(__file__).resolve().parent
b=json.loads((D/'INPUT_BATCH_RESULT.json').read_text());assert b['status']=='COMPLETE_ALL83_REMAINING_ROWS',b['status']
for i in range(85):assert json.loads((D/f'OppositeGQ44SpreadInputRow{i:02}_RESULT.json').read_text())['exit_code']==0
mods=['OppositeGQ44SpreadInputs','OppositeGQ44SpreadExact','OppositeGQ44SpreadAudit'];done=[]
for m in mods:
 p=subprocess.run([sys.executable,str(D/'compile.py'),m,'115'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
 r=json.loads((D/f'{m}_RESULT.json').read_text());print(json.dumps(r),flush=True)
 if r['exit_code']!=0:print(p.stdout,flush=True);raise SystemExit(1)
 done.append(m)
(D/'FINAL_ASSEMBLY_BATCH_RESULT.json').write_text(json.dumps({'status':'COMPLETE','modules':done},indent=2)+'\n')
