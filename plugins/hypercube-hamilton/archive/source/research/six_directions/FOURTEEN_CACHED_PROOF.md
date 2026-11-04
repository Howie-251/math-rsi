# Fourteen-hole residual: cached-positive candidate reuse and exact greedy subset

2026-11-02. Producer-only computational/proof preparation by `/root/higher_forced_cherry_review`. **No new local input or actual application is independently accepted by this document.** The old source/registry files and the frozen FOURTEEN_REUSE package remain unchanged. This is not full fourteen holes; the source reduction still depends on complete twelve-hole Q6, which is not asserted here.

## Exact source and candidate result

The six frozen `FOURTEEN_REUSE_remaining_h14_v{1,7,31}_{covered,free}.bin` files contain48211 original-label13-byte records (Z6 followed by W7), with free root0 and the named odd target. Their first-stage producer source gate is `FOURTEEN_REUSE_MANIFEST.json`; that application's fresh independent acceptance is a separate pending gate. No matching-realizability exclusion is used.

This second stage uses only cached producer-positive local inputs not selected into the already accepted registry:121 of the232 positive `TWELVE_NEW_TYPES_summary.json` rows, and282 of the293 positive `TWELVE_EXTRA_TYPES_summary.json` rows. These403 candidates yield74050 normalized marked keys. Producer full_rank flags identify candidates only, not proofs.

| Target/status | Input | Candidate covered | Exact candidate residual |
|---|---:|---:|---:|
|1 covered|9285|6180|3105|
|1 free|0|0|0|
|7 covered|16108|12495|3613|
|7 free|18|0|18|
|31 covered|22500|16690|5810|
|31 free|300|300|0|
|Total|48211|35665|12546|

The remaining covered count is12528; remaining free count18. These are candidate sufficient subsets conditional on their new local certificate gates, the application gate, and the source gate. They are not newly accepted geometries or counterexamples.

## Actual source/cut predicate

For every original record, try all six target-facing cuts and every legal source subset of the actual type. With k=7, even consumption has s=a+1-b, minority6-a and majority7-b+s, with sources among A Z holes and b>=1. Odd consumption has s=b-a-1, minority7-b and majority6-a+s, with sources among A W holes excluding root mirror and a free target. The code explicitly checks source counts/pool and rejects any mirror which is an original hole/root.

Delete only the outer coordinate, then transform actual minority, majority and marked mirror omissions together. A minority anchor is used when present, otherwise an omission anchor. For each cached canonical row every corresponding source anchor and every coordinate permutation is included. A hit is tied to a named exact cache row/prefix, not just to a type or unmarked hole count.

The scan examines1434085 legal source projections in about0.934 seconds. It retains one witness per **source record/candidate orbit** rather than stopping at the first orbit. Exactly278524 such distinct hits occur, across161 of the403 candidate rows. Thus the complete candidate union is defined by source-index sets, not by adding overlapping orbit counts.

Each per-status `FOURTEEN_CACHED_all_hits_h14_v{v}_{status}.bin` record has28 little-endian bytes: original13-byte-source index uint32; family uint8 (30=NEW cache,31=EXTRA cache); cut uint8; exact local ID uint16; original-label source mask uint64; actual projected minority, majority and omission masks (three uint32). The target and free/covered status come from the filename.

## Greedy sufficient registry: only twenty new local obligations

Greedy selection repeatedly chooses the candidate row with largest uncovered source-record gain, breaking ties by its numerical code (NEW index, EXTRA1000+index). This is a convenient deterministic selection, **not a minimum-cardinality theorem**. The selected twenty rows have exactly the same source-record union as all403 candidates. A chosen selected witness is stored per covered source record; all other source records are copied unchanged in original order to the six `FOURTEEN_CACHED_remaining_h14_v{v}_{status}.bin` files. The greedy script checks complete residual-byte equality with the earlier exhaustive candidate scan outputs.

The exact ordered chosen codes are:

