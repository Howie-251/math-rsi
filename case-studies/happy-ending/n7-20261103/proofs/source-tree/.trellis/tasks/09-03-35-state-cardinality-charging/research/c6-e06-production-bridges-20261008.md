# A[6,6] production bridges search, 2026-10-08

## Live status at 14:18 UTC+8

Read-only server observation on 2026-10-08: both A[6,6] proof solvers are
still running with their original PID/start-tick/boot/argv identities.
The bridges run has elapsed 2.2345 hours (2.2342 CPU hours), with a 9.904 GB
partial proof; the compact run has elapsed 215.5844 hours (215.5518 CPU
hours), with a 562.233 GB partial proof. Neither has a solver exit, checker
start, case status, or campaign stop marker. Both solver stderr files are
empty and logs are updating. Free space is 596.717 GiB. No job was modified.

The compact A[6,7] through A[6,10] receipts still report VERIFIED_UNSAT.
This status check verified their CNF and solver/checker log hashes, matching
exit records (solver 20, checker 0, no timeout), unique `s VERIFIED` output,
and proof file sizes. It did not rehash the large proofs or run new checkers.
The C5 acceptance receipt still matches its accepted SHA-256. C6 is not yet
established; the accepted bound remains N <= 30.

Neither ongoing SAT search exposes a calibrated remaining-time estimate.
The new bridges run is too young to infer an A[6,6] speedup from it. For the
old run only, extrapolating the four completed compact checker times by
current partial-proof size gives 45.15--116.65 hours (roughly 2--5 days) of
checking **if solving ended at this size**. This is a low-confidence size
analogy, excludes remaining solve time and a later independent C6 acceptance
audit, and does not predict the bridges checker duration.

Evidence: [live status snapshot](evidence/c6-e06-dual-status-20261008-1418.json).

## Authorized scope

The user's parenthetical instruction resolves the initial two-cell wording:
launch **only a fresh A[6,6]** with the optimized bridges production code,
keep the original running A[6,6] alive, and do not rerun A[6,7]. This launch
does not restart the original five-cell compact campaign or replace any of
its formulas, proofs, runtime files or receipts.

The selected production builder matches the October 6 deployment and the
local workspace, SHA-256
`2a4600ba21a57cb1e50e8686e66c86a43ee33ad281664128b19ab3b9442ff1fe`.
Its default is `legacy_exact_with_state_path_bridges_v1`, with exact original
state/occupancy/path definitions and counters, plus entailed terminal-path
bridges. This is distinct from the retired compact encoding.

## New campaign

Authoritative root:

`/data/ktqiu_hdd/math_agent/res/state_charging/20261008_c6_e06_bridges_v1`

The new one-shot pipeline was dispatched at **12:02:34 UTC+8** in screen
`1955693.m`, using `/opt/anaconda3/envs/forktqiu3/bin/python3.12`. The old
compact A[6,6] remains in screen `1858221.n`, solver PID `1858257`.
At **12:05:48 UTC+8**, the new proof solver PID **1955731** and the original
PID **1858257** were both active with matching launch identities. The new
SAT-first stage returned UNKNOWN after 60.039 seconds; the unbounded proof
stage then started. All observed error logs were empty, and original sealed
runtime hashes and the completed e7 receipt were unchanged.

The snapshot reads ten formula-source files from the **current production
workspace**. It does not copy a predecessor's builder. A fresh process verifies
the required default, generates the formula, and independently reconstructs
its metadata and full canonical DIMACS bytes. The solver process reconstructs
the formula again before launch. Runtime copies contain no bytecode caches.

| Property | Value |
|---|---|
| Cell | A[6,6], strict mode, N=26, e=6, m=5 |
| Variables | 327,546 |
| Clauses | 1,207,312 |
| Added bridge clauses | 3,600 |
| CNF bytes | 20,344,718 |
| Seed | 0 |
| Parallelism | One new worker, alongside the preserved old solve |

Protocol SHA-256:
`41ceec2ac684bd2aa33cb6afefd368dac4ac99e92d3596d19888766e334c3a67`.
CNF SHA-256:
`500c4ec7e0c6c36014ed15a3209e9c3d53567a00115b92e0a696beb905f641dd`.

The workflow retains SAT-first 60s internal / 75s outer limits, followed by
external AE Kissat proof generation with `--unsat --no-binary --seed=0` and
no deadline. Completed nonempty proofs are checked with the repaired checker,
`-t 0 -b`, also without a deadline. SAT requires complete assignment and
independent state/count semantics. Errors affect only this new generation's
owned subprocesses. There is no code path to launch e7 or signal the old e6.

## Validation and interpretation

The adapter and unchanged controlled-process helper passed **32 Linux tests
in 27.061 seconds**, with no failures, errors or skips. These cover e6-only
selection, default-profile and mode rejection, actual Pool/process control,
real AE proof/checker execution, empty proofs, invalid SAT models, formula
drift, stale stops, rerun refusal and the six production bridge tests. The
production tests retain nonvacuous small-order entailment controls, exact
measured CNF bytes, append-only bridges, and profile-tampering rejection.
Deployment evidence is pinned separately to the October 6 validation receipt.

Implementation and test files are `tmp/c6_e06_bridges_20261008.py` and
`tmp/test_c6_e06_bridges_20261008.py`; server development records are under
`tmp/c6_e06_bridges_dev_20261008/`. The unchanged process helper is reused;
existing sealed campaign programs are not edited.

The [startup snapshot](evidence/c6-e06-bridges-started-20261008/README.md)
retains source/validation/launch/protocol/replay/process bindings and a live
observation of both e6 processes. This is a new case search, not a row theorem.
It binds the accepted C5 receipt and retains `c6_proved=false` and
`theorem_credit=false`. The current scoped bound remains **N<=30**. Later
formal recognition must independently validate the required complete cell set;
a new successful case does not automatically accept C6 or stop the old solve.
