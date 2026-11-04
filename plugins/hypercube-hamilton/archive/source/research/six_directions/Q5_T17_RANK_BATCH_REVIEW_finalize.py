from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parent
def load(n):return json.loads((R/n).read_text(encoding='utf-8'))
def digest(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
m=load('Q5_T17_RANK_BATCH_MANIFEST.json');c=load('Q5_T17_RANK_BATCH_REVIEW_checks.json')
assert c['status']=='PASS' and c['forests']==27648 and c['matrix_bits']==49283072
assert digest('Q5_T17_RANK_BATCH_MANIFEST.json')==c['manifest_sha256']
inputs={'Q5_T17_RANK_BATCH_MANIFEST.json':c['manifest_sha256']}
for n,h in m['input_hashes'].items():
    assert digest(n)==h.removeprefix('sha256:');inputs[n]=digest(n)
imports=['A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md','HIGHER_HOLE_UNIFIED_TRANSFER.md','HIGHER_HOLE_UNIFIED_TRANSFER_REVIEW.json','Q5_T26_RANK_BATCH_REVIEW.json']
for n in ('HIGHER_HOLE_UNIFIED_TRANSFER_REVIEW.json','Q5_T26_RANK_BATCH_REVIEW.json'):
    x=load(n);assert x['verdict']=='PASS'
    for name,h in x['audited_input_hashes'].items():assert digest(name)==h.removeprefix('sha256:'),(n,name)
artifacts=['Q5_T17_RANK_BATCH_REVIEW_check.cpp','Q5_T17_RANK_BATCH_REVIEW_check.py','Q5_T17_RANK_BATCH_REVIEW_finalize.py','Q5_T17_RANK_BATCH_REVIEW_checks.json','Q5_T17_RANK_BATCH_REVIEW_local.json']+[x['remaining_file'] for x in c['reports']]
out=dict(audit_skill='proof-checker',verdict='PASS',reason_code='all_seventeen_local_classifications_root_not_ob_universal_transfer_and_exact_actual_coverage_complete_modulo_explicit_imports',summary='17 local arbitrary-matching classifications and root-not-OB universal transfer PASS; accepted4096 has disjoint2598 unforced+1036 safe forced, exact residual462. No T15 import or whole-layer closure.',reviewer_agent_id='/root/t17_safe_transfer_review',reviewer_model='gpt-6.1-sol',reviewer_reasoning='high',model_override_source='Explicit user route relayed by parent overrides skill default',reviewer_family='openai',executor_family='openai',review_independence='same-family',acceptance_status='provisional',generated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),trace_path='Q5_T17_RANK_BATCH_REVIEW.md',audited_input_hashes=inputs,imported_dependency_hashes={n:digest(n) for n in imports},accepted_input_hashes=c['source_hashes'],checker_artifact_hashes={n:digest(n) for n in artifacts},report_hash=digest('Q5_T17_RANK_BATCH_REVIEW.md'))
out['details']=dict(issues=[],local_theorems=17,unforced_local_orbits=10,forced_local_orbits=7,unforced_rank=2048,forced_reduced_rank=1024,forests_verified=27648,connectivity_bits_recomputed=49283072,independent_gaussian_eliminations=17,all_pivot_xor_certificates_verified=True,local_obligations_closed=12,transfer_obligations_closed=12,root_not_OB_universal_transfer_proved_modulo_imports=True,target_port_degenerate_case_verified=True,arbitrary_original_local_matching_edges=True,original_Q6_matching_short=True,Q6_target_covered=True,Q6_rows=[[3,1],[0,4]],root_in_OB_projections_used=0,accepted_input_records=4096,unforced_union_covered=2598,safe_forced_only_covered=1036,net_new_covered=3634,total_remaining=462,reports=c['reports'],actual_projection_counts=c['actual_projection_counts'],exact_remaining_bytes_equal_producer=True,no_T15_import=True,full_T17_proved=False,full_ten_hole_proved=False,full_P6_proved=False,production_state_modified=False)
out['reports']=c['reports']
(R/'Q5_T17_RANK_BATCH_REVIEW.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(verdict=out['verdict'],json_sha256=digest('Q5_T17_RANK_BATCH_REVIEW.json'),report_hash=out['report_hash'],remaining=462),indent=2))
