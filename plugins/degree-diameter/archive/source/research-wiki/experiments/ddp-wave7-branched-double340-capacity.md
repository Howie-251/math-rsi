---
type: experiment
node_id: exp:ddp-wave7-branched-double340-capacity
title: "signed double的matching K2,2分支跟进"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave7/branched_double340_capacity/REPORT.md; research/ddp/breadth_20261027_wave7/branched_double340_capacity/RESULT.json; research/ddp/breadth_20261027_wave7/branched_double340_capacity/certificate.independent_check.json; research/ddp/breadth_20261027_wave7/branched_double340_capacity/check_weights.py; research/ddp/breadth_20261027_wave7/branched_double340_capacity/terminal.json"
added: 2026-10-27T08:25:53Z
tags: ["ddp", "method-ledger"]
---

# signed double的matching K2,2分支跟进

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** capacity

**目标与阶数：** (8,3)；L=253；条件性n=340（未据此计纪录）

**距目标的证据：** 必须击中5130条必需唯一路；任意matching权重≤2810，统一排除。

**其他指标（保持原计数类型）：**
```json
{
  "required_unique_paths": 5130,
  "matching_hit_upper_bound": 2810,
  "ordinary_bad_unordered_lower_bound": 4640,
  "graphs_generated": 0
}
```





**原始证据：** [research/ddp/breadth_20261027_wave7/branched_double340_capacity/REPORT.md](../../research/ddp/breadth_20261027_wave7/branched_double340_capacity/REPORT.md)；[research/ddp/breadth_20261027_wave7/branched_double340_capacity/RESULT.json](../../research/ddp/breadth_20261027_wave7/branched_double340_capacity/RESULT.json)；[research/ddp/breadth_20261027_wave7/branched_double340_capacity/certificate.independent_check.json](../../research/ddp/breadth_20261027_wave7/branched_double340_capacity/certificate.independent_check.json)；[research/ddp/breadth_20261027_wave7/branched_double340_capacity/check_weights.py](../../research/ddp/breadth_20261027_wave7/branched_double340_capacity/check_weights.py)；[research/ddp/breadth_20261027_wave7/branched_double340_capacity/terminal.json](../../research/ddp/breadth_20261027_wave7/branched_double340_capacity/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定170源、branch baseedges构成matching、未覆盖点加vertical、全部signings

**正向保证：** degree始终8；整数对偶证书不依赖唯一路枚举完备性

**仍未完成：** 不排其他branch集合/度预算或base。

**启发与重启依据：** 只有改变matching分支模板才能重启；不能搜matching或sign。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

