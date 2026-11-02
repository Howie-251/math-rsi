# Complete variable model source review — 2026-10-18

**Same-family provisional review: no outstanding blocking issue.** This
checks implementation against the previously reviewed local
`../refined/VARIABLE_COMPLETION_DESIGN.md`. It supports the planned
root-owned n58 preparation and one bounded discovery run, without asserting
a graph, an exclusion, a runtime prediction or independent certification.

Actual scope: complete `encode.py`, `SCOPE.md` and `discovery.py`; the actual
`verify_hs_candidate.py` input/output contract; the parent runner's import
wiring; and the already examined generic unary/AND, DIMACS, clause-evaluation
and bounded-process definitions. No old mathematical proofs, historical
encoder jobs or unrelated files were reviewed.

- **The representation is exact for the stated monotone family.** Every
  vertex has a free retention bit and every old nonedge has one free
  undirected added-edge bit. Endpoint clauses enforce retention. Old edges
  remain implicit conjunctions of retention bits. Both degree inequalities
  are guarded by `keep[x]`, so a deleted vertex's retained-old-neighbor
  counter is never incorrectly constrained to degree eight. The exact
  deletion count passes negative retention literals to the generic signed
  recurrence correctly. No baseline/refined screen clauses or saved
  deletion choices are imported into the model.
- **Coverage uses real edges of the same graph.** For every old nonedge,
  the unique old common neighbor, mixed old/new paths and all two-new-edge
  paths partition the possible witnesses. Mixed terms are valid under the
  retained-endpoint and added-edge endpoint guards. Each two-new-edge
  witness is defined by a bidirectional AND. Old adjacent pairs need no
  additional clause. The asserted variable/clause totals and 74-literal
  coverage length agree with the reviewed design.
- **Sanity has meaningful positive and negative cases.** The tiny windmill
  becomes a valid four-cycle using mixed paths; omitting its new edges
  fails degree/coverage. An added edge incident to a deleted vertex fails
  its endpoint guard. The star with its center deleted and leaves completed
  to a four-cycle passes using two-new-edge paths, even though the deleted
  center's auxiliary counter is four while the degree target is two. The
  expected outcomes `[True, False, False, True]` are correct. Complete
  primary assignments extend all auxiliaries; saved clause evaluation is
  compared with explicit graph degrees and BFS. Invalid-endpoint examples
  appropriately test rejection without assuming mixed-path simplification.
- **Decode and independent verification now integrate correctly.** Decode
  checks the complete saved assignment, rebuilds actual edges, checks every
  retained degree and all BFS distances, preserves label mapping, and exits
  nonzero on a graph/model failure. Root corrected the initially missing
  top-level `n` and compact `edges` fields; the current source includes both,
  matching the existing verifier exactly. Its expected output is correctly
  read from `candidate.verification.json`. The runner accepts a target only
  after successful decoding, independent BFS, the requested order, exactly
  `4*n` edges, all degrees eight and zero bad pairs.
- **Execution and result scope are bounded correctly.** One no-proof
  CaDiCaL process receives `-t 28`, OS 30 CPU / 45 wall seconds, CPU affinity,
  4 GiB memory and 256 MiB per-file caps. There is no restart or automatic
  certificate task. Only SAT triggers separate decoding (15/20 seconds) and
  independent checking (10/15 seconds). Raw UNSAT stays
  `RAW_UNSAT_UNCERTIFIED`; UNKNOWN or process failures claim no exclusion.

This reviewer performed source inspection only: no preparation, semantic
sanity execution or solver run. Root's forthcoming preparation must supply
the actual sanity and encoding evidence; a discovered SAT model must pass
the stated decoder and independent checker before being reported as a graph.
