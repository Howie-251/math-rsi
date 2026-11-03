import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:
    os.environ[name]='1'
import resource
resource.setrlimit(resource.RLIMIT_CPU,(89,90))
import json,signal,time
from datetime import datetime,timezone
from pathlib import Path

HERE=Path(__file__).resolve().parent;BASE=HERE.parent;CACHE=BASE/'allfree_cover_probe'
N=94186;K=3685;W=1472;COVER_NNZ=60334203;TOTAL_NNZ=60337888
START_UTC=datetime.now(timezone.utc).isoformat();START_WALL=time.monotonic()
def cpu():
    r=resource.getrusage(resource.RUSAGE_SELF);return r.ru_utime+r.ru_stime
def save(name,value):(HERE/name).write_text(json.dumps(value,indent=2)+'\n')
def checkpoint(stage,**kw):
    value={'stage':stage,'pid':os.getpid(),'start_UTC':START_UTC,'CPU_seconds':cpu(),'wall_seconds':time.monotonic()-START_WALL,**kw}
    save('checkpoint.json',value);save('RUN_HANDLE.json',{'status':stage,'running':True,**value})
class BudgetReached(Exception):pass
def cpu_signal(*args):raise BudgetReached('Worker89CPU softlimit')
signal.signal(signal.SIGXCPU,cpu_signal)
checkpoint('IMPORTING_NUMERICAL_LIBRARIES')
import numpy as np
import scipy
from scipy.sparse import csc_array
from scipy.optimize import milp,Bounds,LinearConstraint
import warnings
warnings.filterwarnings('ignore',message='Unrecognized options detected:.*threads.*')

status='UNKNOWN_NOT_SOLVED';solver_info=None;hit=None;dims=None
try:
    meta=json.loads((CACHE/'BALLS_META.json').read_text())
    pins=np.asarray(meta['free_vertices'],dtype=np.int32)
    assert meta['complete'] and meta['source_n']==N and meta['source_m']==657452
    assert len(pins)==K and meta['words_per_row']==W and meta['computed_vertices']==meta['free_vertices']
    degree=np.fromfile(BASE/'degree14.u8.bin',dtype=np.uint8)
    assert degree.shape==(N,) and np.array_equal(pins,np.flatnonzero(degree<14))
    path=CACHE/'allfree_R4.u64le.bin';assert path.stat().st_size==K*W*8
    balls=np.memmap(path,dtype='<u8',mode='r',shape=(K,W))
    support=np.fromfile(CACHE/'target_support.u16le.bin',dtype='<u2')
    assert len(support)==N and int(support.sum())==COVER_NNZ and int(support.min())>0
    checkpoint('ALLOCATING_FULL_CSC',matrix_shape=[N+1,K],cover_rows=N,expected_nonzeros=TOTAL_NNZ)
    indices=np.empty(TOTAL_NNZ,dtype=np.int32)
    indptr=np.empty(K+1,dtype=np.int32)
    data=np.ones(TOTAL_NNZ,dtype=np.float64)
    pos=0
    for j in range(K):
        indptr[j]=pos
        bitrow=np.unpackbits(balls[j].view(np.uint8),bitorder='little')[:N]
        targets=np.flatnonzero(bitrow)
        size=len(targets);indices[pos:pos+size]=targets;pos+=size
        indices[pos]=N;pos+=1
        if j%256==0:checkpoint('BUILDING_FULL_CSC',columns_completed=j+1,nonzeros_filled=pos,matrix_shape=[N+1,K])
    indptr[K]=pos;assert pos==TOTAL_NNZ
    del bitrow,targets
    matrix=csc_array((data,indices,indptr),shape=(N+1,K),copy=False)
    lower=np.ones(N+1);lower[N]=0
    upper=np.full(N+1,np.inf);upper[N]=14
    constraints=LinearConstraint(matrix,lower,upper)
    dims={'variables':K,'binary_variables':K,'true_target_cover_rows':N,'cardinality_rows':1,'rows':N+1,'cover_nonzeros':COVER_NNZ,'total_nonzeros':int(matrix.nnz),'matrix_storage_bytes':int(matrix.data.nbytes+matrix.indices.nbytes+matrix.indptr.nbytes),'CSC_data_dtype':str(matrix.data.dtype),'CSC_indices_dtype':str(matrix.indices.dtype),'preparation_CPU_seconds':cpu(),'preparation_wall_seconds':time.monotonic()-START_WALL,'scipy_version':scipy.__version__,'full_target_model':True,'source_BFS':0,'ball_recomputation':0}
    save('MODEL_DIMENSIONS.json',dims)
    allowance=87.0-cpu()
    if allowance<=0.1:raise BudgetReached('Preparationusedremainingbudget')
    checkpoint('SOLVING_FULL_TARGET_MILP',matrix_dimensions=dims,solver_start_CPU_seconds=cpu(),solver_allowance_wall_seconds=allowance)
    print(json.dumps({'stage':'SOLVING_FULL_TARGET_MILP','pid':os.getpid(),'prep_CPU_seconds':cpu(),'rows':N+1,'columns':K,'nonzeros':int(matrix.nnz),'allowance_wall_seconds':allowance}),flush=True)
    began=cpu()
    answer=milp(np.zeros(K),integrality=np.ones(K,dtype=np.uint8),bounds=Bounds(0,1),constraints=constraints,options={'time_limit':allowance,'threads':1,'mip_rel_gap':0.0,'presolve':True,'disp':False})
    solver_info={'raw_status':int(answer.status),'message':str(answer.message),'solver_CPU_seconds':cpu()-began,'objective':None if answer.fun is None else float(answer.fun),'integer_incumbent_returned':answer.x is not None,'full_target_model':True,'strict_infeasibility_certificate':None}
    save('SOLVER_RESULT.json',solver_info)
    if answer.x is None:
        status='UNCERTIFIED_SOLVER_MODEL_INFEASIBLE' if answer.status==2 else 'UNKNOWN_NO_INCUMBENT'
    else:
        x=np.asarray(answer.x);nearest=np.rint(x)
        if np.max(np.abs(x-nearest))>1e-6 or not np.all((nearest==0)|(nearest==1)):
            status='UNKNOWN_NONINTEGRAL_RETURN'
        else:
            selected=np.flatnonzero(nearest.astype(np.uint8));literal=pins[selected].astype(int).tolist()
            assert len(selected)<=14 and all(int(degree[v])<14 for v in literal)
            union=np.bitwise_or.reduce(balls[selected],axis=0) if len(selected) else np.zeros(W,dtype='<u8')
            missing=np.flatnonzero(np.unpackbits(union.view(np.uint8),bitorder='little')[:N]==0)
            evidence={'selected_columns':selected.astype(int).tolist(),'pins':literal,'pin_count':len(literal),'source_pin_degrees':[int(degree[v]) for v in literal],'complete_cached_R4_missing_count':len(missing),'missing_target_sample':missing[:20].astype(int).tolist(),'binary_discrete_recheck':True,'actual_cached_degree_recheck':True,'complete_R4_OR_checked':True}
            save('INCUMBENT_CHECK.json',evidence)
            if len(missing):
                status='IMPLEMENTATION_CONTRADICTION_FULL_MODEL_INCUMBENT_UNCOVERED'
            else:
                status='PRODUCER_COMPLETE_94187_EXTENSION'
                hit={'status':status,'source_file':str(BASE/'source94186.edges'),'source_n':N,'source_m':657452,'newlabel':N,'n':N+1,'m':657452+len(literal),'max_degree':14,'new_degree':len(literal),'pins':literal,'preserve_all_source_edges':True,'source_D5_inherited':True,'complete_current_R4_missing':0,'cached_proof':evidence,'generator':'generate.py --parameters HIT.json --output graph.edges','actual_newroot_BFS':0,'ordinary_bad_unordered_pairs':None}
                save('HIT.json',hit)
                print(json.dumps({'stage':status,'pins':literal,'n':N+1,'R4_missing':0}),flush=True)
