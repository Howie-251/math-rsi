# Concurrent C3 independent audit and C4 search, 2026-09-18

## Scope and authorization

The user authorized rechecking all eight C3 proofs and starting C4 search
concurrently. C3 execution completed at September 18 04:56:27 UTC+8, eight
VERIFIED_UNSAT cells and clean worker/controller/pipeline exits. The original
search remains immutable. The broader Trellis task remains in progress.

Accepted domain: complete ordered rank-3 signotope colorings with blue-path-5
and red-path-6 bounds and no weak 7-gon. C3 checks A[3,e], e3-e10, exact m=2,
N=23+e. Independent C3 acceptance establishes e>=3 implies m>=3 and N<=32.
C4 searches A[4,e], e4-e10, exact m=3, N=22+e=26..32. These exact searches
are valid independently; deriving the C4 row theorem requires accepted C3.
Only later accepted C4 could give N<=31. Currently the accepted bound is 33.

## Immutable anchors

- C2 acceptance: `7b16c5f84bfdc643dda27828130a6659075f26b42a41b229ae3175c920fbe7c2`.
- C3 search seal: `fa0065d64c5f1213ea6ce3f0b5377438a398ce98aa5a4f790a2a62df2760d8a0`.
- C3 completed terminal: `d16cec36911ccdf6e1901395f5da1755fb64aaf82ff3aead714310d95b07183b`.
- Repaired checker: `0e0b9f7e0aa78ce2f4f970676407d95eae6908dff2b48af212f885d137374787`.

New authoritative roots under `/data/ktqiu_hdd/math_agent/res/state_charging/`:

- `20260918_35_state_cardinality_c3_acceptance_v1` (screen m).
- `20260918_35_state_cardinality_c4_parallel_v1` (screen n).

Development/launch receipts live under
`/data/ktqiu_hdd/math_agent/tmp/c3_c4_dev_20260918`.
The one-shot launcher is `tmp/launch_c3_c4_20260918.py c3|c4`.
Both use `/opt/anaconda3/envs/forktqiu3/bin/python3.12`.

## Validation and execution

C3 acceptance passed **23 tests in 3.309 seconds**, exit 0. Program SHA-256:
`70911d306f61dd864bcf00043e0feb2f4caec66408e3a3a0c3793c20f66c8432`.
Tests cover exact coverage, predecessor gates, checker failure and peer reaping,
byte inequality, post-check drift, publication-last and stale-stop refusal.
A separate read-only structural preflight passed against completed C3 input;
it checked proof sizes but deliberately deferred full proof hashing to the
production prepare stage, so it grants no proof credit itself.

C4 search passed **28 tests in 2.335 seconds**, exit 0. Program SHA-256:
`72c0453bc05b2d99a6fa4e6194ea022a944d75ce173ef46b3ef12c3631f8e5f1`.
Tests cover seven concurrent workers, SAT/error cancellation, real disposable
AE proof generation and repaired checking, formula drift, empty proof,
invalid SAT semantics, stale stop, and pending-C3 acceptance distinction.

The new immutable generations retain the tested C2 process/formula helpers.
Generation-specific coordinates, evidence collection and theorem boundaries
are explicit in the new programs; no frozen predecessor program is edited.

C3 prepare hashes the full completed source inventory. Finalization and audit
each reconstruct all eight formulas, with separate byte-equal final replay;
audit starts eight external repaired checkers with `-t 0 -b` and no deadlines.
Post-check input/hash validation precedes the acceptance receipt. No solver
is invoked by the C3 audit pipeline.

C4 builds and seals seven CNFs, rebuilds each independently, starts seven
SAT-first searches (60-second internal/75-second outer), then unresolved cells
enter unbounded AE proof generation and repaired checking. Audited SAT or
operational errors stop owned peers. Search cannot publish C4 acceptance.

Preflight observed approximately 477 GiB memory available and 3,894 GiB disk
free, no leftover solver/checker processes, and both screen names available.
This records launch resources, not a memory/runtime guarantee. The server
does not contain `.trellis/scripts/get_context.py`; workflow/task/spec context
was read from the local repository, while all code execution stayed on Linux.

Both pipelines started at **10:43:36 UTC+8 on September 18**. Screen m is
`837144.m`, launcher PID 837145; screen n is `837150.n`, launcher PID 837152.
Initial preparation PIDs were 837164 (C3) and 837165 (C4). The workflows
automatically advance from preparation to their respective audit/search
stages; an SSH disconnect does not terminate the screen sessions.

## Live checkpoint, 10:48:32 UTC+8

C4 generated all seven formulas, passed its largest-formula deterministic
smoke and seven independent worker reconstructions, and completed SAT-first.
Seven live AE proof producers were verified against Linux command/start-time
identities, all with null outer deadlines. No terminal case status or global
stop existed; controller stderr was empty. Proof files contained 86-151 MB
at this observation and remained growing afterward.

C4 seal SHA-256:
`a03ef308c3aa5cc324e2a77e756213c7df735fcff44f12e0258baa21bce5a4ed`
(1,575,194 bytes).

| e | N | Worker PID | Proof solver PID |
|---|---|---|---|
| 4 | 26 | 837498 | 837593 |
| 5 | 27 | 837499 | 837594 |
| 6 | 28 | 837500 | 837592 |
| 7 | 29 | 837501 | 837595 |
| 8 | 30 | 837502 | 837597 |
| 9 | 31 | 837503 | 837596 |
| 10 | 32 | 837504 | 837598 |

C3 is still in `prepare`: full source-inventory hashing. Its eight proofs
total 339,215,050,579 bytes. Preparation PID 837164 had finished hashing
e3 and was reading e4 at byte position 19,348,324,352. This is active input
verification, **not yet the fresh-checker stage**. The create-only acceptance
root/seal are created after preparation succeeds; finalization and audit
then follow automatically. No new proof checker was claimed to be running
at this checkpoint. Do not restart preparation or any later stage in place.

The [80-file evidence snapshot](evidence/c3-audit-c4-started-20260918/README.md)
retains C4 seal/start receipts, both pipeline/test receipts, and the completed
C3 execution metadata. All copied sizes and SHA-256 hashes were verified.
Focused source/document whitespace checks and JSONL reference checks passed.

## Completion observed September 22

C3 independent acceptance succeeded at **September 19 06:08:29 UTC+8**, with
eight fresh checks, byte-equal final replay and clean exits. Receipt SHA-256:
`8e2322334352eb2e9c5448c653422b991e7a23677dcd18ef2a06ba2482f669fd`.
This formally establishes scoped bound 32; the historical bound-33 entries
above describe the launch checkpoint, not the accepted result.

C4 search completed all seven checked UNSAT cases at **September 22 13:25:08
UTC+8**, with terminal SHA-256
`d97177f0acda5851c2b07a21db4f3beb61e601a1b6cbeb7fb93608fb7471a9c2`.
All worker/controller/pipeline exits were zero and no global stop existed.
The [subsequent authorized workflow](c4-audit-c5-search-20260922.md) performs
seven fresh C4 checks while starting C5; neither old pipeline is rerun.
