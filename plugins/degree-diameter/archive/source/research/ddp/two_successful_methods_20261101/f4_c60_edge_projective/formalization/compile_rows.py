import json,os,resource,subprocess,time
from pathlib import Path
D=Path(__file__).resolve().parent;ROOT=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');WORKERS=3;CPU_LIMIT=115;AGGREGATE=2400
modules=[f'F4Graph3840CertificateRow{i:02d}' for i in range(1,60)]
start=time.monotonic();running={};records=[];stop=None
def status(final=False):
 x=dict(status=('COMPLETE' if not modules and not running else stop or 'RUNNING') if not final else stop or 'COMPLETE',workers=WORKERS,per_module_CPU_limit=CPU_LIMIT,aggregate_CPU_limit=AGGREGATE,completed_CPU=sum(r['CPU_seconds'] for r in records),completed=len(records),already_passed_current_row00=True,pending=list(modules),running=[dict(module=m,runner_pid=p.pid) for m,(p,_) in running.items()],records=records,wall_seconds=time.monotonic()-start)
 (D/'CERTIFICATE_BATCH_HANDLE.json').write_text(json.dumps(x,indent=2)+'\n')
 if final:(D/'CERTIFICATE_BATCH_RESULT.json').write_text(json.dumps(x,indent=2)+'\n')
while modules or running:
 spent=sum(r['CPU_seconds'] for r in records)
 while modules and len(running)<WORKERS and not stop and spent+(len(running)+1)*CPU_LIMIT<=AGGREGATE:
  m=modules.pop(0);log=(D/f'{m}_runner.log').open('w');p=subprocess.Popen(['python',str(D/'compile.py'),m,str(CPU_LIMIT)],cwd=ROOT,stdout=log,stderr=log);running[m]=(p,log)
 for m,(p,log) in list(running.items()):
  if p.poll() is None:continue
  log.close();r=json.loads((D/f'{m}_RESULT.json').read_text());records.append(r);del running[m];print(json.dumps({k:r[k]for k in ['module','exit_code','CPU_seconds']}),flush=True)
  if r['exit_code']!=0:stop='STOP_AFTER_REAL_COMPILE_FAILURE'
 if not running and modules and not stop and sum(r['CPU_seconds']for r in records)+CPU_LIMIT>AGGREGATE:stop='AGGREGATE_CPU_LIMIT_REACHED'
 status()
 if stop and not running:break
 time.sleep(0.3)
status(final=True)
print(json.dumps(dict(status=stop or 'COMPLETE',completed=len(records),CPU_seconds=sum(r['CPU_seconds']for r in records),wall_seconds=time.monotonic()-start)),flush=True)
