# Audit of the seven-triangle nonzero-repeat budget

**Verdict: PASS, same-family / provisional.** All 38 recorded obligations are discharged in the reviewed paper and complete predecessor arguments. No fatal, critical, major, or minor issue was identified. No proof-source edit was needed. This is a paper review, with no claim of Lean verification or cross-family acceptance.

The fresh reviewer task is `/root/proof_review_seven_repeat_budget`. The local proof-checker skill supplies the requested reviewer target `gpt-6-astra` with reasoning `ultra`; actual backend/model/reasoning telemetry was not supplied to this worker and is not attested here. The explicit task's output restrictions override skill defaults for document formats, output location, hashes, additional reviewers, and wiki writes. Only Markdown/JSON ledgers were written in this directory.

## Reviewed statement and dependency coverage

The main file is `proofs/dd82/n59/seven_triangle_nonzero_repeat_budget_20261011.md`. The reviewer read its full content and all four full named mathematical predecessors: `zero_heavy_global_capacity_20261011.md`, `heavy_cross_repeat_slack_20261011.md`, `nonzero_support_transport_20261011.md`, and `matching_zero_global_trace_obstruction_20261011.md`. Prior review status text in these files did not substitute for checking their arguments.

The theorem assumes one original simple 59-vertex graph, maximum degree 8, diameter 2, and exact induced-support N15 at all zero-triangle vertices. Seven triangles on 21 nonzero vertices give seven disjoint original triangles and nonedge defect budget 4 at each nonzero root. The conclusions are necessary conditions only. No surviving configuration is asserted realizable, and neither the remaining N15 branch nor arbitrary legal order 59 is excluded.

## Exact slack and the weighted bound

Write H_ZZ for the heavy zero-zero count. Zero heavy incidences give 2|Z|=2H_ZZ+K. At a nonzero root n, the local double count is

    l_n + 2h_n + k_n + R_n = 6 − 2t(n).

Each pointwise summand of R_n is nonnegative, using q≤2. Summing and subtracting the heavy incidence identity gives exactly

    2(4m−3T−59) = sum_n l_n + 2(sum_n h_n−H_ZZ) + sum_n R_n.

For m=21,T=7 this is 8. Its three contributions are respectively l_1+2l_2, 2h_2+4h_3, and R_NN+R_NZ. In particular both orientations of each N-N nonedge are included exactly once in R_NN's factor 2; cross pairs occur only in their N-root orientation.

For the pair count P, a nonedge pair in N with exactly two zero common neighbors uniquely determines that zero pair. Conversely, a zero pair with i nonzero common neighbors determines binom(i,2) N-pairs, each nonadjacent because an original edge would produce a triangle through a zero. A zero pair with two or more such neighbors has positive defect; its light or heavy row bounds total common neighbors by 2 or 3. Hence

    P = l_2+h_2+3h_3,
    R_NN = 2(W−P).

Substitution produces precisely

    8 = 2W+l_1−2h_3+R_NZ.

There is no zero-support pairing premise in this calculation. Nonnegativity gives h_3≤2 and W≥3h_3. The separately proved injective heavy-cross charge gives K≤R_NZ. Thus 2W+K+l_1≤8+2h_3≤12 and W≤6. The W=0 predecessor excludes that endpoint while explicitly allowing isolated light zero supports.

## Predecessor checks that matter downstream

The common-zero-neighbor lemma does not assume all defect supports paired at nonzero roots. On any independent zero set each weight class is a matching by N15 at the zero endpoints. Three common zero neighbors would create a positive two-colored defect triangle on that independent set, which is impossible.

For support transport, exact induced N15 computes (BA)_{xr}=B_xr whenever x is zero and B_rx>0: the only positive row-x support neighbor of r is its equal-weight mate. Symmetry and AB=BA give sum_{y∼x}B_ry=B_rx. Nonnegativity then isolates every zero-zero support edge and forces its equal weights. An isolated zero support is allowed and receives exactly its own weight from an independent subset of the nonzero support. Partitioning support-edge contributions proves e_r=5+Q_N(r)−s_N(r)−K_r.

For heavy-cross charging, a heavy n,z with two zero common neighbors x,y has one nonzero common neighbor v. The induced cross pairs v,x and v,y are positive. If both were heavy, they would exhaust v's nonedge budget, force t(v)=1, and leave only a unit triangle edge as nonzero support. Transport of weight 2 at x would then force x∼y, contrary to their both being zero neighbors of n. At least one induced pair is light and contributes one slack unit. Its unique nonzero and zero common neighbors recover the source n,z; this proves injectivity, including separation from self-charged heavy terms.

