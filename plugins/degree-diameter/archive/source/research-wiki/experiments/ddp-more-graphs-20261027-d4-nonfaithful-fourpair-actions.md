---
type: experiment
node_id: exp:ddp-more-graphs-20261027-d4-nonfaithful-fourpair-actions
title: "p61四逆对pattern的剩余11actions：532薄层幸存仍0完整命中"
idea_id: "idea:ddp-breadth-20261027"
verdict: partial
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d4_source_transfer/nonfaithful_actions/REPORT.md; research/ddp/more_graphs_20261027/d4_source_transfer/nonfaithful_actions/RESULT.json; research/ddp/more_graphs_20261027/d4_source_transfer/nonfaithful_actions/PREDICTION.json; research/ddp/more_graphs_20261027/d4_source_transfer/nonfaithful_actions/CAPACITY.json; research/ddp/more_graphs_20261027/d4_source_transfer/nonfaithful_actions/ENUMERATION.json; research/ddp/more_graphs_20261027/d4_source_transfer/nonfaithful_actions/enumerate.cpp"
added: 2026-10-27T14:08:25Z
tags: ["ddp", "method-ledger"]
---

# p61四逆对pattern的剩余11actions：532薄层幸存仍0完整命中

**verdict:** `partial`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** complete-nonfaithful-action-capacity-and-free-translation-screen

**目标与阶数：** (8,4)；L=1100；条件性n=1220（未据此计纪录）；从属目标：[[8, 4]]

**距目标的证据：** No graphgenerated. Actionfreeform capacity thenidentityorigin endpointcoverage;phase10survivorsnotwholegraphbadpairs. Otherphases checkedonlyuntilfirstfailure.；>=1phase10survivor预测获支持：8个allphase-capacity-passedactions的30264项中有532，全部其它phase0/1/2失败。3个actions共11349项容量直接排。r11/50的rawphase10幸存未查，不记0。0图/0完整D4命中。

**其他指标（保持原计数类型）：**
```json
{
  "normalized_scope": 41613,
  "capacity_pruned_cases": 11349,
  "numerically_enumerated_cases": 30264,
  "phase10_survivors_after_allphase_capacity_filter": 532,
  "raw_phase10_survivors_all11": null,
  "raw_phase10_unmeasured_actions": [
    11,
    50
  ],
  "full_hits": 0,
  "new_graphs": 0,
  "native_CPU_seconds": 0.005647,
  "capacity_CPU_seconds": 0.019798330999999995,
  "all_source_BFS": 0,
  "old_primitive_actions_rerun": 0,
  "pending": []
}
```



