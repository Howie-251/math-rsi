#!/usr/bin/env python3
"""Single complete K2 attempt for the new (15,4) source."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import json
from pathlib import Path
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[3]
N, K, W = 15552, 648, 11

def save(name,data):
    (HERE/name).write_text(json.dumps(data,indent=2)+'\n')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--solve',action='store_true',required=True)
    parser.parse_args()
    assert not (HERE/'SOLVER_HANDLE.json').exists(), 'Single batch already started.'
    model = json.loads((HERE/'MODEL.json').read_text())
    assert model['status'] == 'D15_D4_ALL648_FULL15552_K2_CNF_PREPARED_NOT_SOLVED'
    assert (model['all_variables'],model['total_clauses']) == (19440,69306)
    assert model['complete_all_ports'] and model['complete_all_targets']
    route = json.loads((HERE.parent/'d15_D4_K2_route_gate/RESULT.json').read_text())
    prior = model['prepare_CPU_seconds'] + route['aggregate_CPU_seconds']
    start = time.process_time()
    wall = time.monotonic()
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    child0 = before.ru_utime+before.ru_stime
    def total():
        r=resource.getrusage(resource.RUSAGE_CHILDREN)
        return prior+time.process_time()-start+r.ru_utime+r.ru_stime-child0
    def limit():
        resource.setrlimit(resource.RLIMIT_CPU,(121,121))
    command = [str(PROJECT/'.tools/lean-4.24.0-linux/bin/cadical'),'-q','-t','120',
        '-w',str(HERE/'candidate.sol'),str(HERE/'model.cnf')]
    with (HERE/'solver.stdout').open('w') as out:
        p = subprocess.Popen(command,stdout=out,stderr=subprocess.STDOUT,preexec_fn=limit)
        handle = dict(status='RUNNING_SINGLE_D15_D4_K2',driver_pid=os.getpid(),pid=p.pid,
            command=command,running=True,solver_window=120,solver_CPU_hard_limit=121,
            whole_CPU_budget=150,prior_route_and_preparation_CPU=prior,max_calls=1,
            scope='All648 literal freeports and all15552 targets; adjacent two-helper operation')
        save('SOLVER_HANDLE.json',handle)
        print(json.dumps(handle),flush=True)
        observations=0
        while True:
            try:
                code=p.wait(timeout=5)
                break
            except subprocess.TimeoutExpired:
                observations+=1
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    solver_cpu=r.ru_utime+r.ru_stime-child0
    result=dict(status='UNKNOWN',returncode=code,solver_pid=p.pid,driver_pid=os.getpid(),
        command=command,solver_CPU_seconds=solver_cpu,observation_timeouts=observations,
        same_PID_waited_to_exit=True,actual_solver_calls=1,
        all_literal_ports=K,complete_old_targets=N,
        source_graph_reads=0,BFS_runs=0,graphs_generated=0,running=False,
        automatic_continuation=False,pending=[])
    if code==20:
        result.update(status='RAW_UNSAT_D15_D4_ADJACENT_K2_UNCERTIFIED',
            certificate='none; raw result only, not a general15,4 exclusion')
    elif code==10:
        import numpy as np
        values={}
        for line in (HERE/'candidate.sol').read_text().splitlines():
            if line.startswith('v '):
                for token in line[2:].split():
                    x=int(token)
                    if 1<=abs(x)<=2*K:values[abs(x)]=x>0
        assert len(values)==2*K
        A=[j for j in range(K) if values[j+1]]
        B=[j for j in range(K) if values[K+j+1]]
        assert len(A)<=14 and len(B)<=14 and not(set(A)&set(B))
        def mask(ids):
            m=np.zeros(W,dtype=np.uint64)
            for j in ids:m[j//64]|=np.uint64(1)<<np.uint64(j%64)
            return m
        inp=json.loads((HERE/'INPUT_SCOPE.json').read_text())
        r2=np.fromfile(inp['input_R2'],dtype='<u8').reshape(N,W)
        r3=np.fromfile(inp['input_R3'],dtype='<u8').reshape(N,W)
        ma,mb=mask(A),mask(B)
        ownA=np.any(r3&ma,axis=1);ownB=np.any(r3&mb,axis=1)
        ca=ownA|np.any(r2&mb,axis=1)
        cb=ownB|np.any(r2&ma,axis=1)
        assert bool(ca.all()) and bool(cb.all()), 'Complete model/cache binding error.'
        ports=json.loads((HERE/'SELECTOR_MAP.json').read_text())['ports']
        assert len(ports)==K
        oldA=sorted(ports[j]['old_label'] for j in A)
        oldB=sorted(ports[j]['old_label'] for j in B)
        assert len(set(oldA))==len(A) and len(set(oldB))==len(B)
        assert not(set(oldA)&set(oldB))
        hit=dict(status='FULL_CACHED_D15_D4_K2_HIT_PENDING_ROOT_ACCEPTANCE',
            source_n=N,source_m=116316,new_n=N+2,new_m=116316+len(A)+len(B)+1,
            target_degree=15,target_diameter=4,helper_internal_edge=[N,N+1],
            A_old_pins=oldA,B_old_pins=oldB,A_columns=A,B_columns=B,
            full_old_target_count_per_root=N,coverage_misses=[int((~ca).sum()),int((~cb).sum())],
            standalone_R3_full=[bool(ownA.all()),bool(ownB.all())],
            source_diameter_inherited=True,independent_literal_acceptance_pending=True)
        save('HIT_PARAMETERS.json',hit)
        result.update(status=hit['status'],pending=['root independent literal graph acceptance'])
    result.update(whole_CPU_seconds=total(),prior_route_and_preparation_CPU=prior,
        whole_CPU_budget=150,wall_seconds=time.monotonic()-wall)
    assert result['whole_CPU_seconds']<150
    save('SOLVER_TERMINAL.json',result);save('SOLVER_HANDLE.json',result)
    print(json.dumps(result),flush=True)

if __name__=='__main__':main()
