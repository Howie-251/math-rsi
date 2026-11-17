# Production bridges A[6,6] startup evidence

Observed **2026-10-08 12:05:48 UTC+8**. This snapshot contains 25 transferred
files: 23 immutable server files verified locally by byte size and SHA-256,
plus `server_inventory.json` and `live_observation.json`.

The protocol binds one A[6,6] CNF, current-production source snapshot, tested
runner/helper, external dependencies, accepted C5 and fixed solver/checker.
Preparation completed and the worker freshly replayed the formula. After the
60-second SAT-first UNKNOWN result, proof solver PID **1955731** was active
with no deadline. Its process identity matches the start receipt.

The original compact A[6,6], PID **1858257**, is also active and matches its
original start identity. Every original sealed runtime hash still matches.
A[6,7]'s completed status hash is unchanged and no new e7 worker was created.
Preparation/controller/solver error logs were empty at observation time.

The `production/` directory retains the exact default builder and original
path encoder used by the new runtime. `programs/` retains the exact tested
runner/test/process-helper bytes. No complete proof, running solver log or
CNF is transferred; their authoritative paths and bindings are in the seal.
Partial proof size is observational and has no result credit. The current
scoped bound remains 30; no C6 acceptance is claimed.

See [the launch record](../../c6-e06-production-bridges-20261008.md). Do not
rerun this create-only generation or stop the original solve based on this
startup snapshot.