except BudgetReached as e:
    status='UNKNOWN_AGGREGATE_CPU_LIMIT';save('BUDGET_STOP.json',{'reason':str(e),'CPU_seconds':cpu()})
except Exception as e:
    status='UNKNOWN_EXECUTION_ERROR';save('EXECUTION_ERROR.json',{'type':type(e).__name__,'message':str(e),'CPU_seconds':cpu()})

result={'status':status,'target_Delta':14,'target_D':5,'savedL':94186,'hypothetical_n':94187,'actual_n':94187 if hit else None,'actual_D':None,'ordinary_bad_unordered_pairs':None,'full_target_model':bool(dims),'matrix_dimensions':dims,'solver':solver_info,'hit':bool(hit),'new_graph_objects':int(bool(hit)),'newroot_BFS':0,'source_BFS':0,'ball_recomputation':0,'worker_CPU_seconds_before_exit':cpu(),'hard_worker_CPU_seconds':90,'wall_seconds_before_exit':time.monotonic()-START_WALL,'prediction':'SUPPORTED_CACHED_COMPLETE_COVER' if hit else 'UNRESOLVED_UNCERTIFIED_INFEASIBILITY' if status=='UNCERTIFIED_SOLVER_MODEL_INFEASIBLE' else 'UNKNOWN','family_strictly_excluded':False}
save('RESULT.json',result)
save('terminal.json',{'status':status,'execution_finished':True,'pending':[],'worker_CPU_seconds_before_exit':cpu(),'hit':bool(hit)})
save('RUN_HANDLE.json',{'status':status,'running':False,'execution_finished':True,'pid':os.getpid(),'start_UTC':START_UTC,'worker_CPU_seconds_before_exit':cpu()})
print(json.dumps({k:v for k,v in result.items() if k!='matrix_dimensions'},indent=2),flush=True)
