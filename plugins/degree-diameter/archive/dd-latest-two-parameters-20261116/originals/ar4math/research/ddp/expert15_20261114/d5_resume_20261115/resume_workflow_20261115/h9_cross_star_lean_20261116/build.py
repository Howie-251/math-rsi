import json,os,subprocess,time,resource,datetime
from pathlib import Path
d=Path(__file__).resolve().parent
c=json.loads((d/'CONFIG.json').read_text());env=os.environ.copy();env['LEAN_PATH']=c['LEAN_PATH'];env['LEAN_SYSROOT']=c['LEAN_SYSROOT']
cmd=[c['lean'],'-j1','-M2048','DegreeDiameter/Portfolio/H9CrossStar.lean','-o',str(d/'H9CrossStar.olean')]
start=time.time();taskstart=datetime.datetime.strptime(c['start_utc'],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=datetime.timezone.utc).timestamp()
remaining=max(1,150-(start-taskstart));ru=resource.getrusage(resource.RUSAGE_CHILDREN)
def limit(): resource.setrlimit(resource.RLIMIT_CPU,(13,14))
status='UNKNOWN';code=None
with (d/'BUILD.log').open('w') as f:
 try:
  p=subprocess.run(cmd,cwd=c['cwd'],env=env,stdout=f,stderr=subprocess.STDOUT,timeout=remaining,preexec_fn=limit);code=p.returncode;status='PASS' if code==0 else 'COMPILE_ERROR'
 except subprocess.TimeoutExpired:status='WALL_TIMEOUT'
r2=resource.getrusage(resource.RUSAGE_CHILDREN);cpu=r2.ru_utime+r2.ru_stime-ru.ru_utime-ru.ru_stime
r={'status':status,'command':cmd,'cwd':c['cwd'],'LEAN_PATH':c['LEAN_PATH'],'LEAN_SYSROOT':c['LEAN_SYSROOT'],'exit_code':code,'child_CPU':cpu,'compile_wall':time.time()-start,'whole_task_wall':time.time()-taskstart,'CPU_cap':15,'wall_cap':150,'imported_source_not_recompiled':True,'concrete_graph_Lean_closed':False}
(d/'RESULT.json').write_text(json.dumps(r,indent=2));print(json.dumps(r));print((d/'BUILD.log').read_text())
