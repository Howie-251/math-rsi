---
type: experiment
node_id: exp:ddp-d10-dhar-source25-quadratic101-20261027
title: "C25/F101源二次规则20作用：薄层预测支持，完整覆盖无命中"
idea_id: "idea:ddp-breadth-20261027"
verdict: no
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d10_dhar2485_transfer/QUOTIENT25_PREDICTION.json; research/ddp/more_graphs_20261027/d10_dhar2485_transfer/QUOTIENT25_RESULT.json; research/ddp/more_graphs_20261027/d10_dhar2485_transfer/quotient25.py; research/ddp/more_graphs_20261027/d10_dhar2485_transfer/EXPERIMENT_CODE_REVIEW.md"
added: 2026-10-27T15:10:07Z
tags: ["ddp", "method-ledger"]
---

# C25/F101源二次规则20作用：薄层预测支持，完整覆盖无命中

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** finite-cayley-route-coverage-no-accepted-graph

**目标与阶数：** (10,4)；L=2485；条件性n=2525（未据此计纪录）

**距目标的证据：** P2最薄路线数>215得到支持：实际308。20项全部检查25层，代表根R4遗漏52..192；0完整新图，未测普通全图坏对或实际D。

**其他指标（保持原计数类型）：**
```json
{
  "complete_action_count": 20,
  "min_raw_word_count": 308,
  "route_count_prediction_supported": true,
  "new_graphs_generated": 0,
  "representative_root_missing_min": 52,
  "representative_root_missing_max": 192,
  "CPU_seconds": 0.061650158000000004,
  "old_source_BFS": 0
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d10_dhar2485_transfer/QUOTIENT25_PREDICTION.json](../../research/ddp/more_graphs_20261027/d10_dhar2485_transfer/QUOTIENT25_PREDICTION.json)；[research/ddp/more_graphs_20261027/d10_dhar2485_transfer/QUOTIENT25_RESULT.json](../../research/ddp/more_graphs_20261027/d10_dhar2485_transfer/QUOTIENT25_RESULT.json)；[research/ddp/more_graphs_20261027/d10_dhar2485_transfer/quotient25.py](../../research/ddp/more_graphs_20261027/d10_dhar2485_transfer/quotient25.py)；[research/ddp/more_graphs_20261027/d10_dhar2485_transfer/EXPERIMENT_CODE_REVIEW.md](../../research/ddp/more_graphs_20261027/d10_dhar2485_transfer/EXPERIMENT_CODE_REVIEW.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** ExactlyC25/F101,phases1/3/6/7/9,translations[0,r²−1,−r²−1,−r,1];all20primitive25actions.

**仍未完成：** 未取得此参数的完整新纪录；其它作用、相位及一般图未由此排除。完整Lean实例仍0。

**启发与重启依据：** 词数余量确实改善，固定多项式同时绑住两组补位变量却仍失败；选maxminfreecapacity的最小r25，只作一个完整射影参数决策，不按最少遗漏选r80。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

