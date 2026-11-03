#!/usr/bin/env python3
"""Recover statistics after the already completed native build's filename collision.
Never execute the builder, compiler or solver, and never modify the CNF.
"""
import json
import os
from pathlib import Path
import resource
import time
from array import array
HERE=Path(__file__).resolve().parent
START=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(20,21))
assert not (HERE/'METADATA_RECOVERY_RESULT.json').exists()

def save(name,j):
    (HERE/name).write_text(json.dumps(j,ensure_ascii=False,indent=2)+'\n')

native_process=json.loads((HERE/'NATIVE_RESULT.json').read_text())
compile_process=json.loads((HERE/'COMPILE_RESULT.json').read_text())
assert native_process['returncode']==compile_process['returncode']==0
completion=json.loads((HERE/'native.log').read_text().splitlines()[-1])
assert completion['stage']=='COMPLETE'
base=193778+3480
clauses=literals=0
minwidth=7178
maxwidth=0
with (HERE/'model.cnf').open('rb') as f:
    header=f.readline().decode().split()
    assert header==['p','cnf','100492','385396']
    for line in f:
        assert line.endswith(b' 0\n')
        width=line.count(b' ')
        literals+=width
        if clauses>=base:
            minwidth=min(minwidth,width)
            maxwidth=max(maxwidth,width)
        clauses+=1
assert clauses==completion['clauses']==385396
counts=array('I')
counts.frombytes((HERE/'coverage_row_multiplicities.u32le.bin').read_bytes())
mapping=array('I')
mapping.frombytes((HERE/'target_side_to_coverage_row.u32le.bin').read_bytes())
assert len(counts)==188138 and sum(counts)==188372
assert len(mapping)==188372 and max(mapping)==188137
observed=array('I',[0])*len(counts)
for j in mapping:observed[j]+=1
assert observed==counts
data=dict(status='FULL_ALLGROUP_CNF_PREPARED_NOT_SOLVED',pid=native_process['child_pid'],
    variables=100492,selector_variables=7178,cardinality_clauses=193778,
    capacity_mutex_clauses=3480,base_clauses=base,original_sided_rows=188372,
    unique_coverage_rows=188138,duplicate_coverage_rows=234,clauses=clauses,
    literal_occurrences=literals,min_coverage_clause_literals=minwidth,
    max_coverage_clause_literals=maxwidth,cnf_bytes=(HERE/'model.cnf').stat().st_size,
    recovered_from='Completed native stdout, unchanged CNF one streaming scan, and saved row maps',
    native_CPU_seconds=native_process['CPU_seconds'],native_peak_RSS_KiB=None)
save('CNF_BUILD_RESULT.json',data)
measured_before=native_process['CPU_seconds']+compile_process['CPU_seconds']
model=dict(data,status='FULL_ALLGROUP_FULLTARGET_PREPARED_NOT_SOLVED',
    driver_pid=native_process['driver_pid'],driver_returncode=1,
    driver_error='Metadata filename collision after successful complete native build; no CNF alteration',
    native_pid=native_process['child_pid'],native_returncode=0,
    metadata_recovery_pid=os.getpid(),metadata_recovery_returncode=0,
    source_n=94186,source_m=657452,original_free_ports=3685,exact_groups=3589,
    capacity1_groups=3480,capacity2_groups=109,side_pin_limit=13,
    cardinality_auxiliary_variables=93314,
    cardinality_encoding='forward sequential prefix thresholds1..13 with overflow forbidden',
    coverage_conditions=['R4(A) OR R3(B), for every old target','R4(B) OR R3(A), for every old target'],
    complete_all_groups=True,complete_all_targets=True,LP_support_restriction=False,
    row_merging='only exact full positive-literal equality, including either side',
    selector_map='SELECTOR_MAP.json',CNF='model.cnf',target_side_map='target_side_to_coverage_row.u32le.bin',
    target_side_map_layout='uint32 LE, first A-side targets0..94185, then B-side; zero-based coverage row ids',
    row_representatives='coverage_row_representatives.tsv',row_multiplicities='coverage_row_multiplicities.u32le.bin',
    coverage_clause_offset_zero_based=base,
    compile_CPU_seconds=compile_process['CPU_seconds'],native_child_CPU_seconds=native_process['CPU_seconds'],
    metadata_recovery_CPU_seconds=time.process_time()-START,
    initial_driver_self_CPU_seconds=None,
    CPU_accounting_note='Initial Python driver self CPU was not preserved at exception; compile/native CPU and one recovery CPU are measured. No claim of exact aggregate including missing driver self CPU.',
    accounted_CPU_seconds=measured_before+time.process_time()-START,prepare_CPU_budget=90,
    planned_solver_CPU_budget=300,planned_whole_CPU_budget=420,max_planned_solver_calls=1,
    UNKNOWN_policy='stop; no restart or second call',solver_calls=0,
    source_graph_reads=0,BFS_runs=0,graphs_generated=0,running=False,
    generator_runs=1,metadata_recovery_runs=1,
    pending=['Root review before any solver call'])
save('MODEL.json',model)
save('PREPARE_TERMINAL.json',model)
save('PREPARE_HANDLE.json',model)
save('METADATA_RECOVERY_RESULT.json',dict(status='COMPLETE_METADATA_RECOVERED_WITHOUT_REBUILD',
    pid=os.getpid(),CPU_seconds=time.process_time()-START,source_graph_reads=0,
    cache_ball_recomputations=0,native_builder_restarts=0,CNF_modified=False,solver_calls=0))
print(json.dumps(model),flush=True)
