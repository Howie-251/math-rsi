# Full61 triple template — independent source review

Date: 2026-10-13. Reviewer: fresh author-context-isolated Codex agent,
same-family provisional review under project ARIS `experiment-bridge`
Phase 2.5. This is not Gemini review or independent backend attestation.

**Verdict: no blocking implementation issues found.** The sources are suitable
for the separately authorized bounded preparation and first execution. This
receipt establishes source agreement with the stated necessary reduction; it
does not certify a generated CNF, a solver outcome, or the underlying proof.

## Source receipt

Read `encode.py`, `runner.py`, and `SCOPE.md` against
`proofs/dd82/n61/CONNECTED_TRIPLE_FULL_GRAPH_MODEL.md`,
`CONNECTED_TRIPLE_REPEAT_LOCAL.md`, and
`CONNECTED_TRIPLE_LAYER_INTERFACES.md`. The mathematical arguments are separate
root-managed dependencies; this review checked their use in the implementation.
Also read the actual archived definitions of `CNFEmitter`, `add_iff_and`,
`unary_thresholds`, `enforce_exact_under_condition`, and `enforce_exact` in
`context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/code/n62/n62_ab_cnf.py`,
including its guarded entry point; the full
`computations/dd82/construction/verify_hs_candidate.py`; and the installed
LRAT checker's `--no-trim`, input, and verified-exit source behavior in
`.tools/dd82-lrat-check/lrat-trim-rel-0.2.0/lrat-trim.c`.

- **Coverage and normalization:** the 61 labels form the complete disjoint
  partition. The seven fixed neighborhoods match the model. U/V and Ta/Tb
  matching normalization, then independently choosing the five non-special
  Tc and Td labels, do not consume conflicting label freedoms. The two Tb
  interface permutations remain variable. F can independently be labeled,
  with r=37 and s=38 in Case I; no C, sigma, Z cell map, or graph symmetry is
  selected. Fixed F independence and F–{gamma,delta} nonedges are exactly the
  additional layer lemma, while gamma–delta remains free.
- **Layer counts and case selector:** unconditional degrees agree with the
  layer tables. Selector false gives the Case I Tc/Td perfect matching,
  special Z-degree 5, and the two designated Z ports. Selector true gives
  degree 2 precisely at gamma's row/delta's column, degree 4 to Z from every
  Tc/Td point, and the Case II Z counts. Both case families are present in one
  CNF. The helper recurrence is an equivalence for each unary threshold;
  thresholds through target+1 suffice for exact equality. Negating the signed
  condition in the guarded clauses enables exactly the intended case. The
  inactive case's definitional counters do not constrain primary edges.
- **Original graph constraints:** every unordered pair has its own primary
  variable; there are no loop variables. All 61 full degrees equal 8. Every
  one of the 1830 pairs has coverage by its direct edge or all 59 actual middle
  vertices. Each of the 107970 path auxiliaries has all three clauses for the
  AND equivalence. Thus no hypothetical path can satisfy coverage without
  both actual edges. Conversely, a normalized target extends to the counters
  and paths by their actual values.
- **SAT acceptance:** decoding requires the SAT status line and a complete,
  consistent assignment, checks the emitted header/count and every clause,
  and saves the full 244-edge graph. The existing BFS interface consumes that
  JSON and writes exactly `candidate.verification.json`. Its traversal is
  independent of CNF witnesses and checks all original pairs. The runner adds
  exact n=61, 244 edges, all degrees 8, zero bad pairs and diameter at most 2
  to the verifier's broader target predicate. Failure does not accept a graph.
- **Terminal evidence:** solver exit 20 remains RAW_UNSAT. Certificate checking
  is a separate bounded action on the saved input/proof, with no solver
  restart. Installed checker source confirms that supplying the CNF enables
  checking and exit 20 plus `s VERIFIED` requires a checked empty clause.
  The runner additionally rejects wall timeout. UNKNOWN, resource termination,
  malformed models and unsuccessful certificate checks are not exclusions.
  Child limits and the stated maximum solve/decode/BFS budget match the code.

The imported general helpers do not use the historical n62 constants in these
call paths; neither `ABEncoder` nor the historical entry point is invoked.

## Verification performed and scope boundary

In-memory Python syntax parsing passed for both source files. A definition-only
load of `encode.py` and call to `fixed_adjacencies()` found no contradictory
fixed pairs. Direct assertions confirmed all 61 layer labels are distinct,
gamma–delta is unassigned, and both non-special Tb interface blocks remain
unassigned. No helper import, CNF preparation, solver, checker, independent BFS,
or old n62 computation was executed by this reviewer. Author sources were not
modified; no runtime counts or outcome are claimed.

Completeness here means **every original graph whose actual defect support is
connected and has a triple entry**, after the documented normalization.
`SCOPE.md` states this correctly. The root confirms that the prior accepted
connectivity theorem for arbitrary order61 targets supplies this hypothesis;
under that inherited result the model note's “whole triple-repeat branch”
therefore covers all actual triple-defect targets. That prior theorem was not
re-reviewed in this bounded implementation check.
Omitting B-connectivity clauses is a valid necessary relaxation: every SAT
model is still a full original graph, including any model with disconnected B.
No source change is needed. Whole-branch exclusion still
requires accepted reduction proofs and actual checked UNSAT evidence.
