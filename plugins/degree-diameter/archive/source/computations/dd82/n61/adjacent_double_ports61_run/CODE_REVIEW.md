# Adjacent-double ports61: substantive source delta review

**Verdict: no blocking source issue found. The revised parent preparation,
seven-case preparation, and one bounded launch per case are ready for the
specified execution plan. The parent CNF itself is not part of that solve plan.**

Reviewed the final stable `encode.py`, `runner.py`, `prepare_cases.py`, and
`SCOPE.md` on 2026-10-13, including the last SCOPE wording correction about
preserving the old run directory. The reviewer did not author these sources.
This reuses the accepted source review in
`../adjacent_double_full61_run/CODE_REVIEW.md` and examines the substantive
delta only. The mathematical port proof and within-cell relabeling proof
are accepted as separately checked; this note checks their implementation.

## Same actual graph and preserved prefix

The source diff retains the original adjacency allocations, seven selectors,
fixed neighborhoods and B counts, all layer/fiber constraints, and the entire
1,830-pair path/count loop in their original emission order. The added sets,
dictionary assignments, and helper-function definitions before that loop
emit no variable or clause. Collecting existing thresholds inside the loop
also emits nothing. Consequently the recorded baseline prefix preserves
the original variables and clauses. This is a source-level conclusion;
this reviewer did not generate or compare CNF artifacts.

All new port constraints are appended after that prefix. The 456 port pairs
are precisely 36 S×T pairs and 420 (S∪T)×Z pairs, disjoint from the original
fixed-B pairs. Each port bit is the already defined actual threshold
`mu+A >= 2`. Negating its existing third threshold gives `mu+A <= 2`;
original coverage still gives `mu+A >= 1`. Thus each reused bit is exactly
the actual B entry, rather than a new independent choice.

The appended constraints agree with the checked equations:

- Twelve exact counts make P=B[S,T] a variable permutation matrix.
- Thirty-five binary clauses forbid K/P overlap except at (q,p), whose
  A and B bits are left variable.
- Seventy guarded column counts impose the actual S/T-to-Z port marginals,
  using A_pz for S and A_qz for T.
- Twelve guarded row counts impose `1+[x=q]-A_xp` and its T analogue.
  The guard polarity and the special q/p target values are correct.
- The 7,140 ternary clauses forbid an A edge between two Z vertices sharing
  any one of their 12 possible S/T parents. They implement the proved
  independence theorem without prohibiting all triangles in Z or removing
  the parameter case epsilon=0, eta=1.

The 94 count records, reused-threshold mappings, strengthened bound
locations, and appended clause groups refer to the same original A and
actual path counts. K, the ordinary V defect matchings, and p/q transversal
permutations are not fixed by any new heuristic restriction.

## Seven cases and the new label normalization

`prepare_cases.py` requires the unsolved prepared parent, all seven selectors,
the correct parent DIMACS header, and absent output case directories. It
retains each complete parent clause body and adds that case's selector unit
and within-cell ordering clauses, without allocating variables.

Cell membership uses the selected type's actual V parents and the existing
seven-point U groups. Each of its 25 nonempty cells is ordered only among
its own existing Z labels. Consecutive labels receive 15 binary clauses
forbidding descending S parents and 90 four-literal clauses forbidding
descending T parents when the S parents agree. With exactly one S and T
parent per Z vertex, these express nondecreasing lexicographic order and
permit equal keys. The 35 labels across 25 cells give 10 consecutive pairs,
so each case adds 1 selector clause and 1,050 ordering clauses.

The normalization preserves every original graph up to independent Z
relabelings within its existing U/V cells. It does not preserve every
unsorted parent assignment. The metadata and SCOPE state this distinction
correctly. It neither changes the selected C type nor relabels S/T, fixes
K, fixes a V defect matching, or chooses a p/q transversal permutation.
All seven cases remain present. A computational exclusion of the full
branch requires accepted checked contradictions in every case.

Headers preserve the parent variable count and add exactly 1,051 to the
clause count. Each case copies the original edge map, preserves all seven
selector records, identifies its selected case, records both appended
clause groups, and points to shared parent constraint detail files.
Deep-copying metadata prevents one case's updates from altering another.

## Wrappers, validation, and bounded execution

The parent runner is textually unchanged from the previously reviewed
runner. Each case wrapper imports the parent module under a non-main name
and then redirects only HERE to the case directory. Project ROOT and the
solver, checker, helper, and fresh BFS paths retain their correct parent
project locations. The runner's child decoder therefore uses that case's
input, metadata, edge map and output paths. Case preparation through the
runner wrapper is explicitly rejected; the encode wrapper offers decode
only. Importing either wrapper launches no process.

The reused single-attempt guards, 50 CPU/70 wall solver maximum, one-CPU
affinity, 4 GiB address-space limit and 256 MiB solver file caps remain in
effect per case. SAT still requires complete saved-CNF assignment checking
followed by a separate fresh full-graph BFS check. A separate certificate
action still requires actual RAW_UNSAT and checks the selected case's exact
saved input/proof, requiring checker exit 20 and `s VERIFIED`. No automatic
retry, parent solve, batch launcher, or certificate launch is introduced.

## Review boundary

The three Python sources and both embedded wrapper strings compiled in
memory. The unchanged runner comparison used direct source text; no hashes
were computed. No encoder, case generator, helper test, solver, graph
decoder, BFS, or certificate checker was executed by this reviewer. No
source modification or additional review is requested before launch.

This verdict concerns source coverage and execution handling. It is not a
SAT/UNSAT result or backend attestation. UNKNOWN leaves its case open;
even a complete adjacent-double exclusion would not alone exclude all
order61 graphs.
