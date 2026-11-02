# Binary AGL(1,7), nonnormal H: complete two-pair/two-involution batch

All **76,384,728** authorized normalized inputs were examined. None gives diameter at most 5. The best fully scored graph covers every point pair involving a block or head; its remaining 28,224 bad unordered pairs are entirely leaf–leaf. This is a completed finite construction-family experiment, not a new degree–diameter lower bound or an exclusion of the other generator compositions.

## Construction and candidate preservation

The actual construction and first-sample calibration are described in `PROFILE_REPORT.md`. In brief, A=F8², K=AGL(1,7) acts faithfully with coordinates `(a,b,e)∈Z7×Z3×Z2`, and H is its nonnormal subgroup a=0. The group law and action are

    (a,b,e)(c,d,f)=(a+(-1)^e*2^b*c, b+d, e+f),
    (u,v) -> (ζ^a*u^(2^b), ζ^(-a)*v^(2^b)), after swapping u,v when e=1,
    (x,k)(y,l)=(x XOR k(y),kl).

The layer sizes are 2688 leaves, 448 blocks, 64 heads, giving 3200 vertices and degree 7. Leaf label is `x+64*k`, block label `2688+x+64*a`, head label `3136+x`. There are 11200 edges. Actual right multiplication by S gives leaf edges; each leaf is joined to its right-H-coset block, and each block to its right-K-coset head.

For the present composition S has two noninvolution inverse pairs and two distinct nonidentity involutions. HH coverage forces one component in each of the four nonzero horizontal K-orbits O7,O14,O21a,O21b. Thus there are six choices of which colours supply involutions.

The sole normalization is conjugation by **H**, which preserves both H and K. The unique O7 component is moved to an H-orbit representative. There are exactly four involution representatives or 26 inverse-pair representatives. `prepare_production.py` independently matched every orbit member to the source's `STRUCTURE_CHECK.json`, including the original lists of 14 O7 involutions and 140 O7 inverse pairs. The other three components range over their complete colour lists. Remaining stabilizers are **not** quotiented, and no factor-of-six division or arbitrary K conjugation is used. Counts therefore describe normalized inputs, not nonisomorphic graphs.

| Branch | Involution colours | Component list sizes after the O7 anchor | Inputs |
|---|---|---|---:|
| 0 | O7,O14 | 4 × 14 × 420 × 420 | 9,878,400 |
| 1 | O7,O21a | 4 × 42 × 287 × 420 | 20,250,720 |
| 2 | O7,O21b | 4 × 42 × 287 × 420 | 20,250,720 |
| 3 | O14,O21a | 14 × 42 × 26 × 420 | 6,420,960 |
| 4 | O14,O21b | 14 × 42 × 26 × 420 | 6,420,960 |
| 5 | O21a,O21b | 42 × 42 × 26 × 287 | 13,162,968 |
| Total | | | 76,384,728 |

Enumeration order is branch, O7 anchor, then the three remaining list indices in component-position order. All 90 anchor intervals are saved in `production.metadata.json`; their actual counts match those intervals exactly in `production.ANCHOR_COUNTS.csv` and `production.terminal.json`.

The earlier 1200-input balanced random profile was **not an enumeration prefix**. Production started from a new cursor 0. No random-profile candidate cache was used to skip production inputs.

## Exact filter and actual evaluation

HH is automatic from the four verified colour lists. The next necessary condition is the exact nonnormal-H two-mask BB formula in `../NONNORMAL_BLOCK_CRITERIA.md`. The optimized implementation enumerates words of length at most 3 without immediate inverse cancellation; every reduced word of length at most 3 is retained, and every discarded word reduces to an already included shorter word. It includes both head-route terms and the identity word.

Before production, its two masks matched the already calibrated version on all 1200 saved profile inputs, with **no new graph expansion or BFS**. See `production.BB_calibration.json`. The earlier actual first-sample independent check also matched all 448 block targets.

Every BB survivor was expanded into the actual graph and evaluated by three depth-five BFS traversals. The left G action preserves the graph and is transitive on each layer; hence the weighted missing count is exact:

    bad pairs = (2688*m_leaf + 448*m_block + 64*m_head)/2.

