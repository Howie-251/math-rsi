# 23-point one-low vertex with a seven-degree nonunit partner

The completed branch theorem is
`TwentyThreeLowBadHighComplete.propertyB_of_low_bad_high`: an actual simple
five-uniform hypergraph on `Fin 23`, pair covering, exactly 33 edges, exactly
one degree-six vertex, and an actual degree-six/degree-seven pair of codegree
at least two imply `PropertyB H`. This is a branch of T33, not a proof of all
23-point inputs or of T33.

The original exact positional witnesses come from
`round01/large-math/ONE_LOW_BAD_HIGH_V23.json`. The already formalized colored
ten-vertex selection chooses five locks of degrees `(6,7,7,7,7)`, with pair
`01` of codegree two or three, pair `23` of codegree one through three, and all
other distinct pairs of codegree one. A pair `23` of codegree at least four
is handled separately by `TwentyThreeHighPair.propertyB_of_high_pair`.
When pair `23` is nonunit, the actual edge-color argument excludes every edge
containing labels `1,2,3`, including traces larger than that triple.

Every three-element lock subset contains a unit pair, so every large actual
trace has multiplicity zero or one. Summing its actual edge fibers gives the
pair budgets. The shared `TwentyThreeTwoLowHighCatalog` proves coverage of all
16 Boolean high traces with maximal exceptional pair budgets `(3,3)`.
The six applicable budget pairs and the real forbidden-triple condition leave
228 labeled inputs. `TwentyThreeLowBadHighCatalog.classify` checks their
mapping to 130 saved representatives, with an explicit permutation fixing the
unique degree-six label and preserving the complete codegree matrix.

The complete smaller multiplicities are recovered from the actual 33 edges,
the actual five degrees, and the actual pair codegrees. The recovered profile
is realized by the same hypergraph used by the probability caller. The saved
total/pure bad-link deductions are represented as two nonnegative avoided-lock
dual multipliers: the avoided set is either empty or all other selected locks.
`RefinedDeletion` proves the deduction for actual bad pairs, including both
ordered directions and the exact diagonal capacity. Python transports the
witnesses and suggests multipliers; Lean checks every value independently.
The exact maximum bound over these profiles is `21877/21879 < 1`.

## Sources and verification

- Lean source prefix: `formal/Aris4Math/ThirtyThree/TwentyThreeLowBadHigh*`.
- `generate_v23_low_bad_high.py` transports the 130 profiles and computes dual
  witnesses; `generate_v23_low_bad_high_catalog.py` suggests the representative
  mappings. Both are in `computations/propertyb33/round02/`.
- `CERTIFICATES.json` preserves the exact transported counts, positions,
  multipliers, probability rows, and source group numbers.
- `numeric-build.log`: `lake build Aris4Math.ThirtyThree.TwentyThreeLowBadHighNumeric`
  exited 0. All ABC values, dual deductions, and strict final sums are checked.
- `probability-build.log`: the actual-profile probability caller
  `TwentyThreeLowBadHigh.propertyB_of_counts` built with exit 0. Its explicit
  multiplicity premise is discharged by the complete branch module.
- `catalog-direct.log` and `catalog-build.log`: the classifier's direct check
  and managed build both exited 0. The managed build completed 1011 jobs.

The final managed build `lake build Aris4Math.ThirtyThree.TwentyThreeLowBadHighComplete`
exited 0 (`complete-build.log`, 1020 jobs). The independent actual caller
`ImportAudit.lean` also exited 0 (`import-audit.log`), printing the final type
and the transitive axioms. The final theorem, classifier, strict numeric bound,
and dual certificate use only `propext`, `Classical.choice`, and `Quot.sound`.
The actual final caller exposes no profile, classification, multiplicity,
probability, or quota premise. These are local kernel checks, not cross-family
review or another person's independent reproduction.

Reproduce from `formal/` with the project's `.tools/elan` environment:

```sh
lake build Aris4Math.ThirtyThree.TwentyThreeLowBadHighComplete
lake env lean ../context/propertyb33/round02/low-bad-high/ImportAudit.lean
```
