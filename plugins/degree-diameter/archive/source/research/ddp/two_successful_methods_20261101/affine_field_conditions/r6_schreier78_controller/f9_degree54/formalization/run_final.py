import json,subprocess,sys
from pathlib import Path
D=Path(__file__).resolve().parent;N='F9Graph56862'
mods=[N+f'AdjacentChart{i}' for i in range(8)]
mods += [N+s for s in ['Degree','Lower','DiameterInterface','Certificates','Adjacent','Diameter','Exact','Audit']]
for mod in mods:
 rp=D/(mod+'_RESULT.json')
 if rp.exists() and json.loads(rp.read_text())['exit_code']==0:
  print('REUSE_CURRENT_PASS '+mod,flush=True);continue
 p=subprocess.run([sys.executable,str(D/'compile.py'),mod,'60'],capture_output=True,text=True)
 if p.returncode:
  print(p.stdout,p.stderr,flush=True);raise SystemExit(p.returncode)
 r=json.loads(rp.read_text());assert r['exit_code']==0
 print(json.dumps({k:r[k] for k in ['module','exit_code','CPU_seconds','wall_seconds']}),flush=True)
print('FINAL_CONCRETE_AND_SEPARATE_AUDIT_PASS',flush=True)
