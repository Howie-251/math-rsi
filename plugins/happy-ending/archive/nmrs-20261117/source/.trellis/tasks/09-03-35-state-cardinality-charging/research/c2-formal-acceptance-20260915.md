# C2 formal acceptance: protocol and checkpoint

## Accepted on 2026-09-16

**C2 is accepted.** The independent auditor published its receipt at
**2026-09-16 01:10:15 UTC+8**. Nine fresh proof checks passed, final
reconstruction was byte-equal, and the final post-check input validation
succeeded. The receipt has `c2_proved=true`, `C2_VERIFIED_UNSAT`, and
`certified_upper_bound=33` in the mathematical domain below.

- Receipt status: `ACCEPTED_NINE_FRESH_CHECKERS_BYTE_EQUAL`.
- Counts: nine VERIFIED_UNSAT, zero UNKNOWN, zero counterexamples.
- Receipt: 7,018 bytes, SHA-256
  `7b16c5f84bfdc643dda27828130a6659075f26b42a41b229ae3175c920fbe7c2`.
- Auditor and pipeline actual exit codes: zero; both stderr files empty.
- No global-stop receipt exists. Each of the nine checker exits is zero,
  without timeout, and each log has exactly one `s VERIFIED` verdict.
- Slowest fresh check: e8, 25,215.49 seconds (7.00 hours); the formerly
  crashing e7 passed again in 24,164.76 seconds (6.71 hours).
- On September 16 at approximately 10:23 UTC+8, read-only revalidation passed
  receipt fields, exact coverage, pinned seal/final/scope/C1 bindings, all
  checker status/exit/log hashes and verdicts, and wrapper exit/log bindings.
  No production stage or proof check was rerun for this status inspection.
- [26 lightweight accepted artifacts](evidence/c2-accepted-20260916/README.md)
  are retained locally; receipt, protocol and final hashes match the server.

The pending final remains unchanged with `c2_proved=false`; the separate
accepted receipt supplies publication authority. Sections below preserve the
protocol and historical launch observations, including their then-pending
status. C3 and higher layers remain open.

## Authorization and publication boundary

The user authorized formal C2 recognition on 2026-09-15. The original C2
generation and its checker-repair recovery are completed, immutable inputs.
The dedicated acceptance program is `tmp/c2_acceptance_20260915.py`.
Preparation, finalization and independent audit are create-only stages. No
production solver is called. All code and proof checking run on Linux using
`forktqiu3`; the desktop is only used to author and retain files.

The new acceptance root is
`/data/ktqiu_hdd/math_agent/res/state_charging/20260915_35_state_cardinality_c2_acceptance_v1`.

The pending final and the earlier execution terminals retain `c2_proved=false`.
Only an independently completed audit may write
`campaign_acceptance_audit.json` with `c2_proved=true` and bound 33. A failed,
interrupted or ambiguous stage is not retried in place.

## Mathematical scope

The domain is the class of complete ordered rank-3 two-color signotope
colorings satisfying the blue-path-5 and red-path-6 bounds and containing no
weak 7-gon. The definitions and encoding-faithfulness argument are in the
separately sealed `cardinality-layer-theorem.md` snapshot. Endpoint states are
injective, with 25 ordinary and 10 exceptional types, so

`N = 25 + e(X) - m(X)`.

C1 is the already accepted statement `e(X)>=1 => m(X)>=1`. Suppose C2 fails:
`e(X)>=2` and `m(X)<2`. C1 forces `m(X)=1`; hence `e` is one of 2 through 10
and `N=24+e`. This is exactly one of the nine canonical strict cells
`A[2,e]`. Fresh reconstruction binds each checked CNF to its audited semantic
cell. Checked UNSAT of all nine cells excludes every C2 counterexample.

After acceptance, C2 therefore states `e(X)>=2 => m(X)>=2`. If `e=0`, the
identity gives `N<=25`; if `e=1`, C1 gives `N<=25`; if `e>=2`, C2 and `e<=10`
give `N<=25+10-2=33`. This is neither the full inequality `m>=e` nor a proof
of `N<=25`. Until acceptance, the certified bound remains C1's `N<=34`.

## Evidence checks

- Bind the externally recorded original seal, recovery seal, repaired checker
  and accepted C1 receipt; validate C1's final/protocol references.
- Hash both source trees, including all complete and interrupted historical
  proofs. Match the original inventory to its recovery-seal snapshot.
- Validate exact e2-e10 coverage, disjoint owners, exited processes, exact
  commands, actual solver/checker exits, logs, retained-proof provenance and
  all expected case artifacts. Imported e2-e5/e10 require their original zero
  worker exits; e6/e7 reuse completed proofs; e8/e9 use recovery proofs.
- A new immutable input inventory binds the completed recovery outputs too.
- Finalization freshly reconstructs all nine formulas; no extra symmetry or
  N25 transition clauses are added. The final is deterministic and pending.
- A separate auditor reconstructs all formulas and exactly the same final
  bytes, then launches nine independent external proof checks in parallel
  using the repaired checker with `-t 0 -b` and no wrapper deadline.
- Any check failure cancels the audit's owned processes and forbids acceptance.
  Successful checks are followed by another complete input hash validation
  and byte-equal final reconstruction. Acceptance is published last.

## Validation and staged launch

- The Linux unittest suite passed 21 tests in 4.301 seconds using the exact
  final program. The preceding development revision also passed 21 tests.
- A complete read-only real-input preflight passed all nine cells, original
  inventory equality, proof/exit/log bindings, process ownership and C1 gates.
- Final program: 27,327 bytes, SHA-256
  `75d0d74d88d1cf8aba75a6776853559f90ab329e212c4d69460ae6e0bd5ef79b`.
