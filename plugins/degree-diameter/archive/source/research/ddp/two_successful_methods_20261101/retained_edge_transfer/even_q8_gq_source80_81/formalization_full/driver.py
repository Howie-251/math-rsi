"""Bounded, resumable new-module compiler; never builds an imported old module."""
import argparse,json,os,resource,subprocess,sys,time
from pathlib import Path

D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir());F=R/'formal'
TOTAL=12000.;LIMIT=60;SELF0=time.process_time()
def save(path,data):
    temp=path.with_suffix(path.suffix+'.tmp');temp.write_text(json.dumps(data,indent=2)+'\n');os.replace(temp,path)
def alive(pid):
    try:os.kill(pid,0);return True
    except ProcessLookupError:return False
parser=argparse.ArgumentParser();parser.add_argument('--workers',type=int,default=8);parser.add_argument('--resume',action='store_true');parser.add_argument('--take',type=int,default=0)
args=parser.parse_args();assert 1<=args.workers<=8
statepath=D/'CHECKPOINT.json';handlepath=D/'DRIVER_HANDLE.json'
if handlepath.exists():
    old=json.loads(handlepath.read_text())
    if old.get('running')and alive(old['pid']):raise SystemExit('An existing full driver is active')
plan=json.loads((D/'MODULE_PLAN.json').read_text());allmods=plan['common']+plan['leaves']+plan['assembly']
base=json.loads((R/'research/ddp/refresh_20261029/f5_full_d20_D3/FORMAL_ENV_COMMAND.json').read_text())
env=dict(os.environ,LEAN_PATH=base['LEAN_PATH'],LEAN_NUM_THREADS='1')
attemptdir=D/'attempts';attemptdir.mkdir(exist_ok=True)
if statepath.exists():
    if not args.resume:raise SystemExit('Existing ledger: use --resume; the CPU budget is not reset')
    state=json.loads(statepath.read_text())
    if state.get('active_modules'):raise SystemExit('Unreconciled prior handles: inspect before resume')
else:
    prep=json.loads((D/'PREPARATION_RESULT.json').read_text())['CPU_seconds']
    state=dict(status='READY',budget_CPU_seconds=TOTAL,preparation_CPU_seconds=prep,driver_CPU_seconds=0.,attempt_CPU_seconds=0.,completed=[],attempts=[],active_modules=[],running=False,source_targets_complete=False)
previous_driver_cpu=state.get('driver_CPU_seconds',0.);active={};halt=False
initial_attempt_count=len(state['attempts']);requested_stop=False
state.pop('failed_module',None)
def extra_cost():
    return sum(json.loads(p.read_text())['CPU_seconds']for p in list(D.glob('ADAPTATION_*_RESULT.json'))+[D/'EXTERNAL_TABLE_BINDING.json']if p.exists())
def checkpoint(status=None):
    if status:state['status']=status
    state['driver_CPU_seconds']=previous_driver_cpu+time.process_time()-SELF0
    state['additional_preparation_CPU_seconds']=extra_cost()
    state['accounted_CPU_seconds']=state['preparation_CPU_seconds']+state['additional_preparation_CPU_seconds']+state['driver_CPU_seconds']+state['attempt_CPU_seconds']
    state['active_modules']=[{k:v for k,v in job.items()if k not in ('proc','file')}for job in active.values()]
    state['running']=bool(active)or state.get('status')in('RUNNING','READY')
    state['completed_count']=len(state['completed']);state['remaining_count']=len(allmods)-len(state['completed'])
    state['updated_UTC']=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())
    save(statepath,state)
    save(handlepath,dict(pid=os.getpid(),running=state['running'],status=state['status'],checkpoint=str(statepath),completed=state['completed_count'],remaining=state['remaining_count'],active_modules=state['active_modules'],accounted_CPU_seconds=state['accounted_CPU_seconds']))
def launch(mod):
    used=state['preparation_CPU_seconds']+extra_cost()+state['attempt_CPU_seconds']+previous_driver_cpu+time.process_time()-SELF0
    if used+LIMIT*(len(active)+1)>TOTAL:
        return False
    previous=sum(x['module']==mod for x in state['attempts'])
    md=attemptdir/mod;md.mkdir(exist_ok=True)
    attempt=previous+1;logpath=md/f'attempt{attempt:04d}.log'
    audit=mod.endswith('Audit');src=(mod+'.lean')if audit else('DegreeDiameter/Portfolio/'+mod+'.lean')
    out='.lake/build/lib/lean/'+src[:-5]+'.olean'
    cmd=[str(R/'.tools/lean-4.24.0-linux/bin/lean'),'-j1','-s65536','-o',out,src]
    log=logpath.open('w')
    def limits():resource.setrlimit(resource.RLIMIT_CPU,(LIMIT,LIMIT))
    proc=subprocess.Popen(cmd,cwd=F,env=env,stdout=log,stderr=log,preexec_fn=limits)
    job=dict(module=mod,attempt=attempt,pid=proc.pid,CPU_limit_seconds=LIMIT,command=cmd,log=str(logpath),receipt=str(md/f'attempt{attempt:04d}.json'),output=str(F/out),start_monotonic=time.monotonic(),proc=proc,file=log)
    active[proc.pid]=job;checkpoint('RUNNING');return True
