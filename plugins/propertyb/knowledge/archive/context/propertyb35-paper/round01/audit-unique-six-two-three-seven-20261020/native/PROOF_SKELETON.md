# Fresh proof skeleton: unique six-degree, two/three seven-degree branches

The audited quantified theorem is: for every finite set V with |V|=21 and every set H⊆{E⊆V:|E|=5} with |H|=35, if every two distinct V-points occur together in some E∈H, minimum point-degree is6, there is exactlyone point x ofdegree6, and exactlytwo or three points ofdegree7, then there exists c:V→{red,blue} such that every E∈H contains both colors. The proof is by contradiction on that same fixed H. It proves neither the whole21-point branch nor m(5)≥36.

This ledger was extracted after reading all16 assigned units. Source ordinals are stable within each frozen source unit. The receipt proves source-unit coverage only. Each item below records a mathematical obligation and its actual justification, not a confidence score.

## Typed symbols and finite sample spaces

- V:21-element vertexset. H:set of35 distinct five-subsets. x∈V:unique degree6 vertex. d(v), λ(u,v): original integer degree and paircodegree.
- a∈{2,3}:number of degree7 points; b:number of degree8 points; e=Σmax(d−9,0):nonnegative integer high-degreeexcess. Δ=max d. W=Σ_v C(d(v),2).
- n_j∈Z≥0, j=0..4:number of unordered distinct original edgepairs meeting inj points. m=n3,t=n4 in the moment enumeration. τ=Σ_pointpairs C(λ−1,2).
- Γ:simple graph on the35 original edgeindices, adjacent iff intersection≠1. q(F):its degree; EΓ=595−n1:its edgecount. This q is not the private-pair probability q_prob.
- t(F,g):number of original edges meeting F exactlyatg; s(F)=Σ_g t(F,g)=34−q(F). P:unorderedouter/middle flagcount. C_j:part ofP with outerintersectionj. All C_j share oneP.
- μ_T:integer exact selected-point trace multiplicity; repeatedtraces retain distinct originaledgeindices. I_A:inclusive containing-edgecount. Relabelings transport μ, degrees, actualstars and positions together.
- Balanced21-point coloring sample:uniform10-subsets ofV, size352716. Anchor sample:uniformr-subsets ofV\F, size C(16,r). Star sample:uniform10-subsets ofV\{x}, size184756. Conditionalpermutation sample:all(21−s)! injections after fixing s distinct selectedpoints at distinctpositions.
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

### U01

Source: `proofs/propertyb35/TWENTYONE_UNIQUE_SIX_TWO_OR_THREE_SEVEN.md`

**U01-01 — §1.** Context: the stated source hypotheses and U12-01. ⊢ H has 21 points, exactly35 distinct five-edges, paircover, unique degree6 x, exactly a=2 or3 degree7 points; non-B implies e=2a+b−11 and b≤9−r.

Rule and discharge: Total degree175 and the same x-star row excess4; six-unit8 import.

**U01-02 — §1.** Context: the stated source hypotheses and U01-01. ⊢ All possible degree lists lie in the four A2 and twelve A3 displayed spectra.

Rule and discharge: e≥0, b≤9, partition all e≤4 into high-point increments; at least8 base-nine points accommodate all partitions.

**U01-03 — §2.** Context: the stated source hypotheses and U02-06, U04-04, U05-04, U06-06. ⊢ All structural gates apply to the same original H without criticality, oldT34 or thresholdT.

Rule and discharge: Unique x, global excess≤4, paircover; separate proofs of codegree≤4, n4≤13, Gamma minimum4, C3≤13n3.

**U01-04 — §3.** Context: the stated source hypotheses and U11-03. ⊢ The three moments, integer n formulas and tau≥max(0,4(Delta−10)) are necessary.

Rule and discharge: Double-count unordered original edge pairs and covered point pairs; one row of nonnegative tau terms is a subset of total tau, not half of it.

**U01-05 — §4.** Context: the stated source hypotheses and U02-06, U09-01, U09-02. ⊢ P≤B(n1) for exactly35 boxes with s∈[0,30].

Rule and discharge: Gamma min4, s=34−q; discrete convex f and moving one unit between two interior boxes.

