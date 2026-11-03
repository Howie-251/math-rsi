import json,re
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;F=R/'formal';N='F9U10PlaneCloneFamily'
mods=[N+s for s in ['Definitions','Inputs','Exact','Audit']]
rs=[json.loads((D/(m+'_RESULT.json')).read_text()) for m in mods];assert all(r['exit_code']==0 for r in rs)
hist=[json.loads(p.read_text()) for p in (D/'build_history').glob('*_RESULT.json')]
cpu=sum(r['CPU_seconds'] for r in rs+hist);prep=json.loads((D/'PREPARATION_RESULT.json').read_text())['CPU_seconds'];binding=json.loads((D/'INPUT_BINDING_CHECK.json').read_text())
assert binding['case_count']==5 and binding['total_endpoint_recipe_rows_bound']==12150 and not binding['k6_original_target_or_file']
audit=(D/(N+'Audit.log')).read_text();plain=re.sub(r'\s+',' ',audit).replace(N+'.','');assert '@SimpleGraph.Walk.length' in audit
cases=[];source=F/'DegreeDiameter/Portfolio'/(N+'Exact.lean');lines=source.read_text().splitlines()
for k in range(1,6):
 degree=54+k;n=56862+810*k;m=1535274+43740*k;name=f'concrete_{degree}_{n}'
 assert f'Fintype.card (Vertex {k}) = {n}' in plain and f'(graph {k}).degree v ≤ {degree}' in plain
 assert f'DiameterAtMost (graph {k}) 3 ∧ ¬DiameterAtMost (graph {k}) 2' in plain and name in audit and f'final_claim{degree}' in audit
 b=next(c for c in binding['cases'] if c['k']==k);assert b['ordered_rows_bound']==810*k and b['m']==m and b['n']==n
 line=next(i for i,s in enumerate(lines,1) if s.startswith('theorem '+name))
 cases.append(dict(k=k,degree_cap=degree,n=n,m=m,theorem=f'DegreeDiameter.Portfolio.{N}.{name}',final_claim=f'DegreeDiameter.Portfolio.{N}.final_claim{degree}',
  final_module=str(source.relative_to(R)),declaration_line=line,carrier=f'Fin56862⊕(Fin{k}×Fin810)',label_equivalence=f'Fin{n}',
  type=f'card(Vertex{k})={n} ∧ (∀v,(graph{k}).degree v≤{degree}) ∧ trueWalkD3 ∧ nonD2',certificate_premises=[],
  axioms=['propext','Classical.choice','Quot.sound'],independent_summary=b['independent_summary'],literal_graph=b['literal_graph'],
  ordered_literal_N54_rows_bound=810*k,literal_old_edges_retained=1535274,literal_new_old_edges=43740*k,new_new_edges=0,
  degree_histogram=b['degree_histogram'],source_load_histogram=b['old_load_histogram'],independent_new_root_BFS_runs=810*k,
  public_source_guarantee=[56540,57568,58596,59624,60652][k-1],bounded_gain=[1132,914,696,478,260][k-1]))
for text in [audit]+[p.read_text() for p in (F/'DegreeDiameter/Portfolio').glob(N+'*.lean')]+[(F/(N+'Audit.lean')).read_text()]:
 assert not re.search(r'\b(sorry|sorryAx|native_decide|axiom)\b',text)
 for xs in re.findall(r'depends on axioms:\s*\[([^\]]*)\]',text):assert set(re.split(r',\s*',xs.strip()))<={'propext','Classical.choice','Quot.sound'}
assert cpu+prep+binding['CPU_seconds']<600
out=dict(status='KERNEL_COMPLETE_FIVE_EXPLICIT_U10_ORIGINAL_TARGETS_AND_JOINT_SEPARATE_AUDIT_PASS',concrete_original_target_count=5,cases=cases,
 shared_namespace=f'DegreeDiameter.Portfolio.{N}',module_count=4,all_current_modules_exit0=True,all_modules_first_attempt_PASS=not hist,
 generic_family_is_unconditional=True,generic_family_alone_counted_as_five=False,explicit_actual_cases=[1,2,3,4,5],k6_endpoint_instantiated_or_audited=False,
 selected_controllers=[31,32,44,45,59,60,61,72,73,74],fixed_original_source='F9Graph56862.graph on56862vertices',source_is_new55_or_U6_graph=False,
 source_old_edges=1535274,base_centers=810,base_pin_union=43740,target_owner_kernel_checks=60,base_load_bound=1,copy_load_bound='≤k',
 owner_helper_reused='F9SixFiberDouble56.common_plane_pin_index_unique',new_field_inverse_basis_checks=0,source_vertex_clone_pair_enumerations=0,
 center_independence_assumed=False,old_source_labels_preserved=True,clone_index='810*copy+81*uIndex+9*a+b',newlabel='56862+cloneIndex',
 axioms=['propext','Classical.choice','Quot.sound'],certificate_premises=[],
 measured_Lean_child_CPU_all_attempts=cpu,measured_preparation_CPU=prep,measured_recipe_binding_CPU=binding['CPU_seconds'],measured_accounted_CPU=cpu+prep+binding['CPU_seconds'],
 total_CPU_budget=600,workers_max=1,per_module_hard_limit=60,failed_Lean_attempts=sum(r['exit_code']!=0 for r in hist),
 old54_55_U6_generic_sources_or_oleans_changed=False,old_modules_recompiled=False,large_edgefiles_read_here=0,BFS_runs_here=0,ASCII_parser_formalized=False,
 input_binding='INPUT_BINDING_CHECK.json',typed_ordered_recipe='FORMAL_ORDERED_CASE_RECIPE.csv',total_endpoint_recipe_rows_bound=12150,
 independent_summary='../independent_acceptance/SUMMARY.json',independent_actual_status='PASS_ALL_FIVE_COMPLETE_U10_ENDPOINT_GRAPHS',
 independent_new_root_BFS_runs=12150,independent_old_R3_BFS_runs=0,independent_source_R2_only_centers_once=810,
 independent_source_field_controller_finite_checks_repeated=False,global_record_or_priority_certified=False,
 optimality_scope='Root accepted optimum10only for fixedcontroller whole-layer plane model; no point-level/nonrectangular exclusion claimed by these Lean targets.',
 U6_instance_preserved=True,accepted_or_concrete_counts_changed_by_this_task=False,external_review='Root coordinated joint six-target(U6plusfive)A/B/freshC; no review launched here',
 all_local_tasks_terminal=True,receipts=rs,retained_attempt_history=hist)
(D/'FINAL_COMPILE_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','concrete_original_target_count','module_count','measured_Lean_child_CPU_all_attempts','measured_accounted_CPU','failed_Lean_attempts']}))
