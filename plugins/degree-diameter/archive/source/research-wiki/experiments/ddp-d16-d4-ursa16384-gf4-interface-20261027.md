---
type: experiment
node_id: exp:ddp-d16-d4-ursa16384-gf4-interface-20261027
title: "URSA16384字面恢复64×GF4四全局线chart接口"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/PREDICTION.json; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/REPORT.md; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/RESULT.json; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/INTERFACE.json; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/CONTROLLER_SUMMARY.json; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/SOURCE_FACTS.json"
added: 2026-10-27T18:55:31Z
tags: ["ddp", "method-ledger"]
---

# URSA16384字面恢复64×GF4四全局线chart接口

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (16,4)；L=16384；known_source_or_recovery n=16384

**距目标的证据：** 预测该literal有可移植四chart接口被支持。逆type0↔3、1↔2；type0有8个8cycles，type1有16个4cycles。在g=16c+h四base上，alpha0123/beta0132与现有76controller一致；但内部16标签不是普通C16加法。canonical矩阵rank3是line关系代表，不能擅自当可逆transition。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 16384,
  "source_m": 131072,
  "degree16": 16384,
  "controller_n": 64,
  "controller_degree": 4,
  "fiber_order": 256,
  "directed_ports": 256,
  "global_relation_types": 4,
  "affine_relation_failures": 0,
  "type_inverse_pairs": [
    [
      0,
      3
    ],
    [
      1,
      2
    ]
  ],
  "constant_offsets": [
    0,
    0,
    0,
    0
  ],
  "source_reported_D": 4,
  "actual_source_D_recomputed": null,
  "CPU": 0.381141023,
  "old_source_BFS": 0,
  "candidate_search": false,
  "independent_mechanism_count_increment": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/PREDICTION.json](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/PREDICTION.json)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/REPORT.md](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/REPORT.md)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/RESULT.json](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/RESULT.json)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/INTERFACE.json](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/INTERFACE.json)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/CONTROLLER_SUMMARY.json](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/CONTROLLER_SUMMARY.json)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/SOURCE_FACTS.json](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/SOURCE_FACTS.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 当前官方URSA16384 literal一次读取度数与分块。按v=256g+x有64controller×F4^4，全部16384顶点degree16，全部256有向port对256输入均为仿射GF4线关系；恰4全局type，每controller各一次。source D4继承公开源，不重跑旧图BFS。

**仍未完成：** Published sourceD4 is inherited; source all-pairs proof not rerun. No newrecord follows from interface recovery alone.

**启发与重启依据：** 接口恢复属于同一来源的构造理解，不计新纪录或独立新机制。下一受控检验须保具体满秩闭路/低秩pencil资源，不能只凭相同alpha/beta自动移植原GF3充分证书。完整controller/perms、四关系方向/列、所有port已存INTERFACE。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

