# Scoped PASS: seventeen-edge heavy base exclusion

**Verdict: PASS modulo explicitly imported earlier reductions.** Review independence: **same-family**. Semantic acceptance status: **provisional**. No actual mathematical flaw was found in the complete new proof or the checked derivations in its immediate predecessor. No source edits were made.

This fresh review read both input proofs in full and derived the counting and sign arguments directly. It did not accept previous reviewers' conclusions as evidence, rerun upstream finite classifications, enumerate candidate graphs, or claim an order-62 exclusion.

## Load-bearing checks

The mate symmetry follows directly by separating an even difference from a binary difference in heavy-heavy commutation. It makes the heavy adjacency blocks matchings; the exact heavy repeat rows forbid common heavy neighbors for nonmate pairs. Thus the lift has neither original triangles nor four-cycles. A positive signed base cycle of length three or four returns to the starting sheet and yields a prohibited original cycle. The degree-four bound uses the imported complete row at normalized label 4, as stated.

The predecessor's squared-degree count subtracts both original edges and the d mate pairs from the available unordered pairs; its rearrangement and equality matrix are correct. On antisymmetric vectors the equality matrix gives Z²+Z=diag(r). For d=9,m=18 the degree sum and bound force r_i=4, so an integer 9-by-9 matrix would satisfy the irreducible rational quadratic x²+x−4. Its characteristic polynomial would be a power of that quadratic, impossible in odd dimension. The d=5 and d=7 balancing arguments in the same predecessor also check.

The new proof's three obstructions are valid for subgraphs, with no inducedness requirement. Codegree is at most two; adjacent codegree is at most one; every edge belongs to at most one triangle; and the prism sign product is inconsistent. The local identity counts all adjacent and nonadjacent endpoints exactly once with their common-neighbor multiplicity. Its global sum is

`2d(d−1) − Σr_i² = 2(a+b+2c)`.

For m=17 the two degree patterns are exhaustive because the total deficiency from degree four is two. Their squared-degree sums are 130 and 132, yielding slack 7 and 6. With a=17−3t, nonnegativity and edge-disjointness give precisely t in {4,5}.

The triangle-intersection graph is simple since base triangles share at most one vertex, and each base vertex belongs to at most two triangles. A triangle in the intersection graph either puts three original triangles through one vertex, violating maximum degree four, or creates a new base triangle sharing an edge with an old one. It is therefore triangle-free. Five triangles cover `15−|E(I)|` vertices; the resulting six-edge triangle-free graph on five vertices is K_2,3. Its two disjoint degree-three triangles and the edges supplied by the other three triangles give the forbidden prism. This is an exhaustive structural argument, not an enumeration.

Once t=4, pattern B has b=1,c=0 and the unique degree-two vertex has local slack 8 but available slack at most 3. For pattern A, the degree-three vertices satisfy `b_z+2c_z=1+k+2t_z`, with k indicating their adjacency. When b=2,c=0, k=1 would demand at least four incidences supplied by two nonedges each incident to at most one of the two vertices. Hence k=0 and both degree-three vertices avoid every triangle; four triangles would then need at least eight of the remaining seven vertices. When b=0,c=1, parity forces k=1 and both degree-three vertices to be endpoints of the unique counted nonedge, contradicting adjacency. Both branches close.

## Counterexample and boundary pass

- A diamond cannot defeat the triangle-edge restriction: its two negative triangles multiply to a positive four-cycle.
- Three shared neighbors cannot evade the four-cycle obstruction: two of the three path signs agree regardless of additional chords.
- A triangular prism with extra chords still has the same three rectangle cycles and the same sign contradiction.
- Multiple triangles through one vertex and repeated intersection vertices were checked explicitly; the degree-four bound prevents hidden higher multiplicity in the union formula.
- The distance correction is necessary and correctly stated. A nine-vertex tree with edges `ua,uc,ud,ue,vb,vf,vg,ab` has degrees 4 and 3 at u,v and distance three. It satisfies the short-cycle sign conditions vacuously. Thus the proof correctly avoids the false stronger exclusion of a degree-(4,3) distant pair; its actual inequality is 4+3≤9−2.
- Both slack partitions `(b,c)=(2,0),(0,1)` in pattern A, and the sole partition `(1,0)` in pattern B, are exhaustive integer cases. Incidence counts never substitute total unordered pair counts incorrectly.

No counterexample to a claim actually made in the reviewed proofs was found. These checks supplement the displayed derivations; lack of a counterexample is not used as a proof step.

## Incidence scope

Unconditionally for d=9, `|E_G(D,V minus D)|=144−4m≥80`; exactly 54 of these are the edges to each heavy pair's own generated triangle. At least 26 therefore go to W or other generated triangles. The preceding distance lemma excludes the latter only for base distances one or two. No connectivity or diameter property of F is inferred from connected repeat support.

Under the additional diameter-at-most-two assumption all these incidences go to W. The predecessor's repeat-edge bound is separately correct: at least two external repeat ports per generated triangle lie in W; parity upgrades 18 to 19; and `2e_B(W)+18+e_B(S,W)=51` gives `e_B(W)≤7`. The proof keeps this statement conditional and distinguishes repeat edges from original edges.

## Residual scope

The connected-repeat, D1, generated-triangle separation, normalized-row and port facts remain explicit imported assumptions of this review. Their upstream classifications were not rerun. Signed-base feasibility is only a necessary condition for actual-graph feasibility. The result neither excludes d=9 nor constructs an order-62 graph, and leaves the unresolved order-62 problem open. The audit is a same-family provisional mathematical judgment, not a formal verification or a cross-family acceptance.
