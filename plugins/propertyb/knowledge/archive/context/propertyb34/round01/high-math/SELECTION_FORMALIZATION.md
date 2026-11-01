# Actual lock selection for T34

The source modules select vertices of the original hypergraph. They do not
take a local classification certificate as an extra input. The probability
classification and final coloring callers remain separate obligations.

## 24 vertices: eight matching locks — checked

Source: `formal/Aris4Math/ThirtyFour/TwentyFourMatchingSelection.lean`.
Namespace: `Aris4Math.ThirtyFour.TwentyFourMatchingSelection`.

For an actual pair-covering `Simple5Hypergraph (Fin 24)` with 34 edges,
`exists_eight_matching_locks` supplies an eight-element set whose vertices
have degree six or seven. Every row of its nonnegative codegree-excess matrix
has sum at most one, and every mixed degree-six/degree-seven pair is unit.
The indexed export `exists_eight_matching_vertices` supplies a `Fin 8`
embedding, pair codegrees one or two, uniqueness of a codegree-two neighbor,
and equality of the two endpoint degrees for each codegree-two pair.

The degree sum gives `t + 2r ≥ 22`, where `r` and `t` count degrees six and
seven. The checked generic weighted three-partition theorem partitions the
seven-degree points with internal excess at most one. Each six-degree point
has at most one bad partner, so it can join at least two classes. One enlarged
class therefore has at least eight vertices. Restriction to eight points
preserves the actual excess and mixed-pair conclusions.

The unique main Lean executor ran the regular serialized build. The saved log
`../twentyone-lean/build-queue-TwentyFourMatchingSelection-r10.log` reports
success, 953 jobs, and a 1.4-second new module build. Both final exports depend
only on `propext`, `Classical.choice`, and `Quot.sound`. The helper author read
the saved log and did not launch a competing Lean process. This is local
incremental verification, not an independent-machine reproduction or a proof
of the entire 24-point branch.

## 25 vertices: one selection supplies nine or ten unit locks

Source: `formal/Aris4Math/ThirtyFour/TwentyFiveSelection.lean`.
Namespace: `Aris4Math.ThirtyFour.TwentyFiveSelection`.

The main export is

```lean
exists_nine_or_ten_unit_locks
  (H : Simple5Hypergraph (Fin 25))
  (cover : H.PairCovering) (size : H.edges.card = 34) :
  MixedLocks H 5 4 ∨ MixedLocks H 8 2 ∨ NineLowExtension H
```

`MixedLocks H l h` provides `f : Fin (l+h) ↪ Fin 25`, degrees six at indices
less than `l`, degrees seven at the remaining indices, and unit codegrees
between all distinct locks. `NineLowExtension H` provides ten pairwise-unit
locks: the first nine have degree six and the last has degree six or seven.
Thus the three outputs are respectively `6^5 7^4`, `6^8 7^2`, and
`6^9 (6 or 7)`. In the latter two branches the actual tenth lock is already
available when a nine-lock profile needs an extension.

The actual degree budgets are `r ≥ 5` and `2r + t ≥ 30`. At 25 vertices, the
existing `codegree_eq_one_of_twenty_five` theorem makes every degree-six point
unit with every other point. Every degree-seven point has at most four bad
partners. The new `unit_subset_of_bad_bound` greedily removes a chosen point
and its bad partners; if `(k-1)(d+1) < |S|`, it supplies a unit `k`-subset of
the actual set `S`. The caller uses this lemma with `d = 4` and `k = 4,2,1`.

For `r ≤ 7`, the seven-degree set has at least sixteen points, so four unit
high points join any five lows. For `r = 8`, at least fourteen high points
supply a unit high pair alongside eight lows. For `r = 9`, at least twelve
high points supply the tenth lock. For `r ≥ 10`, ten lows suffice.

