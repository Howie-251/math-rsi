# 23-point one-six vertex with unit codegrees to every seven

The intended branch theorem is `TwentyThreeLowUnitComplete.propertyB_of_low_unit`.
Its inputs are the actual simple five-uniform hypergraph on `Fin 23`, pair
covering, exactly 33 edges, exactly one degree-six vertex x, and unit codegree
from x to every degree-seven vertex. Its conclusion is `PropertyB H`.
The complete branch passed its managed build (1032 jobs) and independent
original Bool-coloring import audit on 2026-10-13. Both the exported branch and
its actual input/classification dependencies use only `propext`,
`Classical.choice`, and `Quot.sound`. Evidence: `complete-build.log`,
`ImportAudit.lean`, and `import-audit.log` (exit 0).

## Actual selection and five-lock branch: verified

The incidence budget gives at least 17 degree-seven vertices. A pair of such
vertices with codegree at least three is handled by
`TwentyThreeLowUnitFiveComplete.propertyB_of_high_pair`. Actual selected locks,
their multiplicities, classification into 75 representatives, and the strict
probability bound are connected. The managed build and independent original
Bool-coloring audit passed with only the three standard axioms. Detailed
commands and logs are in `../twentythree-selection/LOW_UNIT_HANDOFF.md`.

Otherwise every degree-seven pair has codegree at most two.
`TwentyThreeLowUnitSixSelection.exists_locks` constructs five degree-seven
locks and the degree-six lock. The exceptional high-high pairs form a matching
of size zero, one, or two. Actual codegrees determine ten Boolean edges;
kernel coverage of all 1024 inputs, all 26 matchings, and a checked permutation
put them in canonical positions 01 and 23. The low lock has label 5.
This actual selection and its independent import audit are complete.

## Complete large-trace family: verified

Any set of at least three of the six labels contains a unit pair, so its actual
edge multiplicity is at most one. Traces larger than five have multiplicity
zero because the original hypergraph is five-uniform. Thus the large traces
are a family of the 41 subsets of sizes three through five.

`BoundedTraceFamilies.mem_enumerate` proves, for arbitrary finite inputs, that
the include/exclude recurrence contains every family satisfying its sum
budgets. The recursive subtraction is justified component by component; no
heuristic pruning is assumed. `TwentyThreeLowUnitSixHighCatalog.covers` applies
this lemma to all 15 pair budgets, with capacity two on 01 and 23 and one
elsewhere. The kernel computes exactly the saved 611 families. The managed
build passed (970 jobs, new module 717 seconds); log `six-high-build.log`.
This is a proved local classification, not enumeration of whole hypergraphs.

For zero, one, or two exceptional pairs respectively, the actual family is one
of 352, 467, or 611 admissible labeled inputs. The generated mapping sends
these 1430 inputs to 243 representatives via explicit permutations of the five
high labels. The full classification and recovery modules now have successful
managed builds (`six-catalog-build2.log`, `six-recovery-build.log`). The first
classifier attempt exceeded the host stack; the accepted version checks
64-row blocks and proves with division/remainder that every index is covered.
It preserves the same finite domain and proposition. The classifier took 484
seconds; recovery took 5337 seconds during a period of concurrent heavy builds.

`SixActual.actual_representative` has also passed its managed build (974 jobs,
new module 2.5 seconds; `six-actual-build.log`). It constructs the actual large
family, derives all pair budgets, applies the complete classifier, composes
the actual vertex embedding with the returned permutation, and proves every
actual multiplicity equals the representative count. The final type needs
only the actual H, 33 edges and the selected degree/codegree data, not a
profile or classification witness. Its transitive axioms are the standard three.

## Probability witnesses

The 75 five-lock representatives passed the bare bound and have been formally
connected to actual inputs. For the 243 six-lock representatives, 234 use the
bare bound. Its managed computation has passed (`six-bare-build2.log`,
997 jobs); the new module used 6961 seconds of wall time during concurrent
heavy builds. All 234 strict inequalities are kernel checked.

The other nine use nonnegative avoided-lock duals. Their source group indices
are 8, 12, 15, 39, 52, 86, 95, 212, 233. The nine-case data, actual quota
interpretation, all exact numeric bounds, and actual-profile probability caller
have formally built (1007 jobs). Independent import of the actual Bool-coloring
conclusion also passed: `six-dual-build.log`, `six-dual-import-audit.log`,
`SixDualImportAudit.lean`. The audited declarations use only `propext`,
`Classical.choice`, `Quot.sound`. The tightest of these nine bounds is
19439/19448; group 212 uses the refined witness with bound 2385/2431.

`SixCounts` connects all 243 actual representative counts with the 234 bare
and nine dual cases (managed build 409 seconds). `SixActual` recovers actual
multiplicities from the selected locks and proved classification.
`LowUnitComplete` joins the five-lock and six-lock alternatives (1.9 seconds).
The resulting branch needs no representative, numeric bound, or certificate
as an extra input. The entire T33 theorem is separate: the three-low branch
and final assembly/audit are still pending at this checkpoint.

Generators are retained under `computations/propertyb33/round02/` with the
`generate_low_unit_` prefix. They propose finite data and exact witnesses;
Lean checks the relevant computations and interpretation. Cross-family reviews
are recorded separately in `../reviews/REVIEW_DISPOSITION.md`.
