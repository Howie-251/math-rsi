---
type: experiment
node_id: exp:ddp-r6-schreier-fixed-even-deck-a3-capacity34-gaussian-obstruction-20261101
title: "固定六port三base拓扑A³覆盖：符号36型与Gaussian字符排m36，evenm≤34"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: yes
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/symbolic_capacity/PRED.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/symbolic_capacity/RESULT.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/symbolic_capacity/check_residues.py; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/symbolic_capacity/DISTINCT_1_TO_2_FORMS.tsv; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/symbolic_capacity/INDEPENDENT_PAPER_CHECK.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/symbolic_capacity/INDEPENDENT_PAPER_RESULT.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/symbolic_capacity/check_symbolic_identity_independent.py; research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/PROOF.md"
added: 2026-11-01T08:44:42Z
tags: ["ddp", "method-ledger"]
---

# 固定六port三base拓扑A³覆盖：符号36型与Gaussian字符排m36，evenm≤34

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** controller

**目标与阶数：** (54,3)；L=不适用／见变体

**距目标的证据：** Local necessary upper bound for fullA³ coverage of one fixed six-port/3base/even cyclic-deck topology; not an actual graph diameter or general6D3bound.；固定六port逐base规则的K³符号型计数独立核为40/46/46,46/38/36,46/36/38，完整A³覆盖先必要m≤36。事前预测m36的36型须模4每桶9，原1024profiles全失败，mod2仍16/32、mod3仍36/243。随后从实际port矩阵独立分解36型为8+4+12+12，h18≡2；一次和强制τ−σ odd，平方和强制α1/α2不全偶，在i处六行Gaussian case的字符和均非0，短证排m36。因此evenm≤34/controller3m≤102，仅固定topology+A³；不是新完整图、一般degree6D3上界或Lean定理。root小余数CPU.037925631，独立符号代数CPU.001513766，0新图/BFS/solver/Lean。

**其他指标（保持原计数类型）：**
```json
{
  "new_named_complete_graphs": 0,
  "new_Lean_instances": 0,
  "new_frameworks": 0,
  "local_paper_result": true,
  "complete_Lean_graph_instance": false,
  "base_pair_type_counts": [
    [
      40,
      46,
      46
    ],
    [
      46,
      38,
      36
    ],
    [
      46,
      36,
      38
    ]
  ],
  "initial_even_m_upper": 36,
  "final_even_m_upper": 34,
  "A3_compatible_controller_order_upper": 102,
  "m34_existence_claimed": false,
  "general_degree6_D3_upper_claimed": false,
  "m36_half_mod4": 2,
  "m36_uniform_mod4_required": [
    9,
    9,
    9,
    9
  ],
  "root_mod4_profiles": 1024,
  "root_mod4_balanced": 0,
  "root_mod2_balanced_profiles": [
    16,
    32
  ],
  "root_mod3_balanced_profiles": [
    36,
    243
  ],
  "root_profile_CPU": 0.037925631,
  "independent_symbolic_CPU": 0.001513766,
  "independent_profile_searches": 0,
  "independent_support_blocks": [
    8,
    4,
    12,
    12
  ],
  "independent_Gaussian_case_rows": 6,
  "new_controller_fiber_BFS_solver_Lean_runs": 0,
  "source_controller_node": "ddp-r6-schreier3base-z26-sixport-controller78-complete-a3-20261101",
  "future_decision": "skip fixed-topology evenm>=36; no currentm34search",
  "current_priority": "finish54/55closedconcreteLean/finalreviews"
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/symbolic_capacity/PRED.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/symbolic_capacity/PRED.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/symbolic_capacity/RESULT.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/symbolic_capacity/RESULT.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/symbolic_capacity/check_residues.py](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/symbolic_capacity/check_residues.py)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/symbolic_capacity/DISTINCT_1_TO_2_FORMS.tsv](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/symbolic_capacity/DISTINCT_1_TO_2_FORMS.tsv)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/symbolic_capacity/INDEPENDENT_PAPER_CHECK.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/symbolic_capacity/INDEPENDENT_PAPER_CHECK.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/symbolic_capacity/INDEPENDENT_PAPER_RESULT.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/symbolic_capacity/INDEPENDENT_PAPER_RESULT.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/symbolic_capacity/check_symbolic_identity_independent.py](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/symbolic_capacity/check_symbolic_identity_independent.py)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/PROOF.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/PROOF.md)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定三base×Z_m，m偶数、h=m/2；a+为0→0+A,1→2+B,2→1+C，a−真逆；b±为base三cycle零shift；s交换0/1并±S、base2自移h；t交换0/2并±T、base1自移h。A,B,C,S,T任意合法电压，不沿用m26的两单位轨归一作其他m的WLOG。要求所有有序控制点对有长度恰3的walk，即A³entrywisepositive。

**正向保证：** 36型从实际port Laurent矩阵K³独立推得，仅用2h=0，精确匹配保存36行TSV；同型碰撞只会减少覆盖，不会突破m≤36。；m36均匀模4必要：sum f≡2(T−S)，sum f²≡2(B²+C²+BC+ST)；继而S/T异奇偶、B/C不全偶。；六行Gaussian整数表及共轭覆盖全部x=i^B,y=i^C至少一非实的情况；偶S/T≡2时q/2−u非0，偶S/T≡0时k(1±i)+(q/2+u)不能相消，k∈{1,−1,−3}。与9(1+i−1−i)=0矛盾，不依赖profile枚举作最终证明。；当前full9line/nointrafiber F9³lift若缺非邻层3walk，最多6*81=486<729点；所以此A³必要界也适用于该固定lift模型。此处接口必要性直接继承，不登记为新认识。

**仍未完成：** m34是否可行未判定；没有controller102或74358点目标图。其他port拓扑、intrafiber边和一般degree6/D3图未排；单纯controller D≤3不自动等价A³>0。未做Lean形式化，无全球新下界／新framework。

**启发与重启依据：** 九basepair符号计数是先读原表后的发现，非事前预测；随后PRED预期m36模4必要域为空获支持，再用独立短字符证明解释重复结构障碍。未来在本固定A³拓扑跳过evenm≥36；当前不启动m34等参数搜索，仍先闭54/55具体Lean及最终外审。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

