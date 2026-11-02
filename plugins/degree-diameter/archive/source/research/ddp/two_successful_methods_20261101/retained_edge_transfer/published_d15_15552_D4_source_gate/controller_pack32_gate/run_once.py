#!/usr/bin/env python3
import os
os.environ['OMP_NUM_THREADS']='1'
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['MKL_NUM_THREADS']='1'
from pathlib import Path
import collections
import json
import math
import resource
import time
import warnings

HERE=Path(__file__).resolve().parent
PARENT=HERE.parent
PRIOR=json.loads((PARENT/'CONTROL_PACKING_TERMINAL.json').read_text())['CPU_seconds']
PREP=0.2
BUDGET=45.0
def save(name,value):(HERE/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
def charged():return PRIOR+PREP+time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(math.floor(BUDGET-PRIOR-PREP),math.floor(BUDGET-PRIOR-PREP)))
save('HANDLE.json',{'pid':os.getpid(),'phase':'imports_and_literal_model','running':True,'worker_count':1,
                     'prior_sourcepacking_CPU_seconds':PRIOR,'cumulative_CPU_budget_seconds':BUDGET,'solver_wall_limit_seconds':30})
try:
    import numpy as np
    import scipy
    from scipy.optimize import Bounds,LinearConstraint,milp
    from scipy.sparse import coo_matrix
except ImportError as exc:
    terminal={'status':'SCIPY_UNAVAILABLE_NO_SOLVER_CALL','error':str(exc),'running':False,'all_processes_terminal':True,
              'prior_sourcepacking_CPU_seconds':PRIOR,'new_preparation_charge_seconds':PREP,
              'actual_new_process_CPU_seconds':time.process_time(),'cumulative_charged_CPU_seconds':charged(),
              'cumulative_CPU_budget_seconds':BUDGET,'solver_calls':0,'no_install':True}
    save('RESULT.json',terminal);save('TERMINAL.json',terminal);save('HANDLE.json',terminal)
    print(json.dumps(terminal,indent=2));raise SystemExit(0)

literal=(PARENT/'ACTUAL_CONTROLLER_TARGETS.txt').read_text()
rows=[list(map(int,line.split())) for line in literal.splitlines() if line.strip()]
assert rows[0]==[192,5] and len(rows)==193
targets={}
for row in rows[1:]:
    a,*ts=row
    assert 0<=a<192 and a not in targets and len(ts)==len(set(ts))==5 and all(0<=t<192 for t in ts)
    targets[a]=ts
assert set(targets)==set(range(192))
(HERE/'TARGETS_INPUT.txt').write_text(literal)
rr=[];cc=[];vv=[]
for a in range(192):
    for t in targets[a]:rr.append(t);cc.append(a);vv.append(1.0)
    rr.append(192);cc.append(a);vv.append(1.0)
A=coo_matrix((vv,(rr,cc)),shape=(193,192)).tocsc()
lb=np.full(193,-np.inf);ub=np.ones(193)
lb[192]=32.0;ub[192]=np.inf
model={'binary_variables':192,'target_constraint_rows':192,'cardinality_rows':1,'nonzeros':int(A.nnz),
       'objective':'zero feasibility','target_rows':'sum{x_i:t in T_i}<=1','cardinality':'sumx>=32',
       'source_literal':'../ACTUAL_CONTROLLER_TARGETS.txt','self_controller_memberships_kept':sum(a in ts for a,ts in targets.items()),
       'scipy_version':scipy.__version__,'options':{'disp':True,'presolve':True,'time_limit':30.0,'threads':1},
       'oldfield_rank_graph_BFS':0,'prior_sourcepacking_CPU_seconds':PRIOR,'cumulative_CPU_budget_seconds':BUDGET}
save('MODEL.json',model)
old=json.loads((PARENT/'CONTROL_PACKING_RESULT.json').read_text())['selected_controller_labels']
oldload=collections.Counter(t for a in old for t in targets[a])
assert len(old)==31 and max(oldload.values())==1
save('BASELINE31_MODEL_SANITY.json',{'selected_old31':old,'target_rows_satisfied':True,
                                   'only_new_cardinality_row_violated':True,'cardinality':31,'required':32,
                                   'old_search_not_repeated':True})
save('HANDLE.json',{'pid':os.getpid(),'phase':'one_HiGHS_feasibility_call','running':True,'worker_count':1,
                     'solver_wall_limit_seconds':30.0,'prior_sourcepacking_CPU_seconds':PRIOR,
                     'cumulative_CPU_budget_seconds':BUDGET,'CPU_before_solver':charged()})
