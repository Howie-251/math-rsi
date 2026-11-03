---
type: experiment
node_id: exp:ddp-d13-d4-matching-control-a-delete-all-z-20261027
title: "6804源受控修改A_delete_all_z：首根缺1519，固定规则停止"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d13_D4_current6804/matching_controls/REPORT.md; research/ddp/more_graphs_20261027/d13_D4_current6804/matching_controls/RESULT.json; research/ddp/more_graphs_20261027/d13_D4_current6804/matching_controls/PREDICTION.json"
added: 2026-10-27T18:46:25Z
tags: ["ddp", "method-ledger"]
---

# 6804源受控修改A_delete_all_z：首根缺1519，固定规则停止

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (12,4)；L=6156；candidate_graph_or_family n=6804

**距目标的证据：** Prediction supported: modified graph is not diameter<=4. Root0 fails at vertex11. 1519 is a single-root endpoint count, not ordinary unordered bad-pair total.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 6804,
  "source_m": 44226,
  "actual_m": 40824,
  "roots_checked": 1,
  "single_root_missing_targets": 1519,
  "first_witness": [
    0,
    11
  ],
  "newgraphs": 0,
  "original_source_BFS": 0,
  "CPU_shared_two_controls": 0.106975075
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d13_D4_current6804/matching_controls/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D4_current6804/matching_controls/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D4_current6804/matching_controls/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D4_current6804/matching_controls/RESULT.json)；[research/ddp/more_graphs_20261027/d13_D4_current6804/matching_controls/PREDICTION.json](../../research/ddp/more_graphs_20261027/d13_D4_current6804/matching_controls/PREDICTION.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Construct actual simple 12-regular graph6804/40824; inspect radius4 only at controller identity/fiber zero. First root misses 1519 targets including vertex11; exact global diameter and connectivity not computed. Original author D4 fact reused without source BFS.

**仍未完成：** Only these two fixed interventions are refuted. Other affine offsets, charts and general constructions remain open; complete Lean is unfinished.

**启发与重启依据：** Removing matching loses controller reach; restoring zero-offset matching repairs599 targets and all controller-level empty fibers, but both controls still miss the same four points in identity fiber. Nonzero affine displacement supplies complementary fiber routes. Stop these exact two controls, no c-grid or successive badpair repairs. Restart requires an independently motivated different connection rule.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

