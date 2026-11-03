# Actual four-by-four triple-repeat block

The graph-to-matrix bridge requested from Step 3 of
`proofs/dd82/n62/RECOVERED_REDUCTION.md` is complete in
`DegreeDiameter/N62TripleActualBlock.lean`.

Starting with only a finite original simple graph `G`, degree at most 8,
diameter at most 2, order 62, and an actual entry
`defectMatrix G u v = 3`, the module constructs the actual labeled
cross-repeat block and proves all four premises of the generic
four-block classification. No block symmetry, diagonal condition,
row-sum certificate, matching, or cell partition is supplied by the
caller.

Actual constructions:

* `triplePositiveLabel` labels the already proved four-point set
  `tripleExclusiveNeighbors G u v` by `Fin 4`, using its actual
  cardinality theorem.
* `tripleNegativeLabel` composes that labeling with the actual original
  matching equivalence onto `tripleExclusiveNeighbors G v u`.
* `tripleActualCrossBlock` is exactly the entry of `defectMatrix G`
  from the positive label `i` to the negative label `j`.

The graph-only connection is explicit in nine exported theorems:

* `n62_triple_exclusive_zero_triangle`: every exclusive-side vertex
  has an independent original neighborhood. If it lay in a triangle,
  both incident triangle repeats would cross to the opposite exclusive
  side, contradicting its unique original matching neighbor.
* `n62_triple_matching_repeat_neighbor_sum`: the actual repeat row
  summed over the original neighbors of another same-side vertex
  collapses to the latter's actual matching mate. All other terms
  vanish by actual repeat crossing and matching uniqueness.
* `n62_triple_matching_repeat_symmetric`: applying actual `AB = BA`
  to those two same-side vertices and using that collapse proves the
  symmetry of the matched cross-repeat entries.
* `n62_triple_labels_adj_iff`: original adjacency between the positive
  and negative labeled vertices holds exactly when their labels agree.
* `n62_triple_actual_block_symmetric`: the constructed matrix is
  symmetric by the preceding actual commutation argument.
* `n62_triple_actual_block_diagonal`: its diagonal matching edges have
  zero repeat because their exclusive endpoint is triangle-free.
* `n62_triple_actual_block_nonnegative`: actual repeat nonnegativity.
* `n62_triple_actual_block_row_sum`: the proved actual sum of three
  into the opposite exclusive side transfers through its constructed
  labeling.
* `n62_triple_actual_block_classification`: applies
  `n62_four_block_classification` with these four derived premises and
  returns a permutation of the four actual labels fixing 0, placing
  all six upper off-diagonal entries into pattern 300, 210, or 111.

The separate audit `ReviewN62TripleActualBlock.lean` prints all three
construction bodies, checks all nine theorem types, and audits the
transitive axioms of all twelve declarations. It also supplies two
original-input callers: the full actual-block classification and the
actual diagonal/row-sum conjunction. All twelve declarations use only
`[propext, Classical.choice, Quot.sound]`; both callers compile.

Validation:

```bash
cd formal
source ../.tools/lean-env.sh
export LEAN_NUM_THREADS=3 RAYON_NUM_THREADS=3
lake build DegreeDiameter.N62TripleActualBlock
lake env lean ReviewN62TripleActualBlock.lean
```

The first targeted build exited 0 in
`logs/n62-triple-actual-block-first.log` (new module time 18s).
There are no new-module warnings; the log replays existing dependency
warnings. The dedicated audit exited 0 without warnings in
`logs/n62-triple-actual-block-type-axiom-audit.log`. This was an
incremental target build plus a separate import audit under the existing
Lean 4.24.0 and pinned Mathlib v4.24.0, not a whole-project clean build.
The shared three-thread build budget was coordinated with the
`N62TripleCellDegrees` author.

No `sorry`, `native_decide`, new axiom, external enumeration, or solver
is used. Existing modules, shared imports, shared status files, and
order-63–65 work were not edited. Parent integration and cross-family
source review are separate and not claimed here.

This closes the original-graph construction and classification of the
actual four-by-four block. The next unresolved bridge is the actual
ordered-parent labeling and incidences on the remaining 24-set, followed
by elimination of patterns 300 and 210 and the analytic repeat-component
contradiction for pattern 111. No complete triple-repeat elimination or
unconditional order-62 exclusion is asserted by this module.
