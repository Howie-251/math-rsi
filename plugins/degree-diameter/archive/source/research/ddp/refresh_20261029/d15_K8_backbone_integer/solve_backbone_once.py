#!/usr/bin/env python3
"""One bounded HiGHS call for the prepared K8 backbone; root must invoke --solve."""
import os
os.environ['OMP_NUM_THREADS']='1'
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['MKL_NUM_THREADS']='1'
import argparse
from datetime import datetime,timezone
import json
from pathlib import Path
import resource
import time
HERE=Path(__file__).resolve().parent

def save(name,obj):
    (HERE/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--solve',action='store_true',required=True)
    parser.add_argument('--time-limit',type=float,default=45)
    args=parser.parse_args()
    assert 0<args.time_limit<=60
    assert not (HERE/'SOLVER_HANDLE.json').exists(),'This one-call batch already started; no restart.'
    start=time.process_time();wall=time.monotonic()
    resource.setrlimit(resource.RLIMIT_CPU,(70,71))
    import numpy as np
    from scipy import sparse
    from scipy.optimize import Bounds,LinearConstraint,milp
    A=sparse.load_npz(HERE/'constraints.csc.npz')
    z=np.load(HERE/'model_arrays.npz')
    handle=dict(status='RUNNING',pid=os.getpid(),started_UTC=datetime.now(timezone.utc).isoformat(),
        solver='scipy.optimize.milp/HiGHS',solver_time_limit_seconds=args.time_limit,
        process_CPU_limit_seconds=70,threads=1,solver_calls=1,colouring_solver_calls=0,running=True)
    save('SOLVER_HANDLE.json',handle)
    print(json.dumps(handle),flush=True)
    solve_start=time.process_time()
    res=milp(c=z['objective'],integrality=z['integrality'],
        bounds=Bounds(z['variable_lb'],z['variable_ub']),
        constraints=LinearConstraint(A.astype(np.float64),z['constraint_lb'],z['constraint_ub']),
        options=dict(time_limit=args.time_limit,mip_rel_gap=0.0,presolve=True,threads=1))
    solver_CPU=time.process_time()-solve_start
    accepted=False
    validation={}
    if res.x is not None:
        candidate=np.rint(res.x).astype(np.int64)
        error=float(np.max(np.abs(res.x-candidate)))
        lhs=A.astype(np.int64)@candidate
        accepted=error<=1e-6 and np.all((candidate==0)|(candidate==1)) and int(lhs[0])==64 and np.all(lhs[1:]>=8)
        validation=dict(rounding_max_error=error,selected_count=int(candidate.sum()),
            minimum_weighted_target_coverage=int(lhs[1:].min()),all_exact_constraints=bool(accepted))
        if accepted:
            cols=np.flatnonzero(candidate)
            save('BACKBONE_CANDIDATE.json',dict(status='VALID_INTEGER_BACKBONE_NOT_COLOURED',
                selected_columns=list(map(int,cols)),selected_old_labels=list(map(int,z['old_labels'][cols])),
                cardinality=64,validation=validation,full_graph_exists_claimed=False))
    status='FEASIBLE_BACKBONE_ONLY' if accepted else ('BACKBONE_INFEASIBLE_RAW_HIGHS' if res.status==2 else 'UNKNOWN_NO_ACCEPTED_BACKBONE')
    result=dict(status=status,raw_status=int(res.status),raw_message=str(res.message),
        solver_calls=1,coloring_solver_calls=0,solver_CPU_seconds=solver_CPU,
        process_CPU_seconds=time.process_time()-start,wall_seconds=time.monotonic()-wall,
        validation=validation,candidate_count=int(accepted),complete_new_graphs=0,
        source_graph_reads=0,BFS_runs=0,running=False,pending=[],automatic_continuation=False,
        limitation='No graph claim: a valid T still needs8-colour residual coverage and degree15 graph acceptance; one failed T colouring cannot exclude K8')
    for name in ('SOLVER_TERMINAL.json','SOLVER_HANDLE.json'):save(name,result)
    print(json.dumps(result),flush=True)

if __name__=='__main__':main()
