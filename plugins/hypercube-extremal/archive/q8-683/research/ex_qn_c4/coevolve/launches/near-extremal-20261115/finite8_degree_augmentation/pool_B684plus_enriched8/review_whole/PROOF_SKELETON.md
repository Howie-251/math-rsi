# Proof skeleton for the frozen upper683 theorem

The original682 goal remains OPEN. This is an acyclic finite proof on one actual maximal graph.

## Typed symbols and exact domains

- `Q_n`: fixed finite labelled n-dimensional cube;n=3,4,6,8 only.
- `G`: arbitrary C4-free spanning subgraph of Q8.
- `H`: ordinary inclusion-maximal C4-free supergraph of G.
- `m`: integer e(H) in684..688 under contradiction hypothesis.
- `n_d(P)`: nonnegative integer degree-d count on one actual parity, sum128,degree sum m,n0=0.
- `S_F,c_F,L_F`: integer specified-parity cubic star sum,full count,low<=2 count on actual Q6.
- `C_d,b_d`: fixed nonnegative integer coefficient lists of length9.
- `lambda`: probability measure on all1120 actual Q4 restrictions of one H.
- `alpha`: half each of two actual parity-profile point masses on645 cover.
- `beta`: probability measure on1024 ambient edge observations,aggregated into1751 endpoint orbits.
- `eta_d,N_d`: expected alpha parity count and global H degree count;N_d=2eta_d.
- `x`: in linear systems: concatenated nonnegative(lambda,alpha,beta);at one root: explicitly typed histogram with total6/7/28 according to context.
- `c_i(K)`: nonnegative integer folded upper coefficients;face and vertex group sums64512.
- `h_j(K)`: nonnegative integer local degree histogram,5 coordinates,sum16.
- `Q,Qbar`: symmetric kernel and its common-root stabilizer average;positivity only when specifically proved.
- `E,b,A,g`: 356 equality matrix,RHS b0=b1=1,selected inequality matrix A=-g,g>=0.
- `y,z,Dy`: integer dual coefficients,356/8051 lengths,z<=0,Dy=10^9.
- `D,NW,NH`: positive common exact denominator551690954352885760000000000 and integer packed/hist numerators.
- `q,qh,T`: nearest-integer oracle query coefficients and positive scale10^9;distinct from row-specific q vectors.
- `delta,Amax,Bmax,eps,M`: fixed exact rational constants in CHECKS.json,not asymptotic or empirical estimates.

## Dependency DAG and micro-claim inventory

Every item below is a sequent: the listed earlier dependencies plus the explicitly discharged hypotheses imply the stated goal. All are DISCHARGED. No limiting operations occur.

### D01 (definition)

Context: fixed definitions / supplied finite data.

Goal: G ranges over all C4-free spanning edge subgraphs of the fixed labelled Q8.

Rule: original object. Source: B01.

Hypotheses verified: Spanning does not impose positive original degree.

### L01 (lemma)

Context: D01.

Goal: For every such G with e(G)>=684, there exists an ordinary inclusion-maximal C4-free H containing G, m=e(H)>=684.

Rule: finite maximal extension. Source: B01.

Hypotheses verified: Only ambient edge additions preserving C4-freeness; finiteness of1024 edges.

### L02 (lemma)

Context: L01.

Goal: Every ordinary inclusion-maximal C4-free H in Q8 has no isolated vertex.

Rule: safe edge addition. Source: B01.

Hypotheses verified: Any added edge at an isolated vertex cannot complete a cycle.

### C01 (finite-certificate)

Context: fixed definitions / supplied finite data.

Goal: All25 CNFs encode the reviewed finite Q6 counterexample cases and have strict RUP derivations of empty;4383882 additions. 

Rule: complete geometric/Boolean reconstruction and previously completed real exact replay. Source: I03/I04;FRESH_REPLAYS.json.

Hypotheses verified: Both parity choices normalized by one whole isometry; arbitrary opposite degrees; actual input/trace/source/binary hashes rebound here; ordinary audited checker trust boundary explicit.

### L03 (lemma)

Context: C01.

Goal: For every C4-free Q6 and either fixed parity P, 4 sum_P C(d,3)+2 #{d=6} <=632+5 #{d<=2}.

