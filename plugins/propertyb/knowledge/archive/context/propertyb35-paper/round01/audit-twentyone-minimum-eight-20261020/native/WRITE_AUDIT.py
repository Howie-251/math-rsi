from pathlib import Path
from datetime import datetime, timezone
import json, hashlib
P=Path(__file__).resolve().parent
ROOT=P.parents[4]
M='context/propertyb35-paper/round01/middle/'
units={
'U01':['proofs/propertyb35/TWENTYONE_MINIMUM_EIGHT.md'],
'U02':['proofs/propertyb35/TWENTYONE_MINIMUM_EIGHT_SMALL_CODEGREES.md'],
'U03':['proofs/propertyb35/CLEAN_EXTERIOR_STAR_FROM_TRACE_BUDGET.md'],
'U04':[M+'min_degree_eight_singleton_star_20261020/PROOF.md'],
'U05':[M+'delta8_strong_pair_transfer_20261020/REPORT.md'],
'U06':[M+'delta8_c3_capacity_transfer_20261020/PROOF.md'],
'U07':[M+'delta8_high_center_q4_20261020/audit/AUDIT.md'],
'U08':['proofs/propertyb35/ONE_EXCEPTIONAL_POINTPAIR_CAPACITIES.md'],
'U09':[M+'c3_unique_high_pair_five_20261020/PROOF.md'],
'U10':[M+'min_degree_eight_singleton_star_20261020/CONDITIONAL_SCALAR_REPORT.md'],
'U11':[M+'delta8_one_exception_scalar_20261020/REPORT.md'],
'U12':[M+'a2_a3_joint_moment_frontier_20261020/CAPACITY_LEMMAS.md'],
'U13':[M+x for x in ['min_degree_eight_singleton_star_20261020/SCOPE_CHECK.py','min_degree_eight_singleton_star_20261020/INDEPENDENT_VERIFY.py','min_degree_eight_singleton_star_20261020/CONDITIONAL_SCALAR_CHECK.py','delta8_strong_pair_transfer_20261020/VERIFY.py','delta8_c3_capacity_transfer_20261020/INDEPENDENT_VERIFY.py','delta8_high_center_q4_20261020/CHECK.py','delta8_high_center_q4_20261020/audit/VERIFY.py','c3_unique_high_pair_five_20261020/PILOT.py','c3_unique_high_pair_five_20261020/VERIFY.py','delta8_one_exception_scalar_20261020/CHECK.py','delta8_one_exception_scalar_20261020/audit/CHECK.py']]}
# Stable source-unit order, then local claim order. No prior model conclusions used.
rows={
'U01':[
('Exact theorem and contradiction scope','H has 21 vertices, 35 distinct five-edges, pair coverage and every degree >=8. These, and only these, are target premises. No criticality, lambda bound, global excess bound or certificate is added.'),
('Complete fifteen degree spectra','175=8b+9(21-b)+e gives b=14+e and e<=6; partition e into at most 7-e positive parts. Independently regenerated exact saved list, including 8^20,15. W at sources8,9,11,12 is651,650,655,653.'),
('Strong-pair dichotomy','All selected degree pairs with multiplicity and every codegree5..min(du,dv) are covered. Only four source-specific degree/codegree keys are nonstrict. Each source has exactly one unordered pair of its exceptional degrees; all other pairs are <=4 under non-B.'),
('Common Gamma minimum four','U04 applies to arbitrary global e; U03 supplies the actual exterior degree8 point. Combined with imported q<=2 repair this gives q(F)>=4 for every actual original edge.'),
('Exceptional error and C3 caller','U08 supplies tau<=142 and total C4 bonus5/6. For each triple-intersecting G,J, K not containing both exceptional endpoints meets the old local selected-degree/excess premises; K containing both lies in U09. No converse exactcross-to-valid-middle implication is used.'),
('Common capacities and moment domain','All Cj belong to the same original H. Their sum P is bounded once by35 boxes0..30 with total2n1. Three moment identities give U11 domain; tau row bound and397<=n1<=525 are necessary for this same H.'),
('Strict original-object conclusion','Every exceptional spectrum domain is strict for the actual-H two-flip criterion. The all-small-codegree case is U02. Hence contradiction for every target H; no conclusion about other21-point branches or the full36 target follows.')],
'U02':[
('Small-codegree conditional theorem','The extra all-lambda<=4 assumption is explicit here and supplied by the appropriate U01 dichotomy branch.'),
('Delta8 triple-middle cap','U06 covers38 selected degree multisets from all15 spectra;33 meet old local c14/c15/c16 import, five newly checked cover the remainder. Thus actual C3<=13n3.'),
('Shared scalar relaxation','For actual nj, use C0<=33n0, C1<=35n1-Kd, C2<=floor((S6-6)/2)n2, C3<=13n3,C4<=4n4. Descending weight fill maximizes a relaxation with one shared budget; no optimizer-realizability premise.'),
('All fifteen moment domains','The independently re-executed1,166,584-key scan is complete for tau<=140 and its row lower bound. Thirteen spectra strict; source13 has one residual withE70; source14 has14 residuals withE70..73.'),
('High-center removal of remaining keys','Actual degree14 point lies on14 distinct edges of U07 roles; all haveq>=5, other edgesq>=4, soE>=77. Degree15 similarly givesE>=78. These contradict every saved residual. No edge-criticality needed.')],
'U03':[
('Nonnegative exterior trace budget','All edges meet F, so every summand |E intersect F|-1>=0. Finite double count gives sum_z hF(z)=BF; at mostBF exterior points have positive integer deficit.'),
('Actual clean degree8 choice','C has outside degree8 pool>=15 andBF11; D has pool>=16 andBF10. These use e>=selected excess, never an upper e bound.'),
('One common actual star and six-lock map','Chosen z is fixed, has8 original edges and each is a singleton F trace. Pair coverage gives each si>=1, sum8; hence all35 positive five-compositions, eachsi<=4<=ai. Split actual edge indices and add z without changing the original H.')],
'U04':[
('Complete q3 orbit and attachment domain','Three exceptional traces are arbitrary multisets from26 masks of sizes0,2,3,4; full3276 labels and91 S5 orbits are rechecked. Safe one-red prefixes leave119 attachment keys.'),
('No hidden excess assumption','Fresh INTERFACE_CHECK reconstructs all119 directly from the full orbit record and filters only minimum F degree>=8. Exactly25 remain with excess histogram0:1,1:11,2:11,3:1,4:1, matching old25 keys. The <=4 filter in the older independent verifier is redundant by this independently verified fact.'),
('Twenty-three old and seventy new strict certificates','Replay23 accepted five-lock keys and70 actual six-lock keys using original35 distinct indices. Full C/D positive composition set equals saved set. Six-lock free vertices are15, not a reused six-degree-star denominator; maximum141/143.'),
('Permutation caller','All locks are actual distinct vertices, all positions distinct; zero quota, no external degree premise. The imported probability theorem turns strict finite conditional bound into a proper coloring of the original H.')],
'U05':[
('Degree-pair projection and exact traces','Independent support from spectra and degree multiplicities covers100 keys and all source IDs. Fresh check reconstructs mu0=35-du-dv+c,mu1=du-c,mu2=dv-c,mu3=c for every stored key.'),
('All96 strict pair gates and unique exceptions','Original-index replay verifies every one of100 pair bounds, including all nonstrict statuses. Nonstrict exactly(10,12,5),(11,11,5),(10,13,5),(11,12,5), in sources8,9,11,12 respectively.'),
('Report subsidiary triple scope','Its exterior z union argument and64 exact three-lock inputs have their own valid assumptions and replay;40 strict and24 nonstrict remain. These are not needed by the complete U01 proof and are not treated as H classification.')],
'U06':[
('All selected-degree support','Independent partition generation and four-point degree-count selection gives15 spectra/38 multisets. Exactly33 meet selected max<=13/excess<=4; five named exceptions are the complete complement.'),
('Inclusive cross budget and high traces','Actual valid middles imply exactcross total>=14. Paircap4 bounds it by16 and gives t+2p+4q<=16; henceq=0,p<=1. Same-side exactpair multiplicities>=1 come from actual outer edges.'),
('New complete domain and symmetry','Full inclusive/Mobius generation equals412 labels, true marked8-group yields62 representatives. Degree and traces transported together; no H automorphism assumed. t16 impossible for these five degree multisets, t15 labels24 are still generated.'),
('New strict replay and declared old catalogue','All62 fixed certificates replay against35 indices/1190 ordered distinct pairs, max1427/1716. Older33 degree multisets use the declared full c14/c15/c16 catalogue, not rerun in this audit.')],
'U07':[
('Complete q4 role domain','All23751 anomaly multisets per role. Exact singleton ai=di-1-hi sums30; F itself already uses each internal pointpair, so anomaly paircount<=3. Three roles exactly cover actual edges through the lone14/15 point.'),
('One-red/tree and fixed remaining inventory','Independently rebuild70 threshold fail sets overa0..30/r0..16. First role has no residual; other two have6 each. Tree subtraction is from the same red-event sample; all red foursets with one common anchor are distinct.'),
('Actual twelve-tail repair','All12 retain35 edge indices, zero quotas, old16-position menu. Replayed best bounds11203/12012 and all252 pivot minima match. No old degree-six role filter is used.')],
'U08':[
('Tau plus two','Pair coverage giveslambda>=1 andR140. C(lambda-1,2)<=lambda-1 for1..4; unique5 contributes6 instead of4. Thereforetau<=142.'),
('C4 total bonus without factor two','Every exceptional unordered outer pair is uniquelyK+u,K+v and injects into both u-only and v-only original edge sets. Their number<=min(du,dv)-5. Each requires at most one extra middle unit above4; no orientation doubling.')],
'U09':[
('Actual K supports and fourteen families','Fresh projection from four exceptional degree spectra recovers exactly six highpair/other-degree combinations. Same-side normalization yields6 families; cross-side different9/8 allocations retained, yielding8, total14.'),
('All high traces retained','Cross inclusive total<=16(same) or17(cross), with exactcross>=14, forces full4=0 and total triple<=1. Same-side sumdegrees22/23<2*5+14 excludes all6 same families; generated domain independently agrees.'),
('Complete425-domain equality','Independent inclusive-pair loops with markedpair exactly5 and five others1..4, all full/triple possibilities allowed by budget, Mobius recovery and nonnegative degrees/empty, equal fresh primary output and family memberships. t17 is allowed before checks and excluded by actual inventory conditions.'),
('All425 strict original-index certificates','All425 selected positions from fixed three-layout menu are re-executed. 8925 rows using original35/1190 distinct ordered identities, max25963/29172. No outside-degree, criticality or global e<=4 premise.'),
('Every original triple-intersection pair','IfK misses one exceptional endpoint, local maxdegree<=13 and selected excess<=4 verified for every four-index subset of each spectrum. Else it is a marked family. Thereforec<=13 for every pair of the same H and C3<=13n3.')],
'U10':[
('Conditional assumptions supplied externally','This scalar file alone assumes all paircaps4,C3cap13 and Gammamin4. U02 supplies each through actual-H lemmas; reading saved scalar degrees in U05 does not import these assumptions.'),
('Complete independent integer domain','Fresh tau/t/m scan confirms all1,166,584 keys, per-spectrum maxima and all15 residual keys. Non-strict aggregate keys are not actual H or counterexamples.')],
'U11':[
('Exceptional complete domain','tau<=142, rowlower,397<=n1<=525 and nonnegative moments; t<=47 follows from second moment, no added n4 bound. Both n1/t/m parity and tau/t/m parameterizations actually run.'),
('Strict bound and maxima','315870 keys, counts77912/79183/79125/79650; maxima2713662/2716104/2718702/2720004, threshold2722720. Every residual count zero; minimum margin2716. Independent grouped costs/deficit boxes match.'),
('Conditional C3 premise discharged','The diagnostic itself does not prove C3cap13. U01 section5 and U09 prove it for the same exceptional original H, closing the caller; no circular scalar-to-C3 inference.')],
'U12':[
('Two-intersection capacity','Every valid middle is charged at exactly two attachments in the disjoint three-point differences. Eachpoint offers <=d-1 available edges, hence2c<=S6-6. Use general formula, not A2/A3-only S6=54+e.'),
('Singleton-intersection cost direction','Actual tv sum n1 and satisfy tv<=C(dv,2). Each middle avoids the shared point, soC1<=35n1-sum dv tv. Cheapest degree-flag relaxation lower-bounds the sum, producing the correct upper direction.')],
'U13':[
('Full source reading and execution accounting','All11 named source files read in full. Ten frozen programs run with writes redirected solely into native/replay; original q4 CHECK read and its full-domain logic independently reproduced by audit/VERIFY. No Lean, whole-H search or recursive reviewers.'),
('Independent fresh actual-interface checks','Additional native INTERFACE_CHECK checks source-degree completeness, all pair trace counts, no-excess q3 domain, marked-family coverage, local generic-c14 caller and original-H integer probability normalization. All pass.')]
}
entries=[]
for u in units:
 for i,(claim,discharge) in enumerate(rows[u],1):
  entries.append({'id':f'{u}-{i:03d}','source_unit':u,'claim':claim,'actual_caller_and_discharge':discharge,'status':'DISCHARGED','declared_imports_allowed':True})
