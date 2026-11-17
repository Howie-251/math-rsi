# C5 audit / compact C6 startup evidence

Read-only server observation: **2026-09-29 14:48:04 UTC+8**.
115 transferred files include 113 immutable server files whose sizes and
SHA-256 values were verified locally, plus `server_inventory.json` and
`live_observation.json`. The inventory lists authoritative server paths.
Large files are retained on the server and represented by explicit bindings;
proof bodies, complete CNFs and ongoing solver/checker logs are not copied.

- `c4_accepted/`: accepted C4 receipt, protocol, pending final, clean exits,
  and fresh checker status/provenance. Seven fresh checks establish the scoped
  bound 31. Logs referenced by these receipts remain on the server.
- `c5_source/`: completed six-case C5 terminal and checker/solver receipts.
  The original source seal exceeds the snapshot size limit; its full binding
  is in `server_inventory.json` and it remains on the server and in the earlier
  C5 startup evidence. Completed execution is not independent acceptance.
- `c6_search/`: new compact protocol, five unique claims, fresh formula replay
  markers, SAT-first results and five proof-producing process identities.
- `launch_validation/`: 25 passing C5 acceptance tests, 30 passing C6 tests,
  launcher start receipts, compact preparation exit, and C5 mathematical scope.
- `programs/`: exact tested orchestration, shared C4 gate, tests and launcher.
- `live_observation.json`: C5 preparation is active and has hashed e5's proof;
  zero new C5 checkers have started. All five C6 proof solvers are active,
  identities match their start receipts, no C6 case is complete, no global stop
  is present, and pipeline/preparation error logs are empty.

This is a launch snapshot, not a C5/C6 result or acceptance. It does not
certify partial proof-file bytes. Follow the
[combined checkpoint](../../c5-audit-c6-compact-search-20260929.md) and live
authoritative server roots for subsequent state. Never rerun these one-shot
generations in place.
