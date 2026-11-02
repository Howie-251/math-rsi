# Triangle-witness refinement proof audit

**Verdict: PASS within the explicit source assumptions; same-family, provisional.** No open proof issue was found in the complete 307-line `CONNECTED_REPEAT_TRIANGLE_WITNESS_REFINEMENT.md`. The 14 original-scope obligations are recorded in `PROOF_SKELETON.md`. Cross-family review is for the parent workflow; this report does not claim it occurred.

Reviewer: `/root/proof_review_n62_triangle_witnesses`. Review date: 2026-10-11. Applied project skill: `.agents/skills/proof-checker/SKILL.md`, with the caller's MD/JSON-only and no-hashes overrides. No source, shared wiki, shared status, or formal project file was edited. No prior audit verdict was read.

## Main checks

The all-witness theorem correctly uses the *entire* heavy-root neighborhood restriction: every positive pair there meets that heavy pair's generated triangle. Generated-triangle separation then excludes every heavy common neighbor of every pair of a nongenerated triangle, rather than only excluding one selected witness.

The type-one argument has all needed domains. The original triangle-pattern paper proves that every center lies in `W` and that distinct triangles have distinct centers. Its complete center row, together with witness nonheaviness, proves `ell(u)=m(u)=0`. Nonnegative commutation proves isolation of `u` among each other witness's repeat neighbors. The triangle-port argument then gives `m≤1` on `U1`. The packing and mixed-trace sums retain possible center/triangle intersections, shared witnesses across triangles, and coincident recipient vertices.

The center relation is symmetric because any triangle containing a type-one center uses two of its three witnesses and has an exact unique center in the original triangle. Its adjacent triangles are disjoint, while two different neighbors overlap. The maximum-degree-two and overlap-cluster arguments exclude `P5`, `C3`, and cycles of length at least five, leaving precisely the stated necessary list `K1,K2,P3,P4,C4`. The `P3` middle-cluster refinement uses distinct centers correctly. These are necessary component types, with no realizability assertion.

For `d=9, v_extra=11`, the only overlap-cluster counts are one isolated triangle and two diamonds. Five type-one triangles would force `P3+K2`; the `P3` consumes the single isolated triangle and one entire diamond, leaving an impossible center-graph edge between the overlapping triangles of the other diamond. The separate trace improvement uses integrality correctly: `tau<44` and `tau≡4 (mod 10)` give `c5≤2501`.

The diamond signed-vector proof correctly gives `A²f+Af=6f`, with both exclusive neighborhoods of size six. Evaluation gives degree exactly one across them. All four port equalities follow individually from commutation. If the tips are originally adjacent, both tip rows have original-edge count two; the type-one bound excludes type one, and overlap excludes type two. The argument never infers `N(x)∩N(y)={p,q}` from membership.

## Adversarial boundary checks

| Attempt | Result |
|---|---|
| Put a heavy endpoint among any of the six type-zero witnesses, or among any of the four type-one witnesses. | It would neighbor a nongenerated triangle pair inside its root neighborhood, contradicting the exact restriction and generated separation. |
| Place a type-one center on another unit triangle, including overlapping type-one triangles. | Allowed where the source allows it. `C1` and `U1\C1` prevent double counting; only centers outside all unit triangles contribute to `c_out`. |
| Identify witnesses belonging to different nongenerated triangles or identify heavy endpoints' light mates. | No proof step assumes distinctness across these objects. Incidence capacity and set unions handle collisions. |
| Use a three-cycle or a five-vertex path/cycle in the center graph. | The 3-cycle simultaneously forces overlap and disjointness. The five-vertex path forces an overlap cluster of at least three triangles. |
| Let a `P3` middle triangle overlap a type-zero triangle. | The overlapping triangle contains one of its two neighbor-centers, forcing it to be type one and to add an edge. This closes the potentially omitted type-zero case. |
| Set diamond ports `p=q`. | Each commutation equality remains valid, and tip adjacency still gives `m(z)=m(w)=2`. No distinct-port or exhausted-common-neighbor assumption is used. |
| Take the sharp `d=9, L3=6` boundary. | The unrefined trace ceiling is 44; any `t1>0` subtracts at least four, so 44 is excluded and the stated five-cycle bound follows. |

No algebraically verified counterexample was found. These checks do not establish existence of any surviving local configuration.

A small independent arithmetic/local-graph check returned:

```text
3s+4k=11: [(1,2)]
(tau,c5) with 0<=tau<44 and tau=10c5-24976:
[(4,2498),(14,2499),(24,2500),(34,2501)]
2*7812-14*496-33728 = -25048
248-24*9+2*6 = 44
Connected graphs on at most six vertices satisfying the abstract center/overlap constraints:
K1, K2, P3, P4, C4
```

The local-graph check enumerated only graphs of maximum degree two and required every pair of distinct neighbors to overlap, with overlap pairs forming a matching disjoint from center-graph edges. It is corroboration of the written finite-path argument, not a proof replacing that argument or a search over actual order-62 graphs. No solver or expensive computation was run.

## Scope of acceptance

The accepted conclusions are the conditional all-witness nonheavy theorem, type-one restrictions, strengthened packing/mixed trace, necessary center-component classification and refinements, the two stated `d=9` consequences, and the diamond matching/tip lemma. There is no arbitrary order-62 exclusion, no exclusion of `d=9`, no exclusion of either nongenerated triangle type in general, and no assertion that the remaining local configurations extend to an actual graph. No dedicated known-order-63–65 work was performed. No source change is required by this review.
