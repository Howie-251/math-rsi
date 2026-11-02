# Reused delta review: per-vertex triangle upper bounds

Date: 2026-10-13. **REUSED same-family provisional delta review** by the
secondary Codex reviewer of the base and sorted implementations. This is
not a fresh independent review, an external Gemini verdict, or evidence
that a triangle instance has been prepared or solved. Earlier reviews are
unchanged and are reused for the existing base and sorted constraints.

**Verdict: correct for the stated delta; no blocking issue found.** Reviewed
the stable `triangles/encode.py`, `triangles/runner.py`, `triangles/SCOPE.md`,
and the triangle-bound section of
`proofs/dd82/construction/JOINT_BOUNDARY_COMPLETION_DIRECTION.md` after the
author confirmed stability. Read the actual affected `CNFEmitter` and
`unary_thresholds` definitions in the archived helper, the source assignment
evaluator, and the current runner's path/budget consumers. No broader review
of historical n62 work was performed.

The necessary bound is valid for every target in this domain. For a degree
8 diameter-at-most-2 graph, `B = A² + A − 7I − J` has diagonal zero,
nonnegative off-diagonal entries, and row sum `64 + 8 − 7 − n = 65 − n`.
On an adjacent pair, its entry is the actual common-neighbor count. Summing
those entries over the neighbors of v counts each triangle at v twice.
Consequently `2t(v) <= 65 − n`, giving `t(v) <= 3` at n58 and `t(v) <= 2`
at n60. This applies to actual target graphs; it does not assume the invalid
source has a nonnegative defect matrix. The source's compliance is checked
separately through its actual triangle assignment.

The added encoding faithfully expresses that necessary condition:

- Each unordered triple is visited once. Its three factors use the unchanged
  free-edge map and fixed O/O values. Any fixed-zero factor discards an
  impossible triangle; three fixed-one factors contribute one fixed triangle
  at each endpoint. A remaining triple has exactly two or three free factors:
  with one vertex in R it has two, and with at least two vertices in R it
  has three. Thus the implementation's factor-count assertion matches the
  actual input domain.
- One indicator is equivalent to the conjunction of those factors, with
  every forward clause and the reverse clause present. It is appended once
  to each of its three distinct endpoint lists. Indicators are shared across
  endpoints; no independent triangle choice or multiplicity is introduced.
  The stated predicted counts follow from the existing partition sizes and
  fixed O/O edge counts: 13424 indicators/51680 defining clauses at n58,
  and 15150/58250 at n60. These are algebraic counts, not preparation results.
- At each vertex, the fixed triangle count is subtracted from the allowed
  total. The helper supplies exact thresholds only through residual+1, and
  the implementation negates precisely that first forbidden threshold.
  This is an upper bound, not an exact triangle count or a triangle-free
  assumption. When all indicators fit, no counter is needed; a fixed excess
  correctly gives an empty clause. The actual helper's bidirectional
  recurrence has the semantics required by this call.

The sorted parent body is copied in binary, following a checked header,
and only the header and appended suffix are new. New variable allocation
starts after the parent's final variable. All earlier clause indices,
variables, row-order constraints and actual pair-coverage clauses survive.
The mapping is copied unchanged. Parent files are read only; all newly
written artifacts are confined to the selected triangle case directory.

The full saved sorted source assignment initializes the extension. The
actual defining-clause order determines each triangle and threshold value
from already known inputs without changing old values. New clauses must
all hold, and the resulting complete DIMACS is reread and evaluated. Its
false-clause list must be exactly the parent's relabeled original bad-pair
coverage list. Those clauses remain physically present. This preserves the
limited source-sanity contract without declaring the source a target.
The new conjunction sanity is confined to the added AND clauses; prior
C5 and lex sanity receipts are explicitly inherited and not rerun.

The runner changes the imported base runner's `HERE` before `main`, so
preparation, solving, decoding, candidate checking and certificate checking
use `triangles/n58/` or `triangles/n60/`. Decode separately changes the base
encoder's `HERE` and checks the complete triangle input, including all new
clauses. Original ROOT/tool paths remain intact. The local process helper
uses the wrapper's 2 GiB per-file limit; the existing 4 GiB address-space
limit, one selected CPU, 300 CPU/360 wall defaults and one-attempt behavior
are preserved. No historical action runs on import. Model validation and
independent BFS remain required for SAT, and exact-input LRAT checking
remains required for raw UNSAT. UNKNOWN proves no exclusion; even checked
UNSAT would concern only the original anchor. The bound preserves every
target and is invariant under the already reviewed R-only relabeling.

Validation by this reviewer: both Python files compiled in memory without
execution. Independent pure Boolean checks passed for all 24 two/three-edge
AND assignments, the exact threshold recurrence, and negating the first
forbidden threshold. No repository implementation was imported for these
checks. No generator, source sanity, old small sanity, solver, graph checker,
certificate checker, or graph search was executed. Actual preparation,
Gemini round 3, profile selection and execution remain root-owned.
