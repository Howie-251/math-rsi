# Exact joint boundary completion at58 and60

At initial source delivery, the implementation agent has **not executed
preparation, a solver, or a certificate checker**. This is the V3 mathematical
adaptation of `experiment-bridge`. Source review, direction/result reviews,
actual bounded preparation and CPU execution belong to the root. The source
does not attest that those stages have completed.

The governing domain is
[JOINT_BOUNDARY_COMPLETION_DIRECTION.md](../../../../proofs/dd82/construction/JOINT_BOUNDARY_COMPLETION_DIRECTION.md).
`encode.py` has two explicit cases and reuses these exact saved sources:

| Case | Source graph |
|---|---|
| n58 | `../twin59_to_58_deflation_run/component.path1.edges` |
| n60 | `../fullgraph60_weighted_run/candidate.current.edges` |

Preparation reads and validates the actual full edge list: vertex bounds,
simplicity, original edge count and degree8 at every vertex. It recomputes
every original uncovered pair from the actual adjacency sets, and sets R
to **all** their endpoints. O is the complement. No minimum vertex cover,
chosen subset of bad pairs, former fiber partition, or old symmetry is used
to choose R. Preparation records the actual R/O sets and original bad pairs.

## Exact search domain

Every unordered pair with at least one endpoint in R gets a free original
adjacency Boolean, including both edges and nonedges in the source. Every
O/O pair is the Boolean constant given by the source, again including both
edges and nonedges. Together the free and constant maps cover every original
pair exactly once. There are no loop variables, auxiliary vertices, or
independently guessed incidences.

Every vertex has total degree exactly8. The degree equation subtracts its
fixed O/O contribution and counts all its free incident edges. An O vertex's
remaining R degree is therefore determined by total degree8 and the frozen
O/O graph; no further R/O degree split is imposed. In particular, vertices
in R can change all neighbors simultaneously without preserving their
original internal or cross degrees. There is no edit-radius bound, fixed
matching, group action, intermediate-loss condition, or61-point B restriction.

For every unordered pair a,b, coverage means its actual direct edge or an
actual conjunction `A_aw AND A_wb` for some third original vertex w. The
encoder simplifies only genuine constants:

- If either path edge is fixed zero, that product is zero.
- If one edge is fixed one, the product is exactly the other edge variable.
- If both edges are fixed one, there is an unconditional real two-edge path.
- If both edges are free, a fresh variable is equivalent to their AND through
  all three defining clauses.

A coverage clause is omitted only when a direct edge or a two-edge path is
already fixed true; its actual witness is saved in `coverage.json`. Otherwise
the clause retains the direct edge when free and every simplified actual path.
Repeated occurrences of the same literal in the OR are deduplicated, while
the actual path witnesses remain recorded. Zero products are omitted. There
is one recorded obligation for every original pair, regardless of whether
its clause is emitted or a fixed witness makes it a tautology.

Consequently a model defines exactly a simple degree8 diameter2 graph in
this anchored domain. Conversely, any such graph with this exact O/O
induced subgraph gives a satisfying assignment by taking its actual free
edges, actual paths and true degree-counter thresholds. This is complete
for the stated anchor; a contradiction cannot exclude all graphs at58/60.
No defect matrix, connected-defect conclusion or weight bound is imported.

## Source assignment sanity uses the full target input

Preparation writes only the **complete target** `input.cnf`. It never writes
a relaxed input with the bad-pair obligations removed. Its evaluation emitter
assigns free edges their saved-source values, then follows the emitted AND and
counter equivalences in their actual acyclic order. With each defining input
already known, the unit consequences assign its output. Degree or coverage
clauses report a violation instead of changing any input or already assigned
output. No solver is involved in this assignment construction.

After writing the target, preparation reads its DIMACS clauses afresh and
evaluates every clause under that complete source assignment. The false-clause
list must agree with the emitter evaluation **and be exactly** the coverage
clauses of the original bad pairs. Thus the saved source satisfies every
other emitted constraint, but explicitly does not satisfy the target.
All original bad-pair coverage clauses remain in the input used for solving.
This demonstrates the requested source sanity after conceptually omitting
just those clauses, without generating any alternative solver input.

`source_sanity.json` records the actual checked counts, original bad pairs,
their clause IDs, the false-clause list, and the precise limited verdict.
`source.assignment.txt` retains the complete edge/path/counter assignment.
`encoding.json` is saved with PREPARED_NOT_RUN only after these checks pass.
A failed sanity prevents that prepared status and is not a solver result.

## Small exact check of the generic encoder

Preparation also encodes an explicit five-cycle, degree2, with R={0,2} and
O={1,3,4}. The frozen O/O part contains both an edge and nonedges; seven
original edges remain free. The actual emitted small CNF is retained only
in memory. Its128 primary assignments are exhaustively extended through
the actual AND/counter definitions and checked against every emitted clause.

For each assignment a separate adjacency-list implementation computes exact
degrees and performs all-pairs BFS. CNF acceptance must agree with those
graph semantics in every one of the128 cases. The five-cycle itself is a
directly constructed positive instance. This checks the reusable encoding
on this small domain; it is not evidence of58/60 feasibility, a replacement
for source review, or a theorem that arbitrary large inputs are correct.
`small_input_sanity.json` records its actual execution when preparation runs.

## Artifacts, decoding and root-owned execution

Interface:

```bash
python computations/dd82/construction/joint_boundary_completion_run/encode.py prepare --case n58
python computations/dd82/construction/joint_boundary_completion_run/encode.py prepare --case n60
python computations/dd82/construction/joint_boundary_completion_run/encode.py decode --case n58
```

The root's runner invokes the same interface under its actual process limits.
Each case writes only inside this directory's `n58/` or `n60/` subdirectory.
Decode defaults to that case's `solver.log` and accepts an explicit `--log`.
The two source graphs are never modified.

Preparation saves the complete target CNF, its measured variable/clause counts,
free-edge mapping, all fixed pair values, exact-degree records, full original
pair-coverage records and the two sanity reports. JSON encoding fields include
`status`, `n`, `scope`, `primary_edge_variables`, `variables` and `clauses`.
The primary count means free original pairs, not the total including path
and counter auxiliaries. Source assignment evaluation does not run CaDiCaL.

SAT decoding requires a complete saved solver assignment, evaluates every
actual target clause, and reconstructs every original edge from the free map
and fixed O/O values. It preserves the full graph in `candidate.json` and
`candidate.edges`, plus `model.assignment.txt`; its status remains pending
independent BFS. The root's existing independent graph verifier must recompute
vertex count, simplicity, degrees and every pair distance from that full list.
SAT clause checking alone does not replace this graph acceptance check.

The encoder imports only the existing generic `CNFEmitter`, `enforce_exact`
and `add_iff_and` definitions (the exact counter uses the helper's unary
threshold implementation). It never instantiates the historical n62 encoder
or invokes its guarded main. The source does not install tools, schedule
jobs, start processes, make external requests, create hashes, or reread old
certificate computations.

The root selects bounded profiles after actual preparation sizes and source
review. UNKNOWN, timeout and process failure establish no obstruction. A
RAW_UNSAT result must pass independent LRAT verification against that case's
exact saved complete input before even the anchored domain can be excluded.
A failed anchor does not authorize an automatic larger R, edit-radius ladder,
unchanged restart, or arbitrary-graph nonexistence claim.
