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
        (D/'HANDLE.json').write_text(json.dumps({'pid':p.pid,'phase':name,'single_worker':True,'CPU_budget_seconds':150},indent=2)+'\n')
        rc=p.wait()
    phases.append({'phase':name,'returncode':rc,'CPU_seconds_including_driver':cpu()-before})
    return rc
rc=call(['g++','-std=c++17','-O2','verify.cpp','-o','verify'],'compile',15)
if rc==0:
    remaining=150-cpu()
    rc=call(['./verify','../../graph_d54_D3_n56862.edges','../graphs',str(min(140,remaining-2))],'validate',min(145,int(remaining-1)))
result=None
if (D/'RESULT.json').exists():result=json.loads((D/'RESULT.json').read_text())
terminal={'status':'PASS' if rc==0 else 'PARTIAL_OR_FAILED','returncode':rc,'total_CPU_seconds_including_compile_source_R2_five_bindings_new_BFS_and_driver_aggregation':cpu(),'wall_seconds':time.time()-wall,'CPU_budget_seconds':150,'single_worker':True,'all_children_terminal':True,'phases':phases,'result':result,'measurement_boundary':'One executable compiler/validator driver batch: one acceptedsource parse and810R2-only predictions, five new literal file bindings, all12150newroot BFS, pilot projection and aggregation. Interactive authoring/initial read-only inspection excluded.'}
(D/'TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
print(json.dumps(terminal,indent=2))
raise SystemExit(rc)
