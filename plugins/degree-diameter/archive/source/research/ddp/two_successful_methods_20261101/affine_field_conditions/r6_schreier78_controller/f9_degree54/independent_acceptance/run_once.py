#!/usr/bin/env python3
import json
import os
from pathlib import Path
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]
start_cpu=time.process_time()
child_start=resource.getrusage(resource.RUSAGE_CHILDREN)
wall=time.time()

def cpu():
    c=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-start_cpu+c.ru_utime+c.ru_stime-child_start.ru_utime-child_start.ru_stime

def fmt(x):
    if isinstance(x,list):return '{{'+','.join(fmt(y) for y in x)+'}}'
    return str(x)

controller=json.loads((BASE/'PARAMETERS.json').read_text())['controller']
chart=json.loads((BASE.parent/'r6_f9_projective_halves/cross_port_extension/PARAMETERS.json').read_text())
matrices=[chart['cross_port_matrix_by_source_target'][k] for k in ['0,1','1,0','2,3','3,2']]
matrices += [chart['self_port_plus'][4],chart['self_port_minus'][4],chart['self_port_plus'][5],chart['self_port_minus'][5]]
text='constexpr array<array<int,6>,78> declared_controller='+fmt(controller)+';\n'
text+='constexpr array<M,8> matrices='+fmt(matrices)+';\n'
text+='constexpr array<V,6> directions='+fmt(chart['port_vectors'])+';\n'
(HERE/'literal_inputs.h').write_text(text)
phases=[]
def call(args,name,limit):
    before=cpu()
    def setlimit():resource.setrlimit(resource.RLIMIT_CPU,(limit,limit+1))
    with (HERE/(name+'.stdout')).open('w') as out,(HERE/(name+'.stderr')).open('w') as err:
        proc=subprocess.Popen(args,cwd=HERE,stdout=out,stderr=err,preexec_fn=setlimit)
        (HERE/'HANDLE.json').write_text(json.dumps({'pid':proc.pid,'phase':name,'single_worker':True,'total_cpu_budget_seconds':120},indent=2)+'\n')
        rc=proc.wait()
    phase={'phase':name,'returncode':rc,'CPU_seconds_including_driver':cpu()-before}
    phases.append(phase)
    return rc

rc=call(['g++','-std=c++17','-O2','verify.cpp','-o','verify'],'compile',30)
if rc==0:
    remaining=int(120-cpu())
    rc=call(['./verify','../graph_d54_D3_n56862.edges'],'validate',min(85,remaining))
result=None
if rc==0:
    result=json.loads((HERE/'validate.stdout').read_text())
    (HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
terminal={'status':'PASS' if rc==0 else 'FAILED','returncode':rc,'total_CPU_seconds_including_preparation_compile_validation_driver_aggregation':cpu(),'wall_seconds':time.time()-wall,'total_cpu_budget_seconds':120,'single_worker':True,'all_children_terminal':True,'phases':phases,'result':result,'measurement_boundary':'Python preparation/input-header creation, compilation, validator including all literal input and BFS, aggregation. Interactive source authoring and read-only preparatory inspection are outside this measured executable batch.'}
(HERE/'TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
print(json.dumps(terminal,indent=2))
raise SystemExit(rc)