**U01-06 — §5.** Context: the stated source hypotheses and U08-01, U08-02, U04-04, U10-04. ⊢ One common P and five caps give the greedy weighted upper bound for original two-flip risk.

Rule and discharge: All Cj nonnegative, weights increase; Kd minimizes actual degree-weighted singleton count; all caps bind the same H.

**U01-07 — §6–7.** Context: the stated source hypotheses and U13-01, U13-02, U13-03, U13-04. ⊢ Complete integer necessary domains give A2 maximumL<2722720 and exactly33 A3 keys after row cut.

Rule and discharge: Two complete parameterizations, exact arithmetic, no thresholdT used in the new bound; wedge is zero at n4≤13.

**U01-08 — §8.** Context: the stated source hypotheses and U03-04, U01-03, U01-07. ⊢ A3 cannot realize any surviving key: six actual x-edges have q≥5, all29 others q≥4, so E≥73, whereas all33 keys E≤72.

Rule and discharge: Each x-edge satisfies the conditional q4 theorem independently in the same H; handshake on original35 edge graph.


### U02

Source: `proofs/propertyb35/TWENTYONE_UNIQUE_SIX_TWO_OR_THREE_SEVEN_MINIMUM_NONUNIT_DEGREE_FOUR.md`

**U02-01 — §1.** Context: the stated source hypotheses and U12-01. ⊢ In the target role e≤4; the general q≤2 repair applies without using paircaps.

Rule and discharge: Six-unit8 pool and degree identity; q≤2 theorem read in full, 21-point branch mathematically rederived.

**U02-02 — §2.** Context: the stated source hypotheses and the original fixed-H definitions. ⊢ For each actual three-exception F, U(v,a,r) bounds the original bad-coloring union.

Rule and discharge: Uniform r-subset of16 exterior points; red-event tree subtraction; exact exceptional trace risk; same actual attachment count.

**U02-03 — §3.** Context: the stated source hypotheses and U14-01, U14-02. ⊢ Safe prefixes and the genuine S5 trace quotient cover all3276 multiset triples, leaving119 attachments and83 necessary role keys.

Rule and discharge: 35 residual-type prefixes; only safe-prefix implication is used despite high-c safe tails; attachments transported with labels.

**U02-04 — §4.** Context: the stated source hypotheses and the original fixed-H definitions. ⊢ Strict sum min(A,B,C)<1 returns a proper coloring of originalH.

Rule and discharge: Uniform injection after fixing distinct lock positions; ordered distinct original edge indices; fixed true common vertex has no r*q factor; greedy critical-event inclusion.

**U02-05 — §5.** Context: the stated source hypotheses and U14-03. ⊢ 79 of83 five-lock inputs are strictly certified and exactlyfour require an actual x-star refinement.

Rule and discharge: All35 trace indices rebuilt; fixed positions; remaining four have F degrees≥7, so x outsideF.

**U02-06 — §6–8.** Context: the stated source hypotheses and U02-01, U02-04, U02-05, U14-03. ⊢ The four residual inputs map to exactly5+5+35+2 necessary common x-stars; all47 strict, hence deltaGamma≥4.

Rule and discharge: Six edges from one x-star; F-incidence excess; at most one multi-trace; C includes its A2 subcase; projection restored exactly.


### U03

Source: `context/propertyb35-paper/round01/middle/four_nonunit_degree_six_center_20261020/REPORT.md`

**U03-01 — Statement/interface.** Context: the stated source hypotheses and the original fixed-H definitions. ⊢ The q4 gate only concerns F containing the unique six-degree x and the five stated local/global conditions.

Rule and discharge: Actual target role verifies every hypothesis; no assumption deltaGamma≥4 is used inside this gate.

**U03-02 — Complete anchor calculation.** Context: the stated source hypotheses and U15-01, U15-02. ⊢ All four-exception marked trace multisets and all anchor failure sets are covered.

Rule and discharge: 26 trace types, repetitions allowed; S4 fixes x; full a0..30/r0..16 failures; exact x row repeat budget≤4.

**U03-03 — Five fixed certificates.** Context: the stated source hypotheses and U15-02, U15-03. ⊢ The complete necessary domain leaves40 labeled joint inputs /5 joint orbits; all five inventories retain35 edge indices.

Rule and discharge: Paircap includes the originalF; d(x)=1+a0+h0=6; nonnegative attachment compositions and exact degree limits.

