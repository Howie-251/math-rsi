# C5 independent audit and compact C6 search, 2026-09-29


Current status, 2026-10-16: **C6 formally accepted by human authorization;
scoped N<=29**, with review provenance **provisional** and backend/model and
effort unverifiable. Five original checked cases are reused; no fresh case
rechecks or proof hashes. See [formal acceptance and exact receipts](c6-formal-acceptance-20261016.md).
C7 remains unaccepted and A[7,7] checking continues. The dated records below
are historical; their earlier pending states and bounds are preserved.

## New parallel bridges search: 2026-10-08, 12:02 UTC+8

The user authorized a fresh production-bridges A[6,6] while retaining the
original compact A[6,6]. Their explicit parenthetical instruction excludes
any A[6,7] rerun. The new root is
`res/state_charging/20261008_c6_e06_bridges_v1`, screen `1955693.m`;
the original stays in `1858221.n`. Both e6 proof solvers were observed running
(new PID 1955731, old PID 1858257), with matching start identities. Old sealed
runtime hashes and e7's completed receipt remain unchanged. The new formula
uses the current default exact encoding plus 3,600 bridges, not a predecessor
builder snapshot. All 32 adapter/process/production-bridge tests passed.
See [the new e6 bridges checkpoint](c6-e06-production-bridges-20261008.md).
Logical coverage remains four checked C6 cells, with e6 still open. No new
row theorem or bound is claimed, and the two e6 runs are separate evidence.

## Latest observation: 2026-10-08, 11:46 UTC+8

**C5 remains independently accepted, scoped bound N<=30. C6 now has four
checked UNSAT cases; only e6 remains an open solve.** This was a read-only
server inspection. The [status evidence](evidence/c5-c6-status-20261008.json)
records receipt validation, process identity, durations and the ETA calculation.
C5's six fresh result/log bindings, dependencies and clean audit exits were
revalidated. C6's unchanged seal, CNF/metadata bindings, completed solver/checker
outputs and verdicts, and completed proof sizes were checked. Large proofs
were not rehashed for this status query.

A[6,7], N27 finished checking on **October 7 at 22:47:46 UTC+8**; its final
VERIFIED_UNSAT status was written at **23:14:02**, after proof rebinding. It
took 128.780 solve hours and 70.824 check hours. e8/e9/e10 remain verified.

A[6,6], N26 is still solving after **213.063 wall hours / 213.031 CPU hours**
(about 8.88 days). Its original PID/start-tick/boot/argv identity matches the
start receipt, output is fresh, stderr is empty and no global stop exists.
Its partial proof is **556.768 GB**, with no result credit. Available disk
space is about 611.24 GiB. No operational stall was observed.

There is no reliable completion ETA for this open SAT search. For planning,
allow further days, potentially over a week, including the subsequent first
proof check. Scaling the completed e7/e8/e9/e10 check durations solely by
the current e6 partial-proof size gives 115.51/90.82/68.94/44.71 hours:
**roughly 2-5 days for checking alone if the proof finished at its current
size**. This is a low-confidence size analogy, not a measured rate for e6
or a bound; final proof size and checking complexity may differ. Later
independent C6 acceptance remains a separate stage. Four of five completed
cases does not mean 80% of total runtime. No C6 row theorem or bound 29 is
claimed, and the existing compact campaign was not modified or restarted.

## Latest observation: 2026-10-07, 22:23 UTC+8

**C5 remains independently accepted, scoped bound N<=30. C6 has three checked
UNSAT cases; e7 is near the end of proof traversal, and e6 remains an open solve.**
This was a read-only inspection. The [status evidence](evidence/c5-c6-status-20261007.json)
records the current process identities, receipts and ETA. C5's six fresh
checker result/log bindings, dependencies and successful audit exits were
revalidated. C6's unchanged seal, CNF/metadata bindings, completed output
hashes/verdicts and proof sizes were checked. Large proofs were not rehashed.

| C6 cell | Current state | Solve hours | Check hours |
|---|---|---:|---:|
| A[6,6], N26 | Still solving | 199.671 elapsed | Not started |
| A[6,7], N27 | UNSAT/20, proof checking | 128.780 | 70.418 elapsed |
| A[6,8], N28 | VERIFIED_UNSAT | 69.590 | 29.820 |
| A[6,9], N29 | VERIFIED_UNSAT | 35.697 | 12.074 |
| A[6,10], N30 | VERIFIED_UNSAT | 75.928 | 14.091 |

