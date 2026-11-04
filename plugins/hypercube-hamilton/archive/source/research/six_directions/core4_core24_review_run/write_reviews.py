import json,hashlib,datetime
from pathlib import Path
R=Path(__file__).resolve().parent.parent
D=Path(__file__).resolve().parent
read=lambda n:json.loads((R/n).read_text(encoding='utf-8-sig'))
hashes=lambda ns:{n:'sha256:'+hashlib.sha256((R/n).read_bytes()).hexdigest() for n in sorted(set(ns))}
base=dict(audit_skill='proof-checker',verdict='PASS',reason_code='all_scoped_obligations_complete_modulo_explicit_imports',reviewer_model='gpt-6.1-sol',reviewer_reasoning='high',reviewer_task='/root/t15_core4_core24_complete_audit',executor_family='openai',reviewer_family='openai',review_independence='same-family',acceptance_status='provisional',model_override_source='Explicit user instruction via parent; overrides skill default',generated_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),full_T15_proved=False,full_eight_hole_proved=False,full_P6_proved=False)
common=['r4_joint_fourbridge_parent.cpp','verify_r4_joint_fourbridge_generic.cpp','R4_DOUBLE_BRIDGE_BLOCKING.md','R4_DOUBLE_BRIDGE_REVIEW.md','R4_DOUBLE_BRIDGE_REVIEW.json','r4_joint_blocking_check.json','q4_five_avoided_jpair_prepare.py','verify_q4_three_avoided.py','Q4_CORE_AND_A4_SPLIT.md','verify_q4_extension_certificates.py','q4_two_hole_3.bin','q4_two_hole_15.bin']
common+=list(read('R4_DOUBLE_BRIDGE_REVIEW.json')['audited_input_hashes'])
tables=json.loads((D/'review_36_tables.json').read_text())['rows']
rerun_sources=['core4_core24_review_run/review_supplement.py','core4_core24_review_run/review_supplement.json','core4_core24_review_run/review_36_tables.json','core4_core24_review_run/review_N14_4.json','core4_core24_review_run/review_python_reruns.json','core4_core24_review_run/review_cert_c2_reruns.json','core4_core24_review_run/review_c2_24_correct.json']
for core in (4,24):
 proof=f'T15_CORE{core}_FULL_CLOSURE.md';manifest=f'T15_CORE{core}_FULL_CLOSURE_VERIFICATION.json'
 files=common+[proof,manifest,f'verify_t15_core{core}_full_closure.py']+rerun_sources+[row['file'] for row in tables if row['core']==core]
 if core==4:
  files+=list(read(manifest)['input_sha256'])
  theorem=dict(ambient='K(V(Q5))',original_matching='arbitrary perfect matching on complement of exactly six holes',holes=[0,1,2,7,11,31],omitted=[1,2],conclusion='simple 30-cycle on Q5 minus omitted vertices, retaining all original edges and using only short new edges',transport='every marked cube-automorphic image')
  counts=[(2,62370,616,76839840,0),(4,51975,272,339292800,3045),(6,13860,32,319334400,8820),(8,1485,1,59875200,2520)]
  direct=1833510;extra=['verify_t15_core4_r4_c0_B.py','verify_t15_core4_r4_c2_types.cpp','t15_core4_r4_c2_types.cpp','t15_core4_r4_small_negative.txt','t15_core4_r4_c2_A_types.txt','t15_core4_r4_c2_B_types.txt']
  found=[dict(id='C4-01',category='NORMALIZATION_MISMATCH',original_severity='CRITICAL',status='REPAIRED_BY_AUTHOR_AND_REAUDITED',original_statement_sha256='565384a86b5d1576556feb06fe7f20f9511d8d8419ff128e58d8e376e1b738a1',note='Initial claim had 19 where construction and certificates require 31. Author corrected the statement and regenerated immutable manifest; accepted theorem uses 31 only.')]
 else:
  theorem=dict(ambient='K(V(Q5))',original_matching='arbitrary perfect matching on complement of exactly six holes',holes=[0,1,7,14,22,31],omitted=[1,7],normalized_holes=[0,2,7,13,21,31],normalized_omitted=[2,7],coordinate_destination_map=[1,0,2,3,4],conclusion='simple 30-cycle retaining every original edge, with all new edges short',transport='every marked cube-automorphic image')
  counts=[(2,62370,786,98045640,0),(4,51975,312,389188800,0),(6,13860,34,339292800,0),(8,1485,1,59875200,0)]
  direct=2650725;extra=['verify_t15_core24_c0_B.py','verify_t15_core24_c2_types.cpp','t15_core24_c2_types.cpp','t15_core24_route_negative.txt','t15_core24_c2_A_types.txt','t15_core24_c2_B_types.txt','t15_core24_route_c0_residual_inputs.bin','t15_core24_c0_residual.bin','verify_t15_core24_raw_residual.cpp','t15_core24_c0_B_verification.json','t15_core24_c0_residual_verification.json','t15_core24_c2_types_verification.json']
  found=[]
 files+=extra
 rows=[];fresh=[]
 for c,A,B,N,bad in counts:
  pre=f'r4_joint_fourbridge_core{core}_c{c}'
  report=pre+('_coverage_verification.json' if core==4 else '_verification.json')
  files+=[pre+'.json',report,pre+'_residual_inputs.bin',f'r4_joint_fourbridge_core{core}_B{c}.txt']
  p=D/f'review_fourbridge{core}_c{c}.json'
  if p.exists() and p.stat().st_size:
   rr=json.loads(p.read_text(encoding='utf-8-sig'));assert rr==dict(status='PASS',c=c,A=A,B=B,inputs=N,residual=bad)
   fresh.append(c);files.append(str(p.relative_to(R)).replace('\\','/'))
  rows.append(dict(c=c,A=A,B=B,inputs=N,residual=bad,fresh_full_rerun=c in fresh))
 files.append('core4_core24_review_run/review_full_fourbridge_reruns.json')
 files=[n for n in files if (R/n).is_file()]
 output=dict(base,theorem=theorem,summary=f'Complete core{core} marked theorem passes relative to N14_4 and fixed finite evidence; no remaining fatal/critical gap.',audited_input_hashes=hashes(files),trace_path=f'T15_CORE{core}_FULL_REVIEW.md',fourbridge=rows,total_fourbridge_inputs=sum(x[3] for x in counts),total_direct_certificates=direct,open_issues=[],repaired_issues=found,imports=['N14_4, whose 270270 finite certificates were freshly verified','restricted R4 inverse-blocking lemma with nonzero retained-hole bridges, current fixed hashes checked'],fresh_evidence=dict(N14_4_records=270270,five_avoided_records=17010,c0_original_inputs_rebuilt=1819125 if core==4 else 2650725,c2_A_inputs=62370,c2_B_inputs=945945,all_direct_certificates_verified=direct,fourbridge_crossing_classes=fresh),verification_note='review_cert_c2_reruns.json records one failed invocation using a nonexistent core24 negative filename; corrected rerun uses t15_core24_route_negative.txt and passes in review_c2_24_correct.json. This was a reviewer command error, not a proof repair.')
 (R/f'T15_CORE{core}_FULL_REVIEW.json').write_text(json.dumps(output,indent=2)+'\n')
 h=theorem['holes'];o=theorem['omitted']
 text=f'''# Complete T15 core{core}: fresh proof review

Verdict: **PASS**, relative to the stated imports. `review_independence: same-family`; `acceptance_status: provisional`. Reviewer route: GPT-6.1-sol / high, explicitly requested by caller, overriding the skill default. No production checker, main state, or dynamic coverage ledger was changed by this review.

Accepted theorem: for every arbitrary complete-graph matching on Q5 with exactly holes {h}, there is a simple cycle on Q5 minus {o}, containing every original matching edge and using only short new edges. The whole marked cube-automorphism orbit is included. This is one complete core, not complete T15, the eight-hole layer, or P6. Exact reviewed inputs and hashes are in the companion JSON.

## Proof obligations and dependency order

N14_4 plus marked Q4 tables imply the two-bridge construction. Restricted five-mode inverse blocking gives the exact B residual supersets for c=4,6,8 and empty residual sets for c=10,12. Independent small-spectrum enumeration covers c=2 outside its exact zero-spectrum B set. Four-bridge forests and their positive eleven-cycles cover each remaining full input, apart from explicitly listed direct positive residual certificates. At c=0, N14_4 gives the uniform A path; all exceptional B inputs times all A matchings have direct certificates. Every possible c is even and lies in {{0,2,4,6,8,10,12}}. No edge in this DAG imports a complete-core conclusion from a parent coverage ledger.

The N14_4 domain allows arbitrary same-parity and long original edges: translating the specified omitted hole to zero and permuting coordinates reduces the other hole to 3 or15. Fresh verification checks all 270270 positive certificates, distinct matching ranks, exact support, input-edge containment and shortness of all additional edges. The restricted R4 application uses retained bridge labels {{3,5,15}} for core4 or {{6,10,15}} for core24; every label is nonzero and avoids B holes 0,1. Thus the prior PASS_WITH_SCOPE_LIMITS hypothesis is discharged here. Fixed R4 input hashes and joint residual lists were rechecked; a missing blocker is never used as an impossibility certificate.

## Four bridges, isolated vertices and compression

Each of the18 bridge geometries has five marked omissions in B, namely 1 plus its four distinct bridge labels; zero remains the sole retained free vertex. For each table the full945 mate arrays have precisely the six required holes. Every positive record is a simple eleven-cycle on exactly the claimed support, includes the input matching, and has only short other edges. Fresh checking also exhausts degree completions for negative records, although construction soundness needs only positives. The36 tables across these two cores contain34020 records.

The A short graph has degree2 at the remaining retained hole u, degree0 at the omitted vertex and the two extra bridge labels, and degree1 elsewhere. Enumerating both neighbors of u followed by every complementary short perfect matching exhausts this degree domain. Rejecting repeated original edges and cyclic components leaves paths. External endpoints are **incidences indexed by position**, not a set of vertex labels. An extra bridge vertex that is an original A port has two distinct incidences at its isolated A vertex, paired with each other. That zero-length A path retains its vertex during expansion. In core24, omission3 permits port0: generation starts from the full mask minus {{3,6,10,15}}, and the c2 encoding includes nibble0.

After mapping all original port incidences through the actual crossing bijection, the graph includes the four short bridges and every B matching edge. The separate traversal checker enforces degree at most2, rejects duplicate edges, and rejects every component whose edge count reaches its vertex count. This catches both ordinary closed components and a doubled original-crossing/bridge edge. The surviving quotient has exactly ten terminal covered B vertices, paired into five paths, plus isolated retained B0. Eleven-cycle expansion restores all fifteen A vertices and four B bridge mirrors, hence 11+15+4=30 distinct vertices. All original edges are restored. Four-bridge spectra introduce no artificial required edges; the two-bridge auxiliary edges are all deleted or replaced in the audited five modes. No long auxiliary edge survives as an unrequired new edge.

## Full input domains and finite evidence

For each c, A inputs number binomial(12,c) times (11-c)!!; B is the exact validated residual list, and all c! sorted-port permutations enumerate every crossing bijection. The independent checker rebuilds the A spectra using adjacency traversal rather than the producer's union-find, and compares every uncovered26-byte full input with the saved stream, rejecting early EOF and trailing data. B files were separately checked for valid disjoint edges, exact support, uniqueness, equality with joint blocker residuals or the complete zero-spectrum set.

| c | A | B | full inputs | residual direct certificates |
|---:|---:|---:|---:|---:|
'''
 for c,A,B,N,bad in counts:text+=f'|{c}|{A}|{B}|{N}|{bad}|\n'
 text+=f'''
Total four-bridge domain: {sum(x[3] for x in counts)}. Fresh full traversal reruns completed at c={fresh}; remaining classes use the fixed complete independent traversal outputs whose sources, exact domains, streams and hashes were reviewed. Every one of the {direct} direct certificates was freshly rerun after recompiling the independent C++ verifier in the isolated directory. It checks the exact input bytes, matching validity, thirty distinct target vertices, all thirteen required edges, closing adjacency and shortness of every other edge.

At c=0 the independent suppression checker freshly rebuilds every exceptional B matching and every A matching, then compares the **entire** saved input byte stream. At c=2 all62370 A and945945 B input signatures were freshly recomputed with DSU components; input uniqueness and cardinality give full matching-domain coverage, and both port orientations are checked. The negative text files were independently compared, family by family, with the actual transported exact Q4 negative tables. Thus neither c=0 nor c=2 relies merely on a residual count or unsuccessful search.

Counterexample checks cover an occupied bridge mirror, paired mirrors, duplicate crossings/bridges, a closed path component disjoint from quotient terminals, isolated Aport/bridge coincidence, Aport0 in core24, reversed c=2 orientations and both c=10,12 boundaries. The degree argument and audited mode hypotheses settle these cases; no new counterexample or open fatal/critical issue remains. There are no asymptotic, limit-interchange or measure-theoretic obligations.

## Scope and reproducibility

Fresh evidence and exact commands/results are preserved in `core4_core24_review_run/`. All reruns used isolated copies; the accepted fixed source files are hashed in the review JSON. Dynamic remaining-geometry ledgers are excluded. The core24 manifest by itself does not freeze all proof inputs, so this review's explicit hash dictionary supplies that missing provenance; it is not treated as a mathematical gap in the construction.

One review invocation used a nonexistent core24 negative filename and failed its spectrum assertion; the corrected invocation with `t15_core24_route_negative.txt` passed. This is recorded transparently in the isolated logs. Complete proof acceptance remains same-family/provisional; N14 and the prior restricted semantic import retain their explicit scope. No main-state integration is performed by this audit.
'''
 if core==4:text+='\nThe first received core4 claim incorrectly ended its hole list at19. The construction and all certificates use31. This was reported as C4-01, the author corrected the theorem and regenerated the manifest, and the revised file/hash were reaudited. Only the corrected31 theorem is accepted.\n'
 (R/f'T15_CORE{core}_FULL_REVIEW.md').write_text(text)
