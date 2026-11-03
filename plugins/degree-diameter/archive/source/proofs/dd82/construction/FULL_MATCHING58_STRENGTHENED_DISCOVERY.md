# Full false-twin58: redundant constraints and complete conjugacy gauge

Parent run: `dd82-v3-f9-c7-20261013-0749`. This is the strengthened
discovery step requested after the actual Gemini round-3 response. It
changes the input by proved redundancy and a candidate-preserving
coordinate normalization, and disables proof logging for the one
authorized 120-CPU-second attempt. It introduces no group action.

## Preserved domain

The full false-twin58 model and its exact SAT equivalence are proved in
[FULL_MATCHING58_CNF_PREPARATION.md](FULL_MATCHING58_CNF_PREPARATION.md).
Its seven root matching blocks are identity; the remaining 21 blocks
are arbitrary permutations before imposing coverage.

The first strengthening is the 630 binary clauses proved in the final
section of that note: for each coordinate, the same-coordinate edges
among the seven outer fibres form a matching. These clauses are
consequences of the original matching and complete coverage conditions.

For the second normalization, relabel every fibre coordinate by the
same permutation $\sigma\in S_6$. Each row-source permutation $p$ becomes
$\sigma p\sigma^{-1}$, and all seven root identities remain identity.
The relabelling preserves the graph, all coverage conditions, and the
630 redundant clauses. Every permutation is conjugate to the canonical
representative with its cycle lengths in ascending order and cycles
on consecutive coordinate labels: label each original cycle in cyclic
order by the corresponding consecutive segment. This explicitly
constructs the required conjugation. Therefore restricting $Q_{12}$ to
the union of **all eleven** cycle-type representatives loses no graph
up to relabelling. No one cycle type is selected in advance.

An actual enumeration of all 720 permutations verified the eleven
cycle types and their multiplicities:

| Cycle lengths | Labelled permutations |
| --- | ---: |
| 1,1,1,1,1,1 | 1 |
| 1,1,1,1,2 | 15 |
| 1,1,1,3 | 40 |
| 1,1,2,2 | 45 |
| 1,1,4 | 90 |
| 1,2,3 | 120 |
| 1,5 | 144 |
| 2,2,2 | 15 |
| 2,4 | 90 |
| 3,3 | 40 |
| 6 | 120 |

The eleven representatives are distinct and have precisely those
cycle types. Their explicit permutations and selector variables are
saved in `full_matching58_strengthened_run/cycle_types.json`.

## Exact input change and preparation check

The source is
[`full_matching58_strengthened.py`](../../../computations/dd82/construction/full_matching58_strengthened.py),
with separate `prepare`, `solve`, and `decode` actions. The original
input, logs and result in `full_matching58_run/` are left unchanged.
The new input preserves its original 115,500-clause body byte for byte
at the line-content level, changes the DIMACS header, and appends:

- the 630 binary root-neighbour constraints;
- one clause selecting at least one of eleven new selector variables;
- six implications from each selector to the six positive edge literals
  of its representative, giving 66 further binary clauses.

The existing exactly-one row constraints make these six edges fix the
whole matching. Distinct representatives differ in at least one row,
so the matching constraints already prevent two distinct selectors
from being true. No extra selector at-most-one assumption is needed.

The resulting sizes are **37,307 variables and 116,197 clauses**:
11 new variables and 697 new clauses. `added_clauses.json` saves every
added clause, and the preparation checks the actual saved prefix and
suffix against the original input and the stated additions.

The old failed seed is relabelled by the common coordinate conjugation
needed to put its $Q_{12}$ into the canonical list. Here the actual
conjugation is the identity, since its permutation already equals
$(012)(345)$. The full new assignment includes all eleven selectors.
Evaluating the actual new CNF finds that every added clause is satisfied
and precisely the original 105 coverage clauses remain false. Their
pairs agree under the recorded relabelling. No BFS was repeated for
this unchanged graph. `sanity.json` records all checks and failed pairs.
Preparation used 0.290803948 CPU seconds and 0.421271734 wall seconds.

## Execution and interpretation

The runner permits one launch, pins the solver to CPU 0, limits it to
120 CPU seconds, 240 wall seconds and 4 GiB address space, and supplies
no proof output argument or LRAT option. It neither restarts nor resumes
after UNKNOWN.

On SAT the wrapper redirects the existing decoder's module-local output
directory to this new run in a separate process. That decoder first
checks the complete model, including all selector variables, against
every clause of the actual strengthened input; it then reconstructs
the graph using the original primary edge mapping and writes only into
the new directory. The existing standalone edge-list BFS checks any
decoded graph independently. A SAT model is not accepted as a target
before that check.

Because proof output is disabled, an UNSAT return is **RAW_UNSAT** and
does not justify any family exclusion. UNKNOWN also gives no existence
or nonexistence conclusion. Even a future certified family exclusion
would not decide arbitrary order-58 graphs without false twins.

The parent read the complete strengthened source, reused decoder and
independent BFS entry point before authorizing the launch. The single
actual run returned **UNKNOWN**, exit code 0. Its measured resources
were 117.424474 CPU seconds and 120.089353 wall seconds; the solver log
reports 844,824 conflicts, 1,488,423 decisions and a maximum resident
set size of 71.89 MB. The command's own `-t 120` limit stopped it at
approximately 120 real-time seconds, before either the 120-second OS
CPU cap or the 240-second wrapper wall cap was reached. This is the
actual stopping distinction, not an additional or resumed run.

The complete command, resources and status are saved in
[`full_matching58_strengthened_run/result.json`](../../../computations/dd82/construction/full_matching58_strengthened_run/result.json),
and the original solver output is
[`solver.log`](../../../computations/dd82/construction/full_matching58_strengthened_run/solver.log).
No model or proof was produced, so no new graph decode or BFS was run.
The unchanged 105-bad-pair graph remains a consistency seed only.

This run removes the prior proof-output cap as a stopping cause and
actually exercises the stronger, conjugacy-normalized input, but it
does not decide the full false-twin family. The changes were not tested
in a controlled performance comparison, so no speedup is claimed for
the redundant clauses or normalization individually. There was no
restart, additional solver attempt or change to the original run.
