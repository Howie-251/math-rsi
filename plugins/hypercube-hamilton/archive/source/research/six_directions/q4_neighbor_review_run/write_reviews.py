import datetime, hashlib, json
from pathlib import Path
R=Path(__file__).resolve().parent.parent
def digest(p):return 'sha256:'+hashlib.sha256((R/p).read_bytes()).hexdigest()
def hashes(fs):return {p:digest(p) for p in fs}
def main():
    result=json.loads((R/'Q4_NEIGHBOR_ABUNDANCE_REVIEW_check.json').read_text(encoding='utf-8'))
    assert result['status']=='PASS'
    geo=json.loads((R/'EIGHT_ALL_EP0_CONSEQUENCES_REVIEW_check.json').read_text(encoding='utf-8'))
    assert geo['status']=='PASS'
    bindings={}
    for review,source in [('T15_CORE1_FULL_REVIEW.json','T15_CORE1_FULL_CLOSURE.md'),('T15_CORE4_FULL_REVIEW.json','T15_CORE4_FULL_CLOSURE.md'),('EIGHT_DOUBLE_BRIDGE_REVIEW.json','EIGHT_HOLE_COVERED_NEXT_DRAFT.md')]:
        old=json.loads((R/review).read_text(encoding='utf-8'));assert old['verdict']=='PASS'
        assert digest(source)==old['audited_input_hashes'][source]
        bindings[review]=dict(sha256=digest(review),bound_source=source,source_sha256=digest(source))
    assert digest('T15_CORE4_FULL_REVIEW.json')=='sha256:28c5adea5c9a944247ebbcaf8ebaf8df58c832e9f613080a709576ab12f52cd9'
    base=dict(audit_skill='proof-checker',verdict='PASS',reason_code='all_scoped_obligations_complete_modulo_explicit_imports',
              reviewer_model='gpt-6.1-sol',reviewer_reasoning='high',reviewer_family='openai',executor_family='openai',
              review_independence='same-family',acceptance_status='provisional',reviewer_task='/root/ep0_neighbor_lifting_audit',
              model_override_source='Explicit user preference relayed by parent overrides skill default',
              generated_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
    finite=['eight_ep0_q4_neighbor_inverse.py','eight_ep0_q4_neighbor_inverse.json',
            'verify_eight_ep0_q4_neighbor_spectrum.cpp','eight_ep0_q4_neighbor_spectrum_verification.json',
            'eight_ep0_q4_pair_spectrum.cpp','eight_ep0_q4_pair_spectrum.json',
            'q4_perfect_endpoint_abundance_check.py','q4_perfect_endpoint_abundance_check.json','Q4_PERFECT_ENDPOINT_ABUNDANCE.md',
            'q4_distance1_avoided_table.bin','q4_distance3_avoided_table.bin','CANONICAL_COMPLETION_REVIEW.json',
            'eight_ep0_q4_star_A_prepare.cpp','eight_ep0_q4_star_A.bin','eight_ep0_q4_star_A.jsonl',
            'eight_ep0_q4_PB_bad_optional.py','eight_ep0_q4_PB_bad_optional.txt',
            'eight_ep0_q4_star_joint.cpp','eight_ep0_q4_star_joint.json',
            'Q4_NEIGHBOR_ABUNDANCE_REVIEW_check.py','Q4_NEIGHBOR_ABUNDANCE_REVIEW_check.json']
    q4=dict(base,summary='Q4 union>=3, perfect-matching optional short-root union>=2, complete444 A-star/16816 B bad-key inputs and60316956 nonempty joint intersections pass fresh semantic and deterministic checks.',
            trace_path='Q4_NEIGHBOR_ABUNDANCE_REVIEW.md',audited_input_hashes=hashes(finite),
            imported_theorems=['Previously audited exact Q4 opposite-hole tables; their raw hashes were checked against CANONICAL_COMPLETION_REVIEW.json'],
            deterministic_checks=result,details=dict(issues=[],fatal=0,critical=0,major=0,minor=0),
            full_Q5_proof_scope='See separate EIGHT_ALL_EP0_CONSEQUENCES_REVIEW.json',full_P6_proved=False)
    (R/'Q4_NEIGHBOR_ABUNDANCE_REVIEW.json').write_text(json.dumps(q4,indent=2)+'\n')
    extra=['Q5_NEIGHBOR_ABUNDANCE_AND_EP0.md',
           'eight_ep0_three_neighbor_geometry.py','eight_ep0_three_neighbor_geometry.json',
           'eight_ep0_three_neighbor_projection.py','eight_ep0_three_neighbor_projection.json',
           'EIGHT_ALL_EP0_CONSEQUENCES_REVIEW_check.py','EIGHT_ALL_EP0_CONSEQUENCES_REVIEW_check.json',
           'Q4_NEIGHBOR_ABUNDANCE_REVIEW.md','Q4_NEIGHBOR_ABUNDANCE_REVIEW.json',
           'T15_CORE1_FULL_CLOSURE.md','T15_CORE1_FULL_REVIEW.json',
           'T15_CORE4_FULL_CLOSURE.md','T15_CORE4_FULL_REVIEW.json',
           'EIGHT_HOLE_COVERED_NEXT_DRAFT.md','EIGHT_DOUBLE_BRIDGE_REVIEW.json','EIGHT_DOUBLE_BRIDGE_REVIEW.md']
    ep=dict(base,summary='Q5 equal-parity-hole neighbor union>=3 and the stated EP0 conversion pass; every realizing short matching in the exact fifty normalized Q6 geometries has the required Hamilton path by marked core1/core4 and audited transfer.',
            trace_path='EIGHT_ALL_EP0_CONSEQUENCES_REVIEW.md',audited_input_hashes=hashes(finite+extra),
            imported_review_bindings=bindings,external_imports=[
                'Fink arbitrary-complete-graph Q4 perfect-matching extension theorem with only short added edges, as imported in the earlier fixed Q4 audits',
                'Previously audited exact Q4 opposite-hole tables, raw hashes rechecked',
                'Complete marked arbitrary K(Q5) T15 core1 and core4 theorems, sources rebound to final review hashes',
                'Previously audited (2,0)+EP0+T15 two-bridge transfer, source hash rebound',
                'Existing classification of seven residual geometry representatives; only their precise fifty target-preserving images are concluded here'],
            theorems=dict(Q5_neighbor_union_at_least_3=True,EP0_under_three_S_neighbor_condition=True,
                          exact_fifty_Q6_geometries=True,all_required_T15_cores_proved=True),
            Q5_claim='For every arbitrary K(V(Q5)) matching with distinct equal-parity holes q,v, at least three short q neighbors occur over valid31-cycles omitting v.',
            consequence_claim='For every realizing short Q6 matching in each listed(root0,target,Z,W) geometry, a Hamilton0-to-target path preserves the matching.',
            closed_geometries=geo['closed_geometries'],closed_geometry_count=50,
            projection_cases=234,core_histogram=geo['core_histogram'],orbit_sizes=geo['orbit_sizes'],
            details=dict(issues=[],proof_obligations=24,fatal=0,critical=0,major=0,minor=0,
                         deterministic_check_status='PASS',fresh_Q4_checks=result,
                         dynamic_main_ledgers_used_as_theorem_dependencies=False),
            full_T15_proved=False,full_eight_hole_proved=False,full_P6_proved=False,
            scope_note='Exact fifty consequences only; parent separately audits any complete eight-hole assembly. No main ledger edited.')
    (R/'EIGHT_ALL_EP0_CONSEQUENCES_REVIEW.json').write_text(json.dumps(ep,indent=2)+'\n')
    for name in ['Q4_NEIGHBOR_ABUNDANCE_REVIEW.json','EIGHT_ALL_EP0_CONSEQUENCES_REVIEW.json']:
        check=json.loads((R/name).read_text(encoding='utf-8'))
        assert all(digest(p)==h for p,h in check['audited_input_hashes'].items())
    print(json.dumps(dict(status='PASS',closed_geometry_count=50,core4_review_hash=digest('T15_CORE4_FULL_REVIEW.json'),review_files=['Q4_NEIGHBOR_ABUNDANCE_REVIEW.json','EIGHT_ALL_EP0_CONSEQUENCES_REVIEW.json'])))
if __name__=='__main__':main()