The e7 checker has traversed **93.92%** of backward proof additions. This is
not a fraction of elapsed runtime. Its displayed linear remaining estimate
is **4.385 hours**; use **roughly 2-6 further hours** as a low-confidence
planning range that may be exceeded. The e6 solver has consumed 199.642 CPU
hours in 199.671 wall hours, with a 525.866 GB partial proof. Neither running
process shows an operational stall: identities match, logs update, stderr is
empty and no global stop exists. About 641.46 GiB disk space remains.

There is still no reliable overall C6 completion date while e6 remains an
open SAT search. Reserve further days, potentially over a week; its eventual
proof must also be checked. Subsequent independent C6 acceptance is separate.
The current C6 jobs retain their sealed compact runtime. The new bridges
default does not modify or restart them.

The bridges A[6,10] comparison remains checked UNSAT: 2.432 solve hours plus
1.936 check hours (4.368 combined). Its pinned receipt, outputs, CNF and proof
size were revalidated. This single-cell comparison grants no C6 row theorem.

## Latest observation: 2026-10-06, 11:51 UTC+8

**C5 remains independently accepted with scoped bound N<=30. C6 still has
three checked UNSAT cases, one proof under checking, and one open solve.**
This was a read-only server inspection; no experiment or program was changed.
The [status evidence](evidence/c5-accepted-c6-progress-20261006.json) records
the observations and ETA calculation. C5 receipt/dependency/fresh checker
log bindings and successful audit exits were revalidated. C6's unchanged
seal, CNF/metadata bindings, completed output hashes/verdicts and proof sizes
were checked. Large proof contents were not rehashed for this status query.

| C6 cell | Current status | Solve hours | Check hours |
|---|---|---:|---:|
| A[6,6], N26 | Still solving | 165.133 elapsed | Not started |
| A[6,7], N27 | UNSAT/20, proof checking | 128.780 | 35.880 elapsed |
| A[6,8], N28 | VERIFIED_UNSAT | 69.590 | 29.820 |
| A[6,9], N29 | VERIFIED_UNSAT | 35.697 | 12.074 |
| A[6,10], N30 | VERIFIED_UNSAT | 75.928 | 14.091 |

The e7 checker reached 24.14% of backward proof-addition traversal, compared
with 4.94% yesterday. This is not elapsed-time completion. Both active process
identities match their start receipts; CPU time tracks wall time, logs are
fresh and stderr is empty. No global stop or terminal exists. Available disk
is about 754 GiB and memory about 332 GiB. No operational stall was observed.

At a subsequent 24.15% sample, the checker displayed a linear remaining time
of 104.40 hours (4.35 days). Cross-proof scaling against completed e8/e9/e10
at the same percentage gives about 39.75/35.33/7.11 hours remaining. Their wide
spread demonstrates the uncertainty: use **roughly 1-4 further days for e7**
as a low-confidence planning range, not a bound. Overall C6 has no defensible
completion date while e6 remains an open SAT search and still needs proof
checking afterward. Allow further days, potentially over a week. A subsequent
independent C6 acceptance audit is separate; no bound 29 is claimed.

The concurrent legacy comparison has also advanced: A[6,9] solved UNSAT in
33.100 hours and is checking (12.025 hours elapsed); A[6,10] remains checked
UNSAT after 10.778 solve and 4.993 check hours. See the
[same-cell comparison record](c6-legacy-comparison-20261004.md).

## Latest observation: 2026-10-05, 11:51 UTC+8

**C5 remains independently accepted; C6 has three checked UNSAT cases,
one completed UNSAT solve under proof checking, and one remaining solve.**
This was a read-only server inspection. The
[status evidence](evidence/c5-accepted-c6-progress-20261005.json) records
unchanged acceptance/protocol bindings and timestamped process observations.
Large proofs were not rehashed. Completed C6 solver/checker exit and log hashes,
qualified verdicts, CNF bindings and proof sizes were checked. C5's pinned
receipt, dependency bindings and successful audit exits were revalidated.

- C5: six fresh checks accepted on October 3 at 19:38:33 UTC+8; scoped bound
  remains **N<=30**. No C6 row theorem or bound 29 is claimed.
- C6 A[6,7], N27: solver returned UNSAT/20 on October 4 at 23:29:54 UTC+8
  after **128.780 hours**. Its 341.365 GB proof began checking at 23:58:19.
  The checker is active after **11.887 hours**, at **4.94%** of backward
  proof-addition traversal. This percentage is not a fraction of runtime.
