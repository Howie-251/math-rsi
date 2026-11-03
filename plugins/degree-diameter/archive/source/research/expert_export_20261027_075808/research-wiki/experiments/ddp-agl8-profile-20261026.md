---
type: experiment
node_id: exp:ddp-agl8-profile-20261026
title: "非正规AGL8八度塔：2000样本未通过BB"
idea_id: "idea:ddp-m2-hierarchical-cover"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "OneCPUworker; one independent8320-root preflight check"
duration: "2.156896 CPU seconds prep/profile plus one independent preflight"
provenance: "research/ddp/m2_coset_tower/d8_binary_agl8/STRUCTURE_SCOPE.md; research/ddp/m2_coset_tower/d8_binary_agl8/REPORT.md; research/ddp/m2_coset_tower/d8_binary_agl8/terminal.json; research/ddp/m2_coset_tower/d8_binary_agl8/preflight.independent_check.json"
added: 2026-10-27T07:55:14Z
tags: ["ddp", "profile", "nonnormal-H", "method-ledger"]
---

# 非正规AGL8八度塔：2000样本未通过BB

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-m2-hierarchical-cover`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (8,5)；L=5334；candidate_graph_or_family n=8320；从属目标：[[8, 5]]

**距目标的证据：** 2000 legalHH actualthree-root samples,0BBpass,minBB21;best scored1802752badpairs. Onlypreflight independently fullroot D6,bad6515712;all1024BB targets matchnewtwo-mask formula.



**既有原文指标：** 2000 legalHH actualthree-root samples,0BBpass,minBB21;best scored1802752badpairs. Onlypreflight independently fullroot D6,bad6515712;all1024BB targets matchnewtwo-mask formula.

**从属变体：**
```json
[
  {
    "label": "best production-scored sample",
    "n": 8320,
    "actualD": null,
    "bad_pairs": 1802752,
    "count_type": "reported_bad_pairs_type_not_explicit",
    "verification": "not independently final-checked in this note",
    "target": [
      8,
      5
    ],
    "savedL": 5334,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": null
  },
  {
    "label": "independently checked preflight",
    "n": 8320,
    "actualD": 6,
    "bad_pairs": 6515712,
    "count_type": "reported_bad_pairs_type_not_explicit",
    "verification": "full-root BFS explicitly stated",
    "target": [
      8,
      5
    ],
    "savedL": 5334,
    "savedL_source": "context/DD_PORTFOLIO_START_20261026/registry/cases.json",
    "distance_gap": 1
  }
]
```

**原始证据：** [research/ddp/m2_coset_tower/d8_binary_agl8/STRUCTURE_SCOPE.md](../../research/ddp/m2_coset_tower/d8_binary_agl8/STRUCTURE_SCOPE.md)；[research/ddp/m2_coset_tower/d8_binary_agl8/REPORT.md](../../research/ddp/m2_coset_tower/d8_binary_agl8/REPORT.md)；[research/ddp/m2_coset_tower/d8_binary_agl8/terminal.json](../../research/ddp/m2_coset_tower/d8_binary_agl8/terminal.json)；[research/ddp/m2_coset_tower/d8_binary_agl8/preflight.independent_check.json](../../research/ddp/m2_coset_tower/d8_binary_agl8/preflight.independent_check.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Profile only; huge full family remainsopen and is paused. This does not close other assignments or compositions.

**启发与重启依据：** Profile only; huge full family remainsopen and is paused. This does not close other assignments or compositions.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

