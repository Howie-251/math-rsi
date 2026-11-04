# Archive scope

This package freezes the six-block Q4 result and the preceding Q4 research chain.
It contains original sources, model data, snapshots, histories, reports, certificate
JSON, exact verifier sources, and recorded verification logs. It runs no new search.

- `certificate_final_q4/`: strongest final Q4 control certificate, raw original
  result and original certification/verification logs. The JSON is unchanged.
- `certificates/Q4_optimized_certificate_20261028/`: full historical source folder
  excluding the precompiled executable; its bound 0.5915869337347425 is superseded.
- `certificates/Q4_059970530_certificate/` and
  `certificates/Q4_refined_certificate_20261027/`: older stages, deduplicated.
- `research/Q4_059970530_research/`, `Q4_refined_research_20261027/`, and
  `optimization_20261028_q4/`: Q4 research chain, including all required binary
  model/index data and generating code. Same SHA payloads are stored only once.
- `research/q5_empty_moment_20261028/`: narrowly selected Q4 control implementation,
  final snapshot/history and original mixed certification harness. No Q5 candidate
  or cut data is included. Two `q5control_*` initializer/history files in the Q4
  optimization tree are included because the Q4 control replay depends on them.
- `validation/`: this handoff's actual full-domain CPU rechecks and provenance audit.
- `tools/`: portable six-block checker, source/package hash checker and archive
  materializer. Generated work directories and binaries are outside the package.

All historical bytes and old reports retain their wording; references to Q5,
prior next-step plans or old records are historical annotations, not current claims.
`inventory.json` is authoritative for source paths, logical targets, actual stored
payloads, hashes, sizes and selected exclusions. The top-level `SHA256SUMS.json`
is generated after editorial documents are finalized, excluding itself.

Excluded: Q5/Q6 optimization attempts and their certificate packages; compressed
Q5 cuts/partitions/candidates; duplicated source ZIP distributions; executable and
shared-library binaries; Python caches. Existing compilers are used to rebuild
checkers. No optimizer or compiler was installed. There is no 100 MB size cap:
the required index arrays are intentionally retained for research continuity.

This is full-domain local Q4 verification, not a filtered-pool scan. It proves a
feasible asymptotic certificate, not globally optimal Q4 SDP value, finite-Q8 bound,
formal proof-assistant verification, or cross-researcher acceptance.
