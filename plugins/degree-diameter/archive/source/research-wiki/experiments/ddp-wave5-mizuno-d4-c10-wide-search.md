---
type: experiment
node_id: exp:ddp-wave5-mizuno-d4-c10-wide-search
title: "8base×C10九自由电压宽证书试验"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/REPORT.md; research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/best80.edges; research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/best80.independent_check.json; research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/best80.labels.json; research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/best_scoring_missing_slots.json; research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/first80.distance_check.json; research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/input.txt; research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/run.py; research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/search.cpp; research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/search_result.json; research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/starts.json; research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/terminal.json"
added: 2026-10-27T08:25:52Z
tags: ["ddp", "method-ledger"]
---

# 8base×C10九自由电压宽证书试验

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** controller

**目标与阶数：** (12,4)；L=5832；controller n=80；条件性n=6480（未据此计纪录）

**距目标的证据：** 实际D=5，目标D=4；普通无序坏对=20；saved_controller_only;hypothetical_lift_not_generated；最佳80控制图D5、20个>4无序对；wide还缺160有序对。

**其他指标（保持原计数类型）：**
```json
{
  "wide_missing_representative_targets": 16,
  "wide_missing_ordered_controller_pairs": 160,
  "ordinary_scope": "80controller only;6480 lift not generated",
  "proposals": 200000
}
```





**原始证据：** [research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/REPORT.md](../../research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/REPORT.md)；[research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/best80.edges](../../research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/best80.edges)；[research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/best80.independent_check.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/best80.independent_check.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/best80.labels.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/best80.labels.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/best_scoring_missing_slots.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/best_scoring_missing_slots.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/first80.distance_check.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/first80.distance_check.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/input.txt](../../research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/input.txt)；[research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/run.py](../../research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/run.py)；[research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/search.cpp](../../research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/search.cpp)；[research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/search_result.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/search_result.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/starts.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/starts.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/terminal.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_C10_wide_search/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 8个固定starts×25000电压提案；只此九自由父族有限批次

**正向保证：** I/R2/100RG4为原chart可复用充分条件；控制图simple quartic connected

**仍未完成：** 宽证书未闭；最佳控制图D5更给投影提升D≥5真实阻断。

**启发与重启依据：** 该父profile停止；只有改变真实结构/覆盖条件才值得重启，不追加seed/sheet/base。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

