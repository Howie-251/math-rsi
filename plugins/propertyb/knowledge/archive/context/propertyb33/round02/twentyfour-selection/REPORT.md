# 24-point actual lock selection

2026-10-13. The module `formal/Aris4Math/ThirtyThree/TwentyFourSelection.lean`
now proves the complete first structural selection from a real 24-vertex,
33-edge pair-covering simple five-uniform hypergraph.

## Completed declarations

- `six_card_ge_three`: at least three degree-six vertices.
- `six_seven_budget`: `27 ≤ 2 * r + t` for the actual degree sets.
- `four_unit_or_five_matching`: if `r ≥ 5`, selects either four unit-codegree
  degree-six vertices or five distinct actual degree-six vertices with exactly
  the two exceptional pairs `(a,b)` and `(c,d)` of codegree two; all other
  codegrees are one. No classification of graphs is assumed.
- `exists_unit_pair_avoiding_crosses`: among at least ten degree-seven vertices,
  selects a unit pair avoiding both crossing products for two disjoint pairs of
  three-element arms. Ordered-pair cardinality proves this generally.
- `mixed_locks_of_many_sevens`: when `t ≥ 18`, selects five distinct actual
  vertices of degrees `6,6,7,7,7`, with all pair codegrees one. For each low
  center and **every actual bad link pair**, at least one member edge is disjoint
  from the three selected degree-seven vertices.
- `selected_of_twenty_four`: from only the reduced original input, selects
  one of the four-unit, five-two-matching, or strengthened mixed configurations.
  The four-unit branch retains `r ≥ 5`, needed by the next quad-trace redirect.

The mixed theorem imports and calls the actual bad-pair and arm construction
in `TwentyFourUniqueBadPair.lean`. It does not assume arms or an unconstructed
certificate as extra input.

## Executed verification

All commands used the project-local `.tools/elan`, pinned Lean 4.24.0, and the
existing pinned Mathlib.

1. `lake env lean Aris4Math/ThirtyThree/TwentyFourSelection.lean`: exit 0,
   saved as `direct-compile.log`.
2. `lake build Aris4Math.ThirtyThree.TwentyFourSelection`: exit 0,
   saved as `build.log`.
3. `lake env lean ../context/propertyb33/round02/twentyfour-selection/ImportAudit.lean`:
   exit 0, saved as `import-audit.log`.

The independent import prints the actual selection type and both configuration
definitions. Transitive axioms are only `propext`, `Classical.choice`, and
`Quot.sound`.

## Remaining work

The full four-lock trace redirect is now also implemented in
`TwentyFourQuadRedirect.lean`. Its `selected_of_twenty_four` is the preferred
complete structural entry point:

1. Four degree-six unit locks with only pair traces.
2. Four degree-six unit locks with exactly one triple and its uncovered pairs.
3. A complete five-degree-six edge, with all pair codegrees one or precisely
   one exceptional pair of codegree two. Every other codegree is explicitly one.
4. Five degree-six locks with exactly two disjoint exceptional pairs.
5. The strengthened two-low/three-high `MixedLocks` configuration.

For the redirect, an actual degree-six point outside the common edge replaces
one lock after deleting its at-most-one bad partner. The original common edge
then has an actual three-point trace. If there is no such point, the low set
equals the five-point edge; the four old unit locks force at most one internal
bad pair. Both conclusions are proved from actual sets and codegrees.

`lake build Aris4Math.ThirtyThree.TwentyFourQuadRedirect` exited 0
(`quad-build.log`). The independent `QuadImportAudit.lean` also includes an
actual `Fin 24` caller under just pair covering and 33 edges, and prints the
transitive axioms of the complete selection theorem. This is a selection result,
not a 24-point Property B theorem. Actual trace multiplicities, complete finite
local domains, weighted bad-pair deletion, strict numerical bounds, and the final
probability caller remain to be connected.
No new external-model review has been conducted by this subagent.

