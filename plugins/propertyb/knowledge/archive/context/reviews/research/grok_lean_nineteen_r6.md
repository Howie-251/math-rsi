`nineteen_propertyB` proves the scoped 19-vertex statement. Every simple 5-uniform hypergraph on `Fin 19` with at most 32 edges has Property B. The failure probability is bounded by a uniform majorant that is strictly below 1, and that majorant is tied to the original greedy coloring. No separating hypergraph and no quantifier mismatch showed up inside this branch. `Aris4Math.Target` is still open.

## What is proved

```149:158:formal/Aris4Math/NoLocks.lean
theorem nineteen_propertyB (H : Simple5Hypergraph (Fin 19))
    (hE : H.edges.card ≤ 32) : PropertyB H := by
  apply ConditionalUnion.propertyB_of_position_bounds H (noLocks 19) (noLocks 19)
    (fun k => 32 * endpointWeight 19 k true)
    (fun k => 32 * endpointWeight 19 k false)
    (fun k => 992 * pairWeight 19 k)
  · exact fun k => endpoint_sum_le H hE k true
  · exact fun k => endpoint_sum_le H hE k false
  · exact fun k => critical_sum_le H hE k
  · exact nineteen_sum_lt_one
```

The only hypotheses are `Simple5Hypergraph (Fin 19)` and `edges.card ≤ 32`. The lock list is the empty embedding `noLocks`, so the sample is all `19!` permutations (`Counting.card_prescribed_images`). Pair-covering, linearity, degree, and a profile hypothesis are not used. This review did not re-run the kernel.

## Failure cover

The direction used is failure implies a critical pair.

`Greedy.FailureAt` is an all-blue image edge after the scan (the all-red disjunct is impossible: `no_all_red_edge`, lines 87–106). `all_blue_implies_critical_pair` (lines 119–147) takes the earliest vertex `x` of that blue edge. The flip witness `A` satisfies `max A = x = min B` and `A ∩ B = {x}`. `failureAt_covered` (lines 198–208) pulls that pair back to the original edges. `ConditionalUnion.failure_ratio_le_critical_sum` (lines 65–72) is the corresponding union bound on `lockedRatio`. The converse, critical pair implies failure, is not used.

`CriticalAt` at a position is then covered twice, both times as the same event:

- `critical_implies_endpoints` (`CriticalCounting.lean` 611–618) gives a real edge whose image maximum is that position, and a real edge whose image minimum is that position.
- `critical_ratio_le_pair_sum` (`ConditionalUnion.lean` 53–61) gives one ordered off-diagonal pair.

`failure_ratio_le_position_bounds` (lines 77–92) takes the minimum of those three upper bounds at each position, then sums.

## Endpoint probability

For a fixed 5-edge and a 0-based position `j`, the maximum lies at `j` exactly when the position set is `{j}` plus 4 positions chosen from the `j` earlier ones:

\[
\frac{\binom{j}{4}}{\binom{19}{5}} = \frac{5\binom{j}{4}}{19\binom{18}{4}}.
\]

The minimum uses the `18-j` later positions. That is `endpointWeight` (`NoLocks.lean` 41–43). `free_endpoint_ratio` puts the factor 5 in by partitioning on which vertex of the edge sits at `j` (`CriticalCounting.lean` 467–512). `endpoint_ratio` (lines 49–57) is this equality for every real edge. With `n ≤ 32` edges,

\[
\sum_e \Pr(\text{endpoint of }e\text{ at }j) = n\cdot p_j \le 32 p_j
\]

(`endpoint_sum_le`, lines 91–102). The factor 32 multiplies an exact single-edge probability. It is not an extra combinatorial choice.

## Ordered critical pairs, and where 992 is bookkeeping

If `|A ∩ B| = 1`, with intersection vertex `x`, the event `CriticalPair` at 0-based `j` is: `σ(x) = j`, the other four vertices of `A` lie before `j`, and the other four of `B` lie after `j`. Those eight vertices are distinct. Counting permutations gives

\[
\frac{\binom{j}{4}\binom{18-j}{4}}{19\binom{18}{4}\binom{14}{4}}.
\]

