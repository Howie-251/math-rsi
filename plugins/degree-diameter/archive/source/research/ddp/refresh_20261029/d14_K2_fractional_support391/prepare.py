#!/usr/bin/env python3
"""Prepare the exact full-target 391-support integer model; never run a solver."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name]='1'
import argparse
import json
from pathlib import Path
import resource
import shutil
import time

START=time.process_time()
WALL=time.monotonic()
resource.setrlimit(resource.RLIMIT_CPU,(15,16))
HERE=Path(__file__).resolve().parent
BASE=HERE.parent
N=94186
ALL_GROUPS=3589
ALL_WORDS=57
K=391

def save(name,value):
    (HERE/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prepare-only',action='store_true',required=True)
    parser.parse_args()
    assert not (HERE/'PREPARE_HANDLE.json').exists(), 'This preparation has already started.'
    save('PREPARE_HANDLE.json',dict(status='PREPARING_ONLY',pid=os.getpid(),running=True,
        CPU_budget=15,solver_calls=0))
    print(json.dumps(dict(status='PREPARING_ONLY',pid=os.getpid())),flush=True)
    import numpy as np
    old=BASE/'d14_K2_exact_signature_compression'
    witness=BASE/'d14_K2_fractional_capacity/EXACT_GLOBAL_WITNESS.json'
    frac=json.loads(witness.read_text())
    assert frac['status']=='EXACT_GLOBAL_FRACTIONAL_WITNESS_VERIFIED'
    nums=frac['group_numerators']
    all_groups=json.loads((old/'PORT_GROUPS.json').read_text())['groups']
    assert len(nums)==len(all_groups)==ALL_GROUPS
    group_ids=[g for g,x in enumerate(nums) if x>0]
    assert len(group_ids)==K
    mappings=[]
    for j,g in enumerate(group_ids):
        entry=all_groups[g]
        assert entry['group']==g
        assert entry['two_helper_capacity']==min(2,sum(entry['member_spares']))
        mappings.append(dict(entry,local_index=j,A_selector=j+1,B_selector=K+j+1,
                             fractional_numerator=nums[g]))
    caps=[m['two_helper_capacity'] for m in mappings]
    save('SELECTOR_MAP.json',dict(source_witness=str(witness),denominator=frac['denominator'],
        local_order='increasing original group id',side_A_selectors=[1,K],
        side_B_selectors=[K+1,2*K],groups=mappings))
    groups_arr=np.asarray(group_ids,dtype=np.uint32)
    groups_arr.tofile(HERE/'selected_group_ids.u32le.bin')

    # Restrict both complete transposed caches to the same literal 391 groups.
    # 7 little-endian u64 per target, with bits391..447 zero.
    restricted=[]
    for radius in (3,4):
        path=old/f'target_R{radius}_group_support.u64le.bin'
        raw=np.memmap(path,dtype='<u8',mode='r',shape=(N,ALL_WORDS))
        packed=np.zeros((N,56),dtype=np.uint8)
        for j,g in enumerate(group_ids):
            bits=((raw[:,g//64] >> np.uint64(g%64)) & np.uint64(1)).astype(np.uint8)
            packed[:,j//8] |= bits << np.uint8(j%8)
        packed.tofile(HERE/f'target_R{radius}_support391.u64le.bin')
        restricted.append(packed.tobytes())
        del raw,packed
    raw3,raw4=restricted
    rowwidth=56
    variables=2*K
    clauses=0
    literal_count=0
    body=HERE/'model.body.clauses'
    with body.open('w') as out:
        def fresh():
            nonlocal variables
            variables+=1
            return variables
        def clause(xs):
            nonlocal clauses,literal_count
            out.write(' '.join(map(str,xs))+' 0\n')
            clauses+=1
            literal_count+=len(xs)
        # Reuse the existing K2 forward sequential at-most13 construction.
        # cur[k] is forced when prefix count >= k+1; converse is unnecessary.
        # Any <=13 assignment extends by taking the actual prefix thresholds.
        for side in (0,1):
            previous=None
            for j in range(K):
                x=1+side*K+j
                cur=[fresh() for _ in range(13)]
                clause([-x,cur[0]])
                if previous is None:
                    for z in cur[1:]:clause([-z])
                else:
                    for p,q in zip(previous,cur):clause([-p,q])
                    for k in range(1,13):clause([-x,-previous[k-1],cur[k]])
                    clause([-x,-previous[12]])
                previous=cur
        counter_clauses=clauses
        for j,cap in enumerate(caps):
            assert cap in (1,2)
            if cap==1:clause([-(j+1),-(K+j+1)])
        base_clauses=clauses
        print(json.dumps(dict(status='CARDINALITY_READY',pid=os.getpid(),variables=variables,
            CPU_seconds=time.process_time()-START)),flush=True)

        # A row is its full 782-bit positive-literal set. Exact integer equality
        # merges equal rows across targets and both sides, without implication cuts.
        seen={}
        counts=[]
        reps=[]
        row_map=np.empty((2,N),dtype='<u4')
        texts=[str(v) for v in range(1,2*K+1)]
        min_width=2*K
        max_width=0
        for t in range(N):
            lo=t*rowwidth
            s3=int.from_bytes(raw3[lo:lo+rowwidth],'little')
            s4=int.from_bytes(raw4[lo:lo+rowwidth],'little')
            assert s3&~s4==0
            for side,bits in enumerate((s4|(s3<<K),s3|(s4<<K))):
                assert bits and bits.bit_length()<=2*K
                idx=seen.get(bits)
                if idx is None:
                    idx=len(seen)
                    seen[bits]=idx
                    counts.append(0)
                    reps.append([side,t])
                    word=bits
                    row=[]
                    while word:
                        low=word&-word
                        row.append(texts[low.bit_length()-1])
                        word^=low
                    width=len(row)
                    min_width=min(min_width,width)
                    max_width=max(max_width,width)
                    out.write(' '.join(row)+' 0\n')
                    clauses+=1
                    literal_count+=width
                row_map[side,t]=idx
                counts[idx]+=1
        row_map.tofile(HERE/'target_side_to_coverage_row.u32le.bin')
    assert sum(counts)==2*N
    save('COVERAGE_ROWS.json',dict(original_targets=N,original_sided_rows=2*N,
        unique_rows=len(reps),row_map_file='target_side_to_coverage_row.u32le.bin',
        row_map_layout='uint32 little-endian [side A then side B][target 0..94185]; value zero-based unique coverage row',
        representatives=reps,multiplicities=counts,
        min_literals=min_width,max_literals=max_width,
        model_clause_offset_zero_based=base_clauses))
    with (HERE/'model.cnf').open('w') as target:
        target.write(f'p cnf {variables} {clauses}\n')
        with body.open() as source:shutil.copyfileobj(source,target,1024*1024)
    elapsed=time.process_time()-START
    model=dict(status='FULL_TARGET_391_POOL_PREPARED_NOT_SOLVED',pid=os.getpid(),
        source_n=N,source_m=657452,all_original_groups=ALL_GROUPS,selected_groups=K,
        positive_group_selection='exact numerator > 0 in saved rational witness',
        capacity1_groups=caps.count(1),capacity2_groups=caps.count(2),
        selector_variables=2*K,all_variables=variables,
        cardinality_auxiliary_variables=variables-2*K,side_pin_limit=13,
        cardinality_encoding='forward sequential prefix thresholds1..13, overflow forbidden',
        cardinality_clauses=counter_clauses,capacity_mutex_clauses=base_clauses-counter_clauses,
        source_target_count=N,source_sided_coverage_rows=2*N,
        unique_coverage_rows=len(reps),merged_exact_duplicate_rows=2*N-len(reps),
        total_clauses=clauses,literal_occurrences=literal_count,
        full_target_system=True,model='model.cnf',selector_map='SELECTOR_MAP.json',
        restricted_support_words_per_target=7,restricted_support_group_order='SELECTOR_MAP local_index',
        prepare_CPU_seconds=elapsed,prepare_wall_seconds=time.monotonic()-WALL,
        prepare_CPU_budget=15,solver_calls=0,source_graph_reads=0,BFS_runs=0,graphs_generated=0,
        planned_future_solver_CPU_budget=120,planned_future_whole_CPU_budget=150,
        max_future_solver_calls=1,UNKNOWN_policy='stop without continuation',
        running=False,pending=['Root source and model review; solver not started'],
        exclusion_scope='Only the fixed 391 positive groups, not all 3589 groups')
    save('MODEL.json',model)
    save('PREPARE_TERMINAL.json',model)
    save('PREPARE_HANDLE.json',model)
    print(json.dumps(model),flush=True)

if __name__=='__main__':
    main()
