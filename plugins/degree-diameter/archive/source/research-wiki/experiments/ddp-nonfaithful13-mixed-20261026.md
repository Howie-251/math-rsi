---
type: experiment
node_id: exp:ddp-nonfaithful13-mixed-20261026
title: "F13半直积C28反射mixed族完整有限检查"
idea_id: "idea:ddp-m1-two-orbit-voltage"
verdict: no
confidence: high
date: "2026-10-26"
hardware: "one CPU"
duration: "1.6695 CPU s search; full BFS 0.0106 s"
provenance: "research/ddp/m1_reflection_nonfaithful/REPORT.md; research/ddp/m1_reflection_nonfaithful/p13_mixed_search/complete_mixed.summary.json; research/ddp/m1_reflection_nonfaithful/p13_mixed_search/best.independent_verify.json"
added: 2026-10-27T08:25:50Z
tags: ["ddp", "no-new-bound", "method-ledger"]
---

# F13半直积C28反射mixed族完整有限检查

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-m1-two-orbit-voltage`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (5,5)；L=650；candidate_graph_or_family n=728

**距目标的证据：** 实际D=6，目标D=5；原报告bad（类型见详情）=5278；Existing Wiki Metrics; no experiment rerun；48 skeletons,105456 assignments,all legal and scored; minimum representative misses29. Best full728vertex1820edge graph is simple connected5regular,D6,5278badpairs.；后续结果优先：research-wiki/experiments/ddp-nonfaithful-remaining-20261026.md；Later existing note completes p17/p29 mixed/both branches; the earlier unexecuted statement is historical.

**其他指标（保持原计数类型）：**
```json
{
  "superseding_existing_wiki": [
    {
      "path": "research-wiki/experiments/ddp-nonfaithful-remaining-20261026.md",
      "note": "Later existing note completes p17/p29 mixed/both branches; the earlier unexecuted statement is historical."
    }
  ]
}
```

**既有原文指标：** 48 skeletons,105456 assignments,all legal and scored; minimum representative misses29. Best full728vertex1820edge graph is simple connected5regular,D6,5278badpairs.



**原始证据：** [research/ddp/m1_reflection_nonfaithful/REPORT.md](../../research/ddp/m1_reflection_nonfaithful/REPORT.md)；[research/ddp/m1_reflection_nonfaithful/p13_mixed_search/complete_mixed.summary.json](../../research/ddp/m1_reflection_nonfaithful/p13_mixed_search/complete_mixed.summary.json)；[research/ddp/m1_reflection_nonfaithful/p13_mixed_search/best.independent_verify.json](../../research/ddp/m1_reflection_nonfaithful/p13_mixed_search/best.independent_verify.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Capacity-preserving normalization and compatible units come from the complete three-group diagnosis. No extra projective normalization or mixed side swap. Only this p13 mixed finite branch was searched; p17/p29 remain unexecuted.

**启发与重启依据：** Capacity-preserving normalization and compatible units come from the complete three-group diagnosis. No extra projective normalization or mixed side swap. Only this p13 mixed finite branch was searched; p17/p29 remain unexecuted.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

