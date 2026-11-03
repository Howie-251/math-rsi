#!/usr/bin/env python3
"""Compile once andproduce once;actualchildCPU shared300CPUstagebudget."""
import json
import math
import resource
import subprocess
import time
from pathlib import Path
HERE=Path(__file__).resolve().parent
def childcpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN);return r.ru_utime+r.ru_stime
def hardlimit(n):
    def apply():resource.setrlimit(resource.RLIMIT_CPU,(n,n))
    return apply

def main():
    assert not(HERE/'graph_d64_D3_n160050.edges').exists(),'onefixedcandidatealreadyexists'
    geometry=json.loads((HERE/'GQ_AXIOM_CHECK.json').read_text())
    assert geometry['status']=='PASS_COMPLETE_FIXED_GEOMETRY_READY_FOR_PRODUCTION'
    geom=geometry['CPU_seconds'];before=childcpu();wall=time.monotonic()
    command=['g++','-O3','-std=c++20','produce.cpp','-o','produce']
    with (HERE/'BUILD.log').open('w') as out:
        built=subprocess.run(command,cwd=HERE,stdout=out,stderr=subprocess.STDOUT,preexec_fn=hardlimit(30))
    buildcpu=childcpu()-before
    receipt={'compile_command':command,'compile_exit_code':built.returncode,'compile_CPU_seconds':buildcpu,'geometry_CPU_seconds':geom,'total_budget_CPU_seconds':300}
    assert built.returncode==0,receipt
    remaining=math.floor(300-geom-buildcpu)
    assert remaining>0
    command=[str(HERE/'produce'),str(geom),str(buildcpu)]
    before=childcpu()
    with (HERE/'PRODUCTION.log').open('w') as out:
        done=subprocess.run(command,cwd=HERE,stdout=out,stderr=subprocess.STDOUT,preexec_fn=hardlimit(remaining))
    receipt.update(production_command=command,production_exit_code=done.returncode,production_child_CPU_seconds=childcpu()-before,production_hard_CPU_seconds=remaining,compile_and_run_wall_seconds=time.monotonic()-wall,workers=1,candidate_generation_calls=1,source_BFS_runs=0)
    (HERE/'BUILD_RUN.json').write_text(json.dumps(receipt,indent=2)+'\n')
    assert done.returncode==0,receipt
    result=json.loads((HERE/'RESULT.json').read_text())
    result['total_measured_CPU_seconds_including_actual_child_receipt']=geom+buildcpu+receipt['production_child_CPU_seconds']
    (HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'n':result['n'],'m':result['m'],'degree_histogram':result['degree_histogram'],'current_complete_R2_checks':result['current_complete_R2_checks'],'production_CPU_seconds':receipt['production_child_CPU_seconds'],'total_CPU_seconds':result['total_measured_CPU_seconds_including_actual_child_receipt'],'graph_closed':True}))

if __name__=='__main__':main()
