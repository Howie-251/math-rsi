"""One complete static R4 model, one LP and at most one MIP; no ball recomputation."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import json
from pathlib import Path
import resource
import signal
import time
from datetime import datetime, timezone

resource.setrlimit(resource.RLIMIT_CPU,(127,128))
HERE=Path(__file__).resolve().parent
CACHE=HERE.parent/'monotone_R4_cover'
N=102060; K=810; W=1595; TW=13; DELTA=15; SOURCE_M=765045
START_WALL=time.monotonic()
def cpu():
    r=resource.getrusage(resource.RUSAGE_SELF)
    return r.ru_utime+r.ru_stime
def save(name,obj):
    (HERE/name).write_text(json.dumps(obj,indent=2)+'\n')
def checkpoint(stage,**kw):
    obj={'stage':stage,'pid':os.getpid(),'CPU_seconds':cpu(),'wall_seconds':time.monotonic()-START_WALL,**kw}
    save('checkpoint.json',obj)
    print(json.dumps(obj),flush=True)
class BudgetStop(Exception): pass
def soft_cpu(*_): raise BudgetStop('Worker127CPUsoftlimit')
signal.signal(signal.SIGXCPU,soft_cpu)

# Future-only fix after the recorded first run. worker.executed.py is its snapshot.
# During a native solver call, a Python SIGXCPU handler can be delayed until the
# call returns. SIG_DFL makes the OS stop at the solver-stage soft CPU deadline.
def begin_solver_stage():
    origin=cpu()
    deadline=min(127,int(origin+95.0))
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
    signal.signal(signal.SIGXCPU,signal.SIG_DFL)
    resource.setrlimit(resource.RLIMIT_CPU,(deadline,128))
    save('SOLVER_STAGE_BUDGET.json',{'stage_CPU_origin':origin,'combined_solver_CPU_budget_seconds':95,
         'OS_soft_CPU_deadline':deadline,'OS_hard_CPU_limit':128,'SIGXCPU_action':'OS_default_termination',
         'timer_version':'future_only_after_first_execution_not_retested'})
def end_solver_stage():
    resource.setrlimit(resource.RLIMIT_CPU,(127,128))
    signal.signal(signal.SIGXCPU,soft_cpu)

checkpoint('IMPORTING_SINGLE_THREAD_NUMERICAL_LIBRARIES')
import warnings
import numpy as np
import scipy
from scipy.sparse import csc_matrix
from scipy.optimize import Bounds,LinearConstraint,linprog,milp
warnings.filterwarnings('ignore',message='Unrecognized options detected:.*threads.*')

result={'target_Delta':15,'target_D':5,'publicL':102060,'source_n':N,'source_m':SOURCE_M,
        'hypothetical_n':N+1,'actual_n':None,'actual_D':None,'ordinary_bad_unordered_pairs':None,
        'source_BFS':0,'ball_recomputation':0,'row_or_ball_deduplication_repeated':False,
        'constraint_generation':False,'LP_calls':0,'MIP_calls':0,'family_strictly_excluded':False}
hit=None; dims=None; solver_cpu=0.0
try:
    meta=json.loads((CACHE/'PREFLIGHT.json').read_text())
    assert meta['status']=='ALL810_R4_COMPLETE' and meta['n']==N and meta['m']==SOURCE_M
    pins=np.loadtxt(CACHE/'eligible.txt',dtype=np.int32,ndmin=1)
    assert pins.shape==(K,) and np.array_equal(pins,np.asarray(meta['eligible_labels']))
    assert (CACHE/'radius4.u64le.bin').stat().st_size==K*W*8
    assert (CACHE/'target_rows.u64le.bin').stat().st_size==N*TW*8
    balls=np.memmap(CACHE/'radius4.u64le.bin',dtype='<u8',mode='r',shape=(K,W))
    support=np.fromfile(CACHE/'target_support.u16le.bin',dtype='<u2')
    assert support.shape==(N,) and support.min()>0
    csr=np.memmap(CACHE/'source.csr.u32le.bin',dtype='<u4',mode='r')
    assert tuple(map(int,csr[:2]))==(N,2*SOURCE_M)
    offsets=csr[2:N+3]; adjacency=csr[N+3:]
    assert int(offsets[0])==0 and int(offsets[-1])==len(adjacency)==2*SOURCE_M
    eligible_degrees=offsets[pins+1]-offsets[pins]
    assert np.all(eligible_degrees==14)
    cover_nnz=int(support.astype(np.int64).sum()); total_nnz=cover_nnz+K
    indices=np.memmap(HERE/'full_csc_indices.i32le.bin',dtype='<i4',mode='w+',shape=(total_nnz,))
    indptr=np.memmap(HERE/'full_csc_indptr.i32le.bin',dtype='<i4',mode='w+',shape=(K+1,))
    pos=0
    for j in range(K):
        indptr[j]=pos
        rowbits=np.unpackbits(balls[j].view(np.uint8),bitorder='little')[:N]
        targets=np.flatnonzero(rowbits)
        size=len(targets)
        assert size==meta['ball_sizes'][j]
        indices[pos:pos+size]=targets;pos+=size
        indices[pos]=N;pos+=1
    indptr[K]=pos
    assert pos==total_nnz
    # This first full-model row-count binding is not a repeat of the known row dedup.
    model_counts=np.bincount(indices,minlength=N+1)
    assert np.array_equal(model_counts[:N],support) and int(model_counts[N])==K
    del rowbits,targets,model_counts
    indices.flush();indptr.flush()
    data=-np.ones(total_nnz,dtype=np.float64)
    data[np.asarray(indptr[1:])-1]=1.0
    matrix=csc_matrix((data,indices,indptr),shape=(N+1,K),copy=False)
    dims={'variables':K,'binary_variables':K,'actual_target_cover_rows':N,'cardinality_rows':1,
          'rows':N+1,'cover_nonzeros':cover_nnz,'total_nonzeros':total_nnz,
          'matrix_storage_bytes':int(matrix.data.nbytes+matrix.indices.nbytes+matrix.indptr.nbytes),
          'indices_dtype':str(matrix.indices.dtype),'indptr_dtype':str(matrix.indptr.dtype),
          'minimum_actual_target_support':int(support.min()),'maximum_actual_target_support':int(support.max()),
          'all_actual_rows_present':True,'all_eligible_degrees':14,'complete_R4_cache_reused':True,
          'preparation_CPU_seconds':cpu(),'preparation_wall_seconds':time.monotonic()-START_WALL,
          'scipy_version':scipy.__version__,'matrix_files':['full_csc_indices.i32le.bin','full_csc_indptr.i32le.bin'],
          'implicit_MIP_data':'Allcoefficients1;row0..102059lower1upperinf;row102060lower0upper15',
          'source_binding':{'CSR':str(CACHE/'source.csr.u32le.bin'),'eligible':str(CACHE/'eligible.txt'),
                            'balls':str(CACHE/'radius4.u64le.bin'),'target_rows':str(CACHE/'target_rows.u64le.bin')}}
    save('MODEL_DIMENSIONS.json',dims)
    checkpoint('FULL_MODEL_READY',**dims)
    if cpu()>25: raise BudgetStop('Completepreparationexceeded25CPU;nosolverstarted')
    # Full LP includes every cover row and the same cardinality cap.
    begin_solver_stage()
    began=cpu();result['LP_calls']=1
    checkpoint('FULL_LP_RUNNING',configured_solver_wall_seconds=20.0)
    lp=linprog(np.ones(K),A_ub=matrix,b_ub=np.r_[-np.ones(N),15.0],bounds=(0,1),
               method='highs',options={'time_limit':20.0,'threads':1,'presolve':True})
    elapsed=cpu()-began;solver_cpu+=elapsed
    lp_info={'raw_status':int(lp.status),'message':str(lp.message),'CPU_seconds':elapsed,
             'fractional_objective':None if lp.fun is None else float(lp.fun),'all_target_rows':N,
             'cardinality_cap':15,'construction_claim':False,'strict_infeasibility_certificate':None}
    if lp.x is not None:
        np.asarray(lp.x,dtype='<f8').tofile(HERE/'LP_fractional_values.f64le.bin')
    save('LP_RESULT.json',lp_info);result['LP']=lp_info
    if lp.status==2:
        end_solver_stage()
        result['status']='UNCERTIFIED_COMPLETE_LP_MODEL_INFEASIBLE'
    else:
        allowance=min(75.0,95.0-solver_cpu,123.0-cpu())
        if allowance<=0.1: raise BudgetStop('NosolverallowanceleftafteroneLP')
        matrix.data.fill(1.0)
        lower=np.ones(N+1);lower[N]=0.0
        upper=np.full(N+1,np.inf);upper[N]=15.0
        constraints=LinearConstraint(matrix,lower,upper)
        result['MIP_calls']=1;began=cpu()
        checkpoint('FULL_MIP_RUNNING',configured_solver_wall_seconds=allowance,LP_CPU_seconds=solver_cpu)
        answer=milp(np.zeros(K),integrality=np.ones(K,dtype=np.uint8),bounds=Bounds(0,1),
                    constraints=constraints,options={'time_limit':allowance,'threads':1,'presolve':True,
                                                   'mip_rel_gap':0.0,'disp':False})
        end_solver_stage()
        elapsed=cpu()-began;solver_cpu+=elapsed
        mip_info={'raw_status':int(answer.status),'message':str(answer.message),'CPU_seconds':elapsed,
                  'configured_time_limit_seconds':allowance,'integer_incumbent_returned':answer.x is not None,
                  'objective':None if answer.fun is None else float(answer.fun),
                  'strict_infeasibility_certificate':None}
        save('MIP_RESULT.json',mip_info);result['MIP']=mip_info
        if answer.x is None:
            result['status']='UNCERTIFIED_COMPLETE_MIP_MODEL_INFEASIBLE' if answer.status==2 else 'UNKNOWN_NO_INTEGER_INCUMBENT'
        else:
            returned=np.asarray(answer.x);nearest=np.rint(returned)
            assert np.max(np.abs(returned-nearest))<=1e-6 and np.all((nearest==0)|(nearest==1))
            selected=np.flatnonzero(nearest.astype(np.uint8));literal=pins[selected].astype(int).tolist()
            assert 0<len(selected)<=15 and len(set(literal))==len(literal)
            actual_degrees=(offsets[pins[selected]+1]-offsets[pins[selected]]).astype(int).tolist()
            assert all(d<15 for d in actual_degrees)
            union=np.bitwise_or.reduce(balls[selected],axis=0)
            holes=np.flatnonzero(np.unpackbits(union.view(np.uint8),bitorder='little')[:N]==0)
            evidence={'selected_columns':selected.astype(int).tolist(),'pins':literal,'pin_count':len(literal),
                      'actual_source_pin_degrees':actual_degrees,'checked_actual_targets':N,
                      'complete_current_R4_missing':len(holes),'missing_sample':holes[:20].astype(int).tolist(),
                      'integer_values_checked':True,'full_cached_ball_OR_checked':True,'degree_CSR_checked':True}
            save('INCUMBENT_CHECK.json',evidence)
            if len(holes):
                result['status']='IMPLEMENTATION_CONTRADICTION_RETURNED_FULLMODEL_INCUMBENT_UNCOVERED'
            else:
                graph=HERE/'graph_d15_D5_n102061.edges';copied=0
                with graph.open('w',buffering=1048576) as out:
                    out.write(f'{N+1} {SOURCE_M+len(literal)}\n')
                    for u in range(N):
                        for vv in adjacency[int(offsets[u]):int(offsets[u+1])]:
                            v=int(vv)
                            if u<v:
                                out.write(f'{u} {v}\n');copied+=1
                    for v in literal:out.write(f'{v} {N}\n')
                assert copied==SOURCE_M
                hit={'status':'PRODUCER_COMPLETE_102061_RETAINED_EDGE_EXTENSION','source_n':N,'source_m':SOURCE_M,
                     'n':N+1,'m':SOURCE_M+len(literal),'max_degree':15,'new_vertex':N,'new_degree':len(literal),
                     'pins':literal,'actual_source_pin_degrees':actual_degrees,'source_D5_inherited':True,
                     'complete_current_R4_missing':0,'all_old_edges_retained':True,'copied_old_edges':copied,
                     'graph_file':str(graph),'D_at_most':5,'D_exact':5,'D4_Moore_bound':44326,
                     'cached_coverage_evidence':'INCUMBENT_CHECK.json','source_CSR':str(CACHE/'source.csr.u32le.bin'),
                     'newroot_BFS_by_this_worker':0,'independent_first_parameter_check_pending':True}
                save('HIT.json',hit)
                result.update(status=hit['status'],actual_n=N+1,actual_m=hit['m'],actual_D=5,pins=literal,
                              graph_file=str(graph),new_graphs_generated=1)
                checkpoint('COMPLETE_TRUE_HIT',pins=literal,n=N+1,m=hit['m'],complete_R4_missing=0)
except BudgetStop as e:
    end_solver_stage()
    result['status']='UNKNOWN_AGGREGATE_OR_PREPARATION_CPU_LIMIT';result['stop_reason']=str(e)
except Exception as e:
    end_solver_stage()
    result['status']='UNKNOWN_EXECUTION_ERROR';result['execution_error']={'type':type(e).__name__,'message':str(e)}

result.update(full_model=bool(dims),matrix_dimensions=dims,solver_CPU_seconds=solver_cpu,
              worker_CPU_seconds_before_exit=cpu(),worker_wall_seconds=time.monotonic()-START_WALL,
              hit=bool(hit),worker_CPU_hard_seconds=128,newroot_BFS=0)
save('RESULT.json',result)
save('terminal.json',{'status':result['status'],'execution_finished':True,'pending':[],
                      'worker_CPU_seconds_before_exit':cpu(),'hit':bool(hit)})
checkpoint('WORKER_FINISHED',status=result['status'],hit=bool(hit))
