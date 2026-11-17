# C3 parallel search, 2026-09-16

## Authorization, cells and mathematical boundary

The user authorized continuing to C3 after accepted C2. The inherited execution
preference is parallel cases in `forktqiu3`; use available `screen m`.
The exact eight strict cells are `A[3,e]`, e=3,...,10, exact missing ordinary
count m=2, occupied ordinary count 23, and order N=23+e=26,...,33.

Accepted C2 supplies `e>=2 => m>=2`. A counterexample to C3 has `e>=3` and
`m<3`, hence m=2 and belongs to exactly one of these eight cells. The domain
and encoding are unchanged: complete ordered rank-3 signotope colorings,
blue-path-5/red-path-6 bounds, no weak 7-gon, exact endpoint states/occupancy,
and exact cardinalities. No symmetry-breaking or N25 transition constraints
are added. A later accepted complete C3 row would yield `e>=3 => m>=3` and
bound N<=32. This search itself cannot publish that result; bound 33 remains
the currently accepted bound.

## Immutable dependencies and new root

- C2 receipt SHA-256:
  `7b16c5f84bfdc643dda27828130a6659075f26b42a41b229ae3175c920fbe7c2`.
- C2 acceptance protocol SHA-256:
  `0f722cabffb73615266ad752412096043603baaac6a3543b93438f72f6f02443`.
- C1 receipt remains pinned through C2:
  `cd362ea5385aca6218c099bf6237a934d6b9beb48c98923be0cf09562f670fd3`.
- Repaired checker SHA-256:
  `0e0b9f7e0aa78ce2f4f970676407d95eae6908dff2b48af212f885d137374787`.

New result root:
`/data/ktqiu_hdd/math_agent/res/state_charging/20260916_35_state_cardinality_c3_parallel_v1`.

The accepted formula runtime is copied byte-for-byte into a new tree. The
repaired checker and its source/regression/validation files are copied from
the sealed C2 recovery. The authoritative solver remains
`/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat`.
All production code and solver/checker execution occur on Linux.

## Execution contract

The new program `tmp/c3_parallel_campaign_20260916.py` imports the unchanged
C2 helper module for artifact hashes, create-only writes, subprocess groups,
parent-death handling, safe reaping, result classification and formula replay.
It supplies C3-specific coordinates, eight-worker supervision, accepted C2
validation, and the repaired checker command. Frozen C1/C2 code is unchanged.

Preparation first validates C2 acceptance, then generates the largest formula
twice as a determinism/size smoke and all remaining formulas. A new external
seal binds the eight canonical CNFs, metadata, runtime, tools, interpreter,
dependencies, accepted predecessors and passing tests.

Every worker reconstructs its formula before a shared eight-party barrier.
Each then runs AE SAT-first with internal 60-second and outer 75-second
limits. Unresolved or raw-UNSAT results proceed to a controlled external
`--unsat --no-binary` proof solve without deadline, then the fixed checker
with `-t 0 -b` and no deadline. Actual SAT assignments must pass the existing
independent CNF/coloring/path/state/injection/count audit. Audited SAT or
operational ERROR stops all owned peers. Partial proofs never earn credit.

Execution emits eight explicit terminal rows with `c3_proved=false` and a
required independent finalization/audit boundary. All stages are create-only;
do not restart a started or failed generation in place.

## Pre-launch checks

At the September 16 preflight, accepted C2 was present and unchanged; no C3
result root or leftover solver/checker processes existed. The server had
approximately 496 GiB memory available and 4,411 GiB disk free. Screen m was
available. This is a resource observation, not a runtime guarantee.

The initial Linux suite passed 26 tests in 2.275 seconds, including eight
parallel synthetic workers, SAT/ERROR cancellation and reaping, real AE proof
generation and repaired checking on a disposable CNF, formula drift, empty
proof rejection, invalid SAT semantic replay, and the unchanged helper suite.
A final stale-stop-before-launch regression was added before sealing.

