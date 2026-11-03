---
type: experiment
node_id: exp:ddp-h9-d13-raw-gauge-obstruction-20261027
title: "(13,5)旧raw映射恢复失败：pairflip不改变边块大小"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d13_D5_h9_transfer/raw_map_recovery/REPORT.md"
added: 2026-10-27T17:10:44Z
tags: ["ddp", "method-ledger"]
---

# (13,5)旧raw映射恢复失败：pairflip不改变边块大小

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** positive-local-obstruction

**目标与阶数：** (13,5)；L=51417

**距目标的证据：** 完整166425个F边块比较：1345个旧4→当前2、1345个旧2→当前4；另8个同计数matching变化。最短反例Fedge26—15837从K2,2变matching，因此任何类内pairflip都不能恢复旧raw同态。

**其他指标（保持原计数类型）：**
```json
{
  "blocks_checked": 166425,
  "complete_to_matching": 1345,
  "matching_to_complete": 1345,
  "matching_parity_changed": 8
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d13_D5_h9_transfer/raw_map_recovery/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/raw_map_recovery/REPORT.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Class-preserving pairflip gauge of the fixed oldcore onto the actual51417 currentcore only.

**仍未完成：** Complete new graph and final Lean remain required; finite scope is not the general graph problem.

**启发与重启依据：** 明确停止虚构旧raw orientation。whole-class closure仍可用已证F短路lift保证core覆盖，属于不同规则；不排任意重标或其它raw实现。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