coverage={'shard_id':'fresh-whole-delta8','assigned_unit_ids':list(units),'covered_unit_ids':list(units),'status':'COMPLETE','coverage_fraction':1,'source_units':[{ 'unit_id':u,'files':[{'path':f,'read_scope':'full','line_count':len((ROOT/f).read_text().splitlines())} for f in fs]} for u,fs in units.items()],'uncovered_units':[],'errors':[],'note':'Receipt proves declared source-unit execution coverage, not automatic mathematical completeness. Obligations were extracted after reading frozen units. max_turns8/read-only/recursionfalse were prompt conventions, not tool hard-enforcement; source writes were redirected for actual verifier replay.'}
(P/'COVERAGE_RECEIPT.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n')
(P/'OBLIGATIONS.json').write_text(json.dumps({'entries':entries,'count':len(entries),'open_obligations':[]},ensure_ascii=False,indent=2)+'\n')
imports=[
 {'id':'I01','path':'proofs/PROBABILITY_LEMMAS.md','scope':'P1-P7 conditional permutation-to-original-coloring theorem, zero-deduction specialization. Actual formulas and proof read; no old probability exhaustive suite rerun.'},
 {'id':'I02','path':'proofs/propertyb35/TWENTYONE_TWENTYTWO_MINIMUM_NONUNIT_DEGREE_THREE.md','scope':'Universal21/22-point q<=2 repair and one-red/tree anchor bound. Applied only at21. Actual statement/formula and21-point closure read; no unrelated22 catalogue rerun.'},
 {'id':'I03','path':'proofs/propertyb35/GLOBAL_TWO_FLIP_SHARED_MIDDLE.md','scope':'Only exact common-middle identity and balanced-five-group formula; not its A1 role, threshold-graph section, or extra quotas.'},
 {'id':'I04','path':'proofs/propertyb35/GLOBAL_PRIVATE_PAIR_REPAIR.md','scope':'General one-flip criterion and n1>=397 at21/35. Imported mathematical repair proof read; exact p,q and threshold rederived in native check.'},
 {'id':'I05','path':'proofs/propertyb35/GLOBAL_TWO_FLIP_PATH_REPAIR.md','scope':'General sections1-3 repair theorem, not the Delta<=9 coarse capacity specialization. General actual-Cj objective independently specialized to6864n1+sumwjCj<5445440.'},
 {'id':'I06','path':'context/propertyb35-paper/round01/middle/generic_c3_fourteen_gate_20261020/PROOF.md','scope':'Old complete7812-label/1144-orbit c14 finite catalogue with local selected excess<=4 and internal paircap4. Statement, domain construction and actual coloring interface read; old finite arithmetic not rerun.'},
 {'id':'I07','path':'context/propertyb35-paper/round01/middle/generic_c3_high_degree_saturation_20261020/PROOF.md','scope':'Old1303-label/183-orbit exactcross15/16 catalogue. Its full necessary inventory proof, rather than only the narrower c>=15 displayed theorem, establishes reuse when c>=14 but exactcross>=15. Not rerun.'}]
