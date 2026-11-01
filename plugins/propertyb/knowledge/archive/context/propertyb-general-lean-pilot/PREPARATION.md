# 一般 Property B：Lean 阶段准备

2026-10-21。仅作源码/API只读评估后的准备；未运行Lean或编译，未启动Goal。原一般下界纸面成果保持完成，旧35 Lean与36自然语言研究继续暂停，不触碰v2。实施时间须由试点实测，现不作工期承诺。

## 阶段出口

先从真实有限重染算法证明一般RS失败上界及充分判据：对任意有限简单k元超图，实际边数m、有向单交对数γ及0<p≤1，失败概率不超过

\[
1-[1-(1-p)^k]^{m/2^{k-1}}+
\gamma\,4^{1-k}\int_0^p(1-y^2)^{k-1}\,dy.
\]

再写真实caller：任意有限顶点类型、简单17元边集且边数≤2^17，取p=1/17，用γ≤m(m−1)及纸面基线估计，推出存在Bool染色且每边两色。空边集单独直接染色。阶段不以“假设RS概率界则可染”结束；界必须从实际算法内部证明，不得新增公理或把概率界当输入证书。

## 有限表示与复用边界

优先评估“初始颜色＋Bernoulli(p)资格位＋均匀顶点排列”的有限加权样本空间。排列代表处理次序，可避开连续时刻、零测碰撞与条件于单点的测度接口；须证明该有限算法自身的坏事件覆盖和权重计数。

固定单交对可按a名必须在交点前的顶点、b名必须在交点后的资格顶点分组；相对顺序权为a!b!/(a+b+1)!。所得有限和再以多项式积分恒等式接到J_k(p)。这仍是拟议表示，尚未编译验收。连续独立Uniform时刻与纸面最贴近，但会增加可测性、独立性及积分接口负担；两种路线择一，不重复建整套框架。

`formal/Aris4Math/Counting.lean`已有`card_prescribed_images`、`card_mapping`、`card_image_eq`、`image_subset_ratio`：计固定位置/子集像，不直接计上述相对次序；需补限制到活跃顶点的均匀性与分块顺序计数。

`formal/Aris4Math/Greedy.lean`的`orderedEdges`、`orderedEdges_uniform`、`failureAt_covered`展示排列重标号及原边身份保留；`propertyB_of_successful_permutation`展示染色拉回，但caller硬编码五元。其算法是全红单向贪心，与RS双颜色、资格位、初始单色触发不同，不能直接调用为RS证明。

`formal/Aris4Math/Reduction.lean`的`pushforward`、`propertyB_pullback`、`merge`及`exists_pair_covering_counterexample`可泛化k与预算；现类型为`Simple5Hypergraph`且最小反例预算固定32。第一阶段RS基线caller无需最小反例结构。

## 已定位的固定mathlib接口

以下路径均在`formal/.lake/packages/mathlib/Mathlib/`：

- `Combinatorics/SetFamily/HarrisKleitman.lean`：`IsUpperSet.le_card_inter_finset`为均匀子集计数；任意p的加权正关联仍需实现，不能直接套用。
- `Analysis/Convex/Jensen.lean`：`ConvexOn.map_sum_le`；`Analysis/Convex/SpecificFunctions/Basic.lean`：`convexOn_exp`。适合有限初始染色的加权Jensen。
- `MeasureTheory/Integral/IntervalIntegral/Basic.lean`：`intervalIntegral.integral_comp_mul_left`、`integral_mono_on`、`integral_pos`。积分连接仍需实际caller核对。
- `Combinatorics/SimpleGraph/Extremal/Turan.lean`：`SimpleGraph.CliqueFree.card_edgeFinset_le`、`mul_card_edgeFinset_turanGraph_le`，后续可替代重新形式化Caro–Wei随机排列证明。

阶段后再评估完整k≥17增长整数增益：新增经典团界、最小反例接口、log/sqrt/floor和最大RS预算存在性。可考虑只用经典公共点二分团界，剥离Gram线代依赖；此为实现范围建议，不改现有纸面源。不会自动扩大k范围、恢复旧题或宣称完整一般定理已形式化。

## 准备文本核对

本次另由GPT-6.1 Sol只读核对阶段Goal及启动文本，属于same-family/provisional：一般RS核心、任意有限17元caller及最终类型／公理审计边界明确，未发现实质冲突。主代理复核基线估计：m/d≤2，a^(m/d)≥a²>1/4，γJ/d²<4/17<1/4；a>1/2由(17/16)^17≥1+17/16>2推出。这里只核目标与纸面调用，尚无Lean运行或新跨家族编码审阅。
