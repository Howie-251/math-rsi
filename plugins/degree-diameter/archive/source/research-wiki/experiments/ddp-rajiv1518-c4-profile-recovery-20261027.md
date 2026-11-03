---
type: experiment
node_id: exp:ddp-rajiv1518-c4-profile-recovery-20261027
title: "Rajiv1518真实C4稳定子、4+1+1邻接与C6因子恢复"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d6_psl23_coset_transfer/source_recovery/REPORT.md; research/ddp/more_graphs_20261027/d6_psl23_coset_transfer/source_recovery/RESULT.json; research/ddp/more_graphs_20261027/d6_psl23_coset_transfer/source_recovery/root_stabilizer.json; research/ddp/more_graphs_20261027/d6_psl23_coset_transfer/source_recovery/source_relations.json"
added: 2026-10-27T16:02:07Z
tags: ["ddp", "method-ledger"]
---

# Rajiv1518真实C4稳定子、4+1+1邻接与C6因子恢复

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (6,5)；L=1518；known_source_or_recovery n=1518；条件性n=1950（未据此计纪录）

**距目标的证据：** 实际D=5，目标D=5；Inheritedknown1518source; targetedsourceautomorphisms only, no repeated BFS.；从实际边表的根配色及邻接精确automorphisms恢复order4稳定子与三个involutive连接生成元；profile4+1+1，normalizer24/rootC6。q25/C4得到1950点规则、78候选、C6容量4602但未据容量声称成功。源recipe与2×2matrix编号绑定仍未恢复。

**其他指标（保持原计数类型）：**
```json
{
  "stabilizer": "C4",
  "neighbor_suborbits": [
    4,
    1,
    1
  ],
  "normalizer_order": 24,
  "source_root_C6": [
    0,
    967,
    1306,
    1294,
    1087,
    981
  ],
  "q25_candidate_count": 78,
  "q25_tested_by_this_node": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d6_psl23_coset_transfer/source_recovery/REPORT.md](../../research/ddp/more_graphs_20261027/d6_psl23_coset_transfer/source_recovery/REPORT.md)；[research/ddp/more_graphs_20261027/d6_psl23_coset_transfer/source_recovery/RESULT.json](../../research/ddp/more_graphs_20261027/d6_psl23_coset_transfer/source_recovery/RESULT.json)；[research/ddp/more_graphs_20261027/d6_psl23_coset_transfer/source_recovery/root_stabilizer.json](../../research/ddp/more_graphs_20261027/d6_psl23_coset_transfer/source_recovery/root_stabilizer.json)；[research/ddp/more_graphs_20261027/d6_psl23_coset_transfer/source_recovery/source_relations.json](../../research/ddp/more_graphs_20261027/d6_psl23_coset_transfer/source_recovery/source_relations.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Literal1518publicsource andsourcepermutationrelations; q25/C4profilearithmeticonly. No sourceBFS, no newparametergraph scan byrecoveryagent.

**仍未完成：** 本轮没有产生新的验收通过纪录；一般图及未明示范围仍开放，Lean完整实例0。

**启发与重启依据：** 保留C6 factor+involutoryvalence4是有依据迁移；q29无C4不能原规则移植；不把未绑定矩阵冒称原作者matrixgenerators。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