**从属变体：**
```json
[
  {
    "label": "r3-order10",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "normalized_scope": 3783,
    "cases_enumerated": 3783,
    "capacity_status": "COMPLETE_FREE_PARAMETER_ENUMERATION_NO_FULL_HIT",
    "minimum_capacity": 111,
    "phase10_form_capacity": 111,
    "phase10_numeric_survivors": 112,
    "phase10_count_scope": "Numerically enumerated",
    "full_hits": 0
  },
  {
    "label": "r9-order5",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "normalized_scope": 3783,
    "cases_enumerated": 3783,
    "capacity_status": "COMPLETE_FREE_PARAMETER_ENUMERATION_NO_FULL_HIT",
    "minimum_capacity": 118,
    "phase10_form_capacity": 118,
    "phase10_numeric_survivors": 30,
    "phase10_count_scope": "Numerically enumerated",
    "full_hits": 0
  },
  {
    "label": "r11-order4",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "normalized_scope": 3783,
    "cases_enumerated": 0,
    "capacity_status": "CAPACITY_REJECTED",
    "minimum_capacity": 50,
    "phase10_form_capacity": 66,
    "phase10_numeric_survivors": null,
    "phase10_count_scope": "Notnumericallyenumerated;otherphasecapacityrejectsD4",
    "full_hits": 0
  },
  {
    "label": "r20-order5",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "normalized_scope": 3783,
    "cases_enumerated": 3783,
    "capacity_status": "COMPLETE_FREE_PARAMETER_ENUMERATION_NO_FULL_HIT",
    "minimum_capacity": 110,
    "phase10_form_capacity": 110,
    "phase10_numeric_survivors": 16,
    "phase10_count_scope": "Numerically enumerated",
    "full_hits": 0
  },
  {
    "label": "r27-order10",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "normalized_scope": 3783,
    "cases_enumerated": 3783,
    "capacity_status": "COMPLETE_FREE_PARAMETER_ENUMERATION_NO_FULL_HIT",
    "minimum_capacity": 111,
    "phase10_form_capacity": 111,
    "phase10_numeric_survivors": 108,
    "phase10_count_scope": "Numerically enumerated",
    "full_hits": 0
  },
  {
    "label": "r34-order5",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "normalized_scope": 3783,
    "cases_enumerated": 3783,
    "capacity_status": "COMPLETE_FREE_PARAMETER_ENUMERATION_NO_FULL_HIT",
    "minimum_capacity": 118,
    "phase10_form_capacity": 118,
    "phase10_numeric_survivors": 30,
    "phase10_count_scope": "Numerically enumerated",
    "full_hits": 0
  },
  {
    "label": "r41-order10",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "normalized_scope": 3783,
    "cases_enumerated": 3783,
    "capacity_status": "COMPLETE_FREE_PARAMETER_ENUMERATION_NO_FULL_HIT",
    "minimum_capacity": 111,
    "phase10_form_capacity": 111,
    "phase10_numeric_survivors": 112,
    "phase10_count_scope": "Numerically enumerated",
    "full_hits": 0
  },
  {
    "label": "r50-order4",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "normalized_scope": 3783,
    "cases_enumerated": 0,
    "capacity_status": "CAPACITY_REJECTED",
    "minimum_capacity": 50,
    "phase10_form_capacity": 66,
    "phase10_numeric_survivors": null,
    "phase10_count_scope": "Notnumericallyenumerated;otherphasecapacityrejectsD4",
    "full_hits": 0
  },
  {
    "label": "r52-order10",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "normalized_scope": 3783,
    "cases_enumerated": 3783,
    "capacity_status": "COMPLETE_FREE_PARAMETER_ENUMERATION_NO_FULL_HIT",
    "minimum_capacity": 111,
    "phase10_form_capacity": 111,
    "phase10_numeric_survivors": 108,
    "phase10_count_scope": "Numerically enumerated",
    "full_hits": 0
  },
  {
    "label": "r58-order5",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "normalized_scope": 3783,
    "cases_enumerated": 3783,
    "capacity_status": "COMPLETE_FREE_PARAMETER_ENUMERATION_NO_FULL_HIT",
    "minimum_capacity": 110,
    "phase10_form_capacity": 110,
    "phase10_numeric_survivors": 16,
    "phase10_count_scope": "Numerically enumerated",
    "full_hits": 0
  },
  {
    "label": "r60-order2",
    "target": [
      8,
      4
    ],
    "n": {
      "actual": null,
      "hypothetical": 1220
    },
    "actual_D": null,
    "ordinary_bad_unordered_pairs": null,
    "normalized_scope": 3783,
    "cases_enumerated": 0,
    "capacity_status": "CAPACITY_REJECTED",
    "minimum_capacity": 19,
    "phase10_form_capacity": 19,
    "phase10_numeric_survivors": null,
    "phase10_count_scope": "Certifiedzero byphase10capacity",
    "full_hits": 0
  }
]
```

**原始证据：** [research/ddp/more_graphs_20261027/d4_source_transfer/nonfaithful_actions/REPORT.md](../../research/ddp/more_graphs_20261027/d4_source_transfer/nonfaithful_actions/REPORT.md)；[research/ddp/more_graphs_20261027/d4_source_transfer/nonfaithful_actions/RESULT.json](../../research/ddp/more_graphs_20261027/d4_source_transfer/nonfaithful_actions/RESULT.json)；[research/ddp/more_graphs_20261027/d4_source_transfer/nonfaithful_actions/PREDICTION.json](../../research/ddp/more_graphs_20261027/d4_source_transfer/nonfaithful_actions/PREDICTION.json)；[research/ddp/more_graphs_20261027/d4_source_transfer/nonfaithful_actions/CAPACITY.json](../../research/ddp/more_graphs_20261027/d4_source_transfer/nonfaithful_actions/CAPACITY.json)；[research/ddp/more_graphs_20261027/d4_source_transfer/nonfaithful_actions/ENUMERATION.json](../../research/ddp/more_graphs_20261027/d4_source_transfer/nonfaithful_actions/ENUMERATION.json)；[research/ddp/more_graphs_20261027/d4_source_transfer/nonfaithful_actions/enumerate.cpp](../../research/ddp/more_graphs_20261027/d4_source_transfer/nonfaithful_actions/enumerate.cpp)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Onlyp61,fixedfourinversepairphases1/12/11/16;remaining11nontrivialr^20=1 actions orders2/4/5/10;A0andall3783projectiveB/C/D cases peraction;primitive8notrerun.

**正向保证：** 完成3容量排+8数值actions的全部41613规范scope，不靠近似评分。；与旧8primitive以及r1Lee321合并，精确关闭此固定fourpairphasepattern全部20actions，不是全C61图。

**仍未完成：** Differentgeneratingphasepatterns,otherquotienttypes,otherprimes andgeneraltargetgraphs notexcluded;twoinvolutionexperimentseparate.

**启发与重启依据：** 改变action确实能补单薄层，但这些连接不能同时覆盖所有层。固定allactions已闭，D4计算停止，不扩phase/prime/seed/solver。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

