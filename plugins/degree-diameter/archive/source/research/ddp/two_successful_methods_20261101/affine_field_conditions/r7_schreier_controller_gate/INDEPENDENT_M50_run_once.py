import json,resource,subprocess,time
from pathlib import Path
D=Path(__file__).resolve().parent
start=time.process_time();initial=resource.getrusage(resource.RUSAGE_CHILDREN);wall=time.time()
def cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-start+r.ru_utime+r.ru_stime-initial.ru_utime-initial.ru_stime
phases=[]
for args,name,limit in [(['g++','-std=c++17','-O2','INDEPENDENT_M50_MOD10.cpp','-o','INDEPENDENT_M50_MOD10'],'compile',3),(['./INDEPENDENT_M50_MOD10'],'joint_mod10',max(1,int(5-cpu()-0.2)))]:
    if name=='joint_mod10':limit=max(1,int(5-cpu()-0.2))
    before=cpu()
    def cap():resource.setrlimit(resource.RLIMIT_CPU,(limit,limit+1))
    with (D/('INDEPENDENT_M50_'+name+'.stdout')).open('w') as out,(D/('INDEPENDENT_M50_'+name+'.stderr')).open('w') as err:
        p=subprocess.Popen(args,cwd=D,stdout=out,stderr=err,preexec_fn=cap);rc=p.wait()
    phases.append({'phase':name,'returncode':rc,'CPU_seconds_including_driver':cpu()-before})
    if rc:break
result=None
if not rc:
    result=json.loads((D/'INDEPENDENT_M50_joint_mod10.stdout').read_text())
    (D/'INDEPENDENT_M50_MOD10_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
terminal={'status':'COMPLETE' if not rc else 'FAILED','returncode':rc,'total_CPU_seconds_including_compile_joint_check_and_driver_aggregation':cpu(),'wall_seconds':time.time()-wall,'CPU_budget_seconds':5,'single_worker':True,'all_children_terminal':True,'phases':phases,'result':result,'measurement_boundary':'One executable compilation/jointCRT-charactercheck/driveraggregation batch; source authoring/read-only inspection outside.'}
(D/'INDEPENDENT_M50_TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n');print(json.dumps(terminal,indent=2));raise SystemExit(rc)