- C6 A[6,6], N26: proof-producing search remains active after **141.140
  hours**; its partial proof is approximately 388 GB and has no result credit.
- C6 e8/e9/e10 retain VERIFIED_UNSAT. Solve/check hours respectively:
  69.590/29.820, 35.697/12.074, and 75.928/14.091.

Both active PID/start-tick/boot/argv identities match their start receipts;
CPU time closely tracks wall time, logs are fresh, stderr is empty, and no
global stop or execution terminal exists. About 837 GiB disk space and
370 GiB available memory remain. No operational stall or failure was observed.

At 4.91% traversal, e7's raw linear checker ETA was **177.94 hours** (7.4 days).
That display assumes uniform work per proof addition. Comparing backward time
at the same 4.91% point with completed C6 e8/e9/e10, and using their time at
99% to approximate full traversal, gives **55.0/51.9/34.4 remaining hours**.
This is analogy across different proofs, not same-proof calibration. A rough
**2–3 further days for e7** is a low-confidence planning estimate and can be
exceeded. Overall C6 completion still cannot be reliably predicted: e6 has
no meaningful search-completion percentage and will also need proof checking.
Allow further days, potentially more than a week. A subsequent independent
C6 acceptance audit is separate from finishing this search and first checking.

## Latest observation: 2026-10-04, approximately 14:15 UTC+8

**C5 is independently accepted; C6 has 3/5 cases solved and checked.**
This was a read-only inspection: no server program, campaign, process or seal
was changed. The [status evidence](evidence/c5-accepted-c6-progress-20261004.json)
retains the C5 receipt and small bindings plus timestamped C6 observations.
Large proofs were not rehashed for this query; their formal complete bindings
were validated by the production audit and remain on the server.

C5 v2 published `ACCEPTED_SIX_FRESH_CHECKERS_BYTE_EQUAL` on **October 3 at
19:38:33 UTC+8**. All six new checkers passed and independent final reconstruction
was byte-equal. The receipt sets `c5_proved=true`, `certified_upper_bound=30`.
Receipt SHA-256:
`4101b158a1516d603148194e34ed44e67769d26b4c47d27b9933020fee137ea3`.
Final SHA-256:
`b99288fe0f6d0876bdde6f721b329edd7ece760235e2e30ee53ca612eebf0ec0`.
All six fresh status/exit/log bindings and qualified VERIFIED verdicts, receipt
dependencies and successful audit exits were revalidated. Checker durations
for e5-e10 were 87.716, 68.655, 46.205, 28.269, 13.201 and 3.655 hours.
The scoped statement is `e>=5 => m>=5`; the currently certified bound is
**N<=30** in the same signotope/path-bounded/weak-7-free domain.

| C6 cell | State | Solver hours | Checker hours |
|---|---|---:|---:|
| A[6,6], N26 | Running | >119.5 | Not started |
| A[6,7], N27 | Running | >119.5 | Not started |
| A[6,8], N28 | VERIFIED_UNSAT | 69.590 | 29.820 |
| A[6,9], N29 | VERIFIED_UNSAT | 35.697 | 12.074 |
| A[6,10], N30 | VERIFIED_UNSAT | 75.928 | 14.091 |

C6 e8 and e10 completed their first checks on October 3 at 19:21:42 and
09:07:11 UTC+8 respectively. All three completed cases retain solver exit 20,
checker exit 0, qualified VERIFIED verdicts and matching output hashes; CNF
bindings and completed proof sizes were also checked. Both active solver
PID/start-tick/boot/argv identities match their original receipts. Each uses
99.9% of one CPU, has fresh output and empty stderr. No global stop or terminal
receipt exists. Disk availability is approximately 982 GiB; memory remains
ample. There is no evidence of a stalled or failed solver.

Completed cases are **3/5 = 60%**, which is not 60% of elapsed or required work.
Neither running case has a reliable search-completion percentage. Both have
already exceeded the longest completed C6 solve (75.928 h), so extrapolating
the completed cases would underestimate them. No narrow remaining-time ETA is
supported. Reserve further days for planning, potentially longer, and allow
proof checking after solving. The completed checks took 12-30 hours; the
remaining partial proofs are already larger, so that range is not a bound on
their future checking time. No C6 theorem or bound 29 is claimed.

## Performance recheck: 2026-10-02, approximately 11:40 UTC+8

