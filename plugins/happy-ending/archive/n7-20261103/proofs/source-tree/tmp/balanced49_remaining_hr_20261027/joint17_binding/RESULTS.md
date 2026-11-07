# Joint17 fixed-row schema binding result

The sole Linux binding invocation returned PASS and exit code 0. All 59,479
source CNF rows matched the literal sets reconstructed from their corresponding
parsed rule rows after source-exact guards, polarity and constant reduction.
All source Valid conditions were checked. The name dictionary contains 92,886
entries; all names decoded and passed bounds/distinctness checks.

The 40-state catalog equals the 20 low and 20 high ideals among all 70 ideals
of the 4 by 4 grid, with state names 0 and 1 respectively empty and singleton.
Seven in-memory mutations were rejected: polarity, dictionary index, rule tag,
required pairChoice label, bound, malformed Boolean and trailing token.

The original complete local ES7Joint17Literal.lean was byte-hash verified:
`22950a14595f72b93a769261738d029b2aa27d04aa27e1f44fa2dce77775da2a`.
No second literal upload was made. The existing read-only remote partial has
30,932,992 bytes and matches that exact local prefix:
`7760d1d01c73536ea64ed3c2f587caff67e37ff3531dfbd5b012bfb32fc823a2`.
The complete quoted CNF starts at byte 126 and its closing quote is at byte
1,490,293, within the authenticated prefix. The decoded CNF payload SHA256 is
`9a70c9ce1aa47c1a7127a3393a8159c7276c371fb523161b38e838feb6e0b467`.
These are zero-based byte offsets. Source atom indices are explicitly
`abs(signed_literal)-1`; positive source literals mean positive polarity.

Only compressed Data/definition snapshots, the validator and request metadata
were uploaded to the fresh joint17_binding directory. The partial source stayed
read-only. The full remote literal and its proof were NOT verified. There were
zero solver calls, zero checker calls, no replay, no Lean compilation and no
acceptance update. Universal abstract semantics remain the main session's
separate obligation; this result supplies fixed rows/Valid/formula binding only.

Limits: CPU 120 seconds, wall 120 seconds, address space 3 GiB. Recorded wall time
1.871411712 seconds, CPU 1.928482 seconds, maximum RSS 89,288 KiB. No retry or
repair run occurred. Raw machine evidence is result.json, transport_receipt.json
and request.json. All input bytes and SHA256 identities are retained under
inputs/ and in the request/result records.

Linux command:

```
timeout --signal=TERM --kill-after=2s 120s /opt/anaconda3/envs/forktqiu3/bin/python3.12 -B /data/ktqiu_hdd/math_agent/tmp/balanced49_remaining_hr_20261027/joint17_binding/validate_joint17_linux.py
```
