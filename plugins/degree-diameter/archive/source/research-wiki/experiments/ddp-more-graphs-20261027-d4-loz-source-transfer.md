---
type: experiment
node_id: exp:ddp-more-graphs-20261027-d4-loz-source-transfer
title: "Loz1100固定整数迁移：primitive61八根与四CRTlift均失败"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d4_source_transfer/REPORT.md; research/ddp/more_graphs_20261027/d4_source_transfer/RESULT.json; research/ddp/more_graphs_20261027/d4_source_transfer/SOURCE.json; research/ddp/more_graphs_20261027/d4_source_transfer/PREDICTION.json; research/ddp/more_graphs_20261027/d4_source_transfer/check.py"
added: 2026-10-27T14:08:25Z
tags: ["ddp", "method-ledger"]
---

# Loz1100固定整数迁移：primitive61八根与四CRTlift均失败

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (8,4)；L=1100；条件性n=1220（未据此计纪录）；从属目标：[[8, 4]]

**距目标的证据：** No graphgenerated;identityroot20phase endpointcoverage,notwholegraphbadpairs.；形式min72容61，固定primitive8与CRT4仍均失败，0新图/旧源重验。

**其他指标（保持原计数类型）：**
```json
{
  "fixed_cases": 12,
  "new_graphs": 0,
  "old_source_BFS": 0,
  "CPU_seconds": 0.066323808,
  "pending": []
}
```



**从属变体：**
```json
[
  {
    "label": "m61r8",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "identityroot_missing_within4": 289,
    "graph_generated": false,
    "scope": "Fixedintegerrule only,notfreetranslations."
  },
  {
    "label": "m61r23",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "identityroot_missing_within4": 127,
    "graph_generated": false,
    "scope": "Fixedintegerrule only,notfreetranslations."
  },
  {
    "label": "m61r24",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "identityroot_missing_within4": 110,
    "graph_generated": false,
    "scope": "Fixedintegerrule only,notfreetranslations."
  },
  {
    "label": "m61r28",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "identityroot_missing_within4": 201,
    "graph_generated": false,
    "scope": "Fixedintegerrule only,notfreetranslations."
  },
  {
    "label": "m61r33",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "identityroot_missing_within4": 98,
    "graph_generated": false,
    "scope": "Fixedintegerrule only,notfreetranslations."
  },
  {
    "label": "m61r37",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "identityroot_missing_within4": 82,
    "graph_generated": false,
    "scope": "Fixedintegerrule only,notfreetranslations."
  },
  {
    "label": "m61r38",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "identityroot_missing_within4": 298,
    "graph_generated": false,
    "scope": "Fixedintegerrule only,notfreetranslations."
  },
  {
    "label": "m61r53",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "identityroot_missing_within4": 86,
    "graph_generated": false,
    "scope": "Fixedintegerrule only,notfreetranslations."
  },
  {
    "label": "m75r2",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1500
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "identityroot_missing_within4": 229,
    "graph_generated": false,
    "scope": "Fixedintegerrule only,notfreetranslations."
  },
  {
    "label": "m93r2",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1860
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "identityroot_missing_within4": 380,
    "graph_generated": false,
    "scope": "Fixedintegerrule only,notfreetranslations."
  },
  {
    "label": "m123r2",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 2460
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "identityroot_missing_within4": 601,
    "graph_generated": false,
    "scope": "Fixedintegerrule only,notfreetranslations."
  },
  {
    "label": "m155r2",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 3100
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "identityroot_missing_within4": 974,
    "graph_generated": false,
    "scope": "Fixedintegerrule only,notfreetranslations."
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/d4_source_transfer/REPORT.md](../../research/ddp/more_graphs_20261027/d4_source_transfer/REPORT.md)；[research/ddp/more_graphs_20261027/d4_source_transfer/RESULT.json](../../research/ddp/more_graphs_20261027/d4_source_transfer/RESULT.json)；[research/ddp/more_graphs_20261027/d4_source_transfer/SOURCE.json](../../research/ddp/more_graphs_20261027/d4_source_transfer/SOURCE.json)；[research/ddp/more_graphs_20261027/d4_source_transfer/PREDICTION.json](../../research/ddp/more_graphs_20261027/d4_source_transfer/PREDICTION.json)；[research/ddp/more_graphs_20261027/d4_source_transfer/check.py](../../research/ddp/more_graphs_20261027/d4_source_transfer/check.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** A0,B=r10-1,C1,D=1+r+r4,fixedphases1/12/11/16;primitivep61all8rootsandliteralr2all4m75/93/123/155. Freeparameterfollowupsseparate.

**仍未完成：** FreeCRTtranslations,otherfields/phasepatterns open;prime61freestudyseparate.

**启发与重启依据：** 源CRT不能套primitivePhi20关系；固定lift停止，不追加offset/prime。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

