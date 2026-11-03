import json,re
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;F=R/'formal';prefix='GQ77Cubic22Clone65'
mods=[prefix+'Definitions']+[prefix+f'InputChunk{i:02d}' for i in range(20)]+[prefix+'Inputs',prefix+'Exact',prefix+'Audit']
rs=[json.loads((D/(m+'_RESULT.json')).read_text()) for m in mods]
assert len(rs)==24 and all(x['exit_code']==0 for x in rs)
history=[json.loads(p.read_text()) for p in sorted((D/'build_history').glob('*_RESULT.json'))]
lean_cpu=sum(r['CPU_seconds'] for r in rs+history)
binding=json.loads((D/'INPUT_BINDING_CHECK.json').read_text());prep=json.loads((D/'PREPARATION_RESULT.json').read_text())
assert binding['literal_edges_equal_fixed_source_clone_formula'] and binding['literal_edges_compared_one_by_one']==5192000
audit=(D/(prefix+'Audit.log')).read_text();exact=(D/(prefix+'Exact.log')).read_text()
assert 'SimpleGraph.Walk' in audit or 'graph.Walk' in audit or 'G.Walk' in audit
plain=re.sub(r'\s+',' ',audit).replace(prefix+'.','')
assert 'Fintype.card Vertex = 161150' in plain and 'graph.degree v ≤ 65' in plain
assert 'DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2' in plain
assert 'propext' in audit and 'Classical.choice' in audit and 'Quot.sound' in audit
for text in [audit,exact]+[(p.read_text()) for p in (F/'DegreeDiameter/Portfolio').glob(prefix+'*.lean')]+[(F/(prefix+'Audit.lean')).read_text()]:
 assert not re.search(r'\b(sorry|sorryAx|native_decide|axiom)\b',text)
 for xs in re.findall(r'depends on axioms:\s*\[([^\]]*)\]',text):assert set(re.split(r',\s*',xs.strip()))<={'propext','Classical.choice','Quot.sound'}
assert lean_cpu+binding['CPU_seconds']+prep['CPU_seconds']<600
source=F/'DegreeDiameter/Portfolio'/f'{prefix}Exact.lean'
decl_line=next(i for i,s in enumerate(source.read_text().splitlines(),1) if s.startswith('theorem concrete_order_degree_and_exact_D3'))
out=dict(status='KERNEL_COMPLETE_UNCONDITIONAL_161150_WITH_SEPARATE_IMPORT_TYPE_BODY_AXIOM_AUDIT',
 final_module=str(source.relative_to(R)),declaration_line=decl_line,audit_module=f'formal/{prefix}Audit.lean',
 theorem=f'DegreeDiameter.Portfolio.{prefix}.concrete_order_degree_and_exact_D3',
 type='Fintype.card Vertex = 161150 ∧ (∀ v, graph.degree v ≤ 65) ∧ DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2',
 carrier='(Fin160000⊕Fin50)⊕Fin1100',clone_index_equivalence='clonePair : Fin1100 ≃ Fin22×Fin50; k=50*i+j',
 total_equivalence='label : Vertex ≃ Fin161150',source_label_preserved=True,new_label='160050+k',certificate_premises=[],
 axioms=['propext','Classical.choice','Quot.sound'],module_count=24,measured_Lean_child_CPU_all_attempts=lean_cpu,
 measured_external_binding_CPU=binding['CPU_seconds'],last_generation_measured_CPU=prep['CPU_seconds'],
 measured_accounted_CPU_including_binding=lean_cpu+binding['CPU_seconds']+prep['CPU_seconds'],CPU_budget=600,per_module_CPU_limit=45,workers_max=2,
 initial_preparation_aborted_attempts=sum(r['exit_code']!=0 for r in history),initial_wide_import_successes=sum(r['exit_code']==0 and r['module']==prefix+'Definitions' for r in history),
 audit_print_visibility_refinement_passes=sum(r['exit_code']==0 and r['module']==prefix+'Audit' for r in history),
 old_sources_changed=False,old_oleans_recompiled=False,generic_sources_changed=False,actual_ovoid_owner_checks=22,actual_line_position_checks=3200,
 actual_spread_uniqueness='reused completed source theorem',center_independence_assumed=False,center_injectivity_assumed=False,
 source_no_isolates='derived from actual source true bounded WalkD3 and explicit distinct old0/old1',
 lower_bound='old bounded-Walk iff via collapseHom inherits source nonD2',input_binding='INPUT_BINDING_CHECK.json',
 ordered_centers_bound=1100,ordered_original_source_pins_bound=70400,source_pins_immutable=True,current_center_neighborhoods_used=False,
 source_edges_retained=5121600,new_edges_bound=70400,literal_edges_equal_fixed_source_clone_formula=5192000,new_new_edges=0,
 ASCII_parser_formalized=False,BFS_runs_in_formalization=0,solver_calls=0,native_computation_oracle=False,new_unproved_axioms=False,
 independent_numerical_acceptance='ROOT_COORDINATED_SEPARATE_1100_NEW_ROOTS; no additional BFS here',
 external_review=dict(A='ROOT_COORDINATED_SCOPE_A229',B='ROOT_COORDINATED_ACTUAL_BRIDGE',C='FRESH_FINAL_SCOPE_PENDING'),
 public_comparison='root best located160750;161150+400;global/priority UNCONFIRMED',
 receipts=[dict(module=r['module'],exit_code=r['exit_code'],CPU_seconds=r['CPU_seconds'],log=r['log']) for r in rs],
 retained_build_history=history)
(D/'FINAL_COMPILE_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','module_count','measured_Lean_child_CPU_all_attempts','measured_accounted_CPU_including_binding','declaration_line']}))
