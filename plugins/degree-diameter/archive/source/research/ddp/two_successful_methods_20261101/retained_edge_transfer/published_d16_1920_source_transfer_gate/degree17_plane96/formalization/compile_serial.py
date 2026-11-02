"""Compile only new assembly modules after the two-leaf queue has drained."""
import json, os, resource, subprocess, sys, time
from pathlib import Path
D=Path(__file__).resolve().parent
R=next(p for p in D.parents if (p/'formal/DegreeDiameter/Portfolio').is_dir())
F=R/'formal'
def save(path,value):
    temp=path.with_suffix(path.suffix+'.tmp')
    temp.write_text(json.dumps(value,indent=2)+'\n');os.replace(temp,path)
s=json.loads((D/'CHECKPOINT.json').read_text())
assert not s['running'], 'Leaf queue must be terminal before serial compilation'
allowed=json.loads((D/'ASSEMBLY_PREPARATION_RESULT.json').read_text())['sequential_modules']
modules=sys.argv[1:] or allowed
assert all(m in allowed for m in modules)
start=time.process_time();previous_driver=s['driver_CPU_seconds']
def aux():
    total=0.
    for name,key in [('CLONE_PREPARATION_RESULT.json','code_preparation_CPU_seconds'),
                     ('ASSEMBLY_PREPARATION_RESULT.json','CPU_seconds'),
                     ('EXTERNAL_BINDING_RESULT.json','CPU_seconds'),
                     ('SERIAL_PREPARATION_RESULT.json','CPU_seconds')]:
        path=D/name
        if path.exists():total+=json.loads(path.read_text()).get(key,0.)
    return total
def cost():
    return (s['pilot_CPU_seconds']+s['full_preparation_CPU_seconds']+aux()+
            previous_driver+time.process_time()-start+sum(a['CPU_seconds'] for a in s['attempts']))
def update(status,active=None):
    active=active or []
    s.update(status=status,phase='ASSEMBLY_SERIAL',running=bool(active),active_modules=active,
             driver_CPU_seconds=previous_driver+time.process_time()-start,
             aux_preparation_CPU_seconds=aux(),CPU_seconds=cost(),CPU_budget_seconds=1200,
             per_module_CPU_limit_seconds=60)
    save(D/'CHECKPOINT.json',s)
    save(D/'DRIVER_HANDLE.json',dict(driver_pid=os.getpid(),status=status,running=bool(active),
         active_modules=active,CPU_seconds=cost(),CPU_budget_seconds=1200,phase=s['phase']))
envdata=json.loads((R/'research/ddp/refresh_20261029/f5_full_d20_D3/FORMAL_ENV_COMMAND.json').read_text())
env=dict(os.environ,LEAN_PATH=envdata['LEAN_PATH'],LEAN_NUM_THREADS='1')
for mod in modules:
    if mod in s['completed']:continue
    if cost()+60>1200:
        update('ASSEMBLY_BUDGET_RESERVATION_STOP');sys.exit(2)
    attempt=1+sum(a['module']==mod for a in s['attempts'])
    stem=f'{mod}_attempt{attempt:03d}'
    rel=(mod+'.lean') if mod.endswith('Audit') else ('DegreeDiameter/Portfolio/'+mod+'.lean')
    output='.lake/build/lib/lean/'+rel[:-5]+'.olean'
    logpath=D/(stem+'.log')
    cmd=[str(R/'.tools/lean-4.24.0-linux/bin/lean'),'-j1','-s65536','-o',output,rel]
    def limits():resource.setrlimit(resource.RLIMIT_CPU,(60,60))
    begin=time.monotonic()
    with logpath.open('w') as log:
        child=subprocess.Popen(cmd,cwd=F,env=env,stdout=log,stderr=log,preexec_fn=limits)
        update('ASSEMBLY_SERIAL_RUNNING',[dict(module=mod,pid=child.pid,log=str(logpath))])
        pid,status,usage=os.wait4(child.pid,0)
        child.returncode=os.waitstatus_to_exitcode(status)
    receipt=dict(module=mod,attempt=attempt,exit_code=child.returncode,
         CPU_seconds=usage.ru_utime+usage.ru_stime,wall_seconds=time.monotonic()-begin,
         CPU_limit_seconds=60,command=cmd,output=str(F/output),log=str(logpath),
         PASS=child.returncode==0 and (F/output).exists())
    save(D/(stem+'.json'),receipt);s['attempts'].append(receipt)
    if receipt['PASS']:s['completed'].append(mod)
    update('ASSEMBLY_SERIAL_STEP_PASS' if receipt['PASS'] else 'ASSEMBLY_FAILED_NEEDS_REPAIR')
    print(json.dumps(dict(module=mod,PASS=receipt['PASS'],CPU_seconds=receipt['CPU_seconds'],
                         cumulative_CPU_seconds=cost())),flush=True)
    if not receipt['PASS']:
        print(logpath.read_text()[:18000],flush=True)
        save(D/'TERMINAL.json',dict(status=s['status'],running=False,CPU_seconds=cost(),
             failed_module=mod,all_source_and_clone_targets_complete=False))
        sys.exit(1)
update('REQUESTED_NEW_SERIAL_MODULES_PASS')
save(D/'TERMINAL.json',dict(status=s['status'],running=False,CPU_seconds=cost(),
     all_source_and_clone_targets_complete=all(m in s['completed'] for m in allowed)))
