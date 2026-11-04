"""Emit the assembly verdict only after the final application PASS gate succeeds."""
import pathlib,json,hashlib,datetime,runpy
R=pathlib.Path(__file__).resolve().parent
runpy.run_path(str(R/'TWELVE_HOLE_FREE_REVIEW_check.py'),run_name='__main__')
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
c=json.loads((R/'TWELVE_HOLE_FREE_REVIEW_check.json').read_text());assert c['status']=='PASS'
report='''# Final independent assembly review: twelve-hole Q6 free endpoints

**PASS**, relative to the explicit final accepted imports. Every26-edge short
matching M of Q6 and every two prescribed free opposite-parity vertices u,v
have a Hamilton u--v path containing M. All path edges are cube edges.
Only the FREE-target twelve-hole theorem is closed. Complete twelve-hole
covered targets, complete higher layers and full P6 remain OPEN.

Fresh assembly reviewer: `/root/higher_q5_nearbalanced_review`, user-selected
GPT-6.1-sol / high. Assurance is same-family / provisional. This is an
independent review of the root producer's TWELVE_HOLE_FREE_CLOSURE.md,
using final accepted reports, not producer pending-status statements.
No producer proof, raw, accepted report or main state was modified.

## Exact quantifiers and proof ledger

For all M subset E(Q6) which are matchings with |M|=26, and for all
distinct u,v outside V(M) of opposite cube parity, there exists a simple
spanning u--v path P with M subset E(P) subset E(Q6). Both endpoints are
prescribed and free. Since every short matching edge covers one vertex
of each parity, M has exactly6 uncovered vertices of each parity.

| ID | Obligation and discharge |
|---|---|
| F01 | If two holes x,y form a short edge, M+xy is a valid27-edge short matching. If xy differs as an unordered edge from uv, it cannot cover both specified endpoints, so at least one of u,v remains free. The complete ten-hole theorem rooted there permits the other prescribed endpoint even when newly covered. Reverse the path if needed. Every edge remains short. |
| F02 | If xy=uv, M+uv has ten remaining holes, so choose another free r and any short neighbor s. The full ten-hole theorem applies to r and its opposite-parity neighbor regardless of whether s is free or covered. It supplies a64-vertex Hamilton path containing M+uv. The edge rs cannot already occur on a simple path between those same endpoints with more than2 vertices. Close with rs, then delete uv. The result has exactly endpoints u,v and still contains M. Since u,v were originally free, the deleted uv was not original; r was free after augmentation, so closing rs was not original and cannot equal uv. |
| F03 | Thus the remaining domain may assume the entire hole set independent. This reduction invokes the complete preceding theorem, including both root parities and covered targets. It cannot be replaced by a theorem only for free targets. The pinned final TEN_HOLE_FULL_REVIEW PASS has exactly the required scope. |
| F04 | Translation by u sends u to0 and the other endpoint to an odd vector, regardless of original root parity. Coordinate permutations normalize that target to1,7,31 according to weights1,3,5. These maps preserve edges, matchings, prescribed endpoints and independent holes and can be inverted after construction. The weight1 case is impossible for independent holes because target would be adjacent to0. |
| F05 | Every remaining matching induces one Z5/W6 geometry in the independently exhaustive normalized domain. The census includes unrealizable geometries, which enlarges the domain safely. No original matching is lost by a feasibility filter or by choosing a favorable realization. |
| F06 | The accepted near-balanced rows require b>=1 and b-a in0,1,2. For odd-source difference2, the actual free target is excluded, and full independence excludes the root mirror from W. Since b>=2 a source exists. The accepted transfer applies to every realizing short matching, not one matching selected by the census. Its exact free residual counts are0/80622/107984, total188606. |
| F07 | The accepted registry reuse uses exact marked local statements and the general multisource transfer with full balanced-Q5 A endpoint inputs. Legal sources exclude free v and the root mirror, actual B holes and omissions are transported together, and arbitrary long/same-parity auxiliary matching edges are allowed. Its exact free residual is0/27/20. The accepted success witnesses and raw complement form an exact byte/order partition, not a subtraction of overlapping counts. |
| F08 | The final T37 application is final PASS. Every remaining free record has a legal two-source row(2,1) or(0,3), with actual minority3/majority7 and precisely its source mirrors omitted. Its common marked image is among the55 accepted rank1024 local rows; the9 other rows are not used. The local statement covers every arbitrary compressed required matching. Completed A holes are1:1, with legal root and prescribed free target. |
| F09 | Independently, every remaining free record has a legal three-source forced-T17 row(4,2) or(1,5), actual minority1/majority7 and precisely its mirrors omitted. Its actual transported obstruction pair excludes root0. The accepted GENERAL forced-cherry theorem applies to free targets and source count3; it constructs the completion proving the actual compressed matching lacks the forbidden edge. The old ten-hole-only application or absence of that edge from original M_B is not substituted for this proof. A holes are2:2. |
| F10 | The transfers use the explicit five-direction Q6 free-root endpoint import when c=0. For c>0 the accepted tagged forest and simultaneous mirror suppression produce the actual required B matching. Expansion restores every original edge and every vertex; completion edges were deleted, compressed edges expanded and the unique uv tag deleted. Therefore the final path has the originally prescribed endpoints, and all surviving added edges are short. With original M short, every path edge is a cube edge. |
| F11 | Each final route separately covers all27 target7 and all20 target31 free records. The independent application checker verifies actual projections, marked membership, root exclusion, all positive witnesses and exact residual sets/bytes. The final free residuals of T37, forced-T17 and their union are all empty. Either route alone completes the47 records; their overlap causes no double counting. |
| F12 | Adjacent-hole reduction, independent normalization, near-balanced successes, reuse successes and the final residual successes exhaust every original free-endpoint input. They produce the same prescribed endpoint assertion at every branch. Existence of completion pairings may depend on the realizing M, which is compatible with the universal-M, existential-path quantifier order. |
| F13 | The dependency DAG is accepted ten-hole preprocessing plus independently accepted Q5 endpoint/marked theorems and generic transfers -> exact normalized filters -> final actual application -> this free-endpoint assembly. Q5 T37 and conditional T17/forced-cherry imports do not assume the desired twelve-hole theorem. No cycle or silent use of a missing higher predecessor occurs. |

## Final gates and independent assembly checks

The assembly checker requires final PASS for all seven relevant reports:
TEN_HOLE_FULL_REVIEW; HIGHER_Q5_FULL_REVIEW;
HIGHER_Q5_FULL_REUSE_REVIEW; HIGHER_Q5_FULL_T37_APPLICATION_REVIEW;
Q5_T37_INDEPENDENT_REVIEW; Q5_T17_RANK_BATCH_REVIEW; and
HIGHER_FORCED_CHERRY_REVIEW. It checks current theorem hashes against
their accepted report bindings and checks every application-manifest file
hash and byte length. The final application review is required to bind
that exact manifest and proof. No draft report is used as acceptance.

The checker additionally decodes the frozen16-byte T37 witnesses and32-byte
forced witnesses and checks that their free-record index sets are exactly
{0,...,26} for target7 and {0,...,19} for target31, separately in EACH
route. It rejects excluded T37 indices, nonaccepted forced row IDs, duplicate
indices and an actual B obstruction containing projected root0. The47
source records are distinct, have the prescribed free target, and have
fully independent holes. Their input hashes match the accepted reuse
residual, which matches the final application's input. All nine separate
route/union free residual files are checked empty. The prior full-domain
census, reuse and final-application audits are imported as accepted
deterministic evidence, rather than rerunning their large certificates.

| Normalized target | After near-balanced rows | After accepted reuse | After either final route |
|---:|---:|---:|---:|
|1|0|0|0|
|7|80622|27|0|
|31|107984|20|0|
|Total|188606|47|0|

Counterexample-first boundaries checked: an added hole edge touching one
prescribed endpoint; the special added edge uv; a neighbor s which is
covered or equals one of the original prescribed endpoints; closing rs
already in the Hamilton path; odd original root; adjacent weight1 target;
a source equal to free v or the root mirror; an unmarked local image;
an excluded/nonfull T37 row; root in the actual forced obstruction; a
missing compressed-matching avoidance argument; a target crossing port;
and an empty-crossing instance. The explicit hypotheses and the imported
final theorems resolve each case. No remaining gap or counterexample was
found within the theorem's exact scope. No limiting, probabilistic or
asymptotic claims enter this finite argument.

## Accepted scope

Set `twelve_hole_free_targets_proved=true` only for the theorem with BOTH
specified endpoints free. The exact combined application still leaves
215243 covered-target geometries, so complete twelve-hole closure and
full P6 remain false. This free-target result is not the complete preceding
endpoint theorem required for all fourteen-hole reductions. No unrestricted
T37 or full T17 theorem is asserted. Semantic acceptance is same-family /
provisional relative to the explicit accepted literature and finite inputs,
and is not formal verification.
'''
(R/'TWELVE_HOLE_FREE_REVIEW.md').write_text(report,encoding='utf-8')
sources={n:sha(n) for n in ['TWELVE_HOLE_FREE_CLOSURE.md',*c['proof_bindings'],*c['final_PASS_imports'],'HIGHER_Q5_FULL_T37_APPLICATION_MANIFEST.json']}
app=json.loads((R/'HIGHER_Q5_FULL_T37_APPLICATION_REVIEW.json').read_text())
manifest=json.loads((R/'HIGHER_Q5_FULL_T37_APPLICATION_MANIFEST.json').read_text())
artifacts=['TWELVE_HOLE_FREE_REVIEW_check.py','TWELVE_HOLE_FREE_REVIEW_check.json','TWELVE_HOLE_FREE_REVIEW_emit.py']
d={'audit_skill':'proof-checker','verdict':'PASS','reason_code':'complete_twelve_hole_two_prescribed_free_endpoint_assembly_closed_modulo_final_accepted_imports',
 'summary':'Every26-short-edge Q6 matching has a Hamilton extension between every prescribed opposite-parity free endpoint pair. Exact free-domain chain188606 ->47 ->0 is final PASS; complete covered-target twelve-hole and P6 remain OPEN.',
 'reviewer_agent_id':'/root/higher_q5_nearbalanced_review','reviewer_model':'gpt-6.1-sol','reviewer_reasoning':'high','model_override_source':'Explicit user-selected route relayed by parent overrides ARIS defaults',
 'reviewer_family':'openai','executor_family':'openai','review_independence':'same-family','acceptance_status':'provisional','generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'trace_path':'TWELVE_HOLE_FREE_REVIEW.md','audited_input_hashes':sources,
 'imported_application_input_hashes':manifest['hashes'],'checker_artifact_hashes':{n:sha(n) for n in artifacts},'report_hash':sha('TWELVE_HOLE_FREE_REVIEW.md'),
 'details':{'issues':[],'mathematical_obligations_closed':13,'theorem_matching_edges':26,'theorem_holes':12,'both_prescribed_endpoints_free_required':True,'every_short_matching_quantifier':True,'every_opposite_parity_free_endpoint_pair_quantifier':True,
 'adjacent_holes_non_uv_reduction_checked':True,'uv_special_case_cycle_and_deletion_checked':True,'complete_predecessor_including_covered_targets_used':True,'all_root_parities_checked':True,'target_weights_exhaustive':[1,3,5],'free_target_legal_source_and_root_mirror_exclusions_checked':True,'actual_marked_transfer_inputs_checked':True,'five_direction_zero_crossing_import_explicit':True,
 'final_application_verdict':app['verdict'],'all_final_dependencies_PASS':True,'all_47_free_inputs_in_each_final_route':True,'exact_free_chain':c['free_domain_chain'],'remaining_free_geometries':0,'remaining_free_target_geometries':0,'remaining_covered_geometries':215243,'noncircular_dependencies_checked':True,
 'twelve_hole_free_targets_proved':True,'full_twelve_hole_proved':False,'twelve_hole_covered_targets_proved':False,'full_higher_hole_layers_proved':False,'full_P6_proved':False,'production_or_main_state_modified':False,'large_upstream_certificates_rerun':False},
 'twelve_hole_free_targets_proved':True,'full_twelve_hole_proved':False,'full_P6_proved':False,
 'scope':'Complete twelve-hole Q6 theorem for two prescribed opposite-parity free endpoints only, relative to final accepted imports. Covered-target/full-layer/higher-layer/P6 claims remain OPEN.'}
(R/'TWELVE_HOLE_FREE_REVIEW.json').write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'verdict':'PASS','review_sha256':sha('TWELVE_HOLE_FREE_REVIEW.json'),'report_sha256':sha('TWELVE_HOLE_FREE_REVIEW.md')},indent=2))
