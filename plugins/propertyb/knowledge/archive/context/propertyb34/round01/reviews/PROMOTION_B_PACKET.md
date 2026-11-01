# Actual sparse promotion catalogue: scoped source review B

The T34 goal is still active and unproved in Lean. This packet concerns one
shared interface replacing repeated large Cartesian trace classifications.
Some new sources are in the serial build queue; a source review is not a
successful Lean run. Do not infer that the 23-point branch or T34 is closed.

Read these source bodies, following defining dependencies only as needed:

- `formal/Aris4Math/ThirtyFour/BoundedAllocations.lean`
- `formal/Aris4Math/ThirtyFour/LockExtension.lean` (r19 compiled)
- `formal/Aris4Math/ThirtyFour/PromotionCatalog.lean`
- `formal/Aris4Math/ThirtyFour/PromotionReconstruction.lean`
- `formal/Aris4Math/ThirtyFour/TwentyThreeFewLowBase.lean`
- `formal/Aris4Math/ThirtyFour/TwentyThreeFewLowFourCoverage.lean`
- Its split dependencies `TwentyThreeFewLowFourData.lean` and
  `TwentyThreeFewLowFourNumeric.lean` in the same directory. The lookup is a
  literal association list using equality, avoiding kernel expansion of
  large-natural-number pattern matches. The mathematical domain is unchanged.

The generator is
`context/propertyb34/round01/middle-lean/generate_fewlow_four_coverage.py`.
Original mathematical scope and tables are in
`context/propertyb34/round01/middle-math/CANDIDATE_ONE_TWO_LOW_23.md` and
`FEW_LOW23_{1_2,2_1,1_3,2_2}.json` in that directory.

For actual locks f:Fin(n+1)→Fin(v), the old exact trace T splits into edges
avoiding and containing the new lock. The latter count is promotion p(T).
The catalogue stores nonempty T; p(empty) is recovered as d−sum(nonempty p).
Every listed allocation respects old multiplicities, new degree and new-old
codegrees. The general induction proves that all actual allocations remain.
The reconstructed inventory includes all edges, including the empty type.

The first 23-point application starts from exactly six 3-lock inventories in
each low-degree family. Capacities enumerate 460/167 allocations respectively;
positive new-old codegrees retain 246/66, corresponding to 73/48 orbits under
degree-preserving permutations. These are local trace types, not hypergraphs.
The source has one kernel coverage statement per seed and an actual-H caller.
Its resulting orbit is not necessarily strict; numeric strict/residual
dispatch and all subsequent extensions remain separate unfinished obligations.

Independently back-translate the actual declarations. Attack: missing old
types; duplicate list keys; empty/new-singleton correction; truncating natural
subtraction; list capacities silently assuming independence; permutation
direction; and whether coverage is an assumption in the final actual caller.
Report concrete mathematical/interface issues and exact scope only. HERO:
do not invent unrelated security checks or generic process tasks. Read-only;
do not run Lean or regenerate the numeric probability tables. Record actual
files read and whether any command was executed. No model verdict is proof.
