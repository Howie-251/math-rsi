---
type: experiment
node_id: exp:ddp-d11-d6-current186033-source-20261027
title: "(11,6)186033实际源：24685free、唯一satN1原型19161"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d11_D6_current186033/REPORT.md; research/ddp/more_graphs_20261027/d11_D6_current186033/SOURCE_PROFILE.json; research/ddp/more_graphs_20261027/d11_D6_current186033/PROTOTYPES.json; research/ddp/more_graphs_20261027/d11_D6_current186033/PREDICTION.json; research/ddp/more_graphs_20261027/d11_D6_current186033/DOWNLOAD_HANDLE.json; research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/INPUT.json; research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/RESULT.json; research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/RESULT_METADATA_ERRATUM.json; research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/FREE_PORT_PARTIAL_PROFILE.json; research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/PRESTART_FAILURE.json; research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/HANDLE.json; research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/TERMINAL.json; research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/run_executed_v1.py; research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/run.py; research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/REPORT.md; research/ddp/refresh_20261029/d11_D6_mechanism_read/LAYER_BINDING_PREDICTION.md; research/ddp/refresh_20261029/d11_D6_mechanism_read/MECHANISM_NOTE.md"
added: 2026-10-29T17:00:19Z
tags: ["ddp", "method-ledger"]
---

# (11,6)186033实际源：24685free、唯一satN1原型19161

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (11,6)；L=186033；known_source_or_recovery n=186033

