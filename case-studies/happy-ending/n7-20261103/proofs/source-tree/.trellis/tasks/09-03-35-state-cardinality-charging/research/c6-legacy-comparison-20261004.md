# Same-cell legacy comparison for A[6,9] and A[6,10]

## Authorization and scope

On October 4, 2026, the user authorized two new old-encoding experiments for
A[6,9] and A[6,10] to compare with their completed compact runs. This is a
performance experiment, not a new row or theorem acceptance. No existing
campaign, input, proof or running solver is changed.

| Cell | N | Exact exceptional count | Exact missing ordinary count | Compact solve hours | Compact check hours |
|---|---:|---:|---:|---:|---:|
| A[6,9] | 29 | 9 | 5 | 35.696538 | 12.074174 |
| A[6,10] | 30 | 10 | 5 | 75.928424 | 14.090974 |

## Protocol

New server root:
`/data/ktqiu_hdd/math_agent/res/state_charging/20261004_c6_legacy_e09_e10_comparison_v1`.
Development/validation root: `tmp/c6_legacy_comparison_dev_20261004`.
Use `forktqiu3`, a detached `m` screen, and two concurrent single-thread workers.

Generate the original exact-state/occupancy encoding from only the 20 bound
runtime files in the sealed C5 source. Use `CardinalityCell(6,9)` and `(6,10)`;
do not substitute same-N C5 cells. Freshly rebuild each formula before a common
worker barrier. Copy and bind the repaired proof checker in the new root.

Retain the same AE binary, default seed 0 and arguments as compact C6:

```text
SAT-first: kissat --time=60 CNF                 (outer deadline 75 seconds)
proof:     kissat --unsat --no-binary CNF PROOF (no deadline)
checker:   proof_checker CNF PROOF -t 0 -b      (no deadline)
```

The original C5 worker and supervisor functions are reused unchanged. Only
their imported task tuple `(9,10)` and receipt schema are configured by the
new adapter. Process control, complete model auditing, proof validation,
cancel/reap behavior and fresh formula replay remain the sealed code.
Inherited `c5_proved=false` fields grant no theorem credit in this experiment.
Errors or audited SAT cancel only the two newly owned workers.

## Validation and evidence

The initial Linux test run passed **27 tests in 2.144 seconds**, including
actual AE/proof-checker integration, two-worker ownership, SAT/error peer
cancellation and reaping, wrong coordinates/options, malformed SAT, empty
proofs, drift and stale-launch rejection, and unchanged process-helper tests.
The exact program/test/source hashes are retained in `validation01.json`.

Compact baseline cell identities, mode, bridge setting, commands, exit
receipts and output hashes are checked and bound separately. Existing large
proofs are not rehashed merely to compare timings; their producer-recorded
bindings are retained and no new theorem acceptance is claimed.

On completion, `comparison_results.json` records solver wall time, solver CPU
time when available, checker time, proof size, and old/new time ratios. A ratio
above one means compact was faster for that cell and default seed. Initial
SAT-first time and proof hashing overhead are not conflated with the solve
and check durations. Original result/exit receipts remain available.

This is a two-cell, one-seed comparison with historical compact runs. Record
resource conditions, and do not infer universal encoder superiority from two
results. CPU availability at preparation was ample: 128 CPUs and load near 2;
free disk was about 1.053 TB. Completion times are not forecast in advance.

## Launch checkpoint

The two controls were launched on **October 4 at 14:37:53 UTC+8**, under
screen **1930841.m**. Both workers freshly reconstructed their full legacy
formulas, synchronized, and completed the 60-second SAT-first stage with
UNKNOWN/exit 0. Unbounded proof production began at approximately **14:39:12**.

| Cell | Variables | Clauses | Actual proof-solver PID |
|---|---:|---:|---:|
| A[6,9], N=29 | 515919 | 1882748 | 1930851 |
| A[6,10], N=30 | 593929 | 2163502 | 1930850 |

