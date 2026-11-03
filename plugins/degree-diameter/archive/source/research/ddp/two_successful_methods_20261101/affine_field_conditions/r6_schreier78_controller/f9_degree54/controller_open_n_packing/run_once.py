import json,resource,subprocess,time
from pathlib import Path

D=Path(__file__).resolve().parent
start=time.process_time();initial=resource.getrusage(resource.RUSAGE_CHILDREN);wall=time.time()
def cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-start+r.ru_utime+r.ru_stime-initial.ru_utime-initial.ru_stime
declared=json.loads((D.parents[1]/'PARAMETERS.json').read_text())['controller']
assert len(declared)==78 and all(len(row)==6 for row in declared)
header='constexpr int literal_controller[78][6]={'+','.join('{'+','.join(map(str,row))+'}' for row in declared)+'};\n'
(D/'controller_input.h').write_text(header)
phases=[]
def call(args,name,limit):
    before=cpu()
    def cap():resource.setrlimit(resource.RLIMIT_CPU,(limit,limit+1))
    with (D/(name+'.stdout')).open('w') as out,(D/(name+'.stderr')).open('w') as err:
        p=subprocess.Popen(args,cwd=D,stdout=out,stderr=err,preexec_fn=cap)
        (D/'HANDLE.json').write_text(json.dumps({'pid':p.pid,'phase':name,'CPU_budget_seconds':20,'single_worker':True},indent=2)+'\n')
        rc=p.wait()
    phases.append({'phase':name,'returncode':rc,'CPU_seconds_including_driver':cpu()-before})
    return rc
rc=call(['g++','-std=c++17','-O3','search.cpp','-o','search'],'compile',5)
if rc==0:
    remaining=20-cpu()
    assert remaining>1
    internal=min(16.5,remaining-0.75)
    rc=call(['./search',str(internal)],'search',max(1,int(remaining-0.25)))
result=None
if rc==0:result=json.loads((D/'SEARCH_RESULT.json').read_text())
terminal={'status':'COMPLETED' if rc==0 else 'PROCESS_FAILED_OR_LIMIT','returncode':rc,'total_CPU_seconds_including_preparation_compile_search_driver_aggregation':cpu(),'wall_seconds':time.time()-wall,'CPU_budget_seconds':20,'single_worker':True,'all_children_terminal':True,'search_calls':1 if len(phases)==2 else 0,'phases':phases,'result':result,'measurement_boundary':'One executable Python input-header preparation/compilation/exactsearch/aggregation batch. Interactive authoring and initial read-only inspection excluded.'}
(D/'TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
print(json.dumps(terminal,indent=2))
raise SystemExit(rc)
