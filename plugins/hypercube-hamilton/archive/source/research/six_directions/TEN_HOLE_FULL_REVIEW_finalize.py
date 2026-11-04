"""Emit final verdict only after final independent T17 theorem acceptance."""
from pathlib import Path
import hashlib,json,re
from datetime import datetime,timezone
P=Path(__file__).resolve().parent
def raw(n):return (P/n).read_bytes()
def load(n):return json.loads(raw(n))
def sha(n):return hashlib.sha256(raw(n)).hexdigest()
c=load('TEN_HOLE_FULL_REVIEW_check.json')
tname='Q5_T17_RANK_BATCH_REVIEW.json';t=load(tname)
assert t['verdict']=='PASS' and t['review_independence']=='same-family'
assert 'ROOT_NOT_OB' in raw('Q5_T17_RANK_BATCH_REVIEW.md').decode().upper() or 'root' in raw('Q5_T17_RANK_BATCH_REVIEW.md').decode().lower()
bound={}
for group in t.values():
 if not isinstance(group,dict):continue
 for n,h in group.items():
  if not isinstance(h,str) or not re.fullmatch('(sha256:)?[0-9a-f]{64}',h):continue
  if not (P/n).exists():
   assert '.' not in n,('missing T17 binding',n)
   continue
  assert sha(n)==h.removeprefix('sha256:'),('stale T17 binding',n)
  bound[n]=sha(n)
for n,d in c['imports'].items():
 assert sha(n)==d['sha256'],('stale imported review',n)
 for f,h in c['import_source_and_evidence_hashes'][n].items():assert sha(f)==h
for v in [1,7,31]:
 n=f'Q5_T17_RANK_BATCH_REVIEW_remaining_v{v}.bin'
 assert sha(n)==c['exact_T17_residual_hashes'][str(v)],('T17 exact set mismatch',v)
 assert n in bound,('T17 residual not bound',v)