```
1040,1007,1186,1156,1016,1248,1148,1041,1300,1132,
1118,1069,1246,1006,1251,1252,1288,161,1205,318
```

An EXTRA code1000+i denotes prefix `TWELVE_EXTRA_TYPES_orbit_iii`; a NEW code i denotes prefix `TWELVE_NEW_TYPES_orbit_iii`, with three decimal digits. The explicit geometries, indices and original certificate prefixes are in `FOURTEEN_CACHED_greedy_registry.json`. Ten selected rows are T26, eight T17 and two T28.

Only these20 new positive local certificate statements are needed to promote the candidate union. The remaining141 active candidates and other inactive candidates are not mathematical premises. Their actual finite hit sets only supplied a target union for choosing a sufficient subset.

| Selected type | Inputs | Covered terminals | Rank each | Forest edges | Total forests | Connectivity bits |
|---|---:|---:|---:|---:|---:|---:|
|T26|10|24|2048|18|20480|41943040|
|T17 unforced|8|24|2048|17|16384|33554432|
|T28 unforced|2|22|1024|18|2048|2097152|
|Total|20|—|—|—|38912|77594624|

All selected witnesses already exist in the old producer cache. The new manifest pins each selected config/metadata/forest/pair/column/matrix/pivot/combination file without editing any of them. A fresh local checker must independently verify all38912 forests and columns, derive their actual endpoint pairings, rebuild all77594624 connectivity bits, and verify exact GF(2) ranks. Producer ranks are not that check.

## Conditional local proof and global transfer

Once verified, the local positive proof is the accepted generic forest-rank argument: legal short forests have degree0 at marked omissions,2 at included holes,1 at covered terminals and no cycles; their endpoint matching rows span the complete matching-connectivity row space when a valid submatrix reaches the generic GF(2) upper bound. Every arbitrary complete-graph matching column is nonzero by cyclically joining its oriented matching edges. Hence some selected forest connects each arbitrary required matching; expansion gives the exact local cycle with short new edges. Common required/forest edges form improper labeled two-edge components and cannot survive connectivity. Required edges may be long or same-parity.

All selected applications use the following k7 rows:

- T26: even(a,b)=(4,3) or odd(2,5), two sources, completed A holes3:3;
- T17: even(5,3) or odd(2,6), three sources, completed A holes3:3;
- T28: even(4,2) or odd(1,5), three sources, completed A holes2:2.

These lie inside even the original accepted uniform transfer's b<=3 / a<=2 ranges. Original M is short, nonroot holes independent, source exclusions preserve root/target, and mirrors are originally internally covered. The completed A endpoint theorem allows arbitrary artificial completion edges and a covered/free prescribed target. Forest compression and simultaneous pendant-mate suppression yield the actual B matching with exactly the looked-up marked set. The new candidate local inputs, if independently accepted, are universal on arbitrary complete-graph matchings, so they apply to every such actual compressed L. Expansion removes completion placeholders and restores every original matching edge with short new physical edges.

No forced local pair classification is used in this cache stage. No root-in-obstruction workaround, unreviewed A opening, MAmax or new rank search is imported. The cut/source witnesses are geometric; local paths/completions may depend on actual M. Thus the every-realizing-M quantifier has the correct conditional route once the independent local/application gates pass.

## Reproduction and gates

```
python FOURTEEN_CACHED_prepare.py
g++ -std=c++17 -O3 FOURTEEN_CACHED_scan.cpp -o FOURTEEN_CACHED_scan.exe
./FOURTEEN_CACHED_scan.exe
python FOURTEEN_CACHED_greedy.py
python FOURTEEN_CACHED_freeze.py
```

Fresh acceptance requires: first-stage FOURTEEN_REUSE actual application;20 new local certificates; complete actual candidate/selected witness replay with common marked transforms; exact selected-union residual complements and source hash alignment. The greedy optimality and completeness of an ambient geometry classification are not required. No full14 or full P6 statement follows from this producer package.
