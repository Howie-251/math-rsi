import json,pathlib,resource,subprocess,time
P=pathlib.Path(__file__).resolve().parent;START=time.process_time();WALL=time.monotonic();r0=resource.getrusage(resource.RUSAGE_CHILDREN);C0=r0.ru_utime+r0.ru_stime
assert (P/'PREPARE_TERMINAL.json').exists() and not (P/'MIP_TERMINAL.json').exists()
assert not (P/'MIP_RESULT.json').exists()
with (P/'mip.stdout').open('w') as out,(P/'mip.stderr').open('w') as err:
 proc=subprocess.Popen(['python','-u',str(P/'mip_once.py')],cwd=P,stdout=out,stderr=err)
 (P/'LIVE_HANDLE.json').write_text(json.dumps({'status':'RUNNING_ONE_MIP','pid':proc.pid,'MIP_calls':1,'solver_seconds':25,'worker_CPU_soft_hard':[29,30]},indent=2)+'\n');print(json.dumps({'status':'RUNNING_ONE_MIP','pid':proc.pid}),flush=True)
 try:code=proc.wait(timeout=40)
 except subprocess.TimeoutExpired:proc.kill();code=proc.wait()
r1=resource.getrusage(resource.RUSAGE_CHILDREN);CPU=r1.ru_utime+r1.ru_stime-C0
term={'status':'TERMINAL','pid':proc.pid,'exit_code':code,'child_CPU_seconds':CPU,'driver_CPU_seconds':time.process_time()-START,'aggregate_CPU_seconds':CPU+time.process_time()-START,'wall_seconds':time.monotonic()-WALL,'MIP_calls':1,'LP_calls':0,'result_exists':(P/'MIP_RESULT.json').exists()}
(P/'MIP_TERMINAL.json').write_text(json.dumps(term,indent=2)+'\n');(P/'LIVE_HANDLE.json').write_text(json.dumps(term,indent=2)+'\n');print(json.dumps(term),flush=True)
if term['result_exists']:print((P/'MIP_RESULT.json').read_text(),flush=True)
