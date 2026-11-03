import json,os,re,resource,subprocess,sys,time
from pathlib import Path
T=time.process_time();D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir());F=R/'formal';S=D.parent
PREFIX='EvenQ8BalancedFullOvoidCopy82';MODS=[PREFIX+x for x in['Definitions','Inputs','Exact','Audit']]
def save(path,data):
    temp=path.with_suffix(path.suffix+'.tmp');temp.write_text(json.dumps(data,indent=2)+'\n');os.replace(temp,path)
parent=json.loads((S.parent/'formalization_full/FINAL.json').read_text())
assert parent['status']=='BOTH_ORIGINAL_CONCRETE_SOURCE_TARGETS_KERNEL_AUDIT_AND_EXTERNAL_BINDING_PASS'
fresh=json.loads((S/'independent_acceptance/RESULT.json').read_text());assert fresh['status'].startswith('PASS_')
binding=json.loads((D/'EXTERNAL_INPUT_BINDING.json').read_text());assert binding['status'].startswith('PASS_')
base=json.loads((R/'research/ddp/refresh_20261029/f5_full_d20_D3/FORMAL_ENV_COMMAND.json').read_text())
env=dict(os.environ,LEAN_PATH=base['LEAN_PATH'],LEAN_NUM_THREADS='1')
ledgerpath=D/'CHECKPOINT.json'
if ledgerpath.exists():
    ledger=json.loads(ledgerpath.read_text());assert not ledger['running']
else:ledger=dict(attempts=[],completed=[],preparation_CPU_seconds=json.loads((D/'PREPARATION_RESULT.json').read_text())['CPU_seconds']+binding['CPU_seconds'],driver_CPU_seconds=0.,running=False)
oldcpu=ledger['driver_CPU_seconds']
def snapshot(status):
    ledger['status']=status;ledger['driver_CPU_seconds']=oldcpu+time.process_time()-T
    ledger['accounted_CPU_seconds']=ledger['preparation_CPU_seconds']+ledger['driver_CPU_seconds']+sum(a['CPU_seconds']for a in ledger['attempts'])
    ledger['remaining']=[m for m in MODS if m not in ledger['completed']]
    save(ledgerpath,ledger)
for mod in MODS:
    if mod in ledger['completed']:continue
    snapshot('READY');assert ledger['accounted_CPU_seconds']+60<=300
    audit=mod.endswith('Audit');src=(mod+'.lean')if audit else('DegreeDiameter/Portfolio/'+mod+'.lean');out='.lake/build/lib/lean/'+src[:-5]+'.olean'
    attempt=1+sum(a['module']==mod for a in ledger['attempts']);stem=f'{mod}_attempt{attempt:03d}'
    cmd=[str(R/'.tools/lean-4.24.0-linux/bin/lean'),'-j1','-s65536','-o',out,src];logpath=D/(stem+'.log');start=time.monotonic()
    before=resource.getrusage(resource.RUSAGE_CHILDREN)
    def limits():resource.setrlimit(resource.RLIMIT_CPU,(60,60))
    with logpath.open('w')as log:
        p=subprocess.Popen(cmd,cwd=F,env=env,stdout=log,stderr=log,preexec_fn=limits)
        ledger['running']=True;ledger['active_module']=dict(module=mod,pid=p.pid,CPU_limit_seconds=60,command=cmd,log=str(logpath));snapshot('RUNNING')
        save(D/'HANDLE.json',dict(driver_pid=os.getpid(),**ledger['active_module']))
        print(json.dumps(dict(event='START',module=mod,pid=p.pid)),flush=True);p.wait()
    after=resource.getrusage(resource.RUSAGE_CHILDREN);cpu=(after.ru_utime+after.ru_stime)-(before.ru_utime+before.ru_stime)
    result=dict(module=mod,attempt=attempt,exit_code=p.returncode,CPU_seconds=cpu,wall_seconds=time.monotonic()-start,CPU_limit_seconds=60,command=cmd,log=str(logpath),output=str(F/out))
    result['PASS']=p.returncode==0 and(F/out).exists();ledger['attempts'].append(result);save(D/(stem+'.json'),result)
    ledger['running']=False;ledger.pop('active_module',None)
    if result['PASS']:ledger['completed'].append(mod)
    snapshot('MODULE_PASS'if result['PASS']else'FAILED_NEEDS_REPAIR')
    print(json.dumps(result),flush=True)
    if not result['PASS']:raise SystemExit(1)
audit=next(a for a in ledger['attempts']if a['module']==PREFIX+'Audit'and a['PASS']);text=Path(audit['log']).read_text()
assert 'error:'not in text and 'sorryAx'not in text
groups=re.findall(r'depends on axioms: \[([^\]]*)\]',text);std={'propext','Classical.choice','Quot.sound'}
assert len(groups)>=4
for g in groups:assert set(x.strip()for x in g.split(',')if x.strip())<=std
snapshot('ORIGINAL_TARGET_KERNEL_AUDIT_EXTERNAL_BINDING_PASS')
result=dict(status=ledger['status'],target='DegreeDiameter.Portfolio.'+PREFIX+'.d82_346515',FinalClaim='DegreeDiameter.Portfolio.'+PREFIX+'.FinalClaim',final_claim='DegreeDiameter.Portfolio.'+PREFIX+'.final_claim',n=346515,max_degree=82,D=3,not_D2=True,genuine_Walk=True,no_user_certificate_premises=True,axioms=sorted(std),new_modules=4,CPU_seconds=ledger['accounted_CPU_seconds'],CPU_budget_seconds=300,attempts=len(ledger['attempts']),failed_attempts=sum(not a['PASS']for a in ledger['attempts']),external_binding=str(D/'EXTERNAL_INPUT_BINDING.json'),Audit_log=audit['log'],source_modules_modified_or_recompiled=False,running=False,active_modules=[],global_priority='UNKNOWN')
save(D/'FINAL.json',result);save(D/'STAGE_STATE.json',result)
save(D/'HANDLE.json',dict(status=result['status'],running=False,active_modules=[],driver_pid=os.getpid(),completed=4,remaining=0,CPU_seconds=result['CPU_seconds']))
print(json.dumps(result),flush=True)
