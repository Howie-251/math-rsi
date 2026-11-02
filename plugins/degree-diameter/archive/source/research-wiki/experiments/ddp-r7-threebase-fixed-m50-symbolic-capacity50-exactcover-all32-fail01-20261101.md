---
type: experiment
node_id: exp:ddp-r7-threebase-fixed-m50-symbolic-capacity50-exactcover-all32-fail01-20261101
title: "固定三base七port m50严格闭域：26+3×8支持，32tiling全缺0→1路线"
idea_id: "idea:ddp-open-parameter-construction-20261026"
verdict: no
confidence: high
date: "2026-11-01"
hardware: ""
duration: ""
provenance: "research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/PRED.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/SYMBOLIC_RESULT.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/M50_RESIDUE_RESULT.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/DISTINCT_FORMS.tsv; research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/INDEPENDENT_M50_NOTE.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/PRED.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/PROOF.md; research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/RESULT.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/TERMINAL.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/SYMBOLIC_IDENTITY_RESULT.json; research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/check_symbolic_identity.py; research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/gate.cpp; research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/run_gate.py"
added: 2026-11-01T09:45:01Z
tags: ["ddp", "method-ledger"]
---

# 固定三base七port m50严格闭域：26+3×8支持，32tiling全缺0→1路线

**verdict:** `no`  ·  **confidence:** `high`  ·  tests `idea:ddp-open-parameter-construction-20261026`

## Metrics
**对象层级：** controller

**目标与阶数：** (77,3)；L=不适用／见变体；条件性n=199650（未据此计纪录）

**距目标的证据：** 固定三baseA/B/S/T/R、simple七port、m50完整A³严格排除；fullF11³无intrafi边lift亦失败，非一般7D3上界。；R只base0 half、交换base1/2避旧S/T重复。实际1029词counts=[[50,64,64],[64,52,56],[64,56,52]]，只该topology evenm≤50。m50 root00必须50型无重复，独立symbolicidentity给26base+三8块；a0归一2/10，d三值排序保图。4802outer全域、844可行base、3736blocks、8140pairnodes，32root00tiling全在0→1失败，0未试/0完整controller。含prepare/编译/identity .919086454CPU。

**其他指标（保持原计数类型）：**
```json
{
  "new_named_complete_graphs": 0,
  "new_Lean_instances": 0,
  "new_frameworks": 0,
  "full_graphs_generated": 0,
  "BFS_runs": 0,
  "Lean_compilations": 0,
  "symbolic_words": 1029,
  "symbolic_counts": [
    [
      50,
      64,
      64
    ],
    [
      64,
      52,
      56
    ],
    [
      64,
      56,
      52
    ]
  ],
  "fixed_topology_even_m_bound": 50,
  "fixed_topology_controller_bound": 150,
  "outer_visited": 4802,
  "outer_total": 4802,
  "root00_tilings": 32,
  "full_support_tests": 32,
  "first_failure_pair": [
    0,
    1
  ],
  "passing_controllers": 0,
  "unvisited": 0,
  "accounted_CPU_seconds": 0.919086454,
  "old_mod10_OPEN_superseded": true,
  "smaller_even_m_remaining_upper": 48,
  "automatic_lower_modulus_authorized": false,
  "all_processes_terminal": true
}
```





**原始证据：** [research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/PRED.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/PRED.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/SYMBOLIC_RESULT.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/SYMBOLIC_RESULT.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/M50_RESIDUE_RESULT.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/M50_RESIDUE_RESULT.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/DISTINCT_FORMS.tsv](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/DISTINCT_FORMS.tsv)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/INDEPENDENT_M50_NOTE.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/INDEPENDENT_M50_NOTE.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/PRED.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/PRED.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/PROOF.md](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/PROOF.md)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/RESULT.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/RESULT.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/TERMINAL.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/TERMINAL.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/SYMBOLIC_IDENTITY_RESULT.json](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/SYMBOLIC_IDENTITY_RESULT.json)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/check_symbolic_identity.py](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/check_symbolic_identity.py)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/gate.cpp](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/gate.cpp)；[research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/run_gate.py](../../research/ddp/two_successful_methods_20261101/affine_field_conditions/r7_schreier_controller_gate/m50_exact_cover/run_gate.py)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 仅此三base拓扑m50、simple和完整A³；旧mod10 passingprofile是必要门旧OPEN，已被本次完整exactcover严格终态覆盖。smaller evenm≤48开放，无自动48/46/44梯子；非所有七port或其他F11机制排除。

**正向保证：** 事前symbolic最小>36获支持、实际50，使最高端m50成为明确有限门。；50真实wordforms与26+三8块逐整数向量相等；不重复旧residue枚举。；缺三walk的0→1 pair非邻（相邻总有backtrack三walk）；继承障碍代入F11，两步至多7×121=847<1331，故此固定fullfiber确不D3；非新普适定理。

**仍未完成：** m50严格失败；同topology evenm≤48/其他拓扑开放，不自动降模数。

**启发与重启依据：** 同层可行32对象均无法同时补0→1，缺的是兼容路线；停止最高端，改四base生成规则且保B三角，再过symbolic/公开门做一次global批次，避免按坏对微降续算。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

