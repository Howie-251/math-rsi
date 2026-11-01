# Matching high-trace catalogue

Active scope: pure finite classification, module
`TwentyFourMatchingHighCatalog.lean`. The actual-H caller is owned by
`matching_actual_finish` in `TwentyFourFiveMatchingComplete.lean`.

The catalogue contains all 51 labelled admissible Boolean families of the
16 subsets of Fin5 of size>=3, given pair budgets2 on01/23 and1 elsewhere.
Each saved family maps via an explicit matching-preserving permutation to one
of the already-verified18 count tables. The reported permutation sigma maps
representative/new labels to actual/old labels, so the actual embedding is
oldVertices composed with sigma. Exact direction is checked for all51 cases.

API is fixed: largeTypes, largeTypes_injective, largeTypes_card,
largeTypes_complete, highValue, pairSum, Admissible, classify. Classify outputs
k:Fin18 and sigma:Fin5≃Fin5 preserving pairDegree and satisfying
highValue h (T.image sigma)=TwentyFourFiveMatchingData.counts k T for cardT>=3.

Current finite kernel check: fourth.log/session16551. Original Fin16→Bool
Fintype enumeration overflowed the process stack; 16 explicit Bool quantifiers
avoid that enumeration. A second speed adjustment analytically derives the ten
7-term scalar Boolean pair budgets (`admissible_fast`), independently compiled
in CheckFast.lean. Complete coverage is still checked on all2^16 assignments,
split into16 blocks; no symmetry or coverage premise is assumed. Current run
has not yet produced a completed object; no final acceptance claim.

Generator: computations/propertyb33/round02/generate_matching_catalog.py;
data source: ../twentyfour-selection/matching-high-coverage-diagnostic.json.
The generated Lean tables and formulas are untrusted inputs to kernel checks.


Update: fourth.log/session16551 completed exit0; classify standard three axioms.
Catalogue olean is available and matching_actual_finish has been notified.
Formal Lake build session58971 is running; independent ImportAudit launched.


Final acceptance: Lake build exit0 (1001 jobs; catalogue213seconds); independent
import audit exit0; standard three axioms. See REPORT.md and final logs.
