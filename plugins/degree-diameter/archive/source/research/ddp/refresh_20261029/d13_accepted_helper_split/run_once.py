"""One CPU-bounded native gate. No source all-root revalidation or Wiki write."""
from pathlib import Path
from datetime import datetime, timezone
import json
import math
import os
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
start_self = time.process_time()
start_child = resource.getrusage(resource.RUSAGE_CHILDREN)
start_wall = time.monotonic()
source = ROOT/'research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/continuation/graphs/graph_d13_D5_n51457.edges'
cal = json.loads((HERE.parent/'d13_D5_static_pool_calibration/RESULT.json').read_text())
assert cal['failed_sets'] == cal['incompatible_pairs'] == cal['port_overloads'] == 0
assert len(cal['sets']) == 40 and cal['unordered_pair_count'] == 780
assert cal['new_new_edges'] == 0
handle = dict(status='RUNNING',driver_pid=os.getpid(),started_UTC=datetime.now(timezone.utc).isoformat(),
    scope='All40 accepted helpers, exact adjacent split PropertyB gate',whole_CPU_budget=10,
    workers=1,source=str(source.relative_to(ROOT)),pending=['compile','40-root gate'])
(HERE/'HANDLE.json').write_text(json.dumps(handle,indent=2)+'\n')


def used():
    child = resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-start_self+child.ru_utime+child.ru_stime-start_child.ru_utime-start_child.ru_stime


with (HERE/'compile.log').open('w') as out:
    subprocess.run(['g++','-O2','-std=c++17',str(HERE/'check.cpp'),'-o',str(HERE/'check')],
                   stdout=out,stderr=subprocess.STDOUT,check=True)
compile_CPU = used()
remaining = 10-compile_CPU-.15
assert remaining > 0


def limits():
    resource.setrlimit(resource.RLIMIT_CPU,(max(1,math.ceil(remaining)),max(2,math.ceil(remaining)+1)))


with (HERE/'native.stdout').open('w') as out:
    process = subprocess.Popen([str(HERE/'check'),str(source),str(HERE),str(remaining-.05)],
        stdout=out,stderr=subprocess.STDOUT,preexec_fn=limits)
    handle.update(child_pid=process.pid,pending=['40-root gate'])
    (HERE/'HANDLE.json').write_text(json.dumps(handle,indent=2)+'\n')
    returncode = process.wait(timeout=20)
aggregate = used()
assert returncode == 0
result = json.loads((HERE/'NATIVE_RESULT.json').read_text())
cases = json.loads((HERE/'CASES.json').read_text())
result.update(completed_UTC=datetime.now(timezone.utc).isoformat(),driver_pid=os.getpid(),
    child_pid=process.pid,returncode=returncode,compile_and_prepare_CPU_seconds=compile_CPU,
    whole_CPU_seconds=aggregate,whole_CPU_budget=10,wall_seconds=time.monotonic()-start_wall,
    prediction='At least one of40 accepted helpers admits this adjacent split',
    prediction_result='SUPPORTED_CANDIDATE_PENDING_ACCEPTANCE' if result['passing_h']>=0 else 'REFUTED' if result['objects_tested']==40 else 'UNKNOWN',
    singleton_rejected_objects=sum(c['singleton_target']>=0 for c in cases),
    exhaustive_partition_rejected_objects=sum(c['singleton_target']<0 and c['passing_A_mask']<0 for c in cases),
    old_old_D5_inherited_from_static40_and780=True,static40_or780_recomputed=False,
    solver_calls=0,accepted_graphs=0,new_record_claimed=False,running=False,pending=[])
assert aggregate <= 10
if result['passing_h']>=0:
    c=cases[-1];A=[v for i,v in enumerate(c['neighbors'])if c['passing_A_mask']&(1<<i)]
    B=[v for i,v in enumerate(c['neighbors'])if not c['passing_A_mask']&(1<<i)]
    params=dict(source=str(source.relative_to(ROOT)),n=51458,m=324864,source_h=c['h'],new_vertex=51457,
        neighbors_A=A,neighbors_B=B,join_edge=[c['h'],51457],old_port_loads_preserved=True,
        maximum_degree_at_most=13,static_old_old_D5_inherited=True,
        PropertyB_all_distance5_supports_pass=True,independent_acceptance_pending=True)
    (HERE/'PARAMETERS.json').write_text(json.dumps(params,indent=2)+'\n')
(HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(HERE/'TERMINAL.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
