import json,pathlib,resource,subprocess,time,math
P=pathlib.Path(__file__).resolve().parent;START=time.process_time();WALL=time.monotonic();cr=resource.getrusage(resource.RUSAGE_CHILDREN);C0=cr.ru_utime+cr.ru_stime
assert json.loads((P/'PREDICTION.json').read_text())['status']=='FROZEN_BEFORE_ANY_TARGET_GRAPH_OR_BFS'
assert not (P/'TERMINAL.json').exists() and not(P/'CASES.jsonl').exists()
def childcpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN);return r.ru_utime+r.ru_stime-C0
with (P/'compile.log').open('w') as log:ret=subprocess.run(['g++','-std=c++17','-O3','search.cpp','-o','search'],cwd=P,stdout=log,stderr=log)
compile_cpu=childcpu();assert ret.returncode==0
remaining=120-childcpu()-(time.process_time()-START);worker_budget=max(1,remaining-2);soft=math.ceil(remaining-1);hard=math.ceil(remaining)
def limits():resource.setrlimit(resource.RLIMIT_CPU,(soft,hard))
with (P/'worker.stdout').open('w') as out,(P/'worker.stderr').open('w') as err:
 proc=subprocess.Popen([str(P/'search'),str(worker_budget)],cwd=P,stdout=out,stderr=err,preexec_fn=limits)
 live={'status':'RUNNING_UNIQUE_TWO_RULE_BATCH','pid':proc.pid,'compile_CPU_seconds':compile_cpu,'native_soft_budget_seconds':worker_budget,'worker_soft_hard_CPU':[soft,hard],'aggregate_CPU_budget':120}
 (P/'LIVE_HANDLE.json').write_text(json.dumps(live,indent=2)+'\n');print(json.dumps(live),flush=True)
 try:code=proc.wait(timeout=150)
 except subprocess.TimeoutExpired:proc.kill();code=proc.wait()
r=json.loads((P/'WORKER_RESULT.json').read_text()) if(P/'WORKER_RESULT.json').exists() else {'status':'UNKNOWN_NO_WORKER_RESULT'}
terminal_status=r['status'] if code==0 and r['status']!='RUNNING' else 'UNKNOWN_PROCESS_TERMINATED'
term={'status':terminal_status,'last_worker_status':r['status'],'pid':proc.pid,'exit_code':code,'compile_CPU_seconds':compile_cpu,'children_CPU_seconds':childcpu(),'driver_CPU_seconds':time.process_time()-START,'aggregate_CPU_seconds':childcpu()+time.process_time()-START,'wall_seconds':time.monotonic()-WALL,'source_BFS':0,'core_BFS':0,'solver_calls':0}
(P/'TERMINAL.json').write_text(json.dumps(term,indent=2)+'\n');(P/'LIVE_HANDLE.json').write_text(json.dumps({'status':'TERMINAL','pid':proc.pid,'exit_code':code},indent=2)+'\n');print(json.dumps(term),flush=True);print(json.dumps(r),flush=True)
