from pathlib import Path
import json,re,time
start=time.process_time();D=Path(__file__).resolve().parent
s=json.loads((D/'CHECKPOINT.json').read_text());h=json.loads((D/'DRIVER_HANDLE.json').read_text())
assert not s['running']and len(s['completed'])==8
audit=D/'F4Graph1920PilotAudit_attempt001.log';text=audit.read_text()
assert 'sorryAx'not in text and 'error:'not in text
name='DegreeDiameter.Portfolio.F4Graph1920.Row0.row0_full_walk_bound'
found=re.search(re.escape("'"+name+"' depends on axioms:")+r'\s*\[([^]]*)\]',text)
assert found and set(x.strip()for x in found.group(1).split(','))=={'propext','Classical.choice','Quot.sound'}
rowmods={'F4Graph1920Row0Data','F4Graph1920Row0Certificate','F4Graph1920Row0Walks'}
perrow=sum(a['CPU_seconds']for a in s['attempts']if a['PASS']and a['module']in rowmods)
base=max(s['CPU_seconds'],h['CPU_seconds']);total=base+time.process_time()-start
record=dict(status='PILOT_COMPLETE_LITERAL_DEFS_MATRIX_WALKS_ONE_FULL_ROW_KERNEL_PASS_FULL_TARGETS_PENDING',
    CPU_seconds=total,CPU_budget_seconds=120,remaining_pilot_CPU_seconds=120-total,
    preparation_CPU_seconds=s['preparation_CPU_seconds'],completed_modules=s['completed'],attempts=s['attempts'],
    failed_attempts=1,failed_attempt_explanation='New Definitions lacked cached Fin sum-equivalence import; minimal import repair passed. Failure cost retained.',
    maximum_module_CPU_seconds=max(a['CPU_seconds']for a in s['attempts']),
    actual_complete_row_certificate_CPU_seconds=23.170562,row_data_certificate_Walk_CPU_seconds=perrow,
    actual_row_source_controller=0,actual_row_NB_pairs=26,actual_row_NB_basis_checks=78,
    actual_row_adjacent_darts=4,actual_row_adjacent_residual_checks=256,
    actual_genuine_Walk_theorem=name,
    actual_genuine_Walk_type='forall x:Fin64 v:Fin1920, exists w:graph.Walk (liftAt 0 x) v, w.length<=3',
    source_vertices_covered_by_this_parameterized_row=64,source_targets_each=1920,
    source_degree_le16_kernel_PASS=True,source_reverse_matrix_basis_checks=360,source_reverse_direction_checks=120,
    source_label='Fin1920',clone_label='Fin2016',clone_FinalClaim_only_typed_not_proved=True,
    no_user_certificate_premises_on_row_Walk_theorem=True,axioms=['propext','Classical.choice','Quot.sound'],
    standalone_pilot_Audit=str(audit),source_full_D3_kernel_complete=False,clone2016_final_claim_kernel_complete=False,
    remaining_source_rows=29,remaining_controller_pairs=870,remaining_NB_pairs=754,remaining_adjacent_darts=116,remaining_adjacent_residual_checks=7424,
    same_design_remaining_row_CPU_extrapolation=29*perrow,
    assembly_lower_clone_externalbinding_additional_CPU_allowance=75,
    same_design_cumulative_CPU_central_estimate=total+29*perrow+75,
    proposed_future_cumulative_CPU_ceiling=1200,future_full_queue_authorized_or_started=False,
    old_PASSED_field_finite_source_generic_modules_modified_or_recompiled=False,
    source_graph_BFS_old_rank_verifier_solver_paidreview_runs=0,new_native_decide_sorry_or_axioms=False,
    concrete_Lean_increment=0,root_counts_expert_frozen_files_modified=False,running=False,active_modules=[])
for name in['RESULT.json','TERMINAL.json']:(D/name).write_text(json.dumps(record,indent=2)+'\n')
(D/'DRIVER_HANDLE.json').write_text(json.dumps(dict(status=record['status'],running=False,active_modules=[],CPU_seconds=total,CPU_budget_seconds=120),indent=2)+'\n')
(D/'STAGE_STATE.json').write_text(json.dumps(dict(status=record['status'],running=False,active_modules=[],completed_modules=8,pilot_complete=True,full_source_or_clone_complete=False,CPU_seconds=total),indent=2)+'\n')
print(json.dumps(dict(status=record['status'],CPU_seconds=total,row_complete_cost=perrow,remaining29row_estimate=29*perrow,central_full_estimate=record['same_design_cumulative_CPU_central_estimate'],running=False)))