**U03-04 — Conclusion.** Context: the stated source hypotheses and U02-04, U03-01, U03-02, U03-03. ⊢ Each remaining inventory gives originalH PropertyB by a strict zero-quota fixed permutation certificate.

Rule and discharge: Representative transport fixes x and moves positions; five-lock conditional criterion, max233003/240240.


### U04

Source: `context/propertyb35-paper/round01/middle/generic_c3_fourteen_gate_20261020/PROOF.md`

**U04-01 — §1.** Context: the stated source hypotheses and the original fixed-H definitions. ⊢ Valid middle implies cross exact trace, but cross exact trace need not be valid.

Rule and discharge: Outer singleton attachments are distinct and lie in opposite exclusive pairs; common3 points prohibited.

**U04-02 — §2.** Context: the stated source hypotheses and the original fixed-H definitions. ⊢ Exact cross14 allows q=0 and at most one triple, giving160+48=208 high-trace shapes.

Rule and discharge: Four inclusive cross caps sum16; a triple spends2; side traces≥1; all cross deficits explicitly exhausted.

**U04-03 — §2.** Context: the stated source hypotheses and U04-01, U04-02. ⊢ Actual selected degrees are7..13, total excess≤4; order8 side-marked transports preserve every condition.

Rule and discharge: Each cross row≥6 plus its side outer; degree recovery by subtraction; no hidden selected minimum degree.

**U04-04 — §1,3–4.** Context: the stated source hypotheses and U16-01, U16-02, U16-03. ⊢ All c≥14 cases are colorable, hence C3≤13n3 under the actual global role.

Rule and discharge: Complete exact14 7812/1144 strict certificates and the t15/16 1303/183 import, whose implementation only needs cross traces rather than actual c≥15.


### U05

Source: `context/propertyb35-paper/round01/middle/generic_high_degree_pair_gates_20261020/REPORT.md`

**U05-01 — §1–2.** Context: the stated source hypotheses and the original fixed-H definitions. ⊢ Two-lock inventory is unique for given21/35,d1,d2,c; complete118 high-pair inputs have110 strict certificates.

Rule and discharge: Möbius inclusion recovery and full degree/codegree range; zero quota; independent binomial/factorial replay.

**U05-02 — §3.** Context: the stated source hypotheses and U01-01. ⊢ Six ofeight numerical tails require more than global excess4, and the other two require A3 e=4.

Rule and discharge: For both high selected vertices, d1+d2−18≤e; no low/high pair is silently discarded.

**U05-03 — §4.** Context: the stated source hypotheses and U05-02. ⊢ Two A3 tails lift through the same unit x-star to exactlyfour triples and all are strict.

Rule and discharge: e4 implies b9 and all four x-row repetitions on degree8 points, so both high points unit; exact Ixyz∈{0,1}.

**U05-04 — §5–6.** Context: the stated source hypotheses and U05-01, U05-03. ⊢ Every actual pair has codegree≤4 in a non-B target H.

Rule and discharge: x-pair row excludes≥6; lambda5 link structure has compatibility177176>29*6006; all degree7..9 pairs lambda≥5 re-evaluated, including7/7; other pairs use complete high domain.


### U06

Source: `context/propertyb35-paper/round01/middle/generic_quad_core_multiplicity_three_20261020/PROOF.md`

**U06-01 — §1–2.** Context: the stated source hypotheses and U05-04. ⊢ Every avoiding-x four-core of multiplicity≥3 maps to q3/q4 shapes and the complete6923/3809 marked degree domain.

Rule and discharge: Core paircaps forceq≤4;97 shapes; star coverage17 gives exact necessary capacity; all86 sorted degree spectra and true stabilizers.

**U06-02 — §3.** Context: the stated source hypotheses and the original fixed-H definitions. ⊢ 3805/3809 representatives are strict; nine nested-quota calculations correctly charge actual bad pairs.

Rule and discharge: Pure bad-pair subset of total; minimal nonnegative weighted union selected without double spending; source weights sum both orientations.

**U06-03 — §3–4.** Context: the stated source hypotheses and U06-01, U06-02. ⊢ The four remaining10^4 inventories lift via one unit x-star to exactly23 five-lock inputs, all strict.

