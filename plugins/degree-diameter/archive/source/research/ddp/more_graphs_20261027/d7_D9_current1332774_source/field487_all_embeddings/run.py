from pathlib import Path
import json,resource,subprocess,time
out=Path(__file__).resolve().parent
before=resource.getrusage(resource.RUSAGE_CHILDREN);started=time.process_time()
with (out/'compile.log').open('w') as log:compile_run=subprocess.run(['g++','-O3','-std=c++17',str(out/'probe.cpp'),'-o',str(out/'probe')],stdout=log,stderr=subprocess.STDOUT)
after_compile=resource.getrusage(resource.RUSAGE_CHILDREN)
compile_cpu=(after_compile.ru_utime+after_compile.ru_stime)-(before.ru_utime+before.ru_stime)
assert compile_run.returncode==0
def limit():resource.setrlimit(resource.RLIMIT_CPU,(60,60))
with (out/'native.log').open('w') as log:
 try:run=subprocess.run([str(out/'probe'),str(out)],stdout=log,stderr=subprocess.STDOUT,preexec_fn=limit,timeout=300);exitcode=run.returncode
 except subprocess.TimeoutExpired:exitcode='WALL_TIMEOUT'
after=resource.getrusage(resource.RUSAGE_CHILDREN)
cpu=(after.ru_utime+after.ru_stime)-(after_compile.ru_utime+after_compile.ru_stime)
if exitcode==0:r=json.loads((out/'NATIVE_RESULT.json').read_text())
else:
 cp=json.loads((out/'checkpoint.json').read_text());k=cp.get('completed_cases',0);r={'status':'UNKNOWN_CURSOR_AFTER_PROCESS_LIMIT','embeddings_total':18,'embeddings_processed':k,'actual_implicit_graphs_complete':k,'hits':int((out/'HIT.json').exists()),'next_cursor':k,'untested':18-k,'actual_global_D':None,'source_BFS':0,'checkpoint':cp}
r.update({'target_n':1498986,'target_m':5246451,'target_Delta':7,'target_D':9,'savedL':1332774,'prediction':'SUPPORTED_PRODUCER_HIT_PENDING_PARENT' if r.get('hits') else ('REFUTED_COMPLETE_ALL18' if r.get('embeddings_processed')==18 else 'UNKNOWN'),'receipt':{'native_exit_code':exitcode,'compile_CPU_seconds_separate':compile_cpu,'native_process_CPU_seconds':cpu,'driver_CPU_seconds':time.process_time()-started,'native_CPU_hard_limit_seconds':60,'workers':1},'live_handle':None})
(out/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');(out/'terminal.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r),flush=True)
