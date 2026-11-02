# Joint path-repair search for the six-matching extension

The joint objective improved the best complete 2812-vertex graph from 364 bad unordered pairs to **331**, but the graph still has diameter 6. No degree-7, diameter-5 new bound was obtained. The single predetermined profile has ended; no additional seed was started.

## What actually changed

The earlier ten candidates mainly selected endpoints for new-root coverage. Their remaining old–old distance damage was much larger than their new-root deficit. This profile explicitly charged for unrepaired old pairs that must become farther than five when any selected edge is removed.

For every source edge e, the complete set `D_e` consists of all unordered pairs with distance greater than five in `G−e`. It is computed by intersecting edge sets across every walk of length at most five, using five frozen dynamic-programming layers. The complete table has 996145 edge/pair incidences. Seven source edge-orbit representatives were independently checked by all-source BFS after deleting the edge, with exact pair-set agreement. Earlier distance-5-only lists remain preserved; they omitted actual damage to originally shorter pairs.

For a matching M, its single-edge damage union `D=union D_e` is contained in the damage caused by deleting all of M. Duplicate pairs are counted only once. The objective charges every pair in D that the new hubs cannot repair, plus both new-root failures. Independent Python and the C++ scorer agree on all ten old candidates. The complete-damage objective gives `[382,392,363,510,464,437,424,403,373,425]`, versus actual `[382,392,364,512,464,439,424,404,373,425]`.

## A useful exact simplification

Let A and B be the endpoints assigned to u and v, with each original matching edge pairing one member of each, and retain the new edge uv. Write `a(x)=d_G(x,A)` and `b(x)=d_G(x,B)`. Then

```
d_F(x,u)=a(x)+1,  d_F(x,v)=b(x)+1,
d_F(x,y)=min(d_(G−M)(x,y), a(x)+a(y)+2, b(x)+b(y)+2).
```

These use distances in the original source graph, and they are exact for this operation. A shortest G path to A cannot meet A before its endpoint. If it uses a deleted matching edge, that edge can only be its final step `b_i→a_i`; replacing the final two-step segment `b_i–a_i–u` by `b_i–v–u` preserves length. The lower bound follows from the general deleted-graph formula and `|a(x)−b(x)|≤1`. The old-pair formula follows by considering whether a shortest path visits either hub; concatenations of shortest segments give the reverse inequality. The independent derivation is in `LOWER_BOUND_CHECK.md` and `REPAIR_GEOMETRY.md`.

Thus the original description of these endpoint distances as merely optimistic was unnecessarily weak. The cross terms in the initial four-inequality implementation are redundant, so the simplification does not change any score or require a search restart. The objective's sole possible omission is **joint deletion damage**: a pair spoiled by several selected edges together, but by none of them alone. A zero score still needs a full graph check.

## Actual profile and complete validation

The [plan](PLAN.md) fixed one CPU, one seed, and 120 CPU seconds. Proposals included matching-edge replacements directed by the small-ball repair condition in `REPAIR_GEOMETRY.md`, along with orientation, endpoint-preserving, arbitrary-edge, and paired changes. A proposal aimed at one defect was still scored against all new damage.

The run ended normally with `BUDGET_EXHAUSTED`: 4542736 proposals, 886971 accepted, 210656 illegal proposals rejected, and 120.078 child CPU seconds including setup. Calibration recorded 230 positive deltas, median 36, giving initial temperature 22.3681. No zero-score candidate was found.

|Saved graph|Scoring lower bound|Actual old–old bad pairs|Actual new–old bad pairs|Actual total|Diameter|
|---|---:|---:|---:|---:|---:|
|Best|330|295|36|331|6|
|Final|339|297|42|339|6|

Both complete edge lists independently have 2812 vertices, 9842 edges, degree exactly seven, no loops or duplicates, and are connected. The best matching destroys 554 old-pair five-step connections; the new hubs repair 259, leaving 295. Its two new-root deficits are 15 and 21. Every old/new distance agreed with the independent deleted-graph distance formulas. The independent validation took 0.828 CPU seconds; see [the full report](PROFILE_INDEPENDENT_REPORT.md).

## Consequence

The revised objective captures almost all observed distance failures and did improve the full graph. It still leaves hundreds of bad pairs, so this profile supplies no reason to append an unchanged random trajectory. It also does not exclude all six-matchings or other augmentations.

A separate concrete construction change uses the actual maximum-degree requirement: a new vertex may have degree below the maximum. For the verified 650-vertex five-regular source, deleting two disjoint edges and joining their four endpoints to one new vertex gives a 651-vertex graph of maximum degree five. That fixed-source family is being checked completely in `../matching_single_vertex650/`; its status and results are separate from this finished profile.

Full best/final edge lists and matching parameters, score regressions, critical-pair tables and independent checks, calibration, log, process termination, and complete verification are saved in this directory. These are discovery and computational evidence, not a new lower bound or a Lean theorem.
