#!/usr/bin/env python3
import csv
import json
from pathlib import Path
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parents[1]
start=time.process_time()
initial=resource.getrusage(resource.RUSAGE_CHILDREN)
wall=time.time()

def cpu():
    c=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-start+c.ru_utime+c.ru_stime-initial.ru_utime-initial.ru_stime

def mul(a,b):
    return (a%3*(b%3)+2*(a//3)*(b//3))%3+3*((a%3*(b//3)+a//3*(b%3))%3)

# Reuse accepted independent source measurements, never producer prediction caches.
rows={int(x['root']):x for x in csv.DictReader((SOURCE/'independent_acceptance/BFS_PREDICTION_VS_ACTUAL.csv').open())}
predictions=[]
for a in range(9):
    for b in range(9):
        center=a+9*b+81*mul(4,a)
        row=rows[center]
        hist=[int(row['actual_R'+str(d)]) for d in range(4)]
        assert hist==[1,54,2476,54331]
        predictions.append({'j':9*a+b,'newroot':56862+9*a+b,'center':center,'accepted_source_histogram':hist,'predicted_new_histogram':[1,54,hist[2]+1,hist[3]+80]})
(HERE/'BEFORE_EXECUTION_DISTANCE_PREDICTIONS.json').write_text(json.dumps(predictions,indent=2)+'\n')
phases=[]

def call(args,name,limit):
    before=cpu()
    def cap():resource.setrlimit(resource.RLIMIT_CPU,(limit,limit+1))
    with (HERE/(name+'.stdout')).open('w') as out,(HERE/(name+'.stderr')).open('w') as err:
        p=subprocess.Popen(args,cwd=HERE,stdout=out,stderr=err,preexec_fn=cap)
        (HERE/'HANDLE.json').write_text(json.dumps({'pid':p.pid,'phase':name,'single_worker':True,'total_CPU_budget_seconds':45},indent=2)+'\n')
        rc=p.wait()
    phases.append({'phase':name,'returncode':rc,'CPU_seconds_including_driver':cpu()-before})
    return rc

rc=call(['g++','-std=c++17','-O2','verify.cpp','-o','verify'],'compile',15)
if rc==0:
    rc=call(['./verify','../../graph_d54_D3_n56862.edges','../graph_d55_D3_n56943.edges'],'validate',min(25,int(45-cpu())))
result=None
if rc==0:
    result=json.loads((HERE/'validate.stdout').read_text())
    (HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
terminal={'status':'PASS' if rc==0 else 'FAILED','returncode':rc,'total_CPU_seconds_including_preparation_compile_validation_driver_aggregation':cpu(),'wall_seconds':time.time()-wall,'CPU_budget_seconds':45,'single_worker':True,'all_children_terminal':True,'phases':phases,'result':result,'measurement_boundary':'Executable Python preparation including inherited-source distance predictions, compilation, complete two-file binding and new-root BFS, aggregation. Interactive source authoring and initial read-only inspection are outside this executable-batch boundary.'}
(HERE/'TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
print(json.dumps(terminal,indent=2))
raise SystemExit(rc)
