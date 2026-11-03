# Three faithful-action families: completed finite search

The three authorized degree-5, target-diameter-5 families contain no qualifying graph. This is a finite result about the two-orbit template with one inverse pair inside each orbit and three cross generators, over the three specified groups. It is not an exclusion of other degree-5 graphs or other allocations of generators.

## Family and reduction

For `G = F_p ⋊ C_m`, multiplication is

`(x,i)(y,j) = (x + r^i y, i+j)`.

The graph has vertices `(0,g),(1,g)`, internal generators `A={a,a^-1}`, `B={b,b^-1}`, and cross generators `S={e,s,t}`. The input quotient skeleton lists the residues of `(a,b,s,t)`. The translations are four field elements in the same order.

For a fixed quotient skeleton, simultaneous conjugation by `(u,0)` changes the four translations by `u*(1-r^alpha,1-r^beta,1-r^sigma,1-r^tau)`. A first nonzero coefficient allows one coordinate to be set to zero. Global field scaling is a group automorphism, so the remaining three coordinates have `p^2+p+1` nonzero projective representatives. The zero class is excluded separately because all generators then lie in a common conjugate of `C_m`. The quotient skeletons generate `C_m`; their canonicalization and complete orbit checks are recorded by `canonical_faithful.py` and `batch.json`. An independent mathematical check is in `m1_d5_faithful_reduction_check.md`.

The generic search rejects an identity internal generator, then a nonidentity internal involution, then collisions among `e,s,t`. These categories are disjoint by this priority. For `p=41,m=8,r=3`, every element with quotient residue 4 is an involution; the implementation rejects the whole internal residue class. Cross generators are allowed to be involutions.

## Completed enumeration

| p,m,r | Vertices | Skeletons | Projective points visited | Legal fully scored | Illegal | Minimum missing sum | Bad unordered pairs in best graph |
|---|---:|---:|---:|---:|---:|---:|---:|
| 109,3,45 | 654 | 9 | 107919 | 105952 | 1967 | 40 | 6540 |
| 41,8,3 | 656 | 173 | 298079 | 196431 | 101648 | 25 | 4100 |
| 37,9,7 | 666 | 240 | 337680 | 329322 | 8358 | 6 | 999 |

All 422 skeletons and all 743678 nonzero projective points were completed. There were 631705 legal graphs fully scored. The 422 zero classes were excluded separately and are not included in the projective or illegal counts. The illegal category counts `(identity, involution, cross collision)` were respectively `(878,0,1089)`, `(2598,96068,2982)`, and `(3411,0,4947)`.

Each legal candidate receives complete depth-5 BFS from the two orbit representatives. Left multiplication by `G` is a graph automorphism, so these two tests exactly determine diameter at most 5. If their missing counts sum to `s`, the full number of bad unordered pairs is `|G|*s/2`. No early failure cutoff was used for scoring, so the reported minima are global over the input skeletons and projective representatives.

The batch used one CPU sequentially, with a cumulative 120-second wall limit. It ended normally after 9.764 seconds wall and 9.45186 child CPU seconds. Per-case CPU seconds were 1.34103, 2.85006, and 5.26077. No extra group, seed, or extension was run.

## Exact best parameters and independent checks

The best parameters, in the `(a,b,s,t)` order, were:

| p,m,r | Quotient residues | Translation values | Two representative missing counts |
|---|---|---|---|
| 109,3,45 | (0,0,1,2) | (1,37,0,10) | (16,24) |
| 41,8,3 | (3,3,1,3) | (0,1,6,34) | (11,14) |
| 37,9,7 | (1,4,2,4) | (0,1,33,24) | (5,1) |

The existing independent edge-list verifier performed full BFS from all 654, 656, and 666 vertices. Each saved graph is simple, connected, 5-regular, and has diameter exactly 6. Its bad-pair total matches the table. Thus none is a successful diameter-5 construction.

Before this batch, the generic implementation repeated the complete old `13,27,3` enumeration. All 267912 projective counts, 260922 legal counts, 6990 illegal counts, the minimum 12, and the entire score histogram matched the old implementation. The generic regression took 4.36249 seconds and rejected no internal involutions, as expected for odd group order. The original implementation and original evidence were preserved.

## Files and reproduction

Code is `computations/ddp/m1/d5_quotient/search_projective_generic.cpp`, with the existing compiled executable alongside it. The authorized batch wrapper is `computations/ddp/m1/d5_quotient/faithful/run_batch.py`. It reads the root-generated `faithful/batch.json` and the three `*.skeletons.txt` files, and runs:

```
search_projective_generic P M R SKELETONS REMAINING_SECONDS OUTPUT_PREFIX
```

In `computations/ddp/m1/d5_quotient/faithful/`, `batch_results.json` records the actual terminal results and CPU times. For each case, the prefix is `pP_mM_rR.search`: `.summary.json` has the full score histogram and terminal state; `.skeleton_results.jsonl` records every completed skeleton and count; `.best.json` has the parameters; `.best.edges` has the complete graph; `.best.independent_bfs.json` has the all-root verification. `batch_process.json`, `batch_current.json`, and case logs identify the completed processes and commands. The old regression comparison is `generic_regression.check.json` in the parent directory.

Every per-skeleton status and count was checked against the summaries, and each independent BFS result was checked against the exact parameter score. This batch is complete; no process remains live.
