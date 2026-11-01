from pathlib import Path
import json,hashlib,datetime
R=Path('/Users/rfy_naiveai/Desktop/aris4math');A=R/'context/propertyb35-paper/round01/audit-unique-six-two-three-seven-20261020/native';B='context/propertyb35-paper/round01/'
paths={
'U01':['proofs/propertyb35/TWENTYONE_UNIQUE_SIX_TWO_OR_THREE_SEVEN.md'],
'U02':['proofs/propertyb35/TWENTYONE_UNIQUE_SIX_TWO_OR_THREE_SEVEN_MINIMUM_NONUNIT_DEGREE_FOUR.md'],
'U03':[B+'middle/four_nonunit_degree_six_center_20261020/REPORT.md'],
'U04':[B+'middle/generic_c3_fourteen_gate_20261020/PROOF.md'],
'U05':[B+'middle/generic_high_degree_pair_gates_20261020/REPORT.md'],
'U06':[B+'middle/generic_quad_core_multiplicity_three_20261020/PROOF.md'],
'U07':[B+'middle/generic_degree_six_star_count_20261020/PROOF.md'],
'U08':[B+'middle/a2_a3_joint_moment_frontier_20261020/CAPACITY_LEMMAS.md'],
'U09':['proofs/propertyb35/GLOBAL_TWO_FLIP_SHARED_MIDDLE.md'],
'U10':['proofs/propertyb35/GLOBAL_TWO_FLIP_PATH_REPAIR.md'],
'U11':['proofs/propertyb35/GLOBAL_PRIVATE_PAIR_REPAIR.md'],
'U12':[B+'twentyone-high/unique6_with7/new_structure_20261020/SIX_UNIT8_POOL_PROOF.md'],
'U13':[B+'middle/a2_a3_min4_cap13_closure_20261020/NO_CRITICAL_FILTER.py',B+'middle/a2_a3_min4_cap13_closure_20261020/NO_CRITICAL_CHECK.py'],
'U14':[B+'middle/three_nonunit_direct_repair_20261020/VERIFY_ASSEMBLY.py'],
'U15':[B+'middle/four_nonunit_degree_six_center_20261020/VERIFY.py',B+'middle/four_nonunit_degree_six_center_20261020/INDEPENDENT_VERIFY.py',B+'middle/four_nonunit_degree_six_center_20261020/FIVE_LOCK_FULL5.py'],
'U16':[B+'middle/generic_c3_fourteen_gate_20261020/VERIFY.py']}
claims={
'U01':[
('§1','H has 21 points, exactly35 distinct five-edges, paircover, unique degree6 x, exactly a=2 or3 degree7 points; non-B implies e=2a+b−11 and b≤9−r.','Total degree175 and the same x-star row excess4; six-unit8 import.','U12-01'),
('§1','All possible degree lists lie in the four A2 and twelve A3 displayed spectra.','e≥0, b≤9, partition all e≤4 into high-point increments; at least8 base-nine points accommodate all partitions.','U01-01'),
('§2','All structural gates apply to the same original H without criticality, oldT34 or thresholdT.','Unique x, global excess≤4, paircover; separate proofs of codegree≤4, n4≤13, Gamma minimum4, C3≤13n3.','U02-06 U04-04 U05-04 U06-06'),
('§3','The three moments, integer n formulas and tau≥max(0,4(Delta−10)) are necessary.','Double-count unordered original edge pairs and covered point pairs; one row of nonnegative tau terms is a subset of total tau, not half of it.','U11-03'),
('§4','P≤B(n1) for exactly35 boxes with s∈[0,30].','Gamma min4, s=34−q; discrete convex f and moving one unit between two interior boxes.','U02-06 U09-01 U09-02'),
('§5','One common P and five caps give the greedy weighted upper bound for original two-flip risk.','All Cj nonnegative, weights increase; Kd minimizes actual degree-weighted singleton count; all caps bind the same H.','U08-01 U08-02 U04-04 U10-04'),
('§6–7','Complete integer necessary domains give A2 maximumL<2722720 and exactly33 A3 keys after row cut.','Two complete parameterizations, exact arithmetic, no thresholdT used in the new bound; wedge is zero at n4≤13.','U13-01 U13-02 U13-03 U13-04'),
('§8','A3 cannot realize any surviving key: six actual x-edges have q≥5, all29 others q≥4, so E≥73, whereas all33 keys E≤72.','Each x-edge satisfies the conditional q4 theorem independently in the same H; handshake on original35 edge graph.','U03-04 U01-03 U01-07')],
'U02':[
('§1','In the target role e≤4; the general q≤2 repair applies without using paircaps.','Six-unit8 pool and degree identity; q≤2 theorem read in full, 21-point branch mathematically rederived.','U12-01'),
('§2','For each actual three-exception F, U(v,a,r) bounds the original bad-coloring union.','Uniform r-subset of16 exterior points; red-event tree subtraction; exact exceptional trace risk; same actual attachment count.',''),
('§3','Safe prefixes and the genuine S5 trace quotient cover all3276 multiset triples, leaving119 attachments and83 necessary role keys.','35 residual-type prefixes; only safe-prefix implication is used despite high-c safe tails; attachments transported with labels.','U14-01 U14-02'),
('§4','Strict sum min(A,B,C)<1 returns a proper coloring of originalH.','Uniform injection after fixing distinct lock positions; ordered distinct original edge indices; fixed true common vertex has no r*q factor; greedy critical-event inclusion.',''),
('§5','79 of83 five-lock inputs are strictly certified and exactlyfour require an actual x-star refinement.','All35 trace indices rebuilt; fixed positions; remaining four have F degrees≥7, so x outsideF.','U14-03'),
('§6–8','The four residual inputs map to exactly5+5+35+2 necessary common x-stars; all47 strict, hence deltaGamma≥4.','Six edges from one x-star; F-incidence excess; at most one multi-trace; C includes its A2 subcase; projection restored exactly.','U02-01 U02-04 U02-05 U14-03')],
'U03':[
('Statement/interface','The q4 gate only concerns F containing the unique six-degree x and the five stated local/global conditions.','Actual target role verifies every hypothesis; no assumption deltaGamma≥4 is used inside this gate.',''),
('Complete anchor calculation','All four-exception marked trace multisets and all anchor failure sets are covered.','26 trace types, repetitions allowed; S4 fixes x; full a0..30/r0..16 failures; exact x row repeat budget≤4.','U15-01 U15-02'),
('Five fixed certificates','The complete necessary domain leaves40 labeled joint inputs /5 joint orbits; all five inventories retain35 edge indices.','Paircap includes the originalF; d(x)=1+a0+h0=6; nonnegative attachment compositions and exact degree limits.','U15-02 U15-03'),
('Conclusion','Each remaining inventory gives originalH PropertyB by a strict zero-quota fixed permutation certificate.','Representative transport fixes x and moves positions; five-lock conditional criterion, max233003/240240.','U02-04 U03-01 U03-02 U03-03')],
'U04':[
('§1','Valid middle implies cross exact trace, but cross exact trace need not be valid.','Outer singleton attachments are distinct and lie in opposite exclusive pairs; common3 points prohibited.',''),
('§2','Exact cross14 allows q=0 and at most one triple, giving160+48=208 high-trace shapes.','Four inclusive cross caps sum16; a triple spends2; side traces≥1; all cross deficits explicitly exhausted.',''),
('§2','Actual selected degrees are7..13, total excess≤4; order8 side-marked transports preserve every condition.','Each cross row≥6 plus its side outer; degree recovery by subtraction; no hidden selected minimum degree.','U04-01 U04-02'),
('§1,3–4','All c≥14 cases are colorable, hence C3≤13n3 under the actual global role.','Complete exact14 7812/1144 strict certificates and the t15/16 1303/183 import, whose implementation only needs cross traces rather than actual c≥15.','U16-01 U16-02 U16-03')],
'U05':[
('§1–2','Two-lock inventory is unique for given21/35,d1,d2,c; complete118 high-pair inputs have110 strict certificates.','Möbius inclusion recovery and full degree/codegree range; zero quota; independent binomial/factorial replay.',''),
('§3','Six ofeight numerical tails require more than global excess4, and the other two require A3 e=4.','For both high selected vertices, d1+d2−18≤e; no low/high pair is silently discarded.','U01-01'),
('§4','Two A3 tails lift through the same unit x-star to exactlyfour triples and all are strict.','e4 implies b9 and all four x-row repetitions on degree8 points, so both high points unit; exact Ixyz∈{0,1}.','U05-02'),
('§5–6','Every actual pair has codegree≤4 in a non-B target H.','x-pair row excludes≥6; lambda5 link structure has compatibility177176>29*6006; all degree7..9 pairs lambda≥5 re-evaluated, including7/7; other pairs use complete high domain.','U05-01 U05-03')],
'U06':[
('§1–2','Every avoiding-x four-core of multiplicity≥3 maps to q3/q4 shapes and the complete6923/3809 marked degree domain.','Core paircaps forceq≤4;97 shapes; star coverage17 gives exact necessary capacity; all86 sorted degree spectra and true stabilizers.','U05-04'),
('§3','3805/3809 representatives are strict; nine nested-quota calculations correctly charge actual bad pairs.','Pure bad-pair subset of total; minimal nonnegative weighted union selected without double spending; source weights sum both orientations.',''),
('§3–4','The four remaining10^4 inventories lift via one unit x-star to exactly23 five-lock inputs, all strict.','Bell4 partitions; each K point belongs to exactlyone x-edge; residual empty budget6−blocks and all35 indices preserved.','U06-01 U06-02'),
('§5','Every non-B target H satisfies the four-core conclusion, including the four exceptions.','A2 e≤2 excludes10^4; A3 e4 exhausts x repetition on four degree8 vertices, giving lambda(x,K)=1.','U01-01 U06-03'),
('§7','Same-sample star plus generic rank≥11 gives n4(H−x)≤6.','20<25 and29>20; incidence Gram positive definite factor; forest extension4→11→28; exact Hunter deduction9306 yields margin28.','U07-03'),
('§7','n4≤6+6+1=13.','Each ofsix cross-star four-intersections has at mostone partner by actual four-core theorem; two star-internal pairs of3-link intersections would consume repetition cost≥6>4.','U06-04 U06-05')],
'U07':[
('§1','All simple six4-stars covering20 points are represented by the five cost4 multiplicity partitions.','Excess4; repeated supports may repeat; only15 fourfold-parallel duplicate stars excluded; all5886 keys.',''),
('§2–4','True S6 orbits and two exact inclusion-exclusion forms give minimumC=164896.','Finite balanced10/10 sample; conflicting red/blue supports havezero count; complete41 orbit cover and independent IE replay.','U07-01'),
('Actual caller','Every selected degree6 x in targetH produces such a star, and compatible properHbar coloring extends toH.','Simple original edges give distinctlinks; paircover gives union20; choose x color having no monochromaticlink.','U07-01 U07-02')],
'U08':[
('Two-intersection capacity','C2≤floor((S6−6)/2)n2=(24+floor(e/2))n2.','Each middle charges exactlytwo distinct exclusive attachments; at least8 degree≥9 points and at most4 above9 put all excess in top6.','U01-01'),
('Singleton capacity','C1≤35n1−Kd(n1).','A middle avoids the unique commonouterpoint; actual tv feasible under C(dv,2); cheapest-capacity filling minimizes degree cost.','')],
'U09':[
('§1','P=sumCj=sumF sumg<h tFg*tFh and sumF sF=2n1 exactly.','Every unorderedouter/middle flag has unique two groups; ordered paths counted twice only in EZ.',''),
('§2','Balanced five attachment groups maximize wedge countf(s); f is discrete convex.','Moving groupmass toward balance lowers square sum; difference s−floor(s/5).',''),
('§3–5 and nonthreshold part§6','Additional A1 inequalities are conditional on their explicitly narrower roles and are not transferred into A2/A3.','Checked algebra, distinct A1 unit relations, n4 import and price inequality; thresholdgraph/DP appendix explicitly excluded from targetdependency.','')],
'U10':[
('§1–2','Every failed two-flip trial produces a counted ordered path and the failure indicator bound is valid.','Initially unique badedge; m_g=1 eliminates new opposite-color badedge; differentg/h yield distincttriples.',''),
('§2–3','EX,ES,EZ yield original coloring when expectationcriterion is strict.','Finite sample; EX=Mp, ES=2n1q, EZ=2sumCjrj; u≥(2k−S)+ and no independence.','U10-01'),
('§3–4','Atn21,k5,M35,a10, pathnumerators are36,120,330,792,1716 and threshold2722720.','Explicit binomial counts recomputed; general exactC criterion does not requireDelta≤9.','U10-02'),
('Main interface','3432n1+(sumwjCj)/2<2722720 implies originalPropertyB.','Substitute exact probabilities in generalcriterion; actualC dominated by common-budget relaxation.','U10-03')],
'U11':[
('§1–2','One-flip failure is bounded by X/2+S/(2k).','A newly badedge meets unique badG exactly at flippedvertex; witnesscounts for differentvertices distinct.',''),
('§3–4','Every non-B21/35simple5 H has n1≥397.','Finite balancedsubset sample; exact rational threshold1190/3; integerceiling.','U11-01'),
('§5','All paircover intersectionmoment identities are exact.','Simple5 excludes edgeintersection5; 350 pointpairincidences cover210 pointpairs; no coloringassumption in the equalities.','')],
'U12':[
('Dependency scope','Six-unit8 theorem has no hidden no-seven or outsider-minimumdegree assumption.','Read old local recovery, three/four/five/six generators, fixed/joint verifier interfaces; selected degrees only. Full older certificate catalogue remains declaredimport.',''),
('§1','Six-neighbor center partition is3+3 or matching;3+3 violates a noncenterdegree7 count.','Every5-view in old26 residuals; same-block triple fully consumedbyx; pairincidences8 require≥8 noncenteredges, butdegree is7.','U12-01'),
('§2','Neighbor codegree1 graph is empty orK1,5; emptycase is old complete270/3 strict import.','Every induced5-graph emptyorK1,4; overlapping5-sets force a unique globalstarcenter.','U12-01'),
('§3–4','Starcase has no compatible six-view realization.','All S5 labels reconstructed from old26; full shared-containing-count join153→999→898→207→15→0 re-executed; sameH makes every overlap identical.','U12-01 U12-02 U12-03')],
'U13':[
('Both source algorithms','Both implementations generate the complete16 degreespectra and necessary integerdomain.','Primarytau,t,m enumeration and independentn1,t,m parity recovery; upperbounds fromn2≥0; no saved survivorlist used to generate domain.','U01-02 U01-04'),
('Box and costs','All1051 deficit states equal independent35-slot knapsack; degree-layer costs and greedyallocation verified.','Cap30 and atmostone interiorbox; no criticalityorT in newP; n4≤13 makes retained oldwedgefilter identicallyzero.','U01-05 U01-06'),
('All admissible maxima','Four A2 maximalL values2713872,2718744,2719626,2716860 are below threshold.','All currentdomainkeys evaluated, notjust storedtails; eachspectrum maxchecked by second generation.','U13-01 U13-02'),
('Survivors/binding','Fresh202 and33 outputkeys/distributions match declarednew files; E70/71/72 counts24/7/2.','Additional exact rebinding because suppliedchecker compares historical202/33 files; this is execution bookkeeping, not a mathematicalgap.','U13-01 U13-02')],
'U14':[
('Prefixes/orbits','All35 prefixcertificates are strict with correctslopes; S5 images disjoint and cover3276 inputs.','Fullcode and execution; no unsupportedmonotonefailuretail.','U02-02'),
('Attachments','All119 generic and83 actualnecessary keys reconstructed.','Thresholddeltas sum≤3; completeall-r/v failurecheck; min6, unique6, totalexcess≤4 only.','U14-01'),
('Fixed replays','79 five-lock and47 six-lock certificates retain35 indices,1190 orderedpairs,21 rows.','Reconstruction and everyrow exact; maximum139/143 and428/429; direct47-key equality.','U02-04 U14-02')],
'U15':[
('VERIFY.py','All23751 labeled four-exception inputs and1563 markedorbits evaluated with all70 fullfailuresets.','S4 fixesx, paircodegree/excess/degree constraints necessary; attachmentchoices include allfailures notjust prefix.','U03-01'),
('INDEPENDENT_VERIFY.py','Different labeled signature/complement-binomial generation gives40 labeledassignments and5 jointorbits.','Fulljoint trace/attachmenttransport and all70 failuretables agree.','U15-01'),
('FIVE_LOCK_FULL5.py','All5 fullinventories have strict fixedcertificate.','Sixteen fixedpositions; zeropairquotas; independentexpanded35-index105-row replay.','U02-04 U15-02')],
'U16':[
('Domain','Independent inclusive-pair/degree enumeration regenerates all7812 exactcross14 keys.','Möbius recovery includingone-triple correction; no negativeinventory; sides≥1; e≤4.','U04-02'),
('Marked transport','Eight side flips/swaps give exactly1144 representativekeys.','Allcounts movedtogether; actualH relabeling not presumedautomorphism.','U16-01'),
('Certificates','All1144 zerodeduction bounds strict, maximum34904/36465.','35 originalindices and1190 orderedpairs each; exact independentinjections.','U02-04 U16-02')]}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
entries=[];hashes={}
for u,ps in paths.items():
 files=[]
 for p in ps:
  b=(R/p).read_bytes();digest='sha256:'+hashlib.sha256(b).hexdigest();hashes[str(R/p)]=digest
  files.append(dict(path=p,line_span=[1,len(b.decode().splitlines())],bytes=len(b),sha256=digest))
 obligations=[dict(id=f'{u}-{i:02d}',extraction_ordinal=i,anchor=c[0],statement=c[1],justification=c[2],depends_on=c[3].split(),status='discharged_modulo_declared_imports' if u=='U12' else 'checked') for i,c in enumerate(claims[u],1)]
 entries.append(dict(source_unit_id=u,files=files,coverage='full_assigned_scope',exclusions=['threshold-graph subsection and threshold-DP appendix from mathematical target dependency'] if u=='U09' else [],obligations=obligations))
