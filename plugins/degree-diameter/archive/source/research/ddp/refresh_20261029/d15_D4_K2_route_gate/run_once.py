#!/usr/bin/env python3
"""One bounded R2 preparation / inherited-R3 T0 gate; no graph search."""
import json,math,os,resource,subprocess,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
SOURCE=ROOT/'research/ddp/more_graphs_20261027/d15_D4_current15552'
START=time.process_time();WALL=time.monotonic()
CHILD=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-START+r.ru_utime+r.ru_stime-CHILD.ru_utime-CHILD.ru_stime
def save(name,data):(HERE/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
assert not (HERE/'HANDLE.json').exists(),'This unique bounded gate already started.'
save('HANDLE.json',dict(status='PREPARING_ROUTE_GATE',driver_pid=os.getpid(),running=True,CPU_budget=10))
def run(command,name):
    remain=10-cpu();assert remain>1
    limit=max(1,math.floor(remain))
    def limits():resource.setrlimit(resource.RLIMIT_CPU,(limit,limit+1))
    before=resource.getrusage(resource.RUSAGE_CHILDREN)
    with (HERE/f'{name}.log').open('w') as log:
        p=subprocess.Popen(command,cwd=HERE,stdout=log,stderr=subprocess.STDOUT,preexec_fn=limits)
        rec=dict(command=command,pid=p.pid,driver_pid=os.getpid(),running=True,observation_timeouts=0)
        save(f'{name.upper()}_HANDLE.json',rec);print(json.dumps(rec),flush=True)
        while True:
            try:rc=p.wait(timeout=2);break
            except subprocess.TimeoutExpired:rec['observation_timeouts']+=1;save(f'{name.upper()}_HANDLE.json',rec)
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    rec.update(running=False,returncode=rc,CPU_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime)
    save(f'{name.upper()}_PROCESS_RESULT.json',rec)
    save(f'{name.upper()}_HANDLE.json',rec)
    if rc!=0:
        save('TERMINAL.json',dict(status='INPUT_OR_CPU_FAILURE_STOP',stage=name,returncode=rc,CPU_seconds=cpu(),running=False,solver_calls=0))
        raise SystemExit(rc if rc>0 else 1)
    return rec
compiled=run(['g++','-O3','-std=c++17','gate.cpp','-o','gate'],'compile')
native=run([str(HERE/'gate'),str(SOURCE/'source15552.header.edges'),str(SOURCE/'single_vertex_R3_cover/R3_MASKS.bin'),str(HERE)],'native')
result=json.loads((HERE/'NATIVE_RESULT.json').read_text())
result.update(driver_pid=os.getpid(),native_pid=native['pid'],native_returncode=native['returncode'],
    compile_CPU_seconds=compiled['CPU_seconds'],native_child_CPU_seconds=native['CPU_seconds'],
    aggregate_CPU_seconds=cpu(),wall_seconds=time.monotonic()-WALL,CPU_budget=10,
    input_R3=str(SOURCE/'single_vertex_R3_cover/R3_MASKS.bin'),source_file=str(SOURCE/'source15552.header.edges'),
    transpose_layout='15552 rows, each 11 uint64 little-endian; bit j follows FREE_ORDER, all648 columns retained',
    R2_cache_layout='uint32 header(648,15552,243), then648 rows: uint32 oldlabel plus243 uint64 closedR2',
    source_header_and_port_order_binding='Complete old freeport set equals cache labels; all labels degree14/spare1; all computed R2 subset inherited R3',
    running=False,pending=[],automatic_continuation=False)
assert result['aggregate_CPU_seconds']<10
for name in ['RESULT.json','TERMINAL.json','HANDLE.json']:save(name,result)
print(json.dumps(result),flush=True)
