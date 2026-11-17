# Accepted C1 lightweight evidence snapshot

Copied without changing server artifacts on 2026-09-13. The authoritative
server root is
`/data/ktqiu_hdd/math_agent/res/state_charging/20260903_35_state_cardinality_c1_timeout_resolution_v3_parallel_20260912_v2`.

| Copied file | Serialized SHA-256 |
|---|---|
| `protocol_seal.json` | `4dae075cb5f56febdddf2554ed83ee03dec556e8dc26d2f15555b6d05ce8467b` |
| `cardinality_c1_resolved_final.json` | `213e7415ebd7eee184679ee45826772dec5ad166c83f47c6033707484dbc182d` |
| `campaign_acceptance_audit.json` | `cd362ea5385aca6218c099bf6237a934d6b9beb48c98923be0cf09562f670fd3` |
| `execution_terminal.json` | `f5ce2d07e561c7be7ffc35e120732240c42aeae8e43d989679384fe755441618` |
| `run_exit.json` | `0650d9be4106a13234d9c6cd3da6acb13c1e0b3143707a04b75c3f0aae822a7e` |
| `audit_started.json` | `5bee81be3d243573f7ad71802ddd12abce182dbd1531dec924c1bacbf95f4f75` |

All six local hashes match the observed server files. The acceptance receipt
was published at 2026-09-13 09:57:33 UTC+8 and records ten checker-qualified
UNSAT cells, five fresh successor proof checks, byte-equal reconstruction,
`c1_proved=true`, and `certified_upper_bound=34`.

The immutable final retains its pre-acceptance `c1_proved=false` and
`PENDING_INDEPENDENT_AUDIT` fields by design. Do not rewrite that file to
reflect receipt acceptance; the receipt is the later publication authority.

CNFs, proof bodies, checker logs, full predecessor artifacts and sealed runtime
files are not copied into this lightweight snapshot. They remain referenced
by authoritative server paths and hashes. This is not a standalone proof bundle.
