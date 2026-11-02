import json,os,resource,subprocess,sys,time
from pathlib import Path
D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir());F=R/'formal'
def save(name,v):
    p=D/name;t=p.with_suffix(p.suffix+'.tmp');t.write_text(json.dumps(v,indent=2)+'\n');os.replace(t,p)
statepath=D/'CHECKPOINT.json'
s=json.loads(statepath.read_text())if statepath.exists()else dict(attempts=[],completed=[],driver_CPU_seconds=0.,running=False)
assert not s['running']
started=time.process_time();old_driver=s['driver_CPU_seconds']
def prep():
    total=0.
    for p in D.glob('*PREPARATION_RESULT.json'):
        r=json.loads(p.read_text());total+=r.get('CPU_seconds',r.get('code_preparation_CPU_seconds',0.))
    return total
def cost():return prep()+old_driver+time.process_time()-started+sum(a['CPU_seconds']for a in s['attempts'])
def update(status,active=None):
    active=active or[]
    s.update(status=status,CPU_seconds=cost(),CPU_budget_seconds=180,per_module_CPU_limit_seconds=60,
        preparation_CPU_seconds=prep(),driver_CPU_seconds=old_driver+time.process_time()-started,
        running=bool(active),active_modules=active)
    save('CHECKPOINT.json',s);save('DRIVER_HANDLE.json',dict(driver_pid=os.getpid(),status=status,CPU_seconds=cost(),
        CPU_budget_seconds=180,running=bool(active),active_modules=active))
envdata=json.loads((R/'research/ddp/refresh_20261029/f5_full_d20_D3/FORMAL_ENV_COMMAND.json').read_text())
env=dict(os.environ,LEAN_PATH=envdata['LEAN_PATH'],LEAN_NUM_THREADS='1')
for mod in sys.argv[1:]:
    assert mod.startswith('F3Graph15552')
    if mod in s['completed']:continue
    limit=min(60,int(180-cost()-0.5))
    if limit<1:update('PILOT_BUDGET_STOP');sys.exit(2)
    attempt=1+sum(a['module']==mod for a in s['attempts']);stem=f'{mod}_attempt{attempt:03d}'
    rel=mod+'.lean'if mod.endswith('Audit')else'DegreeDiameter/Portfolio/'+mod+'.lean'
    output='.lake/build/lib/lean/'+rel[:-5]+'.olean';logpath=D/(stem+'.log')
    command=[str(R/'.tools/lean-4.24.0-linux/bin/lean'),'-j1','-s65536','-o',output,rel]
    def limits():resource.setrlimit(resource.RLIMIT_CPU,(limit,limit))
    wall=time.monotonic()
    with logpath.open('w')as log:
        child=subprocess.Popen(command,cwd=F,env=env,stdout=log,stderr=log,preexec_fn=limits)
        update('NEW_SOURCE_PILOT_COMPILING',[dict(module=mod,pid=child.pid,log=str(logpath))])
        _,status,usage=os.wait4(child.pid,0);child.returncode=os.waitstatus_to_exitcode(status)
    receipt=dict(module=mod,attempt=attempt,exit_code=child.returncode,CPU_seconds=usage.ru_utime+usage.ru_stime,
        wall_seconds=time.monotonic()-wall,CPU_limit_seconds=limit,command=command,log=str(logpath),output=str(F/output),
        PASS=child.returncode==0 and(F/output).exists())
    save(stem+'.json',receipt);s['attempts'].append(receipt)
    if receipt['PASS']:s['completed'].append(mod)
    update('PILOT_NEW_MODULE_PASS'if receipt['PASS']else'PILOT_FAILED_NEEDS_REPAIR')
    print(json.dumps(dict(module=mod,PASS=receipt['PASS'],CPU_seconds=receipt['CPU_seconds'],cumulative_CPU_seconds=cost())),flush=True)
    if not receipt['PASS']:
        print(logpath.read_text()[:20000],flush=True)
        save('TERMINAL.json',dict(status=s['status'],running=False,CPU_seconds=cost(),CPU_budget_seconds=180))
        sys.exit(1)
update('REQUESTED_NEW_PILOT_MODULES_PASS')
save('TERMINAL.json',dict(status=s['status'],running=False,CPU_seconds=cost(),CPU_budget_seconds=180,
     source_full_claim_complete=False,clone_full_claim_complete=False))
