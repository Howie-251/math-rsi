# One-coordinate D32 quotient changes with joint Q64 central lifts

The entire authorized 403-projection range is complete with no D3 graph. Exactly 395 projections had at least one empty quotient target slot and were rejected before central scoring. The other eight projections each had all 8,192 center masks legal; all 65,536 assignments were scored exactly. This excludes D3 in this specific one-coordinate quotient-change family, not in all Q64 lifts.

The minimum scored deficit is 36, or 1,152 bad unordered pairs, attained at projection cursor 185 and center mask 3327. This is the minimum over the eight quotient-complete projections; the 395 rejected projections were not centrally scored, so it is not a minimum-deficit claim over all 403 projections. It does not improve the original saved source with 832 bad pairs.

The parent independently reconstructed the saved 1,024-edge graph and checked all 256 roots: simple, connected, 8-regular, diameter 4, and 1,152 bad unordered pairs. Representative deficits are [10,10,8,8]. Evidence is in [best.independent_check.json](best.independent_check.json) and best.independent_distances.json. No additional final BFS was run by this worker; terminal pending is empty.

The first formal central assignment was cursor 37, mask 0. Its production score was reused and its full path forms were saved. Independent Python reconstructed its simple 1,024-edge graph and ran four complete BFS roots; all 1,024 root-target radius-three distances matched the path-form values and minimum lengths. Its root deficits are [20,22,20,22]. See [first.independent_check.json](first.independent_check.json).

The core retains the actual base-edge identity for nonbacktracking walks, including distinct parallel edges with identical projection. It computes zero-bit constants using the true Q64 inverse and multiplication. Each bad-lift condition is an affine GF2 subspace; all its solutions are enumerated exactly. Same-projection parallel edges require different center bits. The mathematical interface is in [CENTRAL_LIFT_MATH.md](CENTRAL_LIFT_MATH.md), and executable scope is in [SCOPE.md](SCOPE.md).

For the eight scored projections, sparse subspace enumeration made 4,192,256 score increments instead of the naive 33,554,432 slot-by-mask visits. This is an operation-count comparison, not a benchmark of a second bitset implementation. No production BFS was used.

| Cursor | Changed edge | New quotient code | Minimum deficit | Best center mask |
|---:|---:|---:|---:|---:|
| 37 | 2 | 6 | 43 | 276 |
| 40 | 2 | 9 | 51 | 82 |
| 185 | 8 | 31 | 36 | 3327 |
| 272 | 11 | 25 | 43 | 2098 |
| 379 | 15 | 7 | 51 | 492 |
| 380 | 15 | 8 | 39 | 119 |
| 387 | 15 | 15 | 51 | 447 |
| 397 | 15 | 25 | 49 | 64 |

CPU: preparation/compilation 1.097140000 s, production 0.013859000 s, sole first-center calibration 0.003134588 s, total driver-accounted 1.117027000 s. The parent-owned final full-root check cost 0.040258260 s separately. Session 9542, worker PID 3748788, and driver PID 3748777 ended with exit code 0. There was no restart or extension of this 403-input run.

The complete per-projection record is projections.jsonl; the original source and exact quotient are retained in source.json and SCOPE.json. The separate authorized two-coordinate range is disjoint and will use the original 832-bad-pair source, not this batch’s best.
