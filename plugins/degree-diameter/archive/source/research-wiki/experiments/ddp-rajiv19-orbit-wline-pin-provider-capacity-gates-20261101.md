---
type: experiment
node_id: exp:ddp-rajiv19-orbit-wline-pin-provider-capacity-gates-20261101
title: "Rajiv2783源的pin覆盖对照：orbit改W-line修好跨类，全部W-line11+8规则被21<22容量严格排"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/PRED.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/PROOF.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/RESULT.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/REPORT.md; research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/ALL_BASE_CAPACITY_FINAL.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/PREPROCESS_RESULT.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/CONTROLLED_COMPARISON.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/SOURCE_PARAMETERS.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/SOURCE_GEOMETRY.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/TERMINAL.json; research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/prepare.py; research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/check_capacity.py; research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE14_PIN_EXTENSION_TARGETED_20261101.md; research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE14_PIN_EXTENSION_TARGETED_20261101.json"
added: 2026-11-01T05:59:59Z
tags: ["ddp", "method-ledger"]
---

# Rajiv2783源的pin覆盖对照：orbit改W-line修好跨类，全部W-line11+8规则被21<22容量严格排

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (19,3)；L=2783；条件性n=2784（未据此计纪录）；从属目标：[[14, 3]]

**距目标的证据：** Public2783 source D3 inherited, generated once for a new exact R2 provider interface; zero old D3 BFS, no2784 graph. Canonical partial pin coverage is not a full19pin candidate.；公共2783/25773源仅为新接口生成一次，不算新图。11pin transvection orbit覆1331/1331 point和600/1452 line；换W-line11pins仍覆全point、line升1346/1452，仅本class余106。每point/class provider恰whole11-pencil+4gadget，全部1331实际provider比对PASS。全base/class Wline11+8等价K121选9providers；55 omitted-pencil pairs中54乐观≤21<22，唯一[3,9]乐观22又因九pencil分别最大和21严格失败，0solver/2784图。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_Lean_instances": 0,
  "new_general_lemmas": 0,
  "new_lower_bound_mathematically_verified": false,
  "source_n": 2783,
  "source_m": 25773,
  "source_generated_once": true,
  "source_reproduction_counted_as_new": false,
  "source_D3_inherited": true,
  "source_BFS_roots": 0,
  "point_targets": 1331,
  "line_targets": 1452,
  "orbit11_point_coverage": 1331,
  "orbit11_line_coverage": 600,
  "Wline11_point_coverage": 1331,
  "Wline11_line_coverage": 1346,
  "Wline11_only_exceptional_class_missing": 106,
  "provider_full_pencil": 11,
  "provider_external_gadget": 4,
  "exact_point_provider_checks": 1331,
  "all_base_rules_reduced_to_K_vertices": 121,
  "selected_providers_required": 9,
  "omitted_pencil_pairs": 55,
  "initial_excluded_pairs": 54,
  "sole_optimistic_pair": [
    3,
    9
  ],
  "final_per_pencil_capacity": 21,
  "needed_omitted_targets": 22,
  "preprocessing_CPU_seconds": 0.182630432,
  "final_capacity_CPU_seconds": 0.00256846,
  "solver_calls": 0,
  "solver_authorization_used": false,
  "independent_construction_framework_claimed": false
}
```



**从属变体：**
```json
[
  {
    "label": "q8_degree14_geometry_line8_plus_at_most6extras_UNEXECUTED",
    "target": [
      14,
      3
    ],
    "savedL": 1201,
    "hypothetical_n": 1089,
    "status": "BASELINE_BLOCKS_1089_BEFORE_ANY_NEW_SOURCE_READ_OR_EXECUTION",
    "public_main_table_value": 1201,
    "public_main_table_date": "2026-10-30 Rajiv update; checked2026-11-01",
    "stale_detail_value": 1141,
    "old_September_source_value": 1088,
    "existing_public_retained_edge_extension1094": true,
    "source_graphs_generated": 0,
    "new_source_inputs_read": 0,
    "calculations": 0,
    "solver_calls": 0,
    "handles_started": 0,
    "new_graphs": 0,
    "old_q8_degree13_scopes_reopened": false,
    "global_exclusion_claimed": false
  }
]
```

**原始证据：** [research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/PRED.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/PRED.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/PROOF.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/PROOF.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/RESULT.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/RESULT.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/REPORT.md](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/REPORT.md)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/ALL_BASE_CAPACITY_FINAL.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/ALL_BASE_CAPACITY_FINAL.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/PREPROCESS_RESULT.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/PREPROCESS_RESULT.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/CONTROLLED_COMPARISON.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/CONTROLLED_COMPARISON.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/SOURCE_PARAMETERS.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/SOURCE_PARAMETERS.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/SOURCE_GEOMETRY.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/SOURCE_GEOMETRY.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/prepare.py](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/prepare.py)；[research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/check_capacity.py](../../research/ddp/two_successful_methods_20261101/retained_edge_transfer/rajiv19_orbit_pins/check_capacity.py)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE14_PIN_EXTENSION_TARGETED_20261101.md](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE14_PIN_EXTENSION_TARGETED_20261101.md)；[research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE14_PIN_EXTENSION_TARGETED_20261101.json](../../research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE14_PIN_EXTENSION_TARGETED_20261101.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Actual Rajiv q11 fibre source,1331 degree18 points/1452 saturated degree19 lines. Strictly excludes every single-new-vertex retained-edge rule using11 affine points of one isotropic Wline plus at most8 additional old pointpins, across all bases/classes. Arbitrary19point pin sets, original orbit11+8, other sources and cooperative new points remain open. Source reproduction and local provider checks are not new graph/oldD3 validation.

**正向保证：** 全部point/class的R2 line-provider公式由作者beta/pencil/gadget定义导出，并与1331点实际two-step并集逐项一致。；orbit与Wline受控对照支持全point覆盖预测，并识别仅本class line覆盖的同时实现障碍，不只报告总缺项。；9providers必要：8*15=120<121；至少两条pencil未被全pencil提供，22遗漏目标只能靠gadget。；54 omitted-pairs≤21；唯一3,9强制其余九pencil各选1，最大贡献1+2+2+3+3+2+3+2+3=21<22，关闭所有Wline-base而非单seed。

**仍未完成：** 无新增完整图/纪录/Lean。任意19pins与orbit+8没有运行或排除；即使许可新增旧旧边，已用唯一余度的pins和已饱和line不能改这些两步line路线，但删旧边rewiring仍不受本排除。q8/14迁移只是未执行提案，被当前主表1201阻断1089；不当机制失败或新实验节点。

**启发与重启依据：** 覆盖理解改变了base从orbit到W-line，并把逐个seed的模型化简为全K121的9provider条件。最后障碍是pencil/gadget覆盖不能同时满足，故停止一Wline+8全域，不运行已授权但未用的solver。若继续须改变base或联合新点，不能自动恢复本域。q8/14仅换q试1089会落后当前1201，入口停止，不读新源/续旧13度域。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

