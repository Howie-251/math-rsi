import json,resource,subprocess,time
from pathlib import Path
D=Path(__file__).resolve().parent
start=time.process_time();initial=resource.getrusage(resource.RUSAGE_CHILDREN);wall=time.time()
def cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-start+r.ru_utime+r.ru_stime-initial.ru_utime-initial.ru_stime
P=json.loads((D.parents[1]/'ACTUAL_POINTS.json').read_text())['point_ids']
S=json.loads((D.parents[2]/'PARAMETERS.json').read_text())['spread_line_labels']
assert len(P)==33 and len(S)==50
C=[400*p+l for p in P for l in S]
(D/'center_input.h').write_text('constexpr int center_labels[1650]={'+','.join(map(str,C))+'};\n')
phases=[]
def call(args,name,limit):
    before=cpu()
    def cap():resource.setrlimit(resource.RLIMIT_CPU,(limit,limit+1))
    with (D/(name+'.stdout')).open('w') as out,(D/(name+'.stderr')).open('w') as err:
        p=subprocess.Popen(args,cwd=D,stdout=out,stderr=err,preexec_fn=cap)
        (D/'HANDLE.json').write_text(json.dumps({'pid':p.pid,'phase':name,'single_worker':True,'CPU_budget_seconds':180},indent=2)+'\n')
        rc=p.wait()
    phases.append({'phase':name,'returncode':rc,'CPU_seconds_including_driver':cpu()-before})
    return rc
rc=call(['g++','-std=c++17','-O2','verify.cpp','-o','verify'],'compile',15)
if rc==0:
    remaining=180-cpu()
    rc=call(['./verify','../../../graph_d64_D3_n160050.edges','../graphs',str(min(170,remaining-3))],'validate',min(175,int(remaining-1)))
result=None
if (D/'RESULT.json').exists():result=json.loads((D/'RESULT.json').read_text())
terminal={'status':'PASS' if rc==0 else 'PARTIAL_OR_FAILED','returncode':rc,'total_CPU_seconds_including_preparation_compile_source_R2_eight_bindings_max_BFS_and_driver_aggregation':cpu(),'wall_seconds':time.time()-wall,'CPU_budget_seconds':180,'single_worker':True,'all_children_terminal':True,'phases':phases,'result':result,'measurement_boundary':'One executable header preparation/compiler/validator-driver batch: acceptedsource parse once,1650R2-only predictions,eight whole-file bindings,onlymaxk8 all13200newroot ordinaryqueueBFS and aggregation. Interactive authoring/initial read-only inspection excluded.'}
(D/'TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n');print(json.dumps(terminal,indent=2));raise SystemExit(rc)