- Scope snapshot: SHA-256
  `4dcb6cdf20e21af1f51e272dca891e377979884ba9ce53d8010a9582fdaba820`.
- Launcher: 3,295 bytes, SHA-256
  `c22df04821a48391bca126a8cdb9ab13b41324c2a10022785a4a86f5352fad3e`.
- `screen 391833.m` was created on 2026-09-15 at 17:47:18 UTC+8. The
  pipeline PID is 391835, running in `forktqiu3`. These PIDs are historical
  observations and must not be used for signaling without identity checks.
- Startup checks confirmed empty pipeline/prepare stderr and byte-equal
  tested interpreter/helpers. Preparation was hashing input proofs at 17:47:49.

Development validation and launcher records live at
`/data/ktqiu_hdd/math_agent/tmp/c2_acceptance_dev_20260915`.
The launcher invokes prepare, finalize and audit in distinct processes,
checks each real return code, and passes actual seal/final hashes between
stages. It has no retry path. Watch the existing pipeline and do not launch
another prepare/finalize/audit when returning to this checkpoint.

Preparation completed and the finalizer started by 17:51:16 UTC+8:

- Acceptance seal: 42,451 bytes, SHA-256
  `0f722cabffb73615266ad752412096043603baaac6a3543b93438f72f6f02443`.
- Input inventory: 79,679 bytes, SHA-256
  `ccaf2156a388c6db04a769750a5c839337f8f7d11bfc5c28e1a7c9857f97271a`.
- Five lightweight server artifacts are copied byte-for-byte into
  `evidence/c2-acceptance-started-20260915`; local seal/inventory hashes match.
- At 17:52:35 the finalizer was validating original proof bindings, with empty
  stderr. The independent audit had not started at that observation.

### Finalization completed; independent audit running

The finalizer completed at **2026-09-15 17:58:18 UTC+8**, with real process
returncode zero and empty stderr. All nine fresh formula reconstructions
reported `FORMULA_MATCH`.

- `cardinality_c2_resolved_final.json`: 19,021 bytes, SHA-256
  `b6c99fe52750ecfe5907f04764df5b9efa460137bbd7b43f02197e6f2e46e4fa`.
- Exact counts: nine `VERIFIED_UNSAT`, zero UNKNOWN, zero counterexamples.
- Status remains `PENDING_INDEPENDENT_AUDIT`, `c2_proved=false` and no
  certified bound in the pending final.
- The separate auditor PID 391908 was observed live by **17:59:01 UTC+8**,
  parent 391835, start ticks 35202132, boot ID
  `34c2d313-2938-4220-ad0b-8a0018d3c7e8`. Its command names the sealed runtime
  and the exact acceptance-seal and final hashes above.
- At the final launch inspection, it was rehashing input evidence before
  fresh formula reconstruction and nine parallel checker invocations.
  Audit stderr was empty; no acceptance receipt existed. Do not interpret
  auditor startup as completed proof replay or accepted C2.
- The pending final, finalizer exit records and auditor start record were
  also copied into the local evidence directory. The local final hash matches
  the server. The audit will publish acceptance automatically only after its
  nine fresh checks and final post-check equality gates succeed.

### Live inspection at 2026-09-15 20:47-20:48 UTC+8

The independent auditor and all nine fresh checker processes remain live.
Each checker PID/start-tick identity matches its start receipt, consumes about
one CPU core, and has empty stderr. Elapsed checking time is about 2h42m.
Available system memory is about 400 GiB and swap usage is zero. No checker
exit/status, global-stop, acceptance receipt or audit exit exists yet.

| Cell | Reported checker progress | Internal remaining-time estimate |
| --- | ---: | ---: |
| e2 | 39.06% | 4.07 h |
| e3 | 42.89% | 3.47 h |
| e4 | 56.17% | 2.03 h |
| e5 | 37.51% | 4.31 h |
| e6 | 31.05% | 5.70 h |
| e7 | 20.91% | 9.56 h |
| e8 | 15.48% | 13.61 h |
| e9 | 35.93% | 4.49 h |
| e10 | 92.05% | 0.23 h |

These are checker progress counters and internal extrapolations, not a
reliable wall-clock completion percentage. Work per proof step is uneven.
The prior 5-7-hour total estimate should not be treated as a completion
promise; the slowest current internal estimate is roughly another 14 hours,
which extrapolates to September 16 morning. There is no observed crash,
stall, swap pressure, or accepted C2 receipt at this checkpoint.

## Read-only progress observation: 2026-09-15 22:59 UTC+8

The independent audit is still running. Five fresh checks (e2-e5 and e10)
completed with zero exit, no timeout and `s VERIFIED`; their elapsed times
were 16299.572, 15882.939, 14044.838, 16769.552 and 12683.124 seconds.

| Remaining cell | Checker progress | Checker-reported remaining time |
| --- | ---: | ---: |
| e6 | 97.83% | about 381 seconds |
| e7 | 55.43% | about 13669 seconds |
| e8 | 47.63% | about 18559 seconds |
| e9 | 97.59% | about 420 seconds |

All four checker processes were live/runnable at approximately 99.9% CPU;
their logs had recent writes. Audit and pipeline stderr remained empty, and
neither a global stop nor an acceptance receipt existed. All nine original
proof-qualified experiment results remain complete; this is the additional
independent acceptance replay. The original 5-7-hour total estimate was too
optimistic for this run. The current slowest checker suggests roughly another
4-6 hours, including post-check integrity validation; this is only an estimate,
since checker progress and remaining-time forecasts are not linear guarantees.

## Workflow note

The server has no `.trellis/scripts/get_context.py`; the local task, phase
index, scoped specifications and skill instructions were read directly.
The existing broader cardinality task remains in progress while acceptance
and the remaining higher layers are open.
