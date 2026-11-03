---
type: experiment
node_id: exp:ddp-wave8-cooperative-extension-scout
title: "两相邻新点合作扩张：来源准备未执行"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave8/cooperative_extension_scout/REPORT.md; research/ddp/breadth_20261027_wave8/cooperative_extension_scout/SCOUT.json; research/ddp/breadth_20261027_wave8/cooperative_extension_scout/source37628_profile.json; research/ddp/breadth_20261027_wave8/cooperative_extension_scout/source42342_profile.json; research/ddp/breadth_20261027_wave8/cooperative_extension_scout/terminal.json"
added: 2026-10-27T07:55:18Z
tags: ["ddp", "method-ledger"]
---

# 两相邻新点合作扩张：来源准备未执行

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (?,5)；L=不适用／见变体；多目标：[{'Delta': 12, 'D': 5, 'savedL': 42342, 'hypothetical_n': 42344, 'pin_cap_each': 11}, {'Delta': 11, 'D': 5, 'savedL': 37628, 'hypothetical_n': 37630, 'pin_cap_each': 10}]

**距目标的证据：** 尚无新profile/MILP/图；全局可行性UNKNOWN，不能登记实际失败。

**其他指标（保持原计数类型）：**
```json
{
  "new_profile_executed": false,
  "targets": [
    {
      "Delta": 12,
      "D": 5,
      "savedL": 42342,
      "hypothetical_n": 42344,
      "pin_cap_each": 11
    },
    {
      "Delta": 11,
      "D": 5,
      "savedL": 37628,
      "hypothetical_n": 37630,
      "pin_cap_each": 10
    }
  ]
}
```





**原始证据：** [research/ddp/breadth_20261027_wave8/cooperative_extension_scout/REPORT.md](../../research/ddp/breadth_20261027_wave8/cooperative_extension_scout/REPORT.md)；[research/ddp/breadth_20261027_wave8/cooperative_extension_scout/SCOUT.json](../../research/ddp/breadth_20261027_wave8/cooperative_extension_scout/SCOUT.json)；[research/ddp/breadth_20261027_wave8/cooperative_extension_scout/source37628_profile.json](../../research/ddp/breadth_20261027_wave8/cooperative_extension_scout/source37628_profile.json)；[research/ddp/breadth_20261027_wave8/cooperative_extension_scout/source42342_profile.json](../../research/ddp/breadth_20261027_wave8/cooperative_extension_scout/source42342_profile.json)；[research/ddp/breadth_20261027_wave8/cooperative_extension_scout/terminal.json](../../research/ddp/breadth_20261027_wave8/cooperative_extension_scout/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 保留旧边、添加a-b、各连至多Delta-1个oldpins；仅恢复完整条件与来源

**正向保证：** old-old距离保持；完整条件R4(A)∪R3(B)=V及对称式；全部spare点R4并集覆盖两源

**仍未完成：** 有限小pin集合是否同时覆盖未知；旧37628全局单点MILP是UNKNOWN不是UNSAT。

**启发与重启依据：** 另行授权有限双新点profile，不能把旧8起点误说8邻居预算。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

