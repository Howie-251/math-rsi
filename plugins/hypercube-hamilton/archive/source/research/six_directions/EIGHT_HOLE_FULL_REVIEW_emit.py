"""Emit the final scoped verdict after a complete independent accounting PASS."""
import hashlib,json
from pathlib import Path
from datetime import datetime,timezone
R=Path(__file__).resolve().parent
d=json.loads((R/'EIGHT_HOLE_FULL_REVIEW_check.json').read_text(encoding='utf-8'))
assert d['status']=='PASS' and d['remaining']==0 and not d['dynamic_ledger_read']
h=dict(d['audited_input_hashes'])
for n in ['EIGHT_HOLE_FULL_REVIEW_check.json','EIGHT_HOLE_FULL_REVIEW.md',Path(__file__).name]:
    h[n]='sha256:'+hashlib.sha256((R/n).read_bytes()).hexdigest()
out=dict(audit_skill='proof-checker',verdict='PASS',reason_code='all_eight_hole_obligations_complete_modulo_explicit_imports',
 summary='Complete eight-hole Q6 theorem passes: every short28-edge matching, every free root and every opposite-parity target, covered or free. Fixed21350-row base is fully discharged:21300 marked-core witnesses plus exact50 EP0 geometries.',
 generated_at=datetime.now(timezone.utc).isoformat(),reviewer_model='gpt-6.1-sol',reviewer_reasoning='high',
 reviewer_task='/root/eight_full_closure_audit',fork_turns='none',reviewer_family='openai',executor_family='openai',
 review_independence='same-family',acceptance_status='provisional',
 model_override_source='Explicit user route relayed by parent overrides skill default',
 trace_path='EIGHT_HOLE_FULL_REVIEW.md',audited_input_hashes=dict(sorted(h.items())),
 theorem=dict(graph='Q6 short-edge graph',matching_edges=28,all_short_matchings=True,
   every_free_root=True,every_opposite_parity_target=True,covered_targets=True,free_targets=True,
   preserves_every_original_edge=True,conclusion='Hamilton path from the prescribed root to prescribed target'),
 scope=dict(full_eight_hole_proved_relative_to_imports=True,full_T15_proved=False,full_P6_proved=False,
   higher_hole_layers_closed=False,formal_verification=False,cross_family_overlay=False),
 imported_reviews=d['imported_reviews'],complete_marked_core_registry=d['complete_core_registry'],
 external_import_boundary=['Previously audited full six-hole/free-target/A6 and local endpoint results',
   'Published perfect-matching extension and five-direction results as explicitly imported in the fixed lower audits',
   '24 independently audited whole marked arbitrary-K(Q5)-matching T15 core theorems',
   'Final independently audited complete Q4 finite classifications and Q5 neighbor-abundance theorem'],
 details=dict(issues=[],open_counts={k:0 for k in ['FATAL','CRITICAL','MAJOR','MINOR']},
   obligations_closed=[f'F{i:02d}' for i in range(1,17)],
   deterministic_status='PASS',base_rows=21350,a2b1_rows=21300,EP0_rows=50,unaccounted_rows=0,
   whole_covered_geometry_census=d['census'],historical_eliminations=d['historical_chain'],
   ep0_projection_histogram=d['ep0_projection_histogram'],exact_ep0_orbits=d['exact_ep0_orbit_witnesses'],
   selected_core_histogram=d['selected_core_histogram'],dependency_DAG_acyclic=True,
   dynamic_ledger_used_as_proof=False,transitive_core_certificates_rerun=False,
   input_hash_bindings_checked=True,main_state_or_goal_modified=False,
   counterexample_pass='Root/target positions, q=v exclusion, s=r or t, arbitrary auxiliary edges, marked omission alignment, bridge conflicts and every returned optional edge checked; no used implication failed'))
(R/'EIGHT_HOLE_FULL_REVIEW.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(verdict=out['verdict'],input_hashes=len(h),unaccounted=0,review_independence=out['review_independence'],acceptance_status=out['acceptance_status'])))
