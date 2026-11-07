# Through14 fixed schema-to-CNF binding

Result: **PASS**, one authoritative Linux invocation, raw exit **0**, stderr
empty. All **5,077 actual CNF rows** decoded, passed exact source `Valid`
(including `AmbientRules.Base`) and matched the corresponding reconstructed
literal **list in order**. No set comparison, deduplication or skipped row was
used. Source indices are `abs(source_signed_literal)-1`, based at zero.

All **12,158 dictionary names** decoded with exact codecs, proper Boolean tags
and point-index bounds/order. They comprise 9,974 ambient, 728 core and 1,456
witness names, with no duplicate semantic keys. Core point indices are [4,18),
ambient selected point indices [0,22). Source `meaning`/`variableMap` snapshots
retain ambient ranks in the original configuration and core ranks in the
selected14 `coreSet`; the program does not construct a mathematical model.
Historical checker `variables=12156` denotes the CNF's largest used variable,
not the dictionary length; every used source index decoded successfully.

| Wire group | Constructor | Rows |
|---|---|---:|
| 0/0 | ambient pathExtend | 1905 |
| 0/1 | ambient pathMax | 649 |
| 0/2 | ambient endpoint | 210 |
| 0/3 | ambient weak | 40 |
| 0/4 | ambient packet | 339 |
| 0/5 | ambient base | 184 |
| 0/6 | ambient extend | 703 |
| 0/7 | ambient maximum | 16 |
| 0/8 | ambient triple | 185 |
| 0/10 | ambient pair | 120 |
| 0/11 | ambient pathRank | 157 |
| 1 | witnessNeg | 18 |
| 2 | witnessPos | 72 |
| 3 | forward | 195 |
| 4 | attain | 4 |
| 6 | extension | 18 |
| 7 | pair | 114 |
| 8 | maximum | 136 |
| 9 | actualCup | 12 |

The actual fixed table contains no top-level tag5/nesting and no base tag9/suffix
rows. Their source translations exist but received no fixed-row exercise.
No absent constructor was assumed to exist for the control harness.

All **14 mutation controls** were rejected: polarity, undecodable dictionary
index, unsupported rule tag, swapped literal order, malformed base Boolean,
one source-bound mutation for each existing non-base top-level rule family,
and a trailing name token. Examples were selected from actual parsed rows.

## Exact historical evidence link

The existing Linux file
`/data/ktqiu_hdd/math_agent/tmp/balanced49_abstract_port_20261026/through14.cnf`
was read-only and its current SHA256 was required to equal
`8a59bfc9ee2a64987b41fb9fc7251fb25c20a70388508afcd5478b1d51a4812b`.
Its bytes exactly equal the decoded complete `cnfOfText` literal from the full
hash-verified existing source `ES7Through14Literal.lean`, SHA256
`640acebb5128073f1731f88893fe4178fb73d9259577fc562f4579c66650e250`.

The existing historical receipt `through14_replay_result.json`, SHA256
`c4a0e1ed8bc9d42102651915c80caaaa6a8cb400dea84c17d1af5070906468de`,
records status PASS, raw checker exit0, checker JSON status PASS, 5,077 clauses,
the same source before/after SHA, and the same CNF SHA/path. All these fields
were required to match. Its proof SHA
`1c98ef23e6584ea17badddf79555e3d634dc40ecd82a56fb17f038d63ee033ac`
is retained **as historical receipt metadata only**; no new proof check occurred.

## Resources, artifacts and scope

Linux wall time **0.156154990s**; user/system CPU **0.197303 / 0.015784s**;
max RSS **21,504 KiB**. Limits: CPU/wall120s and address space3GiB.
The complete transport envelope took **6.625s**, below its180s cap.
Only a compressed266,616-byte bundle of already acquired snapshots and the new
validator/request was uploaded; no acquisition/download or fallback occurred.

- Parser SHA256: `e35e9bd7e28a16a742046b6e2bb6a53b398277ce4da8aad4a9805be53b1798bb`.
- Raw result SHA256: `ac35cea650ff3d33b0676fd2b09fdc8186d0467c4622a66d19533c1f4b449cb5`.
- Mapped ledger SHA256: `f328e252268b7c7025dc2276448ead5c2ee8f4d4fcb09d93e4e85444c4cd627a`.
- Exact snapshot identities and original paths: `request.json`, repeated in `result.json`.
- Raw transport command/exit/stdio/fetched identities: `transport_receipt.json`.

This supplies fixed-row/source/CNF binding and the identity link to an existing
strict-RUP PASS. Main owns universal abstract semantics and population-branch
arguments. No numerical science ran on Windows. There was no solver, checker,
proof replay, scientific retry, Lean compilation, independent review or acceptance
update. Earlier sources, proofs, receipts, tasks and document checks are unchanged.