The source imports only the existing incidence/low-degree and actual-trace
modules. It does not use the 33-edge selection conclusions. General actual
trace uniqueness, singleton/empty recovery, and lock relabeling remain
available to the later probability caller; no copies are introduced here.

The unique main Lean executor completed the regular serialized build:
`../twentyone-lean/build-queue-TwentyFiveSelection-r19.log` reports success,
909 jobs, and a 1.3-second new module build. The final export's transitive
axioms are only `propext`, `Classical.choice`, and `Quot.sound`. The helper
author inspected that saved output and did not run a second Lean process.
There is no `sorry`, new axiom, or `native_decide`. This selection theorem
alone does not prove the 25-point branch or T34.

## 21 vertices: seven-degree unit neighbors and six actual locks

`TwentyOneSevenUnitSet.unit_set_structure_of_not_propertyB` takes an actual
21-point pair-covering hypergraph with 34 edges, a degree-seven center `x`,
and `¬ PropertyB H`. For any set `U` of at least three degree-eight points
unit with `x`, it derives that every distinct pair in `U` has codegree two
and each actual edge through `x` contains at most two points of `U`. All
four-lock classification assumptions are proved by the imported actual
classifier. The helper exposes no additional local-profile premise.

`TwentyOneSevenSelection` reuses the existing seven- and eight-degree sets.
At minimum degree seven it proves `|L| + 2r ≥ 19`, where `L` is the degree-eight
set. Writing `U_x` for the unit neighbors of `x` in `L`, it proves
`|L| ≤ |U_x| + 8`. A second seven-degree point `y` gives the sharper actual
excess bound `|L| + codegree(x,y) ≤ |U_x| + 9`. The one-seven wrapper therefore
supplies `|L| ≥ 17`, `|U_x| ≥ 9`, and the actual pair/capacity conclusions.
The two-seven wrapper supplies `|L| ≥ 15` and
`|U_x| ≥ 6 + codegree(x,y) ≥ 7`, with the same structural conclusions.

These modules passed the unique executor's regular builds:
`../twentyone-lean/build-queue-TwentyOneSevenUnitSet-r19.log` (1044 jobs,
1.5 seconds for the new module) and
`../twentyone-lean/build-queue-TwentyOneSevenSelection-r20.log` (1045 jobs,
1.6 seconds for the new module). The exported structural theorem and both
selection wrappers have only the standard three transitive axioms.

`TwentyOneSevenOneSelection` uses the one-seven wrapper to construct the
six locks needed by the unique-seven classifier. The sum of actual center
incidences is at least nine. Since the center has seven edges of capacity
two, at least two of those edges contain two selected neighbors. Unit
codegrees make the two pairs disjoint. A fifth neighbor outside those pairs
has a different center edge. The actual center traces are therefore one each
of `{0,1,2}`, `{0,3,4}`, and `{0,5}`, plus four copies of `{0}`.

`exists_locks` returns this root-first six-lock embedding, degrees
`7,8,8,8,8,8`, center codegrees one, leaf codegrees two, and every exact trace
count containing the center. `exists_last_locks` applies a fixed permutation
and the common `LockRelabel.count_comp_perm` theorem. It returns five degree-eight
locks followed by the degree-seven root, with actual `LockExtension.promotion`
equal to four on the empty old trace, one on `{0,1}`, `{2,3}`, and `{4}`, and
zero elsewhere. This is an actual selection and trace-binding interface,
not a supplied numerical certificate.

The unique executor completed the regular serialized build:
`../twentyone-lean/build-queue-TwentyOneSevenOneSelection-r22.log` reports
success, 1047 jobs, and a 2.8-second new module build (exit 0). Both
`exists_locks` and `exists_last_locks` have exactly `propext`,
`Classical.choice`, and `Quot.sound` as transitive axioms. The helper author
inspected the saved output and did not launch a competing Lean process.
This is a local incremental build. None of these helper modules by itself
establishes the whole minimum-degree-seven branch or T34.
