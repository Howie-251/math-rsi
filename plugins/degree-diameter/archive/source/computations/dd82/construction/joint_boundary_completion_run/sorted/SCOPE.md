# Joint-boundary completion with R-row label ordering

At initial source delivery, **no sorted CNF has been generated or solved**.
The implementation agent owns only this `encode.py`, `runner.py`, and
`SCOPE.md`. Original sources, prepared inputs, running or completed first
profiles, and their results remain untouched. The root owns the mathematical
and source delta review, Gemini round2, actual preparation and any later solve.
The earlier base review is not claimed as acceptance of this change.

The exact anchor is unchanged from the
[parent scope](../SCOPE.md). The representation lemma and precise clauses are
in the final section of
[JOINT_BOUNDARY_COMPLETION_DIRECTION.md](../../../../../proofs/dd82/construction/JOINT_BOUNDARY_COMPLETION_DIRECTION.md).
All original O/O edges and nonedges stay fixed. Every R-incident edge stays
free except for the original degree/coverage conditions and this proved
choice of labels. No edit radius, order61 defect condition, additional
fixed adjacency or independent cross-degree split is introduced.

## Coverage of the label choice

Keep O in its original increasing vertex order. For each vertex in R,
form its actual binary adjacency row to O. Relabel R so these rows are
lexicographically nondecreasing, moving **all** incident edges consistently,
including R/R edges. Every O label and every O/O entry is unchanged; degrees
and actual distances are invariant. There was no other label-dependent
requirement on R. Ties are allowed, so identical rows impose no internal
R/R ordering or extra relation.

Thus every graph in the anchored domain has a representative satisfying
the sorted model. This is a change of labels, not an assumption that the
graph has an automorphism. Some unsorted assignments disappear, but no
isomorphism class in the anchored domain is lost. An UNSAT result still
concerns this anchor only and cannot exclude all graphs of the order.

## Exact appended clauses

For two consecutive R rows x,y, let the prefix before the first column
be true. At column k require `prefix_k -> (NOT x_k OR y_k)`.
For every column except the last, introduce q equivalent to
`prefix_k AND (x_k=y_k)`. A nonconstant preceding prefix p uses all five
clauses:

```text
(-q, p)
(-q, -x, y)
(-q, x, -y)
(-p, -x, -y, q)
(-p, x, y, q)
```

For the first prefix p=true, the first clause is omitted and the `-p`
literals disappear, leaving four clauses. No unused prefix is introduced
after the final column. Each adjacent row pair of width m >= 2 therefore adds
m−1 variables and6(m−1) clauses. Width1 adds one lex clause and no prefix variable. This gives exactly:

| Case | R rows / O columns | Added variables | Added clauses |
|---|---:|---:|---:|
| n58 | 24 / 34 | 759 | 4554 |
| n60 | 25 / 35 | 816 | 4896 |

The prepared parent CNF is read and its header checked. Its complete **body
is copied verbatim as bytes** to the new input, preceded by the updated
header; new clauses follow that body. Every old variable ID and clause
index remains unchanged, every original pair coverage obligation remains,
and the free-edge/fixed-pair map is copied unchanged. No old input is
overwritten or shortened. `lex_constraints.json` records each new equivalent
prefix and the actual row/column orders.

## Sanity is performed on a consistently relabelled source

The original saved source is read and checked against its prepared bad-pair
and R metadata. Its rows are sorted by the actual O adjacency, using only
an R permutation. Every source edge is relabelled consistently; the source
O/O graph is identical and its21/26 bad pairs are simply permuted.

The existing encoder is then called **in memory only** on this relabelled
source, with the same fixed R, O and degree8. This does not reprepare or
rerun the base input. Since the fixed O/O values are identical, the generic
encoder has the same free-edge mapping and all the same AND/counter
definitions. Preparation confirms this by comparing every in-memory clause
directly to the retained parent input, not merely comparing counts. This
provides a complete actual-path/counter assignment for the relabelled source.

The new prefix values are computed from their exact stated Boolean
definitions. The complete sorted target DIMACS is then read and evaluated
under the combined assignment. Its false-clause list must be **exactly**
the coverage clauses of the relabelled original bad pairs. Every added lex
clause and every other original constraint must hold. The21/26 false
obligations remain physically present in the target input; no relaxed CNF
is written. The source itself remains an invalid target and is never
reported as a new construction.

Preparation saves `source_sanity.json`, the full `source.assignment.txt`,
and the actual `relabelled_source.edges`, including the complete old-to-new
vertex permutation. The prepared encoding status is written only after
these checks succeed. The prior source and all prior results are preserved.

The earlier small five-cycle sanity is inherited by its explicit project
path and is **not rerun**. For the new clauses only, preparation exhausts
all row-bit and auxiliary-prefix assignments for widths1,2,3, comparing
CNF truth with lexicographic comparison together with exact prefix equality.
This includes both directions of the prefix equivalence and permits ties.
It is a tiny Boolean check of the actual added clauses, not evidence that
the full58/60 anchors are feasible. `lex_sanity.json` records actual results
only when this preparation executes.

## Execution and decoding

The interface matches the parent runner:

```bash
python computations/dd82/construction/joint_boundary_completion_run/sorted/runner.py prepare --case n58 --cpu 1
python computations/dd82/construction/joint_boundary_completion_run/sorted/runner.py prepare --case n60 --cpu 2
```

These are prepared commands, not executed work at source delivery. Outputs
belong to `sorted/n58/` and `sorted/n60/`. The runner imports the existing
bounded joint-boundary runner and changes HERE plus the local process helper's
per-file limit to2 GiB. The first actual base profiles reached their1 GiB
proof limits before their CPU caps; this new cap responds to that observed
failure mode, while the changed clauses are a separate representation delta.
The original runner keeps its1 GiB limit and its actual results are preserved.
Project ROOT, solver, checker and independent BFS paths,4 GiB address-space
limit and per-case budget arguments retain their existing meanings. Defaults
remain300 CPU/360 wall seconds; the root controls actual selected budgets.
No process starts on import, no
new scheduler exists, and no unchanged automatic retry is added. The root
chooses any later bounded solve after reviewing actual first-profile results
and this substantive representation delta.

Decoding imports the existing encoder, changes only HERE, and calls its
existing decode function on the sorted case. It validates every old and new
clause, rebuilds the complete original graph from the unchanged edge mapping,
and saves the full candidate and model. Independent all-pairs BFS remains a
separate acceptance step. A RAW_UNSAT result requires exact-input LRAT
verification and accepted scope coverage. UNKNOWN excludes nothing.

No speedup is claimed before measurement. This change removes proved label
redundancy while leaving the artificial anchor unchanged; it is not evidence
that a longer run alone would help or that the original timeout had a known
single cause. No generator, solver, certificate checker, external call or
hash computation was performed by the author at this source-delivery stage.