The current evidence does **not establish an end-to-end speedup** from the
compact encoding. This inspection was read-only on the server: no campaign,
solver or checker was changed, and no comparison solves were started.

All five C6 metadata files specify `compact_cardinality_756_v1`,
`strict_no_target`, `bridges=false`; their CNF hashes match the sealed inputs.
The protocol hash is unchanged. C5 and C6 bind the same AE solver executable.
All four active C6 solver PID/start-tick/boot/argv identities match their launch
receipts. Each has about 68.97 wall hours and 68.96 CPU hours, fresh progress
output, empty stderr and no global stop. CPU, memory and I/O pressure averages
are zero at this snapshot. This gives no evidence of an operational stall.

The completed e9 status still has solver exit 20, checker exit 0, a qualified
VERIFIED verdict, and matching solver/checker stdout/stderr hashes. Its large
proof was not rehashed for this performance query; formal proof binding remains
the campaign auditor's responsibility.

| N | Current C6 cell | Compact solver time | Earlier C5 cell at the same N | Legacy solver time |
|---|---|---:|---|---:|
| 26 | A[6,6] | >68.97 h, running | A[5,5] | 86.306 h |
| 27 | A[6,7] | >68.97 h, running | A[5,6] | 76.425 h |
| 28 | A[6,8] | >68.97 h, running | A[5,7] | 67.270 h |
| 29 | A[6,9] | 35.697 h, checked | A[5,8] | 60.358 h |
| 30 | A[6,10] | >68.97 h, running | A[5,9] | 44.833 h |

These are different cells: both e and m increase by one in C6. The table is a
workload comparison, not an encoding speedup measurement. In particular, the
N29 improvement and N28/N30 longer runs cannot isolate the encoding effect.
The completed compact N29 proof needed another 12.074 hours of checking.

Re-reading progress rows near 23 and 24 CPU hours gives old/new conflict rates
of 1784.6/1722.8 (N26), 1380.6/1769.9 (N27), 1161.1/1776.9 (N28),
1233.8/1755.7 (N29), and 916.4/1350.1 (N30) conflicts per second. Thus even
conflict throughput is not uniformly higher. Higher throughput also need not
mean a shorter proof search: the required number of conflicts can change.

At N26 and about one CPU hour, old/new active variables are 17280/8319 and
irredundant clauses are 215422/122215. The old solver has already eliminated
much of the raw CNF overhead. This approximately 43.3% reduction of the
reported irredundant clauses is not the original approximately 81% raw-clause
reduction, and it excludes learned clauses. Exact projection equivalence does
not preserve propagation, branching behavior or proof length.

Conclusion: current searches remain operationally healthy and multi-day, but
no measured acceleration factor or narrow remaining-time forecast is justified.
A controlled comparison should hold the actual A[r,e], executable, settings,
seed, proof mode and resource conditions fixed; compare complete old/compact
solve and check times across several cells/seeds. The already-validated optional
bridges are another candidate for that experiment, not an assumed improvement.

## Latest observation: 2026-10-02, 11:32 UTC+8

**C5 v2 has 4/6 fresh proofs verified; C6 has 1/5 cases solved and checked.**
This was a read-only server inspection. Both protocol hashes still match;
completed checker stdout/stderr hashes, exit 0 and qualified verdicts were
validated, as were active PID/start-tick/boot/argv identities. All observed
error logs are empty, neither campaign has a global stop, and C5 has not yet
published acceptance. Large proof files were not rehashed for this status
query; their formal pre/post bindings remain the production auditor's job.

C5 e7/e8/e9/e10 have fresh VERIFIED_UNSAT receipts. Their checker durations
were respectively 46.205, 28.269, 13.201 and 3.655 hours. e7 completed its
receipt on October 1 at 23:53 UTC+8. The remaining checks are:

| C5 cell | Backward additions traversed | Current checker elapsed | Calibrated remaining |
|---|---:|---:|---:|
| A[5,5] | 41.56% | 57.56 h | about 30.7 h |
| A[5,6] | 61.60% | 57.99 h | about 11.6 h |

Calibration compares the original check of each exact same proof at the same
percentage. Current/original backward-time ratios are 1.2144 and 1.2539;
scaling original full durations (72.6455 h and 55.5065 h) by those ratios and
subtracting current elapsed time gives the estimates above. This assumes
similar future relative speed. The raw linear ETAs are 78.34 h and 35.04 h;
proof-addition counts do not represent uniform work. Allow roughly **1.5–2
more days for complete C5 acceptance**, including final inventory revalidation,
if no failure or slowdown occurs. Four of six proofs is 66.7% by case count,
not 66.7% of total runtime.

