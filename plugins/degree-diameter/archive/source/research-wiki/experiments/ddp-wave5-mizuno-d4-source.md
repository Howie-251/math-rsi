---
type: experiment
node_id: exp:ddp-wave5-mizuno-d4-source
title: "原Mizuno72/F3⁴ D4证书继承；5832源升13..16度的完整原N12复制已被公开包络阻断"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave5/mizuno_d4_source/README.md; research/ddp/breadth_20261027_wave5/mizuno_d4_source/C4_wide_C10_capacity.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/alternative76_capacity.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/bfs_certificate_cpp.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/bfs_certificate_numba.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_C4_wide_C10.py; research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_controller_and_capacity.py; research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_quotient.py; research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_wide_C10.py; research/ddp/breadth_20261027_wave5/mizuno_d4_source/construction.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller72.edges; research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller72.labels.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller_and_capacity.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller_routes.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/pencil_routes.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/proof_ja.md; research/ddp/breadth_20261027_wave5/mizuno_d4_source/quotient_check.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/repair_comparison.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/results_degree12-diameter4_certificate.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/search_provenance.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/small_certificate.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/verify_certificate.py; research/ddp/breadth_20261027_wave5/mizuno_d4_source/wide_C10_capacity.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/wide_C10_functions.json; research/ddp/breadth_20261027_wave5/mizuno_d4_source/wide_C10_tight_slot_sum.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d12_5832_D4_source_gate/PRED.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d12_5832_D4_source_gate/NOTE.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d12_5832_D4_source_gate/RESULT.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d12_5832_D4_source_gate/TERMINAL.json"
added: 2026-11-01T15:21:50Z
tags: ["ddp", "method-ledger"]
---

# 原Mizuno72/F3⁴ D4证书继承；5832源升13..16度的完整原N12复制已被公开包络阻断

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (12,4)；L=5832

**距目标的证据：** 原chart支持局部self与12个R2 pencil；exact-NB4不足不否定宽证书。 本次实际公开选择门：13/14/15/16的fullN上包络6318/6804/7290/7776分别被已保存公开D4保证6804/9720/15552/16384超过，STOP无需packing/新图。旧samecap满度筛不冒用于raisedcap；degree13/6804及degree15/15552实际primary还可单调提供冗余阻断。0图/参数/Lean/method，不计源复现/普通容量常识为新成果，报告链接保精确scope。

**其他指标（保持原计数类型）：**
```json
{
  "source_controller_n": 72,
  "source_record_n": 5832,
  "source_reported_D": 4,
  "source_exact_NB4_missing_ordered_pairs": 720,
  "source_exact_NB4_missing_diagonal": 72,
  "published5832_source_frozen_fullN_cap13_16_public_STOP": {
    "status": "ALL_FOUR_CAPS_STOP_PUBLIC_GUARANTEES_EXCEED_FIXED_FULLN_SOURCE_ENVELOPES",
    "source": {
      "q": 3,
      "fiber_dimension": 4,
      "controller": 72,
      "n": 5832,
      "regular_degree": 12,
      "m": 34992
    },
    "scope": "onlythisactualsource_alloldedgeskept_everynewvertexfrozenoriginalN12_nonewnew;caps13to16",
    "inherited_budget": "n<=486Delta",
    "caps": [
      {
        "Delta": 13,
        "fullN_upper": 6318,
        "cached_public": 6804,
        "decision": "STOP"
      },
      {
        "Delta": 14,
        "fullN_upper": 6804,
        "cached_public": 9720,
        "decision": "STOP"
      },
      {
        "Delta": 15,
        "fullN_upper": 7290,
        "cached_public": 15552,
        "decision": "STOP"
      },
      {
        "Delta": 16,
        "fullN_upper": 7776,
        "cached_public": 16384,
        "decision": "STOP"
      }
    ],
    "cached_public_checked_UTC": "2026-10-27 20:54:11 UTC",
    "ordinary_capacity_new_result": false,
    "source_reproduction_new_result": false,
    "new_graph_parameter_Lean_method_increment": [
      0,
      0,
      0,
      0
    ],
    "not_all_D4_or_other_rules_excluded": true,
    "report": "research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d12_5832_D4_source_gate/NOTE.md",
    "result": "research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d12_5832_D4_source_gate/RESULT.json",
    "terminal": "research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d12_5832_D4_source_gate/TERMINAL.json",
    "new_queries_graph_BFS_rank_solver_Lean": 0
  }
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

**原始证据：** [research/ddp/breadth_20261027_wave5/mizuno_d4_source/README.md](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/README.md)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/C4_wide_C10_capacity.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/C4_wide_C10_capacity.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/alternative76_capacity.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/alternative76_capacity.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/bfs_certificate_cpp.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/bfs_certificate_cpp.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/bfs_certificate_numba.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/bfs_certificate_numba.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_C4_wide_C10.py](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_C4_wide_C10.py)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_controller_and_capacity.py](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_controller_and_capacity.py)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_quotient.py](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_quotient.py)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_wide_C10.py](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/check_wide_C10.py)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/construction.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/construction.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller72.edges](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller72.edges)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller72.labels.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller72.labels.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller_and_capacity.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller_and_capacity.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller_routes.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/controller_routes.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/pencil_routes.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/pencil_routes.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/proof_ja.md](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/proof_ja.md)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/quotient_check.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/quotient_check.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/repair_comparison.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/repair_comparison.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/results_degree12-diameter4_certificate.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/results_degree12-diameter4_certificate.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/search_provenance.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/search_provenance.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/small_certificate.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/small_certificate.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/verify_certificate.py](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/verify_certificate.py)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/wide_C10_capacity.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/wide_C10_capacity.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/wide_C10_functions.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/wide_C10_functions.json)；[research/ddp/breadth_20261027_wave5/mizuno_d4_source/wide_C10_tight_slot_sum.json](../../research/ddp/breadth_20261027_wave5/mizuno_d4_source/wide_C10_tight_slot_sum.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d12_5832_D4_source_gate/PRED.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d12_5832_D4_source_gate/PRED.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d12_5832_D4_source_gate/NOTE.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d12_5832_D4_source_gate/NOTE.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d12_5832_D4_source_gate/RESULT.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d12_5832_D4_source_gate/RESULT.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d12_5832_D4_source_gate/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d12_5832_D4_source_gate/TERMINAL.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 原72控制器的I∪R2∪100RG4充分证书；多项从属结构容量检查 2026-11-01只追加同一真实12regular5832源的raised-cap frozenfullN/no-newnew公开选择门：13..16全部STOP；不是原widecontroller全部无解或一般D4排除。

**正向保证：** 原chart18个rank2 planes覆盖self全部81点；12个R2词各自四超平面pencil覆盖81点；100个RG4词满秩

**仍未完成：** source证书≠新控制器；quotient chart的self/R2仅33/45，不能混用。

**启发与重启依据：** 改变容量瓶颈或有新controller证书；原C10父profile已另行终态。 不为此5832源的13..16 frozencompleteN12/全旧边保留/无newnew范围派packing、图/BFS/rank/solver/Lean或换q；此STOP不是所有D4或改旧边/不同接边/其它source排除。另actualpublished15/15552→16的只读源门仍在准备，源648个degree14+14904个degree15非regular，正式receipt未齐不冒packing/图/其它实验授权或结论。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

