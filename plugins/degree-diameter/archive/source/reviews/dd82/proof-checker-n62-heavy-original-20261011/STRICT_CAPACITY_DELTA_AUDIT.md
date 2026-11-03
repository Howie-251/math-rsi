# Strict triangle-capacity delta review

**PASS, same-family provisional.** No mathematical correction is needed in `CONNECTED_REPEAT_STRICT_TRIANGLE_CAPACITY.md` as read on 2026-10-11. This is an independent check of the root-authored delta by the **reused** reviewer `/root/proof_review_n62_heavy_original`; it is not a fresh-context review or cross-family acceptance.

The full new note and its directly relevant source content were read: `CONNECTED_REPEAT_TRIANGLE_WITNESS_REFINEMENT.md`, `CONNECTED_REPEAT_HEAVY_PORT_CLOSURE.md`, and `CONNECTED_REPEAT_UNIT_TRIANGLE_PATTERNS.md`. The pre-existing actual-graph, D1, and connected-repeat reductions remain imported. This delta does not recertify the unrelated center-graph, diamond, mixed-trace, or earlier classification conclusions.

| Obligation | Check |
|---|---|
| All heavy unit incidences end in R | The D1 light-mate result excludes D and every unit-triangle vertex U. The witness refinement proves that a type-one center has a complete unit row whose three witnesses are nonheavy, hence no heavy repeat neighbor. Thus C1 is also excluded. |
| The size of R is exact | D is disjoint from U and C1. The unit-triangle paper excludes heavy endpoints from U and gives a fully unit row at every type-one center, excluding D from C1. Hence the union removed has size 2d + 3d + v_extra + c_out, even when C1 overlaps U. |
| Equality closes D union R | Row capacity gives 2d <= 3 size(R). At equality every R vertex has exactly three unit repeat neighbors in D, exhausting its row; each D row stays in D union R. The resulting set is nonempty because d >= 1 and proper because it omits all 3d generated-triangle vertices. This contradicts connected positive repeat support. |
| Strict algebra and table | Substitution gives 17d + 3v_extra + 3c_out < 186. For integer n = v_extra + c_out, the maximum is floor((185 - 17d)/3), yielding 56, 44, 33, 22, 10 at d = 1, 3, 5, 7, 9. |
| The previous boundary disappears | At d = 9, n <= 10 and c_out >= 0 imply v_extra <= 10. Thus v_extra = 11 itself is impossible; the older conditional type-zero conclusion is now vacuous and implies nothing for an arbitrary d = 9 graph. |
| The v_extra = 10 boundary | At d = 9 it forces c_out = 0. The existing overlap-cluster classification gives 3s + 4k = 10. Nonnegative integrality forces k = 1 and s = 2, so there are s + 2k = 4 nongenerated triangles: two isolated triangles and one diamond. No type or graph-existence conclusion follows. |

The alternative reference to the strict heavy-port theorem is sound: if every R row were saturated by heavy incidences, its saturated-vertex count would satisfy 3L3 = 2d, contradicting that theorem. The direct closed-set proof already suffices.

Counterexample challenges checked: shared light mates are permitted and counted by their row capacity; centers can overlap U without being subtracted twice; a vertex of R has no residual repeat capacity in the equality case; generated triangles guarantee that the closed set is proper; a disconnected repeat support would invalidate the contradiction, but connectedness is explicit. None produces a counterexample under the stated hypotheses.

The strict inequality excludes a numerical boundary configuration, not any remaining value of d. It does not establish existence of a type-zero triangle. No proof source was edited, and no search or solver was used.