In the W=0 consequence, the nonzero root row shapes are 22 and 1111; 211 fails transport. A 22 zero pair is paired, while a 1111 row can initially have 0, 1, or 2 paired zero edges. The proof's parameter b counts the omitted pairs and hence half the isolated light supports. These isolated light terms are disjoint from heavy charges: a charged light pair has common neighbors n,z, and n is not a triangle partner of its root, so transport makes it paired. Therefore a+b≤4. Fourth trace gives a even; fifth trace gives b≡2a mod5. Only a=b=0 survives these conditions, and it violates 84≤76 light cross incidence capacity. This predecessor does not silently pair 1111 rows.

The fourth trace follows from tr A4=126n+s−12T and the elementary closed-walk decomposition tr A4=120n+8C4 at degree 8. The fifth trace expansion gives tr A5=428n+w−2s+102T. Each non-simple five-step closed walk uses one uniquely determined triangle plus a two-step backtrack; each triangle contributes 30 internal walks and 18·10 exterior-backtrack walks. Thus tr A5=10C5+210T. Exact induced zero rows have s_v=10,Q2(v)=5, leading to 5C5=209·59+sum_{n∈N}e_n−54T and sum e_n+T≡4 mod5. These calculations apply with triangles and with chorded five-cycles.

## W=5: weights, isolated supports, and every AB/BA term

W=5 implies h_3=1 and l_1=R_NZ=K=0: the exact identity forces h_3≥1 while W≥3h_3 forces h_3≤1. A heavy zero pair with three nonzero common neighbors supplies a repeat triangle whose three edges have baseline weight one.

The square-sum identity is exact. The 38 zero rows contribute 380; the 21 nonzero row sums contribute 126; N-N nonedge excess contributes 2F and cross-heavy excess contributes 2K. Thus s=506+2F+2K. With K=0, 8C4=776+2F requires F≡0 mod4. The two additional weight units have exactly these possibilities:

| Distribution beyond the baseline unit triangle | F |
|---|---:|
| Both onto one triangle edge | 6 |
| One onto each of two triangle edges | 4 |
| One onto a triangle edge and one new unit edge | 2 |
| One new edge of weight two | 2 |
| Two distinct new unit edges | 0 |

Only the second and fifth rows survive the fourth trace.

In the second case use B_uv=B_uw=2,B_vw=1. The root u has no zero support. Each of v,w has exactly one light zero repeat x_v,x_w; singleton zero supports are isolated. R_NZ=0 excludes adjacency of x_v to any true nonzero neighbor of v, including its two triangle partners, because a light cross pair already has two zero common neighbors. Weight transport also excludes the weight-2 endpoint u. It therefore forces x_v∼w and x_v≁u; symmetrically x_w∼v and x_w≁u. Adjacency to a NONEDGE repeat endpoint is preserved, not prohibited.

Let T_u and T_v be the two original triangle partners of u and v. Then the full sums at (u,v) are

    (BA)_uv = sum_{a∈T_u} A_av + 2A_vv + 2A_wv = p_uv,
    (AB)_uv = sum_{b∈T_v} A_ub + 2A_uu + A_uw + A_ux_v = q_uv.

All displayed extra terms vanish by loops, original nonadjacency of repeat pairs, or the just-proved x_v≁u. There are no further positive row entries. The heavy pair u,v has exactly two zero common neighbors and one nonzero common neighbor. The sets counted by p_uv and q_uv are disjoint: a common vertex in both would belong to both original triangles, whereas t=1 makes them vertex-disjoint. Hence p_uv+q_uv≤1. Commutation yields equality and therefore p_uv=q_uv=0. The identical expansion at u,w gives the other vanishing terms.

For the light pair v,w the two zero common neighbors exhaust all common neighbors. This additionally removes triangle-partner-to-repeat edges in the rows at v,w. Therefore Q_N=1 at u,v,w, with nonzero row-square sums 10,7,7 and K_r=0. Their remainders are −4,−1,−1. All other 18 roots have only their two true triangle partners in nonzero support. Their four light zero repeats must pair, since an isolated one could receive no admissible nonzero support weight; each remainder is 2. The total is 30, contradicting 30+7≡4 mod5. The two-new-unit-edges case remains, exactly as claimed.

## W=6: equality and the two incidence cases

Equality forces h_3=2,l_1=R_NZ=K=0 and l_2=h_2=R_NN=0. The two distinct heavy zero pairs each supply a three-vertex repeat triangle. If these triangles shared two vertices, that N-pair would have at least three distinct zero common neighbors, because the two determining zero pairs are distinct. Therefore the triangles share at most one vertex and have six distinct edges. They exhaust weight W=6, so every edge is unit and there are no others. R_NN=0 gives two zero and no nonzero common neighbors on each repeat edge. Cross repeats are likewise light with two zero and no nonzero common neighbors.

A degree-0 repeat root has four light zero supports, all paired, and e=2. A degree-2 repeat root has two light zero supports. They are either an equal-weight support pair, or both isolated. Its nonzero support comprises its triangle partners and its two nonedge repeat endpoints; triangle-partner-to-repeat edges would violate absence of nonzero common neighbors, while the two repeat endpoints are originally nonadjacent. Thus Q_N=1,s_N=4 and e=1 or 2. Each isolated zero can be adjacent to exactly one of the two repeat endpoints. True triangle partners are excluded, but repeat endpoints remain available.