New protocol SHA-256:
`fb49cb140dc5a24345196501a974f159cfea8552cf78fa4a57988872f0a9cff1`.
Program SHA-256:
`a0a1a21f307e367adfc887aaeb444f9b45ca43ef9eb8eec5defc3b4d8472232f`.

At **14:41:10 UTC+8**, both solver PID/start-tick/boot/argv identities matched.
Each had about 118 seconds of CPU and wall time; proof outputs were growing,
all observed error files were empty, and no global stop was present. This is
an observed launch, not a completion result or a speedup claim. Existing
compact C6 solvers were not signaled or restarted.

The [lightweight startup evidence](evidence/c6-legacy-comparison-started-20261004/live_observation.json)
retains 16 exact/derived small files: baseline receipts, validation, launch,
worker identities, replay checks, SAT-first exits, resource conditions and a
protocol summary with the authoritative full seal binding. Full formulas,
proofs and subsequent logs remain in the server root. No commit or archive
was made; the parent research task remains active.

## October 5 performance checkpoint

Read-only inspection at **2026-10-05 11:59:38 UTC+8**, with receipt/log
validation immediately afterward, found the following proof-solver timings:

| Cell | Legacy solve hours | Compact solve hours | Result |
|---|---:|---:|---|
| A[6,9] | 21.340400 elapsed, still running | 35.696538 completed | Comparison pending |
| A[6,10] | 10.778466 completed | 75.928424 completed | Compact took 7.044456 times as long |

A[6,10] legacy finished with solver exit 20 and checker exit 0, exactly one
`s VERIFIED`, and classification `VERIFIED_UNSAT`. Its completion status is
timestamped **2026-10-05T06:29:57.523376+08:00**. Neither stage timed out.
Legacy checking took **4.992956 hours**, versus **14.090974 hours** for compact.
Solve plus check took **15.771422 hours** for legacy and **90.019398 hours**
for compact, a compact/legacy ratio of **5.707754**. These sums exclude the
separate SAT-first stage, formula generation and hashing overhead.

Legacy/compact solver CPU times were **10.776222 / 75.920544 hours**, closely
matching their wall times; CPU starvation does not explain the observed
sevenfold solve-time difference. Recorded proof sizes were
**27,677,567,012 / 175,461,297,738 bytes**, respectively.

The same logical cell, solver binary, default seed, proof/checker arguments,
source seals, legacy CNF bindings and compact baseline bindings were checked.
Both runs' recorded solver/checker stdout and stderr hashes matched fresh
hashes. Large proof files were not rehashed for this timing inspection; this
checkpoint does not constitute a new independent C6 proof acceptance.

A[6,9] legacy PID **1930851** remained live with matching PID/start-tick/boot/
argv identity, **21.337272 CPU hours**, a recently updated solver log and empty
solver error files. There was no completion receipt or checker start. Neither
proof size nor elapsed time gives a reliable remaining-time estimate.

Conclusion: compact is substantially slower on the completed A[6,10]
default-seed run. A[6,9] remains undecided. Logical equivalence and fewer CNF
clauses do not guarantee faster SAT search. These historical, single-seed
observations do not establish a universal ranking across cells or seeds.
No experiment, source, solver process or existing proof was changed during
this inspection; the legacy A[6,9] run continues.

### October 5, 15:29 UTC+8 follow-up

The legacy A[6,9] solver was still running with its original verified process
identity: **24.831597 wall hours / 24.827989 CPU hours**, recent log activity
and empty stderr. Compact A[6,9] completed in **35.696538 solve hours**, plus
**12.074174 checker hours**. The same-cell speed comparison remains pending;
an unfinished run's elapsed time cannot be treated as its completion time.

A[6,10] timings and qualified completion statuses remain as above. Final
solver logs additionally show the following search statistics:

