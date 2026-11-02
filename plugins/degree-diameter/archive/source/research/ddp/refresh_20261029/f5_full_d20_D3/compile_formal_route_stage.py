import json,os,resource,subprocess,sys,time
from pathlib import Path
ROOT=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;F=ROOT/'formal'
stage=sys.argv[1];modules=sys.argv[2:];base=json.loads((D/'FORMAL_ENV_COMMAND.json').read_text());env=dict(os.environ);env['LEAN_PATH']=base['LEAN_PATH'];env['LEAN_NUM_THREADS']='8'
start=time.monotonic();r0=resource.getrusage(resource.RUSAGE_CHILDREN);records=[];status='COMPLETE'
for module in modules:
 used=resource.getrusage(resource.RUSAGE_CHILDREN);spent=used.ru_utime+used.ru_stime-r0.ru_utime-r0.ru_stime;remaining=max(1,int(110-spent))
 if spent>=109:status='CPU_BUDGET_PARTIAL';break
 cmd=[str(ROOT/'.tools/lean-4.24.0-linux/bin/lean'),'-j8','-o',f'.lake/build/lib/lean/DegreeDiameter/Portfolio/{module}.olean',f'DegreeDiameter/Portfolio/{module}.lean'];logpath=D/f'{stage}_{module}.log'
 def limits():resource.setrlimit(resource.RLIMIT_CPU,(remaining,remaining+1))
 with logpath.open('w')as log:
  p=subprocess.Popen(cmd,cwd=F,env=env,stdout=log,stderr=log,preexec_fn=limits);handle=dict(status='RUNNING',pid=p.pid,stage=stage,module=module,command=cmd,CPU_budget_seconds=110,CPU_spent_before_module=spent);(D/f'{stage}_HANDLE.json').write_text(json.dumps(handle)+'\n')
  try:p.wait(timeout=180)
  except subprocess.TimeoutExpired:p.kill();p.wait()
  record=dict(module=module,pid=p.pid,exit_code=p.returncode,log=str(logpath));records.append(record)
 if p.returncode:status='COMPILE_FAILURE';break
r1=resource.getrusage(resource.RUSAGE_CHILDREN);result=dict(status=status,records=records,wall_seconds=time.monotonic()-start,CPU_seconds=r1.ru_utime+r1.ru_stime-r0.ru_utime-r0.ru_stime,CPU_budget_seconds=110,all_modules_compiled=len(records)==len(modules)and all(t['exit_code']==0 for t in records));(D/f'{stage}_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');(D/f'{stage}_HANDLE.json').write_text(json.dumps(dict(**result,process_state='TERMINAL'))+'\n');print(json.dumps(result))
for rec in records:print(rec['module'],Path(rec['log']).read_text()[:6000])
