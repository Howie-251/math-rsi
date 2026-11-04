"""Emit only after the final independent assembly check and all gates pass."""
import datetime,hashlib,json,pathlib
R=pathlib.Path(__file__).resolve().parent
def read(n):return json.loads((R/n).read_text('utf-8-sig'))
def sha(n):
 h=hashlib.sha256()
 with (R/n).open('rb') as f:
  for b in iter(lambda:f.read(2**20),b''):h.update(b)
 return h.hexdigest()
c=read('FOURTEEN_HOLE_FULL_REVIEW_check.json')
assert c['stage']=='final' and not c['errors'] and c['full_fourteen_hole_proved']
assert not c['full_P6_proved']
for n,v in c['direct_gates'].items():assert sha(n)==v,(n,'changed after final check')
proof='FOURTEEN_HOLE_FULL_CLOSURE.md'
report='FOURTEEN_HOLE_FULL_REVIEW.md'
text=f'''# Complete fourteen-hole independent assembly review

**PASS, relative to the explicit accepted imports.** For every matching M
of 25 short edges of Q6, every u outside V(M), and every opposite-parity
vertex v, including a covered target, there is a Hamilton u--v path
containing every edge of M. Both free and covered residuals are zero.
This accepts the complete fourteen-hole layer. It does not accept full P6.

Reviewer `/root/full14_audit_resume` applied the ARIS proof-checker skill to
the frozen `FOURTEEN_HOLE_FULL_CLOSURE.md` (SHA256 `{sha(proof)}`).
This is a fresh assembly audit of the quantified argument and its exact
accepted interfaces. Assurance is **same-family / provisional**, not Lean
verification or cross-family semantic acceptance. Imported finite proofs
remain explicit premises at their audited scopes.

## Quantifiers and proof obligations

| ID | Obligation and discharge |
|---|---|
| A01 | M is an arbitrary original cube-edge matching of size25. Every matching edge covers one vertex of each parity, leaving seven holes per parity. A normalized record Z6/W7 therefore encodes the full hole set with the root separated from Z. No matching sample or hidden direction filter is used. |
| A02 | Translate by the actual root u and permute the six coordinates. All 2048 ordered opposite-parity endpoint pairs were checked: the root becomes0, the target becomes1,7,31, and the map is a bijection preserving every cube edge. Translation also covers an originally odd root. Inverse transport restores the original path and matching. |
| A03 | The complete TWELVE_HOLE_FULL_REVIEW is PASS with covered targets and arbitrary realizing original matching scope. Its live digest is the exact predecessor bound in REUSE/CACHED. The earlier higher-layer predecessor condition is thus discharged without assuming full14. |
| A04 | For a covered target, adding an adjacent nonroot pair of holes leaves the root free and the target covered. Apply full12 to the augmented matching. For a free target, any adjacent hole edge other than uv leaves at least one prescribed endpoint free; apply full12 rooted there and reverse if necessary. |
| A05 | In the special adjacent-hole case uv, augment by uv, choose another free root r and any short neighbor s, and use full12 for a Hamilton r--s path containing uv. Add rs to close a cycle and delete uv. On64 vertices rs cannot already be a Hamilton endpoint edge. Neither u nor v was originally matched, so no required edge is lost. This is explicitly audited by HALL. |
| A06 | The accepted near-balanced reduction/census exhausts the remaining normalized actual domains. Arbitrary auxiliary completion/compression matchings lie inside the full-Q5 complete-graph matching quantifiers, with both orientations and exact parameter ranges checked by that review. Its exact initial residual is 9252401 covered and232042 free records. |
| A07 | REUSE and CACHED each affirm the universal original-M conclusion, replay all positive constructions, and retain the exact source-order complement. CACHED uses only its accepted20 universal local inputs. No failed rank, unsuccessful search, or candidate class is treated as a negative theorem. |
| A08 | HALL removes only impossible actual-hole geometries: every covered even vertex in S needs a distinct covered odd neighbor, contradicting an explicit strict deficiency. The accepted complete-neighborhood certificates remove8623 records and leave3923 covered/0 free. In particular all18 remaining free records are impossible. The full free-target branch is closed here. |
| A09 | FORCED uses the actual compressed labelled L+R acyclicity statement, including simultaneous cherries, cut/source restrictions and root avoidance. It is universal over every original M. Absence only from the original B matching is not substituted for absence from the compressed matching. Its exact covered complement is2587. |
| A10 | MAXIMAL_A and STAR_EXPANDED enumerate complete inclusion-maximal A domains, not just maximum matchings, and prove the lift from an arbitrary actual internal submatching. Added extension edges are completion edges; extra original holes remain bridge sources. Exact forests, common marked maps, actual B obstruction exclusion and target-edge restoration are accepted, leaving2527 then2407 covered records. |
| A11 | GLOBAL35 uses only the exact accepted local class35, with actual universal forced-transfer hypotheses discharged; MID_SELECTED uses only indices1,15,44. Both bind exact source/output streams and universal realizing-M scope. Their exact complements are2287 then25 covered records. |
| A12 | Independently generate all first-five-coordinate target stabilizer maps. The final source is exactly the disjoint20/5 orbit union of Z={{39,43,45,51,53,57}}, W0={{1,2,4,8,14,16,32}}, W1={{1,2,4,8,16,32,62}}. Neither the orbit sizes nor source counts replace set equality. |
| A13 | FINAL25 is an independently finalized PASS, with complete finite maximal-A domains and exact B certificates. Its universal lift treats actual internal targets and actual crossing target31--63 separately even when maximalization adds an internal target edge. In orbit1 even30 is mandatory internally covered because mirror62 is an original hole. Every actual matching extends into the accepted domain. Auxiliary target edges are removed and the original target edge is restored. Exact final residuals are empty. |
| A14 | Consecutive source/output files agree by live hash and exact13-byte record counts. All named gates are accepted at their precise scopes and the supported declared theorem dependency DAG is acyclic. No complete full14/16/18 or P6 theorem is an imported premise. The restricted R4 bridge-label exclusion is discharged by the actual nonzero retained-label sets in the accepted core4/core24 proofs. |

## Exact residual interfaces

| Gate | Covered | Free |
|---|---:|---:|
'''
for r in c['residual_chain']:text+=f"| {r['gate']} | {r['covered']} | {r['free']} |\n"
text+=f'''
## Live evidence and acceptance boundary

The independent `FOURTEEN_HOLE_FULL_REVIEW_check.py --final` run rehashed
{c['all_live_bound_files_rehashed']} distinct bound files, traversed
{c['transitive_review_nodes']} review nodes and
{c['report_dependency_edges']} declared report edges, and checked
{c['additional_evidence_bindings_checked']} extra legacy evidence/source
bindings. There were no stale/missing bindings or nonaccepted theorem gates
inside this traversal. It checked all2048 endpoint normalizations, exact
consecutive streams, the20/5 orbit union, and the restricted bridge import.

The theorem dependency traversal covers `audited_input_hashes`,
`imported_dependency_hashes`, `checker_artifact_hashes`, and `formal_imports`.
It separately checks `audit_artifact_hashes`, `evidence_hashes`,
`accepted_import_source_bindings` and `report_sha256` as evidence bytes.
Historical partial source reports in these latter fields are not promoted
to theorem premises. Direct gate-manifest input/output hashes are expanded.
This is an explicit schema-limited check, not a claim that arbitrary nested
metadata or every historical manifest has been recursively interpreted.
The final P6 verifier may independently broaden that binding coverage.

Large already accepted censuses, rank matrices and connectivity certificates
were not rerun by this assembly checker. Their independent reviews are named
accepted inputs; no producer code was executed. The ledger, frozen proofs
and finite certificates were not changed by this audit.

Adversarial checks included an originally odd root; distances1/3/5; a covered
target becoming a crossing port; the special uv augmentation; a merely
sampled or maximum A domain; loss of original target mates under extension;
uncovered even30 in orbit1; original-only obstruction avoidance; omission
of whole stabilizer images; duplicated or reordered residual records; stale
predecessor imports; and interpreting Hall/search residuals as counterexamples.
The obligations above and accepted exact local audits close these cases.
No FATAL, CRITICAL, MAJOR or MINOR issue remains in the declared theorem scope.

Full fourteen holes is accepted under the stated provisional assurance.
Full P6 still needs separately accepted complete16/18 layers and the final
rooted-range assembly gate; this report does not grant those conclusions.
'''
(R/report).write_text(text,encoding='utf-8')
artifacts=['FOURTEEN_HOLE_FULL_REVIEW_check.py','FOURTEEN_HOLE_FULL_REVIEW_check.json','FOURTEEN_HOLE_FULL_REVIEW_emit.py']
d={'audit_skill':'proof-checker','verdict':'PASS',
 'reason_code':'all_complete_fourteen_hole_free_and_covered_obligations_closed_modulo_explicit_accepted_imports',
 'summary':'Complete fourteen-hole theorem PASS for every25-short-edge matching, free root and opposite-parity target including covered targets. Exact covered/free residual0. FullP6 not accepted by this gate.',
 'reviewer_agent_id':'/root/full14_audit_resume','reviewer_model':'gpt-6.1-sol','reviewer_reasoning':'high',
 'model_record_source':'Inherited user-selected reviewer route; model identity not independently measured.',
 'executor_family':'openai','reviewer_family':'openai','review_independence':'same-family','acceptance_status':'provisional',
 'generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'trace_path':report,'report_hash':sha(report),
 'audited_input_hashes':{proof:sha(proof),**c['direct_gates']},
 'imported_dependency_hashes':c['direct_gates'],
 'checker_artifact_hashes':{n:sha(n) for n in artifacts},
 'details':{'issues':[],'proof_obligations_closed':[f'A{i:02}' for i in range(1,15)],
  'canonical_statement':'For every matching M subset E(Q6) of25 short edges, every u outside V(M), and every v with parity(v)!=parity(u), there exists a Hamilton u-v path containing M.',
  'full_fourteen_hole_proved':True,'remaining_covered_target_geometries':0,'remaining_free_target_geometries':0,
  'full_P6_proved':False,'covered_targets_included':True,
  'uniform_over_every_realizing_original_short_matching':True,
  'every_realizing_original_short_matching_quantifier':True,
  'full_twelve_hole_predecessor_discharged':True,
  'exact_covered_residual_chain':[r['covered'] for r in c['residual_chain']],
  'exact_free_residual_chain':[232042,318,18,0],
  'final_orbit_sizes':[20,5],'final_orbit_union_equals_exact25':True,
  'all_ordered_opposite_parity_endpoint_normalizations_checked':2048,
  'all_live_bound_files_rehashed':c['all_live_bound_files_rehashed'],
  'transitive_review_nodes':c['transitive_review_nodes'],'report_dependency_edges':c['report_dependency_edges'],
  'dependency_DAG_acyclic':c['dependency_DAG_acyclic'],
  'theorem_dependency_fields':c['theorem_dependency_fields'],'binding_scope':c['binding_scope'],
  'restricted_R4_scope_discharged':True,'producer_code_executed':False,
  'large_imported_census_or_connectivity_checks_rerun':False,'Lean_verified':False,
  'frozen_proofs_certificates_or_ledgers_modified':False}}
(R/'FOURTEEN_HOLE_FULL_REVIEW.json').write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'verdict':'PASS','report_sha256':sha(report),'review_sha256':sha('FOURTEEN_HOLE_FULL_REVIEW.json')},indent=2))
