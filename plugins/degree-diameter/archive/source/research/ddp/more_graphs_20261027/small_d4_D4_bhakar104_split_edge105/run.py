import json, pathlib, resource, shutil, subprocess, time, os
P=pathlib.Path(__file__).resolve().parent
ROOT=pathlib.Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math')
START=time.process_time(); WALL=time.monotonic()
def children():
 r=resource.getrusage(resource.RUSAGE_CHILDREN);return r.ru_utime+r.ru_stime
C0=children()
SRC=ROOT/'research/ddp/breadth_20261027_wave2/sources'
shutil.copyfile(SRC/'bhakar104.edges',P/'source.edges')
d=json.loads((SRC/'bhakar104_distances.json').read_text()); assert len(d)==104 and all(len(r)==104 for r in d)
(P/'source_distances.txt').write_text('\n'.join(' '.join(map(str,r)) for r in d)+'\n')
(P/'INPUT.json').write_text(json.dumps({'source_edges':str(SRC/'bhakar104.edges'),'source_distance_cache':str(SRC/'bhakar104_distances.json'),'source_D4_inherited':True,'source_BFS':0,'n':104,'m':208,'new_n':105,'new_m':210,'planned_parameter_objects':119808,'canonical_partitions':'A contains least neighbor; three choices','xy_domain':'both endpoints outside closed source neighborhood of v','skip_delta_Q_sizes':[0,4],'skip_U':[12,13,41,44,48,49,52,53,104],'CPU_budget_seconds':30},indent=2)+'\n')
compile_start=children()
c=subprocess.run(['g++','-std=c++17','-O3','production.cpp','-o','production'],cwd=P,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
(P/'compile.stdout').write_text(c.stdout);(P/'compile.stderr').write_text(c.stderr)
compCPU=children()-compile_start
if c.returncode: raise RuntimeError('compile failed')
remaining=30-(children()-C0)-(time.process_time()-START)
assert remaining>1
cpu_soft=max(1,min(26,int(remaining)-1))
def limits(): resource.setrlimit(resource.RLIMIT_CPU,(cpu_soft,cpu_soft+1))
with (P/'worker.stdout').open('w') as out,(P/'worker.stderr').open('w') as err:
 proc=subprocess.Popen([str(P/'production')],cwd=P,stdout=out,stderr=err,preexec_fn=limits)
 (P/'LIVE_HANDLE.json').write_text(json.dumps({'pid':proc.pid,'status':'RUNNING','worker_soft_CPU_limit':cpu_soft,'worker_hard_CPU_limit':cpu_soft+1,'aggregate_budget_CPU':30,'compile_CPU_seconds':compCPU},indent=2)+'\n')
 print(json.dumps({'actual_worker_PID':proc.pid,'compile_CPU_seconds':compCPU}),flush=True)
 try: code=proc.wait(timeout=60)
 except subprocess.TimeoutExpired:
  proc.kill();code=proc.wait()
worker = json.loads((P/'WORKER_RESULT.json').read_text()) if (P/'WORKER_RESULT.json').exists() else {'status':'UNKNOWN_NO_WORKER_RESULT'}
terminal={'status':worker['status'],'exit_code':code,'pid':proc.pid,'compile_CPU_seconds':compCPU,'children_CPU_seconds':children()-C0,'driver_CPU_seconds':time.process_time()-START,'aggregate_CPU_seconds':children()-C0+time.process_time()-START,'wall_seconds':time.monotonic()-WALL,'worker_result':'WORKER_RESULT.json','actual_solver_calls':0,'source_BFS':0}
(P/'TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n');(P/'LIVE_HANDLE.json').write_text(json.dumps({'pid':proc.pid,'status':'TERMINAL','exit_code':code},indent=2)+'\n')
print(json.dumps(terminal),flush=True);print(json.dumps(worker),flush=True)
if code: raise RuntimeError(f'worker exit {code}')
