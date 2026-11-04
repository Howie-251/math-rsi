# A[8,8] GRAT validation completion — 2026-10-26

Completed: `VERIFIED_UNSAT` for `cardinality_A_r08_e08_N26`, using the original sealed CNF and DRAT proof. Both external processes returned 0; `checker.out` contains the exact line `s VERIFIED UNSAT`. No work remains in this validation pipeline, so no ETA is needed.

- Generator start: 2026-10-23T20:31:38.058+08:00.
- Generator process finished: 2026-10-25T20:28:19.174+08:00.
- Checker process finished: 2026-10-25T22:59:23.296+08:00.
- Final validation receipt mtime: 2026-10-25T23:16:08.305+08:00 (raw mtime_ns=1792941368305178281). Pipeline receipt mtime_ns=1792941368337179677.
- Collection: 2026-10-26T10:35:05.801+08:00; same boot `e642f7d5-0989-4312-8b28-8e3f48df8fc0`. No gratgen, gratchk, formal_controller, or GNU screen workload was present. The two substring screen matches in raw process evidence are unrelated GNOME screensaver services.

| Phase | Wall seconds | Wall h:mm:ss | Peak RSS bytes | Peak RSS GiB | CPU utilization |
|---|---:|---:|---:|---:|---:|
| gratgen, original `-j 2` policy | 172601.116122553 | 47:56:41 | 328151687168 | 305.615 | 196.378796% |
| gratchk, MLton `max-heap 254g` | 7909.815728782 | 2:11:50 | 270262788096 | 251.702 | 95.542621% |

Total stage execution: 180510.931851335 seconds (50:08:31). Calendar time from generator start through final receipt: 182670.247810841 seconds (50:44:30), including receipt/hash/policy overhead. CPU percentage uses one logical CPU as 100%.
Generator backward checking took 166438.919 seconds (46.233 hours), about 96.43% of generator wall time. The earlier roughly one-day planning estimate was optimistic. There is no measured old A[8,8] full-run baseline supporting a speedup claim.

## Artifact bindings

| Artifact | Bytes | SHA256 |
|---|---:|---|
| Original CNF | 21159914 | `3cf248fb50f3040aa8986142c16326eb8d0e428ef7c288e97205598f2663b5ba` |
| Original DRAT | 235726740482 | `7b3ce017b34227f98f4e11b39d29d650bc06bfb94696b6095cb89d8c30ecbcaa` |
| proof.gratl | 21735805197 | `a57d10084a721de03d6e2fd8e24fa5d66645f57a493349e461ca71f59c035a98` |
| proof.gratp | 96426027392 | `37bbbc98ce8f9fa0d789beae7dae53e2ea933444df315b2bac2a24c1de0279fe` |
| gratgen binary | 122696 | `08b6966f234d293684601d60da4fced2446c278b41df625a2e19d8bde1c73ea6` |
| gratchk binary | 572488 | `ebb43100f775a7fc696b6bedb831f155afac5ce83e7ac96fec0c628121392d03` |

Source directory: `/data/ktqiu_hdd/math_agent/res/state_charging/20261023_a88_grat_validation_v1/formal_e08_j2`.

Independent collection checks matched 10 local archived-file SHA256/size references and all 26 small server references, including the actual gratgen/gratchk binary bytes, all eight sealed runtime files, policy/seal/result receipts and logs. Details are in `local_binding_check.json`, `server_small_binding_check.json`, and `SHA256SUMS.json`.
Large original CNF/DRAT and GRAT output files were not copied or rehashed during this status collection. Their full hashes above are recorded frozen-controller bindings, including pre/post original-input verification and generated-output sealing. This distinction is deliberate: independently checked small bindings do not constitute a new independent read of the large artifacts. Sample streams were not downloaded or rehashed.

## Scope

The checked result concerns this sealed restricted-model cell only. Receipt metadata retains `accepted_bound: 26`, `row_acceptance: false`, and `theorem_credit: false`. No C8 row acceptance, unrestricted theorem or upper-bound update is made. Upstream semantic/model acceptance remains same-family/provisional; this archival task adds no independent LLM review. Existing launch evidence, sealed runtime, CNF, original proof and workload history are preserved. No workloads were launched, restarted, stopped or altered.
