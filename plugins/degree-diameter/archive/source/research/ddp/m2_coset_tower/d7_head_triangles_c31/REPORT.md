# p31 cyclic head-triangle tower: production result

**Actual terminal: `COMPLETE_NO_SOLUTION`**, cursor **18,829,360 / 18,829,360**.

The complete 18,829,360-input safely reduced marked scope was checked with no diameter-5 graph. By the preserved scope in SCOPE.md this computationally excludes all HH-compatible generating sets in this fixed cyclic head-triangle tower. It does not exclude arbitrary degree-7 graphs or the whole M2 mechanism.

The earlier 1,400 random stratified samples are preserved in [PROFILE_REPORT.md](PROFILE_REPORT.md). They were not an enumeration prefix, were not subtracted from production, and their scores were not used as cached production results. Only their 1,400 already-saved BB masks were reused for formula calibration, without generating a graph or running BFS. The separate p43 profile is finished and paused; its sole final independent check found D6, not D5.

## Preserved scope and exact iterator

[SCOPE.md](SCOPE.md) proves the 35,305,050 marked parent range covers every HH-compatible inverse-closed six-element set for this fixed tower. The action uses G=(F31⋊_3 C30)×C3, H=<k^5>, K=C30. HH compatibility forces t=1 or2 cross inverse pairs, at least one nonzero-field cross component, and at least one nonzero-field internal component. A marked nonzero w1 representative is scaled to (1,1,j).

The authorized safe reduction uses T_j=F_(-3^j) composed with C3 inversion, mapping the marked exponent j to -j. It keeps all **16 layers j=0..15**, including **all parameters at fixed layers 0 and15**. Other cross representatives transform as (x,1,k) -> (3^(j-k)x,1,-k), and internal field coordinates scale by -3^j. This is the proved coverage reduction of SCOPE §6, not division by two or a claim of free action. Multiple markings in t2 remain allowed.

Actual internal pools are 31 involutions and 449 noninvolutory inverse pairs, of which 14 pairs have zero field. The five C++ internal lists have sizes **31,465 / 208,785 / 100,485 / 465 / 435**. The t1 two-pair list omits only pairs of zero-field components; the t2 pair list requires nonzero field. For t2, the second w1 representative is encoded by ci=0..929 and only ci=31*j+1 is excluded, exactly the marked anchor. Its field may be zero. Different inverse components are disjoint by construction.

The iterator order is branch, actual internal-set index, j=0..15, then the second w1 representative for t2. It starts at cursor0 and includes an exact cursor formula checked during production. All actual branch counts match the independent SCOPE.json arithmetic and a narrow independent read-only check found no omitted component or fixed layer. The actual scope is **18,829,360**, split into t1 **5,451,760** and t2 **13,377,600**.

| Branch | Full safe scope | Actually checked | BB passes / actual scores | Conditional root minima L/B/H | Full B+H roots |
|---|---:|---:|---:|---|---:|
| 0 t1: four involutions | 503,440 | 503,440 | 0 | — | 0 |
| 1 t1: one pair plus two involutions | 3,340,560 | 3,340,560 | 133,649 | 119/0/0 | 1 |
| 2 t1: two pairs | 1,607,760 | 1,607,760 | 78,008 | 35/0/0 | 6 |
| 3 t2: two involutions | 6,911,760 | 6,911,760 | 284,745 | 121/0/0 | 4 |
| 4 t2: one nonzero pair | 6,465,840 | 6,465,840 | 348,295 | 25/0/0 | 10 |

## Exact filter, actual graphs and statistics

Every input in this iterator satisfies HH. The original BB reachable sets are computed exactly in five multiplicative-H-orbit masks, each containing 18 bits. All nonzero field orbits have size6; zero-field orbits have size1 and are always covered by identity/head-triangle routes. Thus BB missing is a multiple of6. The same formula's masks match all 1,400 prior actual block-root BFS results. The necessary BB test is the only production filter.

All **844,697 BB survivors** actually pass through graph expansion and three-root depth-5 BFS, with a pointwise check against all 465 BB targets. Leaves=2790, blocks=465, heads=93; n=3348, degree7, edges=11718. The builder includes all93 head-triangle edges and checks simple regular adjacency. Left G preserves all graph edges and acts transitively on each layer, so weighted root scores give the exact total of bad unordered pairs.

Among the **844,697 BB survivors**, root minima are **[25, 0, 0]**, root-zero counts are **[0, 44, 71338]**, and **21** inputs have both block and head roots complete. These are conditional counts; rejected BB inputs were not BFS-scored. Coordinatewise minima can occur on different inputs.

Complete block/head-root candidates are saved in `production.block_head_complete.jsonl`, with actual generating sets, positions and scores. These are not successes unless their leaf root is also complete. The first such candidate was cursor1,194,332, S=[1148,1763,294,2538,1414,1416], with roots242/0/0 and 337,590 bad unordered pairs, all LL. This observation changed which route condition remained open in that candidate but did not justify skipping LL.

The global exact BB histogram, per-branch counts and conditional root/layer statistics are in `production.terminal.json`. No full-root population is claimed for inputs rejected by BB. Next position is `None`.

## Saved final graph

Selection: `minimum_bad_pairs_among_BB_survivors_in_completed_prefix`. This minimizes bad pairs among the actually scored BB survivors in the executed range, not among BB-rejected inputs.

    position={'branch': 4, 'internal_index': 258, 'anchor_j': 4, 'second_cross_w1_index': 171, 'cursor': 16202318}
    S=[404, 2493, 512, 2415, 841, 1955]
    root missing=[25, 0, 0]
    layer missing L/B/H:
      [25, 0, 0]
      [0, 0, 0]
      [0, 0, 0]
    bad unordered pairs=34,875

Its type counts are {'LL': 34875, 'LB': 0, 'LH': 0, 'BB': 0, 'BH': 0, 'HH': 0}. These follow from the recorded exact representative-root distances, without another BFS. Complete edges and actual parameters are `production.best.edges` and `production.best.json`. If an independently verified D5 graph is not returned, this diagnostic cannot count as a new lower bound.

## Actual budget and terminal evidence

The fixed budget is one worker and cumulative **360 CPU seconds**, including the preceding shared profiles' 2.805399 seconds. New preparation, compilation and saved-mask calibration cost 1.563972 seconds. Production driver's actual cost was 280.528777 seconds; cumulative implementation/profile/production cost is **284.898156 seconds**. Independent final verification is separately recorded. No process restart, extra parameter, seed continuation or budget enlargement occurred.

The first100,000 actual inputs cost0.211690 CPU seconds, with0.194087 seconds in the BB frontend and no surviving graph in that first four-involution prefix. This was explicitly not treated as the full-production cost estimate; subsequent actual BFS costs remained inside the same process budget. `production.first100k.json`, `production.log`, `production.run.json`, `production.prepare.json` and `production.summary.json` preserve the real checkpoints and final cursor.

## Independent final verification

The sole independent final check is complete. All 11,718 edges match an independent group reconstruction. Full-source BFS of all 3,348 roots confirms a simple connected 7-regular graph of diameter 6, with 34,875 bad unordered pairs, all LL and all at distance 6. The three-root counts 25/0/0 and all 465 BB targets/masks agree independently. Results are in `production.best.independent_check.json` and `best.independent_verify.json`. The additional actual CPU was 0.238365387 seconds; cumulative cost including this independent final is 285.136521387 seconds. The earlier profile-best and first sample were not independently full-source checked, and no check is pending.
