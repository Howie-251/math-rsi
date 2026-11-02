---
type: experiment
node_id: exp:ddp-stale-d8d4-loz1100-single-split-boundary-20261101
title: "长期8D4=1100拆点迁移：95个唯一首步排全部单root相邻拆分，未生1101图"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/PRED.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/NOTE.md; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/RESULT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/TERMINAL.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/SOURCE_RECIPE_INPUT.json; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/R4_BOUNDARY_SUPPORTS.csv; research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/run_once.py"
added: 2026-11-01T17:57:59Z
tags: ["ddp", "method-ledger"]
---

# 长期8D4=1100拆点迁移：95个唯一首步排全部单root相邻拆分，未生1101图

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** necessary_route_or_input_transfer_gate

**目标与阶数：** (8,4)；L=1100；条件性n=1101（未据此计纪录）

**距目标的证据：** No full target graph was generated; source legality inherited only；实际root0距离层(1,8,56,361,674)；674个R4目标中95个firsthop singleton。target2唯一首步533，旧4路0–533–459–223–2；两侧不能同时分到533，故逻辑排全部254有向／127互补分区，未枚分区、未生1101图。近端≤3可容许一次role-edge插步，不是失败点。

**其他指标（保持原计数类型）：**
```json
{
  "new_graphs": 0,
  "new_parameter_pairs": 0,
  "new_Lean_instances": 0,
  "new_independent_method_claims": 0,
  "source_order": 1100,
  "source_degree": 8,
  "source_D": 4,
  "source_legality": "inherited_not_revalidated",
  "actual_N1": [
    55,
    693,
    606,
    899,
    1045,
    462,
    533,
    246
  ],
  "actual_R4": 674,
  "firsthop_support_size_histogram": {
    "1": 95,
    "2": 226,
    "3": 218,
    "4": 100,
    "5": 28,
    "6": 6,
    "7": 1
  },
  "singleton_target_count": 95,
  "witness": {
    "target": 2,
    "singleton_support_mask": 64,
    "mandatory_firsthop_port": 6,
    "mandatory_first_neighbor": 533,
    "actual_source_four_step_route": [
      0,
      533,
      459,
      223,
      2
    ],
    "obstruction": "The side without this mandatory neighbor has distance at least5 to the target after the split."
  },
  "excluded_oriented_partitions": 254,
  "excluded_complement_classes": 127,
  "partitions_actually_enumerated": 0,
  "new_root0_route_support_calculations": 1,
  "source_allroot_BFS": 0,
  "charged_CPU": 0.116906178,
  "actual_process_CPU": 0.016906178,
  "conservative_preparation_charge": 0.1,
  "CPU_budget": 10,
  "terminal": true
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/PRED.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/PRED.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/NOTE.md](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/NOTE.md)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/RESULT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/RESULT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/SOURCE_RECIPE_INPUT.json](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/SOURCE_RECIPE_INPUT.json)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/R4_BOUNDARY_SUPPORTS.csv](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/R4_BOUNDARY_SUPPORTS.csv)；[research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/run_once.py](../../research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/loz1100_split_gate/run_once.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Only the inherited RIGHT-law C20 semidirect_2 Z55 Loz1100 source. Replace one vertex by two adjacent roles, partition all8old neighbors into nonempty disjoint A/B, freeze all other edges. Cayley translation fixes root0. Not multiple splits or other rewiring.

**仍未完成：** No accepted target graph; broader rules beyond the exact recorded scope remain open.

**启发与重启依据：** STOP this exact single-split source/rule. A further experiment needs changed connection rules, multiple split vertices or another source; do not repeat this root/partition batch.

**单独的重启条件：** STOP this exact single-split source/rule. A further experiment needs changed connection rules, multiple split vertices or another source; do not repeat this root/partition batch.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

