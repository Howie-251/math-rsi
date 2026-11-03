---
type: experiment
node_id: exp:dd82-global-matchings58-prefix-capacity-20261018
title: "整数修复容量界排除首批全部8个第六轮前缀"
idea_id: "idea:dd82-global-matchings58"
verdict: partial
confidence: high
date: "2026-10-18"
hardware: "Read saved graph prefixes, exact integer arithmetic, no solver"
duration: "Original capacity0.140762CPU s; repeat augmentation0.135944CPU s; final2potential witnesses0.018763CPU s"
provenance: "computations/dd82/construction/global_matchings58_run/prefix_capacity/{PREFIX_CAPACITY.md,prefix_capacity.json,degree_capacity.json}"
added: 2026-10-18T08:06:32Z
tags: ["dd82", "construction", "capacity", "fixed-prefix", "failure-analysis"]
---

# 整数修复容量界排除首批全部8个第六轮前缀

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:dd82-global-matchings58`

## Metrics
56savedprefixes scanned; top-d excludes6F6 andall8F7; monotone walkrepetition excludesall8F7. Integerpotential bounds additionallyseed0F6:645bad>644repair,seed3F6:639>638. All8savedF6 impossible.

## Reasoning
Every oldbadpair is repaired by one-new-edge coverage or a two-new-edge path. The latter has atmost58*C(d,2)centered endpointpairs. Degree-incidence top-d sums and arbitraryintegervertexpotentials bound the former. Full elementary proofs and integerwitnesses are saved; root independently recomputed the two closing witnesses by adjacencysets. This excludes every monotonecompletion of those actualF6, including odd-cycle2factors, not arbitrary58graphs or allmatchingseeds. F6completion was therefore not prepared/solved; nextconditional experiment frees all decisions after savedseed3F5. Same-thread round2 actually returned and accepted the exact regular-prefix inequalities and actual fixed-prefix exclusions; no extension to arbitrary irregularprefixes. [Proof and exactwitnesses](../../computations/dd82/construction/global_matchings58_run/prefix_capacity/PREFIX_CAPACITY.md).

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

