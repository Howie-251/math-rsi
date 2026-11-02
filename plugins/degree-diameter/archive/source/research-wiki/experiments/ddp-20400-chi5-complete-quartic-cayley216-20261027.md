---
type: experiment
node_id: exp:ddp-20400-chi5-complete-quartic-cayley216-20261027
title: "actualΓ的完整规范216无D10：新213＋严格继承3，quartic Cayley最小直径11"
idea_id: "idea:ddp-breadth-20261027"
verdict: yes
confidence: high
date: "2026-10-27"
hardware: ""
duration: ""
provenance: "research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/REPORT.md; research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/PREDICTION.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/RESULT.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/THEORY_BINDING.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/normalization_proof/PROOF.md; research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/normalization_proof/CONTROL_IDENTITIES.json; research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/run.py; research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/search.cpp"
added: 2026-10-27T20:51:14Z
tags: ["ddp", "method-ledger"]
---

# actualΓ的完整规范216无D10：新213＋严格继承3，quartic Cayley最小直径11

**verdict:** `yes`  ·  **confidence:** `high`  ·  tests `idea:ddp-breadth-20261027`

## Metrics
**对象层级：** candidate_graph_or_family

**目标与阶数：** (4,10)；L=19306；candidate_graph_or_family n=20400

**距目标的证据：** 213新图全部simple/connected/4reg/20400/40800，全0D≤10；3旧D11继承，未试0/UNKNOWN0。216的exactD分布110×11、104×12、2×13，globalD由Γ右regular VT＋完整root0BFS得到。故actualΓ无connectedquartic Cayley D≤10，minpossiblequartic CayleyD=11。未导失败图/新下界0。

**其他指标（保持原计数类型）：**
```json
{
  "fixed_normalized_cases": 216,
  "coverage_theory": "VALID",
  "control_mapping_theory": "VALID",
  "new_actual_cases": 213,
  "new_complete_root_BFS": 213,
  "old_controls_inherited": 3,
  "old_controls_rerun": 0,
  "skip_ordinals": [
    28,
    31,
    135
  ],
  "untested": 0,
  "UNKNOWN": 0,
  "D10hits": 0,
  "exact_global_D_histogram": {
    "12": 104,
    "11": 110,
    "13": 2
  },
  "minimum_quartic_Cayley_D_of_actual_Gamma": 11,
  "all_graphs_n": 20400,
  "all_graphs_m": 40800,
  "all_graphs_simple_connected_4reg": true,
  "leftCayley_rightregular_VT_proof": true,
  "native_CPU_seconds": 0.133757,
  "compiled_CPU_seconds": 1.677065138,
  "total_parent_children_CPU_seconds": 1.8341368749999998,
  "source_D7_BFS": 0,
  "new_source_downloads": 0,
  "exported_failed_edgefiles": 0,
  "new_lower_bounds": 0,
  "ordinary_bad_pair_scope": "Not aggregated across216graphs; rootcounts/histograms preserved separately perrow",
  "prediction": "REFUTED"
}
```





**原始证据：** [research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/REPORT.md](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/REPORT.md)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/PREDICTION.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/PREDICTION.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/RESULT.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/RESULT.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/THEORY_BINDING.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/THEORY_BINDING.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/normalization_proof/PROOF.md](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/normalization_proof/PROOF.md)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/normalization_proof/CONTROL_IDENTITIES.json](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/normalization_proof/CONTROL_IDENTITIES.json)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/run.py](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/run.py)；[research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/search.cpp](../../research/ddp/more_graphs_20261027/d6_D7_current20400_source/four_generator_D10/normalized_group_family/search.cpp)

**统一查重入口：** [方法账本](../DDP_METHOD_LEDGER.md)；机器字段见同目录 JSON。

## Reasoning
**实际范围：** 固定actualΓ χ17=5/sourceMat，firstα^a a1/3/5/7，secondN(v,c1)*Hβ*α^b b0..8，v∈P1(F5)6reps，216完整规范族。独立coverage理论VALID覆盖此Γ全部连通无向degree4Cayley gensets；3旧controls有群等式映射并跳过，只213新actual图/rootBFS。

**仍未完成：** Othergroupmodels, arbitraryquarticgraphs, generalN(4,10) and Lean remain open; alternateχ6 belongs separateproducer and is notcoveredbythis χ5closure.

**启发与重启依据：** 完整群归一化替代按16/31旧坏targets小修，精确关闭actualχ5群全部degree4Cayley范围；不是216非同构图，也不是任意20400quartic图或其它χ/group排除。旧literal witness未transport，继承row witness=null，避免label混用。无需在此Γ加Hframes/phase/score续轮。

有限批次终态不等于整个数学族不存在；范围以以上原文和证据为准。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

