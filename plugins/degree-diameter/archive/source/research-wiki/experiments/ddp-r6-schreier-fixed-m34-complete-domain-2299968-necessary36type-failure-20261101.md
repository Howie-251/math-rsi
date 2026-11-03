---
type: experiment
node_id: exp:ddp-r6-schreier-fixed-m34-complete-domain-2299968-necessary36type-failure-20261101
title: "固定Z34六port三base完整门：2299968合法参数全败于真实36型1→2首门"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/PRED.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/PROOF.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/RESULT.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/TERMINAL.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/NORMALIZATION_AND_DOMAIN.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/SEARCH_RESULT.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/GATE_1_TO_2_FORMS.tsv; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/WALK_LINEAR_FORMS.tsv; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/search.cpp; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/run_once.py; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/compile.log; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/search.log"
added: 2026-11-01T08:57:12Z
tags: ["ddp", "method-ledger"]
---

# 固定Z34六port三base完整门：2299968合法参数全败于真实36型1→2首门

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** controller

**目标与阶数：** (54,3)；L=不适用／见变体

**距目标的证据：** Fixed threebase/sixport/Z34 complete voltage domain fails necessary base1→2 threewalk coverage; no actualcontroller or fibergraph constructed.；α0∉{0,17}经16单位唯一归一1/2，其余四params1..33、α1+α2≠0。raw2371842/合法2299968两branch各1149984完整终态，0未试、末tuple(2,33,33,33,33)。所有项均在真实36型base1→2的34bit mask必要首门失败，survivor0；所以实际其余class展开0次，不冒完整A³验证或witness。总.893814463CPU（含prep/compile/driver，搜索.150192），0controller/fiber/BFS/solver/Lean，非UNKNOWN。

**其他指标（保持原计数类型）：**
```json
{
  "new_named_complete_graphs": 0,
  "new_Lean_instances": 0,
  "new_frameworks": 0,
  "m": 34,
  "controller_candidate_order": 102,
  "normalized_alpha0": [
    1,
    2
  ],
  "raw_normalized_domain": 2371842,
  "valid_normalized_domain": 2299968,
  "branch_tested": [
    1149984,
    1149984
  ],
  "untested": 0,
  "necessary_symbolic_types": 36,
  "necessary_gate_passed": 0,
  "full_three_root_masks": 0,
  "controller_generated": false,
  "fiber_generated": false,
  "BFS_solver_Lean": 0,
  "total_CPU": 0.893814463,
  "search_CPU": 0.150192,
  "all_jobs_terminal": true,
  "combined_remaining_even_m_upper": 32,
  "next_m32_or30_dispatched": false,
  "parent_capacity_node": "ddp-r6-schreier-fixed-even-deck-a3-capacity34-gaussian-obstruction-20261101"
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/PRED.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/PRED.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/PROOF.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/PROOF.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/RESULT.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/RESULT.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/NORMALIZATION_AND_DOMAIN.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/NORMALIZATION_AND_DOMAIN.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/SEARCH_RESULT.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/SEARCH_RESULT.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/GATE_1_TO_2_FORMS.tsv](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/GATE_1_TO_2_FORMS.tsv)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/WALK_LINEAR_FORMS.tsv](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/WALK_LINEAR_FORMS.tsv)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/search.cpp](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/search.cpp)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/run_once.py](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/run_once.py)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/compile.log](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/compile.log)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/search.log](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier102_controller_gate/search.log)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 只限已列固定a±/b±/s/t三base拓扑、Z34、half17，全部合法电压由单位归一覆盖；要求A³逐项正。对应full9line/nointrafiber F9³lift也受此必要门限制。不是一般102点6度D3控制器、其他port拓扑或intrafiber模型的排除。

**正向保证：** 独立核算34=2*17，32合法α0分两个16元单位轨，奇单位保h17与b零电压。每branch33^4−33^3=1149984，未归一36799488合法项由单位轨覆盖，未声称逐枚未归一域。；36型来自实际648三port线性词，只合2h=0；若首门不覆盖34个余数，其他basepair词不能修复该1→2缺项，是严格必要失败。；首门一项不通过，故完整A³成功候选0，不必重复其余class；计数/精确前缀和原日志保存。

**仍未完成：** 其他evenm/port拓扑/一般6D3开放。结合此前evenm≤34容量界，现同一完整A³固定族剩余evenm≤32；不声称32可行，不派32/30搜索，无新完整图／Lean／framework。

**启发与重启依据：** 先前m36的短字符界将最高未排参数定位m34；root在旧54/55形式化收尾后新授权唯一m34完整门，覆盖此前临时等待。全域首门失败支持此范围停止，不据局部缺项下降续算；当前只完成旧四图最终外审/交付，不接m32/30或换拓扑梯子。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