C6 **A[6,9], N=29**, completed with solver exit 20 and a nonempty 97.512 GB
proof, then checker exit 0 and VERIFIED. It took **35.697 h solving plus
12.074 h checking**; its status receipt was completed on October 1 at
14:42:03 UTC+8. Its CNF hash and proof size were also checked in this inspection.
C6 e6/e7/e8/e10 are still solving after approximately **68.8 h**, with fresh
log output and approximately 100% of one CPU each. No operational failure was
observed. The case completion fraction is **1/5 = 20%**; the search-completion
percentage within any running case is unknown. Remaining-variable ratios in
solver logs are not progress percentages.

One completed cell does not give a defensible ETA for the remaining four,
which have already exceeded its solve time. Keep a **multi-day planning
allowance**, with additional proof checking after solves finish, but do not
present a narrow forecast or the previous 3–7-day allowance as a measured ETA.
Partial proof files and the completed proof total about 833.4 GB; available
disk is about 1.33 TB. The currently certified scoped bound remains **N<=31**.

## Prior observation: 2026-10-01, 00:29 UTC+8

**C5 v2 is running with 2/6 fresh proofs verified; C6 has 0/5 completed.**
This corrects the preceding 00:22 observation, which inspected the failed
original C5 preparation but overlooked its already-running v2 successor.
The v1 failure is historical; the v2 recovery described below is active.
No server programs, proofs, processes or seals were changed in this inspection.

C5 v2 protocol SHA-256 is
`a196fad52df4335c1c26b2c1a490299f4df49725df788da0b28b7ec4ea7467e4`.
The launch bindings match and finalization completed successfully. Both e9
and e10 have fresh `VERIFIED_UNSAT` receipts, checker exit 0, matching
stdout/stderr hashes and qualified verdicts; their checker durations were
13.201 and 3.655 hours. Four remaining checker identities match their original
start receipts. Audit and pipeline errors are empty, there is no global stop,
and no C5 acceptance receipt has been published.

| C5 cell | Backward-pass additions processed | Estimated remaining checker time |
|---|---:|---:|
| A[5,5] | 11.33% | about 72 h |
| A[5,6] | 15.60% | about 48 h |
| A[5,7] | 23.30% | about 24 h |
| A[5,8] | 57.07% | about 4 h |
| A[5,9] | verified | complete |
| A[5,10] | verified | complete |

These percentages count additions traversed by the backward checker, not
uniform computation or full-campaign completion. Estimates compare each
current pass with the original check of the exact same proof at the same
percentage. Current/original elapsed backward-time ratios are 1.304, 1.276,
1.232 and 1.177. Scaling original full checker durations by these ratios,
then subtracting current elapsed wall time, gives 72.24, 47.91, 24.19 and
4.10 hours. This assumes similar future relative speed and is not a deadline.
Allow approximately **3-4 further days for C5 acceptance**, including the
final evidence revalidation. The checker's raw linear ETAs (162, 114, 71 and
17 hours) are not calibrated for the nonuniform proof traversal.

C6's five original proof-producing solvers remain active after about **33.7
hours**, with fresh log activity, no solver/checker completion receipts,
empty error logs and no global stop. Its original compact protocol hash still
matches. Completed cases are **0/5**. Neither the roughly 498 GB of partial
proofs nor the log's 26-29% remaining-variable ratios measure search completion.
There is no completed compact C6 sample supporting a reliable finish forecast.
For resource planning only, retain a low-confidence **3-7 further days for
search plus first proof checking**, potentially longer; this is not a measured
ETA and excludes later independent C6 acceptance. The certified scoped bound
remains **N<=31**.
## Original launch authorization and checkpoint

The user authorized independent C5 rechecking and concurrent C6 search using
optimized code. The user explicitly confirmed retaining the original C5 CNFs
and proofs for their audit, while using the compact encoding for every C6 case.
A changed CNF needs a fresh proof even when its semantic projection is equivalent.

## Predecessor evidence

C4 was accepted on September 24 at **17:25:36 UTC+8**, after seven new proof
checks and byte-equal final reconstruction. Its scoped theorem is
`e>=4 => m>=4`; the currently certified bound is **N<=31**, in the documented
signotope/path-bounded/weak-7-free domain. Authoritative acceptance root:

