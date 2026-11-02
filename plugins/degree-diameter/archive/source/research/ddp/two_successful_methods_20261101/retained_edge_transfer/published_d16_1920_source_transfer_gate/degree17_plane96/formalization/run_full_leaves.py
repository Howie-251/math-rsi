import json,os,resource,subprocess,sys,time
from pathlib import Path
D=Path(__file__).resolve().parent;R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir());F=R/'formal'
def save(p,v):
    t=p.with_suffix(p.suffix+'.tmp');t.write_text(json.dumps(v,indent=2)+'\n');os.replace(t,p)
pilot=json.loads((D/'RESULT.json').read_text());prep=json.loads((D/'FULL_PREPARATION_RESULT.json').read_text())
p=D/'CHECKPOINT.json'
if not(D/'PILOT_CHECKPOINT.json').exists():
    old=json.loads(p.read_text());save(D/'PILOT_CHECKPOINT.json',old);save(D/'PILOT_TERMINAL.json',json.loads((D/'TERMINAL.json').read_text()))
    s=dict(status='FULL_AUTHORIZED',pilot_CPU_seconds=pilot['CPU_seconds'],pilot_attempts=old['attempts'],
        completed=old['completed'],attempts=[],full_preparation_CPU_seconds=prep['CPU_seconds'],driver_CPU_seconds=0.,running=False)
else:s=json.loads(p.read_text());assert not s['running']
start=time.process_time();old_driver=s['driver_CPU_seconds'];active={};stop_reason=None
def aux():
    path=D/'CLONE_PREPARATION_RESULT.json'
    return json.loads(path.read_text()).get('CPU_seconds',0.)if path.exists()else 0.
def cost():return s['pilot_CPU_seconds']+s['full_preparation_CPU_seconds']+aux()+old_driver+time.process_time()-start+sum(a['CPU_seconds']for a in s['attempts'])
def update(status):
    s.update(status=status,CPU_budget_seconds=1200,per_module_CPU_limit_seconds=60,
        driver_CPU_seconds=old_driver+time.process_time()-start,CPU_seconds=cost(),aux_preparation_CPU_seconds=aux(),
        running=bool(active),active_modules=[dict(module=v['module'],pid=pid,log=str(v['log']))for pid,v in active.items()])
    save(p,s);save(D/'DRIVER_HANDLE.json',dict(driver_pid=os.getpid(),status=status,running=bool(active),active_modules=s['active_modules'],CPU_seconds=cost(),CPU_budget_seconds=1200,phase=s.get('phase')))
envdata=json.loads((R/'research/ddp/refresh_20261029/f5_full_d20_D3/FORMAL_ENV_COMMAND.json').read_text());env=dict(os.environ,LEAN_PATH=envdata['LEAN_PATH'],LEAN_NUM_THREADS='1')
def launch(mod):
    global stop_reason
    if cost()+60*(len(active)+1)>1200:stop_reason='CONTROLLED_BUDGET_RESERVATION_DRAIN';return False
    attempt=1+sum(a['module']==mod for a in s['attempts']);stem=f'{mod}_attempt{attempt:03d}'
    src='DegreeDiameter/Portfolio/'+mod+'.lean';out='.lake/build/lib/lean/'+src[:-5]+'.olean';logpath=D/(stem+'.log')
    cmd=[str(R/'.tools/lean-4.24.0-linux/bin/lean'),'-j1','-s65536','-o',out,src]
    def limits():resource.setrlimit(resource.RLIMIT_CPU,(60,60))
    log=logpath.open('w');child=subprocess.Popen(cmd,cwd=F,env=env,stdout=log,stderr=log,preexec_fn=limits)
    active[child.pid]=dict(module=mod,attempt=attempt,log=logpath,stream=log,child=child,command=cmd,output=str(F/out),wall=time.monotonic())
    update('FULL_SOURCE_LEAVES_RUNNING');return True
for phase in['Data','Certificate','Walks']:
    s['phase']=phase;queue=[m for m in prep['phases'][phase]if m not in s['completed']]
    while queue or active:
        while queue and len(active)<2 and not stop_reason:
            if launch(queue[0]):queue.pop(0)
        if not active:break
        pid,status,usage=os.wait4(-1,0);v=active.pop(pid);v['child'].returncode=os.waitstatus_to_exitcode(status);v['stream'].close()
        receipt=dict(module=v['module'],attempt=v['attempt'],exit_code=v['child'].returncode,
            CPU_seconds=usage.ru_utime+usage.ru_stime,wall_seconds=time.monotonic()-v['wall'],CPU_limit_seconds=60,
            command=v['command'],output=v['output'],log=str(v['log']),PASS=v['child'].returncode==0 and Path(v['output']).exists())
        s['attempts'].append(receipt);save(D/f"{v['module']}_attempt{v['attempt']:03d}.json",receipt)
        if receipt['PASS']:s['completed'].append(v['module'])
        else:stop_reason='FAILED_SOURCE_LEAF_DRAIN'
        if phase=='Certificate':
            checked=[a for a in s['attempts']if a['PASS']and a['module'].endswith('Certificate')]
            if len(checked)>=5:
                mean=sum(a['CPU_seconds']for a in checked)/len(checked)
                forecast=cost()+(29-len(checked))*mean+29*2.111392+75
                s['actual_cost_full_forecast']=forecast
                if forecast>1200:stop_reason='CONTROLLED_COST_FORECAST_OVER1200_DRAIN'
        update(stop_reason or'FULL_SOURCE_LEAVES_RUNNING')
        print(json.dumps(dict(module=receipt['module'],PASS=receipt['PASS'],CPU_seconds=receipt['CPU_seconds'],cumulative_CPU_seconds=cost(),completed_full_leaves=len(s['completed'])-8,active=len(active),phase=phase)),flush=True)
        if not receipt['PASS']:print(v['log'].read_text()[:16000],flush=True)
    if stop_reason:break
update(stop_reason or'ALL87_NEW_SOURCE_LEAVES_PASS_ASSEMBLY_PENDING')
save(D/'TERMINAL.json',dict(status=s['status'],running=False,active_modules=[],CPU_seconds=cost(),CPU_budget_seconds=1200,
    completed_full_leaves=len(s['completed'])-8,all_source_and_clone_targets_complete=False,stop_reason=stop_reason))
print(json.dumps(dict(status=s['status'],CPU_seconds=cost(),completed_full_leaves=len(s['completed'])-8,running=False)),flush=True)
sys.exit(1 if stop_reason else 0)
