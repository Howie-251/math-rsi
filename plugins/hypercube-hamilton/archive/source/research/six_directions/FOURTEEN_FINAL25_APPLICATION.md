# Exact positive application to the final 25 covered-target geometries

Producer claim, awaiting independent review. The source gate is `FOURTEEN_MID_SELECTED_REVIEW.json`, which must reach final PASS before an application review accepts the upstream reduction. The frozen producer source is `FOURTEEN_MID_SELECTED_PROOF.md` / `FOURTEEN_MID_SELECTED_MANIFEST.json`, and the exact raw inputs are `FOURTEEN_MID_SELECTED_remaining_v{1,7,31}_covered.bin`. No draft review is imported.

The source counts are 0/0/25. Every record is sorted Z6 followed by sorted W7, 13 bytes. The 25 target-31 records split into the two simultaneous coordinate orbits in `FOURTEEN_FINAL25_PROOF.md`, of sizes 20 and 5. `FOURTEEN_FINAL25_actual_witnesses.bin` records all 25 source indices and actual-to-representative common maps, 7-byte `<BIBB>` entries: target, source index, orbit, permutation. All maps fix root 0 and target 31 and preserve short edges. No source index is repeated.

Each representative theorem quantifies over **every original short matching** with the exact uncovered set. Its proof extends the actual internal-A matching to one of the 805006 maximal-domain records, then lifts the selected positive forest back to the actual submatching. Both actual internal-target and actual crossing-target edges are handled; the maximal record's target flag does not decide the actual case. The five exact new B inputs and the actual obstruction-safety proof are needed together.

The maximal-A positive counts are 291743 for orbit 0 and 513263 for orbit 1. The chosen local inputs are 0,1,7 and 100,101, all N22 reduced to N20 by one forced pair, each with 512 positive forests and a full-rank reduced matrix. The producer includes 2560 forests/columns and 1310720 matrix bits, 805006 A certificates of 32 bytes, all simultaneous A/B maps, and a direct independent-order DP count method. Producer author replay is not independent acceptance.

Exact positive subset and byte-complement checks give:

| target | source | positive | remaining |
|---|---:|---:|---:|
| 1 | 0 | 0 | 0 |
| 7 | 0 | 0 | 0 |
| 31 | 25 | 25 | 0 |

All three `FOURTEEN_FINAL25_remaining_v*_covered.bin` files are empty. This application closes only the final 25-source subset once its theorem and source gate are accepted. It does not itself assemble all free/covered branches, establish the entire fourteen-hole layer, or prove P6. No ledger or frozen upstream artifact was changed.
