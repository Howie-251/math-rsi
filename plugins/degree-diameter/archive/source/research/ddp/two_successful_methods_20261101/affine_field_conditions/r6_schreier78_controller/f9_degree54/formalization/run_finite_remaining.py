import json,subprocess,sys
from pathlib import Path
D=Path(__file__).resolve().parent;N='F9Graph56862'
mods=[N+f'ModelChunk{i:02d}' for i in range(1,13)]+[N+f'PairChunk{i}' for i in range(1,6)]
mods += [N+f'AdjacentChart{c}Block{b}' for c in range(8) for b in range(3) if (c,b)!=(0,0)]
for mod in mods:
 p=subprocess.run([sys.executable,str(D/'compile.py'),mod,'60'],capture_output=True,text=True)
 if p.returncode:
  print(p.stdout,p.stderr,flush=True);raise SystemExit(p.returncode)
 r=json.loads((D/(mod+'_RESULT.json')).read_text());assert r['exit_code']==0
 print(json.dumps({k:r[k] for k in ['module','exit_code','CPU_seconds','wall_seconds']}),flush=True)
print('ALL40_REMAINING_FINITE_MODULES_PASS',flush=True)