assert c['remaining']==0 and c['actual_route_witnesses']==4096
md='''# Final independent full ten-hole Q6 proof review

2026-11-01. Fresh reviewer `/root/ten_hole_final_assembly_review`, explicit
user-selected GPT-6.1-sol / high, overriding the ARIS proof-checker defaults.
Assurance is **same-family / provisional**, relative to the named published
and previously accepted mathematical imports.

**PASS for the complete original ten-hole theorem.** For every matching M of
27 short edges of Q6, every uncovered vertex u, and every vertex v of parity
opposite to u, there exists a Hamilton u--v path containing all of M. The
target can be covered or free. Every new physical edge is short. There are
zero remaining free-target or covered-target geometries in this scope.
The complete 12/14/16/18-hole layers and full P6 remain **OPEN**.

## Frozen submission and import boundary

The theorem-bearing submission is `TEN_HOLE_FULL_CLOSURE.md`. Its statements
that final review is pending are gate metadata, not an added mathematical
assumption: this report discharges that gate. The final T17 review was read
and source/evidence hashes checked before this verdict was emitted. No
candidate-only T17 rank output is treated as an accepted theorem.

Imports are the full eight-hole theorem, full ten-hole both-free theorem,
uniform transfer, the complete covered-geometry reduction, full-A8
consequences, marked-T63 split application, full-Q5 endpoint application,
the T26 rank batch, the T15 rank batch, and the final T17 rank batch with its
root-not-obstruction transfer. Their exact scopes supply arbitrary compressed
matching quantifiers. Full unrestricted T15/T17/T26/T63 is unnecessary.
The optional seven-orbit T63 rank batch is not used to close the final union.

Nine earlier final review reports were checked PASS and all 1810 directly
declared file bindings (counted per report) were rehashed; the final T17
report, its declared sources, evidence and exact residuals were checked
separately. The JSON and independent check JSON record the actual file/hash
dictionaries. Large imported finite matching certificates and old whole-domain
censuses were not rerun. This report imports those accepted theorems and
their exact exhaustiveness statements; it does not claim a fresh recreation
of their billions of connectivity bits.

## Quantifiers, normalization and proof-obligation ledger

Q6 has vertices 0,...,63, parity equal to bit-count modulo two, and short
edges of Hamming distance one. A Hamilton path uses all 64 vertices exactly
once. Z and W denote the normalized four nonroot even holes and five odd
holes. A,B are the actual coordinate faces, with v in A. Marked omissions
are transported together with minority, majority, matching and obstruction
under one common cube automorphism.

| ID | Obligation and discharge |
|---|---|
| F01 | Every short matching edge covers one vertex per parity. Thus 27 edges leave exactly five holes of each parity. Translation by the original u makes u=0, possibly reversing parity globally, while preserving shortness, matching containment and Hamilton paths. |
| F02 | If v is free, the accepted `TEN_HOLE_FREE_REVIEW` theorem has exactly these universal matching and endpoint quantifiers. Its adjacent-hole proof includes the special uv augmentation edge and uses covered targets in the full eight-hole import. No free-target configuration is discarded. |
| F03 | If v is covered, translation makes v odd; coordinate permutations take it to 1,7 or31 according to its weight 1,3 or5. Inverting the automorphism preserves the original prescribed endpoint, so all opposite targets are represented, rather than three fixed original targets. |
| F04 | A short edge joining Z to W joins two free vertices distinct from u and v. Add it to obtain a 28-edge matching with u still free and v covered. Full eight-hole P6 gives the same endpoint path through the enlarged matching, hence through M. |
| F05 | The remaining covered domain requires only Z--W independence, not root--W independence. It excludes v from holes and excludes zero from Z. The accepted 145248180-domain census includes every such marked geometry without matching-realizability or direction-use filters. This only enlarges the domain relative to realizable M. |
| F06 | The accepted exact filtering chain leaves 91225, then54222, then41306, then41236, then4096 records. The endpoint stage combines its70 additions with the already accepted12916 T63 split additions by exact sets. Current source and residual hash bindings were checked. |
| F07 | Every sufficient cut theorem handles the empty original crossing matching using the established five-direction endpoint theorem. Positive crossing transfers use arbitrary complete-graph local matching statements, so artificial long or same-parity completion and compressed edges satisfy the import hypotheses. |
| F08 | The actual T15 rows (3,2)/(1,4) use two free sources and their two distinct mirrors as omissions. Root-mirror sources are excluded. The A completion has two holes per parity and the B local statement holds for every realizing compressed matching. Independently reconstructed marked membership gives exactly2346 positive records and the accepted exact1750-record complement. |
| F09 | The actual T17 rows (3,1)/(0,4) use three free sources and precisely their three mirrors as omissions, yielding one minority and seven majority holes. The A completion has one hole per parity. All2598 unforced positives use accepted rank2048 theorems with no obstruction restriction. |
| F10 | The other1036 positives use accepted conditional rank1024 T17 theorems only on an actual projection whose obstruction pair excludes u. The new transfer makes the compressed matching avoid that pair; absence from the original short matching alone is not used. |
| F11 | For the safe transfer, obstruction endpoints have the parity of bridge mirrors; their pendant original mates have opposite parity. Suppression therefore cannot create the obstruction except by directly pairing its two original crossing ports. If both are ports, prescribe the edge between their A partners in D. The selected root is outside that prescribed edge by free-source or crossing-port parity. The arbitrary endpoint import permits this D. |
| F12 | With u in A, the tagged A path is a cycle with at least two deleted D gaps, so endpoints of the prescribed deleted edge cannot lie in one remaining component. With u in B, deletion separates them in a path and the tag adds only a distinct B-root leaf. Target-as-port and isolated target components obey the same argument. Thus the obstruction is absent from the actual final matching, discharging the sole conditional local hypothesis. |
| F13 | Independent exact set calculation gives T17 residual462, exactly the no-T17-cut records, and all462 are in T15positive. No record is credited using totals alone. Each of4096 inputs has a saved valid actual cut/source/marked-orbit witness selecting one accepted route. |
| F14 | Each local theorem is universal over all arbitrary matchings on the specified complement. Consequently the geometry route works for every original short matching realizing that geometry, even though D and the Hamilton witness depend on M. Expansion restores all original edges and vertices, removes artificial D/compressed edges and deletes only the final tag. Every surviving new edge is short. |
| F15 | Free/covered targets, augmentation/independence, the earlier exact positive classes and the final4096 union exhaust the original domain. Undoing normalization proves precisely the original for-every-M, for-every-u, for-every-opposite-v, exists-path statement. No narrowed target or matching quantifier remains. |

The dependency DAG is published/Q4/Q5 local inputs -> accepted local endpoint
and marked-cycle theorems -> uniform cut transfer and its safe conditional
refinement -> exact Q6 covered geometry coverage. Separately the accepted
eight-hole theorem supplies augmentation and the accepted both-free branch
supplies free targets. These feed the present assembly, with no reverse
dependency on it or full P6. There are no limiting interchanges, asymptotic
constants, probabilities or induction on any unproved higher-hole result.

## New independent exact calculation

`TEN_HOLE_FULL_REVIEW_check.py` imports no producer module or checker and
executes no producer search. It constructs the full marked registry images
from coordinate permutations and translations. For each frozen nine-byte
record it validates sorted labels, parity, target/root exclusion and Z--W
independence, then reconstructs every relevant actual cut and every eligible
two- or three-source subset. It transports all marked sets under one
automorphism, and lifts each forced obstruction to the original B face to
check root exclusion. Separate per-record exact sets, not a sum of overlapping
totals, establish the following partition.

| v | Accepted inputs | Unforced T17 | Safe forced T17 only | T17 remainder covered by T15 | T15 total positive | Final remainder |
|---:|---:|---:|---:|---:|---:|---:|
|1|910|570|220|120|480|0|
|7|1476|918|396|162|846|0|
|31|1710|1110|420|180|1020|0|
|Total|4096|2598|1036|462|2346|0|

The T15/T17 overlaps are360/684/840, total1884. Thus T17positive3634
union T15positive2346 contains exactly4096 records. Its complement is empty.
The independent T15 complement equals the accepted reviewer complement as
sets; the independently retained T17 residual bytes match all three final
accepted T17 reviewer binaries and their hashes. All462 T17 residual records
are included in T15positive; no-T17-cut is a geometric diagnostic, not a
matching nonexistence statement. The4096 selected route witnesses are in
`TEN_HOLE_FULL_REVIEW_witnesses.json`.

## Adversarial checks and limits

Attempted failure cases include parity reversal; a covered target at distance1;
root--W adjacency; an augmented edge covering the root; confusing a complete
matching theorem with a bipartite-only theorem; independently moving omissions;
root in the forced obstruction; obstruction introduced only after compression;
a target crossing port incident to the prescribed D edge; a tagged cycle with
only one deleted gap; and double-counting T15/T17 overlaps. The normalization,
source exclusions, full imported matching quantifiers, safe-completion proof,
and fresh exact calculations discharge these attempts. No unresolved FATAL,
CRITICAL, MAJOR or MINOR mathematical issue remains in the declared scope.

This is a computer-assisted proof accepted at same-family/provisional
assurance modulo explicit published and previously audited imports. It is
not a formal or cross-family verification. Full12/14/16/18-hole layers,
unrestricted local T families, and full P6 remain outside this verdict.
No producer, frozen source, main state or claim ledger was modified.
'''
(P/'TEN_HOLE_FULL_REVIEW.md').write_text(md,encoding='utf-8')
inputs=['TEN_HOLE_FULL_CLOSURE.md','TEN_HOLE_FREE_CLOSURE.md','EIGHT_HOLE_FULL_CLOSURE.md',
 'HIGHER_HOLE_UNIFIED_TRANSFER.md','Q5_T17_RANK_BATCH_PROOF.md','Q5_T17_RANK_ROOT_NOT_OB_TRANSFER.md',
 'Q5_T15_RANK_BATCH_PROOF.md','Q5_T15_RANK_batch_summary.json',
 'Q5_T17_RANK_batch_summary.json','Q5_T17_RANK_forced_summary.json']
