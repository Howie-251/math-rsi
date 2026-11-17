# Concurrent C4 independent audit and C5 search, 2026-09-22

## Authorization and scope

The user authorized fresh independent checking of seven completed C4 proofs
and simultaneous C5 search. Both use forktqiu3, repaired checker `-t 0 -b`,
and independent new result roots. Keep all predecessor evidence immutable.
The broader layered research task remains in progress.

The domain remains complete ordered rank-3 signotope colorings with
blue-path-5/red-path-6 bounds and no weak 7-gon. Accepted C3 proves
e>=3 implies m>=3 and establishes scoped bound 32. C4 counterexamples reduce
to exact m=3, A[4,e], e4-e10, N=22+e=26..32. Successful independent acceptance
of all seven cases can establish C4 and N<=31. C5 searches exact m=4,
A[5,e], e5-e10, N=21+e=26..31. These CNFs stand alone, but C5 row publication
requires accepted C4. No C5 theorem, bound 30 or full charging is claimed.

## Predecessor evidence

C3 acceptance completed at **2026-09-19 06:08:29 UTC+8** after 19.415 hours:
eight fresh verified proof checks, byte-equal final replay, zero exits.

- Receipt SHA: `8e2322334352eb2e9c5448c653422b991e7a23677dcd18ef2a06ba2482f669fd`.
- Protocol SHA: `92fffc0f400f9b3f36f4f98a5f3c4d6c5c83fae77d3fcbd93dc660b8bb5d5280`.
- Pending final SHA: `2b5594980ce69d95b397b9954f919a4e431cc85499802b8b281e51ce35356173`.

C4 search finished at **2026-09-22 13:25:08 UTC+8** after 98.692 hours:
seven checker-qualified VERIFIED_UNSAT cells, no stop/failure/counterexample.

- Search seal SHA: `a03ef308c3aa5cc324e2a77e756213c7df735fcff44f12e0258baa21bce5a4ed`.
- Terminal SHA: `d97177f0acda5851c2b07a21db4f3beb61e601a1b6cbeb7fb93608fb7471a9c2`.
- Complete proofs total **582,325,299,205 bytes**.
- Repaired checker SHA: `0e0b9f7e0aa78ce2f4f970676407d95eae6908dff2b48af212f885d137374787`.

Read-only inspection verified all C3 fresh-check and C4 execution status,
exit and log bindings, unique VERIFIED verdicts and zero pipeline exits.
Large C4 proof hashes are recomputed by the new production audit pipeline.

## Programs, tests and boundaries

- `tmp/c4_acceptance_20260922.py`: SHA
  `49cf1c4651df308ee0fa262513712e9329bb25353442ca5a6561d49f97f771ca`.
  **25 tests passed in 4.477 seconds**, exit 0.
- `tmp/c5_parallel_campaign_20260922.py`: SHA
  `145211b26aaf2a5db34d148f8e7b0666d3a86519e200378ee20d87ce65ed0ff5`.
  **28 tests passed in 2.296 seconds**, exit 0.
- Shared `tmp/accepted_c3_gate_20260922.py`: SHA
  `1073a36647385beb3eff25cc94300a8798197ceef9952fcbf28c59913d0f0944`.
  Both tested programs bind and copy this helper into their sealed runtime.

The shared gate validates accepted C3, exact ancestors, receipt/protocol/final
bindings, eight fresh checker results and clean audit exits. C4 additionally
matches its original pending-C3 source and terminal to accepted C3's final.
Tests reject pending/false C3, wrong parents, grid errors, raw UNSAT, invalid
SAT replay, proof drift, stale stops, failed checkers and premature publication.
Real disposable external-process tests cover six-worker cancellation and
the unchanged AE/repaired-checker interface; synthetic tests grant no credit.

The C4 structural preflight exercised the real completed source with proof
size checks in place of full proof hashing. It passed all seven rows, but
does not replace production proof hashing or independent checking.

C4 chains full inventory hashing, finalization with fresh formula replay,
independent byte-equal reconstruction, seven unbounded external checker
processes, post-check full inventory validation and receipt publication last.
C5 chains deterministic CNF generation, six independent formula replays,
SAT-first 60-second internal/75-second outer limits, then unbounded AE proof
production and checking. Audited SAT or operational error stops owned peers.

## Runtime locations

Under `/data/ktqiu_hdd/math_agent/res/state_charging/`:

- `20260922_35_state_cardinality_c4_acceptance_v1`, screen m.
- `20260922_35_state_cardinality_c5_parallel_v1`, screen n.

Preparation/launch receipts:
`/data/ktqiu_hdd/math_agent/tmp/c4_c5_dev_20260922`.
Launcher: `tmp/launch_c4_c5_20260922.py c4|c5`.
Interpreter: `/opt/anaconda3/envs/forktqiu3/bin/python3.12`.

Preflight found both screen names free, approximately 483 GiB memory available
and 3,010.5 GiB disk free. The server lacks `.trellis/scripts/get_context.py`;
workflow/task/spec context was read locally, with all Python and solver work
on Linux. Every production stage is one-shot; inspect failures rather than
restarting in place. The acceptance root/seal only appear after preparation
has validated the full input inventory.

Both pipelines started at **14:39:56 UTC+8 on September 22**. Screen m is
`1216422.m`, launcher PID 1216423, initial C4 prepare PID 1216441. Screen n
is `1216426.n`, launcher PID 1216427. Preparation automatically chains to
finalization/audit or generation/search; SSH disconnection does not stop them.

## Confirmed live checkpoint, 14:43:48 UTC+8

C5 completed all six CNF generations, the largest-cell deterministic smoke,
six independent formula reconstructions and SAT-first. Six actual AE proof
producers were running with matching Linux PID/start-time/command receipts,
`--unsat --no-binary` and null deadlines. No global stop or error was present.

C5 seal: 1,347,935 bytes, SHA-256
`8e4d53797b63fa95a983c470358653f111a37eb22db36838650316dcbd1b4d5b`.

| e | N | Worker PID | Proof solver PID |
|---|---|---|---|
| 5 | 26 | 1216531 | 1216592 |
| 6 | 27 | 1216532 | 1216593 |
| 7 | 28 | 1216533 | 1216595 |
| 8 | 29 | 1216534 | 1216596 |
| 9 | 30 | 1216535 | 1216597 |
| 10 | 31 | 1216536 | 1216594 |

C4 preparation was still performing full inventory hashing. PID 1216441 had
completed e4 and was reading e5 at byte position 13,082,034,176. This is input
validation, **not yet seven fresh proof checkers**. Subsequent reconstruction,
independent audit and checker stages are automatically chained. The final
acceptance root/seal will appear only after full preparation succeeds.

The [96-file startup snapshot](evidence/c4-audit-c5-started-20260922/README.md)
preserves tested launch bytes/receipts, C5 sealed startup evidence, accepted
C3 metadata and completed C4 execution metadata. Every copied size/hash was
checked locally. Focused file whitespace and task JSONL reference checks
passed. No previous production root was modified or rerun, and no commit or
archive was performed while the broader research task remains active.
