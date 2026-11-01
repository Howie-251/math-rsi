# q=5 closure sources and verified actual-family pilot

The q=5 branch now has complete generated Lean **source** from the original
`MixedLocks H 5 4` input to `PropertyB H`. The complete finite collection has not
been built. One nontrivial entire uncolored source family (base 60) has passed
all of its real degree-color inputs, sparse inventory, exact numeric inequality,
and original coloring conclusion.

## Actual mathematical scope

The 374 already-enumerated uncolored unit families have 47,124 nominal choices
of five low vertices. `TwentyFiveLowColorPruning.complete` proves the following
lossless reduction, from actual `Feasible` recovered from the same hypergraph:

* 65 families contain eight distinct blocks through some vertex, so no coloring
  assigning only degrees 6 and 7 can occur. This rejection is done once/family.
* In each remaining family, every degree-six vertex belongs to the explicit set
  of vertices with block incidence at most six.
* All five-subsets of that exact set are retained: 23,759 source colorings.
* 23,507 satisfy the total edge budget and are transported by explicit
  degree-preserving permutations to the 11,692 saved representatives.
* 252 violate the total recovered edge budget. They are rejected with a full
  sparse completion certificate and the exact `not Feasible` inequality.

`Q5_COLORED_CERTIFICATES.json` records all of these rows and the 374 family
inputs. Recovering label permutations took 1.91 seconds. It was not a search
for probability layouts. The generator independently asserts every permutation
and that every one of the 11,692 saved representatives is reached.

All saved probability placements, including the 358 previously labelled
`full_subset_dp`, give a strict **bare** A/B/C bound on exact re-evaluation.
The q=5 export therefore needs no quota subtraction. This removes a genuinely
unnecessary formal obligation; it does not omit a penalty used by the proof.
`Q5_SELECTED_ROW_CERTIFICATES.json` records the chosen A/B/C row and its exact
sum for each representative. Every re-evaluated sum equals the saved bound.

## Structure: named proofs, not global table lookups

`TwentyFiveColoredColoring.Safe degree big` states that every actual 25-vertex
hypergraph with 34 edges and an actual unit lock embedding having those exact
degrees and large traces is colorable. A target representative proves Safe
once, using its exact full inventory and its numeric theorem.

Each retained classification row carries the explicit target block family and
an explicit permutation. Its finite check reads only that row. A named target
Safe theorem supplies its result. Each of the 374 source families has its own
module containing at most 126 rows. There is no global `Fin 11692` function to
look up a target or its numeric witness inside each row check.

The original actual H is connected by `TwentyFiveColoredColoring.actual`:
uncolored completeness -> transported actual low set -> exact feasibility ->
complete degree pruning -> explicit row -> target Safe -> original Property B.

## Verified pilot and causal performance diagnosis

`formal/FiveLowFamilyPilotLazy.lean`, log
`five-low-family-pilot-lazy-r2.log`, passed in 7.62 seconds with peak process RSS
2,136,192 KiB. It closes all feasible five-low inputs of original source family
60: the unique low set is `{0,1,2,3,8}`, its actual permutation reaches target
2153, and the exact numeric bound is **687/728**. The resulting `family_safe`
requires no numeric or certificate assumption. Its transitive axioms are only
`propext`, `Classical.choice`, `Quot.sound`.

Several earlier 20-second probes were stopped by the agreed guard. Their main
extra cost was **not established to be the numeric arithmetic**. A prefix with
numeric value left as an explicit hypothesis still stalled at the completion
interface. The cause was passing `SparseCompletion.complete [blocks]` directly
to a goal containing `pairCompletion big`: Lean tried to identify a literal
Finset with `List.toFinset` by unfolding the entire pair completion. Explicitly
proving the small equality and rewriting it first eliminated that expansion.
The q=9/q=8 generators already contained this equality and were unaffected.
Do not report the stopped complete files as evidence that 2153's numeric value
alone takes over 20 seconds. The fixed complete pilot verifies it successfully.

`CachedChosenRows.profileRow` places A/B/C calls **inside** the selected branch,
so reduction does not need all three expressions as already-supplied arguments.
The only mathematical requirement is `min A (min B C) <= selected`; the finite
certificate need not prove the selection optimal. No separate acceleration
factor is claimed for this change because the preceding failures also included
the completion-interface problem.

Generic standalone probes:
- `low-color-pruning-r1.log`: 2.22 s, exact completeness theorem.
- `colored-coloring-r2.log`: 2.68 s, actual coloring transfer (before the small
  `pruned_table` composition was appended; the final full pilot includes it).
- `five-low-data-probe-r1.log`: 6.92 s, exact profile/validity.
- `five-low-geometry-probe-r1.log`: 4.44 s, data and optional coefficient binding.
- `five-low-caller-frame-probe-r1.log`: 4.37 s, real count caller with the numeric
  equality explicitly parameterized; this is diagnostic, not the final pilot.

## Generated build entry points

Generator: `generate_q5_direct.py`.
Manifest: `Q5_DIRECT_BUILD_MANIFEST.json`.

Helpers, in order:
1. `CachedChosenRows`
2. `TwentyFiveColoredActual`
3. `TwentyFiveColoredRows`
4. `TwentyFiveLowColorPruning`
5. `TwentyFiveColoredColoring`

For group `j`, build `TwentyFiveFiveLowDataj`, then
`TwentyFiveFiveLowInventoryj`, then `TwentyFiveFiveLowNumericj`. Current group
size is 24; group 89 contains target 2153. The first ordinary grouped build
must be profiled before launching all groups, especially for memory. Numerical
proofs are all named per case and can be repartitioned without altering their
mathematical inputs.

`TwentyFiveFiveLowFamilyc` imports only the target groups that its explicit
rows use. Finally, `TwentyFiveFiveLowComplete` exports
`Aris4Math.ThirtyFour.TwentyFiveFiveLow.propertyB` from `MixedLocks H 5 4`.

Only the parent performs ordinary/heavy builds. This report does **not** claim
all 11,692 numeric certificates, all 374 input families, or complete T34 have
passed Lean yet.

## Generated-template follow-up

`five-low-generated-family-probe-r2.log` checks the actual generated template
for the complete retained family 60, a whole-family degree rejection (base 0),
and one of the q=5 total-budget rejection rows. PASS, 8.71 s, peak 2,156,688 KiB.
The generated `List.forall_mem_cons` proof includes an explicit empty-list tail;
a first failed template probe is retained and is not an acceptance record.
Both exported `Family60.safe` and the budget row's actual Safe theorem have
only the standard three axioms.

`Q5_COMPLETE_BUILD_ORDER.json` lists 1,844 dependency-ordered targets for this
source layout. It assumes the independent nine-lock uncolored classification
has already built. It is a source manifest, **not permission to launch the
whole queue before one ordinary 24-case group is profiled**.

`TwentyFiveComplete.lean` is the final 25-point assembly source. Its theorem
`Aris4Math.ThirtyFour.twenty_five_propertyB H cover edges` chooses among the
three already-existing actual lock-selection alternatives and invokes the
q=5, q=8, or q=9 branch internally. The assembly has not yet been built.
