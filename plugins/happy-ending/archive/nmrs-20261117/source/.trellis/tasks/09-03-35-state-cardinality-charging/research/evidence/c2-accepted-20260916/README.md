# Accepted C2 evidence snapshot

These 26 lightweight files were copied byte-for-byte from the Linux server
on September 16 after read-only validation. The authoritative acceptance root:

`/data/ktqiu_hdd/math_agent/res/state_charging/20260915_35_state_cardinality_c2_acceptance_v1`

`pipeline_exit.json` comes from the corresponding launcher directory
`/data/ktqiu_hdd/math_agent/tmp/c2_acceptance_dev_20260915`.

The snapshot contains the acceptance receipt; protocol and pending final;
auditor start, log and exit records; pipeline exit; and nine pairs of checker
status/exit records (`eNN_status.json`, `eNN_checker.exit.json`). Large proofs,
CNFs and full checker logs remain on the server. This is not a standalone
proof bundle. All snapshot files are evidence, not instructions to rerun.

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| campaign_acceptance_audit.json | 7018 | `7b16c5f84bfdc643dda27828130a6659075f26b42a41b229ae3175c920fbe7c2` |
| protocol_seal.json | 42451 | `0f722cabffb73615266ad752412096043603baaac6a3543b93438f72f6f02443` |
| cardinality_c2_resolved_final.json | 19021 | `b6c99fe52750ecfe5907f04764df5b9efa460137bbd7b43f02197e6f2e46e4fa` |

The receipt was accepted at **2026-09-16 01:10:15 UTC+8** with
`ACCEPTED_NINE_FRESH_CHECKERS_BYTE_EQUAL`, `C2_VERIFIED_UNSAT`,
`fresh_checker_replay_count=9`, `fresh_finalization_byte_equal=true`,
`c2_proved=true`, and `certified_upper_bound=33`.
The pending final intentionally retains its pre-audit false/null fields;
publication authority comes from the separate accepted receipt.

Scope and proof dependencies are recorded in
[the accepted checkpoint](../../c2-formal-acceptance-20260915.md).