solver_cpu0=time.process_time();wall0=time.monotonic()
fdout=os.dup(1);fderr=os.dup(2)
with (HERE/'SOLVER.log').open('w') as log:
    os.dup2(log.fileno(),1);os.dup2(log.fileno(),2)
    try:
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('always')
            res=milp(c=np.zeros(192),integrality=np.ones(192),bounds=Bounds(np.zeros(192),np.ones(192)),
                     constraints=LinearConstraint(A,lb,ub),options=model['options'])
    finally:
        os.dup2(fdout,1);os.dup2(fderr,2);os.close(fdout);os.close(fderr)
solver_cpu=time.process_time()-solver_cpu0;solver_wall=time.monotonic()-wall0
save('SCIPY_WARNINGS.json',[str(w.message) for w in caught])

def finite_number(value):
    if value is None:return None
    value=float(value)
    return value if math.isfinite(value) else None

x=res.x.tolist() if getattr(res,'x',None) is not None else None
binding=None;selected=None
if x is not None:
    rounded=[int(round(z)) for z in x]
    residual=max(abs(a-b) for a,b in zip(x,rounded))
    if residual<=1e-6 and all(z in (0,1) for z in rounded):
        chosen=[a for a,z in enumerate(rounded) if z]
        loads=[sum(t in targets[a] for a in chosen) for t in range(192)]
        valid=len(chosen)>=32 and all(z<=1 for z in loads)
        binding={'actual_selected_count':len(chosen),'max_integrality_residual':residual,
                 'all192_target_rows_checked_once_from_literal':True,'all_target_loads_at_most1':all(z<=1 for z in loads),
                 'cardinality_at_least32':len(chosen)>=32,'integer_incumbent_valid':valid,
                 'target_load_histogram':dict(collections.Counter(loads)),
                 'unique_selected_target_labels':sum(z>0 for z in loads)}
        if valid:
            selected=chosen
            save('SELECTED_BLOCKS.json',{'status':'FROZEN_VALID_CONTROLLER_PACKING_INTERFACE_ONLY',
                'selected_controller_count':len(chosen),'selected_controllers':chosen,
                'selected_target_sets':[targets[a] for a in chosen],
                'whole_plane':'W={x1=0},27points/controller;sourcecompletedtargetsretainedincluding self',
                'conditional_center_count':27*len(chosen),'conditional_graph_order':15552+27*len(chosen),
                'actual_graph_generated':False,'maximality_or_global_priority_proved':False})
            with (HERE/'SELECTED_TARGET_ROWS.tsv').open('w') as f:
                f.write('selection_index\tcontroller\tt0\tt1\tt2\tt3\tt4\n')
                for i,a in enumerate(chosen):f.write('\t'.join(map(str,[i,a,*targets[a]]))+'\n')
            with (HERE/'TARGET_LOAD_BINDING.csv').open('w') as f:
                f.write('target,selected_block_load\n')
                for t,z in enumerate(loads):f.write(f'{t},{z}\n')
    else:
        binding={'integer_incumbent_valid':False,'max_integrality_residual':residual}
save('INCUMBENT_BINDING.json',binding)
if selected is not None:status='FOUND_GE32_CONTROLLER_INTERFACE_ONLY'
elif int(res.status)==2:status='INFEASIBLE_GE32_MODEL_HIGHS_TERMINAL'
else:status='UNKNOWN_NO_VALID_GE32_INCUMBENT'
result={'status':status,'prediction':'Atleast32whole27controllerblocks exist;conditionalorder>=16416.',
        'prediction_supported':selected is not None,'solver_status_code':int(res.status),
        'solver_success':bool(res.success),'solver_message':str(res.message),'solver_calls':1,
        'solver_objective':finite_number(getattr(res,'fun',None)),
        'solver_mip_node_count':finite_number(getattr(res,'mip_node_count',None)),
        'solver_mip_dual_bound':finite_number(getattr(res,'mip_dual_bound',None)),
        'solver_mip_gap':finite_number(getattr(res,'mip_gap',None)),
        'dual_bound_scope':'Zero-objective feasibility bound;notamaximumpackingcardinalitybound',
        'solver_x':x,'incumbent_binding':binding,'selected_controllers':selected,
        'actual_selected_count':len(selected) if selected is not None else None,
        'conditional_new_centers':27*len(selected) if selected is not None else None,
        'conditional_graph_order':15552+27*len(selected) if selected is not None else None,
        'actual_graph_generated':False,'graph_legality_or_latest_public_record_claimed':False,
        'existing31_was_not_an_optimum':True,'same_GE32_prior_strict_NO_or_UNKNOWN_located':False,
        'numerical_infeasibility_scope':'Ifstatus2,actualsolverterminalofthisexactbinarymodel;noLeanprooforexternalinfeasibilitycertificateclaimed',
        'solver_CPU_seconds':solver_cpu,'solver_wall_seconds':solver_wall,
        'prior_sourcepacking_CPU_seconds':PRIOR,'new_preparation_charge_seconds':PREP,
        'actual_new_process_CPU_seconds':time.process_time(),'cumulative_charged_CPU_seconds':charged(),
        'cumulative_CPU_budget_seconds':BUDGET,'worker_count':1,'model':model,
        'new_graph_BFS_field_rank_kernel_ARIS_install_or_hash':0,
        'root_Wiki_modified':False,'new_graph_parameter_Lean_increment':[0,0,0],
        'next':'FREEZE_ONE_SELECTION_REPORT_ROOT_THEN_STOP' if selected is not None else 'STOP_NO_TIMER_SEED_MODEL_EXTENSION'}
