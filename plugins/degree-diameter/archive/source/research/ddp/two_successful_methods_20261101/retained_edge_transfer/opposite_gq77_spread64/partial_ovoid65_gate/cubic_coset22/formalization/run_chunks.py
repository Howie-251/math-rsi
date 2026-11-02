import concurrent.futures,json,subprocess,sys
from pathlib import Path
D=Path(__file__).resolve().parent
def run(i):
 mod=f'GQ77Cubic22Clone65InputChunk{i:02d}'
 p=subprocess.run([sys.executable,str(D/'compile.py'),mod,'45'],capture_output=True,text=True)
 r=json.loads((D/f'{mod}_RESULT.json').read_text())
 print(json.dumps({k:r[k] for k in ['module','exit_code','CPU_seconds','wall_seconds']}),flush=True)
 if p.returncode or r['exit_code']:
  print(p.stdout,p.stderr,flush=True);raise RuntimeError(mod)
 return r
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
 list(pool.map(run,range(1,20)))
print('ALL19_REMAINING_CHUNKS_PASS',flush=True)