receipt=dict(shard_id='native-single-shard',assigned_unit_ids=list(paths),covered_unit_ids=list(paths),status='COMPLETE_SOURCE_UNIT_EXECUTION_COVERAGE',source_unit_count=16,declared_source_file_count=sum(map(len,paths.values())),obligation_count=sum(len(x) for x in claims.values()),coverage_fraction='16/16',meaning='Source-unit reading/extraction/execution coverage only; this bookkeeping is not a proof of semantic completeness.',reviewer_agent_id='/root/a2_a3_complete_fresh_audit',reviewer_model='gpt-6-astra',reviewer_reasoning='ultra',identity_source='fresh native reviewer slot selected by parent; no independent service identity attestation',review_independence='same-family',acceptance_status='provisional',prior_model_reviews_read=False,entries=entries,errors=[],generated_at=now,input_binding='SHA256 only for the nineteen declared source files, to bind this verdict to the reviewed snapshot.')
(A/'COVERAGE_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
# The global dependency DAG is assembled only after the complete source receipt exists.
allobs={o['id']:o for e in entries for o in e['obligations']}
visiting=set();seen=set()
def visit(k):
 if k in visiting:raise AssertionError(('DAG cycle',k))
 if k in seen:return
 visiting.add(k)
 for d in allobs[k]['depends_on']:assert d in allobs;visit(d)
 visiting.remove(k);seen.add(k)
for k in allobs:visit(k)
header='''# Fresh proof skeleton: unique six-degree, two/three seven-degree branches

The audited quantified theorem is: for every finite set V with |V|=21 and every set H⊆{E⊆V:|E|=5} with |H|=35, if every two distinct V-points occur together in some E∈H, minimum point-degree is6, there is exactlyone point x ofdegree6, and exactlytwo or three points ofdegree7, then there exists c:V→{red,blue} such that every E∈H contains both colors. The proof is by contradiction on that same fixed H. It proves neither the whole21-point branch nor m(5)≥36.

This ledger was extracted after reading all16 assigned units. Source ordinals are stable within each frozen source unit. The receipt proves source-unit coverage only. Each item below records a mathematical obligation and its actual justification, not a confidence score.

## Typed symbols and finite sample spaces

- V:21-element vertexset. H:set of35 distinct five-subsets. x∈V:unique degree6 vertex. d(v), λ(u,v): original integer degree and paircodegree.
- a∈{2,3}:number of degree7 points; b:number of degree8 points; e=Σmax(d−9,0):nonnegative integer high-degreeexcess. Δ=max d. W=Σ_v C(d(v),2).
- n_j∈Z≥0, j=0..4:number of unordered distinct original edgepairs meeting inj points. m=n3,t=n4 in the moment enumeration. τ=Σ_pointpairs C(λ−1,2).
- Γ:simple graph on the35 original edgeindices, adjacent iff intersection≠1. q(F):its degree; EΓ=595−n1:its edgecount. This q is not the private-pair probability q_prob.
- t(F,g):number of original edges meeting F exactlyatg; s(F)=Σ_g t(F,g)=34−q(F). P:unorderedouter/middle flagcount. C_j:part ofP with outerintersectionj. All C_j share oneP.
- μ_T:integer exact selected-point trace multiplicity; repeatedtraces retain distinct originaledgeindices. I_A:inclusive containing-edgecount. Relabelings transport μ, degrees, actualstars and positions together.
- Balanced21-point coloring sample:uniform10-subsets ofV, size352716. Anchor sample:uniformr-subsets ofV\\F, size C(16,r). Star sample:uniform10-subsets ofV\\{x}, size184756. Conditionalpermutation sample:all(21−s)! injections after fixing s distinct selectedpoints at distinctpositions.
- A_k,B_k,C_k in permutationlemmas are event majorants; C_k is distinct from global middlecounts C_j. Every sum is finite. There is no limit, asymptoticuniformity, differentiation, or improperintegral obligation.

## Assumption ledger and dependency graph

The primary hypotheses are exactly21,35,simple5,paircover,unique6,exacttwo/three7. Exact35 is used in momentcounts, stubidentities, totaldegree175, graph34-neighbor limit and both repairthresholds. Paircover gives positive λ and x-starunion20; it is also needed for nestedlink quotas and the four-core cover17 condition. Unique6 forces every otherpoint degree≥7 and locates x outside the four q3 residual F. Exacta≤3 gives e≤4 through the unit8 pool and atmostthree degree7 points in q4 F. No T33/T34 theorem, edgecriticality, maximumΓdegree29, thresholdgraph optimization, or degreeprefix DP enters the graph.

The principal acyclic chain is:

1. Original H + declared old local unit8 catalogue → six-unit8 pool → sixteen spectra/e≤4.
2. The spectra → strong-pair gates → λ≤4; separately the spectra + generalq≤2 + q3actualstar → δΓ≥4.
3. λ≤4 + e≤4 + actualxstar → threefoldfour-core exclusion; starcount + genericrank + thisexclusion → n4≤13.
4. λ≤4 + e≤4 → C3≤13n3. Actualdegrees → C1,C2; paircap → C4; original35 → C0.
5. Original moments + rowτ + δΓ≥4 → complete integerdomain and commonP box. Fivecaps + that oneP → two-flip majorant.
6. A2 complete maxima strict. A3 leaves33 necessarykeys with EΓ≤72.
7. Every one ofsix actual x-edges satisfies q4gate → q≥5 there; allotheredges q≥4 → EΓ≥73 → contradiction.

In particular q3 uses no paircap; q4 uses no δΓ premise. The old677 assertion that nonunitseven points have codegreetwo is unnecessary in the new chain: the weaker expenditure of at leastone x-row unit per nonunitseven point already suffices. The strong7/7 case was independently checked through its two-lock certificates, avoiding any dependence on that stronger statement.

Declared import retained: the older complete local unit8 catalogue (selected(6,8,8) gates; three/four/five-neighbor domains and fixed/rationaljoint witnesses; six-neighbor270-label/3-orbit certificates), as called by U12. Its written mathematics, recovery/generator code and fixed/joint source interfaces were checked for the present role. Its new matching/star join was actually rerun. The full older catalogue was not regenerated/replayed in this audit. This is an explicit reproducible import, not an unresolved new lemma, and is the reason for PASS_WITH_DECLARED_IMPORTS. Generalq≤2, conditionalpermutation, genericrank and t15/16 were additionally read in their actual sources; their relevant mathematics was checked, and t15/16 finitecertificates were rerun.

## Source-ordered micro-claims
'''
parts=[header]
for ent in entries:
 parts.append('\n### '+ent['source_unit_id']+'\n\n')
 parts.append('Source: '+', '.join('`'+z['path']+'`' for z in ent['files'])+'\n\n')
 for ob in ent['obligations']:
  parts.append(f"**{ob['id']} — {ob['anchor']}.** Context: the stated source hypotheses and {', '.join(ob['depends_on']) or 'the original fixed-H definitions'}. ⊢ {ob['statement']}\n\nRule and discharge: {ob['justification']}\n\n")
parts.append(f'\nThe mechanically checked obligation DAG has {len(allobs)} nodes and no directed cycle. The semantic review separately checked that all role/finite-input assertions used here precede the conclusion and none depends on A2/A3 colorability.\n')
(A/'PROOF_SKELETON.md').write_text(''.join(parts))
(A/'AUDIT_META.json').write_text(json.dumps(dict(generated_at=now,audited_input_hashes=hashes,obligation_count=len(allobs),dag_acyclic=True),indent=2)+'\n')
print('Coverage',len(paths),'units;',len(hashes),'sources;',len(allobs),'obligations; DAG acyclic')