For two disjoint repeat triangles, let z be the third repeat vertex on an edge v,w. The full sums reduce to

    (BA)_vw = [triangle-partner sum, zero] + A_ww + A_zw + j_vw = j_vw,
    (AB)_vw = [triangle-partner sum, zero] + A_vv + A_vz + j_wv = j_wv.

The third-vertex terms vanish because repeat-triangle edges are nonedges of G. Paired zero supports have no neighbors elsewhere in positive support, so contribute nothing. Hence j_vw=j_wv. Row totals are either 0 or 2. A triangle with only one active vertex would have all its incident j values forced to zero by its inactive neighbors, a contradiction. Each triangle therefore has 0, 2, or 3 active vertices. The total remainder is 36+q, so q≡1 mod5 and 0≤q≤6. The sole possibilities are 1 and 6, and 1 is impossible. Thus all six are active. On each triangle, the three symmetric edge variables have pairwise sums 2, which uniquely forces all three variables to be 1.

For shared repeat triangles uab and ucd, u has four unit nonedge repeats and no zero repeats. Original edges between {a,b} and {c,d} form a matching: two at a would make a a nonzero common neighbor of c,d, and the other three cases are symmetric. Denote the matching size by c_0. Here Q_N(u)=1+c_0,s_N(u)=6, so e_u=c_0; the four outer roots contribute 4+q and the other 16 roots contribute 32. Hence sum e=36+c_0+q and c_0+q≡1 mod5.

At (a,u), every term can be written as

    (BA)_au = [partners of a, zero] + A_uu + A_bu + j_au = j_au,
    (AB)_au = [partners of u, zero] + A_aa + A_ab + A_ac + A_ad = c_a.

Triangle-partner sums vanish because a,u is a repeat edge without a nonzero common neighbor. The remaining zero terms are loops and repeat nonedges; root u has no zero support. Thus j_au=c_a. At the outer repeat edge a,b the only possible nonzero terms are j_ab and j_ba, giving their equality. Transport then gives

    2ε_a−c_a = j_ab = j_ba = 2ε_b−c_b.

Since c_a,c_b∈{0,1}, parity forces c_a=c_b and then ε_a=ε_b. Apply the same to c,d. A matching of size one violates these equalities. With c_0=0, q∈{0,2,4}, none satisfying q≡1 mod5. Therefore c_0=2. All four c_a-type quantities equal one, forcing all outer roots active. Each uses one isolated zero on the shared root and the other on its outer partner. This agrees with c_0+q=6≡1 mod5.

## Counterexample attempts and boundary checks

These were mathematical adversarial checks, not claims of graph existence or exhaustive graph enumeration.

- Three common zeros were tested against the weakened N15 premise. Their forced positive two-colored defect triangle already contradicts matching in one weight class; no full induced-support assumption was smuggled into that lemma.
- A heavy cross pair with two zero common neighbors was tested with both induced cross repeats heavy. Transport of weight 2 forces the forbidden zero-zero edge. The injectivity test recovers the heavy source uniquely from the light target's two common neighbors.
- W=0 with isolated light supports was retained using the full p_n∈{0,1,2} range. Their slack terms cannot coincide with charged paired light repeats. This confirms that the W≥1 import does not use a pairing shortcut.
- W=5 weight-three edges, a new weight-two edge, and mixed old/new additions were included explicitly in the five-case table. They fail the fourth trace; the remaining weighted triangle was checked with its two isolated zero supports present in AB/BA.
- W=6 with all zero supports paired, and with a single active vertex, was tested. The fifth trace and symmetric j equations exclude these assignments. The general local transport interface does allow isolated zeros to attach to NONEDGE repeat endpoints; the audit never deletes those admissible terms.
- A shared W=6 configuration with one outer matching edge fails parity. Matching size zero was tested at all possible even active counts and fails the fifth trace. Matching size two with all four outer roots active survives the stated local equations and is left as a necessary configuration, not rejected or promoted to an original graph.
- Every possible original triangle-partner term in the decisive row products was retained before its elimination. The heavy W=5 pair requires p=q and p+q≤1, while the light W=6 pairs use the stronger absence of all nonzero common neighbors.

No counterexample or unresolved candidate to a claimed lemma was found. These checks supplement the derivations and do not replace them.

## Acceptance and limits

The dependency graph is acyclic, all main theorem applications discharge the hypotheses of their predecessors, and the finite cases include zero slack and isolated-support boundaries. There are no probabilistic, limiting, or asymptotic interchanges to check. The final conclusions match the theorem's conditional scope.

Acceptance remains **same-family / provisional**. No external cross-family review, Lean proof, numerical graph search, artifact hashes, TeX/PDF/HTML output, or wiki update was performed in this bounded task.
