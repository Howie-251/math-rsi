# Refined screen source review — 2026-10-18

**Same-family provisional review; no blocking issue found.** This bounded
ARIS experiment-bridge Phase 2.5 review supports proceeding to root-owned
sanity/preparation and short discovery runs. It is not an independent
mathematical certification, solver result, or completion witness.

Actual read scope: project `AGENTS.md`, the current human-in-loop goal and
latest comment priorities; this directory's complete `screen.py` and
`SCOPE.md`; the complete parent screen and scope; saved geometry metadata
and edges; the saved n58/n59 deletion sets needed by sanity; and only the
generic emitter, unary-threshold, clause-evaluation and DIMACS-checking
helper definitions used here. Historical n61 proofs/jobs and the old n62
encoder were not reviewed or run. The baseline mathematical reduction is
inherited, rather than recertified by this source pass.

- **Encoding is correct for the stated necessary screen.** Exact unary
  counters define retained degree 7 in both directions. Choices range over
  every directed old nonedge, imply a unit-deficit source and a retained,
  unsaturated target, and give each unit source exactly one outgoing choice.
  Reciprocity correctly prevents two unit vertices from using inconsistent
  copies of an undirected edge. When a unit-to-saturated pair loses its sole
  old common neighbor, the coverage clause requires the unit vertex's new
  neighbor to lie in the saturated vertex's fixed old neighborhood. Every
  actual monotone completion supplies these choices; no deletion shape or
  extra aggregate bound is imposed. The saved edge data independently has
  324 edges and exactly one common neighbor for each of its 2,304 nonedges.
- **Decoding matches the scope.** It checks every saved DIMACS clause with a
  complete assignment, recomputes the direct predicates and both indicator
  families, and reports old bad pairs, partial added edges and capacity
  overflow. Reciprocal choices are deduplicated before counting partial
  degrees. Higher-deficit capacity and full completion are deliberately
  absent and clearly labeled; SAT must remain a partial candidate only.
- **Sanity is meaningful, with one nonblocking gap.** The eight assignments
  compare all indicators, all constraint groups and each cover clause, and
  exercise invalid source/target guards plus one-way versus reciprocal unit
  choices. Their saved prerequisites exist at both orders (32/25 unit
  vertices and 16/14 saturated vertices respectively). However, no sample
  gives one source two outgoing choices, so the false branch of
  `at_most_one_choice` is untested. Add one explicit sample with two distinct
  old-nonedge targets from the same unit source; the direct predicate and
  its CNF group should both reject it. This is a small sanity improvement,
  not an observed encoder defect.

No source changes, preparation, full semantic-sanity execution, solver,
network call or hash generation occurred in this review. Root should run
the existing sanity/preparation path for both orders; the first returned
SAT model should pass the existing decoder before any candidate analysis.

## Delta review — added sanity sample and discovery runner

**Same-family provisional; no blocking issue found.** Read only the changed
`explicit_assignments` section, updated `SCOPE.md`, new `discovery.py`, and
the parent runner's import/save wiring plus its imported generic `bounded`
helper. No experiment was executed by this reviewer.

The ninth `two_outgoing_choices` sample uses distinct old-nonedge targets
from the same unit source, so it closes the reported false-branch sanity
gap; the existing per-group comparison checks its rejection directly.

The discovery runner launches one CaDiCaL process per order with `-t 28`,
OS CPU limit 30 seconds, wall limit 45 seconds, one pinned CPU, 4 GiB address
space and 256 MiB per-file cap. It passes neither a proof option nor a proof
output path. Existing launch/log/result files prevent an unchanged repeat;
there is no restart loop or automatic certificate job. Wall timeout kills
and reaps the solver. SAT alone triggers bounded decoding (a separate
15 CPU / 20 wall seconds); only decoder success receives
`REFINED_SCREEN_SAT_CHECKED`. Exit 20 remains
`RAW_UNSAT_UNCERTIFIED`, with `proof_checked=False` and an explicit statement
that no certified exclusion or target was obtained. Imports do not invoke
historical entry points. These additions are consistent with the requested
short candidate-discovery run and its stated mathematical scope.
