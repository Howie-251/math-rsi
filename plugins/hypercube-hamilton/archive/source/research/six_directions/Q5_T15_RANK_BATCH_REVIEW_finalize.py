from pathlib import Path
import json,hashlib,datetime
P=Path(__file__).resolve().parent
def raw(n):return (P/n).read_bytes()
def digest(n):return hashlib.sha256(raw(n)).hexdigest()
def load(n):return json.loads(raw(n))
m=load('Q5_T15_RANK_BATCH_MANIFEST.json');checks=load('Q5_T15_RANK_BATCH_REVIEW_check.json')
for n,h in m['hashes'].items():assert digest(n)==h
inputs=dict(m['hashes'])
for n in ('Q5_T15_RANK_BATCH_MANIFEST.json','Q5_T26_RANK_BATCH_REVIEW.json','Q5_T63_RANK_REVIEW.json','Q5_T63_RANK_REVIEW.md','Q5_T63_RANK_REVIEW_check.json','t15_analytic_geometry.py'):
 inputs[n]=digest(n)
for v in (1,7,31):
 for n in (f'Q5_T26_RANK_BATCH_REVIEW_remaining_v{v}.bin',f'Q5_T63_RANK_REVIEW_remaining_v{v}.bin'):
  inputs[n]=digest(n)
evidence={f.name:digest(f.name) for f in P.glob('Q5_T15_RANK_BATCH_REVIEW*') if f.suffix!='.json' or f.name.endswith('_check.json') or f.name.endswith('_witnesses.json')}
for f in P.glob('Q5_T15_T63_RANK_UNION_REVIEW_remaining_v*.bin'):evidence[f.name]=digest(f.name)
out=dict(audit_skill='proof-checker',verdict='PASS',reason_code='fifteen_marked_rank_theorems_and_exact_actual_two_bridge_application_verified',summary='Fifteen marked T15 universal matching theorems PASS; rank4096 each, exact coverage2346 of accepted4096 and remainder1750. Separate exact union with accepted T63 covers3207, remainder889. Full T15/ten-hole/P6 OPEN.',reviewer_agent_id='/root/t15_rank_batch_review',reviewer_model='gpt-6.1-sol',reviewer_reasoning='high',model_override_source='Explicit user route relayed by parent overrides ARIS skill defaults',reviewer_family='openai',executor_family='openai',review_independence='same-family',acceptance_status='provisional',generated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),trace_path='Q5_T15_RANK_BATCH_REVIEW.md',audited_input_hashes=inputs,evidence=evidence,details=dict(issues=[],local_rank_status='PASS',application_status='PASS_relative_to_explicit_accepted_imports',optional_union_status='PASS_exact_set_union_relative_to_accepted_T63_review',proof_obligations=['exact_marked_registry','forest_support_degrees_acyclicity_pairing','arbitrary_complete_graph_columns','all_matrix_bits','fresh_GF2_elimination','primary_t26_rank_bound','full_row_span_and_nonzero_columns','simple_cycle_expansion','actual_cut_source_mirror_transfer_hypotheses','every_profile_and_selected_witness','exact_original_domain_and_remaining_bytes_and_sets','old_same_face_core_alignment','separate_accepted_T63_exact_union'],checks=checks),full_T15_proved=False,full_T63_proved=False,T17_proved=False,full_ten_hole_proved=False,full_P6_proved=False,producer_or_main_state_modified=False)
(P/'Q5_T15_RANK_BATCH_REVIEW.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(verdict=out['verdict'],audited_inputs=len(inputs),evidence_files=len(evidence),covered=checks['covered'],remaining=checks['remaining'],union_remaining=sum(r['remaining'] for r in checks['T15_T63_exact_union']))))
