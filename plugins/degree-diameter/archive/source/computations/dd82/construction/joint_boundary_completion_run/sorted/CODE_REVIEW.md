# Reused delta review: sorted R-to-O rows

Date: 2026-10-13. **Reused same-family provisional review** by the secondary
Codex reviewer who wrote `../CODE_REVIEW.md`. This is not a fresh independent
reviewer, an external Gemini verdict, or a review of new computational results.
The earlier review remains unchanged. Its base-encoder and acceptance-chain
review is reused; only the sorting lemma, stable sorted sources, and changed
runner behavior are reviewed here.

**Verdict: no blocking issue.** The sorted encoder and wrapper correctly
implement the lossless label choice for the existing anchored domains.
One minor documentation formula clarification is listed below; it does not
affect either actual case or any emitted clause.

Reviewed the added representation argument in
`proofs/dd82/construction/JOINT_BOUNDARY_COMPLETION_DIRECTION.md`, plus
`sorted/encode.py`, `sorted/runner.py`, and `sorted/SCOPE.md` after the author
confirmed stability. Read both parent `result.json` files: each records
`SIGXFSZ`, a 1 GiB proof, and `OUTPUT_LIMIT_UNKNOWN`, with no verified target
or checked exclusion. Those are existing result records, not jobs executed
by this reviewer.

The losslessness argument is correct. O is fixed pointwise; R is invariant
as a set under arbitrary permutations of its labels. A target's adjacency
rows to O can therefore be sorted by permuting R and moving **every** edge
consistently, including R/R edges. Fixed O/O values are unchanged, and degrees
and distances are invariant. There is no further R-label-specific constraint
in the parent model. Ties are permitted. Thus every anchored target has a
sorted representative; this neither assumes a graph automorphism nor expands
the anchor.

The implementation matches the proof:

- Adjacent rows are constrained by the exact prefix equality recurrence and
  `prefix -> (not x or y)` at each column. Both directions of each prefix
  equivalence are present. The first prefix is simplified with its preceding
  prefix fixed true; the last column allocates no unused next prefix. Exact
  prefixes permit ties and make the lex condition nondecreasing. For width
  m >= 2, each row comparison has m−1 new variables and 6(m−1) clauses.
  Consequently the actual additions are 23×33 = 759 variables and 4554
  clauses for n58, and 24×34 = 816 variables and 4896 clauses for n60.
- The parent mapping and header are read. The rebuilt old model is checked
  clause by clause against the actual saved parent input, with the same
  variable and clause counts and exactly the same free/fixed maps. The target
  receives a new header, then a binary copy of the entire original body,
  then the lex clauses. No old variable or clause is renumbered or removed.
  Parent inputs are opened only for reading and all new artifacts go below
  `sorted/n58/` or `sorted/n60/`.
- Source sorting builds an explicit permutation of all original vertices,
  fixes O, and relabels every source edge and original bad pair. Rebuilding
  the original definitions in memory supplies the appropriate path/counter
  values for these relabeled edges, rather than reusing the old assignment's
  values. New prefixes are assigned from their exact recurrence. The complete
  sorted DIMACS is evaluated afresh and must fail at exactly the coverage
  clauses of the relabeled original bad pairs. Every lex clause must hold.
  All bad-pair obligations remain in the target; no relaxed input is written.
- The prior C5 sanity is explicitly inherited by path and is not rerun.
  The new small sanity tests every row-bit and prefix assignment at widths
  1, 2, and 3 against lex order plus exact prefix equality. Its limited claim
  is appropriate. `PREPARED_NOT_RUN` is saved only after the new preparation
  checks pass; this review does not claim that they have run.

Both `HERE` overrides reach their intended consumers. The sorted runner
changes the imported runner's global `HERE` before `main`, so prepare, solve,
decode, graph acceptance, and certificate checking all use the sorted case
paths. The sorted decoder likewise changes the imported encoder's `HERE`
before calling `decode`, ensuring that both original and added clauses are
checked. Project ROOT and the solver/checker/BFS paths remain the original
ones. The base runner source and earlier results are not changed.

The wrapper sets the imported process helper's actual `OUTPUT_BYTES` global
to 2 GiB, which is the value used by its resource limit and result records.
This responds to the two observed 1 GiB failures. It preserves one selected
CPU, the 4 GiB address-space limit, the 300 CPU/360 wall defaults and maxima,
and the existing one-attempt guards. It introduces no automatic retry or
execution on import. SAT still requires exact full-CNF model checking and
independent BFS; raw UNSAT still requires the exact sorted-input LRAT check.
UNKNOWN excludes nothing, and even checked UNSAT concerns only the anchor.
No speedup or future solver result follows from this source review.

Non-blocking documentation clarification sent to the author: `SCOPE.md`'s
general formula `6(m−1)` clauses needs the qualifier `m >= 2`. Width 1, which
the tiny sanity intentionally includes, has no prefix variables but has one
lex clause. The code handles it correctly; widths 34 and 35 are unaffected.

Reviewer validation: both stable Python files compiled in memory without
execution. An independent pure Boolean check confirmed the five-clause and
four-clause prefix equivalences, lex semantics for all pairs of rows of
widths 1–5, and the stated actual counts. No repository implementation was
imported by that check. No generator, old C5 sanity, full source sanity,
solver, graph checker, certificate checker, or graph search was executed.
Actual preparation, the Gemini delta review, profile execution and result
acceptance remain root-owned.
