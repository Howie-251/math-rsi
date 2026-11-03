---
type: experiment
node_id: exp:ddp-stale-d3d5-afy70-threecut-twohelpers-repair-20261101
title: "3D5旧70源三匹配删边加两helper：非邻规则全NO；邻接加oldrepair修互距但168案损旧路线"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/PROOF.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/adjacent_helpers_repair/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/adjacent_helpers_repair/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/adjacent_helpers_repair/PROOF.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/adjacent_helpers_repair/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/adjacent_helpers_repair/TERMINAL.json"
added: 2026-11-01T17:57:59Z
tags: ["ddp", "method-ledger"]
---

# 3D5旧70源三匹配删边加两helper：非邻规则全NO；邻接加oldrepair修互距但168案损旧路线

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** necessary_route_or_input_transfer_gate

**目标与阶数：** (3,5)；L=70；条件性n=72（未据此计纪录）

**距目标的证据：** No full target graph was generated; source legality inherited only；第一规则166390匹配×10=1663900配置全遍；1663872先漏helper70→old，余28虽到全old≤5却helper互距6。新相邻helper＋oldrepair规则真实修复互距，2455530合法repair×3=7366590全遍：7365708漏helper70old、714漏helper71old；168案两helper到全old≤5且互距1，但全部old-old仍>5。首例cutIDs[0,5,7]、repair(0,4)、pins70[1,3]/71[2,56]留下oldpair(0,17)。不是未执行oldold检查就推NO。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "first_rule": {
    "status": "EXHAUSTIVE_FIXED_RULE_NO72",
    "matchings": 166390,
    "configurations": 1663900,
    "first_failure_counts": {
      "helper70_old_R5": 1663872,
      "helper_pair_R5": 28,
      "helper71_old_R5": 0,
      "old_old_R5": 0
    },
    "remaining_helper_pair_distance": 6,
    "old_R4_union_is_diagnostic_not_necessary_filter": true,
    "exact_check_scope": {
      "new_helper70_radius5_checks": 1663900,
      "new_helper71_radius5_checks": 0,
      "old_old_radius5_checks": 0,
      "full72root_batches": 0,
      "source_radius4_diagnostic_roots": 70,
      "source_validity_or_source_D5_BFS_roots": 0
    }
  },
  "adjacent_repair_rule": {
    "status": "EXHAUSTIVE_FIXED_ADJACENT_REPAIR_RULE_NO72",
    "matchings": 166390,
    "valid_repair_choices": 2455530,
    "rejected_duplicate_repairs": 40320,
    "configurations": 7366590,
    "first_failure_counts": {
      "helper70_old_R5": 7365708,
      "helper71_old_R5": 714,
      "old_old_R5": 168
    },
    "both_helpers_all_old_PASS": 168,
    "all_remaining_old_old_rejected": 168,
    "first_old_failure": {
      "pair": [
        0,
        17
      ],
      "cut_edge_ids": [
        0,
        5,
        7
      ],
      "repair": [
        0,
        4
      ],
      "pins70": [
        1,
        3
      ],
      "pins71": [
        2,
        56
      ]
    }
  },
  "cumulative_measured_CPU": 4.660693,
  "CPU_budget": 20,
  "CPU_accounting_note": "one CPU second reserved for preceding brief code/PRED preparation and final receipts; these operations not individually metered",
  "source_validity_D5_BFS_repeated": false,
  "full72root_batches": 0,
  "new_helper_route_tests_are_candidate_gate_not_source_reverification": true,
  "terminal": true
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/PROOF.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/PROOF.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/adjacent_helpers_repair/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/adjacent_helpers_repair/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/adjacent_helpers_repair/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/adjacent_helpers_repair/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/adjacent_helpers_repair/PROOF.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/adjacent_helpers_repair/PROOF.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/adjacent_helpers_repair/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/adjacent_helpers_repair/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/adjacent_helpers_repair/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/adjacent_helpers_repair/TERMINAL.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** One fixed literal AFY70 cubic/D5 source. Rule1 deletes exactly3disjoint old edges, adds2nonadjacent helpers and partitions6endpoints3+3. Rule2 uses the same3matching cuts, one nondouble old-old endpoint repair, partitions remaining4endpoints2+2 between adjacent helpers. No other edge edits or source changes.

**仍未完成：** No accepted target graph; broader rules beyond the exact recorded scope remain open.

**启发与重启依据：** STOP both fixed AFY70 patterns; no further timer or nearby repair batch. Future research requires a changed structural premise or another source and must preserve the distinction between helper coverage and old-old damage.

**单独的重启条件：** STOP both fixed AFY70 patterns; no further timer or nearby repair batch. Future research requires a changed structural premise or another source and must preserve the distinction between helper coverage and old-old damage.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

