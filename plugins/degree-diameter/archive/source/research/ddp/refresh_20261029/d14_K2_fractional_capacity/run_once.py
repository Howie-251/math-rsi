#!/usr/bin/env python3
"""Bounded sparse LP diagnosis on saved support bitsets, no graph or SAT."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:
    os.environ[key]='1'
from pathlib import Path
import ctypes
import json
import math
import resource
import subprocess
import time
import warnings

HERE=Path(__file__).resolve().parent
DATA=HERE.parent/'d14_K2_exact_signature_compression'
assert not (HERE/'HANDLE.json').exists(), 'This bounded LP attempt already started.'
start=time.process_time();wall=time.monotonic()
c0=resource.getrusage(resource.RUSAGE_CHILDREN);child0=c0.ru_utime+c0.ru_stime
def cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-start+r.ru_utime+r.ru_stime-child0
def save(name,data):(HERE/name).write_text(json.dumps(data,indent=2)+'\n')
save('HANDLE.json',{'status':'PREPARING_FRACTIONAL_CAPACITY','pid':os.getpid(),'running':True})
try:
    import numpy as np
    import scipy
    from scipy.optimize import linprog
    from scipy.sparse import csr_matrix
except ImportError as exc:
    save('TERMINAL.json',{'status':'SCIPY_UNAVAILABLE_STOP','error':str(exc),'CPU_seconds':cpu(),'running':False})
    raise SystemExit(0)

N=94186;G=3589;W=57;DEN=10**9
groups=json.loads((DATA/'PORT_GROUPS.json').read_text())['groups']
assert len(groups)==G and [g['group'] for g in groups]==list(range(G))
caps=np.array([g['two_helper_capacity'] for g in groups],dtype=np.int64)
assert (caps==1).sum()==3480 and (caps==2).sum()==109
r3=np.fromfile(DATA/'target_R3_group_support.u64le.bin',dtype='<u8')
r4=np.fromfile(DATA/'target_R4_group_support.u64le.bin',dtype='<u8')
assert r3.size==r4.size==N*W
save('INPUT.json',{'targets':N,'groups':G,'words_per_target':W,
    'R3_file':str(DATA/'target_R3_group_support.u64le.bin'),
    'R4_file':str(DATA/'target_R4_group_support.u64le.bin'),
    'group_definition':str(DATA/'PORT_GROUPS.json'),
    'capacity1_groups':3480,'capacity2_groups':109,
    'scipy_version':scipy.__version__,'numpy_version':np.__version__,
    'LP':'min sum x; 0<=x<=cap; (R3+R4)x>=2 for all targets',
    'solver_CPU_budget':20,'whole_CPU_budget':30,'max_rounds':3,
    'initial_rows':256,'rows_added_per_failed_full_check':256,
    'fixed_rational_denominator':DEN,'no_dense_full_matrix':True})
compile_command=['g++','-O3','-shared','-fPIC',str(HERE/'support_ops.cpp'),'-o',str(HERE/'support_ops.so')]
def compile_limit():resource.setrlimit(resource.RLIMIT_CPU,(8,8))
compiled=subprocess.run(compile_command,capture_output=True,text=True,preexec_fn=compile_limit)
(HERE/'compile.log').write_text(compiled.stdout+compiled.stderr)
if compiled.returncode!=0:
    save('TERMINAL.json',{'status':'COMPILE_FAILED_STOP','CPU_seconds':cpu(),'running':False})
    raise SystemExit(0)
lib=ctypes.CDLL(str(HERE/'support_ops.so'))
U64=np.ctypeslib.ndpointer(dtype=np.uint64,flags='C_CONTIGUOUS')
I64=np.ctypeslib.ndpointer(dtype=np.int64,flags='C_CONTIGUOUS')
U32=np.ctypeslib.ndpointer(dtype=np.uint32,flags='C_CONTIGUOUS')
I32=np.ctypeslib.ndpointer(dtype=np.int32,flags='C_CONTIGUOUS')
F64=np.ctypeslib.ndpointer(dtype=np.float64,flags='C_CONTIGUOUS')
lib.support_counts.argtypes=[U64,U64,ctypes.c_int,ctypes.c_int,U32]
lib.row_nnz.argtypes=[U64,U64,I32,ctypes.c_int,ctypes.c_int,I32]
lib.fill_rows.argtypes=[U64,U64,I32,ctypes.c_int,ctypes.c_int,I32,I32,F64]
lib.evaluate_double.argtypes=[U64,U64,F64,ctypes.c_int,ctypes.c_int,F64]
lib.evaluate_integer.argtypes=[U64,U64,I64,ctypes.c_int,ctypes.c_int,I64]
for name in ['support_counts','row_nnz','fill_rows','evaluate_double','evaluate_integer']:
    getattr(lib,name).restype=None
counts=np.empty(N,dtype=np.uint32)
lib.support_counts(r3,r4,N,W,counts)
active=list(map(int,np.argsort(counts,kind='stable')[:256]))
active_set=set(active)
solver_cpu=0.0;rounds=[];status='NOT_STARTED';exact_witness=None;dual_certificate=None
# Process-level hard CPU ceiling counts HiGHS threads too; child compilation is charged separately.
self_cpu=resource.getrusage(resource.RUSAGE_SELF)
self_cpu=self_cpu.ru_utime+self_cpu.ru_stime
hard=max(1,math.floor(self_cpu+30-cpu()-0.2))
resource.setrlimit(resource.RLIMIT_CPU,(hard,hard))

for round_id in range(1,4):
    if cpu()>26 or solver_cpu>=19.8:
        status='CPU_BUDGET_STOP';break
    rows=np.array(active,dtype=np.int32)
    nnz_rows=np.empty(rows.size,dtype=np.int32)
    lib.row_nnz(r3,r4,rows,rows.size,W,nnz_rows)
    ptr=np.empty(rows.size+1,dtype=np.int32);ptr[0]=0
    np.cumsum(nnz_rows,out=ptr[1:])
    cols=np.empty(int(ptr[-1]),dtype=np.int32);values=np.empty(cols.size,dtype=np.float64)
    lib.fill_rows(r3,r4,rows,rows.size,W,ptr,cols,values)
    C=csr_matrix((values,cols,ptr),shape=(len(active),G))
    allowance=min(20-solver_cpu-0.2,30-cpu()-4)
    if allowance<=0:
        status='CPU_BUDGET_BEFORE_LP';break
    handle={'status':'RUNNING_HIGHS_IN_PROCESS','pid':os.getpid(),'round':round_id,
        'active_rows':len(active),'sparse_nonzeros':int(C.nnz),'threads':1,
        'solver_CPU_used_before':solver_cpu,'whole_CPU_used_before':cpu(),
        'this_time_limit_seconds':allowance,'running':True}
    save('HANDLE.json',handle);print(json.dumps(handle),flush=True)
    t=time.process_time()
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter('always')
        lp=linprog(np.ones(G),A_ub=-C,b_ub=-2*np.ones(len(active)),
                   bounds=list(zip(np.zeros(G),caps.astype(float))),method='highs',
                   options={'time_limit':allowance,'threads':1,
                            'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
    this_solver=time.process_time()-t;solver_cpu+=this_solver
    rec={'round':round_id,'active_target_ids':active.copy(),'active_rows':len(active),
        'sparse_nonzeros':int(C.nnz),'solver_status':int(lp.status),'solver_message':str(lp.message),
        'solver_CPU_seconds':this_solver,'solver_CPU_cumulative':solver_cpu,
        'warnings':[str(w.message) for w in caught]}
    rounds.append(rec)
    if lp.status!=0:
        status='LP_UNKNOWN_OR_FAILURE_STOP'
        save(f'round_{round_id:02d}.json',rec);break
    x=np.asarray(lp.x,dtype=np.float64)
    rec['objective']=float(x.sum())
    # A rigorous dual bound from the actually present exact subset of rows.
    Y=np.floor(np.maximum(0.0,-np.asarray(lp.ineqlin.marginals))*DEN).astype(np.int64)
    Ci=csr_matrix((values.astype(np.int64),cols,ptr),shape=C.shape)
    column_sum=np.asarray(Ci.T@Y,dtype=np.int64)
    Z=np.maximum(column_sum-DEN,0)
    numerator=2*sum(map(int,Y))-sum(int(c)*int(z) for c,z in zip(caps,Z))
    assert np.all(column_sum-Z<=DEN) and np.all(Y>=0) and np.all(Z>=0)
    rec['exact_subset_dual_numerator']=numerator;rec['exact_subset_dual_denominator']=DEN
    if numerator>26*DEN:
        dual_certificate={'denominator':DEN,'lower_bound_numerator':numerator,
            'target_multipliers':[[int(t),int(y)] for t,y in zip(rows,Y) if y],
            'group_upper_bound_multipliers':[[g,int(z)] for g,z in enumerate(Z) if z],
            'column_coefficient_sums':list(map(int,column_sum)),
            'group_caps':list(map(int,caps)),
            'exact_feasibility':'Y>=0, Z>=0, C^T Y-Z<=DEN',
            'exact_bound':'(2 sum Y - sum cap*Z)/DEN > 26'}
        save('DUAL_CERTIFICATE.json',dual_certificate)
        status='EXACT_DUAL_BOUND_ABOVE26'
        save(f'round_{round_id:02d}.json',rec);break
    covered=np.empty(N,dtype=np.float64)
    lib.evaluate_double(r3,r4,x,N,W,covered)
    smallest=np.argsort(covered,kind='stable')[:16]
    violations=np.flatnonzero(covered<2-1e-9)
    rec.update(full_target_count_checked=N,minimum_float_coverage=float(covered.min()),
        minimum_float_target=int(np.argmin(covered)),float_violation_count=int(violations.size),
        tightest_float_targets=[[int(t),float(covered[t])] for t in smallest])
    save(f'round_{round_id:02d}.x.json',{'group_x':list(map(float,x)),
         'group_caps':list(map(int,caps)),'sum_x':float(x.sum())})
    if x.sum()<=26 and violations.size==0:
        X=np.minimum(caps*DEN,np.ceil(np.maximum(0,x)*DEN).astype(np.int64))
        exact_cover=np.empty(N,dtype=np.int64)
        lib.evaluate_integer(r3,r4,X,N,W,exact_cover)
        sumX=sum(map(int,X))
        passed=bool(np.all(X>=0) and np.all(X<=caps*DEN) and sumX<=26*DEN and np.all(exact_cover>=2*DEN))
        rec['rationalization']={'denominator':DEN,'sum_numerator':sumX,
            'minimum_coverage_numerator':int(exact_cover.min()),
            'minimum_target':int(np.argmin(exact_cover)),
            'integer_violation_count':int(np.count_nonzero(exact_cover<2*DEN)),
            'all_94186_rows_exactly_checked':True,'passed':passed}
        if passed:
            exact_witness={'denominator':DEN,'group_numerators':list(map(int,X)),
                'group_caps':list(map(int,caps)),'sum_numerator':sumX,
                'sum_float':sumX/DEN,'full_target_count_checked':N,
                'minimum_coverage_numerator':int(exact_cover.min()),
                'tightest_target_ids':list(map(int,np.flatnonzero(exact_cover==exact_cover.min()))),
                'exact_integer_capacity_check':True,'exact_integer_coverage_check':True,
                'exact_sum_at_most26_check':True,
                'scope':'Feasible symmetric fractional relaxation, not a legal integer helper construction'}
            save('EXACT_FRACTIONAL_WITNESS.json',exact_witness)
            exact_cover.tofile(HERE/'exact_target_coverages.i64le.bin')
            status='EXACT_FULL_TARGET_FRACTIONAL_FEASIBLE_AT_MOST26'
        else:
            status='NUMERICAL_FULL_TARGET_FEASIBLE_ONLY_NO_RATIONAL_RETRY'
        save(f'round_{round_id:02d}.json',rec);break
    save(f'round_{round_id:02d}.json',rec)
    if round_id==3:
        status='MAX_THREE_ROUNDS_STOP_NO_GLOBAL_FEASIBILITY_CONCLUSION';break
    additions=[]
    for t in np.argsort(covered,kind='stable'):
        t=int(t)
        if covered[t]>=2-1e-9:break
        if t not in active_set:
            additions.append(t)
            if len(additions)==256:break
    if not additions:
        status='NO_NEW_VIOLATED_ROW_STOP';break
    active.extend(additions);active_set.update(additions)
    rec['new_exact_targets_added']=additions
    save(f'round_{round_id:02d}.json',rec)

terminal={'status':status,'rounds':rounds,'LP_calls':len(rounds),
    'solver_CPU_seconds':solver_cpu,'whole_CPU_seconds':cpu(),'wall_seconds':time.monotonic()-wall,
    'solver_CPU_budget':20,'whole_CPU_budget':30,'max_rounds':3,
    'exact_full_target_fractional_witness':exact_witness is not None,
    'exact_dual_exclusion_above26':dual_certificate is not None,
    'source_graph_reads':0,'BFS_runs':0,'SAT_calls':0,'graphs_generated':0,
    'running':False,'automatic_continuation':False,'pending':[]}
for name in ['RESULT.json','TERMINAL.json','HANDLE.json']:save(name,terminal)
print(json.dumps({k:v for k,v in terminal.items() if k!='rounds'}),flush=True)
