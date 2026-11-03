import json,os,resource,subprocess,sys,time
from pathlib import Path
D=Path(__file__).resolve().parent;R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir());F=R/'formal'
mod=sys.argv[1];assert mod.startswith(('DiagonalFillReallocation','Q4DiagonalFill','Q8DiagonalFill'))
def save(p,d):
 t=p.with_suffix(p.suffix+'.tmp');t.write_text(json.dumps(d,indent=2)+'\n');os.replace(t,p)
p=D/'CHECKPOINT.json'
if p.exists():s=json.loads(p.read_text());assert not s['running']
else:s=dict(attempts=[],completed=[],preparation_CPU_seconds=0.,running=False,driver_CPU_seconds=0.)
s['preparation_CPU_seconds']=sum(json.loads(p.read_text())['CPU_seconds']for p in D.glob('*PREPARATION_RESULT.json'))
startcpu=time.process_time();oldcpu=s['driver_CPU_seconds']
def state(status):
 s['status']=status;s['driver_CPU_seconds']=oldcpu+time.process_time()-startcpu;s['CPU_seconds']=s['preparation_CPU_seconds']+s['driver_CPU_seconds']+sum(a['CPU_seconds']for a in s['attempts']);save(p,s)
assert mod not in s['completed'];state('READY');assert s['CPU_seconds']+60<=600
attempt=1+sum(a['module']==mod for a in s['attempts']);stem=f'{mod}_attempt{attempt:03d}';audit=mod.endswith('Audit');src=mod+'.lean'if audit else'DegreeDiameter/Portfolio/'+mod+'.lean';out='.lake/build/lib/lean/'+src[:-5]+'.olean'
base=json.loads((R/'research/ddp/refresh_20261029/f5_full_d20_D3/FORMAL_ENV_COMMAND.json').read_text());env=dict(os.environ,LEAN_PATH=base['LEAN_PATH'],LEAN_NUM_THREADS='1')
cmd=[str(R/'.tools/lean-4.24.0-linux/bin/lean'),'-j1','-s65536','-o',out,src];logpath=D/(stem+'.log');t=time.monotonic();before=resource.getrusage(resource.RUSAGE_CHILDREN)
def limits():resource.setrlimit(resource.RLIMIT_CPU,(60,60))
with logpath.open('w')as log:
 child=subprocess.Popen(cmd,cwd=F,env=env,stdout=log,stderr=log,preexec_fn=limits);s['running']=True;s['active_module']=dict(module=mod,pid=child.pid,command=cmd,log=str(logpath));state('RUNNING');save(D/'HANDLE.json',dict(driver_pid=os.getpid(),**s['active_module']));child.wait()
after=resource.getrusage(resource.RUSAGE_CHILDREN);cpu=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
r=dict(module=mod,attempt=attempt,exit_code=child.returncode,CPU_seconds=cpu,wall_seconds=time.monotonic()-t,command=cmd,log=str(logpath),output=str(F/out),PASS=child.returncode==0 and(F/out).exists());s['attempts'].append(r);s['running']=False;s.pop('active_module',None)
if r['PASS']:s['completed'].append(mod)
state('MODULE_PASS'if r['PASS']else'FAILED_NEEDS_REPAIR');save(D/(stem+'.json'),r);save(D/'HANDLE.json',dict(status=s['status'],running=False,active_modules=[],CPU_seconds=s['CPU_seconds']));print(json.dumps(r),flush=True);print(logpath.read_text()[:14000]);sys.exit(0 if r['PASS']else 1)
