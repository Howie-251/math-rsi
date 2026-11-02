# Joint-boundary completion with explicit triangle upper budgets

This is one possible further representation delta for the existing anchored
n58/n60 mechanism. **At initial source delivery, no triangle input has been
generated or solved.** Its use remains a root decision after the actual
sorted-profile results and the next same-thread Gemini review. The author
changes only `triangles/encode.py`, `triangles/runner.py`, and this scope.
All earlier sources, inputs, assignments and results stay untouched.

The exact domain and row-label normalization are inherited from the
[base scope](../SCOPE.md) and [sorted scope](../sorted/SCOPE.md). The new
bound is the final section of
[JOINT_BOUNDARY_COMPLETION_DIRECTION.md](../../../../../proofs/dd82/construction/JOINT_BOUNDARY_COMPLETION_DIRECTION.md):
for an actual degree8 diameter2 target, nonnegative
`B=A²+A−7I−J` has row sum65−n. Its sum over A-neighbors of v is exactly
twice the number t(v) of triangles containing v. Therefore t(v)≤3 at58,
and t(v)≤2 at60. This is an inherited necessary count, not an assumption
that the graph is triangle-free or a new order61 defect restriction.

## Same graph, exact triangle indicators

Every unordered triple of original vertices is visited exactly once.
The three relevant values come from the unchanged original free-edge map
and the unchanged O/O constants. If any value is fixed zero, that triple
cannot be a triangle. If all three are fixed one, one fixed triangle is
charged at each of its three endpoints. Otherwise there are two or three
actual free edge factors; only O/O entries can be constants.

Each nonconstant possible triangle gets a single indicator q, equivalent
to the conjunction of those actual factors. All clauses are present:
`NOT q OR edge` for each factor, and `q OR NOT edge1 OR ...` for the
reverse implication. Fixed-one edges require no variable or guessed
incidence. The same indicator is then counted once in each of the three
endpoint lists. There is no independent triangle choice or B variable.

For every vertex the allowed variable-triangle count is its total budget
minus its fixed triangle count. The existing exact unary thresholds are
generated only through the first forbidden level, and that level is
negated. **Only an upper bound is imposed:** lower levels are not required
true, so zero, one, or other allowed triangle counts are retained. There
is no fixed triangle count, fixed R/O degree split, new symmetry, or new
adjacency requirement.

From the already measured R/O sizes and fixed O/O edge counts, the planned
indicator counts follow algebraically, before running this encoder:

| Case | Three free factors | Two free factors | Indicator count | Definition clauses |
|---|---:|---:|---:|---:|
| n58 | C(24,3)+C(24,2)·34=11408 | 24·84=2016 | 13424 | 51680 |
| n60 | C(25,3)+C(25,2)·35=12800 | 25·94=2350 | 15150 | 58250 |

These are predicted definition counts, **not an executed preparation**.
Counter-variable and total-clause counts, constant triangles, and measured
resource costs are saved from the actual emitter only when preparation runs.

## Complete preserved input and source-assignment sanity

The parent input is `../sorted/n58/input.cnf` or
`../sorted/n60/input.cnf`. Preparation checks its header, copies its entire
body verbatim as bytes, and appends the new definitions and upper-bound
clauses with an updated header. All previous IDs, clauses, degree equations,
lex constraints and original pair-coverage obligations remain intact.
The free-edge/fixed-pair mapping is copied unchanged.

The already saved sorted source assignment supplies every parent variable
value. New triangle and threshold values are extended through the actual
emitted equivalences, using the existing assignment evaluator. The sources
are known to obey the budget despite their uncovered pairs, and this is
checked again against the newly emitted clauses. The whole resulting target
DIMACS is read and evaluated under the extended assignment. Its false-clause
list must be exactly the parent's21/26 relabelled original bad-pair coverage
clauses; every newly appended clause must hold. Those false obligations are
still present in the real target. No relaxed input is written and the source
is never described as a valid target.

The source assignment and its exact limited sanity verdict are saved in the
new case directory. `triangle_constraints.json` records every nonconstant
triangle, its actual edge factors, each endpoint counter, fixed triangles,
and the actual source triangle counts. A new24-assignment truth-table check
covers only the actual two/three-factor conjunction clauses, including both
directions. It is not a graph feasibility test. The earlier C5 and lex
checks are explicitly inherited by path and are not rerun. No source graph
or old input is re-encoded or modified.

Every full graph in the original anchored domain already satisfies the
triangle budgets. Together with the proved R-row relabeling, it therefore
has a model of the strengthened input. A certified contradiction would
still exclude only that anchored domain. This representation may improve
propagation; no speedup or diagnosed search bottleneck is claimed in advance.

## Root-owned execution and decoding

The interface matches the existing runner:

```bash
python computations/dd82/construction/joint_boundary_completion_run/triangles/runner.py prepare --case n58 --cpu 1
python computations/dd82/construction/joint_boundary_completion_run/triangles/runner.py prepare --case n60 --cpu 2
```

These are prepared commands, not executed actions at source delivery.
Outputs belong to `triangles/n58/` and `triangles/n60/`. The runner imports
the existing bounded root runner, changes HERE, and retains the sorted
profile's2 GiB per-file limit,4 GiB address-space limit, and default
300 CPU/360 wall seconds. Only the root can decide to launch the changed
profile; no automatic retry or batch launcher is added. No process starts
on import.

Decode delegates to the existing exact decoder with HERE changed to this
directory. It checks all old and new clauses and reconstructs the complete
original edge list using the unchanged mapping. Independent all-pairs BFS
remains mandatory for a candidate. RAW_UNSAT still needs exact-input LRAT
checking and scope review; UNKNOWN or an output/resource limit proves no
exclusion. This delta is not a new run-ID reset, new anchor, or a reason
for an unchanged longer solve. No generator, solver, external request,
certificate check or hash computation was performed by the author.
