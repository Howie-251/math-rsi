from pathlib import Path
import json,resource,subprocess,time,math
out=Path(__file__).resolve().parent;started=time.process_time();before=resource.getrusage(resource.RUSAGE_CHILDREN)
def compile_limit():resource.setrlimit(resource.RLIMIT_CPU,(29,29))
with (out/'compile.log').open('w') as log:c=subprocess.run(['g++','-O3','-std=c++17',str(out/'core_gate.cpp'),'-o',str(out/'core_gate')],stdout=log,stderr=subprocess.STDOUT,preexec_fn=compile_limit,timeout=60)
afterc=resource.getrusage(resource.RUSAGE_CHILDREN);compile_cpu=afterc.ru_utime+afterc.ru_stime-before.ru_utime-before.ru_stime;assert c.returncode==0
limit=max(1,math.floor(30-compile_cpu-(time.process_time()-started)-0.25))
def native_limit():resource.setrlimit(resource.RLIMIT_CPU,(limit,limit))
with (out/'native.log').open('w') as log:
 try:r=subprocess.run([str(out/'core_gate'),str(out)],stdout=log,stderr=subprocess.STDOUT,preexec_fn=native_limit,timeout=120);code=r.returncode
 except subprocess.TimeoutExpired:code='WALL_TIMEOUT'
after=resource.getrusage(resource.RUSAGE_CHILDREN);native_cpu=after.ru_utime+after.ru_stime-afterc.ru_utime-afterc.ru_stime
if code==0:result=json.loads((out/'NATIVE_RESULT.json').read_text())
else:result={'status':'UNKNOWN_AFTER_PROCESS_LIMIT','checkpoint':json.loads((out/'checkpoint.json').read_text()),'source_BFS':0,'target_BFS':0,'target_graphs':0,'target_settings_tested':0}
result.update({'receipt':{'native_exit_code':code,'compile_CPU_seconds':compile_cpu,'native_process_CPU_seconds':native_cpu,'driver_CPU_seconds':time.process_time()-started,'native_CPU_hard_limit_seconds':limit,'total_CPU_budget_seconds':30,'workers':1},'live_handle':None,'follow_on_target_batch':'NOT_STARTED_PER_LATEST_SMALL_PARAMETER_STEERING'})
(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');(out/'terminal.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