That is `pairWeight` (lines 45–47). `free_critical_ratio` (lines 301–334) derives the same quantity: probability `1/19` that `x` is at `j`, then the locked joint ratio on the remaining four-plus-four vertices. There is no factor `5·5` and no choice of intersection point. `critical_ratio_le` (lines 70–86) is equality in this case.

If `|A ∩ B| ≠ 1`, `critical_ratio_zero_of_intersection` (lines 627–633) gives actual probability 0. Lines 87–89 then use only `0 ≤ pairWeight`.

`offDiag` is ordered, so its cardinality is `n(n-1)`. For `n ≤ 32`,

\[
n(n-1) \le 32\cdot 31 = 992
\]

(`offDiag_card_le`, lines 104–111). `critical_sum_le` (lines 113–127) therefore bounds the sum of actual pair probabilities by `992 · pairWeight`. The `992` charges every ordered pair the single-intersection weight, including pairs whose probability is 0. That charge is a majorant. The proof does not treat it as those pairs’ probability.

One-based `Numeric` slots agree with these 0-based slots: position `k` has `k-1` places before it and `v-k` places after it (`Numeric.lean` 38–42), which is `j` and `18-j` for `j = k-1`. The `v19` profile is 32 edges, no locks, pair count `32·31`, deduction 0 (lines 79–81 and 141–142). `nineteen_sum_eq_numeric` identifies the two closed sums. The proof never casts a one-based index into `Fin 19`.

## The 19-term minimum

Write `D = 19\binom{18}{4} = 58140` and `A(j) = 160\binom{j}{4}/D`, and likewise `B(j)` with `18-j`. Let `C(j)` be the `992` pair majorant. Then

\[
\frac{A(j)}{C(j)} = \frac{5005}{31\binom{18-j}{4}},
\]

so `A(j) ≤ C(j)` exactly when `18-j ≥ 10`, i.e. `j ≤ 8`. Symmetrically `B(j) ≤ C(j)` for `j ≥ 10`. Positions `j < 4` and `j > 14` are zero: a 5-edge cannot end in the first four positions or start in the last four.

| 0-based `j` | active term |
|---|---|
| 0–3, 15–18 | 0 |
| 4–8 | `A(j)` |
| 9 | `C(9)` |
| 10–14 | `B(j) = A(18-j)` |

So the sum is `2(A(4)+…+A(8)) + C(9)`.

\[
\binom{4}{4}+\cdots+\binom{8}{4} = 126, \qquad 2\cdot\frac{8\cdot 126}{2907} = \frac{2016}{2907} = \frac{160160}{230945}.
\]

\[
C(9) = \frac{992\cdot 126^{2}}{19\cdot 3060\cdot 1001} = \frac{15748992}{58198140} = \frac{62496}{230945}.
\]

\[
\frac{160160+62496}{230945} = \frac{222656}{230945} < 1.
\]

That is `Numeric.v19_value` and `nineteen_sum_lt_one` (lines 140–144). The strict inequality is on this majorant, so the actual failure ratio is at most a number strictly below 1.

## Original witness

`propertyB_of_failure_ratio_lt_one` (`ConditionalUnion.lean` 96–111): if every locked permutation failed, the ratio would be 1. Hence some permutation `σ` has `¬ FailureAt`. `propertyB_of_successful_permutation` (`Greedy.lean` 241–285) sets `c(x)` true when position `σ(x)` stayed red. Each original edge gets at least one red vertex from success, and at most four because `no_all_red_edge` supplies a blue vertex. That is the count in `PropertyB` (`Aris4Math.lean` 31–34): between 1 and 4 red vertices, with no balance requirement.

## Paper interface

`FORMAL_SPEC.md` F and `proofs/STRUCTURE_19_23.md` §1 state the 19-vertex case under `|E| = 32` and pair-covering. Those hypotheses are not inputs of `nineteen_propertyB`. Fewer edges only shrink `n` and `n(n-1)`, and a non-singleton intersection has critical probability 0, so the same 32/992 majorant still applies. The Lean statement is the stronger one, and the proof is what supplies that extra range. The `v = 20` drop from 992 to 948 in the note really does use pair-covering. The 19-vertex arithmetic does not.