inputs+=list(c['imports'])+[n.replace('.json','.md') for n in c['imports']]+[tname,'Q5_T17_RANK_BATCH_REVIEW.md']
inputs+=list(c['source_hashes'])
evidence=['TEN_HOLE_FULL_REVIEW.md','TEN_HOLE_FULL_REVIEW_check.py','TEN_HOLE_FULL_REVIEW_check.json',
 'TEN_HOLE_FULL_REVIEW_witnesses.json','TEN_HOLE_FULL_REVIEW_finalize.py']
j=dict(audit_skill='proof-checker',verdict='PASS',reason_code='all_original_ten_hole_obligations_complete_modulo_explicit_accepted_imports',
 summary='Every 27-short-edge Q6 matching, every free root and every opposite-parity target (covered or free) has a Hamilton extension; exact final4096 union has remainder0. Higher complete layers and P6 remain OPEN.',
 reviewer_agent_id='/root/ten_hole_final_assembly_review',reviewer_model='gpt-6.1-sol',reviewer_reasoning='high',
 model_override_source='Explicit user-selected model/effort route relayed by parent overrides ARIS defaults',
 executor_family='openai',reviewer_family='openai',review_independence='same-family',acceptance_status='provisional',
 generated_at=datetime.now(timezone.utc).isoformat(),trace_path='TEN_HOLE_FULL_REVIEW.md',
 audited_input_hashes={n:sha(n) for n in inputs},evidence={n:sha(n) for n in evidence},
 accepted_import_source_and_evidence_hashes=c['import_source_and_evidence_hashes']|{tname:bound},
 details=dict(issues=[],theorems_audited=1,proof_obligations_closed=[f'F{i:02}' for i in range(1,16)],
 canonical_statement='For every M subset E(Q6) a matching of27 short edges, for every u not in V(M), and every v with parity(v)!=parity(u), there exists a Hamilton u-v path P in Q6 with M subset E(P).',
 full_ten_hole_proved=True,remaining_covered_target_geometries=0,remaining_free_target_geometries=0,
 full_P6_proved=False,full_higher_layers_proved=False,open_complete_hole_levels=[12,14,16,18],
 uniform_over_every_realizing_short_matching=True,covered_targets_included=True,
 final_exact_partition=c['rows'],T15_T17_overlap=1884,T17_remaining_all_in_T15=True,
 actual_route_witnesses=4096,earlier_complete_covered_domain=145248180,
 earlier_census_and_large_matching_certificates_rerun=False,earlier_final_reviews_rehashed=True,
 final_T17_review_rehashed=True,exact_final_T17_residual_bytes_match=True,
 dependency_DAG_acyclic=True,production_or_main_state_modified=False))
(P/'TEN_HOLE_FULL_REVIEW.json').write_text(json.dumps(j,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'verdict':j['verdict'],'proof_sha256':sha('TEN_HOLE_FULL_CLOSURE.md'),
 'review_sha256':sha('TEN_HOLE_FULL_REVIEW.json'),'T17_review_sha256':sha(tname),'T17_bindings':len(bound)}))
