import json,re,time
from pathlib import Path
started=time.process_time();D=Path(__file__).resolve().parent
def save(name,value):(D/name).write_text(json.dumps(value,indent=2)+'\n')
s=json.loads((D/'CHECKPOINT.json').read_text());assert not s['running']
required=['F3Graph15552Definitions','F3Graph15552Linear','F3Graph15552Routes',
          'F3Graph15552PilotData','F3Graph15552PilotCertificate','F3Graph15552PilotWalks','F3Graph15552PilotAudit']
assert all(m in s['completed']for m in required)
assert 'F3Graph15552Row0Data'in s['completed']and'F3Graph15552Row0FullrankCertificate'in s['completed']
audit=[a for a in s['attempts']if a['module']=='F3Graph15552PilotAudit'and a['PASS']][-1]
text=Path(audit['log']).read_text();assert'sorryAx'not in text
axioms=re.findall(r'depends on axioms:\s*\[([^]]*)\]',text,re.S)
standard={'propext','Classical.choice','Quot.sound'}
assert axioms and all({a.strip()for a in names.split(',')if a.strip()}<=standard for names in axioms)
preps=[]
for path in sorted(D.glob('*PREPARATION_RESULT.json')):
    r=json.loads(path.read_text());preps.append(dict(file=path.name,CPU_seconds=r.get('CPU_seconds',r.get('code_preparation_CPU_seconds',0.))))
cost=sum(p['CPU_seconds']for p in preps)+s['driver_CPU_seconds']+sum(a['CPU_seconds']for a in s['attempts'])
forecast=json.loads((D/'ROW0_COST_PREPARATION_RESULT.json').read_text())
initial=forecast['baseline_vector_and_controller_work'];nat=forecast['Nat_lookup_CPU_estimate'];fixed=forecast['fixed_import_CPU_estimate']
fullrank=[a for a in s['attempts']if a['module']=='F3Graph15552Row0FullrankCertificate'and a['PASS']][-1]
remaining_steps=forecast['remaining_work']['vector_route_steps']-172*16
remaining_lookups=forecast['remaining_work']['controller_lookups']-172*4
optimistic_unit=forecast['baseline_finite_vector_CPU_estimate']/initial['vector_route_steps']
new_unit=(fullrank['CPU_seconds']-fixed-172*4*nat)/(172*16)
optimistic=cost+remaining_steps*optimistic_unit+remaining_lookups*nat+4*fixed
updated=cost+remaining_steps*new_unit+remaining_lookups*nat+4*fixed
finalizer=time.process_time()-started;cost+=finalizer
status='PILOT_COMPLETE_REPRESENTATIVE_TRUE_WALKS_PASS_ROW0_INCOMPLETE_CONTROLLED_COST_STOP'
r=dict(status=status,CPU_seconds=cost,CPU_budget_seconds=180,
       preparation_receipts=preps,driver_CPU_seconds=s['driver_CPU_seconds'],finalizer_CPU_seconds=finalizer,
       completed_modules=s['completed'],completed_module_count=len(s['completed']),attempts=s['attempts'],
       failed_attempts=sum(not a['PASS']for a in s['attempts']),maximum_module_CPU_seconds=max(a['CPU_seconds']for a in s['attempts']),
       representative_results=[dict(theorem='DegreeDiameter.Portfolio.F3Graph15552.PilotLargestGroup.all_walk_bound',
          source_controller=0,target_controller=0,all81start_and81target_fibers=True,genuine_SimpleGraph_Walk_length_bound=4,user_certificate_premises=False),
          dict(theorem='DegreeDiameter.Portfolio.F3Graph15552.PilotFullrank.all_walk_bound',source_controller=0,
          target_controller=33,all81start_and81target_fibers=True,genuine_SimpleGraph_Walk_length_bound=4,user_certificate_premises=False)],
       actual_representative_Audit=audit['log'],axioms=sorted(standard),
       source_type='Fin15552, actual192xF3^4/fiveglobaltypes/960arcs',
       clone_type='Fin15552 + Fin837, explicitlabelFin16389',
       holding_steps_proved_as_nil_walks=True,symbolic_offset_coset_theorem_kernel_PASS=True,
       source_and_clone_FinalClaim_definitions_typed_only=True,
       row0_partial=dict(data_PASS=True,additional_fullrank_words_basis_and_controller_PASS=172,
         shared_fullrank_words_including_pilot=173,new_fullrank_basis_vector_checks=688,
         fullrank_source0_caller_theorem_compiled=False,remaining_source0_coset_groups=18,
         row0_full_Walk_bound_compiled=False,source0_row_Audit_compiled=False),
       stop_forecast=dict(remaining_vector_route_steps=remaining_steps,remaining_controller_lookups=remaining_lookups,
         optimistic_cumulative_CPU_estimate=optimistic,updated_cumulative_CPU_estimate=updated,
         excludes_extra1458_choice_group_index_cost=True,reason='Both actualcost-derived estimates exceed180; queue naturallydrained without starting remainingcoset/caller modules.'),
       next_shared_scope=dict(root_data='../../SYMMETRY_REDUCED_KERNEL_SCOPE.json',representatives=[0,1,2,3,9,10,16,35],
         source_controller_pairs=1536,fullrank_pairs=1384,coset_pairs=152,
         required_distinct_fullrank_words=173,already_kernel_passed_fullrank_words=173,new_fullrank_basis_checks=0,
         remaining_coset_groups=90,remaining_group_column_vector_identities=2160,remaining_group_cover_vector_identities=7290,
         proposed_generators=2,commutation_cases=1920,start_controller_bindings=192,
         symmetry_kernel_status='NOT_STARTED_ROOT_MATH_DATA_ONLY',
         recommended_future_cumulative_CPU_ceiling_including_this_pilot=1200,
         estimated_total_cumulative_CPU_range=[750,1000],estimate_not_actual_receipt=True,
         fullqueue_authorized_or_started=False),
       external_binding='EXTERNAL_BINDING_PREPARATION_RESULT.json',
       source_full_D4_finalclaim_kernel_complete=False,clone16389_finalclaim_kernel_complete=False,
       source_reproduction_count_increment=0,concrete_Lean_increment=0,
       old_PASSED_modules_modified_or_recompiled=False,old_field_rank_BFS_solver_paidreview_runs=0,
       new_axioms_sorry_native_decide=False,root_Wiki_expert_frozen_source17_files_modified=False,
       running=False,active_modules=[])
save('FINAL.json',r);save('RESULT.json',r)
s.update(status=status,CPU_seconds=cost,running=False,active_modules=[],finalizer_CPU_seconds=finalizer)
save('CHECKPOINT.json',s)
save('TERMINAL.json',dict(status=status,CPU_seconds=cost,CPU_budget_seconds=180,running=False,active_modules=[],
     representative_walks_and_Audit_PASS=True,row0_complete=False,source_finalclaim_complete=False,clone_finalclaim_complete=False))
save('DRIVER_HANDLE.json',dict(status=status,CPU_seconds=cost,CPU_budget_seconds=180,running=False,active_modules=[],
     all_previous_compile_sessions_terminal=True))
(D/'STAGE_STATE').write_text('PILOT_TERMINAL_REPRESENTATIVE_WALKS_PASS_ROW0_INCOMPLETE_CONTROLLED_COST_STOP\n')
print(json.dumps({k:r[k]for k in ['status','CPU_seconds','CPU_budget_seconds','completed_module_count','failed_attempts']}))
