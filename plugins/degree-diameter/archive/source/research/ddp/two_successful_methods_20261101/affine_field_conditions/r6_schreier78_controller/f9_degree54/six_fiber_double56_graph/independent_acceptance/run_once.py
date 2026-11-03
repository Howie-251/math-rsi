import json,resource,subprocess,time
from pathlib import Path

D=Path(__file__).resolve().parent
start=time.process_time();initial=resource.getrusage(resource.RUSAGE_CHILDREN);wall=time.time()
def cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-start+r.ru_utime+r.ru_stime-initial.ru_utime-initial.ru_stime
phases=[]
def call(args,name,limit):
    before=cpu()
    def cap():resource.setrlimit(resource.RLIMIT_CPU,(limit,limit+1))
    with (D/(name+'.stdout')).open('w') as out,(D/(name+'.stderr')).open('w') as err:
        p=subprocess.Popen(args,cwd=D,stdout=out,stderr=err,preexec_fn=cap)
        (D/'HANDLE.json').write_text(json.dumps({'pid':p.pid,'phase':name,'single_worker':True,'CPU_budget_seconds':45},indent=2)+'\n')
        rc=p.wait()
    phases.append({'phase':name,'returncode':rc,'CPU_seconds_including_driver':cpu()-before})
    return rc
rc=call(['g++','-std=c++17','-O2','verify.cpp','-o','verify'],'compile',15)
if rc==0:rc=call(['./verify','../../graph_d54_D3_n56862.edges','../graph_d56_D3_n57834.edges'],'validate',min(25,int(45-cpu())))
result=None
if rc==0:
    result=json.loads((D/'validate.stdout').read_text())
    (D/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
terminal={'status':'PASS' if rc==0 else 'FAILED','returncode':rc,'total_CPU_seconds_including_compile_source_R2_prediction_binding_new_BFS_and_driver_aggregation':cpu(),'wall_seconds':time.time()-wall,'CPU_budget_seconds':45,'single_worker':True,'all_children_terminal':True,'phases':phases,'result':result,'measurement_boundary':'One executable driver/compile/validator batch, including486sourceR2-only local predictions before newfile input, two complete literal graph reads, all972newroot BFS and aggregation. Interactive source authoring/initial read-only inspection excluded.'}
(D/'TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
print(json.dumps(terminal,indent=2))
raise SystemExit(rc)