Rule: finite cover, analytic low-root replacements and residue table. Source: I03.

Hypotheses verified: All0/1/2 specified degrees; no opposite minimum degree; six min3 cases,17 one-low2 cases,two four-full inputs,analytic degree1/0 and three-full slots.

### L04 (lemma)

Context: L01, L03.

Goal: For every H and either actual parity P, sum C_d n_d(P)<=138432-201m; hence m<=688.

Rule: sum112 actual Q6 face inequalities. Source: B01/I01.

Hypotheses verified: Same global parity inherited on each face; multiplicities10 and C(d,6); low l_d exact; all C_d>=0; two degree sums.

### L05 (lemma)

Context: D01.

Goal: For every C4-free H and either actual parity P, sum b_d n_d(P)<=6912-10m.

Rule: Q3 full-star injection. Source: B01/I01.

Hypotheses verified: Any two distinct same-parity Q3 roots distance2; both full stars force their square;1792 Q3 faces.

### L06 (finite-cover)

Context: L02, L04, L05.

Goal: Every parity profile of an H with m>=684 lies in the frozen645 row cover, at its same m in{684,...,688}.

Rule: independent complete nonnegative integer enumeration. Source: B01;CHECKS.json.

Hypotheses verified: Positive C budget bounds n1,n2,n3,n4,n7,n8; n5,n6 uniquely solved; no additional683 filters; exact row set and counts385/170/66/20/4.

### D02 (definition)

Context: L01, L06.

Goal: For each fixed H, lambda is uniform on1120 actual Q4 restrictions, alpha is half each actual parity profile, eta_d=N_d/2, beta is empirical over1024 ambient edges.

Rule: three pushforwards of one H. Source: B02.

Hypotheses verified: All three measures nonnegative and mass1; no root-type conditional normalization.

### L07 (lemma)

Context: L01.

Goal: Every actual missing-root histogram has x7>=1; every retained-root histogram excludes state7.

Rule: ordinary maximality and coordinate-square characterization. Source: B02/I01.

Hypotheses verified: Any C4 through an added edge is its square with one other axis; seven external directions.

### L08 (lemma)

Context: L01.

Goal: Every leaf is joined to a distinct degree8 vertex; its retained-root histogram is pure5 or pure6 under endpoint orientation.

Rule: maximal leaf closure and injection. Source: B02/B04/I12.

Hypotheses verified: Only retained direction at a leaf must be the direction of every completing square; two leaves sharing a neighbor contradict closure.

### L09 (finite-cover)

Context: L07, L08.

Goal: All actual beta observations map to the frozen1751 columns; these are exactly endpoint-flip orbits of3202 allowed raw histograms.

Rule: independent full lexicographic histogram and orbit enumeration. Source: B02;CHECKS.json.

Hypotheses verified: 1716 missing,1486 retained; each raw row once; common flip preserves every later observable, no class-size multiplier.

### L10 (sampling-identity)

Context: D02.

Goal: For every actual H and every symmetric face kernel Q, E_lambda T_Q = average_actual_roots x^T Qbar x/36, with full-state x>=0 integer,total6.

Rule: exact with-replacement collision identity. Source: B03/I06.

Hypotheses verified: Uniform two of six external directions;1120*24=1792*15; simultaneous root gauge; both face coefficients nonnegative and total64512.

### L11 (sampling-identity)

Context: D02.

Goal: For every actual H and symmetric9x9 Q, E_lambda T_Q=E_vertex x^TQx/784, with actual square-state x,total28.

Rule: overlap-category finite sampling. Source: B03/I06.

Hypotheses verified: Among28 pairs:15 disjoint,12 overlap,1 equal; completion multiplicities1,5,15; local weights720,144,24; vertex coefficient mass64512.

### L12 (equality)

Context: D02.

Goal: Rows0..6 hold on actual(lambda,alpha): both masses1 and five hypergeometric degree marginals.

Rule: uniform vertex/four-axis count. Source: B03.

Hypotheses verified: 128*C(8,4)=8960; local histogram/16; no fixed683 assumption.

### L13 (equality)

Context: D02, L10.

Goal: Rows7..70 equate the64 true-upper edge moments U/129024 to Gnum beta/98.

