import json,pathlib,hashlib,datetime
R=pathlib.Path(__file__).resolve().parent
def h(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
m=json.loads((R/'HIGHER_Q5_FULL_MANIFEST.json').read_text(encoding='utf-8-sig'))
c=json.loads((R/'HIGHER_Q5_FULL_REVIEW_check.json').read_text())
d={
 'audit_skill':'proof-checker','verdict':'PASS',
 'reason_code':'nearbalanced_transfer_predecessor_lemmas_and_four_exact_independent_census_raw_domains_complete_modulo_explicit_imports',
 'summary':'All three full-Q5 near-balanced row families, both predecessor reductions, and complete independent four-layer census/raw-set audits pass. Twelve-hole reduction uses final ten-hole PASS; higher predecessor reductions remain conditional. No complete12/14/16/18 layer or P6 closure.',
 'reviewer_agent_id':'/root/higher_q5_nearbalanced_review','reviewer_model':'gpt-6.1-sol','reviewer_reasoning':'high',
 'model_override_source':'Explicit user-selected model/effort route relayed by parent overrides ARIS defaults',
 'reviewer_family':'openai','executor_family':'openai','review_independence':'same-family','acceptance_status':'provisional',
 'generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'trace_path':'HIGHER_Q5_FULL_REVIEW.md',
 'audited_input_hashes':{'HIGHER_Q5_FULL_MANIFEST.json':h('HIGHER_Q5_FULL_MANIFEST.json'),**m['hashes']},
 'checker_artifact_hashes':{p:h(p) for p in ['HIGHER_Q5_FULL_REVIEW_check.cpp','HIGHER_Q5_FULL_REVIEW_check.py','HIGHER_Q5_FULL_REVIEW_check.json',*[f'HIGHER_Q5_FULL_REVIEW_k{k}.json' for k in range(6,10)]]},
 'report_hash':h('HIGHER_Q5_FULL_REVIEW.md'),
 'details':{
  'issues':[],'mathematical_micro_obligations_closed':18,
  'matching_quantifier':'Every short Q6 matching realizing the stated holes; every arbitrary K(Q5) auxiliary matching, no original-matching sample or realizability filter.',
  'cut_rows':[{'b_minus_a':0,'b_min':1},{'b_minus_a':1,'b_min':1},{'b_minus_a':2,'legal_odd_source_required':True}],
  'legal_source_free_target_exclusion_checked':True,'root_mirror_exclusion_checked':True,
  'five_direction_zero_crossing_import_explicit':True,'actual_new_holes_checked':True,'root_port_and_completion_parity_checked':True,
  'q5_balanced_endpoint_range':[1,16],'q5_balanced_cycle_range':[0,16],'q5_imbalance_two_parameter_range':[1,15],
  'predecessor_reduction_lemmas':'Free: any adjacent pair, including special uv closure/deletion. Covered: Z--W adjacent pair. Complete preceding layer required.',
  'twelve_hole_predecessor_final_PASS':True,'higher_hole_predecessor_reductions_conditional':[14,16,18],
  'independent_census_status':c['status'],'independent_enumeration':c['independent_enumeration'],
  'all_four_layers_actual_six_cut_tests':True,'old_k_ge_7_shortcut_used':False,
  'distinct_ZW_geometries':c['distinct_ZW_geometries_all_four_levels'],
  'eligible_target_marked_records':c['eligible_marked_records'],
  'raw_records_individually_checked':c['raw_records_individually_validated'],'raw_files_checked':24,
  'raw_exact_set_equality_proof':c['exact_raw_set_equality_reason'],
  'all_eligible_rootadj_cut_residual_counts_match':True,'frozen_hashes_and_sizes_checked':c['frozen_file_hashes_checked'],
  'frozen_bytes_checked':c['frozen_bytes_checked'],'port_population_checks':c['port_population_checks'],
  'residual_totals':{str(l['holes']):{s:sum(t['residual'] for t in l['targets'] if t['free_target']==f) for s,f in [('covered',False),('free',True)]} for l in c['levels']},
  'residual_counts_are_initial_nearbalanced_filter_only':True,
  'full_twelve_hole_proved':False,'full_fourteen_hole_proved':False,'full_sixteen_hole_proved':False,'full_eighteen_hole_proved':False,
  'full_higher_hole_layers_proved':False,'full_P6_proved':False,
  'production_proof_census_raw_or_state_modified':False,'upstream_large_certificates_rerun':False,
 },
 'scope':'Exact stated cut theorem, conditional predecessor lemmas, complete four-layer geometry census and exact24 raw-set audit. Does not close any complete12--18 layer or fullP6.'
}
(R/'HIGHER_Q5_FULL_REVIEW.json').write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'verdict':d['verdict'],'report_sha256':d['report_hash'],'review_sha256':h('HIGHER_Q5_FULL_REVIEW.json'),'residual_totals':d['details']['residual_totals']},indent=2))