`/data/ktqiu_hdd/math_agent/res/state_charging/20260922_35_state_cardinality_c4_acceptance_v1`

- Receipt: `84a1f4aafa6d03ffb3a4413a33f901bb2a16e1a658c6c49203cd78f49be95cb8`.
- Protocol: `f75fecb3ec545e2403a1216c38a5ecd9649aeaa6a7f25cb514cce5a74b7169db`.
- Pending final, retained unchanged: `79d7ccfa785ca4175abce13a7a08677c2d6a20553a79654cbcddc09061bb4b97`.

C5 completed six original-encoding checked UNSAT cases on September 29 at
**06:05:56 UTC+8**, after 159.433 hours. Its proof files total
**735,064,237,842 bytes**. This is execution evidence, not an accepted C5 theorem.
Source root:

`/data/ktqiu_hdd/math_agent/res/state_charging/20260922_35_state_cardinality_c5_parallel_v1`

- Source seal: `8e4d53797b63fa95a983c470358653f111a37eb22db36838650316dcbd1b4d5b`.
- Execution terminal: `0e2f6a3624640e840dc11b90166f3581dc8ebfb644ad8bf008b8e2d8a1ff5876`.

## New launch

Both one-shot pipelines were dispatched on September 29 at **14:41:34 UTC+8**,
using `/opt/anaconda3/envs/forktqiu3/bin/python3.12`:

| Pipeline | Screen | New authoritative result directory below `res/state_charging/` |
|---|---|---|
| C5 independent audit | `1858218.m` | `20260929_35_state_cardinality_c5_acceptance_v1` |
| C6 compact search | `1858221.n` | `20260929_35_state_cardinality_c6_compact_parallel_v1` |

C5 first hashes the complete source inventory, including all 735 GB of proof
bytes. It then seals a fresh audit protocol, reconstructs all original formulas,
creates a pending final, independently reconstructs identical final bytes, and
runs six fresh repaired external checkers. Post-check input equality and fresh
result validation are required before the separate receipt can accept C5 and
the scoped bound 30. At the first launch observation C5 was still in the input
hashing stage; no fresh checker launch or C5 acceptance was claimed.

C6 uses `compact_cardinality_756_v1`, `strict_no_target`, `bridges=false`,
with exact m=5 and five cases e6-e10. Every export was freshly reconstructed
during preparation and again by its worker before the common start barrier.

| Case | N | Variables | Clauses |
|---|---:|---:|---:|
| A[6,6] | 26 | 31,159 | 230,376 |
| A[6,7] | 27 | 34,929 | 266,944 |
| A[6,8] | 28 | 38,992 | 307,704 |
| A[6,9] | 29 | 43,359 | 352,965 |
| A[6,10] | 30 | 48,041 | 403,047 |

C6 protocol SHA-256:
`70212068b0ffd6c93e683629692bf7e512cfa3ee2dcde898e6db5612e2ba0ecc`.
At **14:43:25 UTC+8**, five real AE proof-producing processes were running
after SAT-first: e6/e7/e8/e9/e10 PIDs 1858257/1858258/1858259/1858256/1858260.
No case had completed and no global stop was present. Proof/checker deadlines
are null; checking uses the repaired `-t 0 -b` executable. SAT assignments
must pass the compact complete-clause and independent coloring/state/count
audit. Audited SAT or operational error stops owned peers.

C6 execution retains `c6_proved=false`. Its seal binds accepted C4 and the
completed original C5 source/terminal as an explicitly pending dependency.
Even five checked UNSAT cases cannot establish the C6 row or bound 29 without
accepted C5 and a later independent C6 audit.

## Code, validation, and evidence

Programs are retained locally under `tmp/` and on the server under
`tmp/c5_c6_dev_20260929/`:

- `c5_acceptance_20260929.py`: SHA-256 `3f327d884b7fc4608149eef8bc69f448fafc65a7073af4b7391a0cfa59ba90ee`.
- `c6_compact_campaign_20260929.py`: SHA-256 `0f05123468138360e2e9158c788ab64d369fa8663020ef5a91b84788faaf3170`.
- Shared `accepted_c4_gate_20260929.py` pins accepted C4, verifies seven fresh
  checker log/result bindings and clean exits, and recursively validates C3.
- `launch_c5_c6_20260929.py` binds the tested program bytes, creates each stage
  once, and retains actual process exits. Do not restart either generation.

