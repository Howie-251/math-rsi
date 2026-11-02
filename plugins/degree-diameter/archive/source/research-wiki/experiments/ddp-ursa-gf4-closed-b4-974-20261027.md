---
type: experiment
node_id: exp:ddp-ursa-gf4-closed-b4-974-20261027
title: "GF4强制b⁴闭合974项：samefiber保护成立，全部x0必要覆盖失败"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/closed_b4_transfer/REPORT.md; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/closed_b4_transfer/PREDICTION.json; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/closed_b4_transfer/EVEN_PHASE_PREDICTION.json; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/closed_b4_transfer/RESULT.json; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/closed_b4_transfer/ROWS.json; research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/closed_b4_transfer/run.py"
added: 2026-10-27T18:59:15Z
tags: ["ddp", "method-ledger"]
---

# GF4强制b⁴闭合974项：samefiber保护成立，全部x0必要覆盖失败

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-construction-experiment

**目标与阶数：** (16,4)；L=16384

**距目标的证据：** b⁴voltage和0且1111/2222rank4，所有samefiber对任意x均保护；整体necessarypass0/G4pass0/未试0/UNKNOWN0，全部base0已缺。126odd+61even已无unique rank3槽仍有其它完整union洞。

**其他指标（保持原计数类型）：**
```json
{
  "hypothetical_orders": [
    17408,
    19456,
    18432
  ],
  "original650": {
    "expected": 650,
    "evaluated": 650,
    "untested": 0,
    "simple_controller": 614,
    "non_simple_controller_retained": 36,
    "necessary_passers": 0,
    "strong_G4_passers": 0,
    "no_unique_rank3_slots": 126,
    "first_failed_source_base_histogram": {
      "0": 650
    }
  },
  "even324": {
    "expected": 324,
    "evaluated": 324,
    "untested": 0,
    "simple_controller": 306,
    "non_simple_controller_retained": 18,
    "necessary_passers": 0,
    "strong_G4_passers": 0,
    "no_unique_rank3_slots": 61,
    "first_failed_source_base_histogram": {
      "0": 324
    }
  },
  "total_assignments": 974,
  "source_base_zero_checks": 3896,
  "words_per_check": 341,
  "necessary_passers": 0,
  "strong_G4_passers": 0,
  "untested": 0,
  "UNKNOWN": 0,
  "simple_controllers": 920,
  "non_simple_controllers_retained": 54,
  "source_edge_parses": 0,
  "word_image_recomputations": 0,
  "graphs_generated": 0,
  "BFS": 0,
  "algebra_CPU_before_serialization": 0.7760931719999999,
  "prediction_main": "REFUTED",
  "b4_samefiber_guarantee": "SUPPORTED",
  "even_no_unique_rank3_prediction": "SUPPORTED"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/closed_b4_transfer/REPORT.md](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/closed_b4_transfer/REPORT.md)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/closed_b4_transfer/PREDICTION.json](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/closed_b4_transfer/PREDICTION.json)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/closed_b4_transfer/EVEN_PHASE_PREDICTION.json](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/closed_b4_transfer/EVEN_PHASE_PREDICTION.json)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/closed_b4_transfer/RESULT.json](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/closed_b4_transfer/RESULT.json)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/closed_b4_transfer/ROWS.json](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/closed_b4_transfer/ROWS.json)；[research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/closed_b4_transfer/run.py](../../research/ddp/more_graphs_20261027/d16_D4_ursa16384_affine_probe/closed_b4_transfer/run.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定alpha0123,beta0132,va=(0,x,y,0),vb=(-1,0,0,1)。原m17/19共650项＋单独even18对照324，全974/4base/fiber0的341word actualimage并必要筛；未生成974图，0BFS。920simple与54重复port全保留，未按simple筛。

**仍未完成：** Othercontrollerpatterns, fields/charts, affineoffsets and arbitrary(16,4)graphs remain open; no completeLean claim.

**启发与重启依据：** 闭合满秩b⁴解决真实self缺口但不自动补跨fiber；even2torsion可移除部分唯一坏槽而仍未造出全图。完整关闭指定974constantchart规则，不加modulus/voltage/offset；不据此说全部affine offsets无效。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

