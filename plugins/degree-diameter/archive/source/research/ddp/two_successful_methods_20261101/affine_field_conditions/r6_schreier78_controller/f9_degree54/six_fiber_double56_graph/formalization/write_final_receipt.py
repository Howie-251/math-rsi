import json,re
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;F=R/'formal';N='F9SixFiberDouble56'
mods=[N+s for s in ['Definitions','Inputs','Exact','Audit']]
rs=[json.loads((D/(m+'_RESULT.json')).read_text()) for m in mods];assert all(r['exit_code']==0 for r in rs)
hist=[json.loads(p.read_text()) for p in (D/'build_history').glob('*_RESULT.json')]
cpu=sum(r['CPU_seconds'] for r in rs+hist);binding=json.loads((D/'INPUT_BINDING_CHECK.json').read_text())
assert binding['clone_center_labels_bound']==972 and binding['independent_all972_immutable_N54_exact'] and binding['independent_literal_edges_bound']==1587762
audit=(D/(N+'Audit.log')).read_text();plain=re.sub(r'\s+',' ',audit).replace(N+'.','')
assert '@SimpleGraph.Walk.length' in audit and 'Fintype.card Vertex = 57834' in plain and 'graph.degree v ≤ 56' in plain
assert 'DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2' in plain
for text in [audit]+[p.read_text() for p in (F/'DegreeDiameter/Portfolio').glob(N+'*.lean')]+[(F/(N+'Audit.lean')).read_text()]:
 assert not re.search(r'\b(sorry|sorryAx|native_decide|axiom)\b',text)
 for xs in re.findall(r'depends on axioms:\s*\[([^\]]*)\]',text):assert set(re.split(r',\s*',xs.strip()))<={'propext','Classical.choice','Quot.sound'}
assert cpu+binding['CPU_seconds']<300
source=F/'DegreeDiameter/Portfolio'/f'{N}Exact.lean';line=next(i for i,s in enumerate(source.read_text().splitlines(),1) if s.startswith('theorem concrete_order_degree_and_exact_D3'))
out=dict(status='KERNEL_COMPLETE_UNCONDITIONAL_U6_57834_DEGREE56_TRUE_WALK_D3_NON_D2_SEPARATE_AUDIT_PASS',
 theorem=f'DegreeDiameter.Portfolio.{N}.concrete_order_degree_and_exact_D3',final_module=str(source.relative_to(R)),declaration_line=line,
 audit_module=f'formal/{N}Audit.lean',type='card(Vertex)=57834 ∧ (∀v,graph.degree v≤56) ∧ DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2',
 carrier='Fin56862⊕Fin972',label_equivalence='label : Vertex ≃ Fin57834',source='F9Graph56862.graph, original56862 source',source_is_new55_graph=False,
 selected_controllers=[0,1,2,3,9,15],plane='F9PlaneClone55.plane: (a,b,4*a)',base_center_count=486,copies=2,new_vertices=972,
 base_index_equivalence='Fin486 ≃ Fin6×Fin81',clone_index_equivalence='Fin972 ≃ Fin2×Fin486',
 clone_index='486*copy+81*uIndex+9*a+b',new_label='56862+cloneIndex',old_source_labels_preserved=True,
 certificate_premises=[],axioms=['propext','Classical.choice','Quot.sound'],base_load_bound=1,clone_load_bound=2,
 reusable_owner_helper=f'{N}.common_plane_pin_index_unique',reusable_helper_scope='Any actual controller fibers with injective(fiberIndex,port)target map; no equal-chart condition.',
 reusable_local_map_helper=f'{N}.sourcePlaneMap_injective',reused55_pinMap_injective=True,new_field_inverse_basis_checks=0,
 actual_target_double_index_checks=36,actual_same_zero_chart_checks=36,source_vertex_clone_pair_enumerations=0,
 center_independence_assumed=False,current_center_neighborhood_used=False,old_walk_collapse_lower_bound=True,
 module_count=4,all_current_modules_exit0=True,measured_Lean_child_CPU_all_attempts=cpu,measured_recipe_binding_CPU=binding['CPU_seconds'],
 measured_Lean_plus_recipe_binding_CPU=cpu+binding['CPU_seconds'],source_preparation='Manual source edits; no separate preparation executable or expensive computation.',
 total_CPU_budget=300,workers_max=1,per_module_hard_limit=60,failed_Lean_attempts=sum(r['exit_code']!=0 for r in hist),
 old54_or55_sources_changed=False,old54_or55_oleans_recompiled=False,old_generic_sources_changed=False,
 input_binding='INPUT_BINDING_CHECK.json',typed_ordered_recipe='FORMAL_ORDERED_CLONE_RECIPE.csv',producer_and_independent_rows_bound_by_j=972,
 independent_physical_row_order_assumed=False,independent_summary='../independent_acceptance/SUMMARY.json',
 independent_actual_status=binding['independent_status'],independent_literal_edges_bound=1587762,independent_original_edges_retained=1535274,
 independent_new_old_edges=52488,independent_new_new_edges=0,independent_new_root_BFS_runs=972,independent_old_R3_BFS_runs=0,
 large_edgefiles_read_here=0,BFS_runs_here=0,old_field_checks_repeated=False,ASCII_parser_formalized=False,
 public_source_guarantee=57568,bounded_gain=266,global_record_or_priority_certified=False,
 U7_generated=False,U6_instance_preserved=True,accepted_counts_changed_by_this_task=False,
 external_review='Root coordinated A/B/freshC after actual final packet',all_local_tasks_terminal=True,receipts=rs,retained_attempt_history=hist)
(D/'FINAL_COMPILE_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','module_count','measured_Lean_child_CPU_all_attempts','measured_Lean_plus_recipe_binding_CPU','failed_Lean_attempts','declaration_line']}))
