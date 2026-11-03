from pathlib import Path
import json,os,resource,subprocess,time
out=Path(__file__).resolve().parent
started=time.process_time();child0=resource.getrusage(resource.RUSAGE_CHILDREN)
with (out/'compile.log').open('w') as log:
 result=subprocess.run(['g++','-O2','-std=c++17',str(out/'count_words.cpp'),'-o',str(out/'count_words')],stdout=log,stderr=subprocess.STDOUT)
child1=resource.getrusage(resource.RUSAGE_CHILDREN)
compile_cpu=(child1.ru_utime+child1.ru_stime)-(child0.ru_utime+child0.ru_stime)
assert result.returncode==0
def limit():resource.setrlimit(resource.RLIMIT_CPU,(3,3))
with (out/'native.log').open('w') as log:
 run=subprocess.run([str(out/'count_words')],stdout=log,stderr=subprocess.STDOUT,preexec_fn=limit,timeout=10)
child2=resource.getrusage(resource.RUSAGE_CHILDREN)
native_process_cpu=(child2.ru_utime+child2.ru_stime)-(child1.ru_utime+child1.ru_stime)
assert run.returncode==0
result=json.loads((out/'native.log').read_text());(out/'NATIVE_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
result.update({'status':'RAW_CAPACITY_PASSES' if result['minimum_raw_count']>=43 else 'RAW_CAPACITY_OBSTRUCTION','target_fiber_size':43,'prediction_supported':result['minimum_raw_count']>=43,'capacity_is_sufficient':False,'field_endpoint_evaluations':0,'graphs':0,'BFS':0,'solver_runs':0,'compile_CPU_seconds':compile_cpu,'native_process_CPU_seconds':native_process_cpu,'parent_CPU_seconds':time.process_time()-started,'native_CPU_hard_limit_seconds':3,'workers':1,'endpoint_encoding':'19*phase+normal19','scope':'Exact reduced-word count on the fixed342state projection only. No field graph or graph diameter.'})
(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
terminal={'status':result['status'],'prefix_count':result['prefix_count'],'minimum_raw_count':result['minimum_raw_count'],'prediction_supported':result['prediction_supported'],'compile_CPU_seconds':compile_cpu,'native_process_CPU_seconds':native_process_cpu,'graphs':0,'BFS':0}
(out/'terminal.json').write_text(json.dumps(terminal,indent=2)+'\n')
print(json.dumps(terminal),flush=True)
