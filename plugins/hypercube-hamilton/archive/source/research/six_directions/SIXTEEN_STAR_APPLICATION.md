# Exact application of the sixteen-hole root-star package

This is a producer application, pending independent review of `SIXTEEN_STAR_PROOF.md` and the frozen finite data. The source is the final PASS `SIXTEEN_LOCAL_REVIEW.json`, binding the exact 148 covered-target geometries in `SIXTEEN_LOCAL_remaining_v{1,7,31}_covered.bin`. Records are 15 bytes, sorted Z7 followed by sorted W8.

The new theorem applies to exactly one representative and its coordinate orbit:
$$v=31,\quad Z=\{39,43,45,51,53,57,63\},\quad W=\{1,2,4,8,14,16,22,32\}.$$
Only the five coordinates within 0..31 are permuted; coordinate 32 stays fixed. All permutations fix root 0 and target 31. The actual-to-representative maps are recorded in `SIXTEEN_STAR_actual_witnesses.bin`, using `<BIB>` records: target, original source index, permutation index. This is a 30-record/180-byte positive application file. Its source IDs are unique.

The exact set equality to verify is: the positive subset consists of all source records whose two hole sets simultaneously map to this representative; the three output raw files are precisely the byte-preserving ordered complement. Counts are

| target | input | positive | remaining |
|---|---:|---:|---:|
| 1 | 0 | 0 | 0 |
| 7 | 18 | 0 | 18 |
| 31 | 130 | 30 | 100 |
| total | 148 | 30 | 118 |

Every matching on each positive geometry is covered: pull it back through the recorded coordinate map, retain all actual internal-A matching edges, extend that matching to an inclusion-maximal T-covered short matching, use its positive A record, and apply the simultaneous certified B input. The proof does not quantify only over the maximal matchings as original inputs; the maximal-lift argument preserves the arbitrary actual submatching, its target mate, and the prescribed root port. Target 31 has its cross neighbor 63 in Z, so its actual edge is internal before any maximal extension.

The three B local inputs are exactly indices 5,6,7 of `SIXTEEN_STAR_B_summary.json`, not all 20 exploratory candidates. Each has 256 positive forests and full reduced rank 256. The finite A domain is 120463 (size-9:120075; size-8:388), with 120463 positive 32-byte records. `SIXTEEN_STAR_author_finite.json` and `SIXTEEN_STAR_B_author_check.json` describe producer checks; neither is independent acceptance.

The surrounding reduction of the entire sixteen-hole layer remains conditional on the complete fourteen-hole theorem. This package leaves 118 geometries for further work and does not prove full fourteen holes, full sixteen holes, or P6. No ledger or previously frozen source file is changed.
