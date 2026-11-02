---
type: experiment
node_id: exp:ddp-h3-364-two-root-port-barrier-20261027
title: "自然H3两新根：互助仅盖6/28端口，均匀排除"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/two_root/REPORT.md; research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/two_root/RESULT.json"
added: 2026-10-27T17:10:44Z
tags: ["ddp", "method-ledger"]
---

# 自然H3两新根：互助仅盖6/28端口，均匀排除

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (4,5)；L=364；条件性n=366（未据此计纪录）

**距目标的证据：** 相邻新根各接3个不同旧ports，R4(A)∪R3(B)在port集仅A∪B，必漏22；3767400对全部由同一障碍排除，实际枚举/编译/BFS均0。假设族D恰6，无实际新图。

**其他指标（保持原计数类型）：**
```json
{
  "unordered_pairs_excluded": 3767400,
  "pairs_evaluated": 0,
  "missing_ports_per_root": 22,
  "CPU_seconds": 0.001109331
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/two_root/REPORT.md](../../research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/two_root/REPORT.md)；[research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/two_root/RESULT.json](../../research/ddp/more_graphs_20261027/d4_D5_polarity_extensions/two_root/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 相邻新根各接3个不同旧ports，R4(A)∪R3(B)在port集仅A∪B，必漏22；3767400对全部由同一障碍排除，实际枚举/编译/BFS均0。假设族D恰6，无实际新图。

**仍未完成：** Complete new graph and final Lean remain required; finite scope is not the general graph problem.

**启发与重启依据：** 双新点互助不能越过旧port间距；停止小根组合枚举，改整体helper必要结构研究。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

