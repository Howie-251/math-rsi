#!/usr/bin/env python3
"""One complete all-group, all-target K2 attempt; separate from older batches."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
from collections import Counter
import json
import resource
import subprocess
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[3]
G, W = 3589, 57

def save(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2)+'\n')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--solve', action='store_true', required=True)
    parser.parse_args()
    assert not (HERE/'SOLVER_HANDLE.json').exists(), 'One batch already started.'
    assert not (HERE/'SOLVER_TERMINAL.json').exists()
    model = json.loads((HERE/'MODEL.json').read_text())
    assert model['status'] == 'FULL_ALLGROUP_FULLTARGET_PREPARED_NOT_SOLVED'
    assert model['complete_all_groups'] and model['complete_all_targets']
    assert not model['LP_support_restriction']
    assert (model['exact_groups'],model['variables'],model['clauses']) == (3589,100492,385396)
    start = time.process_time()
    wall = time.monotonic()
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    child_start = before.ru_utime + before.ru_stime
    prior = 90.0  # Charge the full preparation cap; original driver self CPU is unrecorded.
    measured_prepare = model['accounted_CPU_seconds']
    def total_cpu():
        r = resource.getrusage(resource.RUSAGE_CHILDREN)
        return prior + time.process_time()-start + r.ru_utime+r.ru_stime-child_start
    def limit():
        resource.setrlimit(resource.RLIMIT_CPU,(301,301))
    solver = PROJECT/'.tools/lean-4.24.0-linux/bin/cadical'
    command = [str(solver),'-q','-t','300','-w',str(HERE/'candidate.sol'),str(HERE/'model.cnf')]
    with (HERE/'solver.stdout').open('w') as out:
        process = subprocess.Popen(command,stdout=out,stderr=subprocess.STDOUT,preexec_fn=limit)
        handle = dict(status='RUNNING_SINGLE_INTEGER_CALL',driver_pid=os.getpid(),pid=process.pid,
            command=command,running=True,solver_window=300,solver_CPU_hard_limit=301,
            whole_CPU_budget=420,prior_preparation_CPU=prior,max_calls=1,
            pool_scope='All3589 exact groups and full94186 targets of fixed adjacent-K2 operation')
        save('SOLVER_HANDLE.json',handle)
        print(json.dumps(handle),flush=True)
        observations = 0
        while True:
            try:
                code = process.wait(timeout=5)
                break
            except subprocess.TimeoutExpired:
                observations += 1
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    solver_cpu = after.ru_utime+after.ru_stime-child_start
    result = dict(status='UNKNOWN',returncode=code,solver_pid=process.pid,driver_pid=os.getpid(),
        command=command,solver_CPU_seconds=solver_cpu,observation_timeouts=observations,
        same_PID_waited_to_exit=True,actual_solver_calls=1,
        complete_source_targets_encoded=94186,selected_groups=G,
        source_graph_reads=0,BFS_runs=0,graphs_generated=0,
        running=False,automatic_continuation=False,pending=[])
    if code == 20:
        result['status'] = 'RAW_UNSAT_ALLGROUP_K2_UNCERTIFIED'
        result['UNSAT_certificate'] = 'none; raw outcome only, no strict exclusion before certificate/encoding audit'
    elif code == 10:
        import numpy as np
        values = {}
        for line in (HERE/'candidate.sol').read_text().splitlines():
            if line.startswith('v '):
                for token in line[2:].split():
                    literal = int(token)
                    if 1 <= abs(literal) <= 2*G:
                        values[abs(literal)] = literal > 0
        assert len(values) == 2*G
        groups = json.loads((HERE/'SELECTOR_MAP.json').read_text())['groups']
        A = [j for j in range(G) if values[j+1]]
        B = [j for j in range(G) if values[G+1+j]]
        assert len(A) <= 13 and len(B) <= 13
        assert all((j in A)+(j in B) <= groups[j]['two_helper_capacity'] for j in range(G))
        def mask(indices):
            words = np.zeros(W,dtype=np.uint64)
            for j in indices:
                words[j//64] |= np.uint64(1) << np.uint64(j%64)
            return words
        info = json.loads((HERE/'INPUT.json').read_text())
        r3 = np.fromfile(info['R3_file'],dtype='<u8').reshape(94186,W)
        r4 = np.fromfile(info['R4_file'],dtype='<u8').reshape(94186,W)
        ma,mb = mask(A),mask(B)
        a4 = np.any(r4&ma,axis=1)
        b4 = np.any(r4&mb,axis=1)
        coverA = a4 | np.any(r3&mb,axis=1)
        coverB = b4 | np.any(r3&ma,axis=1)
        assert bool(coverA.all()) and bool(coverB.all()), 'Full-target model/cache inconsistency.'
        oldA,oldB = [],[]
        for j,g in enumerate(groups):
            sides = (j in A,j in B)
            if all(sides):
                if 'literal_ports_for_two_uses' in g:
                    v,w = g['literal_ports_for_two_uses']
                else:
                    twice = [v for v,s in zip(g['member_old_labels'],g['member_spares']) if s>=2]
                    if twice:
                        v = w = twice[0]
                    else:
                        v,w = g['member_old_labels'][:2]
                oldA.append(v);oldB.append(w)
            elif sides[0]:
                oldA.append(g['member_old_labels'][0])
            elif sides[1]:
                oldB.append(g['member_old_labels'][0])
        spares = {v:s for g in groups for v,s in zip(g['member_old_labels'],g['member_spares'])}
        assert len(set(oldA)) == len(A) and len(set(oldB)) == len(B)
        assert all(n <= spares[v] for v,n in Counter(oldA+oldB).items())
        hit = dict(status='FULL_CACHED_K2_HIT_PENDING_LITERAL_ROOT_ACCEPTANCE',source_n=94186,
            source_m=657452,new_n=94188,new_m=657452+len(oldA)+len(oldB)+1,
            max_degree=14,diameter_at_most=5,helper_internal_edge=[94186,94187],
            A_old_pins=sorted(oldA),B_old_pins=sorted(oldB),
            A_local_groups=A,B_local_groups=B,full_cached_old_targets_per_root=94186,
            old_coverage_misses=[int((~coverA).sum()),int((~coverB).sum())],
            standalone_single_helper_R4_full=[bool(a4.all()),bool(b4.all())],
            source_distance_inherited=True,independent_literal_acceptance_pending=True)
        save('HIT_PARAMETERS.json',hit)
        result.update(status=hit['status'],pending=['root literal source/new-graph acceptance'])
    result.update(charged_whole_CPU_seconds=total_cpu(),
        measured_whole_CPU_lower_bound=total_cpu()-prior+measured_prepare,
        preparation_CPU_reservation=prior,recorded_prepare_CPU_seconds=measured_prepare,
        exact_initial_prepare_self_CPU_missing=True,
        whole_CPU_budget=420,wall_seconds=time.monotonic()-wall)
    assert result['charged_whole_CPU_seconds'] < 420
    save('SOLVER_TERMINAL.json',result)
    save('SOLVER_HANDLE.json',result)
    print(json.dumps(result),flush=True)

if __name__ == '__main__':
    main()