Rule: edge sampling and exact face pullback. Source: B03/I07.

Hypotheses verified: Unbiased local kernel(3zzT-2diag z)/21; global x/7; true-upper multiplier diagonal2y offdiag y; raw lift392 and extra1/2 give784.

### L14 (equality)

Context: D02.

Goal: Rows71..88 hold: EP beta=RHS alpha/512.

Rule: count all ambient endpoint incidences. Source: B03.

Hypotheses verified: Endpoint degrees r+bit sums; N_d=2eta_d; retained degree d or missing degree8-d.

### L15 (equality)

Context: D02.

Goal: Rows89..124: all36 mixed-state retained-minus-missing balances vanish.

Rule: one mixed square offers one retained and one missing root. Source: B03/I08.

Hypotheses verified: Same H and degree at marked endpoint; row scaling1/7 positive.

### L16 (equality)

Context: D02, L11.

Goal: Rows125..151:2304 B beta=7 W F_vertex^T lambda.

Rule: same-vertex group second-moment double count. Source: B03/I08.

Hypotheses verified: Group totals F0,F1,F2; C incidence first moment factor1/2;392; folded W diagonal2/off1; stored lambda7WF/129024,beta-B/56.

### L17 (equality)

Context: D02, L10.

Goal: Rows152..355: E_lambda L_z/64=E_beta H_z/70 for all204 triple histograms, and L_z/64=T_Kz/80.

Rule: actual occurrence bijection and collision cancellation. Source: B03/I09/I10.

Hypotheses verified: Both orientations;32 local/1024 global ambient edges;35 external triples; A symmetric and common-root invariant; K=12A-diag A_i-diag A_j.

### L18 (equality-system)

Context: L12, L13, L14, L15, L16, L17.

Goal: Every actual x=(lambda,alpha,beta) satisfies Ex=b, with exactly b0=b1=1 nonzero.

Rule: combine all356 actual scientific equations. Source: B03.

Hypotheses verified: All families refer to the same H and same root transport.

### L19 (inequality)

Context: L10.

Goal: All19 active PSD-ray rows are nonnegative on every actual H.

Rule: q qT quadratic square. Source: B04.

Hypotheses verified: Actual q integer correct dimensions and blocks0..3; scales positive; common-root average preserves validity.

### L20 (inequality)

Context: L10.

Goal: All49 active integer-six rows are nonnegative on every actual H.

Rule: 36(L-t)(L-t-1)>=0 for integer L. Source: B04.

Hypotheses verified: All q,t integers;n=6;all nonnegative integer root counts total6; no n28 premise.

### L21 (inequality)

Context: D02.

Goal: For t in{1,2,3,7,8}, the five actual neighbor-capacity slacks are nonnegative.

Rule: distinct forced missing remote incidences. Source: B04.

Hypotheses verified: Every retained-direction pair forces one of two distinct remote incidence omissions; summing degree-t vertices;beta normalization1024,alpha N_t/2;positive division16.

### L22 (equality)

Context: L02, L11, D02.

Goal: The selected conditional195 row has expected value0 on every actual no-isolated H.

Rule: explicit81-entry matrix10^6(2ssT-J) and degree-group counts. Source: B04;CONDITIONAL195_ANALYTIC_IDENTITY.json.

Hypotheses verified: s=1 outside I0;S=28-C(8-d,2);actual B_d cancels xQx for d1..8;B0 unused because n0=0;alpha factor128*784.

### C02 (finite-certificate)

Context: fixed definitions / supplied finite data.

Goal: Each of the eight actual connector matrices is nonnegative on all54264 integer16-count histograms of total6.

Rule: previously completed independently reconstructed exact integer full-domain check. Source: 83 annex;independent_B8/INDEPENDENT_RESULT.json.

Hypotheses verified: Source hashes rebound;actual minima240,240,112,176,56,104,66,128;exact same matrices/scales as combination.

### L23 (inequality)

Context: L10, C02.

Goal: All eight selected full-state connector rows hold for every actual C4-free H.

Rule: all-full-state connector pullback. Source: B04/I11.

Hypotheses verified: Every legal flag uses connector code f&15;all six actual flags contribute;common root action preserves complete integer total6 domain;no PSD/copositivity/A-case premise.

