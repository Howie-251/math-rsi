import json,re
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;F=R/'formal';N='F9Graph56862'
mods=[N+s for s in ['Field','','MatrixCertificate','Routes','Linear','RouteData','Models','DecoderInterface','ModelBridge']]
mods += [N+f'ModelChunk{i:02d}' for i in range(13)]+[N+f'PairChunk{i}' for i in range(6)]
mods += [N+f'AdjacentChart{c}Block{b}' for c in range(8) for b in range(3)]
mods += [N+f'AdjacentChart{c}' for c in range(8)]
mods += [N+s for s in ['Certificates','Adjacent','DiameterInterface','Diameter','Lower','Degree','Exact','Audit']]
rs=[json.loads((D/(m+'_RESULT.json')).read_text()) for m in mods]
assert len(mods)==len(set(mods))==68 and all(r['exit_code']==0 for r in rs)
current=[json.loads(p.read_text()) for p in D.glob(N+'*_RESULT.json')]
history=[json.loads(p.read_text()) for p in (D/'build_history').glob('*_RESULT.json')]
lean_cpu=sum(r['CPU_seconds'] for r in current+history)
prep_cpu=sum(json.loads(p.read_text())['CPU_seconds'] for p in D.glob('*PREPARATION_RESULT.json'))
binding=json.loads((D/'INPUT_BINDING_CHECK.json').read_text());assert binding['literal_edges_bound_by_fresh_checker']==1535274
assert binding['independent_literal_inputs_match_typed_controller_matrices_directions']
audit=(D/(N+'Audit.log')).read_text();plain=re.sub(r'\s+',' ',audit).replace(N+'.','')
assert '@SimpleGraph.Walk.length' in audit and 'Fintype.card (Fin 56862) = 56862' in plain
assert 'graph.degree' in plain and '≤ 54' in plain and '= 54' in plain
assert 'DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2' in plain
for text in [audit]+[p.read_text() for p in (F/'DegreeDiameter/Portfolio').glob(N+'*.lean')]+[(F/(N+'Audit.lean')).read_text()]:
 assert not re.search(r'\b(sorry|sorryAx|native_decide|axiom)\b',text)
 for xs in re.findall(r'depends on axioms:\s*\[([^\]]*)\]',text):
  assert set(re.split(r',\s*',xs.strip()))<={'propext','Classical.choice','Quot.sound'}
assert lean_cpu+prep_cpu+binding['CPU_seconds']<1500
source=F/'DegreeDiameter/Portfolio'/f'{N}Exact.lean'
line=next(i for i,s in enumerate(source.read_text().splitlines(),1) if s.startswith('theorem concrete_order_degree_and_exact_D3'))
out=dict(status='KERNEL_COMPLETE_UNCONDITIONAL_56862_REGULAR54_ACTUAL_WALK_D3_NON_D2_SEPARATE_AUDIT_PASS',
 theorem=f'DegreeDiameter.Portfolio.{N}.concrete_order_degree_and_exact_D3',final_module=str(source.relative_to(R)),declaration_line=line,
 regular_theorem=f'DegreeDiameter.Portfolio.{N}.concrete_regular_and_exact_D3',audit_module=f'formal/{N}Audit.lean',
 type='Fintype.card (Fin56862)=56862 ∧ (∀v,graph.degree v≤54) ∧ DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2',
 regular_type='card56862 ∧ (∀v,graph.degree v=54) ∧ trueWalkD3 ∧ nonD2',certificate_premises=[],
 axioms=['propext','Classical.choice','Quot.sound'],carrier='Fin56862',label='729*u+x0+9*x1+81*x2',
 field='GF3[w]/(w²+1),codea+3b; literal9elementCommRing',controller='fixed6regular78, (2,6,17,5,10)',
 graph_formula='y=T_dart*x+t*ell_reversePort; original fixed8chart matrices',reverse_noise='-t',
 same_nonadjacent_route_pairs=5616,actual_nondefault_noise_types=169,local_model_basis_checks=507,
 pair_chunks=6,model_chunks=13,adjacent_charts=8,adjacent_chart_blocks=24,adjacent_offset_checks=5832,
 all_pairs_D3='actual affine route decoders and genuine3edge SimpleGraph.Walk for arbitrary vertices',
 no_fiber_translation_automorphism_assumed=True,nonD2_witness=[0,729],nonD2_finite_controller_checks=42,
 final_closure_new_module_count=68,successful_new_modules_including_unused_pilot=sum(r['exit_code']==0 for r in current),
 all_current_closure_modules_exit0=True,measured_Lean_child_CPU_all_attempts=lean_cpu,measured_preparation_CPU=prep_cpu,
 measured_input_binding_CPU=binding['CPU_seconds'],measured_accounted_CPU=lean_cpu+prep_cpu+binding['CPU_seconds'],
 total_CPU_budget=1500,pilot_result='PILOT_RESULT.json',per_module_limit_max=60,workers_max=1,
 failed_Lean_attempts=sum(r['exit_code']!=0 for r in current+history),old_sources_changed=False,old_concrete_or_generic_oleans_recompiled=False,
 input_binding='INPUT_BINDING_CHECK.json',literal_edges_bound_by_fresh_checker=1535274,
 independent_summary='../independent_acceptance/SUMMARY.json',independent_literal_roots=806,independent_all_graph_roots_BFS=False,
 large_edgefiles_read_by_formalization=0,BFS_runs_by_formalization=0,ASCII_parser_formalized=False,
 public_comparison='root bestlocated55350;56862+1512 within boundedcompare;globalrecord/priority pending',
 accepted_counts_changed_by_this_task=False,external_review='Root coordinated distinct A/B/freshC scopes',all_local_tasks_terminal=True,
 receipts=[dict(module=r['module'],exit_code=r['exit_code'],CPU_seconds=r['CPU_seconds'],log=r['log']) for r in rs],
 retained_attempt_history=history)
(D/'FINAL_COMPILE_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['status','final_closure_new_module_count','measured_Lean_child_CPU_all_attempts','measured_accounted_CPU','failed_Lean_attempts','declaration_line']}))