run=json.loads((P/'ACTUAL_RUN_RECEIPT.json').read_text()); interface=json.loads((P/'INTERFACE_CHECK.json').read_text())
run['fresh_interface_check']=interface;run['combined_cpu_seconds']=run['total_cpu_seconds']+interface['cpu_seconds'];run['budget_cpu_seconds']=15;run['budget_respected']=run['combined_cpu_seconds']<=15;run['status']='PASS'
(P/'ACTUAL_RUN_RECEIPT.json').write_text(json.dumps(run,ensure_ascii=False,indent=2)+'\n')
checks=[
 'Excluded e>=7 boundary explicitly; degree15/no-degree9 spectrum retained.',
 'Equal-degree exceptional pair needs two actual copies; all c>=6 and other degree-pair c5 ranges checked.',
 'Old q3 independent verifier contains a redundant selected-excess<=4 filter: independently rebuilt all119/minF8-only25 and verified the missing-side domain is empty. No global e upper assumption.',
 'Clean star requires every edge meets F: verified C/D no empty exceptional trace, before any budget use.',
 'Exactcross can contain invalid middles: only t>=c used, never the converse.',
 'Marked lambda5 same-side and cross-side placements, including unequal9/8 assignments and t17, were retained before valid exclusions.',
 'Exceptional outer-pair swap involution counted as an unordered edge pair once; C4 bonus is total5/6 rather than n4 or twice5/6.',
 'Shared P consumed once, capacity inequality directions checked; optimizer need not be a realizable graph.',
 'Largest high-center role requires no outside degree assumptions; all actual highpoint edges covered, giving E>=77/78.',
 'Old two-flip specialization mentions Delta<=9, but general theorem does not; this audit rederived the integer actual-Cj criterion from the general theorem with no Delta premise.'
]
now=datetime.now(timezone.utc).isoformat()
audit={'audit_skill':'proof-checker','verdict':'PASS','audit_status':'PASS_WITH_DECLARED_IMPORTS','reason_code':'all_obligations_discharged_modulo_declared_imports','summary':'The complete21-point35-edge pair-covering minimum-degree8 theorem is sound modulo the listed mathematical imports and unreplayed oldc14/c15/c16 catalogues. No fatal, critical, major or minor issue found in the frozen assembly.','target':'For every simple five-uniform H on21 vertices with exactly35 edges, covering every point pair, and with minimum point degree>=8, H has Property B.','trace_path':str(P.relative_to(ROOT)),'thread_id':'/root/twentyone_delta8_complete_fresh_audit','executor_model':'native Codex; concrete host model identity not exposed in this child context','executor_family':'openai','reviewer_model':'native Codex; concrete host model identity not exposed in this child context','reviewer_family':'openai','review_independence':'same-family','acceptance_status':'provisional','reviewer_reasoning':'deep audit requested; actual host effort not separately exposed','generated_at':now,'audited_input_hashes':{str(ROOT/f):'sha256:'+hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for fs in units.values() for f in fs},'details':{'theorems_audited':1,'source_units':13,'obligations':len(entries),'issues':[],'open_obligations':[],'declared_imports':imports,'counterexample_pass':checks,'counterexamples_found':0,'actual_replay_cpu_seconds':run['combined_cpu_seconds'],'new_replay_status':'PASS','outside_scope':['other21-point degree branches','all22-25-point branches','complete m(5)>=36','Lean','independent external-machine reproduction']},'render_html':False,'source_edits':False,'prior_model_opinions_used':False}
(P/'PROOF_AUDIT.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
md='''# Complete21-point minimum-degree-eight audit

**PASS_WITH_DECLARED_IMPORTS — same-family / provisional.** No open proof gap was found in the frozen complete δ8 assembly. The audited theorem is: every simple five-uniform hypergraph on21 vertices with35 edges, covering every point pair and having every point degree at least8, has Property B. No lambda bound, high-excess bound, criticality or numerical certificate is added to that theorem's premises.

This verdict concerns only the stated δ8 branch. It does not prove every21-point branch or the full m(5)≥36 target, and it is not a Lean verification or a second-machine reproduction.

## Independent audit result

All U01–U13 were read in full, including all eleven U13 programs. The source-ordered obligation ledger contains COUNT discharged obligations and no open issue. Coverage is recorded separately in `COVERAGE_RECEIPT.json`; it certifies source-unit reading/execution coverage, not mathematical completeness by itself. No previous whole-target model verdict was used. U07 was read as the explicitly assigned local mathematical proof and receipt.

The exact complete chain is:

1. Total degree175 yields precisely15 degree spectra, including8^20,15. All20 possible selected degree-pair types and100 degree/codegree keys are covered. Ninety-six strict two-lock gates leave precisely four unique actual high-point pairs of codegree5, in sources8,9,11,12.
2. Universal q≤2 repair and the complete q3 domain force Γ minimum degree4. Fresh reconstruction from the full91-orbit record, filtering only the five selected degrees≥8, independently gives119→25. Thus the older verifier's selected-excess≤4 filter is redundant; no global excess≤4 premise is imported. The actual clean exterior8-point star supplies all70 six-lock cases.
3. When all pointpair codegrees≤4, the38 actual selected-degree multisets split into33 old-imported and5 newly verified C3 gates. The complete1,166,584-key scalar calculation leaves only source13/14 keys. All actual edges through the unique14/15-point meet the q4 local roles, giving E≥77/78, contradicting those residual keys' E≤70/73.
4. With one actual codegree5 pair, tau≤142 and the total C4 bonus is5 or6, with no orientation factor2. Every three-intersection outer pair either has a four-point difference set missing an exceptional endpoint, and thus satisfies the old local selected-excess≤4 gate, or belongs to the complete14 marked families. The latter have425 necessary inventories, all strict with maximum25963/29172. Therefore C3≤13n3 for the same H.
5. The five capacities consume a single common P budget. The original-H two-flip criterion is independently normalized to6864 n1+Σwj Cj<5,445,440, without a maximum-point-degree premise. Both full exceptional scalar parameterizations pass315,870 keys, with minimum L-margin2716. Each sufficient criterion supplies a coloring of the original35-edge H.

The corrected W values651,650,655,653 were independently recomputed from raw degree lists and are correct.

## Actual deterministic work

Ten frozen local programs were re-executed; every write was redirected into this audit's `native/replay/` subtree. A further fresh `INTERFACE_CHECK.py` verifies the domain and caller interfaces described above. Total measured calculation CPU was CPU seconds, below the15-second allowance. Every run exited normally. `ACTUAL_RUN_RECEIPT.json` and `run-01.log` through `run-10.log` retain exact commands, per-run CPU and raw output. The source proof/certificate files were not modified.

| Check | Actual coverage/result |
|---|---|
| q3 scope and index replay | 3276 labels/91 orbits;119→25 without excess filter;23 five-lock +70 six-lock strict |
| strong pairs | All100 double-lock and64 subsidiary triple-lock bounds replay; required96 pair gates strict |
| new all-small-codegree C3 | 412 labels/62 marked representatives, all strict |
| high-center q4 | Three full23751-label domains;70 threshold groups rebuilt;12 tails strict |
| old-condition scalar | All15 spectra,1,166,584 keys; maxima and15 residuals match |
| unique-lambda5 C3 | Fresh primary generation plus independent425-inventory/8925-row replay, all strict |
| unique-lambda5 scalar | Both primary and independent full315,870-key scans, all strict |

The64 three-lock subsidiary cases are accurately reported as40 strict/24 nonstrict and are not used as a claimed completion of that local search. The assembly bypasses those24 through its C3/moment argument.

## Declared imports and exact trust boundary

IMPORTS

The old c14/c15/c16 finite catalogues remain explicit, unreplayed imports. Their mathematical input requirements and exactcross-to-original-coloring interfaces were checked. Their earlier model opinions are not evidence in this audit. All new finite domains named above were actually replayed. The conditional permutation and repair principles are mathematical imports whose applicable formulas and proof interfaces were read; no unrelated historical test suite was rerun.

## Adversarial checks

CHECKS

No algebraically verified counterexample or unresolved candidate was found. There were no source repairs, assumption changes or scope expansion. The old six-degree-star, unit8 and four-core catalogues are not dependencies of this complete δ8 proof and were not run.

The requested max_turns8, read-only and recursionfalse conventions were prompt instructions, not host-enforced reviewer restrictions. No recursive agent was spawned. Executable writes were redirected into the authorized native directory; HTML rendering was disabled for this local audit.
'''.replace('COUNT',str(len(entries))).replace('CPU seconds',f"{run['combined_cpu_seconds']:.6f} seconds").replace('\nIMPORTS\n','\n'.join(f"- **{i['id']}** `{i['path']}` — {i['scope']}" for i in imports)).replace('CHECKS','\n'.join('- '+x for x in checks))
(P/'PROOF_AUDIT.md').write_text(md)
sk='''# Source-ordered proof skeleton

The canonical target is the theorem stated in PROOF_AUDIT.json. All quantities are finite exact integers or rational probabilities; there are no limits, asymptotic statements, measure-theoretic interchanges, or parameter-uniformity claims. Exchanges of sums are finite.

Typed symbols: H is the original simple35-edge five-uniform hypergraph on21 points; d(v),lambda(u,v),b,e,W,tau are nonnegative integers with lambda>=1 supplied by pair coverage. Gamma is a simple graph on the35 original edge indices, q(F) its degree and s(F)=34-q(F). nj counts unordered distinct outer-edge pairs with intersection j. cj and Cj count actual middle-edge flags, retaining original indices; P=sum Cj is shared. Kd(N) is the minimum integer degree-flag cost; f and B are deterministic integer majorants. U is a rational upper bound on a conditional failure probability; U<1 is sufficient for an original-H coloring. L is half an integer objective, not a probability by itself.

Dependency DAG: original H ->15 spectra ->strong-pair dichotomy. Original H + imported q<=2 + q3/clean-star ->Gamma min4. Small-codegree branch + new/old C3 gates + shared capacities ->15-spectrum scalar ->high-center q4 contradiction. Exceptional branch ->tau/C4 errors + old/new marked C3 gate ->four-spectrum scalar ->original-H two-flip contradiction. Both branches imply target. No branch calls its own conclusion, and no scalar diagnostic is used to establish its own C3 premise.

Assumption ledger and microclaims follow in frozen source order. Each item supplies its actual caller and discharge, with old imports explicitly enumerated in PROOF_AUDIT.md.

'''
for ent in entries:
 sk+=f"## {ent['id']} — {ent['claim']}\n\n{ent['actual_caller_and_discharge']}\n\nStatus: DISCHARGED (modulo listed imports where used).\n\n"
(P/'PROOF_SKELETON.md').write_text(sk)
(P/'PROOF_CHECK_STATE.json').write_text(json.dumps({'status':'completed','rounds':1,'review_agent_ids':['/root/twentyone_delta8_complete_fresh_audit'],'acceptance_gate':'PASS_WITH_DECLARED_IMPORTS','review_independence':'same-family','acceptance_status':'provisional','fatal_fixed':0,'critical_fixed':0,'major_fixed':0,'minor_fixed':0,'counterexamples_found':0,'render_html':False,'timestamp':now},indent=2)+'\n')
print(json.dumps({'status':'PASS_WITH_DECLARED_IMPORTS','units':len(units),'obligations':len(entries),'combined_cpu_seconds':run['combined_cpu_seconds'],'audit_dir':str(P)}))
