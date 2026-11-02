import json,os,resource,subprocess,sys,time
from pathlib import Path
ROOT=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math'); D=Path(__file__).resolve().parent; F=ROOT/'formal'
base=json.loads((ROOT/'research/ddp/refresh_20261029/f5_full_d20_D3/FORMAL_ENV_COMMAND.json').read_text());env=dict(os.environ);env['LEAN_PATH']=base['LEAN_PATH'];env['LEAN_NUM_THREADS']='1'
mod=sys.argv[1];budget=int(sys.argv[2]) if len(sys.argv)>2 else 60
audit=mod.endswith('Audit')
source=f'{mod}.lean' if audit else f'DegreeDiameter/Portfolio/{mod}.lean'
output=f'.lake/build/lib/lean/{mod}.olean' if audit else f'.lake/build/lib/lean/DegreeDiameter/Portfolio/{mod}.olean'
cmd=[str(ROOT/'.tools/lean-4.24.0-linux/bin/lean'),'-j1','-o',output,source]
logpath=D/f'{mod}.log';start=time.monotonic();cpu0=resource.getrusage(resource.RUSAGE_CHILDREN);cpu_start=cpu0.ru_utime+cpu0.ru_stime
if logpath.exists():
 archive=D/'build_history';archive.mkdir(exist_ok=True)
 stamp=time.time_ns();(archive/f'{mod}_{stamp}.log').write_text(logpath.read_text())
 resultpath=D/f'{mod}_RESULT.json'
 if resultpath.exists():(archive/f'{mod}_{stamp}_RESULT.json').write_text(resultpath.read_text())
def limits():resource.setrlimit(resource.RLIMIT_CPU,(budget,budget+1))
with logpath.open('w') as log:
 p=subprocess.Popen(cmd,cwd=F,env=env,stdout=log,stderr=log,preexec_fn=limits);(D/f'{mod}_HANDLE.json').write_text(json.dumps(dict(status='RUNNING',pid=p.pid,module=mod,command=cmd,CPU_budget_seconds=budget))+'\n');(D/'COMPILE_HANDLE.json').write_text((D/f'{mod}_HANDLE.json').read_text());p.wait()
r=resource.getrusage(resource.RUSAGE_CHILDREN);result=dict(module=mod,command=cmd,exit_code=p.returncode,CPU_seconds=r.ru_utime+r.ru_stime-cpu_start,child_cpu_baseline=cpu_start,wall_seconds=time.monotonic()-start,CPU_budget_seconds=budget,log=str(logpath));(D/f'{mod}_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');(D/f'{mod}_HANDLE.json').write_text(json.dumps(dict(status='TERMINAL',**result))+'\n');(D/'COMPILE_HANDLE.json').write_text((D/f'{mod}_HANDLE.json').read_text());print(json.dumps(result));print(logpath.read_text()[:18000])
