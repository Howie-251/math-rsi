# C1 parallel final acceptance checkpoint

Updated: 2026-09-13, Asia/Singapore. The independent audit is now accepted:
C1 has effective 10/10 checker-qualified UNSAT coverage and implies `N<=34`
in the documented domain. This checkpoint records the actual receipt; it is
not a replacement for the immutable evidence. September 12 launch details
below are historical provenance, not live-process instructions.

## Immutable execution result

Active Linux root:
`/data/ktqiu_hdd/math_agent/res/state_charging/20260903_35_state_cardinality_c1_timeout_resolution_v3_parallel_20260912_v2`.

- Protocol SHA-256:
  `4dae075cb5f56febdddf2554ed83ee03dec556e8dc26d2f15555b6d05ce8467b`.
- Sealed controller `tmp/c1_parallel_protocol_20260912_v2.py` SHA-256:
  `50f092b0a657642c28b78c1ee5177e57726d38e6513933851604a5d677309ba4`.
- All four tasks completed; e6/e7/e8/e9 are `VERIFIED_UNSAT`, with unique
  ownership and actual zero worker exits. No global stop or controller error.
- The controller finished at 19:47:43 UTC+8. `execution_terminal.json` is
  9,996 bytes, SHA-256
  `f5ce2d07e561c7be7ffc35e120732240c42aeae8e43d989679384fe755441618`.
- `run_exit.json` is 430 bytes, SHA-256
  `0650d9be4106a13234d9c6cd3da6acb13c1e0b3143707a04b75c3f0aae822a7e`,
  and records zero. The persistent run wrapper also exited zero.
- The sealed read-only `validate_execution(fresh=False, replay=False)` passed,
  including nonempty proof hashes, exact checker verdicts, task inventories,
  unique claims, retained e9 evidence, inherited e10 and frozen predecessors.

| Task | Proof bytes | Proof SHA-256 |
|---|---:|---|
| e6 | 6,480,063,344 | `6e143456c184885471fb3a4aa12552f56163fa7381bd15fd980d45451abd2efb` |
| e7 | 9,311,401,245 | `ec440a9d8a1ee901848227f0f86e6dd5ce3f103c90b75ac32e98fb8ef5f0b7b1` |
| e8 | 10,894,796,940 | `f7cd1bafb5262c259d250919c8ffb372d5c8f80667f47822571d5e8459155ba6` |
| e9, retained original v3 | 15,750,030,233 | `2ba0862972f1d6de214f82eead021a62de3dcabdf01c70752f1b1b889aa9b26c` |

e9 had zero new solver invocations. e10 remains inherited from original v3;
e1-e5 remain inherited from accepted finite v2. None is rerun as a solver.

## One-shot finalizer completed

The user authorized completing final acceptance. The finalizer started once
at 20:12:28 UTC+8 in screen `162262.c1parallelfinal_v2_20260912`, main PID
162266. Treat PIDs only as provenance; check boot ID/start ticks/argv before
deciding whether a process remains live.

- Launcher: `tmp/launch_c1_parallel_finalize_20260912_v2.sh`, SHA-256
  `2e55e3d501839f0f7ec21f6bbc33edbc8418c4c4ec7834881c8c839332617631`.
- `finalize_started.json`: 417 bytes, SHA-256
  `f7dcb754a59bd4800be46419c88caa8aec4b1b11e8e8e6b881a855ba19100b2d`.
- Log: `tmp/c1_parallel_finalize_20260912_v2.log`; `.exit` records this
  wrapper's normalized success/failure, not an inferred original process code.
- Source reconstruction completed without a source-campaign or solver rerun.
- The final file was written at 20:22:45 UTC+8; the process exited and the
  wrapper recorded exactly `0\n`. Log output agrees with actual file bytes.
- `cardinality_c1_resolved_final.json`: 53,489 bytes, externally pinned SHA-256
  `213e7415ebd7eee184679ee45826772dec5ad166c83f47c6033707484dbc182d`.
- Canonical JSON, exact e1-e10 coverage, all ten checker-qualified rows,
  zero UNKNOWN/counterexamples and protocol binding were checked separately.
- The immutable final's status is `PENDING_INDEPENDENT_AUDIT`,
  `all_ten_checker_qualified=true`, `c1_proved=false`, and
  `certified_upper_bound=null`. Those pre-audit fields remain unchanged;
  the separate accepted receipt below supplies publication authority.