## Completed four-low all-pairs probability branch

`TwentyFourFourLow.propertyB_of_four_pairs` now concludes actual `PropertyB H`
from `H : Simple5Hypergraph (Fin 24)`, pair covering, 33 edges, and four actual
degree-six unit locks whose real multipoint traces are all pairs. The proof:

- labels the actual lock set and recovers all 16 true type multiplicities;
- obtains each actual bad link pair and matches its unordered type slot to one
  of seven explicit slots, with both orientations covered;
- covers every `Fin 4 → Fin 7` slot tuple (2,401 local possibilities) by one of
  twelve lock orders;
- binds all 336 finite slot weights back to the actual ordered bad-pair sum
  through `ActualBadSlot.slot_weight_lower`;
- proves the uncorrected bound is `8535/8398`, with `C` active at all four locks;
- obtains at least `78/4199 = 6/323` in real deletion and hence a bound at most
  `441/442 < 1`, then calls `propertyB_of_custom_deletion`.

`TwentyFourFourLowData.lean` contains the finite certificates. Only the exact
profile, weight and local slot calculations use `decide +kernel`; no whole
hypergraphs are searched or enumerated by the proof. The constructor-to-caller
connection is part of the Lean theorem, not a supplied certificate premise.

`lake build Aris4Math.ThirtyThree.TwentyFourFourLow` and independent
`FourLowImportAudit.lean` both exited 0; logs are `four-low-build.log` and
`four-low-import-audit.log`. The final branch declaration has only the standard
three transitive axioms. This closes one selected 24-point probability branch;
it does not complete all of the 24-point theorem or T33.

## Completed four-low single-triple probability branch

`TwentyFourTripleLow.propertyB_of_four_triple` now also returns actual
`PropertyB H` from four degree-six unit locks whose multipoint trace family is
one actual triple plus the uncovered pairs. The true triple is relabelled to
`{0,1,2}`, true edge multiplicities are recovered, all actual bad slots are
covered, and twelve lock orders suffice. The original finite domain has
`4^3 * 7 = 448` inputs; the Lean indexing pads the four-slot centers by repeating
existing slots, so the full `Fin 4 → Fin 7` theorem covers this without an
extra premise. It adds no new actual types.

The exact baseline numerators are 17,217 or 17,256 over 16,796, and all four
lock positions have an active C bound. Kernel-checked slot weights and coverage
give a strict corrected total below one for every input. `ActualBadSlot` and
`CustomDeletion` connect that inequality to actual deleted edge pairs and the
original coloring witness.

The module build (`triple-low-build.log`) and independent import
(`TripleLowImportAudit.lean`, `triple-low-import-audit.log`) exited 0. Only
`propext`, `Classical.choice`, and `Quot.sound` occur in the final theorem's
transitive axioms. The complete five-low-edge probability branch is next; its
uncorrected numeric bounds are already below one, so no new deletion lemma is
needed there.

## Completed full-five-low edge branch

`TwentyFourFullFive.propertyB_of_full_five` takes an actual 24-point, 33-edge
hypergraph and the `FullFiveLocks H` conclusion of quad redirection. It returns
`PropertyB H`; neither type multiplicities nor probability certificates are
assumed. It does not require pair covering as an additional premise.

The full edge is labeled by five actual vertices. In the exceptional-pair case,
that pair receives labels 0 and 1. Every trace on at least three selected
vertices contains a pair other than this possible exception. Such a pair has
codegree one and already belongs to the full edge, which forces the actual
edge to be that full edge. This proves the complete large-type multiplicities;
`MultiLockRecovery.actual_recovered` then derives all remaining true counts
from 33 edges, degree six, and the actual pair codegrees.

There are only two local profiles:

- Unit codegrees: the full type has multiplicity 1, every singleton 5, empty 7.
  Lock positions `(10,11,12,13,14)` give the bare bound `8071/8398 < 1`.
