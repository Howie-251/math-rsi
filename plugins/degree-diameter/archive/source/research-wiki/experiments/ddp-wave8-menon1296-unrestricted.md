---
type: experiment
node_id: exp:ddp-wave8-menon1296-unrestricted
title: "Menon1296：96独立S36混类置换有限试验"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/breadth_20261027_wave8/menon1296_unrestricted/REPORT.md; research/ddp/breadth_20261027_wave8/menon1296_unrestricted/best.edges; research/ddp/breadth_20261027_wave8/menon1296_unrestricted/best.independent_check.json; research/ddp/breadth_20261027_wave8/menon1296_unrestricted/best_pi.json; research/ddp/breadth_20261027_wave8/menon1296_unrestricted/best_score.json; research/ddp/breadth_20261027_wave8/menon1296_unrestricted/first_proposal_calibration.json; research/ddp/breadth_20261027_wave8/menon1296_unrestricted/run.py; research/ddp/breadth_20261027_wave8/menon1296_unrestricted/search.cpp; research/ddp/breadth_20261027_wave8/menon1296_unrestricted/search_result.json; research/ddp/breadth_20261027_wave8/menon1296_unrestricted/structure.json; research/ddp/breadth_20261027_wave8/menon1296_unrestricted/terminal.json"
added: 2026-10-27T08:25:53Z
tags: ["ddp", "method-ledger"]
---

# Menon1296：96独立S36混类置换有限试验

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (8,4)；L=1100；candidate_graph_or_family n=1296；条件性n=1296（未据此计纪录）

**距目标的证据：** 实际D=5，目标D=4；普通无序坏对=69737；saved_explicit_graph；最佳图root唯一全1296源确认D5、69737个>4无序对。

**其他指标（保持原计数类型）：**
```json
{
  "legal_proposals": 2000,
  "bad_layers": {
    "AA": 91,
    "AC": 15253,
    "AB": 2296,
    "CC": 3841,
    "BC": 40661,
    "BB": 7595
  }
}
```





**原始证据：** [research/ddp/breadth_20261027_wave8/menon1296_unrestricted/REPORT.md](../../research/ddp/breadth_20261027_wave8/menon1296_unrestricted/REPORT.md)；[research/ddp/breadth_20261027_wave8/menon1296_unrestricted/best.edges](../../research/ddp/breadth_20261027_wave8/menon1296_unrestricted/best.edges)；[research/ddp/breadth_20261027_wave8/menon1296_unrestricted/best.independent_check.json](../../research/ddp/breadth_20261027_wave8/menon1296_unrestricted/best.independent_check.json)；[research/ddp/breadth_20261027_wave8/menon1296_unrestricted/best_pi.json](../../research/ddp/breadth_20261027_wave8/menon1296_unrestricted/best_pi.json)；[research/ddp/breadth_20261027_wave8/menon1296_unrestricted/best_score.json](../../research/ddp/breadth_20261027_wave8/menon1296_unrestricted/best_score.json)；[research/ddp/breadth_20261027_wave8/menon1296_unrestricted/first_proposal_calibration.json](../../research/ddp/breadth_20261027_wave8/menon1296_unrestricted/first_proposal_calibration.json)；[research/ddp/breadth_20261027_wave8/menon1296_unrestricted/run.py](../../research/ddp/breadth_20261027_wave8/menon1296_unrestricted/run.py)；[research/ddp/breadth_20261027_wave8/menon1296_unrestricted/search.cpp](../../research/ddp/breadth_20261027_wave8/menon1296_unrestricted/search.cpp)；[research/ddp/breadth_20261027_wave8/menon1296_unrestricted/search_result.json](../../research/ddp/breadth_20261027_wave8/menon1296_unrestricted/search_result.json)；[research/ddp/breadth_20261027_wave8/menon1296_unrestricted/structure.json](../../research/ddp/breadth_20261027_wave8/menon1296_unrestricted/structure.json)；[research/ddp/breadth_20261027_wave8/menon1296_unrestricted/terminal.json](../../research/ddp/breadth_20261027_wave8/menon1296_unrestricted/terminal.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 全部96incidence独立S36；两固定seed各1000合法transpositions

**正向保证：** simple8regular connected；samepointAA≤2,AC≤3,CC≤4在最终检查兑现；第一swap完整6066576短walk校准MATCH

**仍未完成：** 跨point AC及其他层远端尚缺；没有一般S36不可能性结论。

**启发与重启依据：** 固定profile停止，不加πmoves/seeds/H自由度或类修补。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

