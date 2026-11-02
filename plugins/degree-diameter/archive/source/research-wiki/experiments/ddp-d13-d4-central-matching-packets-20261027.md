---
type: experiment
node_id: exp:ddp-d13-d4-central-matching-packets-20261027
title: "6804中心匹配32/36路线包完整铺满；原生成元模8受奇偶核阻断"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d13_D4_current6804/central_matching_packets/REPORT.md; research/ddp/more_graphs_20261027/d13_D4_current6804/central_matching_packets/RESULT.json"
added: 2026-10-27T18:48:42Z
tags: ["ddp", "method-ledger"]
---

# 6804中心匹配32/36路线包完整铺满；原生成元模8受奇偶核阻断

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (13,4)；L=6804；条件性n=7776（未据此计纪录）

**距目标的证据：** 作者README已明确三coset tiling原则，本项只作实际32/36量化和固定C8坐标的奇偶障碍，不登记新tiling定理。

**其他指标（保持原计数类型）：**
```json
{
  "full_packets": 32,
  "partial_packets": 4,
  "partial_union_size": 54,
  "phase_capacity_upper_min": 1280,
  "module8_phase_required": 648,
  "parity_kernel_max_controller_order": 48,
  "CPU": 0.034883321,
  "BFS": 0,
  "graphs": 0,
  "tiling_principle": "INHERITED_AUTHOR_README"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d13_D4_current6804/central_matching_packets/REPORT.md](../../research/ddp/more_graphs_20261027/d13_D4_current6804/central_matching_packets/REPORT.md)；[research/ddp/more_graphs_20261027/d13_D4_current6804/central_matching_packets/RESULT.json](../../research/ddp/more_graphs_20261027/d13_D4_current6804/central_matching_packets/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 量化实际6804 chart的36个reduced3word插z四位置包；32包三coset齐全、每源81，4包每源54。仅线性-I与M交换；完整仿射gamma未必交换。对保原a=(1,1),b=(0,4),z=(0,6)的C8任意unit action，chi(i,j)=i-j mod2使生成子群至多48/96，故此保坐标迁移不连通。

**仍未完成：** No general parameter-family exclusion; complete Lean remains unproved.

**启发与重启依据：** 中心plain边的作用是通过c−Mc制造同方向的三偏移类，而非提供spares。模数变更前须保连通；只排保留这些坐标的C8迁移，不扩为全部C8控制器。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

