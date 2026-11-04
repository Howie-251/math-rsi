"""Emit only after the independent final checker and semantic audit close."""
from pathlib import Path
import datetime,hashlib,json
R=Path(__file__).resolve().parent
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
c=json.loads((R/'P6_FULL_REVIEW_check.json').read_text('utf-8'))
assert c['stage']=='final' and not c['errors'] and c['dependency_DAG_acyclic']
for n,h in c['gates'].items():assert sha(n)==h
assert sha('P6_FULL_CLOSURE.md')==c['frozen_P6_proof_hash']
p=R/'P6_FULL_REVIEW.md';text=p.read_text('utf-8')
text=text.split('\n## Final checked result\n')[0]
text=text.replace('FINAL GATE PENDING. The root/lower-layer review is complete; final acceptance\nmust await the bound full fourteen- and sixteen/eighteen-hole reports.',
 '**PASS: complete P6 is proved relative to the explicit accepted imports.**\nAll nine complete layers and the root-preserving range reduction are accepted.\nThere are zero remaining predecessor conditions or hole levels.')
text=text.replace('FOURTEEN_HOLE_FULL_REVIEW; final acceptance pending','FOURTEEN_HOLE_FULL_REVIEW; complete12 predecessor discharged, both endpoint branches complete')
text=text.replace('SIXTEEN_EIGHTEEN_FULL_REVIEW; final acceptance pending','SIXTEEN_EIGHTEEN_FULL_REVIEW; complete14=>complete16=>complete18 predecessors discharged')
text+='\n## Final checked result\n\n'
text+=f"The final independent run rehashed {c['bound_files_rehashed']} distinct bound files,\ntraversed {c['transitive_review_nodes']} accepted review nodes and {c['report_dependency_edges']}\nbound report edges, and checked {c['evidence_bindings']} auxiliary evidence bindings.\nThere are no missing/stale bindings, dependency cycles or unresolved imported\nconditions in the supported declared schemas. Directly bound manifest input/output\nfiles are checked; arbitrary undocumented metadata is not recursively interpreted.\nThe final14 source is exactly the independently reconstructed disjoint20/5 orbit\nunion. On each target, the final16 star and small-cut retained sets partition\nthe same source exactly and have empty intersection; their positive union\ntherefore leaves no record. The complete16 antecedent discharges the precise\ncomplete16=>complete18 implication. Final14, final16 and final18 each have\nzero free and covered residuals.\n\n"
text+='This closes the original arbitrary short-matching theorem with every free\nroot and every opposite-parity target, including targets covered before or\nduring augmentation. All substantive imported premises remain explicit; no\nfull original literature proof or large historical finite computation was\nrepeated here. No fatal, critical, major or minor open issue remains in\nthis final assembly at the stated import and assurance boundary.\n'
p.write_text(text,encoding='utf-8')
proofs=['P6_FULL_CLOSURE.md','GENERAL_NEAR_PERFECT.md','FOUR_HOLE_FULL.md',
 'SIX_HOLE_CLOSED.md','EIGHT_HOLE_FULL_CLOSURE.md','TEN_HOLE_FULL_CLOSURE.md',
 'TWELVE_HOLE_FULL_CLOSURE.md','FOURTEEN_HOLE_FULL_CLOSURE.md',
 'SIXTEEN_EIGHTEEN_FULL_CLOSURE.md','ROOTED_MAXIMAL_18_HOLES.md',
 'A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md']
d={'audit_skill':'proof-checker','verdict':'PASS',
 'reason_code':'all_original_P6_proof_obligations_complete_modulo_explicit_imports',
 'summary':'Complete P6: every Q6 short matching, every free root and every opposite-parity target including covered targets; all nine layers and predecessors closed relative to explicit accepted imports.',
 'reviewer_agent_id':'/root/p6_final_independent_audit',
 'reviewer_model':'gpt-6.1-sol','reviewer_reasoning':'high',
 'model_configuration_source':'Parent authorized requested GPT-6.1-sol/high; served backend not independently attested',
 'reviewer_family':'openai','executor_family':'openai',
 'review_independence':'same-family','acceptance_status':'provisional',
 'generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'trace_path':'P6_FULL_REVIEW.md',
 'audited_input_hashes':{n:sha(n) for n in proofs},
 'imported_dependency_hashes':c['gates'],
 'checker_artifact_hashes':{n:sha(n) for n in ['P6_FULL_REVIEW_check.py','P6_FULL_REVIEW_check.json','P6_FULL_REVIEW_emit.py']},
 'report_hash':sha('P6_FULL_REVIEW.md'),
 'details':{'issues':[],'full_P6_proved':True,'all_original_short_matchings':True,
  'every_free_root':True,'every_opposite_parity_target_including_covered':True,
  'all_predecessor_conditions_discharged':True,'dependency_DAG_acyclic':True,
  'remaining_full_p6_hole_levels':[],'complete_hole_levels':[2,4,6,8,10,12,14,16,18],
  'canonical_statement':'For every matching M subset E(Q6), every u outside V(M), and every v of opposite parity, there exists a Hamilton u-v path containing M.',
  'root_preserving_maximalization_checked':True,'covered_after_augmentation_target_included':True,
  'rooted_range_literature_import':'Havel-Krivanek 1982 Theorem2: every inclusion-maximal full-Q6 matching has at least24 edges',
  'external_literature_original_proofs_reproved':False,
  'explicit_external_literature_imports':['Havel-Krivanek 1982 Theorem2 maximal Q6 matching bound',
   'Fink perfect-matching extension theorem',
   'Fink-Muetze extension/avoidance/endpoint theorems and established five-direction endpoint theorem at the lower audited scopes',
   'Cygan-Kratsch-Nederlof 2018 Theorem3.4/Corollary3.5: GF2 complete matching-connectivity rank 2^(t/2-1) for even t; DOI10.1145/3148227'],
  'all_live_bound_files_rehashed':c['bound_files_rehashed'],
  'transitive_review_nodes':c['transitive_review_nodes'],'report_dependency_edges':c['report_dependency_edges'],
  'ordered_opposite_parity_endpoint_pairs_checked':2048,
  'final14_exact_orbit_union_independently_checked':True,
  'final16_exact_complementary_retained_sets_independently_checked':True,
  'restricted_R4_bridge_import_discharged':True,'live_mutable_ledgers_used_as_premises':False,
  'supported_binding_scope':'Declared audited_input_hashes/imported_dependency_hashes/checker_artifact_hashes/formal_imports, named auxiliary evidence maps with legacy alias resolution, report hashes, and directly bound manifest input/output maps; not arbitrary undocumented metadata.',
  'large_local_certificates_rerun':False,'producer_code_executed':False,
  'proof_assistant_verified':False,'cross_family_review':False,
  'novelty_peer_review_or_publication_certified':False,
  'arbitrary_complete_graph_Q6_matching_claim':False,
  'frozen_proofs_certificates_or_ledgers_modified':False}}
(R/'P6_FULL_REVIEW.json').write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'verdict':'PASS','P6_FULL_REVIEW.json':sha('P6_FULL_REVIEW.json'),'report_hash':d['report_hash']}))
