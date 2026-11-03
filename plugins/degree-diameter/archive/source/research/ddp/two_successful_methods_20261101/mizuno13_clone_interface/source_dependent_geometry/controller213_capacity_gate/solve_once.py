from pathlib import Path
from collections import Counter
from datetime import datetime,timezone
import os,time,json,resource,warnings
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name]='1'
D=Path(__file__).resolve().parent;G=D.parent;S=G.parent
START=time.process_time();WALL=time.monotonic()
resource.setrlimit(resource.RLIMIT_CPU,(59,60))
def save(name,x):(D/name).write_text(json.dumps(x,indent=2)+'\n')
assert not (D/'SOLVER_HANDLE.json').exists(),'Single-call batch already started; do not restart.'
handle={'status':'PREPARING','PID':os.getpid(),'started_UTC':datetime.now(timezone.utc).isoformat(),'solver':'scipy.optimize.milp/installed HiGHS','solver_time_limit_seconds':55,'whole_process_CPU_soft_limit':59,'whole_process_CPU_hard_limit':60,'threads':1,'solver_calls':0,'running':True}
save('SOLVER_HANDLE.json',handle);print(json.dumps(handle),flush=True)
try:
    import numpy as np
    from scipy.optimize import Bounds,LinearConstraint,milp
    from scipy.sparse import csc_matrix
except ImportError as e:
    out={**handle,'status':'NO_INSTALLED_SOLVER_NO_CALL','solver_calls':0,'running':False,'pending':[],'process_CPU_seconds':time.process_time()-START}
    save('RESULT.json',out);save('SOLVER_HANDLE.json',out);print(json.dumps(out),flush=True);raise SystemExit(0)
C=json.loads((S/'LINE_KERNELS.json').read_text())['chart'];M=json.loads((S/'MAPPING_DATA.json').read_text());R=json.loads((G/'RESULT.json').read_text());E=json.loads((G/'exceptional_g4_gate/EXCEPTIONAL_SOURCE_RESULTS.json').read_text())['source_records']
g4={int(a) for a,g in R['source_gmax'].items() if g==4}|{r['source'] for r in E if r['has_local_g4']}
assert len(g4)==203 and len(C)==364
cost=[5 if a in g4 else 6 for a in range(364)];mt=M['main_fiber_target'];A=[[0]*364 for _ in range(364)];incoming=[[] for _ in range(364)]
for a,row in enumerate(C):
    assert len(row)==4 and len({e['target'] for e in row})==4
    assert mt[a]!=a and mt[mt[a]]==a and mt[a] in [e['target'] for e in row]
    for e in row:A[e['target']][a]+=1;incoming[e['target']].append(a)
    A[mt[a]][a]+=1
assert all(len(v)==4 and len(set(v))==4 for v in incoming)
assert all(sum(row)==5 and Counter(v for v in row if v)=={1:3,2:1} for row in A)
assert all(sum(A[b][a] for b in range(364))==5 and Counter(A[b][a] for b in range(364) if A[b][a])=={1:3,2:1} for a in range(364))
assert all(A[b][mt[b]]==2 for b in range(364))
model={'binary_variables':364,'controller_rows':364,'ordinary_incoming':incoming,'M_mate':mt,'source_cost':cost,'row_sparse_coefficients':[[[a,z] for a,z in enumerate(row) if z] for row in A],'all_controller_row_sums':5,'all_controller_column_sums':5,'coefficient_pattern_every_row_column':{'1':3,'2':1},'cardinality_lower':213,'cost_upper':1092,'solver_objective':'zero feasibility','g4_sources':sorted(g4),'cost_histogram':dict(Counter(cost)),'row_formula':'sum_ordinary_incoming x_a + x_mate(b) <=3','point_graph_generated':False,'P_load_ignored_as_relaxation':True,'affine_normal_phase_constraints_ignored_as_relaxation':True}
save('MODEL.json',model)
Aall=csc_matrix(np.asarray(A+[[1]*364,cost],dtype=np.float64));lb=np.asarray([-np.inf]*364+[213,-np.inf]);ub=np.asarray([3]*364+[np.inf,1092])
handle.update(status='RUNNING',solver_calls=1,pre_solver_CPU_seconds=time.process_time()-START);save('SOLVER_HANDLE.json',handle);print(json.dumps(handle),flush=True)
SOLVESTART=time.process_time()
with warnings.catch_warnings(record=True) as ws:
    warnings.simplefilter('always')
    ans=milp(c=np.zeros(364),integrality=np.ones(364),bounds=Bounds(np.zeros(364),np.ones(364)),constraints=LinearConstraint(Aall,lb,ub),options={'time_limit':55.,'threads':1,'presolve':True,'mip_rel_gap':0.,'disp':True})
solveCPU=time.process_time()-SOLVESTART
accepted=False;verify={};candidate=None
if ans.x is not None:
    values=[float(v) for v in ans.x];candidate=[int(round(v)) for v in values];err=max(abs(v-q) for v,q in zip(values,candidate))
    # Recompute from source lists and matching map, not the numeric solver matrix.
    lhs=[sum(candidate[a] for a in incoming[b])+candidate[mt[b]] for b in range(364)];count=sum(candidate);weighted=sum(c*x for c,x in zip(cost,candidate))
    accepted=err<=1e-6 and all(x in (0,1) for x in candidate) and max(lhs)<=3 and count>=213 and weighted<=1092
    verify={'max_rounding_error':err,'all_binary':all(x in (0,1) for x in candidate),'selected_count':count,'source_cost':weighted,'controller_row_values':lhs,'row_value_histogram':dict(Counter(lhs)),'max_controller_row':max(lhs),'all364_rows_cardinality_cost_pass':accepted}
    if accepted:save('FEASIBLE_VECTOR.json',{'status':'CONTROLLER_NECESSARY_CAPACITY_ONLY','x':candidate,'selected_sources':[a for a,x in enumerate(candidate) if x],'verification':verify,'full_graph_or_phase_assignment_claimed':False})
status='FEASIBLE_CONTROLLER_CAPACITY_ONLY' if accepted else ('RAW_HIGHS_INFEASIBLE' if ans.status==2 else 'UNKNOWN_NO_ACCEPTED_CONTROLLER_VECTOR')
out={'status':status,'PID':os.getpid(),'started_UTC':handle['started_UTC'],'finished_UTC':datetime.now(timezone.utc).isoformat(),'raw_status':int(ans.status),'raw_message':str(ans.message),'solver_success':bool(ans.success),'solver_calls':1,'threads':1,'solver_time_limit_seconds':55,'pre_solver_CPU_seconds':handle['pre_solver_CPU_seconds'],'solver_CPU_seconds':solveCPU,'process_CPU_seconds':time.process_time()-START,'wall_seconds':time.monotonic()-WALL,'verification':verify,'mip_node_count':None if getattr(ans,'mip_node_count',None) is None else int(ans.mip_node_count),'mip_gap':None if getattr(ans,'mip_gap',None) is None else float(ans.mip_gap),'warnings':[str(w.message) for w in ws],'BFS_runs':0,'complete_graphs':0,'new_graphs':0,'running':False,'pending':[],'automatic_continuation':False,'scope':'Binary source selection necessary relaxation only, including all364 sources. No phase, M/P point-disjointness or target-normal compatibility model. Raw infeasibility is not an independently verified proof.'}
for name in ['RESULT.json','SOLVER_HANDLE.json','TERMINAL.json']:save(name,out)
print(json.dumps(out),flush=True)
