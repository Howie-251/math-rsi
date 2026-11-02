#!/usr/bin/env python3
"""Prepare only: all 3589 exact groups and all 94186 double-sided targets."""
import argparse
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
BASE=HERE.parent
START=time.process_time()
CHILD_START=resource.getrusage(resource.RUSAGE_CHILDREN)
WALL=time.monotonic()
BUDGET=90

def used():
    ru=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-START+ru.ru_utime+ru.ru_stime-CHILD_START.ru_utime-CHILD_START.ru_stime

def save(name,value):
    (HERE/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def run_child(command,name):
    remaining=BUDGET-used()
    assert remaining>=2,'Preparation CPU budget exhausted before child start'
    hard=max(1,math.floor(remaining))
    before=resource.getrusage(resource.RUSAGE_CHILDREN)
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU,(max(1,hard-1),hard))
    with (HERE/f'{name}.log').open('w') as output:
        child=subprocess.Popen(command,cwd=HERE,stdout=output,stderr=subprocess.STDOUT,
                               preexec_fn=limits)
        handle=dict(stage=name,driver_pid=os.getpid(),child_pid=child.pid,command=command,
                    child_hard_CPU_limit=hard,running=True,observational_timeouts=0)
        save(f'{name.upper()}_HANDLE.json',handle)
        print(json.dumps(handle),flush=True)
        while True:
            try:
                rc=child.wait(timeout=5)
                break
            except subprocess.TimeoutExpired:
                handle['observational_timeouts']+=1
                save(f'{name.upper()}_HANDLE.json',handle)
        after=resource.getrusage(resource.RUSAGE_CHILDREN)
        handle.update(running=False,returncode=rc,
            CPU_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime)
        save(f'{name.upper()}_RESULT.json',handle)
        save(f'{name.upper()}_HANDLE.json',handle)
    return handle

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prepare-only',required=True,action='store_true')
    parser.parse_args()
    assert not (HERE/'PREPARE_HANDLE.json').exists(),'Preparation already started; do not restart.'
    save('PREPARE_HANDLE.json',dict(status='PREPARING_ONLY',driver_pid=os.getpid(),running=True,
                                  CPU_budget=BUDGET,solver_calls=0))
    old=BASE/'d14_K2_exact_signature_compression'
    groups=json.loads((old/'PORT_GROUPS.json').read_text())['groups']
    assert len(groups)==3589
    mapped=[]
    for g,entry in enumerate(groups):
        assert g==entry['group']
        assert entry['two_helper_capacity']==min(2,sum(entry['member_spares']))
        mapped.append(dict(entry,local_index=g,A_selector=g+1,B_selector=3590+g))
    save('SELECTOR_MAP.json',dict(groups=mapped,group_range=[0,3588],
        selector_A_range=[1,3589],selector_B_range=[3590,7178],
        group_selection='ALL saved exact groups; no LP support restriction',
        source_group_file=str(old/'PORT_GROUPS.json')))
    caps=[g['two_helper_capacity'] for g in groups]
    assert caps.count(1)==3480 and caps.count(2)==109
    (HERE/'group_caps.u8.bin').write_bytes(bytes(caps))
    input_spec=dict(targets=94186,groups=3589,words_per_target=57,
        R3_file=str(old/'target_R3_group_support.u64le.bin'),
        R4_file=str(old/'target_R4_group_support.u64le.bin'),
        group_file=str(old/'PORT_GROUPS.json'),
        input_layout='target-major, 57 uint64 little-endian per target; bit g is group g',
        all_groups=True,all_targets=True,no_LP_column_filter=True)
    save('INPUT.json',input_spec)
    compile_result=run_child(['g++','-O3','-std=c++17','prepare_native.cpp','-o','prepare_native'],'compile')
    if compile_result['returncode']!=0:
        save('PREPARE_TERMINAL.json',dict(status='COMPILE_FAILED_STOP',driver_pid=os.getpid(),
            whole_CPU_seconds=used(),running=False,solver_calls=0,pending=[]))
        return
    native_result=run_child([str(HERE/'prepare_native'),input_spec['R3_file'],input_spec['R4_file'],
                             str(HERE/'group_caps.u8.bin'),str(HERE)],'native')
    if native_result['returncode']!=0:
        save('PREPARE_TERMINAL.json',dict(status='NATIVE_FAILED_OR_BUDGET_STOP_NOT_FULL_MODEL',
            driver_pid=os.getpid(),native_pid=native_result['child_pid'],native_returncode=native_result['returncode'],
            whole_CPU_seconds=used(),running=False,solver_calls=0,pending=[]))
        return
    native=json.loads((HERE/'CNF_BUILD_RESULT.json').read_text())
    assert native['variables']==100492
    assert native['original_sided_rows']==188372
    model=dict(native,status='FULL_ALLGROUP_FULLTARGET_PREPARED_NOT_SOLVED',
        driver_pid=os.getpid(),native_pid=native_result['child_pid'],native_returncode=0,
        source_n=94186,source_m=657452,original_free_ports=3685,exact_groups=3589,
        capacity1_groups=3480,capacity2_groups=109,side_pin_limit=13,
        cardinality_auxiliary_variables=93314,
        cardinality_encoding='forward sequential prefix thresholds1..13 with overflow forbidden',
        coverage_conditions=['R4(A) OR R3(B), for every old target','R4(B) OR R3(A), for every old target'],
        complete_all_groups=True,complete_all_targets=True,LP_support_restriction=False,
        row_merging='only exact full positive-literal equality, including either side',
        selector_map='SELECTOR_MAP.json',CNF='model.cnf',
        target_side_map='target_side_to_coverage_row.u32le.bin',
        target_side_map_layout='uint32 LE, first A-side targets0..94185, then B-side; zero-based coverage row ids',
        row_representatives='coverage_row_representatives.tsv',
        row_multiplicities='coverage_row_multiplicities.u32le.bin',
        coverage_clause_offset_zero_based=native['base_clauses'],
        compile_CPU_seconds=compile_result['CPU_seconds'],native_child_CPU_seconds=native_result['CPU_seconds'],
        prepare_CPU_seconds=used(),prepare_wall_seconds=time.monotonic()-WALL,prepare_CPU_budget=90,
        planned_solver_CPU_budget=300,planned_whole_CPU_budget=420,max_planned_solver_calls=1,
        UNKNOWN_policy='stop; no restart or second call',solver_calls=0,
        source_graph_reads=0,BFS_runs=0,graphs_generated=0,running=False,
        pending=['Root review before any solver call'])
    save('MODEL.json',model)
    save('PREPARE_TERMINAL.json',model)
    save('PREPARE_HANDLE.json',model)
    print(json.dumps(model),flush=True)

if __name__=='__main__':
    main()