Rule and discharge: Bell4 partitions; each K point belongs to exactlyone x-edge; residual empty budget6−blocks and all35 indices preserved.

**U06-04 — §5.** Context: the stated source hypotheses and U01-01, U06-03. ⊢ Every non-B target H satisfies the four-core conclusion, including the four exceptions.

Rule and discharge: A2 e≤2 excludes10^4; A3 e4 exhausts x repetition on four degree8 vertices, giving lambda(x,K)=1.

**U06-05 — §7.** Context: the stated source hypotheses and U07-03. ⊢ Same-sample star plus generic rank≥11 gives n4(H−x)≤6.

Rule and discharge: 20<25 and29>20; incidence Gram positive definite factor; forest extension4→11→28; exact Hunter deduction9306 yields margin28.

**U06-06 — §7.** Context: the stated source hypotheses and U06-04, U06-05. ⊢ n4≤6+6+1=13.

Rule and discharge: Each ofsix cross-star four-intersections has at mostone partner by actual four-core theorem; two star-internal pairs of3-link intersections would consume repetition cost≥6>4.


### U07

Source: `context/propertyb35-paper/round01/middle/generic_degree_six_star_count_20261020/PROOF.md`

**U07-01 — §1.** Context: the stated source hypotheses and the original fixed-H definitions. ⊢ All simple six4-stars covering20 points are represented by the five cost4 multiplicity partitions.

Rule and discharge: Excess4; repeated supports may repeat; only15 fourfold-parallel duplicate stars excluded; all5886 keys.

**U07-02 — §2–4.** Context: the stated source hypotheses and U07-01. ⊢ True S6 orbits and two exact inclusion-exclusion forms give minimumC=164896.

Rule and discharge: Finite balanced10/10 sample; conflicting red/blue supports havezero count; complete41 orbit cover and independent IE replay.

**U07-03 — Actual caller.** Context: the stated source hypotheses and U07-01, U07-02. ⊢ Every selected degree6 x in targetH produces such a star, and compatible properHbar coloring extends toH.

Rule and discharge: Simple original edges give distinctlinks; paircover gives union20; choose x color having no monochromaticlink.


### U08

Source: `context/propertyb35-paper/round01/middle/a2_a3_joint_moment_frontier_20261020/CAPACITY_LEMMAS.md`

**U08-01 — Two-intersection capacity.** Context: the stated source hypotheses and U01-01. ⊢ C2≤floor((S6−6)/2)n2=(24+floor(e/2))n2.

Rule and discharge: Each middle charges exactlytwo distinct exclusive attachments; at least8 degree≥9 points and at most4 above9 put all excess in top6.

**U08-02 — Singleton capacity.** Context: the stated source hypotheses and the original fixed-H definitions. ⊢ C1≤35n1−Kd(n1).

Rule and discharge: A middle avoids the unique commonouterpoint; actual tv feasible under C(dv,2); cheapest-capacity filling minimizes degree cost.


### U09

Source: `proofs/propertyb35/GLOBAL_TWO_FLIP_SHARED_MIDDLE.md`

**U09-01 — §1.** Context: the stated source hypotheses and the original fixed-H definitions. ⊢ P=sumCj=sumF sumg<h tFg*tFh and sumF sF=2n1 exactly.

Rule and discharge: Every unorderedouter/middle flag has unique two groups; ordered paths counted twice only in EZ.

**U09-02 — §2.** Context: the stated source hypotheses and the original fixed-H definitions. ⊢ Balanced five attachment groups maximize wedge countf(s); f is discrete convex.

Rule and discharge: Moving groupmass toward balance lowers square sum; difference s−floor(s/5).

**U09-03 — §3–5 and nonthreshold part§6.** Context: the stated source hypotheses and the original fixed-H definitions. ⊢ Additional A1 inequalities are conditional on their explicitly narrower roles and are not transferred into A2/A3.

Rule and discharge: Checked algebra, distinct A1 unit relations, n4 import and price inequality; thresholdgraph/DP appendix explicitly excluded from targetdependency.


### U10

Source: `proofs/propertyb35/GLOBAL_TWO_FLIP_PATH_REPAIR.md`

**U10-01 — §1–2.** Context: the stated source hypotheses and the original fixed-H definitions. ⊢ Every failed two-flip trial produces a counted ordered path and the failure indicator bound is valid.

