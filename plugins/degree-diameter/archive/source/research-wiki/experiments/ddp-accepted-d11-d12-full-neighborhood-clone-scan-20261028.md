---
type: experiment
node_id: exp:ddp-accepted-d11-d12-full-neighborhood-clone-scan-20261028
title: "Accepted degree11/12 finals: full-neighborhood single and adjacent-pair clone gates empty"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/PREDICTION.json; research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/RESULT.json; research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/REPORT.md; research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/SCAN_RESULT.json; research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/PROFILE_D11.json; research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/PROFILE_D12.json; research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/saturated_neighbor_counts_d11.u8.bin; research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/saturated_neighbor_counts_d12.u8.bin; research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/source_degrees_d11.u8.bin; research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/source_degrees_d12.u8.bin; research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/scan_once.py; research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/TERMINAL.json; research/ddp/more_graphs_20261027/h9_paired_full_neighborhood_clone_rule/PREDICTION.json; research/ddp/more_graphs_20261027/h9_paired_full_neighborhood_clone_rule/BINDING_RESULT.json; research/ddp/more_graphs_20261027/h9_paired_full_neighborhood_clone_rule/REPORT.md; research/ddp/more_graphs_20261027/h9_paired_full_neighborhood_clone_rule/prepare_paper_probe.py; research/ddp/refresh_20261029/d11_to_d12_clone_capacity/PROOF.md; research/ddp/refresh_20261029/d11_to_d12_clone_capacity/RESULT.json"
added: 2026-10-30T03:29:48Z
tags: ["ddp", "method-ledger"]
---

# Accepted degree11/12 finals: full-neighborhood single and adjacent-pair clone gates empty

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** 多目标：degree11_accepted_final→[11, 5]／L=37628；degree12_accepted_final→[12, 5]／L=42342；accepted37631_cap12_complete_old_neighborhood_integer_clone_capacity_20261030→[12, 5]／L=42402（逐变体，不合成一个距离）

**距目标的证据：** 原fullN单点扫描80033 vertices均eligible0，CPU0.514673336保持。追加paired gate CPU0.124853835：D11 full satN1候选空；D12仅28565/36331，两者不相邻且唯一满邻均27674，另有7处共享boundary超load。paired eligible0，0图/BFS/R4/solver。；继承完整degree/sat-neighbor profile的两行加权证书给11Σk≤44197，Σk≤4017，达不到超过42402所需4772。0源读/BFS/LP/solver/新图；上界不称可达。

**其他指标（保持原计数类型）：**
```json
{
  "actual_counts": {
    "source_graphs": 2,
    "source_vertices_scanned": 80033,
    "eligible": 0,
    "candidate_graphs": 0,
    "solver_calls": 0,
    "R4_checks": 0,
    "BFS": 0,
    "D13_rescan": 0,
    "new_lower_bounds": 0
  },
  "source_D5_acceptance": "Inherited for both final graphs",
  "new_lower_bound_mathematically_verified": false,
  "method_count_note": "One multi-target eligibility application of the same prototype-neighborhood mechanism.",
  "paired_variant": {
    "label": "paired_adjacent_full_neighborhood_clones_necessary_gate",
    "record_role": "subordinate_two_parameter_variant_not_new_method",
    "source_cases": [
      {
        "target_Delta": 11,
        "target_D": 5,
        "source_n": 37631,
        "source_m": 205329,
        "hypothetical_n": 37633,
        "full_satN1_candidates": []
      },
      {
        "target_Delta": 12,
        "target_D": 5,
        "source_n": 42402,
        "source_m": 245937,
        "hypothetical_n": 42404,
        "full_satN1_candidates": [
          28565,
          36331
        ]
      }
    ],
    "rule": "Chooseoldedgeuv;addadjacentuprime/vprime;copyN(u)minusv/N(v)minusu;retainalloldedges",
    "complete_necessary_gate": "Becauseeveryoldvertexhasasaturatedneighbor,legalpairrequiresSatN(u)={v},SatN(v)={u};bothfullsatN1",
    "D12_candidate_endpoints_are_adjacent": false,
    "D12_unique_saturated_neighbor_of_each": 27674,
    "D12_shared_boundary_capacity_blocks": 7,
    "eligible_pairs": 0,
    "candidate_graphs": 0,
    "BFS": 0,
    "R4_checks": 0,
    "solver_calls": 0,
    "CPU_seconds": 0.124853835,
    "status": "COMPLETE_PAIRED_RULE_BLOCKED_BY_DEGREE_AND_OLD_EDGE_BINDING",
    "actual_n": null,
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null
  },
  "original_scan_CPU_seconds": 0.514673336,
  "paired_gate_CPU_seconds": 0.124853835,
  "no_repeated_source_scan_for_paired_gate": true,
  "cap12_clone_count_upper": 4017,
  "cap12_final_order_upper": 41648,
  "cap12_integer_packing_solved": false,
  "cap12_upper_bound_attainable_claimed": false
}
```



