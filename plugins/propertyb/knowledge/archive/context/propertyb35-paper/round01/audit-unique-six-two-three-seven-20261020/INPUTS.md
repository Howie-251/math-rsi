# 已冻结的两条实际分支：独立 proof-checker 输入

本次只核21点、35条互异五元边、点对覆盖、最小度6、唯一六度点、恰2或3名七度点的完整Property B定理。没有全21点或全m(5)≥36结论。旧35 Lean paused；不运行Lean、不访问v2。

主稿为 `proofs/propertyb35/TWENTYONE_UNIQUE_SIX_TWO_OR_THREE_SEVEN.md`，冻结于2026-10-20 06:17:29 UTC。新主链不使用T33/T34、critical、threshold T、prefix degree DP。以下source unit均须核完整声明及对应全部证明；未重证进口应逐项列明，而不是当作已全文审阅。

从项目根解析：

- U01：`proofs/propertyb35/TWENTYONE_UNIQUE_SIX_TWO_OR_THREE_SEVEN.md`，全文§1–9及定理。
- U02：`proofs/propertyb35/TWENTYONE_UNIQUE_SIX_TWO_OR_THREE_SEVEN_MINIMUM_NONUNIT_DEGREE_FOUR.md`，全文§1–8。
- U03：`context/propertyb35-paper/round01/middle/four_nonunit_degree_six_center_20261020/REPORT.md`，全文。
- U04：`context/propertyb35-paper/round01/middle/generic_c3_fourteen_gate_20261020/PROOF.md`，全文。
- U05：`context/propertyb35-paper/round01/middle/generic_high_degree_pair_gates_20261020/REPORT.md`，全文及调用前提。
- U06：`context/propertyb35-paper/round01/middle/generic_quad_core_multiplicity_three_20261020/PROOF.md`，全文，尤其实际四尾的共同星及§7。
- U07：`context/propertyb35-paper/round01/middle/generic_degree_six_star_count_20261020/PROOF.md`，全文。
- U08：`context/propertyb35-paper/round01/middle/a2_a3_joint_moment_frontier_20261020/CAPACITY_LEMMAS.md`，全文。
- U09：`proofs/propertyb35/GLOBAL_TWO_FLIP_SHARED_MIDDLE.md`，共同middle恒等式及非threshold部分全部证明；threshold附录不进入主链。
- U10：`proofs/propertyb35/GLOBAL_TWO_FLIP_PATH_REPAIR.md`，原染色修复、各事件计数及21点M35阈值。
- U11：`proofs/propertyb35/GLOBAL_PRIVATE_PAIR_REPAIR.md`，原单翻计数及n1≥397调用。
- U12：`context/propertyb35-paper/round01/twentyone-high/unique6_with7/new_structure_20261020/SIX_UNIT8_POOL_PROOF.md`，全文。
- U13：`context/propertyb35-paper/round01/middle/a2_a3_min4_cap13_closure_20261020/NO_CRITICAL_FILTER.py` 与 `NO_CRITICAL_CHECK.py`，全文算法、全部有限域覆盖和结果。
- U14：`context/propertyb35-paper/round01/middle/three_nonunit_direct_repair_20261020/VERIFY_ASSEMBLY.py`，完整91轨/83必要键/79+47固定证书覆盖算法及对应输入。
- U15：`context/propertyb35-paper/round01/middle/four_nonunit_degree_six_center_20261020/VERIFY.py`、`INDEPENDENT_VERIFY.py`、`FIVE_LOCK_FULL5.py`，完整marked域及五证书。
- U16：`context/propertyb35-paper/round01/middle/generic_c3_fourteen_gate_20261020/VERIFY.py`，完整7812域与1144固定证书的验证算法。

声明进口包括通用q≤2门及其完整数学来源、conditional permutation概率引理、旧t15/16饱和门、一般删星rank≥11等。应检查实际caller，并区分本次全文核、接口核、程序执行。不得用此前模型赞同替代这些依据。

重点攻击：同H共享资源、精确role与degree谱、实际x-star共同恢复、S5/S4运输、无放回注入、cross迹仅是valid middle上界、row τ下界不可除二、盒凸性方向、五容量只共享一个P、完整16谱/整数域、33→E≤72与六条实际x边→E≥73的同图矛盾。

产物：覆盖receipt、依赖DAG/assumption ledger、逐义务与反例攻击记录、PROOF_AUDIT.md/json、PROOF_CHECK_STATE.json。审阅不得修改证明源码；问题交root修。native同家族保留provisional，Grok/Gemini成稿另行有效审阅。此为数学Markdown证明，不额外制作LaTeX前后对照报告；本次audit HTML暂不渲染，完整36阅读HTML在全题闭合后交付。