Rule and discharge: Initially unique badedge; m_g=1 eliminates new opposite-color badedge; differentg/h yield distincttriples.

**U10-02 — §2–3.** Context: the stated source hypotheses and U10-01. ⊢ EX,ES,EZ yield original coloring when expectationcriterion is strict.

Rule and discharge: Finite sample; EX=Mp, ES=2n1q, EZ=2sumCjrj; u≥(2k−S)+ and no independence.

**U10-03 — §3–4.** Context: the stated source hypotheses and U10-02. ⊢ Atn21,k5,M35,a10, pathnumerators are36,120,330,792,1716 and threshold2722720.

Rule and discharge: Explicit binomial counts recomputed; general exactC criterion does not requireDelta≤9.

**U10-04 — Main interface.** Context: the stated source hypotheses and U10-03. ⊢ 3432n1+(sumwjCj)/2<2722720 implies originalPropertyB.

Rule and discharge: Substitute exact probabilities in generalcriterion; actualC dominated by common-budget relaxation.


### U11

Source: `proofs/propertyb35/GLOBAL_PRIVATE_PAIR_REPAIR.md`

**U11-01 — §1–2.** Context: the stated source hypotheses and the original fixed-H definitions. ⊢ One-flip failure is bounded by X/2+S/(2k).

Rule and discharge: A newly badedge meets unique badG exactly at flippedvertex; witnesscounts for differentvertices distinct.

**U11-02 — §3–4.** Context: the stated source hypotheses and U11-01. ⊢ Every non-B21/35simple5 H has n1≥397.

Rule and discharge: Finite balancedsubset sample; exact rational threshold1190/3; integerceiling.

**U11-03 — §5.** Context: the stated source hypotheses and the original fixed-H definitions. ⊢ All paircover intersectionmoment identities are exact.

Rule and discharge: Simple5 excludes edgeintersection5; 350 pointpairincidences cover210 pointpairs; no coloringassumption in the equalities.


### U12

Source: `context/propertyb35-paper/round01/twentyone-high/unique6_with7/new_structure_20261020/SIX_UNIT8_POOL_PROOF.md`

**U12-01 — Dependency scope.** Context: the stated source hypotheses and the original fixed-H definitions. ⊢ Six-unit8 theorem has no hidden no-seven or outsider-minimumdegree assumption.

Rule and discharge: Read old local recovery, three/four/five/six generators, fixed/joint verifier interfaces; selected degrees only. Full older certificate catalogue remains declaredimport.

**U12-02 — §1.** Context: the stated source hypotheses and U12-01. ⊢ Six-neighbor center partition is3+3 or matching;3+3 violates a noncenterdegree7 count.

Rule and discharge: Every5-view in old26 residuals; same-block triple fully consumedbyx; pairincidences8 require≥8 noncenteredges, butdegree is7.

**U12-03 — §2.** Context: the stated source hypotheses and U12-01. ⊢ Neighbor codegree1 graph is empty orK1,5; emptycase is old complete270/3 strict import.

Rule and discharge: Every induced5-graph emptyorK1,4; overlapping5-sets force a unique globalstarcenter.

**U12-04 — §3–4.** Context: the stated source hypotheses and U12-01, U12-02, U12-03. ⊢ Starcase has no compatible six-view realization.

Rule and discharge: All S5 labels reconstructed from old26; full shared-containing-count join153→999→898→207→15→0 re-executed; sameH makes every overlap identical.


### U13

Source: `context/propertyb35-paper/round01/middle/a2_a3_min4_cap13_closure_20261020/NO_CRITICAL_FILTER.py`, `context/propertyb35-paper/round01/middle/a2_a3_min4_cap13_closure_20261020/NO_CRITICAL_CHECK.py`

**U13-01 — Both source algorithms.** Context: the stated source hypotheses and U01-02, U01-04. ⊢ Both implementations generate the complete16 degreespectra and necessary integerdomain.

Rule and discharge: Primarytau,t,m enumeration and independentn1,t,m parity recovery; upperbounds fromn2≥0; no saved survivorlist used to generate domain.

**U13-02 — Box and costs.** Context: the stated source hypotheses and U01-05, U01-06. ⊢ All1051 deficit states equal independent35-slot knapsack; degree-layer costs and greedyallocation verified.

