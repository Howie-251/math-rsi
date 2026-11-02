---
type: experiment
node_id: exp:ddp-h3-helper13-tree-class-exclusion-20261027
title: "(4,5)13helpers整体树形方案：全部拓扑归约后排除"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/helper13_tree_probe/REPORT.md; research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/helper13_tree_probe/RESULT.json; research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/helper13_tree_probe/terminal.json"
added: 2026-10-27T17:26:52Z
tags: ["ddp", "method-ledger"]
---

# (4,5)13helpers整体树形方案：全部拓扑归约后排除

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** positive-local-obstruction

**目标与阶数：** (4,5)；L=364；条件性n=377（未据此计纪录）

**距目标的证据：** k13强制H为diam≤4的degree≤4tree、全部28ports使用。3276个leaftriples的good(T)全0先排333及含3-leafbranch拓扑；余唯一2222拓扑的81900个(T,parentport)也全部good0<18。因此固定364/714host保边且不加old-old边的13helper类全排；必要helpers现至少14。

**其他指标（保持原计数类型）：**
```json
{
  "stage1_triples": 3276,
  "stage1_maximum_good_count": 0,
  "stage1_existence_prediction": "REFUTED",
  "stage2_pairs": 81900,
  "stage2_maximum_good_count": 0,
  "stage2_obstruction_prediction": "SUPPORTED",
  "stage1_CPU_seconds": 0.0188914,
  "stage2_CPU_seconds": 0.299655898,
  "minimum_helpers": 14,
  "BFS": 0,
  "new_graphs": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/helper13_tree_probe/REPORT.md](../../research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/helper13_tree_probe/REPORT.md)；[research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/helper13_tree_probe/RESULT.json](../../research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/helper13_tree_probe/RESULT.json)；[research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/helper13_tree_probe/terminal.json](../../research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/helper13_tree_probe/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** k13强制H为diam≤4的degree≤4tree、全部28ports使用。3276个leaftriples的good(T)全0先排333及含3-leafbranch拓扑；余唯一2222拓扑的81900个(T,parentport)也全部good0<18。因此固定364/714host保边且不加old-old边的13helper类全排；必要helpers现至少14。

**仍未完成：** No new complete graph in this probe; other parameters and mechanisms remain open.

**启发与重启依据：** 原存在预测被反驳、后maxgood<18障碍预测被支持，二者不混作构造成功。停止该host的helper逐阶长尾；k14未查，任意377图/其它host不受此结论。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

