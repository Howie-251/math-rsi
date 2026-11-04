import pathlib,json,hashlib,datetime
R=pathlib.Path(__file__).resolve().parent
def load(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
c=load('TWELVE_NEW_FORCED_HALL_REVIEW_check.json');g=load('TWELVE_NEW_FORCED_HALL_REVIEW_gate.json');assert c['status']==g['status']=='PASS'
for n,h in c['audited_frozen_hashes'].items():assert sha(n)==h,n
for n,key in [('TWELVE_NEW_TYPES_APPLICATION_REVIEW.json','source_review_sha256'),('TWELVE_NEW_FORCED_REVIEW.json','local27_review_sha256'),('HIGHER_FORCED_CHERRY_REVIEW.json','generic_safe_transfer_review_sha256')]:
 assert load(n)['verdict']=='PASS' and sha(n)==g[key]
manifests=['TWELVE_NEW_FORCED_APPLICATION_MANIFEST.json','TWELVE_HALL_MANIFEST.json','TWELVE_NEW_FORCED_HALL_UNION_MANIFEST.json']
deps=['TWELVE_NEW_TYPES_APPLICATION_REVIEW.json','TWELVE_NEW_TYPES_APPLICATION.md','TWELVE_NEW_FORCED_REVIEW.json','HIGHER_FORCED_CHERRY_REVIEW.json','HIGHER_FORCED_CHERRY_TRANSFER.md']
arts=['TWELVE_NEW_FORCED_HALL_REVIEW_check.py','TWELVE_NEW_FORCED_HALL_REVIEW_check.json','TWELVE_NEW_FORCED_HALL_REVIEW_gate.py','TWELVE_NEW_FORCED_HALL_REVIEW_gate.json','TWELVE_NEW_FORCED_HALL_REVIEW_emit.py']
d={'audit_skill':'proof-checker','verdict':'PASS','reason_code':'actual_safe_forced_subset_explicit_Hall_deficiency_exclusions_and_exact_common_domain_union_complete_modulo_final_accepted_source_and_local_imports',
 'summary':'Final accepted37405 covered-target domain partitions into552 safe forced successes,7483 explicitly impossible marked geometries and29370 remaining records. Exact subsets are disjoint and all9 remaining byte streams match. Remaining realizability unverified; full12/P6 OPEN.',
 'reviewer_agent_id':'/root/higher_q5_nearbalanced_review','reviewer_model':'gpt-6.1-sol','reviewer_reasoning':'high','model_override_source':'Explicit user-selected model/effort route relayed by parent overrides ARIS defaults',
 'reviewer_family':'openai','executor_family':'openai','review_independence':'same-family','acceptance_status':'provisional','generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'trace_path':'TWELVE_NEW_FORCED_HALL_REVIEW.md','audited_input_hashes':{**c['audited_frozen_hashes'],**{n:sha(n) for n in manifests}},'imported_dependency_hashes':{n:sha(n) for n in deps},'checker_artifact_hashes':{n:sha(n) for n in arts},'report_hash':sha('TWELVE_NEW_FORCED_HALL_REVIEW.md'),
 'details':{'issues':[],'mathematical_obligations_closed':12,'source_application_final_PASS':True,'source_review_sha256':g['source_review_sha256'],'original_source_records':37405,'all_three_source_output_hashes_bound_to_final_review':True,
 'forced_application_verdict':'PASS','Hall_exclusion_verdict':'PASS','exact_union_verdict':'PASS','forced_application_uniform_over_every_realizing_short_matching':True,'conditional_local_arbitrary_complete_graph_quantifier_checked':True,'local27_final_PASS_bound':True,'generic_safe_completion_final_PASS_bound':True,
 'actual_root_obstruction_exclusion_checked':True,'actual_projected_minority_majority_omission_obstruction_masks_checked':True,'all_six_target_cuts_and_legal_source_subsets_exhausted':True,'legal_source_projections_evaluated':49489,'independent_marked_lookup_entries':3600,'accepted_local_rows_tried':27,'selected_witness_local_indices':c['forced_selected_local_indices'],'selected_safe_witnesses_replayed':552,'safe_forced_subset':552,
 'Hall_explicit_unrealizability_proved':True,'Hall_witnesses_directly_verified':7483,'Hall_scope':'No short Q6 matching realizes the exact certified holes; no negative Hamilton-extension conclusion about an actual matching.','Hall_checks':['nonempty S subset actual covered evens','T equals the entire short neighborhood intersect actual covered odds','strict |T|<|S|','valid unique original target/index'],'Hall_size_histogram':c['Hall_size_histogram'],'matching_solver_executed_or_trusted':False,'Hall_converse_or_solver_failure_used':False,
 'actual_subset_intersection':0,'union_removed':8035,'remaining_covered_target_geometries':29370,'remaining_v1':6315,'remaining_v7':9828,'remaining_v31':13227,'reports':c['reports'],'all_nine_remaining_files_exact_independent_bytes':True,'exact_partition_uses_common_original_indices':True,
 'frozen_unique_files_rehashed_before_and_after':32,'remaining_matching_existence_unverified':True,'remaining_geometries_claimed_realizable':False,'remaining_geometries_claimed_counterexamples':False,'producer_matching_diagnostics_used':False,
 'full_twelve_hole_proved':False,'full_higher_hole_layers_proved':False,'full_P6_proved':False,'production_or_main_state_modified':False,'large_local_certificates_rerun':False},
 'remaining_covered_target_geometries':29370,'full_twelve_hole_proved':False,'full_P6_proved':False,
 'scope':'Three components: exact552 actual safe forced-cherry extensions; direct7483 necessary neighbor-deficiency unrealizability witnesses; exact common-domain union leaving29370 covered-target geometries. Does not assert remaining realizability, full12, higher complete layers or P6.'}
(R/'TWELVE_NEW_FORCED_HALL_REVIEW.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps({'verdict':'PASS','review_sha256':sha('TWELVE_NEW_FORCED_HALL_REVIEW.json'),'report_sha256':sha('TWELVE_NEW_FORCED_HALL_REVIEW.md')},indent=2))