| Statistic | Legacy | Compact |
|---|---:|---:|
| Conflicts | 67,426,427 | 409,902,304 |
| Conflicts per second | 1,738.04 | 1,499.75 |
| Decisions | 229,458,913 | 1,185,541,087 |
| Propagations | 170,318,908,977 | 574,787,131,026 |
| Propagations per second | 4,390,295 | 2,103,029 |
| Peak resident bytes | 384,073,728 | 93,478,912 |

Compact reduced memory consumption, but this run required substantially more
search work and took **7.044456 times the legacy solve time**. Source, solver
and baseline bindings were rechecked; compact completed solver/checker log
hashes matched their receipts. This inspection changed no running experiment.

## October 6 performance checkpoint

Read-only server inspection at **2026-10-06 11:50 UTC+8**, with formula,
binary and command binding checks completed at **11:53 UTC+8**, found that
both legacy proof solvers have now finished. Ratios in this table are
**compact / legacy** (the inverse of the report's old/new convention).

| Cell | Legacy solve hours | Compact solve hours | Compact / legacy |
|---|---:|---:|---:|
| A[6,9] | 33.099636 | 35.696538 | 1.078457 |
| A[6,10] | 10.778466 | 75.928424 | 7.044456 |

Legacy A[6,9] returned exit 20 with `s UNSATISFIABLE`, no timeout, and
**119158.688636 seconds** wall / **119142.13 seconds** CPU. Compact took
**128507.537688 seconds** wall / **128492.92 seconds** CPU. Compact therefore
took **7.8457% longer**, an additional **2.596903 hours**, on this run.

Legacy A[6,9] proof checking is still in progress: checker PID **1943526**
matched its PID/start-tick/boot/argv receipt and had approximately **11.9953
wall hours / 11.9867 CPU hours** at the initial snapshot. No checker exit or
worker status receipt existed at 11:53. Its proof has **81,924,814,724 bytes**;
compact's recorded proof has **97,511,996,469 bytes**. The legacy solver time
is final, but its result must not yet be described as checked UNSAT.

Both A[6,10] results and compact A[6,9] retain `VERIFIED_UNSAT`, with solver
exit 20 and checker exit 0, no timeout, and a unique `s VERIFIED` verdict.
A[6,10] solve-plus-check timings remain **15.771422 hours** legacy versus
**90.019398 hours** compact, or **5.707754 times** as long. The comparison
controller has not emitted its final report because legacy A[6,9] is still
being checked.

Fresh final solver statistics for A[6,9]:

| Statistic | Legacy | Compact |
|---|---:|---:|
| Conflicts | 182,545,763 | 241,442,922 |
| Decisions | 584,055,992 | 686,794,390 |
| Propagations | 421,800,384,136 | 295,558,731,307 |
| Peak resident bytes | 602,607,616 | 92,098,560 |

The A[6,10] search statistics recorded above also match the final logs.
Compact saves memory on both cells but takes longer to solve both. More
conflicts and decisions are observed in both compact runs; this does not
identify which encoding transformation caused the regression. Fewer clauses
and logical equivalence alone do not establish a runtime improvement.

Both protocol seal hashes matched their recorded bindings. All four CNFs,
both compact metadata files, solver/checker binaries, matching logical cell
identities, and actual proof-solver argument lists were verified. All completed
solver/checker stdout and stderr hashes matched their exit receipts. Large
proof files were not rehashed, and this timing inspection grants no new
independent theorem acceptance. The same binary, default seed 0 and proof
mode are compared, but these remain historical single-seed runs rather than
repeated randomized trials. No running experiment or source was changed.

### October 6, 23:20 UTC+8 completion inspection

Both legacy comparison cells now have checked UNSAT. A[6,9] completed at
**14:20:23 UTC+8**, with **33.099636 solve hours** and **14.463776 check hours**.
Solver/checker exits and verdicts, complete output hashes, CNF bindings and
recorded proof sizes were freshly validated. The comparison run exit is zero
and no global stop is present. A[6,10] retains its previously checked result.
This status inspection did not rehash large proofs or modify any experiment.
Exact measurements are in the [23:20 observation](evidence/c5-c6-status-20261006-2320.json).