Linux validation passed **25 C5 acceptance tests in 4.515s** and **30 C6 tests
in 11.463s**, including real controlled child processes, failure cancellation,
real AE/repaired-checker integration, full compact A[6,6] export/replay,
metadata/coordinate/mode rejection, and the unchanged process-helper suite.
The compact builder itself is unchanged from the September 27 validated
implementation (51 regression tests and 92 proof-backed semantic queries).
New runtime copies exclude Python bytecode caches, bind all copied source
files, and require imported formula modules to belong to the frozen runtime.

The local [startup evidence](evidence/c5-audit-c6-started-20260929/README.md)
contains only small immutable receipts and an explicitly timestamped live
observation. Large proofs remain on the server. The parent task remains active;
this checkpoint creates no commit, archive, or theorem beyond accepted C4.

## Evening status and C5 recovery, September 29

At 21:39 UTC+8 C6 had five healthy proof-producing solvers, about 6.94 hours
each, no finished case, no checker invocation and no global stop. Partial proof
sizes e6-e10 were 31.085, 29.643, 27.441, 26.277 and 24.257 GB. These are growing
intermediate files, not checked proofs or completion percentages.

C5 v1 had stopped at **15:30:37 UTC+8**, after 49.06 minutes of preparation.
It had not created an acceptance root or started any fresh checker. The exact
error was `runtime/tools drift`: nine additional Python bytecode caches,
with filesystem modification times September 27 10:41, were present under
the original C5 runtime. All 20 sealed runtime files and four tools matched
their original hashes. The creating process was not established. The original
25 synthetic/integration tests did not inspect this actual source namespace;
the production validator checked it only after hashing all six large proofs.

The failure and original evidence are preserved. A create-only v2 amendment
pins the nine exact cache paths, sizes and hashes, retains them in the full
pre/post source inventory, and copies only the original 20 sealed runtime
files into the new audit runtime. No caches are executed or copied; every
other namespace/hash change is still rejected. The cheap actual runtime/tool
preflight now precedes proof hashing. C6 was not modified or restarted.

- Successor program: `tmp/c5_acceptance_20260929_v2.py`, SHA-256
  `ad077215a3eec2d09a5f6c50d2d3bab383448a7a46b20a935538e9e1a7f06d77`.
- **29 Linux tests passed in 3.850s**, including actual source preflight,
  changed/missing/additional cache rejection, source/tool drift and symlinks.
- New root: `/data/ktqiu_hdd/math_agent/res/state_charging/20260929_35_state_cardinality_c5_acceptance_v2`.
- New development/launch directory: `tmp/c5_audit_dev_20260929_v2`.
- Started **21:44:50 UTC+8**, screen `1887840.m`. At the recovery observation,
  preparation was active, its error logs were empty, and fresh checking had
  not yet started. The root is created after full input validation succeeds.
- Original failed preparation exit receipt SHA-256:
  `6e0b86a376ebd7f73bbab590839e57785b7bd25d5c0f451e266a4740cb255027`.

Evidence: [recovery snapshot](evidence/c5-audit-recovery-20260929/README.md).
Estimated remaining C5 time is **3–5 days from recovery**, using the original
maximum checker duration of 72.645 hours plus inventory/replay overhead and
resource variation. C6 has no completed compact case from which to estimate
a completion rate. **3–7 more days** for search plus first checking is only a
low-confidence planning allowance based on the previous multi-day campaigns;
it may take longer and excludes later independent C6 acceptance. The certified
bound remains 31. Neither campaign has a new accepted theorem.

## Read-only status check, 2026-09-30 12:11 UTC+8

C5 v2 has reached independent proof checking. A[5,10] passed with checker
exit 0, one `s VERIFIED`, matching stdout hash, and 3.655 hours of checking.
Five other checker process identities match their start receipts. There is no
global stop or acceptance receipt; pipeline and audit error logs are empty.
The v2 seal is `a196fad52df4335c1c26b2c1a490299f4df49725df788da0b28b7ec4ea7467e4`;
pending-final SHA is `b99288fe0f6d0876bdde6f721b329edd7ece760235e2e30ee53ca612eebf0ec0`.

