<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# Ordinary N(8,6,6) <= 58

The original 59 target and the stronger 58 target are proved by the full-domain original-P state/shared-label argument. No central-population or Delta restriction enters the final global queries.

- [Mathematical proof](../../../research/N866_ORDINARY_BOUND_PROOF_20261119.md)
- [Readable computational verification](VERIFICATION.md)
- [H10 independent formula reconstruction and actual DRAT replay](../../../SOURCE_MAP.md#excluded-sources)
- [H11 independent formula reconstruction and actual DRAT replay](../../../SOURCE_MAP.md#excluded-sources)
- [H10 upstream kernel audit](../../../SOURCE_MAP.md#excluded-sources)
- [H11 upstream kernel audit](../../../SOURCE_MAP.md#excluded-sources)

Both full queries were checked twice with the actual repaired external DRAT checker. The baseline's 2,165,442 clauses were independently regenerated. Every appended support row, all 15 Hall groups (2,876 clauses), original-P endpoint units and cardinality upper unit were reconstructed and hash-matched. The independent upstream audit replays the imported kernel proofs and their legal grid transports.

The complete [local replay archive](../../../SOURCE_MAP.md#excluded-sources) is present and verified: 168,233,569 bytes; SHA256 `e60fff51f73e7c8c39a4a65b5ec9fda2e619c0880ef60e54858b630c03b30000`. All 21 transfer parts were individually hash-checked and reassembled directly into this directory; the whole archive hash exactly matches Linux: [local receipt](../../../SOURCE_MAP.md#excluded-sources). [BUNDLE_MANIFEST.json](../../../SOURCE_MAP.md#excluded-sources) records the part hashes. The same final archive was actually unpacked into a new Linux directory and both full proofs replayed successfully: [fresh archive replay receipt](../../../SOURCE_MAP.md#excluded-sources).

On Linux, extract the archive into a fresh directory and run:

```sh
python3 verify_full_bundle.py --checker /absolute/path/to/drat-trim --budget 10 11
```

The replay verifies all archived file hashes, regenerates the exact full CNFs from the baseline and bound input snapshots, and performs the actual full proof checks. The archive also contains the original 271-row standalone evidence, the independently replayed 1750-mask/208-row package, original fresh-feed small cores, source snapshots and verification receipts. All source directories remain preserved.

Authoritative Linux originals:

```text
<private-artifact-root>
<private-artifact-root>
<private-artifact-root>
```

All scientific execution and proof checking occurred on Linux. Auxiliary mixed-H11 jobs owned by this task were stopped only after the full H11 reconstruction and second proof check passed; their artifacts remain available. No H12 task was launched.
