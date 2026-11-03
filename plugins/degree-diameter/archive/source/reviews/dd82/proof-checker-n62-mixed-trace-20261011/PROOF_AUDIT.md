# Fresh mixed-trace review

Date: 2026-10-11. Reviewer: `/root/proof_review_n62_mixed_trace`.
Final scoped verdict: **PASS, same-family/provisional**, after one minor wording and derivation clarification. No fatal, critical, or major gap was found in the mixed-trace argument under its stated upstream reductions. This is a mathematical paper review, not formal certification or cross-family acceptance.

The complete input was `proofs/dd82/n62/CONNECTED_REPEAT_MIXED_TRACE_AND_ROOT_PATTERNS.md`. Original mathematical dependencies read were the D1 hard-branch reduction, C4 refinement, connected-repeat reduction, unit-triangle pattern note, triangle-pairing proof, D0 component proof, and the relevant disjointness/port sections of the global quotient note. Prior audit files were not used; historical verdict mentions embedded in original sources supplied no proof evidence.

## Verified mathematics

The polynomial calculation is exact: the J contribution is −33728, tr(A⁴)=7812+4d, tr(A²)=496, and triangle-freeness gives tr(A⁵)=10c5. Therefore tau=10c5+8d−25048.

The local trace formula retains repeat weights and its factor of two. D1 heavy rows and all generated-triangle rows have independent original repeat neighborhoods. Hence tau=2 sum_{w∈W} m(w).

Every heavy endpoint's unique light mate lies outside D and S. Counting incidences, rather than distinct light mates, gives sum ell(w)=2d. Every heavy mate is isolated among a light mate's three repeat neighbors. The sharp elementary three-vertex bounds 2,1,0,0 give tau≤248−24d+2L3 and 3L3≤2d. The generated disjointness and incidence bound also give 17d≤186; opposite-pair counting gives d odd and c4=(93+d)/2.

The three parent pairs at a positive row are distinct. Their graph contains disjoint edges and consequently is exactly one of 3K2, P3+K2, P4, after isolated vertices are omitted. The allowable positive triangle-free mate graphs give precisely five necessary cases. This is a classification of local necessary shapes, not a realizability claim.

In the two-edge P3+K2 case, the clarified argument proves B_ac=1 because the repeat mates a,c are nonheavy, nonadjacent, and share distinct original neighbors h,b. The triple {w,a,c} has exactly one common original neighbor h and is therefore a type-one nongenerated unit triangle. No assumption eliminating nongenerated triangles is used.

Exact integer arithmetic independently checked the J constant, mixed-trace constant, all five c5 ranges, and the conditional tau=0 ⇒ d=1, c5=2504. The d=9 range is 2498≤c5≤2502.

## Issue and fix

**MT-01 — MINOR / UNCLEAR / COSMETIC / LOGICAL_GAP (expository antecedent).** Original §5, lines 237–238 said, after naming common neighbors h,b, “Neither can be a heavy endpoint, by the preceding isolation property, so B_ac=1.” The directly applicable isolation statement concerns the repeat mates a,c. Reading “Neither” as h,b does not justify B_ac≤1.

Fix strategy: **ADD_DERIVATION**. With root authorization, replace that sentence by explicit reference to a,c and the inequalities B_ac≥1 and B_ac≤1. The corrected paragraph was reread and its hypotheses checked. The common neighbors h,b are distinct because h is adjacent to w and b is not; a,c cannot be adjacent because both neighbor b in a triangle-free graph. Neither a nor c is heavy because each is incident to an original edge in the three-mate graph. No hypothesis or conclusion changed. See `FIX_RECEIPT.md`.

The initial wording warrants WARN before clarification. After this fix there is no open issue in the reviewed new argument. No new reviewer round is claimed; this same fresh reviewer checked the cosmetic correction, as directed by the root executor.

## Adversarial checks

- Tested the factor and weighting in the trace formula on a hypothetical heavy row of weights two and one: its local contribution would be 4A_uv to the trace, correctly vanishing only after the D1 nonedge is used.
- Tested ell=3, which would make 2−ell negative without the L3 correction; the stated indicator supplies the needed zero bound.
- Allowed shared light mates of different heavy pairs; the incidence count remains exact and does not assume an injective mate map.
- Tried equal parent pairs; B≤2 forces a generated triangle containing the positive root, contradicting its membership in W.
- Tested missing three-edge shapes: a star and a triangle have no disjoint edges, and a third edge added to two disjoint ones yields exactly the three listed shapes.
- Tested the type-one deduction for a third a,c common neighbor: this would force B_ac=2, making a,c heavy and contradicting isolation. An additional common neighbor of w,a,c would separately contradict P_a∩P_c={h}.
- Tested the attempted implication B_pq=0 ⇒ A_pq=0. In a triangle-free graph every original edge has B_pq=0; the common-neighbor identity permits A_pq=1 with zero common neighbors. Thus that inference is unavailable. This is a logical compatibility check, not a constructed order-62 graph.

No algebraically verified counterexample to a stated claim was found. No solver or graph search was run. The deterministic check used integer arithmetic only.

## Scope and open work

The exact graph identities, B≤2, triangle-freeness, and D1 local reductions are the stated mathematical inputs. The local rows, disjointness, and port applications were checked from original proofs; this audit does not recertify every earlier finite classification or its formal implementation. Automatic connectedness is unnecessary because the reviewed statement assumes connected support.

Zero mixed trace is unproved. The five positive local patterns, including whether a light mate's two ordinary repeat mates are joined by the existing original matching, remain unresolved. No actual graph realizing these patterns is asserted. Arbitrary order-62 exclusion and the exact degree-diameter value remain open.
