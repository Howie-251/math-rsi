import json, os, pathlib, resource, subprocess, time
D=pathlib.Path(__file__).resolve().parent
ROOT=D.parents[5]
# Fixed case bill: includes read-only history/metadata gate and all visible preparation.
prior=0.529389544
prep=0.5
cap=20.0
start=time.process_time(); wall=time.time()
os.chdir(D)
def child(cmd, log, limit):
    before=resource.getrusage(resource.RUSAGE_CHILDREN)
    def bounded():
        resource.setrlimit(resource.RLIMIT_CPU,(max(1,int(limit)),max(2,int(limit)+1)))
        resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
    with open(log,'w') as out:
        p=subprocess.Popen(cmd,stdout=out,stderr=subprocess.STDOUT,preexec_fn=bounded)
        handle={'pid':p.pid,'argv':cmd,'start_utc':time.strftime('%Y-%m-%d %H:%M:%S UTC',time.gmtime()),'case_cpu_cap':cap,'prior_read_cpu':prior,'new_prep_charge':prep}
        (D/'DRIVER_HANDLE.json').write_text(json.dumps(handle,indent=2)+'\n')
        code=p.wait()
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    return code,(after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime)
compile_code, compile_cpu=child(['g++','-O2','-std=c++17','run_once.cpp','-o','run_once'], 'COMPILE.log',5)
num_code=None; numeric_cpu=0.0
if compile_code==0:
    remaining=cap-prior-prep-compile_cpu-(time.process_time()-start)-0.6
    soft=max(0.1,remaining-1.0)
    source=ROOT/'more_graphs_20261027/d3_D10_current1250_source/source1250.edges'
    # ROOT here is ddp; no source traversal is performed by this driver.
    num_code,numeric_cpu=child([str(D/'run_once'),str(source),str(soft)],'RUN.log',max(1,int(remaining)))
actual_parent=time.process_time()-start
bill=prior+prep+compile_cpu+numeric_cpu+actual_parent
num_path=D/'NUMERIC_RESULT.json'
result=json.loads(num_path.read_text()) if num_path.exists() else {'status':'UNKNOWN_EXECUTION_FAILURE'}
result.update({'case_cpu_cap':cap,'prior_read_cpu':prior,'new_prep_charge':prep,'compile_exit':compile_code,'compile_cpu':compile_cpu,'numeric_exit':num_code,'numeric_actual_child_cpu':numeric_cpu,'driver_actual_cpu':actual_parent,'cumulative_case_cpu':bill,'source_D10_validation_bfs':0,'new_graph_count':0,'new_parameter_count':0,'new_Lean_count':0})
(D/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
term={'status':result['status'],'terminal':True,'cpu_seconds':bill,'cpu_cap':cap,'compile_exit':compile_code,'numeric_exit':num_code,'wall_seconds':time.time()-wall,'source_parse_count':result.get('source_parse_count',0),'source_D10_validation_bfs':0,'root_acceptance':'PENDING_PARENT_DISPOSITION','no_automatic_continuation':True}
(D/'TERMINAL.json').write_text(json.dumps(term,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
