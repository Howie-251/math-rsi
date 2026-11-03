# D1_MATCH C4 and triangle-status delta audit

**Verdict: PASS25, zero open issues.** This extends the previously completed PASS36 by checking two stable additions:

- `proofs/dd82/n62/D1_MATCH_C4_TRANSPORT_REFINEMENT.md`, all 116 lines.
- `proofs/dd82/n62/D1_MATCH_INTERNAL_EDGE_TRIANGLE_FREE.md`, all 35 lines, including the completed C4 corollary.

The prior hard-branch reduction is reused as an inspected dependency. No source was edited. The requested reviewer is `gpt-6-astra`, effort `ultra`; actual backend identity remains unattested. Review independence is `same-family` and semantic acceptance is `provisional`. This is an incremental review by `/root/proof_review_n62_d1_reduction`, not a new cross-family judgment.

The deductions concern an actual order-62 graph with the normalized hard D1 parent structure and actual B=A²+A−7I−J. They do not exclude D1_MATCH, prove evenness of heavy edges in its repeat component, or establish an order-62 upper bound.

## Assumptions and dependency closure

All notation is inherited from the PASS36 reduction. The named b and c are triangle-free because B2b=B3c=1 and labels 2,3 are triangle-free; the universal triangle-pairing theorem preserves triangle status along every positive B entry. The labels 1,2,3,4 are triangle-free, hence each of C1,C2,C3,C4 is independent in the original graph. Independence of an original class and absence of internal repeats are different assertions throughout.

The C4 refinement uses only the base reduction and actual commutation. Its no-unit-B-triangle argument for r reroots the same original graph and reapplies the already proved argument for a. The base proof supplies every rerooted D1 hypothesis; no later internal-edge triangle-freeness assertion is used. The second document uses the refinement's saturated rows plus the previously inspected triangle-pairing theorem. This dependency graph is acyclic.

Every newly introduced symbol is an actual vertex or finite set of vertices. The vertices f,g are distinct unit endpoints of row 4. The vertices y_i,z_i are actual repeat mates of v_i in the specified classes, with z_i=a in the exceptional case v_i=p. The C4 endpoints x_i, their H-mates h_i, and their remaining unit endpoints k_i are local to the corollary. Counts d_Cj(v) are original-graph degrees into C_j; they are not repeat-weight sums. All quantification is finite and pointwise; there are no asymptotics or analytic interchanges.

## Obligation ledger

Every obligation below is discharged. Source locations R refer to the C4 refinement; T to the internal-edge triangle-freeness note.

| ID | Location | Checked implication and decisive justification |
|---|---|---|
| D01 | R7–25 | All inherited rows, locations and triangle statuses apply to the same actual graph; b,c obtain triangle-freeness through their positive repeats to labels 2,3. |
| D02 | R29 | The two unspent units of row 4 have ordinary endpoints: all other X entries and entries to 0,w,a vanish by the base rows. |
| D03 | R31–44 | At (4,a), AB=2 and BA=1+B_4,U, so exactly one residual unit is in U. Integrality excludes a single double endpoint, giving distinct unit endpoints f∈U and g∉U. The root equation forces g∈W. |
| D04 | R46 | g≠W4 because 4 is triangle-free; f≠c because every U point has total X-repeat weight one and c already uses its unit at label 3. No unsupported claim b≠g is made. |
| D05 | R48–56 | (2,4) gives B_4,C2=[b=W4]; only f could be in C2, at u2. Thus f=u2 iff b=W4. The (3,4) entry gives B_4,C3=0 and f≠u3. |
| D06 | R60–62 | B4c=0, A4c=0 and c adjacent a imply CN(4,c)={a}. Since N(4)={0,a}∪C4, c has no C4-neighbor. |
| D07 | R64–68 | The base transport formula at targets y∈C4 gives B_C3,y=A_cy=0. Nonnegativity kills the entire C3–C4 repeat block, including Bpq. |
| D08 | R70 | CN(4,x)=1 on C3 and CN(3,y)=1 on C4 give original degrees 1−[x=u3] and 1−[y=W4]. Thus the original cross edges form the stated five-edge matching. |
| D09 | R74–76 | Expand (4,y): BA=[y∈C1]+A_fy+A_gy; AB=[y=p]+[y=q]+B_C4,y. This proves (5) for every ordinary target, including q. |
| D10 | R78 | The nonedges 4f and 4g each have two common neighbors. f shares a with 4 and has one C4-neighbor; g shares neither 0 nor a and has two C4-neighbors. |
| D11 | R80–82 | Summing (5) on C4 gives total internal B weight 1+2−1=2. Symmetry, zero diagonal and nonnegative integrality force exactly one unordered unit edge. The q row additionally requires A_fq+A_gq≥1. |
| D12 | R86–90 | Each v_i has three distinct unit endpoints: internal mate v_j, C2 mate y_i, and its H mate or a if v_i=p. The three locations are disjoint and exhaust its row. The p case has no missing unit. |
| D13 | R92–97 | (a,v_i) yields A_pvi+A_qvi=A_avj+A_ayi+A_azi. C3 independence kills A_pvi; v_j≠u3 and z_i∈H∪{a} kill the other two terms, giving A_qvi=[y_i=u2]. |
| D14 | R92–97 | (r,v_i) yields A_wvi+A_svi+A_tvi=A_rvj+A_ryi+A_rzi. The base endpoint exclusions and independent C2,C3 kill all terms except A_tvi and A_rzi, giving the second equation (7), also when z_i=a. |
| D15 | R101 | Row a has support {0,p,q}; B0p=B0q=Bpq=0. Therefore no support triangle, in particular no unit B triangle, contains a. |
| D16 | R103 | The base persistent-reroot theorem applies at w, with new light mate r. Reapplying D15 in that representation proves the same statement for r. This uses neither D1 exclusion nor a universal claim about all unit-repeat vertices. |
| D17 | R107–110 | Sum AB−BA over C2×C3. The H terms cancel, original labels and 0,w contribute zero, a contributes one, and the sole internal C3 edge contributes two. The remaining D block is exactly the two sums in (8). |
| D18 | R112 | c has exactly three original neighbors in D, of which exactly one lies in W. b is not among them, since b,c are distinct neighbors of triangle-free r. Each such d has d_C2(d)=1−[d∈W], so the first sum in (8) is two. |
| D19 | R114 | b has exactly five D-neighbors and none is in W, since b∈W and w is triangle-free. None equals c. The label-3 common-neighbor equation gives d_C3(d)=1 for each, so the second sum is five and (8) is 3+2−5=0. |
| D20 | T11–13 | y1,y2 are distinct by the C2–C3 repeat matching. If v_i=p, its repeat to triangle-free a gives both internal C3 endpoints triangle-free immediately. |
| D21 | T15–19 | With neither endpoint p, z1,z2 are distinct H points. If the v_i bear triangles, their nonadjacent positive repeat makes them paired-triangle external mates. Their other row entries are exactly their triangle partners. B[C2]=B[H]=0 forces the crossed external pairing, which gives y1 two distinct unit repeats into H, contradicting the deficient matching. |
| D22 | T25 | If q is an internal C4 endpoint, its positive repeat to a makes both endpoints triangle-free. |
| D23 | T27–29 | Otherwise each C4 endpoint has one distinct H-mate h_i, with h1≠h2. The internal edge and H matching have exact weight one each, so row sum three leaves one different unit endpoint k_i, not a doubled known entry. |
| D24 | T31–33 | If the C4 endpoints bear triangles, their nonadjacent repeat makes them paired-triangle external mates. B[H]=0 forces cross pairing between h and k, giving k1 two distinct positive repeat neighbors in H. Globally every vertex has at most one: H's whole support is its three deficient matchings into C2,C3,C4. Contradiction. |
| D25 | R105–116; T21,35 | The stated conclusions stay local. The aggregate identity is consistent, and neither document infers global triangle-freeness, a D1 contradiction, or heavy-edge parity from these facts. |