Rule and discharge: Cap30 and atmostone interiorbox; no criticalityorT in newP; n4≤13 makes retained oldwedgefilter identicallyzero.

**U13-03 — All admissible maxima.** Context: the stated source hypotheses and U13-01, U13-02. ⊢ Four A2 maximalL values2713872,2718744,2719626,2716860 are below threshold.

Rule and discharge: All currentdomainkeys evaluated, notjust storedtails; eachspectrum maxchecked by second generation.

**U13-04 — Survivors/binding.** Context: the stated source hypotheses and U13-01, U13-02. ⊢ Fresh202 and33 outputkeys/distributions match declarednew files; E70/71/72 counts24/7/2.

Rule and discharge: Additional exact rebinding because suppliedchecker compares historical202/33 files; this is execution bookkeeping, not a mathematicalgap.


### U14

Source: `context/propertyb35-paper/round01/middle/three_nonunit_direct_repair_20261020/VERIFY_ASSEMBLY.py`

**U14-01 — Prefixes/orbits.** Context: the stated source hypotheses and U02-02. ⊢ All35 prefixcertificates are strict with correctslopes; S5 images disjoint and cover3276 inputs.

Rule and discharge: Fullcode and execution; no unsupportedmonotonefailuretail.

**U14-02 — Attachments.** Context: the stated source hypotheses and U14-01. ⊢ All119 generic and83 actualnecessary keys reconstructed.

Rule and discharge: Thresholddeltas sum≤3; completeall-r/v failurecheck; min6, unique6, totalexcess≤4 only.

**U14-03 — Fixed replays.** Context: the stated source hypotheses and U02-04, U14-02. ⊢ 79 five-lock and47 six-lock certificates retain35 indices,1190 orderedpairs,21 rows.

Rule and discharge: Reconstruction and everyrow exact; maximum139/143 and428/429; direct47-key equality.


### U15

Source: `context/propertyb35-paper/round01/middle/four_nonunit_degree_six_center_20261020/VERIFY.py`, `context/propertyb35-paper/round01/middle/four_nonunit_degree_six_center_20261020/INDEPENDENT_VERIFY.py`, `context/propertyb35-paper/round01/middle/four_nonunit_degree_six_center_20261020/FIVE_LOCK_FULL5.py`

**U15-01 — VERIFY.py.** Context: the stated source hypotheses and U03-01. ⊢ All23751 labeled four-exception inputs and1563 markedorbits evaluated with all70 fullfailuresets.

Rule and discharge: S4 fixesx, paircodegree/excess/degree constraints necessary; attachmentchoices include allfailures notjust prefix.

**U15-02 — INDEPENDENT_VERIFY.py.** Context: the stated source hypotheses and U15-01. ⊢ Different labeled signature/complement-binomial generation gives40 labeledassignments and5 jointorbits.

Rule and discharge: Fulljoint trace/attachmenttransport and all70 failuretables agree.

**U15-03 — FIVE_LOCK_FULL5.py.** Context: the stated source hypotheses and U02-04, U15-02. ⊢ All5 fullinventories have strict fixedcertificate.

Rule and discharge: Sixteen fixedpositions; zeropairquotas; independentexpanded35-index105-row replay.


### U16

Source: `context/propertyb35-paper/round01/middle/generic_c3_fourteen_gate_20261020/VERIFY.py`

**U16-01 — Domain.** Context: the stated source hypotheses and U04-02. ⊢ Independent inclusive-pair/degree enumeration regenerates all7812 exactcross14 keys.

Rule and discharge: Möbius recovery includingone-triple correction; no negativeinventory; sides≥1; e≤4.

**U16-02 — Marked transport.** Context: the stated source hypotheses and U16-01. ⊢ Eight side flips/swaps give exactly1144 representativekeys.

Rule and discharge: Allcounts movedtogether; actualH relabeling not presumedautomorphism.

**U16-03 — Certificates.** Context: the stated source hypotheses and U02-04, U16-02. ⊢ All1144 zerodeduction bounds strict, maximum34904/36465.

Rule and discharge: 35 originalindices and1190 orderedpairs each; exact independentinjections.


The mechanically checked obligation DAG has 64 nodes and no directed cycle. The semantic review separately checked that all role/finite-input assertions used here precede the conclusion and none depends on A2/A3 colorability.
