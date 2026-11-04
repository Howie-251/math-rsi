import pathlib,json,hashlib,datetime
R=pathlib.Path(__file__).resolve().parent
def load(p):return json.loads((R/p).read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256((R/p).read_bytes()).hexdigest()
m=load('HIGHER_Q5_FULL_REUSE_MANIFEST.json');p=load('HIGHER_Q5_FULL_REUSE_REVIEW_prepare.json');c=load('HIGHER_Q5_FULL_REUSE_REVIEW_census.json');f=load('HIGHER_Q5_FULL_REUSE_REVIEW_check.json')
assert p['status']==c['status']==f['status']=='PASS'
arts=['HIGHER_Q5_FULL_REUSE_REVIEW_prepare.py','HIGHER_Q5_FULL_REUSE_REVIEW_prepare.json','HIGHER_Q5_FULL_REUSE_REVIEW_check.cpp','HIGHER_Q5_FULL_REUSE_REVIEW_census.json','HIGHER_Q5_FULL_REUSE_REVIEW_finish.py','HIGHER_Q5_FULL_REUSE_REVIEW_check.json']+[f'HIGHER_Q5_FULL_REUSE_REVIEW_{n}.txt' for n in ['T26','T15','T17','T63']]
d={
 'audit_skill':'proof-checker','verdict':'PASS',
 'reason_code':'general_multisource_transfer_exact_accepted_marked_registries_all_positive_witnesses_and_complete_remaining_domain_verified',
 'summary':'Accepted registry reuse proves7660439 sufficient geometries from the prior accepted8008722 twelve-hole residual, leaving exactly348283 (covered348236/free47). Every positive witness replayed and every remaining cut/source exhaustively checked. Full12/higher/P6 remain OPEN.',
 'reviewer_agent_id':'/root/higher_q5_nearbalanced_review','reviewer_model':'gpt-6.1-sol','reviewer_reasoning':'high',
 'model_override_source':'Explicit user-selected model/effort route relayed by parent overrides ARIS defaults',
 'reviewer_family':'openai','executor_family':'openai','review_independence':'same-family','acceptance_status':'provisional',
 'generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'trace_path':'HIGHER_Q5_FULL_REUSE_REVIEW.md',
 'audited_input_hashes':{'HIGHER_Q5_FULL_REUSE_MANIFEST.json':sha('HIGHER_Q5_FULL_REUSE_MANIFEST.json'),**m['hashes']},
 'imported_dependency_hashes':{**p['bound_imports'],'HIGHER_Q5_FULL_REVIEW.json':sha('HIGHER_Q5_FULL_REVIEW.json')},
 'checker_artifact_hashes':{n:sha(n) for n in arts},'report_hash':sha('HIGHER_Q5_FULL_REUSE_REVIEW.md'),
 'details':{
  'issues':[],'mathematical_obligations_closed':14,'port_population_checks':f['port_population_checks'],
  'general_source_transfer_proved_modulo_explicit_imports':True,
  'original_matching_quantifier':'Every realizing original short Q6 matching, free root and opposite-parity free/covered target; arbitrary complete-graph auxiliary matchings.',
  'full_balanced_Q5_A_input_hypotheses_checked':True,'source_excludes_free_target_and_root_mirror':True,
  'actual_B_holes_and_marked_omissions_checked':True,'multimirror_conflict_paths_including_Y_Y_checked':True,
  'five_direction_zero_crossing_import_explicit':True,'forced_T17_used':False,
  'accepted_registry_statement_rows':p['statement_rows'],'old_T15_core_images':p['old_core_images'],'old_T15_split_images':p['old_split_images'],'old_T15_union':p['old_union'],
  'independent_lookup_exact_set_counts':p['lookup_exact_sets'],'lookup_rebuilt_from_hash_bound_theorem_tables':True,
  'all_producer_lookup_sets_equal_independent':True,'frozen_hashes_and_sizes_checked':44,
  'accepted_input':8008722,'covered_by_validated_witnesses':7660439,'remaining':348283,'remaining_covered_target':348236,'remaining_free_target':47,
  'all_positive_witnesses_replayed':True,'positive_witness_record_bytes':26,'positive_witness_actual_masks_verified':True,
  'all_remaining_records_exhaustive_six_cuts_and_every_legal_source_subset':True,
  'exact_domain_partition_reason':'Each source index has a valid independently checked positive witness or an identical remaining record in source order; every remaining record has no accepted cut/source; no duplicate/out-of-range witness index or trailing/partial records.',
  'reports':c['reports'],'selected_witness_family_histogram':f['witness_family_histogram'],
  'producer_first_witness_tiebreaking_reproduced':False,'tiebreaking_not_needed_for_exact_predicate_union':True,
  'matching_realizability_filter_used':False,'producer_modules_or_executables_executed':False,
  'complete_twelve_hole_proved':False,'full_twelve_hole_proved':False,'full_higher_hole_layers_proved':False,'full_P6_proved':False,
  'upstream_large_certificates_rerun':False,'production_proof_lookup_census_raw_or_state_modified':False,
 },
 'scope':'Generalized full-balanced-A multisource transfer plus exact conservative accepted-registry reuse over the prior independently accepted twelve-hole residual. Does not close full12, higher complete layers or P6.'
}
(R/'HIGHER_Q5_FULL_REUSE_REVIEW.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps({'verdict':d['verdict'],'report_sha256':d['report_hash'],'review_sha256':sha('HIGHER_Q5_FULL_REUSE_REVIEW.json')},indent=2))
