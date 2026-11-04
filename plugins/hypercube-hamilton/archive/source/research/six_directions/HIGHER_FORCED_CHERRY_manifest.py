from pathlib import Path
import hashlib,json,datetime
R=Path(__file__).resolve().parent
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
proofs=['HIGHER_FORCED_CHERRY_TRANSFER.md']
checks=['HIGHER_FORCED_CHERRY_author_check.py','HIGHER_FORCED_CHERRY_author_check.json','HIGHER_FORCED_CHERRY_manifest.py']
imports=['Q5_A10_FULL_CLOSURE.md','Q5_A10_FULL_REVIEW.json','Q5_HIGHER_HOLE_REDUCTION.md','Q5_HIGHER_HOLE_REDUCTION_REVIEW.json','HIGHER_HOLE_UNIFIED_TRANSFER.md','HIGHER_HOLE_UNIFIED_TRANSFER_REVIEW.json','Q5_T17_RANK_ROOT_NOT_OB_TRANSFER.md','Q5_T17_RANK_BATCH_REVIEW.json','A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md']
for n in imports:
    if n.endswith('_REVIEW.json'):assert json.loads((R/n).read_text(encoding='utf-8'))['verdict']=='PASS'
c=json.loads((R/'HIGHER_FORCED_CHERRY_author_check.json').read_text())
assert c['status']=='AUTHOR_SANITY_PASS_PENDING_FRESH_REVIEW'
out=dict(status='PRODUCER_COMPLETE_CONDITIONAL_PROOFS_PENDING_FRESH_REVIEW',generated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),proof_status='PROVABLE AS STATED relative to explicitly assumed local inputs',input_hashes={n:sha(n) for n in proofs+checks+imports},theorems=['single_cherry_uniform_transfer_s_ge_3_both_target_statuses','multiple_cherry_local_iff_labeled_F_plus_R_acyclic_from_reduced_full_rank','multiple_cherry_uniform_transfer_with_automatic_extra_gap'],global_short_matching=True,nonroot_holes_independent=True,free_target_legal_sources_required=True,full_hole_independence_suffices_for_free_source_existence=True,root_excluded_from_all_obstruction_endpoints=True,all_obstruction_endpoints_same_parity_as_Y=True,additional_matching_dependent_gap_assumption=False,automatic_gap_bound='j <= floor(c/2) < d for s>=3',scope_hole_counts=[12,14,16,18],any_higher_whole_layer_proved=False,full_P6_proved=False,production_state_modified=False,author_sanity_counts={'local_pairing_comparisons':c['local_pairing_comparisons'],'automatic_gap_parameter_cases':c['automatic_gap_parameter_cases']})
(R/'HIGHER_FORCED_CHERRY_MANIFEST.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'manifest_sha256':sha('HIGHER_FORCED_CHERRY_MANIFEST.json'),'proof_sha256':sha(proofs[0]),'status':out['status']},indent=2))
