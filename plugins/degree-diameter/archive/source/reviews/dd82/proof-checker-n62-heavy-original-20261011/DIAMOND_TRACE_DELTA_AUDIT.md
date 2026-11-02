# Diamond-trace delta review

**PASS, same-family provisional.** No mathematical correction is needed in the 100-line `CONNECTED_REPEAT_DIAMOND_TRACE_REFINEMENT.md` read on 2026-10-11. This is an independent check of a root-authored delta by the **reused** reviewer `/root/proof_review_n62_heavy_original`. It is not a fresh-context review or cross-family acceptance.

## Checked source scope

The full new note was checked against the directly used content of:

- `CONNECTED_REPEAT_TRIANGLE_WITNESS_REFINEMENT.md`, Sections 2–4 and 6: center and type-one vertex penalties, center graph, and adjacent-tip implication.
- `CONNECTED_REPEAT_UNIT_TRIANGLE_PATTERNS.md`, Sections 2–3 and 6: generated-triangle separation, centers outside generated triangles, injective centers, and overlap clusters.
- `CONNECTED_REPEAT_MIXED_TRACE_AND_ROOT_PATTERNS.md`, Sections 1–3: exact mixed trace, local interpretation, and baseline inequality.
- `CONNECTED_REPEAT_HEAVY_PORT_CLOSURE.md`, Sections 1–2: strict L3 bound and five-cycle range.
- `CONNECTED_REPEAT_STRICT_TRIANGLE_CAPACITY.md`: the d = 9, v_extra = 10 cluster count and c_out = 0.
- `CONNECTED_REPEAT_CENTER_CYCLE_EXCLUSION.md`, Sections 1–2, together with the witness paper's center-component classification.
- `CONNECTED_REPEAT_SIXTH_CYCLES_AND_DETERMINANT.md`, Sections 1–2: the sixth-cycle trace calculation and u congruent c5 modulo two. The determinant material is not used or recertified here.

Existing actual-graph, connected-repeat, and D1 reductions remain imported. Prior audit verdicts were not used to discharge the new claims.

## Proof obligations

| ID | Obligation and discharge |
|---|---|
| D1 | At a diamond shared endpoint x, the repeat neighbors are y,z,w. The pairs yz and yw are positive repeat pairs and hence original nonedges in the triangle-free graph. The only possible original edge among them is zw. The analogous row at y gives m(x) = m(y) = A_zw exactly. |
| D2 | A shared endpoint lies in a unit triangle, so ell = 0. If either diamond triangle has type one, the witness paper's adjacent-tip implication rules out A_zw = 1; thus both shared endpoints have m = 0. If neither is type one, the unconditional local bound is m <= 1. |
| D3 | The incremental penalty is valid pointwise. Centers already receive the full improvement two from baseline 2 to m = 0 and are excluded from the new charge. A noncenter shared endpoint in U1 previously received improvement one and now receives another one because m = 0. A noncenter shared endpoint outside U1 previously had bound 2 and now has bound 1. Membership in U1 here is equivalent to one of its two diamond triangles being type one, because the overlap cluster is exactly that diamond. |
| D4 | Multiplying the pointwise improvements by two in tau = 2 sum m gives the claimed extra term 2 times the number of shared endpoints outside C1, without assuming disjointness of H and U1. All charged sets are in W: nongenerated triangle vertices and type-one centers avoid both heavy endpoints and generated triangles. |
| D5 | At d = 9 and v_extra = 10, strict capacity gives c_out = 0, and the cluster equation gives two isolated triangles plus one diamond. If all four triangles are type one, Gamma has four vertices and no isolates. The allowed component list leaves 2K2 or P4; P4 would require two distinct diamonds. Hence Gamma = 2K2. |
| D6 | The four centers are distinct, outside generated triangles, and inside U by c_out = 0. Under the all-type-one assumption they therefore lie in the ten-vertex U1, yielding six vertices of U1 outside C1. A shared endpoint cannot be a center: its own triangle is different from both diamond triangles, and membership in both would give that triangle two Gamma neighbors, contradicting Gamma = 2K2. Hence H outside C1 has size two. |
| D7 | At d = 9, strict heavy-port closure gives L3 <= 5. The total penalty is 4 times 4 plus 2 times 6 plus 2 times 2 = 32, while the right side is at most 248 - 216 + 10 = 42. Thus tau <= 10. |
| D8 | The total unit-triangle count is u = 9 + 4 = 13. The sixth-cycle identity forces c5 odd. Within 2498 <= c5 <= 2501, only 2499 and 2501 remain, producing tau = 10c5 - 24976 equal to 14 or 34. Both contradict tau <= 10. The conclusion is therefore that this boundary contains a type-zero triangle. |

## Challenges and limits

The double-counting challenge is resolved by the pointwise split in D3: an H vertex already counted through U1 receives a genuinely additional improvement, while a center receives none. A mixed-type diamond also satisfies the stronger shared-endpoint bound because one type-one triangle already forbids adjacent tips. An all-type-zero diamond needs only the weaker m <= 1 bound. Potential intersections of centers with nongenerated triangles are retained until the boundary argument explicitly analyzes them.

The center-graph argument does not assume that overlapping diamond triangles are adjacent in Gamma; they are not. It uses the number of triangles containing a center. The parity conclusion concerns all unit repeat triangles, and the count 13 includes the nine generated ones. The numerical contradiction uses the existing exact mixed-trace identity, not an assumed vanishing trace.

No counterexample or open proof obligation was found in this delta. The result does not exclude d = 9, force v_extra = 10, or establish a type-zero triangle for every d = 9 candidate. No proof source was edited, and no graph search, solver, or formalization was used.
