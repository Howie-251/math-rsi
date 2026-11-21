<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# Verified full-query evidence

Authoritative Linux root: `<private-artifact-root>`.

| Query | Bound | Variables / clauses | Original solve / actual check | Full proof SHA256 |
|---|---:|---:|---:|---|
[Process-control details omitted; historical mathematical status and receipts retain their separate scope.]
| `global-h11` | holes <= 11 | 69,208 / 2,168,962 | 330.20 s / 280.17 s, CHECKED_UNSAT | `7d7703f258757851b40f5251d77647f591d4dc75961eedb77cb6da39d62572d6` |

CNF hashes are respectively `b47b58b2da4a29dfeb2b3122a25cff8f42ef9c6e69cc6d52d41e997aaab2eb32` and `4ac85311d51cc9cc731a60d5d189101554e319ed3a861f1a6d78a5f3681e1497`. Proof sizes are 100,341,770 and 269,214,281 bytes. Each original solve returned 20; each actual external checker returned 0 with `s VERIFIED`.

H10 independent replay has passed. It independently regenerated all 2,165,442 baseline clauses, the 575 distinct necessary support rows, 2,876 Hall clauses from all 15 charge subsets, original-P units -1 and -2, and threshold upper unit -69207. The regenerated complete CNF has the exact original hash. A second full DRAT check returned 0 and exactly one `s VERIFIED` marker in 72.61 seconds. Its receipt is `global-h10/independent-replay/VERIFICATION.json`.

H11 independent replay has also passed. It independently regenerated all 2,165,442 baseline clauses, 641 distinct support rows, the same 2,876 Hall clauses and actual-P endpoint units, and upper unit -69208. The complete rebuilt CNF has the exact original hash. Its second actual DRAT check returned 0 and exactly one `s VERIFIED` in 279.88 seconds (288.45 seconds including reconstruction). The receipt is `global-h11/independent-replay/VERIFICATION.json`.

The separate upstream worker independently replayed the old271 and m32_208 standalone packages in fresh directories. It also rechecked the 42 original cores behind the frozen H11 162-row feed, verified all 1,982 nonoccupancy clauses against the original base, and recomputed the four grid-orbit supports exactly. Its H11 full-query comparison independently agrees on the base prefix, 641 rows, 2,876 Hall clauses, original-P endpoints and budget unit. The independent upstream receipts are archived as `upstream-h10-VERIFICATION.json` and `upstream-h11-VERIFICATION.json`; their authoritative originals are under `<private-artifact-root>` and `h11-upstream-independent01/`.

Every input is a one-read immutable snapshot under the corresponding `inputs/` directory. H10 uses old271 + m32_208 + 96 fresh grid-orbit rows; H11 uses old271 + m32_208 + 162 fresh grid-orbit rows. The original baseline hash is `6ac37a76af080e68b1342c6679004a39a40e943e421f4fc688017227a251251d`. The original builder hash is `3d7a9b93c1335ddf4ae76fa58fa870c5c3324fe01cad84cf0f4d3cf72f93c4a2`. The authoritative AE binary and actual repaired DRAT checker are hash-bound in each manifest.

The parent task and independent upstream worker connect these necessary formulas to ordinary N(8,6,6), audit the old271/m32_208/fresh-feed proof sources and prove the Hall/actual-P conditions. This evidence report does not replace that mathematical bridge with a solver status. No fixed Delta, central population or selected mask occurs in either global formula.

The earlier fixed-mask result is `ALL_COVERAGE_AUDIT.json`: PASS_COMPLETE_1750_COVER, all 1750 original indices, 59 original small cores actually rechecked, 208 distinct I/T/D/DT necessary rows, and 2,063 nonoccupancy core clauses independently found in the immutable baseline. Its 10,009,784-byte self-contained bundle was actually replayed in a fresh Linux directory and transferred locally with SHA256 `3c89c7b476e9eeed4e516542ad5f56173cc1882c47637c404729914c73a1b95e`.

Only the owned redundant mixed-H11 exploration was stopped after the second global H11 proof check passed; its termination record has no remaining process IDs. All completed and partial exploratory files were preserved. H12 was not launched.

The final [full replay archive](../../../SOURCE_MAP.md#excluded-sources) is locally present in this stable directory: 168,233,569 bytes, SHA256 `e60fff51f73e7c8c39a4a65b5ec9fda2e619c0880ef60e54858b630c03b30000`. All 21 parts and the reassembled whole archive passed byte hashes; [LOCAL_BUNDLE_RECEIPT.json](../../../SOURCE_MAP.md#excluded-sources) records the exact local result. The identical archive was actually extracted into a fresh Linux directory and both full proofs checked again, independently rebuilding the exact CNFs: [FINAL_BUNDLE_REPLAY.json](../../../SOURCE_MAP.md#excluded-sources). These final archive replays add a third actual full proof check to each budget.