# Standalone immutable eleven-geometry artifact, also included in consequence hashes.
supp=json.loads((D/'review_supplement.json').read_text())
closed=supp['closed_normalized_geometries'];assert len(closed)==11
artifact='EIGHT_EP0_CORE4_CLOSED_GEOMETRIES.json'
(R/artifact).write_text(json.dumps(dict(closed_geometries=closed,count=11,scope='two specified target-preserving normalized orbits'),indent=2)+'\n')
cons_files=['ep0_core4_projection_check.py','ep0_core4_projection_check.json','EIGHT_EP0_FAST_ROUTE.md','EIGHT_NEW_PARTIAL_BRANCHES_REVIEW.md','EIGHT_NEW_PARTIAL_BRANCHES_REVIEW.json','EIGHT_DOUBLE_BRIDGE_REVIEW.md','EIGHT_DOUBLE_BRIDGE_REVIEW.json','EIGHT_HOLE_COVERED_NEXT_DRAFT.md','GENERAL_NEAR_PERFECT.md','T15_CORE4_FULL_CLOSURE.md','T15_CORE4_FULL_CLOSURE_VERIFICATION.json','T15_CORE4_FULL_REVIEW.md','T15_CORE4_FULL_REVIEW.json','t15_analytic_geometry.json',artifact,'core4_core24_review_run/review_supplement.py','core4_core24_review_run/review_supplement.json']
out=dict(base,theorem='For every realizing short matching in each of the eleven listed normalized Q6 geometries, a Hamilton path exists from root0 to its covered odd target, preserving the original matching and using short additional edges.',summary='The complete marked core4 theorem closes the required T15 instance for every EP0 witness option; precisely these11 of50 exceptional normalized geometries close by the audited transfer.',closed_geometries=closed,closed_geometry_count=11,remaining_exceptional_geometries_unproved=39,remaining_exceptional_orbits_unproved=5,projection_options_checked=18,audited_input_hashes=hashes(cons_files),trace_path='EIGHT_EP0_CORE4_CONSEQUENCES_REVIEW.md',imports=['N10 at the already audited complete-graph auxiliary matching scope','the audited two-orbit EP0 lemma','the audited conditional double-bridge transfer','the complete core4 theorem accepted in this review'],open_issues=[],projection_status_note='The input projection JSON core4_currently_proved=false is an old descriptive status field, not a proof premise; its geometric rows are checked independently here.')
(R/'EIGHT_EP0_CORE4_CONSEQUENCES_REVIEW.json').write_text(json.dumps(out,indent=2)+'\n')
text='''# EP0 plus complete core4: exact eleven-geometry consequences

Verdict: **PASS**, relative to N10 and the explicitly audited imports. `review_independence: same-family`; `acceptance_status: provisional`.

For every short matching realizing any of the eleven normalized geometries listed in the JSON, a Hamilton0-to-target path preserving that matching exists. The scope consists of the target1 orbit with representative Z={3,5,9}, W={14,31,47,62}, of size10, and the target7 orbit with Z={15,23,39}, W={56,59,61,62}, of size1. Each has root0. The exact list is saved in `EIGHT_EP0_CORE4_CLOSED_GEOMETRIES.json` and included in the fixed proof hashes.

The prior EP0 proof chooses its cut after seeing the matching edge at covered vertex15 or63. Its artificial z1z2 edge is permitted by N10's complete-graph scope; acyclicity of the N10 Hamilton path forces an additional short edge qs into the mirrored odd-hole set. Thus the existential cut and path witness are available for every realizing matching, with no assumption of a prescribed optional edge theorem. For the displayed cuts root0 is in A and q differs from the target. The existing double-bridge transfer deletes its auxiliary matching and qs, restores the original crossings, and exposes exactly the two mirrored even holes Y. The B T15 input has retained free root equal to the third original even hole a, retains W except the consumed odd hole t, and must omit exactly Y. Its matching may contain long auxiliary edges, which the now-complete arbitrary-matching core4 theorem permits.

The projection code translates by a, then deletes the cut bit. This maps a to0; its avoided pair is proj(z XOR cutbit) for the two A even holes, and its retained included holes are0 plus proj(W minus {t}). A fresh independent checker enumerates all18 permitted choices qs across both representatives and directly finds a coordinate permutation carrying the **concrete marked theorem** avoided={1,2}, retained={0,7,11,31} to each resulting pair/set. It does not infer applicability merely from the label core=4 or an unmarked hole-set isomorphism. Every possible EP0 witness therefore has a fully proved corresponding T15 instance. Applying the audited transfer yields the path conclusion for every realizing matching.

The checker separately enumerates target-preserving Q6 coordinate permutations, obtaining exactly10 and1 distinct geometries, with no overlap, and records all eleven. Its hashes cover the EP0 proof, transfer, projection checker, concrete core4 proof/review and exact list artifact. The projection JSON's historical `core4_currently_proved=false` flag is descriptive and is not used as a premise. No dynamic remaining-geometry ledger enters the proof.

The other five exceptional orbits, containing39 normalized geometries, remain unproved by this route. The prior avoid-sufficient-edge witnesses do not refute EP0; they show that this particular triangle rule does not cover those orbits. This consequence does not establish all eight-hole configurations, complete T15, or P6. Interpreting the seven orbit union as all50 exceptions retains the previously declared external census assumption. No main-state file is changed here.
'''
(R/'EIGHT_EP0_CORE4_CONSEQUENCES_REVIEW.md').write_text(text)
print('Three review pairs and exact eleven-geometry artifact written')
