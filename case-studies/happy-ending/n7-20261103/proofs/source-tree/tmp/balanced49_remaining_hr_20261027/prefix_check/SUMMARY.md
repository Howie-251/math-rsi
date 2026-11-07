# Prefix fixed-table and fixed-schema check

Result: **PASS**, one authoritative Linux invocation, raw exit 0, stderr empty.
Parser SHA256: `19bb1cd473db6b2fd15bf4f06d74658d1d93e4d433f1230a3a395acf11317081`.
Raw result SHA256: `20aaf32b5bdfcdf50a1aefeda310c014e7e336de44c0c5e2fa053cf825b725ba`.
All 17 byte snapshots and original paths are bound in `input_manifest.json`
and repeated in `result.json`. The PrefixData and ClosureData hashes also match
the previously acquired source pins.

The 129 parsed patterns comprise four n=4 base patterns, seven n=5 sector
patterns, and 118 n=6 sector patterns. All 759 owners, 2,446 recorded bits,
1,864 labels and 3,728 color/pair rank entries passed the source-aligned checks.
Every recurrence rank was compared against independently enumerated increasing
subset paths; the derived down-set states matched the exact catalog owners.
`Checked`, `pattern_records`, `PairComplete`, base and sector checks passed.

| Sector | Completions examined | Good completions | Table colors | Missing / extra / duplicate |
|---|---:|---:|---:|---|
| n=5, cut=1 (RBBB) | 64 | 7 | 7 | 0 / 0 / 0 |
| n=6, cut=4 (RRRR) | 65,536 | 118 | 118 | 0 / 0 / 0 |

Every wire-tag 7 row was decoded from all 190,932 rule rows. All 3,198 prefix
rows satisfied their constructor's exact `Valid` predicate:

| Constructor | Rows |
|---|---:|
| activation | 360 |
| order | 106 |
| exhaustion | 1,185 |
| sign | 602 |
| attainment | 746 |
| unique | 167 |
| implies | 29 |
| baseCover | 1 |
| sectorCover | 2 |

All 3,198 symbolic clauses were reconstructed from guards/conclusions and
mapped to the 151,801-entry name dictionary using source atom indices based
at zero. Dictionary keys had no duplicates. `prefix_rule_rows.jsonl` retains
each original rule index/wire, symbolic atoms, and reduced dictionary literals;
SHA256 `bba0f718d956a95167d31b7979b5aca5427af04a84bcc530598a725c9ab0a5f5`.

All five mutation controls were rejected. The attainment control removes
predecessor 0 from actual rule row 187,746, whose wire is
`7 4 0 1 9 2 2 1 0`; its source coverage condition then fails. Removing
sector row 4 creates a missing Good color and fails sectorCover Valid.
Owner, bit and label alterations on pattern 0 fail Checked comparisons.

The Linux executable was `/opt/anaconda3/envs/forktqiu3/bin/python3.12`.
Validation wall time was 1.5677028379868716 seconds; recorded user/system
times were 1.519682 / 0.10797699999999999 seconds and max RSS was 108,876 KiB.
Limits were CPU/wall 60 seconds and address space 2 GiB. The SSH/SFTP transport
took 33.5 seconds. No numerical checks ran on Windows, no SAT was invoked,
and no retry, independent review or acceptance update occurred.

This is fixed-table coverage and fixed-row Valid evidence. ClosureLiteral was
unavailable, so actual Closure CNF equality remains unchecked. Universal
abstract semantics, the main-session G4 reduction, D29/C49, and a complete
target counterexample are outside this result.
