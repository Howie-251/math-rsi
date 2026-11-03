# Connected-repeat D1 diagnostic, 2026-10-11

Both changed canonical CNFs now have **externally checked UNSAT certificates**.
Official lrat-trim 0.2.0 verified both saved binary LRAT traces in a separate
follow-up. The original solver reports retain their historical
`RAW_UNSAT_WITH_UNCHECKED_LRAT` status. These are checked CNF results, not a
Lean theorem or a complete arbitrary-graph exclusion.

This diagnostic changes the two existing canonical hard-D1 inputs by adding
exactly these necessary conditions from
`proofs/dd82/n62/CONNECTED_REPEAT_REDUCTION.md`, Section 4:

1. Every original-graph vertex is triangle-free.
2. The number of unordered pairs with actual repeat entry B=2 is at most nine.

No connectedness encoding, oddness encoding, symmetry breaker, or other
restriction is added. The prior canonical scope and coverage remain those of
the old driver and its reviewed sources. This is not an order62 exclusion.
The complete original-graph-to-CNF Lean bridge remains missing.

## Variable interpretation and coverage

The archived `code/n62/n62_ab_cnf.py` allocates primary graph edges, B selectors
and triangle-membership variables before all other auxiliaries. Preparation
regenerates the *full* count-only encoding and compares its entire variable
map, including tau and template unit assignments, with the old saved map.
The variable and clause counts also match the old D1 base.

The 62 actual triangle indicators are tau(u)=4983+u, for 0≤u≤61. In the
encoder, each incident triangle-edge contribution is A_uv AND [B_uv=1], with
fixed contributions handled separately. The core pair equations impose
B_uv=common_neighbors(u,v)+A_uv−1; adjacent B=2 is already forbidden.
The tau-false branch requires the sum of incident triangle-edge contributions
to be zero, while the tau-true branch requires two. Thus setting all tau
false imposes original-graph triangle-freeness in these inputs.

The 1,891 unordered vertex pairs partition as follows:

| Pair category | Number | Representation |
|---|---:|---|
| Pairs incident with root 0 | 61 | Template-fixed B |
| Pairs within X={1,…,8} | 28 | Template-fixed B |
| X–Y and Y–Y pairs | 1,802 | One B1 and one B2 selector per pair |

These sets are explicitly checked to be disjoint and exhaustive. Among the
89 fixed pairs, the only double is (0,9). The other pairs have B in {0,1}.
The mutual-exclusion clause and the core equations make each B2 selector
equivalent to B_uv=2. Therefore the actual unordered double count is

    d = 1 + sum(the 1802 distinct dynamic B2 selectors).

Each selector is counted once, not twice as in the encoder's weighted B-row
sum. The added bound is consequently **sum(B2 selectors)≤8**. The 593 dynamic
selectors already fixed false by each canonical input remain in the counter;
none is fixed true. They require no further constant adjustment.

## Exact added clauses

Both inputs preserve every old clause, in its original order. Only the DIMACS
header changes, and the following clauses are appended:

- The 62 unit clauses −4983 through −5044. Twelve already occur in each old
  canonical input, so fifty supply new triangle-free information.
- 62,917 defining clauses from the archive's `unary_thresholds`, with the
  1,802 B2 selectors in lexicographic unordered-pair order and maximum nine.
- The unit clause −444839, forbidding the final ninth threshold.

The exact appended DIMACS clauses are saved in each `.added.cnf`; the ordered
input variables and clause counts are saved in each `.constraints.json`.
There are 16,182 new variables, numbered 428658 through 444839, and 62,980
added clauses per case. Final sizes are:

| Case | Variables | Old clauses | Final clauses |
|---|---:|---:|---:|
| b=28 | 444,839 | 1,570,438 | 1,633,418 |
| b=41 | 444,839 | 1,570,439 | 1,633,419 |

For completeness, the counter's induction invariant is
s(i,j) iff the first i input selectors contain at least j true values.
For j=1 it encodes out iff (previous_same OR input), using three clauses
(two at the first input). For j>1 with both previous thresholds present,
write p=s(i−1,j), q=s(i−1,j−1), x=input, and z=s(i,j). Its four clauses are

    (¬p ∨ z), (¬x ∨ ¬q ∨ z),
    (¬z ∨ p ∨ x), (¬z ∨ p ∨ q).

These are exactly z iff p OR (x AND q). On the boundary where p is absent,
its three clauses encode z iff x AND q. Induction proves the threshold
semantics; forbidding s(1802,9) is exactly the desired at-most-eight bound.
All satisfying input assignments have the uniquely determined threshold
extension, so the counter introduces no unintended restriction. The existing
primitive audit also passed exhaustive checks for input sizes zero through
four (31 primary assignments) and its repeated-input check.

## Resource bounds and reproduction

Driver: `computations/dd82/n62/d1_connected_diagnostic.py`.
Preparation took 2.336 seconds on pinned CPU0. The old canonical CNFs are only
read; new outputs are isolated here. Invocations are sequential:

    python computations/dd82/n62/d1_connected_diagnostic.py --prepare-only
    python computations/dd82/n62/d1_connected_diagnostic.py --profile
    python computations/dd82/n62/d1_connected_diagnostic.py --run

