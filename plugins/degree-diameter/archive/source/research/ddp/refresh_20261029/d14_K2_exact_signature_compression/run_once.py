#!/usr/bin/env python3
from pathlib import Path
import json
import math
import os
import resource
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
PROJECT=HERE.parents[3]
BASE=HERE.parent/'d14_D5_K2_route_gate'
OLD=PROJECT/'research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/allfree_cover_probe'
assert sys.byteorder=='little'
assert not (HERE/'HANDLE.json').exists(), 'Once-only representation gate has already started.'
start=time.process_time();child0=resource.getrusage(resource.RUSAGE_CHILDREN)
child0=child0.ru_utime+child0.ru_stime
def used():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-start+r.ru_utime+r.ru_stime-child0
def save(name,data):(HERE/name).write_text(json.dumps(data,indent=2)+'\n')
save('HANDLE.json',{'status':'PREPARING','driver_pid':os.getpid(),'CPU_budget':10,'running':True})
compile_command=['g++','-O2','-std=c++17',str(HERE/'compress.cpp'),'-o',str(HERE/'compress')]
compilation=subprocess.run(compile_command,capture_output=True,text=True)
(HERE/'compile.log').write_text(compilation.stdout+compilation.stderr)
assert compilation.returncode==0
compile_cpu=used()
remaining=10-used()-0.15
assert remaining>0.5
def limit():resource.setrlimit(resource.RLIMIT_CPU,(math.ceil(remaining),math.ceil(remaining)))
command=[str(HERE/'compress'),str(BASE/'allfree_R3.u64le.bin'),str(OLD/'allfree_R4.u64le.bin'),
         str(BASE/'FREE_SPARES.txt'),str(HERE),str(remaining)]
with (HERE/'native.log').open('w') as out:
    process=subprocess.Popen(command,stdout=out,stderr=subprocess.STDOUT,preexec_fn=limit)
    handle={'status':'RUNNING_EXACT_EQUALITY','driver_pid':os.getpid(),'pid':process.pid,
            'command':command,'compile_CPU_seconds':compile_cpu,'native_CPU_allowance':remaining,'running':True}
    save('HANDLE.json',handle);print(json.dumps(handle),flush=True)
    code=process.wait()
native=json.loads((HERE/'NATIVE_RESULT.json').read_text()) if (HERE/'NATIVE_RESULT.json').exists() else {'status':'TERMINATED_WITHOUT_NATIVE_RESULT'}
result=dict(native,returncode=code,compile_CPU_seconds=compile_cpu,aggregate_CPU_seconds=used(),
            CPU_budget=10,running=False,solver_calls=0,new_graphs=0,pending=[])
for name in ['RESULT.json','TERMINAL.json','HANDLE.json']:save(name,result)
print(json.dumps(result),flush=True)