## Aggregate identity independently expanded

Write d_j(z)=sum_{x∈Cj}A_xz and beta_j(z)=sum_{x∈Cj}B_xz. Summing the C2×C3 block gives

    0 = sum_z (d_2(z) beta_3(z) − beta_2(z) d_3(z)).

This finite rearrangement needs no additional hypotheses. The contributions are:

- z∈{0}∪X∪{w}: zero, using the complete root/label rows and singleton parents.
- z=a: 1·1−0·1=1.
- z∈H: 1·1−1·1=0 pointwise.
- z∈C2: zero because both its original and repeat internal degrees are zero.
- z∈C3: two in total, because its original C2-degree is one and internal repeat weight totals two, while its original internal degree is zero.
- z∈D: beta_3(z)=A_cz and beta_2(z)=A_bz, giving exactly the two displayed sums in (8).

Thus the constant three in (8) has the correct sign and multiplicity. For the evaluation, the only exceptional label-2 target in D would be b and the only exceptional label-3 target would be c. The proved nonedge bc excludes each from the relevant sum. The claimed values two and five therefore use exact common-neighbor equations without suppressing exceptional terms.

## Counterexample and exceptional-case pass

No counterexample was found. The following potentially consequential degeneracies were checked explicitly:

- A doubled residual entry in row 4 cannot place exactly one residual unit on U. The f,g split is therefore justified before their neighborhoods are used.
- b=g and b=W4 are not silently rejected. The latter is exactly the allowed f=u2 case; g≠W4 then follows independently. The implications used later remain valid in both branches.
- f=u3 or f=c would violate the proved label-3 or total X-repeat restriction. These exclusions do not assume every U vertex is triangle-free.
- p may equal one of v1,v2; its missing H repeat is replaced by its known a repeat. The complete row (6), both identities (7), and the triangle-freeness proof cover this case explicitly.
- z_i=a makes A_rzi=0 because ar is a proved nonedge. No distinct H-mate is demanded in this exceptional case.
- The sole internal C4 edge may contain q. Its triangle-free status is handled before the generic h_i,k_i construction.
- In the generic C4 case, the remaining repeat cannot double either the internal edge or the H edge, whose weights are already exactly one. Under a hypothetical original triangle, the triangle-pairing theorem itself makes the paired triangles disjoint; it supplies the distinctness needed for the two mate-bijection possibilities.
- Replacing the triangle-pairing theorem by triangle-count parity would not prove the endpoint claims. Both documents use the actual paired-triangle structure, including the external mate bijection and its saturated rows.
- Equation (8) is satisfied identically after the established local counts. It is not treated as a contradiction.

## Artifacts and remaining scope

No fixes were needed. This delta adds 25 discharged obligations to the prior 36, for 61 across these three local notes. The two delta artifacts and the existing state file record this result. No digests, TeX/PDF/HTML, SAT, finite-checker rerun, new axioms, or order63–65 work were used.

The supported new conclusions are the complete row at label 4, zero C3–C4 repeat block, one internal C4 unit edge, equations (5)–(8), absence of unit B triangles at the two light mates, and triangle-free original status of both internal C3 and C4 repeat-edge endpoints. The hard D1 branch remains open.
