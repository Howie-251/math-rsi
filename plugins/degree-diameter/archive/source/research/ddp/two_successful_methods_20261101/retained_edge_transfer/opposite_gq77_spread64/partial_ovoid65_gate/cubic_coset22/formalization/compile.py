import json,os,resource,subprocess,sys,time
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;F=R/'formal'
base=json.loads((R/'research/ddp/refresh_20261029/f5_full_d20_D3/FORMAL_ENV_COMMAND.json').read_text())
env=dict(os.environ);env['LEAN_PATH']=base['LEAN_PATH'];env['LEAN_NUM_THREADS']='1'
mod=sys.argv[1];budget=min(int(sys.argv[2]) if len(sys.argv)>2 else 115,115)
assert mod.startswith('GQ77Cubic22Clone65')
spent=sum(json.loads(p.read_text())['CPU_seconds'] for p in D.glob('GQ77Cubic22Clone65*_RESULT.json'))
spent+=sum(json.loads(p.read_text())['CPU_seconds'] for p in (D/'build_history').glob('*_RESULT.json')) if (D/'build_history').exists() else 0
for name in ['PREPARATION_RESULT.json','INPUT_BINDING_CHECK.json']:
 if (D/name).exists():spent+=json.loads((D/name).read_text())['CPU_seconds']
assert spent+budget<=600,('Insufficient remaining batch CPU',spent,budget)
audit=mod.endswith('Audit');source=f'{mod}.lean' if audit else f'DegreeDiameter/Portfolio/{mod}.lean'
output=f'.lake/build/lib/lean/{mod}.olean' if audit else f'.lake/build/lib/lean/DegreeDiameter/Portfolio/{mod}.olean'
cmd=[str(R/'.tools/lean-4.24.0-linux/bin/lean'),'-j1','-o',output,source]
logpath=D/f'{mod}.log';start=time.monotonic();cpu0=resource.getrusage(resource.RUSAGE_CHILDREN);cpu_start=cpu0.ru_utime+cpu0.ru_stime
if logpath.exists():
 a=D/'build_history';a.mkdir(exist_ok=True);stamp=time.time_ns();(a/f'{mod}_{stamp}.log').write_text(logpath.read_text())
 rp=D/f'{mod}_RESULT.json'
 if rp.exists():(a/f'{mod}_{stamp}_RESULT.json').write_text(rp.read_text())
def limits():resource.setrlimit(resource.RLIMIT_CPU,(budget,budget+1))
with logpath.open('w') as log:
 p=subprocess.Popen(cmd,cwd=F,env=env,stdout=log,stderr=log,preexec_fn=limits)
 hp=D/f'{mod}_HANDLE.json';hp.write_text(json.dumps(dict(status='RUNNING',pid=p.pid,module=mod,command=cmd,CPU_budget_seconds=budget))+'\n');p.wait()
r=resource.getrusage(resource.RUSAGE_CHILDREN)
result=dict(module=mod,command=cmd,exit_code=p.returncode,CPU_seconds=r.ru_utime+r.ru_stime-cpu_start,wall_seconds=time.monotonic()-start,CPU_budget_seconds=budget,log=str(logpath))
(D/f'{mod}_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');hp.write_text(json.dumps(dict(status='TERMINAL',**result))+'\n')
print(json.dumps(result));print(logpath.read_text()[:18000])
