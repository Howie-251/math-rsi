import json,re
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;F=R/'formal';prefix='GQ77Cubic22Clone70'
mods=[prefix+s for s in ['Definitions','Inputs','Exact','Audit']]
receipts=[json.loads((D/(m+'_RESULT.json')).read_text()) for m in mods]
assert all(r['exit_code']==0 for r in receipts)
history=[json.loads(p.read_text()) for p in (D/'build_history').glob('*_RESULT.json')] if (D/'build_history').exists() else []
lean_cpu=sum(r['CPU_seconds'] for r in receipts+history)
audit=(D/(prefix+'Audit.log')).read_text();plain=re.sub(r'\s+',' ',audit).replace(prefix+'.','')
assert '@SimpleGraph.Walk.length' in audit and 'Fintype.card Vertex = 166650' in plain
assert 'graph.degree v ≤ 70' in plain and 'DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2' in plain
texts=[audit]+[(p.read_text()) for p in (F/'DegreeDiameter/Portfolio').glob(prefix+'*.lean')]+[(F/(prefix+'Audit.lean')).read_text()]
for text in texts:
 assert not re.search(r'\b(sorry|sorryAx|native_decide|axiom)\b',text)
 for xs in re.findall(r'depends on axioms:\s*\[([^\]]*)\]',text):assert set(re.split(r',\s*',xs.strip()))<={'propext','Classical.choice','Quot.sound'}
binding=json.loads((D/'INPUT_BINDING_CHECK.json').read_text())
assert binding['ordered_clone_centers_and_labels_bound']==6600 and binding['independent_literal_status']=='PASS'
assert binding['independent_recipe_matches_typed_O22_spread_and_clone_order'] and binding['independent_all6600_source_full_neighborhoods_exact']
assert binding['independent_literal_edges_bound']==5544000 and binding['large_edgefiles_read_by_this_checker']==0
assert lean_cpu+binding['CPU_seconds']<300
source=F/'DegreeDiameter/Portfolio'/f'{prefix}Exact.lean'
line=next(i for i,s in enumerate(source.read_text().splitlines(),1) if s.startswith('theorem concrete_order_degree_and_exact_D3'))
out=dict(status='KERNEL_COMPLETE_UNCONDITIONAL_166650_WITH_SEPARATE_IMPORT_TYPE_BODY_AXIOM_AUDIT',
 theorem=f'DegreeDiameter.Portfolio.{prefix}.concrete_order_degree_and_exact_D3',final_module=str(source.relative_to(R)),declaration_line=line,
 audit_module=f'formal/{prefix}Audit.lean',type='Fintype.card Vertex = 166650 ∧ (∀ v, graph.degree v ≤ 70) ∧ DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2',
 carrier='(Fin160000⊕Fin50)⊕Fin6600',explicit_equivalence='label : Vertex ≃ Fin166650',clone_index_equivalence='clonePair : Fin6600 ≃ Fin6×Fin1100',
 original_source='OppositeGQ77Spread.graph, accepted original160050',source_is_current161150=False,
 center_formula='GQ77Cubic22Clone65.center (clonePair k).2',clone_index_formula='1100*copy+50*i+j',new_label_formula='160050+k',
 original_source_label_preserved=True,multiplicity=6,certificate_premises=[],axioms=['propext','Classical.choice','Quot.sound'],
 load_bound='load≤6 via injection of adjacentcloneindices into Fin6, using completedbase load≤1',
 center_independence_assumed=False,center_injectivity_assumed=False,source_clone_pair_enumerations=0,
 module_count=4,all_current_modules_exit0=True,measured_Lean_child_CPU_all_attempts=lean_cpu,
 measured_final_recipe_binding_CPU=binding['CPU_seconds'],prior_recipe_binding_attempt_CPU=0.054900339,
 measured_Lean_plus_both_recipe_binding_attempts_CPU=lean_cpu+binding['CPU_seconds']+0.054900339,
 total_CPU_budget=300,per_module_CPU_limit=60,workers_max=1,failed_Lean_attempts=sum(r['exit_code']!=0 for r in receipts+history),
 old_generic_sources_changed=False,old_graphs_changed=False,old_415_or_24_modules_recompiled=False,old_oleans_changed=False,
 binding='INPUT_BINDING_CHECK.json',ordered_typed_recipe='FORMAL_ORDERED_CLONE_RECIPE.csv',ordered_centers_and_labels_bound=6600,
 independent_literal_summary='../independent_acceptance/SUMMARY.json',independent_literal_summary_actual_status='PASS',
 independent_edges_bound=5544000,independent_immutable_source_neighborhoods_bound=6600,independent_new_edges_bound=422400,
 independent_source_old_edges_retained_exactly=5121600,independent_new_new_edges=0,
 large_edgefiles_read_by_formalization=0,BFS_runs_in_formalization=0,ASCII_parser_formalized=False,
 independent_new_root_BFS_runs=6600,independent_old_root_BFS_runs=0,
 external_review='Root coordinated newscope A/B/C; currentpacket CHECKPOINT_C.md',
 public_comparison='root boundedbestlocated164500;166650 is2150larger;globalrecord/priority pending',
 accepted_counts_changed_by_this_task=False,all_local_tasks_terminal=True,receipts=receipts,retained_build_history=history)
(D/'FINAL_COMPILE_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','module_count','measured_Lean_child_CPU_all_attempts','measured_Lean_plus_both_recipe_binding_attempts_CPU','declaration_line']}))
