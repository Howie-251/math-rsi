# Bounded hard-D1 diagnostic, 2026-10-11

Both canonical surviving inputs returned **UNKNOWN**, not SAT or UNSAT.
Each received one cold start with a ten-second solver budget on one pinned CPU.
The actual wall times were 10.215 and 10.096 seconds; peak resident memory was
about 305 MB. The solver processes have exited.

The canonical coverage and added necessary conditions passed the focused
PASS14 review in `reviews/dd82/proof-checker-n62-d1-reduction-20261011/`.
The b=34 case is excluded by the paper's common-neighbor argument and was
not run. Remaining representatives b=28 and b=41 are both unresolved.

Reproducible driver: `computations/dd82/n62/d1_hard_diagnostic.py`.
It can generate the archived D1 base if absent, transcribes the current
canonical JSON, adds the proved block zeros and distinguished triangle-free
facts, and records the new clauses. It imposes no historical symmetry breaker.
Base: 428657 variables, 1568399 clauses. Added conditions:
b=28 has 1322 unit clauses and 717 group clauses; b=41 has 1320 and 720.

`results.json` contains exact commands and results. The LRAT files are partial
traces from interrupted searches, about 39 and 42 MB. They are not UNSAT
certificates and were not checked. There is no complete formal CNF-to-graph
bridge. Neither run changes any mathematical exclusion or the known bounds.
No retry or longer run is scheduled on these unchanged inputs.
