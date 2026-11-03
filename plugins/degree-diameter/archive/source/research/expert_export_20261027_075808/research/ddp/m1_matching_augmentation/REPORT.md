# Six-matching augmentation of the 2810-vertex source: ten-candidate profile

The ten predetermined candidates were completed and independently checked. Every graph is simple, connected, 7-regular on 2812 vertices, but every graph has diameter **6**, so none improves the degree-7, diameter-5 lower bound. The best candidate has **364** bad unordered pairs: **350 old–old** and **14 new–old**. The batch is finished, with no additional candidate or trajectory started.

## Exact construction and legality

Start with the verified public 2810-vertex graph in `research/ddp/m1_d7d5_source/baseline_normalized.edges`. Choose six oriented old edges `(a_i,b_i)` with twelve distinct endpoints. Delete those edges, add vertices `u=2810`, `v=2811`, and add `uv`, all six `u a_i`, and all six `v b_i`.

Each old matching endpoint loses one edge and gains one, every other old vertex retains degree 7, and each new vertex has six old neighbors plus the other new vertex. Distinct endpoints make the attachments distinct; the new labels prevent loops or old/new edge collisions. Hence the result is simple and 7-regular, with 2812 vertices and `9835−6+13=9842` edges. Connectivity follows by replacing every deleted old edge `a_i b_i` in an original path by the walk `a_i-u-v-b_i`. No assertion about diameter follows from these degree and connectivity facts.

Let `H=G−M`, `A={a_i}`, `B={b_i}`, `a(x)=d_H(x,A)`, and `b(x)=d_H(x,B)`. Allow infinite distances if `H` is disconnected. The exact new-root distances are

```
d(u,x) = min(a(x)+1, b(x)+2),
d(v,x) = min(b(x)+1, a(x)+2).
```

The exact old–old distance is

```
min(d_H(x,y),
    a(x)+a(y)+2, b(x)+b(y)+2,
    a(x)+b(y)+3, b(x)+a(y)+3).
```

For the lower bound, a shortest path uses neither new vertex, just one, or both; if it uses both, their joining subpath can be replaced by the edge `uv`. These are the five terms. Each finite term also supplies a walk of that length, proving the reverse inequality. Both new roots cover every old vertex within five steps exactly when every old `x` satisfies `min(a(x),b(x))≤3` or `max(a(x),b(x))≤4`.

The independent checker verified these formulas against full BFS for all 3,946,645 old–old pairs and all 5620 new–old pairs in each candidate, with zero mismatches.

## Ten fixed generation policies

The source's known semidirect-product presentation gives seven undirected edge orbits of size 1405: internal A, internal B, and cross voltages `e,412,1338,186,45` in its normalized labels. Candidates 00–06 restrict the six selected edges to one of these orbits. Candidates 07–09 permit all edges and respectively prioritize balanced new-root coverage, low single-edge distance-5 damage, and endpoint separation. The policies are saved in `policies.json`; no random generator or seed was used.

At each greedy step, an oriented edge `(a,b)` contributes `B_G^4(a)∪B_G^3(b)` to the prospective coverage of `u`, and the swapped expression to `v`. Coverage policies first maximize the smaller covered count, then the sum, then analogous counts covered by at least two selected matching edges. These are balls in the original graph, so they provide an upper bound on coverage after deleting the matching, not a proof of final diameter. Ties use the stated edge-damage and separation quantities, then deterministic edge/orientation order. All candidates have six mutually disjoint edges; duplicates up to exchange of the two new vertices were skipped.

The edge-damage quantity `critical5(e)` counts unordered original distance-5 pairs for which **every shortest path uses e**. It is computed exactly by intersecting edge sets over predecessor paths in each BFS shortest-path DAG. Deleting `e` destroys all length-at-most-5 paths for precisely those original distance-5 pairs. This count does not include damage to pairs originally closer than 5, and sums over a matching do not account for interaction or overlap between deletions. It is a selection signal, not an exact damage objective for six deleted edges.

The seven orbit values of `critical5` are respectively **70,69,65,90,87,78,71**. All 2810 source-root distance computations were completed before generating the ten candidates.

