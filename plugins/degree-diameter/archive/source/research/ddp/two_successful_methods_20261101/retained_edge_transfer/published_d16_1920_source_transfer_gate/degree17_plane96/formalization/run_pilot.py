import json,os,resource,subprocess,sys,time
from pathlib import Path
D=Path(__file__).resolve().parent;R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir());F=R/'formal'
def save(p,d):
    t=p.with_suffix(p.suffix+'.tmp');t.write_text(json.dumps(d,indent=2)+'\n');os.replace(t,p)
fresh=json.loads((D.parent/'independent_acceptance/RESULT.json').read_text())
assert fresh['status']=='PASS_COMPLETE_LITERAL_D17_N2016_EXACT_D3'and fresh['new_roles_bound']==96
prep=json.loads((D/'PREPARATION_RESULT.json').read_text());checkpoint=D/'CHECKPOINT.json'
if checkpoint.exists():state=json.loads(checkpoint.read_text());assert not state['running']
else:state=dict(status='PREPARED',completed=[],attempts=[],running=False,driver_CPU_seconds=0.,preparation_CPU_seconds=prep['CPU_seconds'])
start=time.process_time();old_driver=state['driver_CPU_seconds']
def cost():
    return state['preparation_CPU_seconds']+old_driver+time.process_time()-start+sum(a['CPU_seconds']for a in state['attempts'])
def update(status):
    state['status']=status;state['driver_CPU_seconds']=old_driver+time.process_time()-start;state['CPU_seconds']=cost();save(checkpoint,state)
environment=json.loads((R/'research/ddp/refresh_20261029/f5_full_d20_D3/FORMAL_ENV_COMMAND.json').read_text())
env=dict(os.environ,LEAN_PATH=environment['LEAN_PATH'],LEAN_NUM_THREADS='1')
for mod in prep['modules']:
    if mod in state['completed']:continue
    used=cost();assert used<120
    limit=min(60,max(1,int(120-used)))
    attempt=1+sum(a['module']==mod for a in state['attempts']);stem=f'{mod}_attempt{attempt:03d}'
    src=mod+'.lean'if mod.endswith('Audit')else'DegreeDiameter/Portfolio/'+mod+'.lean'
    out='.lake/build/lib/lean/'+src[:-5]+'.olean';logpath=D/(stem+'.log')
    cmd=[str(R/'.tools/lean-4.24.0-linux/bin/lean'),'-j1','-s65536','-o',out,src]
    before=resource.getrusage(resource.RUSAGE_CHILDREN);wall=time.monotonic()
    def limits():resource.setrlimit(resource.RLIMIT_CPU,(limit,limit))
    with logpath.open('w')as log:
        child=subprocess.Popen(cmd,cwd=F,env=env,stdout=log,stderr=log,preexec_fn=limits)
        state['running']=True;state['active_module']=dict(module=mod,pid=child.pid,log=str(logpath),command=cmd)
        update('RUNNING')
        save(D/'DRIVER_HANDLE.json',dict(driver_pid=os.getpid(),running=True,CPU_seconds=cost(),CPU_budget_seconds=120,**state['active_module']))
        print(json.dumps(dict(status='COMPILING',module=mod,pid=child.pid,CPU_seconds=cost(),limit=limit)),flush=True)
        child.wait()
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    receipt=dict(module=mod,attempt=attempt,exit_code=child.returncode,CPU_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
        wall_seconds=time.monotonic()-wall,CPU_limit_seconds=limit,command=cmd,log=str(logpath),output=str(F/out),PASS=child.returncode==0 and(F/out).exists())
    state['attempts'].append(receipt);state['running']=False;state.pop('active_module',None)
    if receipt['PASS']:state['completed'].append(mod)
    update('MODULE_PASS'if receipt['PASS']else'FAILED_STOP_NEEDS_REPAIR');save(D/(stem+'.json'),receipt)
    save(D/'DRIVER_HANDLE.json',dict(status=state['status'],running=False,active_modules=[],CPU_seconds=cost()))
    print(json.dumps(receipt),flush=True)
    if not receipt['PASS']:
        print(logpath.read_text()[:25000],flush=True)
        save(D/'TERMINAL.json',dict(status='PILOT_ATTEMPT_FAILED_STOP',running=False,CPU_seconds=cost(),CPU_budget_seconds=120,completed=state['completed'],attempts=state['attempts'],full_source_or_clone_Lean_complete=False))
        raise SystemExit(1)
update('PILOT_EIGHT_MODULES_KERNEL_PASS_FULL_SOURCE_PENDING')
save(D/'DRIVER_HANDLE.json',dict(status=state['status'],running=False,active_modules=[],CPU_seconds=cost()))
print(json.dumps(dict(status=state['status'],completed=state['completed'],CPU_seconds=cost())),flush=True)
