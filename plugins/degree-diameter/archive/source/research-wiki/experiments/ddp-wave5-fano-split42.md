---
type: experiment
node_id: exp:ddp-wave5-fano-split42
title: "Fano独立集拆点42固定完整族"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave5/fano_split42/REPORT.md; research/ddp/breadth_20261027_wave5/fano_split42/RESULT.json; research/ddp/breadth_20261027_wave5/fano_split42/best.edges; research/ddp/breadth_20261027_wave5/fano_split42/best.independent_check.json; research/ddp/breadth_20261027_wave5/fano_split42/best_bad_pairs.json; research/ddp/breadth_20261027_wave5/fano_split42/best_parameters.json; research/ddp/breadth_20261027_wave5/fano_split42/build_metrics.json; research/ddp/breadth_20261027_wave5/fano_split42/execution_metrics.json; research/ddp/breadth_20261027_wave5/fano_split42/input.txt; research/ddp/breadth_20261027_wave5/fano_split42/prepare.py; research/ddp/breadth_20261027_wave5/fano_split42/search.cpp; research/ddp/breadth_20261027_wave5/fano_split42/source.edges; research/ddp/breadth_20261027_wave5/fano_split42/source_structure.json; research/ddp/breadth_20261027_wave5/fano_split42/terminal.json; research/ddp/breadth_20261027_wave5/fano_split42/upper_bound_reading.json"
added: 2026-10-27T08:25:52Z
tags: ["ddp", "method-ledger"]
---

# Fano独立集拆点42固定完整族

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (4,3)；L=41；candidate_graph_or_family n=42；条件性n=42（未据此计纪录）

**距目标的证据：** 实际D=4，目标D=3；普通无序坏对=45；saved_explicit_graph；全13122候选无D3；最佳显式图D4、45坏对。

**其他指标（保持原计数类型）：**
```json
{
  "candidates_examined": 13122
}
```





**原始证据：** [research/ddp/breadth_20261027_wave5/fano_split42/REPORT.md](../../research/ddp/breadth_20261027_wave5/fano_split42/REPORT.md)；[research/ddp/breadth_20261027_wave5/fano_split42/RESULT.json](../../research/ddp/breadth_20261027_wave5/fano_split42/RESULT.json)；[research/ddp/breadth_20261027_wave5/fano_split42/best.edges](../../research/ddp/breadth_20261027_wave5/fano_split42/best.edges)；[research/ddp/breadth_20261027_wave5/fano_split42/best.independent_check.json](../../research/ddp/breadth_20261027_wave5/fano_split42/best.independent_check.json)；[research/ddp/breadth_20261027_wave5/fano_split42/best_bad_pairs.json](../../research/ddp/breadth_20261027_wave5/fano_split42/best_bad_pairs.json)；[research/ddp/breadth_20261027_wave5/fano_split42/best_parameters.json](../../research/ddp/breadth_20261027_wave5/fano_split42/best_parameters.json)；[research/ddp/breadth_20261027_wave5/fano_split42/build_metrics.json](../../research/ddp/breadth_20261027_wave5/fano_split42/build_metrics.json)；[research/ddp/breadth_20261027_wave5/fano_split42/execution_metrics.json](../../research/ddp/breadth_20261027_wave5/fano_split42/execution_metrics.json)；[research/ddp/breadth_20261027_wave5/fano_split42/input.txt](../../research/ddp/breadth_20261027_wave5/fano_split42/input.txt)；[research/ddp/breadth_20261027_wave5/fano_split42/prepare.py](../../research/ddp/breadth_20261027_wave5/fano_split42/prepare.py)；[research/ddp/breadth_20261027_wave5/fano_split42/search.cpp](../../research/ddp/breadth_20261027_wave5/fano_split42/search.cpp)；[research/ddp/breadth_20261027_wave5/fano_split42/source.edges](../../research/ddp/breadth_20261027_wave5/fano_split42/source.edges)；[research/ddp/breadth_20261027_wave5/fano_split42/source_structure.json](../../research/ddp/breadth_20261027_wave5/fano_split42/source_structure.json)；[research/ddp/breadth_20261027_wave5/fano_split42/terminal.json](../../research/ddp/breadth_20261027_wave5/fano_split42/terminal.json)；[research/ddp/breadth_20261027_wave5/fano_split42/upper_bound_reading.json](../../research/ddp/breadth_20261027_wave5/fano_split42/upper_bound_reading.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** O4中7个Fano点各3种unordered2+2partition及6个固定matching shifts，共13122项

**正向保证：** 全部候选simple4regular；旧O4三步覆盖已核对

**仍未完成：** 未排其他orientation、任意matching或一般42点图。

**启发与重启依据：** 须改变明确模板，不加相同族参数。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

