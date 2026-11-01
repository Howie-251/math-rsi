# Complete matching high-trace catalogue

The full finite classification is now kernel checked. The direct Lean check
`fourth.log` exited0; `classify` uses only `propext`, `Classical.choice`,
`Quot.sound`. The separate actual-H caller belongs to
`TwentyFourFiveMatchingComplete.lean`, maintained by the matching actual agent.
This report certifies the finite coverage module, not by itself Property B.

There are16 possible subsets of five labels of size at least3. High trace
multiplicities are represented by Boolean flags; the actual-H caller must prove
its large traces have multiplicity at most1 and enter this representation.
For each point pair, the sum of incident large-trace flags is bounded by2 on
pairs01 and23, and by1 on the other pairs. `Admissible` states these ten budgets
in the uniform all-pairs form used by actual counting.

`covers` checks all65536 Boolean assignments and proves every admissible one
matches one of51 explicit labelled families. There is no presumed symmetry
quotient in this completeness check. `representatives` checks each51 family
against one of18 already verified complete count tables using an explicit
permutation preserving the matching pair degrees. The reported permutation
maps representative/new labels to actual/old labels:

```
highValue h (T.image sigma) = TwentyFourFiveMatchingData.counts k T
```

Thus the actual caller can relabel its embedding by oldVertices composed with
sigma, recover small traces from actual totals/degrees/codegrees, and invoke the
18-case probability theorem. The catalogue supplies actual witness indices
and permutations, not just an existence statement about unbound numeric data.

The source witness file is
`context/propertyb33/round02/twentyfour-selection/matching-high-coverage-diagnostic.json`.
The generator `computations/propertyb33/round02/generate_matching_catalog.py`
expands its data and proof statements into the new module. The Lean kernel
checks the full input domain, so correctness does not rely on trusting this
Python generator or the completeness of its saved51-item list.

To make kernel computation practical, `admissible_fast` analytically expands
the ten pair sums into seven-term Boolean sums. Complete coverage then uses16
explicit Boolean arguments, split into16 blocks. This avoids materializing the
Fintype universe of functions while checking the same full65536 assignments.
The original function-universe attempt overflowed the native process stack;
it was not treated as a pass. No `native_decide`, `sorry` or new axioms occur.

Reproduction from `formal/`, with project ELAN_HOME:

```
lake build Aris4Math.ThirtyThree.TwentyFourMatchingHighCatalog
lake env lean ../context/propertyb33/round02/matching-catalog/ImportAudit.lean
```

Formal Lake build completed successfully (1001 jobs, catalogue module213seconds),
recorded in `final-build.log`. The independent expanded-budget import audit also
exited0 (`import-audit.log`), with standard three axioms for covers, representatives
and classify. The generator was checked to reproduce the verified source exactly.