Each solver starts cold with the existing CaDiCaL `--lrat`, on the same one
pinned CPU. There is one five-second profile of b=28 followed, if feasible,
by at most one 120-second run per case. The final budget is reduced if needed
to keep measured total CPU below 245 seconds, allowing for coarse CPU-limit
delivery. There are no retries or seed portfolios. Solver outputs cannot be
overwritten by this driver.

Each solver has a four-GiB address-space limit and 512-MiB per-file output
limit. CPU soft limit equals the selected budget, hard limit is one second
larger, and the outer wall limit is five seconds larger. The driver records
actual termination, CPU time, wall time, command, and trace bytes. The profile
hit the OS CPU limit after 5.334 CPU seconds (5.433 wall seconds), exit −24;
its last progress showed 5,000 conflicts and about 295 MB memory, with a
22,765,568-byte partial LRAT. It found neither SAT nor UNSAT. This was treated
as a bounded inconclusive profile, with no rerun of the profile.

A SAT candidate would be reconstructed from its actual 62-vertex adjacency
and independently checked for degree eight, diameter at most two, triangle
freeness, actual B entries/row sums, double count, and selector agreement.
At solver-run completion, no standalone CLI checker was found in the existing
environment, so the solver reports recorded RAW status. The separately
authorized follow-up below obtained an official checker. Partial LRAT traces
from interrupted or UNKNOWN searches remain non-certificates.

## Result

| Case | Status | Exit | Wall seconds | CPU seconds | Peak RSS MB | LRAT bytes |
|---|---|---:|---:|---:|---:|---:|
| b=28 profile | CPU_LIMIT, inconclusive | −24 | 5.433 | 5.334 | last progress 295 | 22,765,568 |
| b=28 bounded run | RAW_UNSAT, unchecked | 20 | 43.486 | 42.899 | 311.72 | 86,914,031 |
| b=41 bounded run | RAW_UNSAT, unchecked | 20 | 59.979 | 58.020 | 330.62 | 109,304,664 |

Both bounded runs terminated within their 120-second budgets; the final
budget did not need reduction. Total measured solver CPU including the
profile was 106.253 seconds, and total measured solver wall time was 108.898
seconds. The profile plus two declared budgets total 245 seconds. All solver
processes exited. The b=28 and b=41 final runs recorded 124,267 and 184,166
conflicts respectively.

The two global consequences make both canonical CNFs UNSAT according to
CaDiCaL, a concrete improvement over the old ten-second UNKNOWN diagnostics.
The exact solver results and commands are in `results.json` and per-run
JSON/log files. Those historical reports retain `proof_checked=false` and
`lean_graph_bridge=false`; they are superseded only on certificate status
by the separate follow-up record below.

## Independent certificate-check follow-up

The official [lrat-trim release rel-0.2.0](https://github.com/arminbiere/lrat-trim/tree/rel-0.2.0)
was downloaded into `.tools/dd82-lrat-check/`, compiled with assertions enabled
on CPU0, and passed its upstream test suite. Source/version metadata and build
logs are retained there; no checker source was modified. Its documented
[binary format](https://github.com/arminbiere/lrat-trim/blob/rel-0.2.0/NEWS.md)
supports the CaDiCaL-generated traces directly, without conversion.

`check_d1_connected_certificates.py` checked the saved CNF and binary LRAT
for each case using `lrat-trim --no-trim <cnf> <proof>`. Supplying the CNF
enables proof checking; `--no-trim` checks all added clauses. The observed
mode was backward checking all clauses without trimming. Both runs returned
exit 20 and `s VERIFIED`.

| Case | Clauses checked | Wall seconds | CPU seconds | Peak RSS KiB |
|---|---:|---:|---:|---:|
| b=28 | 1,344,762 | 1.106 | 1.000 | 247,276 |
| b=41 | 1,463,908 | 1.459 | 1.294 | 276,764 |

Both checks used one pinned CPU, with 120-second CPU/wall limits, four-GiB
address-space limit, and 512-MiB output-file limit. No SAT solver was rerun.
`certificate_checks/results.json` and its logs contain the current external
certificate results with `proof_checked=true`, `lean_kernel_checked=false`,
and `lean_graph_bridge=false`. The exact raw CNFs are now externally verified
unsatisfiable. Complete graph-to-CNF integration and Lean checking remain
separate outstanding work. No order62 exclusion or new exact N(8,2) value is
claimed by this diagnostic.

## Exact source regeneration

The complete archived base encoder, old canonical driver and new connected
driver were rerun in prepare-only mode in a temporary project directory.
All seven base/canonical/new/added CNF files agree byte-for-byte with the
saved inputs, including DIMACS headers and clause order; the complete
variable map also agrees. See `regeneration_verification.json` and
`../verify_d1_connected_regeneration.py`. The successful check took5.244s
on one CPU, with no solver/checker rerun and no hashes. An initial
preparation-only attempt encountered a symlink-path provenance mismatch;
resolving the workspace path fixed it. Temporary outputs were removed.