**从属变体：**
```json
[
  {
    "label": "degree11_accepted_final",
    "target_Delta": 11,
    "target_D": 5,
    "source_n": 37631,
    "source_m": 205329,
    "source": "research/ddp/more_graphs_20261027/h9_d11_followups/graph_d11_D5_n37631.edges",
    "hypothetical_new_n": 37632,
    "actual_new_n": null,
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "eligible_prototypes": 0,
    "minimum_saturated_neighbors": 1,
    "saturated_neighbor_histogram": {
      "1": 15,
      "2": 16,
      "3": 185,
      "4": 144,
      "5": 77,
      "6": 79,
      "7": 100,
      "8": 785,
      "9": 8102,
      "10": 4583,
      "11": 23545
    },
    "free_vertices": 2471,
    "spare_degree_slots": 3283,
    "vertices_scanned": 37631,
    "CPU_seconds": 0.230489849,
    "new_graphs": 0,
    "BFS": 0,
    "R4_checks": 0,
    "savedL": 37628,
    "target": [
      11,
      5
    ],
    "n": {
      "actual": null,
      "hypothetical": 37632
    }
  },
  {
    "label": "degree12_accepted_final",
    "target_Delta": 12,
    "target_D": 5,
    "source_n": 42402,
    "source_m": 245937,
    "source": "research/ddp/more_graphs_20261027/h9_redei15/production/continuation/graphs/graph_d12_D5_n42402.edges",
    "hypothetical_new_n": 42403,
    "actual_new_n": null,
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "eligible_prototypes": 0,
    "minimum_saturated_neighbors": 1,
    "saturated_neighbor_histogram": {
      "1": 20,
      "2": 65,
      "3": 338,
      "4": 812,
      "5": 2039,
      "6": 4448,
      "7": 7462,
      "8": 9407,
      "9": 8167,
      "10": 6416,
      "11": 2644,
      "12": 584
    },
    "free_vertices": 13857,
    "spare_degree_slots": 16950,
    "vertices_scanned": 42402,
    "CPU_seconds": 0.27869404699999994,
    "new_graphs": 0,
    "BFS": 0,
    "R4_checks": 0,
    "savedL": 42342,
    "target": [
      12,
      5
    ],
    "n": {
      "actual": null,
      "hypothetical": 42403
    }
  },
  {
    "label": "paired_adjacent_full_neighborhood_clones_necessary_gate",
    "record_role": "subordinate_two_parameter_variant_not_new_method",
    "source_cases": [
      {
        "target_Delta": 11,
        "target_D": 5,
        "source_n": 37631,
        "source_m": 205329,
        "hypothetical_n": 37633,
        "full_satN1_candidates": []
      },
      {
        "target_Delta": 12,
        "target_D": 5,
        "source_n": 42402,
        "source_m": 245937,
        "hypothetical_n": 42404,
        "full_satN1_candidates": [
          28565,
          36331
        ]
      }
    ],
    "rule": "Chooseoldedgeuv;addadjacentuprime/vprime;copyN(u)minusv/N(v)minusu;retainalloldedges",
    "complete_necessary_gate": "Becauseeveryoldvertexhasasaturatedneighbor,legalpairrequiresSatN(u)={v},SatN(v)={u};bothfullsatN1",
    "D12_candidate_endpoints_are_adjacent": false,
    "D12_unique_saturated_neighbor_of_each": 27674,
    "D12_shared_boundary_capacity_blocks": 7,
    "eligible_pairs": 0,
    "candidate_graphs": 0,
    "BFS": 0,
    "R4_checks": 0,
    "solver_calls": 0,
    "CPU_seconds": 0.124853835,
    "status": "COMPLETE_PAIRED_RULE_BLOCKED_BY_DEGREE_AND_OLD_EDGE_BINDING",
    "actual_n": null,
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null
  },
  {
    "label": "accepted37631_cap12_complete_old_neighborhood_integer_clone_capacity_20261030",
    "status": "FIXED_D11_SOURCE_CAP12_COMPLETE_OLD_NEIGHBORHOOD_CLONE_PACKING_CANNOT_BEAT_TARGET",
    "target_Delta": 12,
    "target_D": 5,
    "savedL": 42402,
    "source_n": 37631,
    "source_m": 205329,
    "old_degree_cap": 11,
    "new_degree_cap": 12,
    "scope": "Fixed accepted37631 old graph, preserve all old edges, each new clone contains a complete original open neighborhood, arbitrary nonnegative integer multiplicity and cap12",
    "inherited_every_prototype_has_saturated11_neighbor": true,
    "multiplicity_per_prototype_upper": 1,
    "total_old_pin_capacity": 40914,
    "old_degree11_slack": 3283,
    "weighted_bound": "11 sum(k) <= 40914+3283=44197",
    "clone_count_upper": 4017,
    "final_order_upper": 41648,
    "needed_clones_to_beat42402": 4772,
    "bound_claimed_attainable": false,
    "source_reads": 0,
    "BFS_runs": 0,
    "LP_calls": 0,
    "solver_calls": 0,
    "graph_generations": 0,
    "local_static_proof": true,
    "external_review_status": "NOT_YET_RECORDED",
    "old_cap11_failure_extrapolated": false,
    "extra_new_new_edges_do_not_reduce_old_pin_load": true
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/PREDICTION.json](../../research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/PREDICTION.json)；[research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/RESULT.json](../../research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/RESULT.json)；[research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/REPORT.md](../../research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/REPORT.md)；[research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/SCAN_RESULT.json](../../research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/SCAN_RESULT.json)；[research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/PROFILE_D11.json](../../research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/PROFILE_D11.json)；[research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/PROFILE_D12.json](../../research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/PROFILE_D12.json)；[research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/saturated_neighbor_counts_d11.u8.bin](../../research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/saturated_neighbor_counts_d11.u8.bin)；[research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/saturated_neighbor_counts_d12.u8.bin](../../research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/saturated_neighbor_counts_d12.u8.bin)；[research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/source_degrees_d11.u8.bin](../../research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/source_degrees_d11.u8.bin)；[research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/source_degrees_d12.u8.bin](../../research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/source_degrees_d12.u8.bin)；[research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/scan_once.py](../../research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/scan_once.py)；[research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/TERMINAL.json](../../research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/TERMINAL.json)；[research/ddp/more_graphs_20261027/h9_paired_full_neighborhood_clone_rule/PREDICTION.json](../../research/ddp/more_graphs_20261027/h9_paired_full_neighborhood_clone_rule/PREDICTION.json)；[research/ddp/more_graphs_20261027/h9_paired_full_neighborhood_clone_rule/BINDING_RESULT.json](../../research/ddp/more_graphs_20261027/h9_paired_full_neighborhood_clone_rule/BINDING_RESULT.json)；[research/ddp/more_graphs_20261027/h9_paired_full_neighborhood_clone_rule/REPORT.md](../../research/ddp/more_graphs_20261027/h9_paired_full_neighborhood_clone_rule/REPORT.md)；[research/ddp/more_graphs_20261027/h9_paired_full_neighborhood_clone_rule/prepare_paper_probe.py](../../research/ddp/more_graphs_20261027/h9_paired_full_neighborhood_clone_rule/prepare_paper_probe.py)；[research/ddp/refresh_20261029/d11_to_d12_clone_capacity/PROOF.md](../../research/ddp/refresh_20261029/d11_to_d12_clone_capacity/PROOF.md)；[research/ddp/refresh_20261029/d11_to_d12_clone_capacity/RESULT.json](../../research/ddp/refresh_20261029/d11_to_d12_clone_capacity/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 保留原两源全邻域首点扫描，追加同机制的相邻双原型复制必要门：37631/cap11与42402/cap12；必须旧edge uv且复制双方除对方外的完整N，新增clone间edge，全部旧边保留。旧profile证明各旧vertex至少一满邻，故完整候选只可能互为唯一满邻的full satN1端点；无新距离计算。；新cap迁移另按37631旧源、保全旧边及完整原N(v)整数复制处理：cap12每原型k≤1、总clone≤4017、最终≤41648；不是从旧cap11无首clone直接外推。

**正向保证：** A legal ordinary full-neighborhood clone automatically preserves D5 by the shortest-path first-edge substitution lemma.；Both final actual-source degree profiles were computed completely; degree minima cannot be inferred from completed geometric pools alone.

**仍未完成：** 未排任意partial-neighborhood、guards、不同多helper规则、edgechanges或其它source；本批不触发这些后续。；其他源、改变邻域/删旧边/动态生成或合作改造均不由4017上界排除。

**启发与重启依据：** 同一prototype-neighborhood机制的完整首步/成对合法性检查；共同满邻不能替代互为旧邻的条件，共享free pin也可能只有1slot却承受2load。只关闭这两固定规则；其它协作和edgechanges保持开放，不从minSat见证自动续guard。；停止该固定源cap12完整原邻域packing，不值得再求最大packing；保持原N(v)时添加新新边也不能逃过旧端口负载上界。

**单独的重启条件：** This exact full-N(v) first-step rule is closed on these fixed sources. No automatic deleted-pin or guard continuation from the minimum-saturation witnesses.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