**距目标的证据：** 实际D=6，目标D=6；Inherited officialsourceD6; no new sourceallBFS.；事前存在satN≤1预测SUPPORTED，但source恢复不是新下界。 后续一次真实prefix标签门通过四层degree/连通二分签名与63030异色双锚条件；固定K6所需六半类资源门被H7 color0的0个free反驳，CPU1.214964867。另三半类未计数；未生成K6图／新球／solver或重验sourceD6，不外推其它helper规则。

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 186033,
  "source_m": 1010817,
  "degree_histogram": {
    "7": 3,
    "8": 11,
    "9": 13,
    "10": 24658,
    "11": 161348
  },
  "free_vertices": 24685,
  "free_slots": 24729,
  "minSatN": 1,
  "full_spare_star_count": 0,
  "one_fault_star_count": 1,
  "source_allBFS": 0,
  "profile_CPU_seconds": 2.978168826,
  "download_bytes": 5936714,
  "download_wall_seconds": 67.65634925663471,
  "source_credit": "Dharunish Yugeswardeenoo; preserves RishabhRajiv182618 andadds3415",
  "official_URL": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g6.html",
  "baseline_date": "2026-10-27",
  "tower_prefix_and_fixed_K6_gate": {
    "prefix_signature": "SUPPORTED",
    "fixed_K6_capacity": "REFUTED",
    "successful_worker_CPU_seconds": 1.214964867,
    "four_connected_bipartite_layer_checks": 4,
    "opposite_color_two_anchor_checks": 63030,
    "H9_half_free_counts": [
      12353,
      12280
    ],
    "H7_color0_free_count": 0,
    "half_classes_checked": 3,
    "half_classes_unchecked": 3,
    "source_D6_distance_BFS": 0,
    "new_balls": 0,
    "solver_calls": 0,
    "candidate_graphs": 0,
    "alternative_partitions_tried": 0,
    "generalized_hexagon_isomorphism_proved": false,
    "fixed_K6_closed_only": true
  }
}
```



**从属变体：**
```json
[
  {
    "label": "actual_tower_prefix_and_fixed_K6_halfclass_capacity_20261029",
    "record_type": "source-label-binding-and-fixed-rule-resource-gate",
    "target_Delta": 11,
    "target_D": 6,
    "source_n": 186033,
    "n": {
      "actual": null,
      "hypothetical": 186039
    },
    "status": "PREFIX_SIGNATURE_SUPPORTED_K6_CAPACITY_REFUTED",
    "scope": "Unique frozen fourprefix intervals andsix-halfclassfreecapacityforfixedK6oneanchorperhalf rule;noalternativepartitionorhelpernumber",
    "result": {
      "status": "FREE_PORT_CAPACITY_GATE_FAIL",
      "prefix_signature_prediction": "SUPPORTED",
      "six_half_free_port_prediction": "REFUTED",
      "source_n": 186033,
      "source_m": 1010817,
      "source_old_n": 182618,
      "prefix_bounds": [
        0,
        132860,
        172076,
        179888,
        182618,
        186033
      ],
      "counterexample": {
        "layer": 1,
        "color": 0,
        "current_free_count": 0,
        "required": 6
      },
      "layers": [
        {
          "layer": 0,
          "range": [
            0,
            132860
          ],
          "n": 132860,
          "expected_internal_degree": 10,
          "internal_degree_histogram": {
            "10": 132860
          },
          "vertices_degree_checked": 132860,
          "bipartite": true,
          "connected": true,
          "canonical_color0_root": 0,
          "color_class_sizes": {
            "0": 66430,
            "1": 66430
          },
          "later_original_neighbor_histogram": {
            "1": 99516,
            "0": 33344
          }
        },
        {
          "layer": 1,
          "range": [
            132860,
            172076
          ],
          "n": 39216,
          "expected_internal_degree": 8,
          "internal_degree_histogram": {
            "8": 39216
          },
          "vertices_degree_checked": 39216,
          "bipartite": true,
          "connected": true,
          "canonical_color0_root": 132860,
          "color_class_sizes": {
            "0": 19608,
            "1": 19608
          },
          "later_original_neighbor_histogram": {
            "1": 21084,
            "0": 18132
          }
        },
        {
          "layer": 2,
          "range": [
            172076,
            179888
          ],
          "n": 7812,
          "expected_internal_degree": 6,
          "internal_degree_histogram": {
            "6": 7812
          },
          "vertices_degree_checked": 7812,
          "bipartite": true,
          "connected": true,
          "canonical_color0_root": 172076,
          "color_class_sizes": {
            "0": 3906,
            "1": 3906
          },
          "later_original_neighbor_histogram": {
            "1": 5460,
            "0": 2352
          }
        },
        {
          "layer": 3,
          "range": [
            179888,
            182618
          ],
          "n": 2730,
          "expected_internal_degree": 5,
          "internal_degree_histogram": {
            "5": 2730
          },
          "vertices_degree_checked": 2730,
          "bipartite": true,
          "connected": true,
          "canonical_color0_root": 179888,
          "color_class_sizes": {
            "0": 1365,
            "1": 1365
          },
          "later_original_neighbor_histogram": {
            "0": 2730
          }
        }
      ],
      "layer_bipartite_connected_traversals_completed": 4,
      "source_D6_BFS": 0,
      "radius_ball_queries": 0,
      "solver_calls": 0,
      "candidate_graphs": 0,
      "other_prefix_or_permutation_trials": 0,
      "geometry_isomorphism_proved": false,
      "internal_D6_proved_by_this_gate": false,
      "automatic_179888_coverage_certified_here": false,
      "cpu_seconds": 1.214964867,
      "wall_seconds": 1.2866156287491322,
      "pid": 2395092,
      "budget_cpu_seconds": 20,
      "free_half_profiles": [
        {
          "layer": 0,
          "color": 0,
          "class_size": 66430,
          "current_free_count": 12353,
          "first_free_ids": [
            1,
            6,
            7,
            14,
            15,
            19,
            20,
            22,
            34,
            35,
            40,
            58
          ],
          "passes_need6": true
        },
        {
          "layer": 0,
          "color": 1,
          "class_size": 66430,
          "current_free_count": 12280,
          "first_free_ids": [
            66433,
            66436,
            66439,
            66440,
            66442,
            66449,
            66469,
            66470,
            66489,
            66493,
            66497,
            66501
          ],
          "passes_need6": true
        },
        {
          "layer": 1,
          "color": 0,
          "class_size": 19608,
          "current_free_count": 0,
          "first_free_ids": [],
          "passes_need6": false
        }
      ],
      "cross_layer_anchor_checks": 63030,
      "metadata_correction": {
        "field": "prefix_signature_prediction",
        "original_executed_writer_value": "REFUTED",
        "corrected_value": "SUPPORTED",
        "reason": "Writercondition originally recognizedonlyjointPASS;capacityfailure was reachedonlyafter allstructural checks completed. No numericdatachanged orrerun."
      },
      "six_half_free_port_profiles_complete": false,
      "free_half_classes_checked": 3,
      "free_half_classes_not_checked": [
        {
          "layer": 1,
          "color": 1
        },
        {
          "layer": 2,
          "color": 0
        },
        {
          "layer": 2,
          "color": 1
        }
      ],
      "checked_H9_free_total": 24633,
      "all_six_free_count_sum": null
    },
    "prefix_signature_prediction": "SUPPORTED",
    "six_half_free_port_prediction": "REFUTED",
    "closed_scope": "Thefixedcurrent-sourceK6withonefreeoldpinperhelperineachsixupperhalfclasscannotbeformed.",
    "unclosed_gap": "InternalH(q)isomorphism/D6notprovedbythissignaturegate;otherconnectionrulesandgeneral11D6notexcluded. NoK6coverageorgraphtested.",
    "source_D6_BFS": 0,
    "new_balls": 0,
    "solver_calls": 0,
    "candidate_graphs": 0,
    "measured_successful_worker_CPU_seconds": 1.214964867,
    "other_half_class_counts": "H7 color1 and both H5 colors not checked after decisive H7 color0 failure",
    "evidence_paths": [
      "research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/INPUT.json",
      "research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/RESULT.json",
      "research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/RESULT_METADATA_ERRATUM.json",
      "research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/FREE_PORT_PARTIAL_PROFILE.json",
      "research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/PRESTART_FAILURE.json",
      "research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/HANDLE.json",
      "research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/TERMINAL.json",
      "research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/run_executed_v1.py",
      "research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/run.py",
      "research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/REPORT.md",
      "research/ddp/refresh_20261029/d11_D6_mechanism_read/LAYER_BINDING_PREDICTION.md",
      "research/ddp/refresh_20261029/d11_D6_mechanism_read/MECHANISM_NOTE.md"
    ]
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/d11_D6_current186033/REPORT.md](../../research/ddp/more_graphs_20261027/d11_D6_current186033/REPORT.md)；[research/ddp/more_graphs_20261027/d11_D6_current186033/SOURCE_PROFILE.json](../../research/ddp/more_graphs_20261027/d11_D6_current186033/SOURCE_PROFILE.json)；[research/ddp/more_graphs_20261027/d11_D6_current186033/PROTOTYPES.json](../../research/ddp/more_graphs_20261027/d11_D6_current186033/PROTOTYPES.json)；[research/ddp/more_graphs_20261027/d11_D6_current186033/PREDICTION.json](../../research/ddp/more_graphs_20261027/d11_D6_current186033/PREDICTION.json)；[research/ddp/more_graphs_20261027/d11_D6_current186033/DOWNLOAD_HANDLE.json](../../research/ddp/more_graphs_20261027/d11_D6_current186033/DOWNLOAD_HANDLE.json)；[research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/INPUT.json](../../research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/INPUT.json)；[research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/RESULT.json](../../research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/RESULT.json)；[research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/RESULT_METADATA_ERRATUM.json](../../research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/RESULT_METADATA_ERRATUM.json)；[research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/FREE_PORT_PARTIAL_PROFILE.json](../../research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/FREE_PORT_PARTIAL_PROFILE.json)；[research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/PRESTART_FAILURE.json](../../research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/PRESTART_FAILURE.json)；[research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/HANDLE.json](../../research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/HANDLE.json)；[research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/TERMINAL.json](../../research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/TERMINAL.json)；[research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/run_executed_v1.py](../../research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/run_executed_v1.py)；[research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/run.py](../../research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/run.py)；[research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/REPORT.md](../../research/ddp/refresh_20261029/d11_D6_mechanism_read/layer_binding/REPORT.md)；[research/ddp/refresh_20261029/d11_D6_mechanism_read/LAYER_BINDING_PREDICTION.md](../../research/ddp/refresh_20261029/d11_D6_mechanism_read/LAYER_BINDING_PREDICTION.md)；[research/ddp/refresh_20261029/d11_D6_mechanism_read/MECHANISM_NOTE.md](../../research/ddp/refresh_20261029/d11_D6_mechanism_read/MECHANISM_NOTE.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 单次官方gzip下载后一次实际解析；186033/1010817，度7:3/8:11/9:13/10:24658/11:161348，free24685/slots24729。全部186033原型satN检查：0fullsparestar、仅v19161有satN1且旧度10。

**正向保证：** Actual four-prefix degree/connectivity/bipartition and opposite-color anchor signatures bind cached labels; this does not prove generalized-hexagon isomorphism or internal D6.

**仍未完成：** 已闭固定mandatory9+至多2guard及本次固定K6半类资源规则；一般11D6增广、其它helper连接规则、内部几何同构未排。H7 color1及H5两色资源未在本门统计。

**启发与重启依据：** 奇数阶仅保证非正则；实际余量集中但没有完整star。只能据真实唯一onefault原型开展覆盖实验，不能凭free数量宣称可增点。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