## Full results, ordered by total bad pairs

Every row has diameter 6, no unreachable pairs, and no bad `u,v` pair. “H damage” counts old pairs at distance greater than 5 after deleting the six edges; “repaired” counts those restored by the two new vertices.

| Candidate | Policy | Total bad | New–old bad | Old–old bad | critical5 sum | H damage | Repaired | New roots' missing counts |
|---|---|---:|---:|---:|---:|---:|---:|---|
| 02 | cross e only | 364 | 14 | 350 | 390 | 514 | 164 | (9,5) |
| 08 | mixed low critical5 | 373 | 17 | 356 | 390 | 510 | 154 | (8,9) |
| 00 | internal A only | 382 | 18 | 364 | 420 | 577 | 213 | (9,9) |
| 01 | internal B only | 392 | 22 | 370 | 414 | 538 | 168 | (11,11) |
| 07 | mixed balanced coverage | 404 | 13 | 391 | 454 | 599 | 208 | (8,5) |
| 06 | cross 45 only | 424 | 19 | 405 | 426 | 590 | 185 | (9,10) |
| 09 | mixed endpoint separation | 425 | 30 | 395 | 452 | 587 | 192 | (18,12) |
| 05 | cross 186 only | 439 | 21 | 418 | 468 | 602 | 184 | (11,10) |
| 04 | cross 1338 only | 464 | 22 | 442 | 522 | 642 | 200 | (11,11) |
| 03 | cross 412 only | 512 | 22 | 490 | 540 | 808 | 318 | (11,11) |

For all ten candidates, each new root's actual missing count equals the count predicted from the original-graph coverage upper bound. Deleting the chosen matching did not create additional new-root failures in these particular candidates. Nevertheless, neither new root pair achieved complete coverage. More substantially, the extension repaired only part of the old–old damage, leaving 350–490 old bad pairs per candidate. The policy with the fewest new–old failures, candidate 07, does not minimize total failures.

The best candidate 02 deletes the following oriented matching and attaches each first endpoint to `u`, each second endpoint to `v`:

```
(0,1405), (1856,451), (395,1800),
(1946,541), (1746,341), (2459,1054).
```

Its two new-root distance histograms at distances 0 through 6 are

```
u: [1,7,42,242,1120,1391,9]
v: [1,7,42,243,1127,1387,5].
```

All ten full edge sets are retained. No partial graph or root-only score was treated as a successful construction.

## What this profile establishes

The extension operation is mathematically valid and inexpensive to construct and verify. These ten instances fail mainly because removing six old edges creates old–old distance defects that the new shortcuts do not fully repair. Improving only prospective new-root coverage is therefore insufficient for these examples. A justified continuation would need to account jointly for actual matching-deletion damage and the exact endpoint repair conditions. The profile neither excludes all six-matchings nor establishes that a successful one exists. No such continuation was run in this batch.

Baseline preprocessing took **0.648619 CPU seconds**, deterministic candidate generation **2.325415 CPU seconds**, and the independent ten-candidate checks **4.36956 CPU seconds**: approximately **7.344 CPU seconds** in total. The independent checks included full 2812-root BFS, exact edge-set differences, full old-root BFS in `H`, and the stated pairwise formula comparisons. Compilation is not included in these computation times.

## Files

All batch files are under `research/ddp/m1_matching_augmentation/`:

- `preprocess.cpp`, `preprocess`: original distances and exact `critical5` data; outputs `baseline.distances.u8`, `baseline.edge_critical5.txt`, and `baseline.preprocess.json`.
- `generate_ten.py`, `policies.json`, `generation.json`: the fixed candidate rules and their actual outputs.
- `candidate_00.edges` through `candidate_09.edges`: every complete 2812-vertex graph. Each corresponding `.parameters.json` records all six oriented edges and the greedy decisions.
- `independent_check_batch.cpp`, `independent_check_batch`, `independent_validation.json`, `INDEPENDENT_CHECK_REPORT.md`: the independently implemented full graph and distance checks.
- `ranked_results.json`: the result table in total-bad-pair order.

The source graph was not modified. No running process or follow-on queue remains.
