# Additive notation erratum: F3 endpoint indexing

This records the independent GPT review's single MINOR, nonblocking
documentation finding. The original177 primary files remain unchanged.

Original frozen formal_row_derivation.md line54 says:

> (the implementation's zero-based equivalents are v and N-1-v).

Correct replacement description:

> The frozen implementation uses one-based vertices v=1,...,order and the
> displayed bounds v-1 for occupied proper subsets and order-v for occupied
> proper supersets.

The preceding mathematical bounds v-1 and N-v are already correct. Frozen
f3_main_rank.py lines192-195 use range(1, order + 1), select v-1 or order-v,
and guard the resulting inequality with state_vars[v,h]. This correction
changes no theorem, case, CNF, solver/checker receipt, runtime or candidate.
No new case check, test run or review is required for this notation correction.

Exact local original derivation:
D:\科研\math agent\erdos-szekeres-sat-main\.trellis\tasks\09-03-35-state-cardinality-charging\research\evidence\c8-row-audit-20261026\originals\148_formal_row_derivation.md
SHA256: 2ba5aa2ad4c44f040813287c19f526775719da395d6816682c823948a6036305
Original server: /data/ktqiu_hdd/math_agent/res/state_charging/20261026_c8_row_acceptance_v1/formal_row_derivation.md

Exact frozen implementation:
D:\科研\math agent\erdos-szekeres-sat-main\.trellis\tasks\09-03-35-state-cardinality-charging\research\evidence\c8-row-audit-20261026\originals\038_f3_main_rank.py
SHA256: d5ea34863e4f7c00b20665c56bff06929e16a86721438434d48d429791287004
Original server: /data/ktqiu_hdd/math_agent/res/state_charging/20261017_c8_f3_main_parallel_v1/runtime/state_charging/f3_main_rank.py

The original planned Claude review_route/status remains historical in the
sealed pending certificate. The separate explicit human override and GPT
invocation/response/receipt identify the review actually completed as native
GPT with same-family/provisional assurance. Exact backend/model and actual
effort are unreported and unverifiable. Human formal acceptance is pending.
