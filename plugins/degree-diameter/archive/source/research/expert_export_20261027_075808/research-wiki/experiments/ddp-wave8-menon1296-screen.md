---
type: experiment
node_id: exp:ddp-wave8-menon1296-screen
title: "Menon16/6/2×K9：方向类保留模板必要筛"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave8/menon1296_screen/REPORT.md; research/ddp/breadth_20261027_wave8/menon1296_screen/RESULT.json; research/ddp/breadth_20261027_wave8/menon1296_screen/design_and_groups.json; research/ddp/breadth_20261027_wave8/menon1296_screen/screen.py"
added: 2026-10-27T07:55:18Z
tags: ["ddp", "method-ledger"]
---

# Menon16/6/2×K9：方向类保留模板必要筛

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** capacity

**目标与阶数：** (8,4)；L=1100；条件性n=1296（未据此计纪录）

**距目标的证据：** 块外point、不同方向类的B-C必dist≥5；整个指定模板排除D4。

**其他指标（保持原计数类型）：**
```json
{
  "ordinary_bad_unordered_lower_bound": 155520,
  "ordered_bad_BC_and_CB_lower_bound": 311040,
  "proven_D_lower_bound": 5,
  "graphs_generated": 0,
  "a_CSP_run": false
}
```





**原始证据：** [research/ddp/breadth_20261027_wave8/menon1296_screen/REPORT.md](../../research/ddp/breadth_20261027_wave8/menon1296_screen/REPORT.md)；[research/ddp/breadth_20261027_wave8/menon1296_screen/RESULT.json](../../research/ddp/breadth_20261027_wave8/menon1296_screen/RESULT.json)；[research/ddp/breadth_20261027_wave8/menon1296_screen/design_and_groups.json](../../research/ddp/breadth_20261027_wave8/menon1296_screen/design_and_groups.json)；[research/ddp/breadth_20261027_wave8/menon1296_screen/screen.py](../../research/ddp/breadth_20261027_wave8/menon1296_screen/screen.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定Menon/K9/B三角形，所有保留四方向类的incidence置换，含每类内任意S9

**正向保证：** simple8regular connected；samepoint A-C≤3,C-C≤4；12个AG匹配组正确

**仍未完成：** 一般S36混类π不受此障碍；一般三色CSP未解且不需要求。

**启发与重启依据：** 必须混合方向类；已由一般S36profile跟进，不开a CSP。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