- Local matching snapshot:
  `tmp/c1_parallel_final_20260912/cardinality_c1_resolved_final.json`.

## One-shot independent auditor completed

The auditor started once at 20:25:51 UTC+8 in screen
`162958.c1parallelaudit_v2_20260912`, PID 162962, parent 162960, start ticks
10167466, boot ID `34c2d313-2938-4220-ad0b-8a0018d3c7e8`. Its identity and
exact argv were checked live; CPU time was unlimited. The command was the sealed
controller's `audit` mode with the protocol and final hashes above.

- Launcher: `tmp/launch_c1_parallel_audit_20260912_v2.sh`, SHA-256
  `cc59a69e1b7fe50fc9e2e0dd2ff6d5be2c458657e59d6b71347aad3f43c9489c`.
- `audit_started.json`: 598 bytes, SHA-256
  `5bee81be3d243573f7ad71802ddd12abce182dbd1531dec924c1bacbf95f4f75`.
- Log: `tmp/c1_parallel_audit_20260912_v2.log`; `.exit` records normalized
  wrapper success/failure. At startup no exit marker or acceptance existed.
- Fresh e6-e10 proof checks and byte-equal final reconstruction were mandatory
  and completed successfully. The auditor performed read-only source
  reconstruction first. No solver, checker or shell deadline was introduced.
- Never rerun finalize/audit, even after an ambiguous or error exit. Never
  use the retired serial finalizer/auditor or repeat any solver.

The receipt was published on September 13 at 09:57:33 UTC+8. The process has
exited, and its wrapper recorded exactly `0\n`. The audit log's recorded
path, size and SHA-256 match the receipt's actual bytes:

- `campaign_acceptance_audit.json`: 4,213 bytes, SHA-256
  `cd362ea5385aca6218c099bf6237a934d6b9beb48c98923be0cf09562f670fd3`.
- `status=ACCEPTED_PARALLEL_TASKSET_FRESH_CHECKERS_BYTE_EQUAL`.
- `campaign_status=C1_VERIFIED_UNSAT`; ten `VERIFIED_UNSAT`, zero `UNKNOWN`,
  zero `COUNTEREXAMPLE`.
- `fresh_checker_replay_count=5` and `fresh_finalization_byte_equal=true`.
- `c1_proved=true`; `certified_upper_bound=34`.

Subsequent read-only revalidation passed: the sealed controller hash,
byte-equal final reconstruction without solver/checker replay, exact receipt
bytes, proof bindings, frozen inventories, unique task claims, original
source anchors, and actual audit wrapper/log all agree. No publication
stage or production solver/checker was repeated during this inspection.

Six byte-identical lightweight files are now retained in
[the accepted snapshot](evidence/c1-accepted-20260913/README.md). Large proofs
and CNFs remain on the server, so this is not a standalone proof bundle.

## Verification and continuation

The launcher passed Linux `bash -n` and local/remote byte equality. The
unchanged Linux suite ran through its actual unittest entry point:

```text
/opt/anaconda3/envs/forktqiu3/bin/python3.12 -B tmp/test_c1_parallel_protocol_20260912_v2.py
Ran 21 tests in 2.359s — OK
```

A preceding `pytest` invocation executed no tests because pytest is absent;
no package was installed. The standard-library unittest run above is the
successful focused check. Test SAT/ERROR output belongs exclusively to
synthetic disposable fixtures, never the production task set.

The server has no `.trellis/scripts/get_context.py`; local workflow/spec/PRD
files were read directly instead. This is a local workflow-tool availability
issue, not evidence drift. No sealed runtime was edited.

At the September 12 launch checkpoint, the existing heartbeat
`monitor-c1-unbounded-reruns` was found paused and
restored to ACTIVE with its two-hour cadence. Its continuation checkpoint
required using the already-running auditor and externally pinned final,
forbidding duplicate publication and keeping unchanged healthy execution
silent. This is historical automation provenance; the September 13 summary
does not change or assert the current automation setting.

The accepted receipt now discharges the C1 publication gate. The scoped
theorem is `e(X)>=1 => m(X)>=1` and hence `N<=34`, not the full inequality
`m>=e` or `N<=25`. The report, PRD and
[scientific summary](methods-and-results-20260913.md) record the final/receipt
hashes and preserve all failed-generation provenance. The unchanged Linux
unittest suite passed again on September 13: 21 tests in 2.520 seconds,
using only disposable synthetic fixtures. No production experiment,
publication rerun, commit or archive was performed for the summary.
