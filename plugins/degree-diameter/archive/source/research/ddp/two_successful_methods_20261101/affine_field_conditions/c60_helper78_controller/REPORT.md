# C60 + 18 helpers: bounded UNKNOWN

The single authorized CaDiCaL call returned **UNKNOWN**, exit 0. It used
58.932141 CPU seconds and 59.122760 wall seconds. Preparation used
0.263513 CPU seconds; the tracked one-shot worker total was 59.218355
CPU seconds, below the 90-CPU scope budget. No continuation was run.

The fixed model has 44,460 variables and 145,047 clauses. It contains
60 old-vertex exact-one conditions, the 18 exact pin loads, all 129
cross-component helper-pair conditions, all 1,080 helper-old exact
three-step conditions, and only legal helper minimum-pin symmetries.
An independent paper and actual-code review found the translation
correct. The accepted source remains attributed to Bhakar.

The final solver statistics include 425,342 conflicts, 621,758 decisions,
4,803 restarts, and 822,569,173 propagations. Its solution file contains
only `c UNKNOWN`; it supplied no partial pin assignment. The canonical
CNF, full log, final statistics, command, and terminal timings are saved.

This is neither an UNSAT exclusion of the fixed model nor evidence that
the broader helper/controller family is impossible. There is no
78-vertex witness, no literal 78-edge artifact or port table, no full
56,862-vertex fiber graph, and no new accepted graph or record claim.
The F9 arbitrary-dart chart extension is a separate accepted local
interface and does not change this search result.

Artifacts: `PRED.md`, `DERIVATION.md`, `MODEL_REVIEW.md`, `MODEL.json`,
`model.cnf`, `SOLVER_STARTED.json`, `SOLVER.log`,
`SOLVER_PARTIAL_STATE.json`, `solver_solution.txt`, `HANDLE.json`, and
`TERMINAL.json`. `verify_witness.py` is prepared for a SAT witness but
was not executed because the solve returned UNKNOWN. No old fiber BFS,
Lean, Gemini, installation, Wiki, global STATE, or global edits occurred.