- One codegree-two pair `{0,1}`: the full type and that pair each have count 1,
  the two exceptional singletons have count 4, the other three count 5, empty 8.
  Positions `(10,14,11,12,13)` give the bare bound `224/247 < 1`.

The bounds here are the complete uncorrected minimum sums; no deleted pair is
needed. This simplifies the earlier candidate's full-edge argument, which had
also included a valid additional deletion. `TwentyFourFullFiveData` checks both
recovery formulas and exact numerical values in the Lean kernel. `FiveProfiles`
provides the shared complete 32-label profile realization for actual five-lock
inputs. Only the two explicit local profiles are evaluated, not hypergraphs.

Full-five module build and independent actual caller both exited 0
(`full-five-build.log`, `FullFiveImportAudit.lean`,
`full-five-import-audit.log`); only the standard three axioms occur.

`TwentyFourLowComplete.propertyB_or_matching_or_mixed` assembles all completed
24-point selection and probability lemmas. Its only premises are a genuine
`Simple5Hypergraph (Fin 24)`, pair covering, and exactly 33 edges. It returns
`PropertyB H ∨ FiveMatchingLocks H ∨ MixedLocks H`. Module build and independent
actual caller exited 0 (`low-complete-build.log`, `LowCompleteImportAudit.lean`,
`low-complete-import-audit.log`) with standard three axioms. Thus only the two
remaining five-lock probability callers are left for the full 24-point theorem.

## Completed five-low matching probability caller

`TwentyFourFiveMatchingComplete.propertyB_of_five_matching` takes an actual
`Simple5Hypergraph (Fin 24)`, exactly 33 edges, and the structural selection
output `TwentyFourSelection.FiveMatchingLocks H`. It concludes `PropertyB H`.
There is no supplied classification, type-count, probability, or certificate
premise in this theorem.

The selected vertices are labeled so that pairs `{0,1}` and `{2,3}` have
codegree two and every other distinct pair has codegree one. Every subset of
at least three labels contains a unit-codegree pair, so its actual edge-type
multiplicity is at most one. The resulting 16 Boolean large-type values obey
the real pair-codegree budgets by summing disjoint actual edge fibers.
`TwentyFourMatchingHighCatalog.classify` covers every Boolean vector satisfying
these budgets and sends it, by a matching-preserving permutation, to one of
the 18 profiles. The actual multiplicity relabeling is proved as an equality
of filtered edge sets, rather than assumed from the numerical table.

After relabeling, `TwentyFourFiveMatching.propertyB_of_large` recovers every
smaller actual multiplicity from 33 edges, degree six, and the fixed pair
codegrees. Its checked profile bound is at most `8273/8398 < 1`; the established
probability caller returns an ordinary Property B coloring witness.

The exact module compiled directly with exit 0 (`matching-complete-direct.log`).
The independent actual caller `MatchingCompleteImportAudit.lean` also imported
and checked with exit 0 (`matching-complete-import-audit.log`). It prints the
exported theorem and the transitive axioms of both that theorem and
`TwentyFourMatchingHighCatalog.classify`; both use only `propext`,
`Classical.choice`, and `Quot.sound`. This is kernel-checked Lean evidence,
not an additional cross-family review or another person's reproduction.

Commands, from `formal/` with the project `.tools/elan` environment:

```sh
lake env lean -o .lake/build/lib/lean/Aris4Math/ThirtyThree/TwentyFourFiveMatchingComplete.olean Aris4Math/ThirtyThree/TwentyFourFiveMatchingComplete.lean
lake env lean ../context/propertyb33/round02/twentyfour-selection/MatchingCompleteImportAudit.lean
```

The managed build `lake build Aris4Math.ThirtyThree.TwentyFourFiveMatchingComplete`
also exited 0 after the catalog dependency's managed build completed;
`matching-complete-build.log` records `Build completed successfully (1002 jobs)`.
