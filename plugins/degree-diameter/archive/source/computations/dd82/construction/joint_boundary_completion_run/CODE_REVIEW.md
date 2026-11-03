# Joint boundary completion source review

Date: 2026-10-13. Fresh secondary Codex review under the local
`experiment-bridge` Phase 2.5. This is a **same-family provisional source
review**, not an external Gemini verdict or an executed experiment result.

**Verdict: correct for the stated anchored domain; no blocking or
non-blocking defect found.** The implementation is suitable for the root's
bounded preparation and, after the required direction review and successful
sanities, the planned bounded profiles. This verdict does not assert that
those stages have occurred.

Reviewed the stable `encode.py`, `runner.py`, `SCOPE.md`, the governing
`proofs/dd82/construction/JOINT_BOUNDARY_COMPLETION_DIRECTION.md`, and project
instructions. Read the two actual source edge lists, whose headers are
`58 232` and `60 240`, at the paths named by both the direction and encoder.
Inspected only the reused helpers' relevant interfaces, defining-clause order,
guarded import behavior, bounded-process implementation, and independent BFS
acceptance interface. This was not a new review of old n62 reductions,
certificates, searches, or generic helper theory.

The mathematical implementation is faithful:

- `read_source` uses the saved full adjacency, validates simplicity and degree 8,
  recomputes all uncovered unordered pairs, and takes **all** their endpoints
  as R. `build_model` allocates exactly one edge variable for every R-incident
  pair and fixes every O/O pair, including nonedges. There is no seed-action,
  fiber, matching, edit-count, or trajectory restriction. The source values
  stored in the evaluation emitter do not alter emitted target clauses.
- Each degree counter counts every free incident edge and subtracts only the
  fixed O/O degree. For an outside vertex the resulting cross degree is the
  consequence of the anchor and total degree 8; no extra degree split is
  imposed. R vertices have all their incident pairs free.
- Coverage considers every unordered original pair and every possible third
  original vertex. Fixed-zero, fixed-one, and two-free-edge products are
  simplified correctly. Every two-free-edge path receives all three clauses
  of its AND equivalence. A coverage clause is omitted only for an actual
  fixed direct edge or fixed two-edge path; the witness is recorded. Removing
  repeated OR literals preserves the condition. Thus models give exactly
  degree 8 graphs of diameter at most 2 in this anchored domain, and every such
  graph extends through the path and exact-counter definitions to a model.
- Source assignment evaluation is separate from target construction. The
  current AND and unary-counter defining-clause order determines each new
  auxiliary from already assigned inputs; false degree/coverage clauses
  cannot rewrite the assignment. Preparation rereads the saved full DIMACS
  and requires its false clauses to be **exactly** the original bad-pair
  coverage clauses. All these clauses remain in the solve input. The small
  C5 check compares every one of its 128 primary assignments against separate
  degree/BFS semantics; its stated scope is appropriately limited.
- Decode requires the SAT status and a complete consistent assignment,
  reevaluates every clause of the saved input, checks that fixed and free maps
  partition all original pairs, and reconstructs the full edge list including
  fixed O/O edges. It records a candidate pending independent BFS. The runner
  accepts a target only after the separate verifier confirms the intended
  order, simplicity, exactly 4n edges, all degrees 8, no bad pairs, and diameter
  at most 2.

The runner respects the bounded experiment and its conclusion limits. It
reuses the generic subprocess function without invoking historical actions;
the encoder similarly imports definitions without instantiating or running
the historical n62 encoder. Child processes have one selected CPU, a 4 GiB
address-space limit and explicit CPU/wall limits. A solve is bounded to the
selected 3–300 CPU and 5–360 wall seconds, with defaults 300/360, a soft solver
limit two seconds below the OS CPU limit and a 1 GiB per-file cap. The final
runner limit change was read and syntax-checked after the initial source
review. Preparation has 30/45 CPU/wall seconds; each SAT decode and BFS step
has 10/15. Separate LRAT checking has
90/120. Existing launch/proof/log artifacts prevent an unchanged solve retry.

SAT alone remains a candidate; raw UNSAT is not an exclusion. Certification
uses the same case's saved `input.cnf` and proof and requires both the checker's
successful verified status and no wall timeout. Even then, the conclusion is
restricted to the anchored domain. UNKNOWN, timeout, output limits and
process failures do not certify any exclusion or trigger larger R/restarts.
These boundaries agree with `SCOPE.md` and the direction.

Validation performed by this reviewer: Python `compile` on both source files
in memory passed. No encoder import, generator, small-input sanity, source
assignment check, graph checker, solver, certificate checker, or graph search
was executed. No prepared instance or computational outcome is claimed.
The root still owns actual preparation/sanity results, profile selection,
execution, and Gemini direction/result review.