The final Linux suite passed **27 tests in 2.285 seconds**, return code 0,
using the final program bytes with SHA-256
`69453895a8dc5db333d645d54ff6bd624e49bc67a344bb9db9bd2c6294532fe7`.
The one-shot launcher started at **10:40:47 UTC+8** in screen `703331.m`;
launcher PID 703333 and preparation PID 703340. The launcher stages CNF
preparation, seal creation and the controlled eight-worker run automatically.

## Sealed production inventory

All eight formulas were generated successfully. The protocol seal is
1,802,284 bytes with SHA-256
`fa0065d64c5f1213ea6ce3f0b5377438a398ce98aa5a4f790a2a62df2760d8a0`.
The largest formula passed exact repeated metadata/clause equality. The
controller PID is 703359; worker PIDs for e3-e10 are 703360-703367.

| e | N | Variables | Clauses | CNF bytes |
|---|---|---|---|---|
| 3 | 26 | 327546 | 1203712 | 20270043 |
| 4 | 27 | 383285 | 1404837 | 23937349 |
| 5 | 28 | 445905 | 1630561 | 27902304 |
| 6 | 29 | 515953 | 1882827 | 32341722 |
| 7 | 30 | 593997 | 2163652 | 37290921 |
| 8 | 31 | 680626 | 2475127 | 42787162 |
| 9 | 32 | 776416 | 2819338 | 48867791 |
| 10 | 33 | 882032 | 3198611 | 55572092 |

Focused source/document whitespace checks and task JSONL reference checks
passed. Repository-wide `git diff --check` reports an existing unrelated
blank line at `.trellis/workspace/astro/journal-1.md:529`; that file was not
changed by the C3 launch. The 27-test Linux suite is the execution quality gate.

## Confirmed running checkpoint

At **10:45:34 UTC+8 on September 16**, all eight SAT-first stages had ended
and eight real AE proof-producing solver processes were running. Their Linux
PID/start-time/command identities matched their create-only launch receipts;
all had null outer deadlines and `--unsat --no-binary`. Every formula replay
matched its sealed CNF. No global stop, terminal case status or controller
error was present. Each proof file already contained approximately 85-180 MB.

| e | Worker PID | Proof solver PID |
|---|---|---|
| 3 | 703360 | 703381 |
| 4 | 703361 | 703382 |
| 5 | 703362 | 703383 |
| 6 | 703363 | 703384 |
| 7 | 703364 | 703386 |
| 8 | 703365 | 703387 |
| 9 | 703366 | 703388 |
| 10 | 703367 | 703385 |

The [startup evidence snapshot](evidence/c3-started-20260916/README.md)
contains 54 byte-exact server artifacts, including the seal, passing tests,
formula replay and process receipts, plus a file/hash inventory. All copied
hashes and sizes were checked locally. This checkpoint establishes actual
parallel execution, not any completed C3 proof. Continue inspecting this
existing run; do not launch a duplicate or mutate its sealed runtime.

## Completed execution, September 18

All eight cases completed with checker-qualified VERIFIED_UNSAT at
**2026-09-18 04:56:27 UTC+8**, about 42.261 hours after pipeline launch.
Worker/controller/pipeline exits are zero and there was no global stop.
The terminal SHA-256 is
`d16cec36911ccdf6e1901395f5da1755fb64aaf82ff3aead714310d95b07183b`.

| e | N | Proof solve hours | Initial proof-check hours |
|---|---|---|---|
| 3 | 26 | 15.74 | 14.34 |
| 4 | 27 | 18.34 | 13.52 |
| 5 | 28 | 19.68 | 11.54 |
| 6 | 29 | 19.47 | 11.29 |
| 7 | 30 | 23.80 | 9.81 |
| 8 | 31 | 31.91 | 10.06 |
| 9 | 32 | 23.60 | 6.30 |
| 10 | 33 | 5.43 | 2.87 |

Read-only inspection on September 18 checked exact status/exit/log bindings,
eight unique VERIFIED verdicts, the unchanged seal and proof byte sizes.
Full proof hashes are being recomputed by the subsequently authorized
[independent C3 acceptance](c3-audit-c4-search-20260918.md), concurrently
with C4 search. Completed execution alone retains c3_proved=false and the
prior accepted bound 33 until that independent receipt succeeds.