### L24 (inequality-system)

Context: L08, D02, L19, L20, L21, L22, L23.

Goal: Every actual x satisfies the83 selected inequalities g(x)>=0, equivalently Ax<=0 for A=-g.

Rule: combine precisely nonzero-weight valid rows. Source: B04.

Hypotheses verified: Global leaf eta8-eta1>=0;no inactive finite projection,vertex28,683-only or joint-projection premise.

### C03 (exact-coefficients)

Context: fixed definitions / supplied finite data.

Goal: The actual integer arrays represent a=(yE+zA)/10^9 with101801 packed,5histogram,645alpha,1751beta coefficients over common D.

Rule: independent exact scientific reconstruction and parameter/array/hash agreement. Source: B05;exact combination;I15/I16/I17.

Hypotheses verified: All356 maps rebuilt from geometry; every active parameter source and positive scale bound; native floating maps used only diagnostic.

### L25 (lower-bound)

Context: L18, L24, C03.

Goal: Every actual x obeys a.x>=delta=92993/500000000.

Rule: z<=0 and A x<=0 imply zA x>=0. Source: B05.

Hypotheses verified: y unrestricted;b only0,1;all83 active z signs checked;no solver optimality or primal premise.

### L26 (uniform-bound)

Context: L10, L11, C03.

Goal: For every legal labelled Q4 K, |l(K)-lhat(K)|<=eps=529874002317/601295421440000000000.

Rule: groupwise triangle inequality on nonnegative coefficients. Source: B05.

Hypotheses verified: Face and vertex masses each64512;histogram mass16;exact nearest-integer rounding scale10^9;complete coefficients checked.

### L27 (invariance)

Context: L10, L11.

Goal: For any symmetric query matrices and degree-histogram coefficients, the synchronized finite-eight functional is invariant under every Q4 isometry.

Rule: common root stabilizer averaging and marked-vertex axis quotient. Source: I06/I13/I14.

Hypotheses verified: Both flags transported together;external swap symmetric;all faces/vertices and pair intersections permuted.

### C04 (finite-maximum)

Context: L27.

Goal: For this exact hash-bound final integer query, every legal Q4 has raw score<=-37440, and equality is attained.

Rule: complete ordered-Q3-layer-pair orbit cover and all allowed crossing independent sets. Source: B05;I13/I14;actual final B8 stdout.

Hypotheses verified: All2902 legal Q3;all8421604 ordered layer pairs;90179 common orbits;all crossing sets;13150453 marked completions;actual complete independent source-recompiled run;source/query hashes match;integer overflow bound checked.

### L28 (upper-bound)

Context: D02, L09, L06, L26, C04, C03.

Goal: For every actual x, a.x <= M+eps+Amax+Bmax, M=-13/22400000000.

Rule: three separate finite maxima and probability averaging. Source: B05/B06.

Hypotheses verified: Each measure mass1;full alpha/beta covers;exact positive Amax and Bmax allowed;no common maximizing graph required.

### T01 (theorem)

Context: L01, L04, L25, L28.

Goal: For every C4-free spanning edge subgraph G of Q8, e(G)<=683.

Rule: positive exact margin contradiction. Source: B06.

Hypotheses verified: delta-M-eps-Amax-Bmax=782808475930428709/4209067950080000000000>0;all m684..688 excluded;maximal extension may change edge count.

### S01 (scope)

Context: T01.

Goal: The separate theorem e(G)<=682 is not proved; m683 remains open.

Rule: exact statement-conclusion scope. Source: B06/B07.

Hypotheses verified: No claim beyond upper683 or graph realizability.

## Closure and counterexample pass

Topological order: D01, C01, C02, C03, L01, L03, L05, L02, L04, L07, L08, L06, L09, D02, L10, L11, L12, L14, L15, L21, L13, L16, L17, L19, L20, L22, L23, L26, L27, L18, L24, C04, L25, L28, T01, S01.

No cycle, open hypothesis, conditional import or repaired issue remains in the frozen upper683 submission. Counterexample/boundary attempts and the precise computation trust boundary are in the unabridged REVIEW.md. No author repair was necessary.
