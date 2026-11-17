# Q₈ 无四环子图上界 683：完整材料目录

本文件夹汇集 **ex(Q₈,C₄) ≤ 683** 的已完成计算辅助证明及其依赖、发现过程、核验、审查和框架说明。材料从原工作区复制，原文件和仍在进行的研究均保留。

当前准确结论：所有 Q₈ 的无 C₄ 边子图至多有 **683** 条边。已有 682 边构造，因此区间为 **682 ≤ ex(Q₈,C₄) ≤ 683**。主目标上界 682 仍开放。

## 建议阅读顺序

1. [框架与结果 HTML](research/ex_qn_c4/reports/q8-683-framework-20261116/Q8_683_FRAMEWORK.html)：MathRSI、用户提出的上下界协同、奖励设计和关键中间值。单文件离线可读。
2. [完整证明 Theorem B](research/ex_qn_c4/coevolve/launches/near-extremal-20261115/finite8_degree_augmentation/pool_B684plus_enriched8/B684_EXCLUSION.md)：从任意反例到最终精确矛盾。
3. [非作者全文审查原文](research/ex_qn_c4/coevolve/launches/near-extremal-20261115/finite8_degree_augmentation/pool_B684plus_enriched8/PROOF_AUDIT.md)及 [主代理验收记录](research/ex_qn_c4/coevolve/launches/near-extremal-20261115/finite8_root_checks/ROOT_THEOREM_B_CONSUMPTION.json)。
4. [材料地图](MATERIALS.md)：各前置引理、证书和程序在哪里。
5. [复现说明](REPRODUCE.md)：检查文件、重新计算最终局部最大值、重放 25 组 Q₆ 证书。

## 收入的材料

| 目录 / 文件 | 内容 |
|---|---|
| `research/ex_qn_c4/coevolve/launches/near-extremal-20261115/` | Theorem B 的前置引理、共同统计、精确系数、完整局部枚举、核验和审查；B 分支 enriched1–8 的发现记录 |
| `q6_sources/q8_upper_independent/` | 前置 Q₆ 证明来源、检查器源码、25 组实际 CNF／完整 DRAT 轨迹，以及相关覆盖与边界见证 |
| `research/ex_qn_c4/proofs/` | 实际使用的历史解析引理及其相关材料 |
| `research/ex_qn_c4/coevolve/` | 上下界协同框架源码、配置、测试、工程记录、种子和运行档案 |
| `research/ex_qn_c4/reports/` | HTML、规范源稿、模板、截图和渲染审查 |
| `research/ex_qn_c4/research-wiki/` | 本次定理、相关 Q₆ 实体和导航快照 |
| `math-rsi/` | 与本成果有关的 MathRSI／ARIS 工作流、技能、文档和领域适配；并非整个 MathRSI 仓库副本 |
| `MATERIALS_MANIFEST.json` | 每份材料的包内路径、当前大小与 SHA256、原始散列和收集理由 |
| `validation/` | 在本文件夹中实际执行的交接检查与重放结果 |

前置证书统一放在 `q6_sources/`，相关目录名和路径引用已经整理。主证明、审查和 HTML 的相对证据链接继续可用。`PRESENTATION_EDITS.json` 记录整理副本的前后散列；原审查中的散列仍描述当时版本，本次整理不构成重新数学审查。历史 `PENDING` 状态保留其原意；当前 Theorem B 验收请以上面列出的全文审查和主代理消费记录为准。

## 审查范围

Theorem B 的全文审查结论为 **PASS**，保障级别为 **同模型家族、暂定验收**。有限计算有独立重建与全域核验，但没有宣称 Lean 内核形式化、跨模型家族验收或外部同行审稿。本次文件收集与重放不升级这一数学审查范围，也不证明上界 682。

包内包含证明所用的数据和源码；Python、C++17 编译器及可选的 NumPy／SciPy 属于运行依赖，见复现说明。没有复制凭据、已安装环境缓存或无关的整套旧搜索结果。恰好 683 边的后续开放研究不在本包的主交付范围内。