def nextready():
    done=set(state['completed']);running={v['module']for v in active.values()}
    for mod in plan['common']:
        if mod not in done:
            return mod if mod not in running and not active else None
    for mod in plan['leaves']:
        if mod not in done and mod not in running:return mod
    if active:return None
    for mod in plan['assembly']:
        if mod not in done:return mod
    return None
checkpoint('READY')
print(json.dumps(dict(event='DRIVER_STARTED',pid=os.getpid(),checkpoint=str(statepath),completed=len(state['completed']),total=len(allmods))),flush=True)
last_report=0.;smoke_completions=0
try:
    while True:
        if (D/'STOP_REQUEST').exists():halt=True;requested_stop=True
        if args.take and len(state['attempts'])-initial_attempt_count>=args.take:
            halt=True;requested_stop=True
        while not halt and len(active)<args.workers:
            if args.take and len(state['attempts'])-initial_attempt_count+len(active)>=args.take:break
            mod=nextready()
            if mod is None:break
            if not launch(mod):halt=True;checkpoint('BUDGET_RESERVATION_STOP');break
        reaped=False
        while active:
            pid,status,usage=os.wait4(-1,os.WNOHANG)
            if not pid:break
            reaped=True;job=active.pop(pid);code=os.waitstatus_to_exitcode(status)
            job['proc'].returncode=code;job['file'].close()
            cpu=usage.ru_utime+usage.ru_stime
            result=dict(module=job['module'],attempt=job['attempt'],pid=pid,exit_code=code,CPU_seconds=cpu,wall_seconds=time.monotonic()-job['start_monotonic'],CPU_limit_seconds=LIMIT,command=job['command'],log=job['log'],output=job['output'])
            success=code==0 and Path(job['output']).exists()
            result['PASS']=success;save(Path(job['receipt']),result)
            state['attempts'].append(result);state['attempt_CPU_seconds']+=cpu
            if success:state['completed'].append(job['module'])
            else:halt=True;state['failed_module']=job['module']
            smoke_completions+=1
            checkpoint('FAILED_DRAINING'if halt else'RUNNING')
            if not success or len(state['completed'])%8==0 or time.monotonic()-last_report>30:
                print(json.dumps(dict(event='MODULE_END',module=job['module'],PASS=success,CPU_seconds=cpu,completed=len(state['completed']),remaining=len(allmods)-len(state['completed']),accounted_CPU_seconds=state['accounted_CPU_seconds'])),flush=True);last_report=time.monotonic()
        if halt and not active:
            checkpoint('FAILED_NEEDS_REPAIR'if state.get('failed_module')else('CONTROLLED_STOP'if requested_stop else'BUDGET_STOP'));break
        if len(state['completed'])==len(allmods):
            state['source_targets_complete']=True;checkpoint('ALL_MODULES_PASS_AWAIT_EXTERNAL_BINDING');break
        if not active and nextready()is None:
            checkpoint('BLOCKED_DEPENDENCY_STATE');break
        if not reaped:time.sleep(.25)
        if time.monotonic()-last_report>45:
            checkpoint();print(json.dumps(dict(event='HEARTBEAT',completed=len(state['completed']),active=len(active),accounted_CPU_seconds=state['accounted_CPU_seconds'])),flush=True);last_report=time.monotonic()
except BaseException:
    checkpoint('DRIVER_EXCEPTION_INSPECT_HANDLES')
    raise
finally:
    if not active:
        state['running']=False;checkpoint(state['status'])
        handle=json.loads(handlepath.read_text());handle['running']=False;save(handlepath,handle)
print(json.dumps(dict(event='DRIVER_TERMINAL',status=state['status'],completed=len(state['completed']),remaining=len(allmods)-len(state['completed']),CPU_seconds=state['accounted_CPU_seconds'])),flush=True)
sys.exit(0 if state['source_targets_complete'] else 1)