save('RESULT.json',result)
interpretation=(f'Oneactual{len(selected)}-controllerpackingwasfoundandbound,with{5*len(selected)}distincttargetlabels;itwasfrozenwithouttrimmingorenlarging.' if selected is not None else
                'HiGHSreturnedactualinfeasibleforthe>=32binarymodel,notatimeout.ThisisnumericMIPevidenceatthespecifiedmodelscale;noformalcertificateisclaimed.' if int(res.status)==2 else
                'Nolegal>=32incumbentwasreturnedintheoneboundedcall;thefamilyremainsUNKNOWN.Noretryisstarted.')
(HERE/'NOTE.md').write_text(f'''# Whole27 block feasibility target32

Actualstatus:{status}. {interpretation}

OldFOUND31stoppedatfirst31,exhausted=false,notamaximum. The192-rowliteralTinputandall24selfmembershipsarepreserved. Themodelhas192binaryvariables,192targetloadrowsandone>=32cardinalityrow,objective0. Theknown31selectionpassesalltargetrowsandfailsonlythenewcardinalityrow,sothenewmodelwasnotmistakenforanoldstrictNO.

OneHiGHSfeasibilitycall,status{int(res.status)}:{str(res.message)}. Incumbent,rowbindingandactualrawstatus/dual/nodefieldsareinRESULTandINCUMBENT_BINDING;thedualobjectiveisnotacardinalityupperbound. Sourceedgesandoldfield/rank/BFSwerenotreadorrevalidated. Thismodeltestswholecontrollerblocks,notarbitrarypointlevelpacking.

Apositivecertificateonlyprovidestheconditionalacceptedplane/fullNinterface:n=15552+27kwithmaxdegree<=16andsourcederivedroutingifproducedandverified.Noactualgraph,fullNpinbinding,freshdiameter/kernel,globalpriorityorgraphcountisclaimed. Rootseparatelychecksbaselineandauthorizesanyproduction. Keeponeactualselectionevenifk>32;nomaximum/prefix/degreefamilyisgenerated.

Budgetinherits{PRIOR:.9f};newpreparationcharge{PREP},singleprocessandallimports/solver/outputincluded. SolverCPU{solver_cpu:.9f},wall{solver_wall:.9f}withinrequested30s. Cumulative{charged():.9f}/45CPU,oneworker. Noresume,secondseed,changedmodel,solverinstallation,graph/BFS/Lean/ARIS/hashorroot/Wikiedits.
''')
terminal={'status':status,'running':False,'all_processes_terminal':True,'solver_calls':1,'worker_count':1,
          'solver_status_code':int(res.status),'solver_CPU_seconds':solver_cpu,'solver_wall_seconds':solver_wall,
          'prior_sourcepacking_CPU_seconds':PRIOR,'new_preparation_charge_seconds':PREP,
          'actual_new_process_CPU_seconds':time.process_time(),'cumulative_charged_CPU_seconds':charged(),
          'cumulative_CPU_budget_seconds':BUDGET,'no_timer_reset':True,'no_automatic_continuation':True}
save('TERMINAL.json',terminal);save('HANDLE.json',{'pid':os.getpid(),'phase':'terminal',**terminal})
print(json.dumps({'status':status,'selected_controllers':selected,'k':len(selected)if selected is not None else None,
                  'conditional_n':result['conditional_graph_order'],'solver_status':int(res.status),
                  'solver_message':str(res.message),'terminal':terminal},ensure_ascii=False,indent=2))
