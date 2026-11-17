# Full N30 exact R6-endpoint population decisions, 2026-10-27

Both fresh exhaustive population branches returned **TIMEOUT_UNDECIDED**.
Each received its one authorized external AE invocation. There is no SAT
witness, raw UNSAT, checked UNSAT, new bound, or acceptance change from these
runs. Total solver invocations: **2**. Proof-checker invocations: **0**.

| Branch | Wall seconds including reap | User CPU seconds | System CPU seconds | Exit | Peak RSS KiB |
| --- | ---: | ---: | ---: | ---: | ---: |
| E5 | 180.007603 | 179.742598 | 0.139911 | -9 | 68140 |
| E6 | 180.007554 | 179.610521 | 0.251885 | -9 | 67168 |

The controller's wall deadline was 180 seconds from before process creation;
the recorded elapsed values include kill/reap overhead. Each owned process
group was killed at that deadline, reaped, and independently confirmed absent
by `final_inventory.py`. RLIMIT_CPU was 180 seconds, RLIMIT_AS 4,294,967,296
bytes, with one CPU in the inherited affinity set. There were no retries,
fallbacks, extensions, or restarts.

## Exact expression and source bindings

Each branch contains 40,718 variables and 445,518 clauses. The unchanged full
N30 D7 base has 24,965 variables and 387,004 clauses; rebuilding it reproduced
the old N30 CNF byte-for-byte, SHA256
`b59fea8b3b300555e695da8e77620db5ee739df8f20d9d844f3e5f69f5f9ebac`.
All 4,060 actual triples and 27,405 packets remain present.

The additive definitions are the unchanged exact forward recurrence snapshot
from `single_root26`, exact E_i iff OR of all R6 reaches ending at actual i,
all 4,060 guarded right-root triples, and a new exact prefix-threshold counter.
Only the two final count units differ between branches. Old one-way flags are
never counted. No four-deletion constraints, endpoint positions, templates,
or H-R conditions were added. The canonical-lifting argument is in
`CHANGE_BOUNDARY.md`; the main mathematical scope and exhaustive-branch
reduction are retained in `R30_ENDPOINT_DECISION_SPEC.md`.

| Binding | SHA256 |
| --- | --- |
| binding.json | 7cb2950e03991649f55fc457e715fee5e4e7e3a92b847cb3853ef6eefd356d37 |
| E5/query.cnf | 2b0cc6a65ab6a99a27fbef9daeeaabb116f405b20dfc4d1eab677a5d2bcece1e |
| E6/query.cnf | ec0bdd579e17fc290039d87bd264d00d5f8b3ee7dd19f2c3c80f46680c3a3746 |
| variable_ledger.json | 3bcf99b1472b8d5f71b48c47e03f5395e61f66ad0efac8e113f01104f22d5efc |
| controls.json | 98e64b9d5f8ee61a9ae0844168fd2dd28e4e70704aa83bf7d30a2cac26c89e03 |
| final_inventory.json | 852e091315b458c6ddc3ddbe5888232c293e8e996c79e5be9f3323538cacc5c3 |

The controls passed before either solver launch: 1,102 coloring/path fixtures,
571 Boolean counter inputs, 222,187 canonical clause checks, 79,280 rejected
single-auxiliary corruptions, and 518 local iff truth-table cases. Coloring
fixtures exhaust N3..5 and use 20 deterministic cases each at N6..8. Counter
inputs exhaust N1..8 and cover 61 N30 inputs. A separate color-only longest-path
oracle passed its 24 deterministic fixtures against exhaustive subset paths.
These are bounded controls; the general lift uses the stated length and prefix
induction, not just agreement of overall SAT statuses.

## Runtime and retained artifacts

Authoritative directory:
`/data/ktqiu_hdd/math_agent/tmp/d7_global_exchange_semantics_20261027/r30_endpoint`.
Scientific execution used `/opt/anaconda3/envs/forktqiu3/bin/python3.12`
(Python 3.12.12), and the default external solver
`/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat`, SHA256
`c2e44161cd142694f2b612e0be2dcc59cb656df6d42f8713adc4d05b9a22f5fa`.
Commands in the branch launch receipts are exactly the solver path,
`--time=180`, branch `query.cnf`, and branch `query.drat`.

Each branch retains complete stdout, stderr, launch receipt, raw/final status,
CNF, and partial proof stream on Linux. Both proof streams were interrupted,
with `finalized_by_UNSAT_solver_exit=false`:

| Branch | Partial stream bytes | Partial stream SHA256 |
| --- | ---: | --- |
| E5 | 81788928 | 1d639c42d484fbe8270f73e461be4ed57577623330f93b2a9b77e2e737efe01b |
| E6 | 83886080 | 289e02da82fb59f498531a5bd1db3327a5d2d40aa1d36990addacc0ed9ec1bb0 |

These streams are not UNSAT certificates. Final inventory checks passed for
both stream hashes, full CNF hashes, all original source bindings, both
stdout/stderr hashes, the shared variable ledger, and the absence of both
owned solver process groups. Local mirrors include both CNFs, all streams
except the partial DRAT files, and all receipts.

The complete SAT assignment/clause, exact endpoint/counter, color-only D7,
all actual R6, all root triples, and mapped Y25 state audits are implemented
but were not invoked, because neither solver returned SAT. No SAT validation
success is claimed.

Only this new result directory was written. Existing completeR30, n18,
single_root26, all historical science/task documents, sealed runtimes, proofs,
running jobs, and acceptance records were preserved. Requested executor role
was native gpt-6.1-sol/high; requested role is not independent backend/effort
attestation. All new artifacts remain unreviewed/unaccepted.
