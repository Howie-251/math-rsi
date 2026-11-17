# Acquisition outcome and smallest next binding stages

## Scope and preserved evidence

`inventory.json` is the original pre-connection metadata inventory. It hashes
118 acquired Lean-source copies across three scoped local source roots against
the existing public formal manifest, with zero mismatches. It also hashes the
primary receipts and existing transport/replay machinery. Its initial 128 MiB
budget preflight is historical; `acquisition_request.json` records the explicit
revised one-attempt specification. No existing file outside this directory was
written by this executor.

## Single fresh acquisition outcome

Native tool escalation was accepted, and the unchanged established SSH/Paramiko
security pattern connected successfully. The authoritative command was:

`timeout 60s /opt/anaconda3/envs/forktqiu3/bin/python3.12 -B /data/ktqiu_hdd/math_agent/tmp/balanced49_remaining_hr_20261027/binding/acquire_sources_linux.py`

Its outer exit is **124**, and the SSH/SFTP envelope took 63.187 seconds including
connection and bounded fetch. The Linux raw receipt's last saved state is
`status=STARTED`, `stage=ES7ClosureLiteral.lean:range_request`, `seconds=56.13965701602865`.
This is an incomplete progress receipt, not a final success or final error.
`transport_complete` describes successful transport of that partial receipt.

PrefixData completed: 29,724 bytes plain, 2,121 bytes received including ZIP
header/name, CRC and manifest SHA verified. The locally fetched bytes were
independently SHA checked and equal
`3aba553125c23cc817d8d1ba7e98fc62f9517b2ac7a8466890c000224af72777`.
Both local `ES7PrefixData.lean` and the authoritative Linux file are recorded.
The bounded declaration list names `patterns` at line 6, `basePattern` at 136,
`extendedPattern` at 137, `patternColor` at 139, `Checked` at 142,
`checked_patterns` at 149, and `pattern_records` at 150. These are textual
locations only; the declarations were not compiled or executed.

ClosureLiteral did not complete. Its last saved record has 0 received bytes,
0 plain bytes, and no HTTP status/body or verified output path. No later live
server inventory was performed, so do not assert a post-kill filesystem state.
Declared identity remains 732,220,946 plain / 163,629,410 compressed bytes and
SHA `0c4ddc5ab3aa65bed742b9f34d1bab65589e70c2108c21d5b935d9086a0f08ed`.
The receipt's last recorded cumulative download is 2,121 bytes. No automatic
retry, second process, whole archive download, dependency install or deployment
occurred.

## Source/formula/proof evidence distinctions

| Family | Source status | Formula/proof status in inspected receipts |
|---|---|---|
| Through14 | Two local source copies hashed against manifest | Historical authoritative strict RUP PASS over CNF/proof SHA in `formula_proof_inventory.json` |
| Terminal20 | Not in scoped local source roots; present in dated Linux inventory | Historical authoritative strict RUP PASS over CNF/proof SHA in `formula_proof_inventory.json` |
| Joint17 | Already acquired locally, 38,734,663 bytes; hash verified again | No completed strict replay or formula/proof hashes found in scoped inspected receipts |
| ClosureData | Already acquired locally, 6,338,580 bytes; hash verified again | Schema/data wrapper source only; no binding completion receipt |
| PrefixData | Newly acquired/hash verified, 29,724 bytes | No compilation or deterministic predicate check run |
| ClosureLiteral | Acquisition stopped before verified output | Missing verified formula/proof source; no strict replay or binding completion receipt |

Existing finite replay PASS receipts do not establish schema-to-CNF binding or
a common abstract assignment. `formula_proof_inventory.json` copies existing
receipt fields only. No theorem, review, assurance or acceptance upgrade follows.

## Smallest actionable next stages

1. Main can now inspect the newly acquired PrefixData alongside existing
   PrefixRules/Schema and ClosureData bytes. No execution is needed for that
   source inspection.
2. Once exact deterministic scope and budgets are sent, a fresh isolated Linux
   work area can bind currently acquired Data rows to their codec/schema rules
   and compare reconstructed clauses with verified literal CNF bytes. Existing
   complete Through14/Terminal20 receipts may be reused as historical inputs;
   the exact source/schema/formula equality must have its own new receipt.
3. Joint17's source is already present locally, so uploading those existing
   verified bytes and running bounded extraction/replay is a distinct future
   check, not a missing-source acquisition. The dated Linux snapshot does not
   establish its current server presence.
4. Closure formula/proof extraction and replay remain blocked on verified
   ClosureLiteral bytes. The sole authorized acquisition attempt is exhausted;
   no new network attempt is made. Any source acquisition beyond this point
   needs a newly explicit scope from main/user.
5. Common-model/assignment construction is a mathematical prerequisite owned
   by main. A fixed-byte replay alone cannot fill it. No attempt is made to
   replace that task with finite SAT search or source declaration names.
