No mismatch with the specification’s T33. The 19-vertex branch and the reduction to 20–25 vertices match the sources. The new 20-vertex double-lock bounds also check, including the ordinary-link step; that branch is not a Lean proof of Property B.

## What was read and run

Read only. No shell commands and no edits. Read in full: `context/propertyb33-preparation/FORMAL_SPEC_PROPERTYB_33.md`, `formal/Aris4Math/ThirtyThree/{Target,Reduction,GlobalPairs,Nineteen,Assembly}.lean`, `formal/Aris4Math/GlobalPairs.lean`, `formal/Aris4Math/NoLocks.lean` through the weight lemmas, `formal/Aris4Math/ConditionalUnion.lean` from the weighted-deletion interface, `proofs/propertyb33/TWENTY.md`, `proofs/PROBABILITY_LEMMAS.md` (P1–P8), `computations/propertyb33/round01/twenty_bounds.py`, `computations/multilock.py`, `computations/independent_structure_bounds.py`, and `formal/Aris4Math/ThirtyThree/TwentyTwoStructure.lean`. Read the three round-01 reports under `context/propertyb33/round01/{reduction,reduction/next,nineteen}/`. From `TWENTY_BOUNDS.json`, read all twelve case headers and the full row blocks for (7,9) and (8,8). The build logs were not executed.

## Target33 against the specification

The Lean proposition is the specification’s T33. For every finite vertex set and every finite set of distinct 5-subsets, at most 33 edges implies a map into a 2-element color set whose `true` class meets every edge in 1, 2, 3, or 4 vertices. Pair covering, a vertex-count bound, regularity, and linearity are absent from both statements. `Fintype` is the finite-vertex restriction, and `Finset` supplies distinct unordered edges. The count bound is the specification’s sum, not a different predicate. The specification’s sentence that T33 is equivalent to `m(5) ≥ 34` is the same claim under that notation; it is not an extra premise.

`Reduction.lean` is the specification’s §3 argument, now proved: a counterexample yields some `v ∈ {19,…,25}`, exactly 33 edges, and pair covering. The integer degree step is the one that excludes 26 (`7·26 = 182 > 165`). Padding to 33 edges does not use the old 32-edge theorem. `target_iff_finite_goal` is that equivalence. `Assembly.lean` discharges only `v = 19` and leaves `RemainingGoal` (`20 ≤ v ≤ 25`, exactly 33 edges, pair covering) as an explicit premise of `Target33`. That is not a proof of T33.

## Nineteen vertices

`nineteen_propertyB` has no pair-covering premise and allows at most 33 edges. The double count `20|E| ≤ S + 2 C(v,2)` is the pair-incidence identity in `GlobalPairs.lean`: each edge contains `C(5,2) = 10` pairs, and `2n ≤ n(n-1)+2`. For `v = 19` and `|E| = 33`, `S ≥ 318`. At most six common pairs per ordered edge pair, so at least 53 ordered pairs meet in two or more vertices. Of the 1056 ordered pairs, the singleton-intersection count is at most 1003. Empty intersections only make that count smaller. The kernel statement uses this 1003, not the unformalized 1002.

Recomputed from the no-lock weights: the position minimum uses the endpoint bound except at the middle index, where the pair bound is active. The sum is `228354/230945`, margin `2591/230945`. Replacing 1003 by 1002 changes only that middle term, by `63/230945`, and gives the preparation value `228291/230945`. Both are strictly below 1. This is P1–P5 and P7 with no locks. It does not prove vertices 20–25.

## Twenty vertices

The twelve degree pairs are exactly the pairs produced by the selection rule. A minimum-degree vertex `x` satisfies `5 ≤ d(x) ≤ 8`. The codegree-1 set `W` has size at least `38−4d(x)`, and some `y ∈ W` has degree at most `d(x) + ⌊(165−20d(x))/|W|⌋`. The ranges are 5–8, 6–9, 7–9, and 8, twelve pairs. The profile counts `34−d(x)−d(y)`, `d(x)−1`, `d(y)−1`, `1` sum to 33 and match all twelve JSON count blocks. P8’s numerical lower bound `⌈(4d−19)/3⌉` does not need the links to cover every other vertex: `C(a,2) ≥ a−1` still holds at `a = 0`.

For every pair except (8,8), the deletion puts that quota on the cheaper of the ordinary–ordinary and ordinary–double classes, within capacity. At positions 10 and 11 the double class is cheaper (`21/2210 < 126/12155`). At positions 11 and 12, used only for partner degree 9, the ordinary class is cheaper at the lower center. The (7,9) weights were recomputed from P4: deductions `70/2431` and `10/221`.

The ordinary-link step is the (8,8) case. After deleting the unique common edge, seven 4-subsets lie in an 18-vertex set, with appearance sum 28. Thus `Σ C(a_z,2) ≥ 28−18 = 10`. Each positive link intersection has size at most 3 and makes the original edges meet in at least two vertices, so there are at least `⌈10/3⌉ = 4` ordinary–ordinary bad pairs. P8 still gives at least 5 bad pairs among all eight links. Since `126/12155 > 21/2210`, the worst weighted mix is four ordinary pairs plus one ordinary–double pair:

`4·(126/12155) + 21/2210 = 1239/24310`

at each of positions 10 and 11. Both directions are the P6b weights; one ordinary–double direction is zero and is not charged twice. The unstrengthened placement of all five pairs on the cheaper class is only `21/442 = 1155/24310`. That raises the (8,8) sum derived below by `168/24310`, to `24378/24310 > 1`. The split is what makes this case strict.

The two tight sums were recomputed from P2 and P4. For (8,8), positions 5–9 and 12–16 contribute the empty-type endpoint bounds, and positions 10 and 11 contribute the corrected pair bounds `567/2431`. The total is `2421/2431`, margin `10/2431`. For (7,9) the same endpoint contributions, the free pair bound `3066/12155` at position 10, the corrected pair bound `434/2431` at 11, and the endpoint bound `28/153` at 12 sum to `19813/19890`, margin `77/19890`. At position 12 the corrected pair bound stays above `28/153`, so P7b discards that whole `10/221` deletion. The other ten JSON totals agree with the paper’s table; their inputs and deletion rules check, and each displayed total is below 1. The paper’s minimum margin is the (7,9) margin.

No counterexample to this lemma turned up. It remains a conditional counting argument, not a finished 20-vertex proof. `ConditionalUnion.propertyB_of_weighted_position_bounds` still needs, from an arbitrary 20-vertex pair-covering 33-edge hypergraph, the chosen vertices and positions, the twelve profiles, the bad ordered pairs, and these rational lower bounds. `TWENTY.md` states that this Lean connection is open.

## What remains, and one concrete next calculation

Proved in the sources read here: T33 is equivalent to the seven-vertex finite goal, and the 19-vertex case is unconditional. Not proved: Property B for 20–25 vertices. The 20-vertex prose is the remaining case with a checked strict bound.

Conjecture, not a proved improvement: on the 22-vertex degree-7 branch already selected by `exists_two_locks_of_twenty_two`, repeat the ordinary-link split rather than charging all `⌈(4·7−21)/3⌉ = 3` bad pairs to the cheaper class. Six ordinary 4-links on the 20-vertex set `V\{x,y}` give appearance sum 24 and `Σ C(a_z,2) ≥ 4`, hence at least two ordinary–ordinary bad pairs. If the ordinary weight exceeds the ordinary–double weight at the chosen center, the worst mix is `2 w_LL + w_LD` instead of `3 w_LD`. The (7,9) row shows the limit of this move: if the active term at that center is already the endpoint bound, P7b will ignore any further pair deletion there.
