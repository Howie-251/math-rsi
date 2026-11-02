import json,pathlib,resource,subprocess,time,math
P=pathlib.Path(__file__).resolve().parent;START=time.process_time();WALL=time.monotonic();r=resource.getrusage(resource.RUSAGE_CHILDREN);C0=r.ru_utime+r.ru_stime
assert not(P/'TERMINAL.json').exists()
def childcpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN);return r.ru_utime+r.ru_stime-C0
with(P/'compile.log').open('w') as f:ret=subprocess.run(['g++','-O3','-std=c++17','scan.cpp','-o','scan'],cwd=P,stdout=f,stderr=f)
assert ret.returncode==0;compileCPU=childcpu();remaining=15-childcpu()-(time.process_time()-START);assert remaining>1
budget=remaining-1;soft=math.ceil(remaining-.5);hard=math.ceil(remaining)
def limits():resource.setrlimit(resource.RLIMIT_CPU,(soft,hard))
with(P/'native.stdout').open('w') as out,(P/'native.stderr').open('w') as err:
 proc=subprocess.Popen([str(P/'scan'),str(budget)],cwd=P,stdout=out,stderr=err,preexec_fn=limits)
 (P/'LIVE_HANDLE.json').write_text(json.dumps({'status':'RUNNING_ALL_COMPONENTS','pid':proc.pid,'compile_CPU_seconds':compileCPU,'worker_budget_seconds':budget,'worker_limits':[soft,hard]},indent=2)+'\n');print(json.dumps({'actual_worker_PID':proc.pid,'compile_CPU_seconds':compileCPU}),flush=True)
 try:code=proc.wait(timeout=35)
 except subprocess.TimeoutExpired:proc.kill();code=proc.wait()
w=json.loads((P/'WORKER_RESULT.json').read_text()) if(P/'WORKER_RESULT.json').exists() else {'status':'UNKNOWN_NO_RESULT'}
status=w['status'] if code==0 and w['status']!='RUNNING' else 'UNKNOWN_PROCESS_TERMINATED'
t={'status':status,'exit_code':code,'pid':proc.pid,'compile_CPU_seconds':compileCPU,'children_CPU_seconds':childcpu(),'driver_CPU_seconds':time.process_time()-START,'aggregate_CPU_seconds':childcpu()+time.process_time()-START,'wall_seconds':time.monotonic()-WALL,'source_D5_BFS':0,'solver_calls':0}
(P/'TERMINAL.json').write_text(json.dumps(t,indent=2)+'\n');(P/'LIVE_HANDLE.json').write_text(json.dumps({'status':'TERMINAL','pid':proc.pid,'exit_code':code},indent=2)+'\n');print(json.dumps(t),flush=True);print(json.dumps(w),flush=True)
