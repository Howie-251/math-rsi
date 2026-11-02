---
type: experiment
node_id: exp:ddp-wave5-mizuno-d4-source
title: "Mizuno72宽D4证书恢复及从属容量筛"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave5/mizuno_d4_source/README.md; research/ddp/breadth_20261027_wave5/mizuno_d4_source/C4_wide_C10_capacity.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/alternative76_capacity.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/bfs_certificate_cpp.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/bfs_certificate_numba.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_C4_wide_C10.py; research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_controller_and_capacity.py; research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_quotient.py; research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_wide_C10.py; research/ddp/breadth_20261027_wave5/mizuno_d4_source/construction.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller72.edges; research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller72.labels.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller_and_capacity.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller_routes.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/pencil_routes.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/proof_ja.md; research/ddp/breadth_20261027_wave5/mizuno_d4_source/quotient_check.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/repair_comparison.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/results_degree12-diameter4_certificate.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/search_provenance.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/small_certificate.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/verify_certificate.py; research/ddp/breadth_20261027_wave5/mizuno_d4_source/wide_C10_capacity.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/wide_C10_functions.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/wide_C10_tight_slot_sum.json"
added: 2026-10-27T07:55:17Z
tags: ["ddp", "method-ledger"]
---

# Mizuno72宽D4证书恢复及从属容量筛

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (12,4)；L=5832

**距目标的证据：** 原chart支持局部self与12个R2 pencil；exact-NB4不足不否定宽证书。

**其他指标（保持原计数类型）：**
```json
{
  "source_controller_n": 72,
  "source_record_n": 5832,
  "source_reported_D": 4,
  "source_exact_NB4_missing_ordered_pairs": 720,
  "source_exact_NB4_missing_diagonal": 72
}
```



**从属变体：**
```json
[
  {
    "id": "source8base-exactNB4",
    "kind": "capacity",
    "hypothetical_controller_n": 80,
    "hypothetical_lift_n": 6480,
    "scope": "固定8base的uniform≥10sheet exact-NB4",
    "result": "闭词碰撞至多9状态；只排exact条件，不排宽证书"
  },
  {
    "id": "alternative4base-C19",
    "kind": "capacity",
    "hypothetical_controller_n": 76,
    "hypothetical_lift_n": 6156,
    "result": "紧槽18<19；固定模板全部赋值失败",
    "evidence": "alternative76_capacity.json"
  },
  {
    "id": "source8base-C10-forced20C4",
    "kind": "capacity",
    "hypothetical_controller_n": 80,
    "hypothetical_lift_n": 6480,
    "result": "六自由强制C4族宽容量9<10；未枚举10^6",
    "evidence": "C4_wide_C10_capacity.json"
  },
  {
    "id": "source8base-C10-ninefree",
    "kind": "capacity-pass",
    "hypothetical_controller_n": 80,
    "hypothetical_lift_n": 6480,
    "result": "宽容量最小10，通过必要筛；有限profile另记",
    "evidence": "wide_C10_capacity.json"
  }
]
```

**原始证据：** [research/ddp/breadth_20261027_wave5/mizuno_d4_source/README.md](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/README.md)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/C4_wide_C10_capacity.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/C4_wide_C10_capacity.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/alternative76_capacity.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/alternative76_capacity.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/bfs_certificate_cpp.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/bfs_certificate_cpp.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/bfs_certificate_numba.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/bfs_certificate_numba.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_C4_wide_C10.py](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_C4_wide_C10.py)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_controller_and_capacity.py](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_controller_and_capacity.py)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_quotient.py](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_quotient.py)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_wide_C10.py](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_wide_C10.py)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/construction.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/construction.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller72.edges](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller72.edges)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller72.labels.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller72.labels.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller_and_capacity.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller_and_capacity.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller_routes.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller_routes.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/pencil_routes.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/pencil_routes.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/proof_ja.md](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/proof_ja.md)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/quotient_check.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/quotient_check.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/repair_comparison.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/repair_comparison.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/results_degree12-diameter4_certificate.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/results_degree12-diameter4_certificate.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/search_provenance.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/search_provenance.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/small_certificate.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/small_certificate.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/verify_certificate.py](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/verify_certificate.py)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/wide_C10_capacity.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/wide_C10_capacity.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/wide_C10_functions.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/wide_C10_functions.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/wide_C10_tight_slot_sum.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/wide_C10_tight_slot_sum.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 原72控制器的I∪R2∪100RG4充分证书；多项从属结构容量检查

**正向保证：** 原chart18个rank2 planes覆盖self全部81点；12个R2词各自四超平面pencil覆盖81点；100个RG4词满秩

**仍未完成：** source证书≠新控制器；quotient chart的self/R2仅33/45，不能混用。

**启发与重启依据：** 改变容量瓶颈或有新controller证书；原C10父profile已另行终态。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

