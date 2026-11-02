---
type: experiment
node_id: exp:ddp-d16-d6-current1793786-source-slack-profile-20261027
title: "Current1793786 five-copy H11compound:8946spares but minSat10, complete-neighborhood clone empty"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d16_D6_current1793786_source/REPORT.md; research/ddp/more_graphs_20261027/d16_D6_current1793786_source/PREDICTION.json; research/ddp/more_graphs_20261027/d16_D6_current1793786_source/SOURCE.json; research/ddp/more_graphs_20261027/d16_D6_current1793786_source/SOURCE_RECEIPT.json; research/ddp/more_graphs_20261027/d16_D6_current1793786_source/SOURCE_PROFILE.json; research/ddp/more_graphs_20261027/d16_D6_current1793786_source/RESULT.json; research/ddp/more_graphs_20261027/d16_D6_current1793786_source/PREPARE_URL_CORRIGENDUM.json; research/ddp/more_graphs_20261027/d16_D6_current1793786_source/profile.cpp; research/ddp/more_graphs_20261027/d16_D6_current1793786_source/run_profile.py; research/ddp/more_graphs_20261027/d16_D6_current1793786_source/prepare_source.py; research/ddp/more_graphs_20261027/d16_D6_current1793786_source/profile.log; research/ddp/more_graphs_20261027/d16_D6_current1793786_source/terminal.json; research/ddp/more_graphs_20261027/d15_D5_current102060_source/LATEST_AUTHOR_README.md; research/ddp/more_graphs_20261027/d15_D5_current102060_source/targeted_source_receipts.json"
added: 2026-10-27T22:40:54Z
tags: ["ddp", "method-ledger"]
---

# Current1793786 five-copy H11compound:8946spares but minSat10, complete-neighborhood clone empty

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** known_source_or_recovery

**目标与阶数：** (16,6)；L=1793786；known_source_or_recovery n=1793786；条件性n=1793787（未据此计纪录）

**距目标的证据：** Actualsimpleundirected1793786/14345738/max16,degree14:154/15:8792/16:1784840;free8946/slots9100. minSatN10 at12prototypes, zeroSatN0/onefault0;thefixedsource whole-open-neighborhood false-twininsertion rule isempty. 0graph/BFS/proxy/guard/solver/newlowerbound.

**其他指标（保持原计数类型）：**
```json
{
  "source_n": 1793786,
  "source_m": 14345738,
  "source_reported_D": 6,
  "source_degree_histogram": {
    "14": 154,
    "15": 8792,
    "16": 1784840
  },
  "free_vertices": 8946,
  "free_slots": 9100,
  "minSatN": 10,
  "minSatN_count": 12,
  "minimum_prototype_labels": [
    324705,
    532599,
    638606,
    650568,
    665807,
    1323761,
    1363050,
    1395560,
    1626440,
    1690254,
    1715149,
    1749783
  ],
  "zeroSatN_count": 0,
  "onefault_count": 0,
  "native_profile_CPU_seconds": 2.76847,
  "compile_CPU_seconds": 0.700083,
  "profile_parent_children_CPU_seconds": 3.502249,
  "decompression_CPU_seconds": 4.784264027,
  "profile_plus_decompression_CPU_seconds": 8.286513027,
  "download_wall_seconds": 117.39073020964861,
  "source_all_roots_BFS_repeated": 0,
  "candidate_graphs": 0,
  "partial_proxy_or_guard_search": 0,
  "solver": 0,
  "ordinary_bad_pairs": null,
  "prediction": "REFUTED",
  "UNKNOWN": 0,
  "new_lower_bounds": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d16_D6_current1793786_source/REPORT.md](../../research/ddp/more_graphs_20261027/d16_D6_current1793786_source/REPORT.md)；[research/ddp/more_graphs_20261027/d16_D6_current1793786_source/PREDICTION.json](../../research/ddp/more_graphs_20261027/d16_D6_current1793786_source/PREDICTION.json)；[research/ddp/more_graphs_20261027/d16_D6_current1793786_source/SOURCE.json](../../research/ddp/more_graphs_20261027/d16_D6_current1793786_source/SOURCE.json)；[research/ddp/more_graphs_20261027/d16_D6_current1793786_source/SOURCE_RECEIPT.json](../../research/ddp/more_graphs_20261027/d16_D6_current1793786_source/SOURCE_RECEIPT.json)；[research/ddp/more_graphs_20261027/d16_D6_current1793786_source/SOURCE_PROFILE.json](../../research/ddp/more_graphs_20261027/d16_D6_current1793786_source/SOURCE_PROFILE.json)；[research/ddp/more_graphs_20261027/d16_D6_current1793786_source/RESULT.json](../../research/ddp/more_graphs_20261027/d16_D6_current1793786_source/RESULT.json)；[research/ddp/more_graphs_20261027/d16_D6_current1793786_source/PREPARE_URL_CORRIGENDUM.json](../../research/ddp/more_graphs_20261027/d16_D6_current1793786_source/PREPARE_URL_CORRIGENDUM.json)；[research/ddp/more_graphs_20261027/d16_D6_current1793786_source/profile.cpp](../../research/ddp/more_graphs_20261027/d16_D6_current1793786_source/profile.cpp)；[research/ddp/more_graphs_20261027/d16_D6_current1793786_source/run_profile.py](../../research/ddp/more_graphs_20261027/d16_D6_current1793786_source/run_profile.py)；[research/ddp/more_graphs_20261027/d16_D6_current1793786_source/prepare_source.py](../../research/ddp/more_graphs_20261027/d16_D6_current1793786_source/prepare_source.py)；[research/ddp/more_graphs_20261027/d16_D6_current1793786_source/profile.log](../../research/ddp/more_graphs_20261027/d16_D6_current1793786_source/profile.log)；[research/ddp/more_graphs_20261027/d16_D6_current1793786_source/terminal.json](../../research/ddp/more_graphs_20261027/d16_D6_current1793786_source/terminal.json)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/LATEST_AUTHOR_README.md](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/LATEST_AUTHOR_README.md)；[research/ddp/more_graphs_20261027/d15_D5_current102060_source/targeted_source_receipts.json](../../research/ddp/more_graphs_20261027/d15_D5_current102060_source/targeted_source_receipts.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** Actualcurrent1793786literal only, fromexactauthor23691325filename. Onecomplete degree/free/saturated-neighborprofile; no sourceD6BFS orcandidate. Distinctfive-H11-copy compoundfromdegree13H9control. Older1790870/1783834/1779528sources notsubstituted.

**仍未完成：** Arbitrarydegree16monotone-neighborhood extensions,rewiring,othercompoundparameters andgeneralN(16,6) are notexcluded. CompactT5recipe/currentgeometriccoordinates were not recovered;onlycurrentliteral/authorconstructiondescription arebound.

**启发与重启依据：** Actualsparecount doesnotpredictanavailablecomplete-neighborhood clone. Thisdifferentcompound has everyprototype adjacenttoatleast10fullvertices, so successfulzero/onefault rulescannotbe transferred directly. Stop atthisstructure result; do notweakenproxy orstartguardladders. Restartonlywithasubstantivelydifferentroute/augmentation mechanism.

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

