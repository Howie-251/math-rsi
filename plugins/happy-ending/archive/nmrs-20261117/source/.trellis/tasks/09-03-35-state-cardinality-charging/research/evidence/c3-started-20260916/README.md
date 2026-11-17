# C3 startup evidence, 2026-09-16

This is a byte-exact lightweight snapshot of 54 server artifacts. The local
`inventory.json` binds each relative file to its authoritative server path,
byte size and SHA-256. All 54 hashes and sizes passed local comparison.

Authoritative result root:
`/data/ktqiu_hdd/math_agent/res/state_charging/20260916_35_state_cardinality_c3_parallel_v1`.

Protocol SHA-256:
`fa0065d64c5f1213ea6ce3f0b5377438a398ce98aa5a4f790a2a62df2760d8a0`.

- `protocol_seal.json`, `validation.json`, `formula_smoke.json` bind the
  eight formulas, immutable runtime and repaired checker to passing tests.
- `launch_receipt.json`, `run_started.json`, `workers_started.json` and
  `workers/` contain actual launcher, worker, formula and solver receipts.
- `launch/` preserves successful generation/test evidence, the launcher,
  and the read-only live-process observation at 10:45:34 UTC+8.

All eight e3-e10 AE proof solvers were running in `forktqiu3`, screen
`703331.m`. CNFs, live logs, runtime binaries and growing proofs are retained
on the server and are not copied here. No C3 acceptance or theorem credit
is represented by this snapshot. The accepted scoped bound remains 33.

See [the search record](../../c3-parallel-search-20260916.md) for the exact
mathematical scope, command contract, process IDs and verification boundary.
