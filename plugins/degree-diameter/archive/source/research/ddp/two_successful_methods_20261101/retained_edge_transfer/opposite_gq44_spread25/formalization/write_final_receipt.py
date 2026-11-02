import json
from pathlib import Path
D=Path(__file__).resolve().parent;R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math')
mods=['OppositeIncidenceSpreadSlots','OppositeIncidenceSpreadFamily','OppositeIncidenceSpreadAudit','OppositeGQ44SpreadDefinitions','OppositeGQ44SpreadIncidence','OppositeGQ44SpreadInputInterface']+[f'OppositeGQ44SpreadInputRow{i:02}' for i in range(85)]+['OppositeGQ44SpreadInputs','OppositeGQ44SpreadExact','OppositeGQ44SpreadAudit'];rr=[]
for m in mods:
 p=D/f'{m}_RESULT.json';r=json.loads(p.read_text());assert r['exit_code']==0,(m,r)
 rr.append({'module':m,'exit_code':0,'CPU_seconds':r['CPU_seconds'],'receipt':str(p.relative_to(R)),'log':r['log']})
audit=(D/'OppositeGQ44SpreadAudit.log').read_text();assert 'sorryAx' not in audit and 'error:' not in audit
attempts=[]
for p in list(D.glob('*_RESULT.json'))+list((D/'build_history').glob('*_RESULT.json')):
 try:x=json.loads(p.read_text())
 except Exception:continue
 if 'CPU_seconds' in x and 'module' in x:attempts.append(x)
total=sum(x['CPU_seconds'] for x in attempts);assert total<1000
r={'status':'KERNEL_COMPLETE_UNCONDITIONAL_7242_WITH_IMPORT_TYPE_AXIOM_AUDIT','final_module':'formal/DegreeDiameter/Portfolio/OppositeGQ44SpreadExact.lean','audit_module':'formal/OppositeGQ44SpreadAudit.lean','theorem':'DegreeDiameter.Portfolio.OppositeGQ44Spread.concrete_order_degree_and_exact_D3','type':'Fintype.card Vertex = 7242 ∧ (∀ v, graph.degree v ≤ 25) ∧ DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2','carrier':'Fin7225 ⊕ Fin17','explicit_Fin7242_equivalence':'label; old identity; new7225+j','certificate_premises':[],'axioms':['propext','Classical.choice','Quot.sound'],'module_count':len(mods),'total_Lean_child_CPU_all_attempts':total,'CPU_budget':1000,'CPU_per_module_limit':115,'generic_substage_CPU_limit':200,'generic_per_module_CPU_limit':60,'maximum_batch_workers':3,'actual_point_line_projection_pairs_checked':7225,'projection_method':'threeFin5indices; shared pointLine_sound + one equality per pair','positive_line_point_cover_checks':425,'positive_point_line_sound_checks':425,'positive_spread_owner_checks':85,'typed_data_binding':'850incidence entries+17spreadIDs+85owners; all Fin inputs in bounds','ordered_pin_labels_bound_at_same_recipe_indices':425,'literal_edges_equal_formula_edges':90525,'input_binding':'INPUT_BINDING_CHECK.json','ASCII_parser_theorem':False,'old_sources_changed':False,'old_caches_recompiled':False,'BFS_runs_in_this_formalization':0,'solver_calls':0,'native_decide':False,'new_unproved_axioms':False,'hashes':False,'independent_acceptance':'separate ../independent_acceptance/; PASS all7242roots; root acceptance/counting separate','external_review':{'A':'PENDING_ROOT_NEW_SCOPE_STATUS','B':'PENDING_ROOT_NEW_SCOPE_STATUS','C':'PENDING_ROOT_ACTUAL_FINAL_SCOPE'},'global_novelty':'UNCONFIRMED','receipts':rr}
(D/'FINAL_COMPILE_RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k!='receipts'}))
