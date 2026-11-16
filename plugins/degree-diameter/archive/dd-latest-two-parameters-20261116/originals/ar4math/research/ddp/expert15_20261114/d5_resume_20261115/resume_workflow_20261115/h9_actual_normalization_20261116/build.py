import json,os,subprocess,time,resource
from pathlib import Path
d=Path(__file__).resolve().parent
c=json.loads((d/'CONFIG.json').read_text())
old=json.loads((d/'BUILD_ATTEMPTS.json').read_text()) if (d/'BUILD_ATTEMPTS.json').exists() else []
cpu_before=sum(x['child_CPU'] for x in old)
env=os.environ.copy();env['LEAN_PATH']=c['LEAN_PATH'];env['LEAN_SYSROOT']=c['LEAN_SYSROOT']
cmd=[c['lean'],'-j1','-M2048','DegreeDiameter/Portfolio/H9CrossNormalize.lean','-o',str(d/'H9CrossNormalize.olean')]
remaining=max(1,35-c['charged_preparation_CPU']-cpu_before)
def limit(): resource.setrlimit(resource.RLIMIT_CPU,(int(remaining),int(remaining)+1))
start=time.time();ru=resource.getrusage(resource.RUSAGE_CHILDREN);code=None
with (d/('BUILD_%02d.log'%len(old))).open('w') as f:
 try:
  p=subprocess.run(cmd,cwd=c['cwd'],env=env,stdout=f,stderr=subprocess.STDOUT,timeout=max(1,900-(start-c['start_epoch'])),preexec_fn=limit);code=p.returncode;status='PASS' if code==0 else 'COMPILE_ERROR'
 except subprocess.TimeoutExpired:status='WALL_TIMEOUT'
r2=resource.getrusage(resource.RUSAGE_CHILDREN);cpu=r2.ru_utime+r2.ru_stime-ru.ru_utime-ru.ru_stime
r={'status':status,'exit_code':code,'child_CPU':cpu,'compile_wall':time.time()-start,'whole_task_wall_conservative':time.time()-c['start_epoch'],'cumulative_compile_CPU':cpu_before+cpu,'log':'BUILD_%02d.log'%len(old)}
old.append(r);(d/'BUILD_ATTEMPTS.json').write_text(json.dumps(old,indent=2));print(json.dumps(r));print((d/r['log']).read_text())
