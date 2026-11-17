# C3 audit / C4 search startup snapshot

This directory preserves 80 exact server artifacts, with source paths, byte
sizes and SHA-256 hashes in `inventory.json`. Every copied file passed local
size/hash comparison on September 18.

- `c4/` contains the seven-case search seal, validation, formula smoke,
  launcher/controller/worker receipts and SAT-first/proof-producer starts.
- `launch/` contains both passing test reports/logs, both pipeline start
  receipts, the launcher and C3 mathematical scope, successful C4 generation,
  and the read-only live observation at 10:48:32 UTC+8.
- `c3_completed/` contains the original completed eight-cell execution
  terminal, zero controller exits, and per-case status/solver/checker exits.

At snapshot time all seven C4 proof solvers were running in screen `837150.n`.
C3 acceptance was performing full input hashing in screen `837144.m`; it
had not yet reached finalization or the eight fresh proof checkers. Subsequent
stages are automatically chained by the one-shot launcher. No C3 acceptance
receipt or C4 theorem is contained in this startup snapshot.

C4 seal SHA-256:
`a03ef308c3aa5cc324e2a77e756213c7df735fcff44f12e0258baa21bce5a4ed`.
Original C3 terminal SHA-256:
`d16cec36911ccdf6e1901395f5da1755fb64aaf82ff3aead714310d95b07183b`.

Large proofs, CNFs and live logs stay on the authoritative Linux server.
See [the combined experiment record](../../c3-audit-c4-search-20260918.md)
for mathematical scope, commands, roots, process IDs and pending stages.
