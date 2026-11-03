#!/usr/bin/env python3
"""Prepare full literal-port D15/D4 K2 coverage CNF; no solve mode."""
import argparse
from array import array
import json
import os
from pathlib import Path
import resource
import shutil
import sys
import time

HERE=Path(__file__).resolve().parent
GATE=HERE.parent/'d15_D4_K2_route_gate'
START=time.process_time()
WALL=time.monotonic()
resource.setrlimit(resource.RLIMIT_CPU,(15,16))
N=15552
K=648
LIMIT=14
W=11

def save(name,obj):
    (HERE/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prepare-only',action='store_true',required=True)
    parser.parse_args()
    assert not (HERE/'PREPARE_HANDLE.json').exists(),'This preparation already started; no restart.'
    save('PREPARE_HANDLE.json',dict(status='PREPARING_ONLY',pid=os.getpid(),running=True,CPU_budget=15))
    print(json.dumps(dict(status='PREPARING_ONLY',pid=os.getpid())),flush=True)
    assert sys.byteorder=='little'
    gate=json.loads((GATE/'RESULT.json').read_text())
    assert gate['source_n']==N and gate['source_m']==116316
    assert gate['ports']==K and gate['all_port_spares']==1
    labels=list(map(int,(GATE/'FREE_ORDER.txt').read_text().split()))
    binary=array('I');binary.frombytes((GATE/'FREE_ORDER.u32le.bin').read_bytes())
    assert len(labels)==len(set(labels))==K and labels==list(binary)
    assert all(0<=v<N for v in labels)
    save('SELECTOR_MAP.json',dict(source_n=N,source_m=116316,port_count=K,
        side_A_range=[1,K],side_B_range=[K+1,2*K],
        order='exact inherited R3-cache port order, bound by d15_D4_K2_route_gate',
        ports=[dict(column=i,old_label=v,spare=1,A_selector=i+1,B_selector=K+i+1)
               for i,v in enumerate(labels)]))
    paths={r:GATE/f'target_R{r}_support.u64le.bin' for r in (2,3)}
    raw={r:p.read_bytes() for r,p in paths.items()}
    assert all(len(b)==N*W*8 for b in raw.values())
    save('INPUT_SCOPE.json',dict(source_n=N,source_m=116316,all_literal_ports=K,all_targets=N,
        input_R2=str(paths[2]),input_R3=str(paths[3]),input_order=str(GATE/'FREE_ORDER.txt'),
        input_layout='target-major; 11 uint64 little-endian per target; bit i is literal port column i',
        cache_source_binding=str(GATE/'RESULT.json'),
        operation='Keep all old edges, add adjacent helpers y,z, each connected to <=14 original freeports',
        port_capacities=1,new_helper_edge=True,proposed_order=15554,
        target_degree=15,target_diameter=4,source_diameter_inherited_not_rechecked=True,
        no_LP_support_filter=True,no_port_group_reduction=True,no_symmetry=True,no_line_restriction=True))

    variables=2*K
    clauses=literals=0
    body=HERE/'model.body.clauses'
    with body.open('w') as out:
        def fresh():
            nonlocal variables
            variables+=1
            return variables
        def clause(xs):
            nonlocal clauses,literals
            out.write(' '.join(map(str,xs))+' 0\n')
            clauses+=1;literals+=len(xs)
        for side in (0,1):
            previous=None
            for j in range(K):
                x=1+side*K+j
                cur=[fresh() for _ in range(LIMIT)]
                clause([-x,cur[0]])
                if previous is None:
                    for z in cur[1:]:clause([-z])
                else:
                    for p,q in zip(previous,cur):clause([-p,q])
                    for k in range(1,LIMIT):clause([-x,-previous[k-1],cur[k]])
                    clause([-x,-previous[LIMIT-1]])
                previous=cur
        cardinality_clauses=clauses
        assert variables==19440 and cardinality_clauses==37554
        for i in range(K):clause([-(i+1),-(K+i+1)])
        base_clauses=clauses
        seen={};reps=[];counts=[]
        mapping=array('I',[0])*(2*N)
        text=[str(i+1) for i in range(2*K)]
        min_width=2*K;max_width=0
        for t in range(N):
            start=t*W*8
            s2=int.from_bytes(raw[2][start:start+W*8],'little')
            s3=int.from_bytes(raw[3][start:start+W*8],'little')
            assert not (s2&~s3) and s3.bit_length()<=K
            for side,bits in enumerate((s3|(s2<<K),s2|(s3<<K))):
                assert bits
                idx=seen.get(bits)
                if idx is None:
                    idx=len(seen);seen[bits]=idx
                    reps.append([side,t]);counts.append(0)
                    word=bits;row=[]
                    while word:
                        low=word&-word;row.append(text[low.bit_length()-1]);word^=low
                    out.write(' '.join(row)+' 0\n')
                    width=len(row);clauses+=1;literals+=width
                    min_width=min(min_width,width);max_width=max(max_width,width)
                mapping[side*N+t]=idx;counts[idx]+=1
        assert sum(counts)==2*N
    (HERE/'target_side_to_coverage_row.u32le.bin').write_bytes(mapping.tobytes())
    save('COVERAGE_ROWS.json',dict(original_targets=N,original_sided_rows=2*N,
        unique_rows=len(reps),representatives=reps,multiplicities=counts,
        min_literals=min_width,max_literals=max_width,
        row_map='target_side_to_coverage_row.u32le.bin',
        row_map_layout='uint32 little-endian; first sideA targets0..15551, then sideB; zero-based coverage row ID',
        model_clause_offset_zero_based=base_clauses))
    with (HERE/'model.cnf').open('w') as out:
        out.write(f'p cnf {variables} {clauses}\n')
        with body.open() as inp:shutil.copyfileobj(inp,out,1024*1024)
    elapsed=time.process_time()-START
    assert elapsed<15
    model=dict(status='D15_D4_ALL648_FULL15552_K2_CNF_PREPARED_NOT_SOLVED',pid=os.getpid(),
        source_n=N,source_m=116316,all_literal_ports=K,all_port_capacities=1,
        side_pin_limit=LIMIT,selectors=2*K,all_variables=variables,
        cardinality_auxiliaries=variables-2*K,cardinality_clauses=cardinality_clauses,
        mutex_clauses=K,base_clauses=base_clauses,coverage_original_rows=2*N,
        coverage_unique_rows=len(reps),exact_duplicate_rows_removed=2*N-len(reps),
        coverage_clause_min_literals=min_width,coverage_clause_max_literals=max_width,
        total_clauses=clauses,literal_occurrences=literals,cnf_bytes=(HERE/'model.cnf').stat().st_size,
        complete_all_ports=True,complete_all_targets=True,
        formulas=['R3(A) OR R2(B), every old target','R3(B) OR R2(A), every old target'],
        cardinality_encoding='forward prefix thresholds1..14 plus overflow; existential-equivalent <=14',
        symmetry_constraints=False,line_constraints=False,LP_column_restriction=False,port_grouping=False,
        prepare_CPU_seconds=elapsed,prepare_wall_seconds=time.monotonic()-WALL,prepare_CPU_budget=15,
        proposed_new_order=15554,new_helper_degrees_at_most=15,
        planned_solver_CPU_seconds=120,planned_whole_CPU_seconds=150,max_planned_solver_calls=1,
        UNKNOWN_policy='stop; no continuation',solver_calls=0,source_graph_reads=0,
        R2_balls_recomputed=0,R3_balls_recomputed=0,BFS_runs=0,graphs_generated=0,
        running=False,pending=['Root review before any solver call'])
    for name in ('MODEL.json','PREPARE_TERMINAL.json','PREPARE_HANDLE.json'):save(name,model)
    print(json.dumps(model),flush=True)

if __name__=='__main__':main()
