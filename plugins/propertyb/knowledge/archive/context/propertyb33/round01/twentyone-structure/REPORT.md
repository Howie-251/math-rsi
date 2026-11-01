# Actual 21-point lock selection

`formal/Aris4Math/ThirtyThree/TwentyOneStructure.lean` proves
`exists_locks_of_twenty_one` for any finite vertex type, from exactly 21 vertices,
33 simple five-element edges, and pair coverage.

It selects actual distinct vertices in the original hypergraph. The alternatives
are the four two-lock ranges or the 588, 677, 678, and 777 three-lock ranges in
`proofs/propertyb33/TWENTY_ONE.md`. In the 777 case all three actual pair
codegrees are at most two; pair coverage supplies the lower bounds. This keeps
all eight ordered binary possibilities, without a relabeling assumption.

The zero-triple 588 and 678 cases supply the literal proposition that no original
edge contains all three chosen vertices. The other triples place no additional
assumption on triple codegree; its bounds follow from actual pair counts.

The proof uses actual degree sums and good-partner budgets. In the unique-6,
unique-7 case, the union of the two xy edges after removing x and y has at most
six points. Together with at most four bad partners of x, it excludes at most
ten points from at least twelve good partners of y. This yields an actual
third point of degree eight and no triple edge.

Validation: `lake build Aris4Math.ThirtyThree.TwentyOneStructure` passed.
`ImportAudit.lean` independently imports the built module, prints its final type
and the configuration definitions, and reports only `propext`,
`Classical.choice`, and `Quot.sound`. See `build.log` and `import-audit.log`.
This is the complete structural input for the 21-point probability caller,
not by itself a Property B proof.

## Probability connection for every two-lock alternative

`TwentyOnePairAssembly.propertyB_of_pairCase` now feeds all four structural pair
ranges into the actual checked high/low probability callers. Its hypotheses are
only the original H, pair coverage, edge total, distinct selected vertices, and
`TwentyOneStructure.PairCase`. Codegree upper bounds are derived from actual
edge-filter inclusion. `tripleCodegree_zero` and `tripleCodegree_le_pairs` provide
the literal edge-filter bridges for the remaining three-lock callers.
`pair-assembly-build.log` records a successful build and standard axiom audits.

## Complete 21-point theorem

`Aris4Math.ThirtyThree.twenty_one_propertyB` now proves Property B for every
pair-covering simple 5-uniform hypergraph on `Fin 21` with exactly 33 edges.
There is no remaining lock, type-table, triple-count, or probability premise.
`TwentyOne.lean` binds the actual selected vertices to all 24 labelled numeric
configurations from `TwentyOneTriples.lean`, using actual triple-codegree bounds.
The mathematical nine 777 types appear in all eight ordered binary pair-codegree
patterns, so no unproved relabeling step is needed.

The latest `twenty-one-build.log` is a clean successful build with only the
standard three axioms for the final theorem. An earlier build succeeded but
Lean's broad `simp_all` reported an internal simproc panic while simplifying a
finite matrix; that log is preserved as `twenty-one-build-simproc.log`. Replacing
that simplification by nine explicit `exact` steps removed the diagnostic and
preserved the theorem and standard axiom dependencies.

`Assembly.lean` now actually calls the 21-point theorem. Its visible remaining
premise is reduced to 22–25 vertices (pending the separate 25-point compilation
and remaining cases). This does not yet establish the arbitrary-vertex T33.
