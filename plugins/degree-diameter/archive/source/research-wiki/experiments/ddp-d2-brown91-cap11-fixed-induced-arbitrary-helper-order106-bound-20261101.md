---
type: experiment
node_id: exp:ddp-d2-brown91-cap11-fixed-induced-arbitrary-helper-order106-bound-20261101
title: "Brown91升cap11任意helper：107被逐组路线容量与奇偶矛盾排除"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/PRED.json; research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/PROOF.md; research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/RESULT.json; research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/COHORT_RESULT.json; research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/INTEGER_RESULT.json; research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/TERMINAL.json; research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/pin_profiles/RESULT.json"
added: 2026-11-01T08:29:56Z
tags: ["ddp", "method-ledger"]
---

# Brown91升cap11任意helper：107被逐组路线容量与奇偶矛盾排除

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** necessary_or_symbolic_model

**目标与阶数：** (11,2)；L=106

**距目标的证据：** 旧Brown91诱导图完全固定，不增加或修改old-old边；任意新点、任意old-helper与helper-helper边，H无clique或正则假设。；初步h≤16/order≤107、B96..101；GF9几何93002 line/pin pairs、175profiles和小DP提出cohort缺口。最终解析每组ed−δ≤4s−a−24，求和≤3(B−101)≤0，必要条件强制B101、全部helper满度，合度176−101=75odd矛盾。因此h≤15/order≤106，与公开106相同；不声称106构造存在或一般N(11,2)上界。accounted2.016578981CPU，0图/BFS/solver/Lean。

**其他指标（保持原计数类型）：**
```json
{
  "new_named_complete_graphs": 0,
  "new_Lean_instances": 0,
  "source_n": 91,
  "target_cap": 11,
  "helper_upper": 15,
  "order_upper": 106,
  "public_order": 106,
  "new_graphs": 0,
  "solver_calls": 0,
  "old_n61_queue_restarted": false,
  "accounted_CPU": 2.016578981,
  "independent_paper_attack": "PASS"
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/PRED.json](../../research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/PRED.json)；[research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/PROOF.md](../../research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/PROOF.md)；[research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/RESULT.json](../../research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/RESULT.json)；[research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/COHORT_RESULT.json](../../research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/COHORT_RESULT.json)；[research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/INTEGER_RESULT.json](../../research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/INTEGER_RESULT.json)；[research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/pin_profiles/RESULT.json](../../research/ddp/two_successful_methods_20261101/d2_spare_dominating_fill/brown91_cap11_interface/pin_profiles/RESULT.json)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 旧Brown91诱导图完全固定，不增加或修改old-old边；任意新点、任意old-helper与helper-helper边，H无clique或正则假设。

**正向保证：** 所有旧点都必须被pin，81个非绝对点各有唯一owner；内部owner≤6pins、外部≤8pins；绝对点数量计入逐组线路覆盖。；最终是解析整数不等式与奇偶链；profiles/DP用于发现和核对，不把必要条件DP命中当图。

**仍未完成：** 改old-old边、其他source／cap及一般11度D2图未排。

**启发与重启依据：** 目标107的放宽容量最初可行，加入同时实现的routecohort后只有B101边界，再由helper度奇偶推翻；停止固定source操作，不继续强化h15或q梯子。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