This is the actual 3200-vertex graph, not a quotient-LL test. A genuine zero score would stop production and save the full graph immediately. No such candidate occurred.

## Complete terminal counts

All 76,384,728 inputs were legal and HH-covered; invalid count is zero. Exactly **299,928** passed BB, and every one of those received all three BFS evaluations.

| Branch | BB survivors / fully scored | Head-root zero among scored | Block-root zero | Best scored bad pairs |
|---|---:|---:|---:|---:|
| 0 | 63,766 | 4,271 | 0 | 52,416 |
| 1 | 72,010 | 5,168 | 0 | 43,008 |
| 2 | 72,880 | 4,729 | 0 | 51,072 |
| 3 | 26,962 | 2,518 | 0 | 47,040 |
| 4 | 24,610 | 2,525 | 0 | 44,352 |
| 5 | 39,700 | 4,418 | 2 | 28,224 |
| Total | 299,928 | 23,629 | 2 | 28,224 |

Among these fully scored BB survivors, root minima are `[21,0,0]` and root-zero counts are `[0,2,23629]`. Every scored graph still misses some leaf–leaf pairs. Four normalized inputs cover all BL pairs; two also cover the entire block and head roots. These two are counts of normalized inputs, not a claim of two nonisomorphic graphs.

The root and layer minima/zero counts are conditional on passing BB. In particular, 23,629 is not claimed to be the number of all head-covered inputs in the full family. The count of inputs with both complete block-root and head-root coverage is exactly two over the full processed family, because any complete block root necessarily passes BB. Likewise, the best bad-pair score is a minimum over the 299,928 fully scored inputs, not over the BB failures.

## Best actual graph

The best saved candidate occurs at production cursor **63,657,826**, branch 5, global anchor 64 (branch-local anchor 0):

    S=[1690,27,73,405,770,967],
    root missing=[21,0,0],
    missing by root/target layer=[[21,0,0],[0,0,0],[0,0,0]].

The exact 11200-edge graph is `production.best.edges`; parameters and labels are in `production.best.json` and `profile_structure.json`. Its bad-pair count is 2688×21/2 = **28,224**, all LL. All BB, BL, BH, LH, HH pairs are covered within five steps. Thus the new nonnormal-H mechanism realizes the complete joint block/head condition, but this generator composition did not complete leaf–leaf coverage.

The inherited profile writer originally printed an incorrect descriptive branch number (`cursor/200`). After the process finished, only that display field was corrected using the exact saved production cursor intervals; the actual enumeration indices, per-branch counters, graph, and score were unaffected. `production.best.json` retains the correction provenance, and `run_production.py` now performs the same correction on final output. No process was restarted or candidate rescored for this label repair.

The independent generic checker rebuilt adjacency from `production.best.edges` and checked all 3200 roots: simple, connected, 7-regular, **diameter 6**, with exactly **28,224** bad unordered pairs, all at distance 6. See `best.independent_verify.json`; its runtime was 0.249207 seconds. The final check did not rerun the earlier preflight or any other graph. The exact all-LL type follows from the saved actual representative-root results and agrees with this independently verified total.

## Budget and scope boundary

The single production process completed at cursor 76,384,728 with `COMPLETE_NO_SOLUTION`. Its CPU time was about 103.393 seconds; the driver-inclusive production charge was 103.396659. Prior profile, first-candidate independent verification, and new compilation/preparation brought the cumulative recorded charge to **106.524997298 CPU seconds**, below the 360-second limit. There were no restarts and no additional parameter or topology.

The first-million observation used 1.769931 CPU seconds: HH construction/counting 0.179991, BB 0.717107, actual graph construction/BFS 0.683990, other overhead 0.188843. Fine-grained timing was stopped after that observation to avoid charging its repeated clock calls throughout the full batch. `production.first_million.json`, `production.progress.json`, `production.log`, and `production.summary.json` retain the actual measurements.

This complete computation closes only this normalized two-pair/two-involution range for the specified group action and tower. It is discovery-level finite computational evidence, not a formal certificate. The zero-pair and one-pair generator compositions are **not included** and remain open here. No subsequent search was started.

Including the final independent checker, the cumulative recorded charge is **106.774204298 seconds**. All requested verification is complete; no independent result remains pending.
