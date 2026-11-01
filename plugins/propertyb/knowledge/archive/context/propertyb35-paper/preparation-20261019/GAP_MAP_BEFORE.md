# Gap Map

T33 与原 T32 的数学义务均已闭合。G5 记录新增 m(5)≥34；G1–G4 是原32边证明的既有义务，保持其原记录。

## G6 — T34长期Goal active，完整目标开放

原目标为≤34边可染，即m(5)≥35。最新[完整候选地图](../context/propertyb34/round01/PAPER_CANDIDATE_MAP.md)与[进度](../context/propertyb34/PROGRESS.md)。所有19–25点已有完整纸面候选，fresh整篇R1无实质数学缺口。Lean已完成≤20及21δ5/δ6/δ8；Assembly1183 jobs与EightAudit四项标准三公理通过，21仅剩最小度恰7。23实际六锁与等号外点、24实际八匹配锁选择已验；22/23强共度实际排除及其完整轨道覆盖已通过。通用锁点重标号已通过，21四锁纯表356→31、联合24→1并已接实际δ8全支。22–25完整染色和最终Main仍待，m(5)≥35尚未验收，已交付下界仍m(5)≥34。 维持idea active/pending，不新增verified主张；原题审计与最终跨家族C审阅尚待。

## G5 — 33边 Property B：已闭合

2026-10-13，`Aris4Math.propertyB_of_at_most_thirty_three : Target33` 已完整证明任意有限简单五元超图至多33边可染，故 m(5)≥34。19–25点全部分支、23点六条度数分支、最小反例约化、局部分类覆盖、真实类型重数及实际坏对扣除均在内部连接；没有顶点数、点对覆盖或证书作为原主定理的额外前提。

显式 `lake build Aris4Math.ThirtyThree.Main` 完成1138 jobs、exit0，构建后的裸 `[Finite V]` / `Finset` 原题独立复述也exit0。8项顶层传递公理仅 `propext`、`Classical.choice`、`Quot.sound`。Grok与Gemini最终C均有效返回，在静态源码/日志审阅范围内未发现实质问题，未执行Lean。正文两处说明已修正，HTML保真通过；可读证明、交接包与wiki归档也已完成。

入口：[规范证明正文](../proofs/propertyb33/PROOF_PACKAGE.md)、[单卷HTML](../PROOF_PACKAGE_33.html)、[进度与证据](../context/propertyb33/PROGRESS.md)、[形式核验](../context/propertyb33/FORMAL_VERIFICATION.md)、[证明审计](../context/propertyb33/round02/final-audit/PROOF_AUDIT.md)、[主定理](../formal/Aris4Math/ThirtyThree/Main.lean)、[规格](../context/propertyb33-preparation/FORMAL_SPEC_PROPERTYB_33.md)。此前候选和开放义务快照移至[导航历史](../context/propertyb33/round02/final-audit/NAVIGATION_HISTORY.md)，不再作为当前任务。

## G1 — 概率公式与类型表示：已闭合

`Greedy` 证明实际算法失败覆盖，`Counting`、`JointCounting`、`EndpointCounting`、`CriticalCounting` 证明锁定条件下的真实排列计数。`ProfileProbability` 将这些计数与数值权重逐项对齐，`TypeCounting` 证明真实类型纤维及不同有序边对的精确聚合。`ConditionalUnion` 和 `ProfileApplication` 将逐位置 min 上界接到原 `PropertyB`，全部应用条件已在分支中消除。

## G2 — 结构选择与分类：已闭合

`Structure`、`LowDegree`、`Traces`、`SevenPoint`、`Avoidance` 证明所需锁点存在。`BlockClassification`、`K6Classification`、`K6Traces` 解析证明标签分类、七点选六点及迹恢复；`SmallLockProfiles`、`DoubleTripleLockProfiles`、`TripleLockProfiles`、`K4Profiles`、`TraceProfiles` 给出21–25点的真实精确类型表。分类覆盖由定理证明，没有以穷举输入超图替代完备性论证。

## G3 — 实际 link 扣除：已闭合

`LinkCounting` 证明真实无序坏边对数量下界。`LinkDeletion` 和 `ProfileDeletion` 将它们转为同一位置不重复的非贡献有序边对集合；`LinkWeightCertificates` 证明两个方向的权重下界以及23点677末中心至多一个零权重例外。`TwentyOne`、`TwentyTwo`、`TwentyThree` 完成全部实际扣除实例化，扣除进入 C 项后再取 min。

## G4 — 最终闭合：已闭合

`SmallVertices` 证明原 T 等价于19–25点、恰32边、点对覆盖的有限目标，并完成至多18点。七个完整分支由 `NoLocks`、`GlobalPairs`、`TwentyOne`、`TwentyTwo`、`TwentyThree`、`LargeVertices` 给出，`Aris4Math.finite_goal` 汇总后返回任意有限顶点类型。

`Aris4Math.propertyB_of_at_most_thirty_two` 已完整证明原 T；展开类型的 `two_colorable_of_at_most_thirty_two` 和直接下界 `non_propertyB_edges_ge_thirty_three` 均已构建。独立导入审计显示传递公理只有 `propext`、`Classical.choice`、`Quot.sound`。

最终跨模型装配审阅及文档验收的状态由[审阅汇总](../context/reviews/research/REVIEW_NOTES.md)单独维护，不混作未闭合数学引理。有限反例搜索和模型一致意见都不是主定理的前提。

入口：[完整证明](../PROOF_PACKAGE.md)、[义务账本](../PROOF_SKELETON.md)、[形式核验记录](../context/FORMAL_VERIFICATION_PROGRESS.md)、[Lean主定理](../formal/Aris4Math/Main.lean)。
