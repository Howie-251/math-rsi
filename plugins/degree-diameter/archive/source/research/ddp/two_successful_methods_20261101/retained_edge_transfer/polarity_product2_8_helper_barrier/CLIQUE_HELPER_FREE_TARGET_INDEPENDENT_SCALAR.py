#!/usr/bin/env python3
"""One tiny integer clique-size check; no graph construction or BFS."""
import json
from pathlib import Path
import resource
import time
resource.setrlimit(resource.RLIMIT_CPU,(2,2))
started=time.process_time()
before=resource.getrusage(resource.RUSAGE_SELF)
r=4;Delta=31;M=325;F=(r+1)*M
rows=[]
for t in range(33):
    q=Delta+1-t
    value=(t+r)*q
    assert value==(r+14)**2-(t-14)**2
    rows.append(dict(t=t,allowed_nonempty_clique=1<=t<=32,
        pins_per_helper_upper_bound=q,class_capacity=value,
        free_target_capacity=(r+1)*value,free_targets=F,
        shortfall=F-(r+1)*value))
allowed=[row for row in rows if row['allowed_nonempty_clique']]
maximum=max(row['class_capacity']for row in allowed)
maximizers=[row['t']for row in allowed if row['class_capacity']==maximum]
assert maximum==324 and maximizers==[14]
assert all(row['free_target_capacity']<F for row in allowed)
assert 5*(10-5)==25  # Algebraic comparison only; do not rerun the230 graph.
after=resource.getrusage(resource.RUSAGE_SELF)
cpu=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
D=Path(__file__).resolve().parent
result=dict(status='SUPPORTED_CLIQUE_HELPER_CAP31_IMPOSSIBILITY_IN_FIXED_MODEL',
    prediction='CLIQUE_HELPER_FREE_TARGET_PREDICTION.md',r=4,cap=31,
    abstract_source_n=8775,abstract_source_generated_here=False,
    classes=325,representatives_per_class=5,free_targets=1625,
    allowed_helper_clique_size_interval=[1,32],maximum_class_capacity=maximum,
    maximizing_t=maximizers,maximum_free_target_capacity=1620,minimum_shortfall=5,
    exhaustive_t0_to32_scalar_rows=rows,t0_is_only_endpoint_relaxation=True,
    proven_route_containment='P union N_F(P) union N_F^2(P_h) union sameclass(P_h)',
    per_helper_free_target_bound='(r+1)(|P|+r*p_h)',
    clique_necessary_condition='325 <= (t+r)(28+r-t)',
    old_matching_offcenter_theorem_used=False,
    K5_calibration=dict(inherited_actual_graph_n=230,no_rerun=True,delta0=9,r=0,M=25,
        necessary_bound='25 <= t*(10-t)',attained_t=5,attained_capacity=25),
    new_exclusion_scope='Only cap31 complete helper cliques, arbitrary F-F edges, fixed source/complete uniform r4 copying/all mandatory edges retained',
    inherited_not_new_exclusions='r0..3/caps27..30 from earlier650-target barrier',
    arbitrary_nonclique_helpers_excluded=False,
    CPU_seconds_rusage=cpu,CPU_seconds_process_time=time.process_time()-started,CPU_limit_seconds=2,
    operations=dict(tiny_scalar_runs=1,graph_generation=0,field_geometry=0,BFS=0,solver=0,
        Lean=0,paid_review=0,web=0,old_toy_rerun=0,factor_subset_enumeration=0),
    portfolio_increment=0,new_parameter_increment=0,Lean_increment=0,
    root_counts_Wiki_frozen_artifacts_modified=False)
(D/'CLIQUE_HELPER_FREE_TARGET_INDEPENDENT_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
terminal=dict(state=result['status'],running=False,active_processes=[],
    CPU_seconds_rusage=cpu,CPU_limit_seconds=2,nonclique_solver_or_new_queue_started=False,
    graph_increment=0,Lean_increment=0,existing_A_B_C_scope_used=False,
    root_counts_Wiki_frozen_artifacts_modified=False)
(D/'CLIQUE_HELPER_FREE_TARGET_INDEPENDENT_TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
print(json.dumps(dict(status=result['status'],maximum_class_capacity=maximum,
    maximizing_t=maximizers,maximum_free_target_capacity=1620,minimum_shortfall=5,
    CPU_seconds_rusage=cpu)))
