# 证明与依赖地图

以下 `BASE` 指 [near-extremal-20261115](research/ex_qn_c4/coevolve/launches/near-extremal-20261115/)。

## 1. 最终定理与已接受证书

`BASE/finite8_degree_augmentation/pool_B684plus_enriched8/`

- `B684_EXCLUSION.md`：完整 Theorem B，覆盖所有无 C₄ 的 Q₈ 边子图。
- `B684_ACTIVE_83_PARAMETERS.{md,json}`：实际使用的 83 条约束、参数及来源。
- `EXTRA_EQUALITY_LAYOUT.json`、`EXTRA_EDGE3_LAYOUT.json` 与相应矩阵：356 条一致性等式的具体接口。
- `PROFILE_SNAPSHOT.json`：684–688 边的 645 个必要奇偶侧度数分布。
- `GENERATOR_HISTOGRAMS.json`、`GENERATOR_DEDUPLICATION.json`：1,751 类边邻域直方图及完整归并关系。
- `exact_row_combination001/`：有理数组合、局部整数查询与误差界。
- `connector_pricing/`、`vertex_pricing/`：被选中的约束及其生成、独立核验记录。
- `PROOF_AUDIT.{md,json}`、`review_whole/`：完整非作者审查、语义依赖和源单元覆盖。
- `FROZEN_CANDIDATE_INPUT_HASHES.json` 等：当时冻结的输入绑定，保持历史状态。

`pool_B684plus_enriched1` 到 `pool_B684plus_enriched7` 保留通向最终证书的发现轨迹。阅读结论时以 enriched8 的完整证明和验收为准，早期正数值余量不单独构成最终定理。

## 2. Q₆ 前置引理

`BASE/finite8_q6_import_audit/PROOF.md` 与 `VERIFICATION.md` 给出局部不等式、完整条件、独立输入重建和证书重放范围。`FRESH_REPLAYS.json` 记录 **25** 个输入、**4,383,882** 次已检查 RUP 添加。

实际 CNF 与 DRAT 位于 `q6_sources/q8_upper_independent/results/`；检查器和重建程序也随包提供。`SOURCE_UNITS.json`、`DEPENDENCIES.json`、各份 `.receipt.json` 与 stdout/stderr 共同保留原证据链。

历史解析引理在 `research/ex_qn_c4/proofs/`，尤其是 `low1_cycle006/analytic/`、`q6_three_full_structure_cycle010/` 和 `q8_single_three_cycle007/local_weighted/`。这些原件的旧全局应用范围与本次实际使用的局部结论分别保留。

## 3. 把局部统计接回同一个图

| BASE 下的目录 | 在 Theorem B 中的作用 |
|---|---|
| `finite8_maximal_route/` | 极大扩张、Q₆ 平均、必要度数分布完整覆盖与进口闭合 |
| `finite8_flags/` | 固定维数的局部矩、共同根运输和精确抽样系数；`main.tex` 为核心源之一 |
| `finite8_edge_flags/` | 边邻域矩到完整面旗的精确提升 |
| `finite8_edge_vertex_bridge/` | 同一顶点／环境边的混合状态与矩平衡 |
| `finite8_edge3_sampling/` | 三方向边旗的共同抽样 |
| `finite8_degree_augmentation/edge3_quad_lift/` | 上述三方向统计到原 Q₄ 计分族的精确提升 |
| `finite8_connector_frequency/` | 连接状态有限整数计数及其有效约束 |

部分随包背景材料涉及更强但最终未使用的条件锥、投影或探索候选；Theorem B 的准确数学前提以其 83 条非零权重清单为准。

## 4. 独立重建与完整 Q₄ 枚举

- `BASE/finite8_root_checks/reconstruct_exact_dual.py`：从实际整数参数与有理数权重重建证书。
- `BASE/finite8_root_checks/exact_dual/B_enriched8_candidate001/`：最终重建数据及完整枚举原始输出。
- `BASE/finite8_root_checks/exact_dual/review/independent_audit.py`：独立科学系数重建；该目录保留独立结果、源码审查和冻结记录。
- `BASE/finite8_full_oracle_independent/independent_q4.cpp`：独立完整局部最大化程序。
- `BASE/finite8_full_oracle_independent/COVERAGE_AND_VERIFICATION.md`：覆盖及数学计分解释。
- `BASE/finite8_degree_augmentation/check_B684_certificate.py`：对完整枚举输出计算最终精确矛盾余量。

最终查询应返回 **13,150,453** 个带标记补全、整数最大值 **−37,440**，从而得到严格正余量

`782808475930428709 / 4209067950080000000000`。

## 5. 框架与可读展示

[HTML](research/ex_qn_c4/reports/q8-683-framework-20261116/Q8_683_FRAMEWORK.html) 着重解释 MathRSI 与上下界协同。其目录包含源稿、模板、原渲染审查和桌面／移动端截图。

[协同框架说明](research/ex_qn_c4/coevolve/README.md) 对应实际程序、指标、候选不等式、反例检验和奖励反馈。运行档案与早期样本仍保留其原始含义，未把工程试跑或样本相关性追认为上界证明。

包内旧 wiki 导航会提到本次范围以外的题目或后续研究；它用于保留研究背景，不替代这里明确列出的证明依赖地图。
