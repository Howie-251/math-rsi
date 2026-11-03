# Adjacent-double full61 source review

**Verdict: no blocking source issue found; suitable for the specified single bounded first launch.**
Reviewed the final `encode.py`, `runner.py`, and `SCOPE.md` on 2026-10-13,
after the implementation author reported them stable. This includes the last
propagation addition, the Z-to-U/V-fiber matching degrees at encoder lines
232–245. The reviewer did not author or change those sources.

This is a bounded source review against
`proofs/dd82/n61/ADJACENT_DOUBLE_FULL_GRAPH_MODEL.md` and
`proofs/dd82/n61/ADJACENT_DOUBLE_REPEAT_LOCAL.md`, with their mathematical
imports accepted as directed. It is not a solver result, a new proof of
those imports, or independent backend attestation.

## Coverage and necessary constraints

- The labels partition exactly 61 vertices, with q=14 in S and p=20 in T.
  The four complete A neighborhoods and B rows agree with the specification.
  Read-only evaluation of the labeling functions found 604 fixed A pairs
  (62 ones, 542 zeros) and 674 fixed B pairs (one value 2, 17 values 1,
  656 zeros). The remaining 1,156 pairs receive the inherited upper bound.
- The seven partitions of 5 each produce the intended permutation, C=I+P,
  and H=1+C. All C rows and columns sum to two. Each type allocates exactly
  35 Z points and seven points to each V parent. The disjunction and pairwise
  exclusions choose exactly one selector. Only that selector forces its
  actual V-parent incidences. Unconditional U-parent incidences and the
  later independent ordinary S/T labels agree with the specified compatible
  normalization.
- All 1,830 original unordered pairs have distinct adjacency variables.
  Every pair receives all 59 genuine middle-vertex conjunctions, totaling
  107,970 paths. Each conjunction is encoded in both directions. Coverage
  uses the direct A edge and these same actual paths. Exact B counts impose
  `mu+A=1+B`; all other pairs use coverage and a negated fourth threshold,
  giving exactly `1 <= mu+A <= 3`.
- Every vertex has degree eight. All additional layer degree constraints
  agree with the proved table, including the exceptional q row and p column
  of K, their five Z neighbors, and the ordinary S/T six Z neighbors.
  The four complete B core rows, B[U]=B[V]=0, B[U/V,Z]=0, the p/q zeros,
  and the ordinary U-to-S/T unit matchings all count these same A paths.
- The direct U-fiber counts for ordinary S/T vertices are `1+delta_ij`,
  because their common neighbors with U_i are precisely their neighbors in
  Z_i. The p/q counts are one in every U fiber and, conditionally, every
  selected V fiber. The final Z-fiber constraints follow from
  `mu(U_i,z)=d_Z_i(z)=1-A(U_i,z)` and the analogous V equation; filtering
  z itself out of its fiber correctly handles the absent loop. These are
  necessary redundant counts, not additional assumptions about matchings.
- K retains every binary matrix with the prescribed row/column degrees.
  Ordinary S/T defect matchings to V and the p/q transversals are unfixed.
  No particular matching between Z fibers, automorphism, preferred
  transversal permutation, or heuristic cut is imposed. The documented
  omitted necessary B constraints enlarge the model and therefore do not
  harm the stated implication from actual graphs to satisfying assignments.

## Helpers and result handling

The archived helper was inspected read-only. Its AND clauses express the
full equivalence. Its unary recurrence expresses each threshold in both
directions; the exact and conditional-exact helpers impose the intended
counts. For unselected cases the threshold definitions impose no restriction
on A, and the conditional count clauses are inactive. The helper's sole
top-level guard is `__name__ == '__main__'`. Importing it under the encoder's
distinct name does not execute the historical main, instantiate ABEncoder,
or launch any historical branch.

The runner records a single solver launch and refuses an unchanged second
attempt in the directory. Preparation has 20 CPU/30 wall seconds; the solver
has at most 50 CPU/70 wall seconds, a default 48-second soft limit, one CPU,
4 GiB address space, and 256 MiB per solver output file. Only SAT starts
the separate 5 CPU/10 wall decode and 5 CPU/10 wall BFS children. There is
no automatic solver restart or certificate-check launch.

SAT decoding requires the complete assignment, evaluates every clause of
the saved DIMACS, decodes every original adjacency pair, requires 244 edges
and exactly one C selector, and saves the graph. The separately invoked
`verify_hs_candidate.py` builds fresh neighbor sets and runs all-pairs BFS;
it rejects loops and repeated edges. Runner acceptance additionally requires
61 vertices, 244 edges, every degree eight, no bad pair, and diameter at
most two. A decode or BFS resource failure cannot become graph acceptance.

Only solver exit 20 yields RAW_UNSAT. The separate check action requires
that status and invokes the existing `lrat-trim --no-trim` on the same saved
`input.cnf` and `proof.lrat`. Exit 20 plus the exact `s VERIFIED` line and
absence of a wall timeout are required for CHECKED_UNSAT_TEMPLATE. These
checker success conditions match its inspected source. Unknown, killed,
limited, failed, or unverified runs make no mathematical exclusion claim.

## Checks performed and boundary

Both Python sources compiled in memory. Only the pure C-type and fixed-A/B
label functions were evaluated to confirm the counts above; the helper's
top-level structure was inspected with AST. No CNF, solver, decoder, BFS,
certificate check, old search, or old Lean execution was run by this reviewer.
No source change or additional audit is requested before the bounded launch.

A later checked UNSAT would certify the saved CNF. Transferring it to every
adjacent-double graph also uses the accepted reduction and this source
coverage review; it would not exclude nonadjacent doubles or order61 itself.
