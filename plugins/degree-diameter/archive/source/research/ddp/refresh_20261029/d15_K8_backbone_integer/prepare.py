#!/usr/bin/env python3
"""Prepare the complete D15/D4 K8 uncoloured backbone; never solve."""
import os
os.environ['OMP_NUM_THREADS']='1'
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['MKL_NUM_THREADS']='1'
import argparse
import json
from pathlib import Path
import resource
import time
START=time.process_time()
WALL=time.monotonic()
import numpy as np
from scipy import sparse

HERE=Path(__file__).resolve().parent
GATE=HERE.parent/'d15_D4_K2_route_gate'
N=15552
K=648
W=11

def save(name,obj):
    (HERE/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prepare-only',action='store_true',required=True)
    parser.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU,(10,11))
    assert not (HERE/'PREPARE_HANDLE.json').exists(),'One preparation already started; do not rerun.'
    save('PREPARE_HANDLE.json',dict(status='PREPARING_ONLY',pid=os.getpid(),running=True,CPU_budget_seconds=10))
    binding=json.loads((GATE/'RESULT.json').read_text())
    assert binding['source_n']==N and binding['source_m']==116316
    assert binding['ports']==K and binding['all_port_spares']==1
    labels=np.fromfile(GATE/'FREE_ORDER.u32le.bin',dtype='<u4')
    text_labels=np.array(list(map(int,(GATE/'FREE_ORDER.txt').read_text().split())),dtype=np.uint32)
    assert labels.shape==(K,) and len(set(map(int,labels)))==K
    assert np.array_equal(labels,text_labels) and np.all(labels<N)
    data={}
    for radius in (2,3):
        raw=(GATE/f'target_R{radius}_support.u64le.bin').read_bytes()
        assert len(raw)==N*W*8
        bits=np.unpackbits(np.frombuffer(raw,dtype=np.uint8).reshape(N,W*8),axis=1,bitorder='little')
        assert not np.any(bits[:,K:])
        data[radius]=bits[:,:K].copy()
    assert np.all(data[2]<=data[3])
    assert np.all(data[2].sum(axis=0)==191)
    assert np.all(data[3].sum(axis=0)==2310)
    coefficients=(data[3]+7*data[2]).astype(np.int8)
    assert np.all(np.isin(coefficients,(0,1,8)))
    A=sparse.vstack((sparse.csr_matrix(np.ones((1,K),dtype=np.int8)),sparse.csr_matrix(coefficients)),format='csc')
    assert A.shape==(N+1,K) and A.nnz==1497528
    sparse.save_npz(HERE/'constraints.csc.npz',A,compressed=False)
    np.savez(HERE/'model_arrays.npz',objective=np.zeros(K,dtype=np.float64),
        integrality=np.ones(K,dtype=np.uint8),variable_lb=np.zeros(K,dtype=np.float64),
        variable_ub=np.ones(K,dtype=np.float64),
        constraint_lb=np.r_[64.0,np.full(N,8.0)],
        constraint_ub=np.r_[64.0,np.full(N,np.inf)],old_labels=labels)
    save('SELECTOR_MAP.json',dict(indexing='zero-based column p is z_p and FREE_ORDER[p]',
        ports=[dict(column=i,old_label=int(v),spare=1) for i,v in enumerate(labels)]))
    save('INPUT_SCOPE.json',dict(source_n=N,source_m=116316,source_D4='inherited accepted source; no source BFS',
        ports=K,target_rows=N,input_R2=str(GATE/'target_R2_support.u64le.bin'),
        input_R3=str(GATE/'target_R3_support.u64le.bin'),input_order=str(GATE/'FREE_ORDER.u32le.bin'),
        input_layout='15552 target-major rows of11 little-endian uint64; bit p is FREE_ORDER column p',
        source_binding=str(GATE/'RESULT.json'),full_all_ports=True,full_all_targets=True,
        LP_support_restriction=False,fiber_restriction=False,symmetry_restriction=False,
        operation='Uncoloured necessary backbone for8 helpers forming K8, each with8 disjoint old pins',
        target_order=15560,target_degree=15,target_diameter=4))
    elapsed=time.process_time()-START
    assert elapsed<10
    result=dict(status='COMPLETE_K8_BACKBONE_MODEL_PREPARED_NOT_SOLVED',pid=os.getpid(),
        variables=K,binary_variables=K,rows=N+1,cardinality_equalities=1,target_inequalities=N,
        matrix_shape=[N+1,K],matrix_nnz=int(A.nnz),matrix_dtype=str(A.dtype),
        matrix_row0='sum z =64',matrix_rows1_to15552='R3-count+7*R2-count>=8',
        target_row_coefficients=[1,8],matrix_file='constraints.csc.npz',arrays_file='model_arrays.npz',
        matrix_bytes=(HERE/'constraints.csc.npz').stat().st_size,arrays_bytes=(HERE/'model_arrays.npz').stat().st_size,
        objective='zero: feasibility only',R2_subset_R3_checked=True,complete_all648_ports=True,complete_all15552_targets=True,
        preparation_CPU_seconds=elapsed,preparation_wall_seconds=time.monotonic()-WALL,preparation_CPU_budget_seconds=10,
        solver_calls=0,coloring_solver_calls=0,source_graph_reads=0,BFS_runs=0,graphs_generated=0,
        running=False,pending=['Root static review before any solver call; feasible T still needs balanced8-colour coverage'])
    for name in ('MODEL.json','PREPARE_TERMINAL.json','PREPARE_HANDLE.json'):save(name,result)
    print(json.dumps(result),flush=True)

if __name__=='__main__':main()
