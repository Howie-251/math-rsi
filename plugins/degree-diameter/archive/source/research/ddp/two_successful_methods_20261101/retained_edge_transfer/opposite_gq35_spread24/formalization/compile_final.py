import json,subprocess,sys,time
from pathlib import Path
D=Path(__file__).resolve().parent
batch=json.loads((D/'INPUT_BATCH_RESULT.json').read_text());assert batch['status']=='COMPLETE_ALL60_REMAINING_ROWS',batch['status']
for p in range(64):assert json.loads((D/f'OppositeGQ35SpreadInputRow{p:02}_RESULT.json').read_text())['exit_code']==0
mods=['OppositeGQ35SpreadInputs','OppositeGQ35SpreadDegree','OppositeGQ35SpreadDiameter','OppositeGQ35SpreadLower','OppositeGQ35SpreadExact','OppositeGQ35SpreadAudit'];done=[]
for m in mods:
 p=subprocess.run([sys.executable,str(D/'compile.py'),m,'115'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
 r=json.loads((D/f'{m}_RESULT.json').read_text());print(json.dumps(r),flush=True)
 if r['exit_code']!=0:
  print(p.stdout,flush=True);raise SystemExit(1)
 done.append(m)
(D/'FINAL_ASSEMBLY_BATCH_RESULT.json').write_text(json.dumps({'status':'COMPLETE','completed':done},indent=2)+'\n')