Checker backward-pass progress e5-e9 is approximately 4.15%, 5.97%, 9.13%,
17.05%, 74.02%. These percentages count proof additions, not uniform work.
At matching percentages, the ratio of current to original backward-pass time
is 1.29, 1.22, 1.23, 1.18, 1.02. Scaling original complete checker durations
by those ratios gives rough remaining wall times 83, 57, 37, 16, 1.4 hours.
This extrapolation assumes future relative speed remains similar, and includes
no guaranteed completion date. Allow **3–5 more days** for full C5 acceptance,
including post-check inventory/replay. The checker's naive e5 ETA is 193 hours;
it is a linear extrapolation from a demonstrably nonuniform proof pass.

C6 has **0/5 completed**, with all five original proof-solver identities alive
after approximately 21.4 hours, no checker started, no error or global stop.
Partial proofs total 346,864,746,496 bytes. These bytes are not proof credit or
a completion percentage. There is still no completed compact C6 calibration
sample; **3–7 more days for search plus first checking** remains only a low
confidence planning allowance and may be exceeded. Later independent C6
acceptance is excluded. The certified bound remains 31.

Available disk is 1,821,957,734,400 bytes. The roughly 141-second observation
interval shows combined C6 proof growth around 12.5 GB/hour; unchanged growth
would consume that space in about six days. This is a short-interval resource
projection, not a prediction of solver completion. No processes were modified
or restarted during this status check.

## Compact performance inspection, 2026-09-30 13:54–13:56 UTC+8

The user asked whether C6 runtime with the optimized encoding meets expectations.
This was a read-only server inspection; no solver, checker, source or sealed
artifact was changed. All five original proof-solver PID/start-tick/boot
identities matched. All were running at approximately 99.9% of one CPU after
23.2 hours, with fresh conflict/proof output, empty error logs, no global stop,
no solver exit and no completed C6 case. The live export confirms
`compact_cardinality_756_v1`, `strict_no_target`, `bridges=false`.

| C6 cell | N | Current conflicts | Active variables | Recent conflicts/s | C5 same-N cell | Its solve hours | Its conflicts/s at similar elapsed time |
|---|---:|---:|---:|---:|---|---:|---:|
| A[6,6] | 26 | 191,567,032 | 8,253 | 1,648.0 | A[5,5] | 86.306 | 1,406.2 |
| A[6,7] | 27 | 187,031,868 | 9,518 | 1,805.5 | A[5,6] | 76.425 | 1,268.7 |
| A[6,8] | 28 | 176,078,210 | 10,866 | 1,605.6 | A[5,7] | 67.270 | 1,182.7 |
| A[6,9] | 29 | 168,751,701 | 12,346 | 1,553.5 | A[5,8] | 60.358 | 1,176.2 |
| A[6,10] | 30 | 153,860,858 | 14,190 | 1,477.1 | A[5,9] | 44.833 | 795.2 |

Recent rates are conflict differences over approximately the preceding hour
of solver-reported time, using the nearest retained progress rows. Old solve
hours come from `proof_solver.exit.json` and exclude checking. Each same-N
comparison changes both e and m by one; it is descriptive evidence, not a
controlled same-cell encoding benchmark or an end-to-end speedup ratio.

After one hour, N26 old/new active-variable counts were 17,280/8,319, and
reported irredundant-clause counts were 215,422/122,215. At roughly 23 hours
they were 16,715/8,253 and 206,335/121,138. Thus the original 80% raw-clause
reduction does not translate into an 80% reduction of the working database:
the old solver already eliminates many auxiliaries. The new encoding also
changes propagation and search; the total number of conflicts needed for a
proof is unknown. None of these counters measures fraction of search complete.
In particular, `remaining` in this solver's `src/report.c` is the percentage
of original variables still active, not a completion percentage.

The five partial proofs were about 368.5 GB in total at 13:55. Available disk
was about 1.80 TB. At the earlier observed 12.5 GB/hour growth, that is roughly
six days of space, conditional on unchanged growth and no other disk use;
it is not a solver ETA. Per-solver RSS was approximately 57–78 MB. CPU and
memory pressure averages were zero and recent I/O pressure was negligible;
there is no observed resource stall explaining the running time.

Conclusion: approximately 23 hours without completion is compatible with the
previous multi-day workload, and compressed formulas/search throughput show
real improvements in these descriptive comparisons. End-to-end acceleration
is not established. A presumed fivefold solve-time reduction is unsupported.
There is still no completed compact C6 case to calibrate remaining time; the
earlier multi-day allowance remains a planning allowance only. A controlled
same-cell old/new comparison would be needed to isolate encoding performance.
