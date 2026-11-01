# m(5) ≥ 35：自然语言证明全文已完成

**完整自然语言证明稿已经写齐；端到端 Lean 形式证明尚未完成。**

正文覆盖原命题的约化和全部顶点数分支，首轮完整纸面审阅未发现实质数学缺口。目前保存的是完整候选证明稿；新下界将在剩余 Lean 连接及最终验收完成后正式交付。已经验收的成果是 [m(5) ≥ 34](M5_GE34.html)。

更新于 2026 年 10 月 14 日。研究按用户时限暂停，以下进度以最后实际构建和独立导入结果为准。

## 这次要证明什么

设 $V$ 是任意有限顶点集，$E$ 是由互不相同的五元子集组成的超图边集。目标是证明：

$$
|E|\le 34\quad\Longrightarrow\quad
\exists c:V\to\{0,1\},\ \forall e\in E,\ c(e)=\{0,1\}.
$$

也就是说，至多 34 条五元边总能二染色，使每条边同时含两种颜色。若 $m(5)$ 表示不可二染色的简单五元超图的最少边数，这等价于 $m(5)\ge35$，不要求证明等号。

正式定义、量词与验收要求见 [数学规格](FORMAL_SPEC_PROPERTYB_34.md)。代码目录 `ThirtyFour` 和记号 T34 指“至多 34 条边”，因此对应的下界是 **35**。

## 自然语言证明已经完成到哪里

全部分支的论证、结构分类、精确数值证书及实际超图的对应关系均已有完整文字稿。其总体推理是：从原始有限超图出发，通过最小反例约化限制顶点数，再按实际度数和共度选择锁点，控制随机顺序染色失败的概率，得到合法染色。

约化后的核心输入有 34 条边、覆盖每一对顶点，总度数为

$$
\sum_{x\in V}d(x)=5\cdot34=170.
$$

点对覆盖还给出 $4d(x)\ge |V|-1$。这些整数约束决定各顶点数下有哪些度数分支；它们是从原始输入内部推导的性质，不是原命题额外要求。

证明的关键推进是把多个锁点的约束放在**同一个实际超图**上联合使用。某个单独局部上界不够严格时，其他锁点的真实迹、边对和度数预算进一步排除残型，或提供更强的联合上界。有限局部分类的覆盖、实际计数和概率界需要同时成立。

首轮完整纸面审阅已经读过整条候选链，并攻击了选点、分类遗漏、联合计数和最紧数值证书，未发现实质数学问题。Grok 与 Gemini 也已按具体义务审阅若干关键推导。全文首轮属于同家族独立审阅，模型意见与 Lean 核验分别记录；详见 [纸面审阅记录](context/propertyb34/round01/paper-audit/PROOF_AUDIT.md) 和 [跨模型审阅范围](context/propertyb34/round01/reviews/REVIEW_DISPOSITION.md)。

## Lean 已经闭合的完整分支

以下“完整”均指从该分支的实际超图条件出发，内部构造所需局部输入，最终返回合法染色。

| 分支 | 已核验结果 |
|---|---|
| 至多 20 个顶点 | 全部分支已闭合 |
| 21 点、最小度 5 | 已闭合 |
| 21 点、最小度 6 | 已闭合 |
| 21 点、最小度至少 8 | 已闭合 |
| 21 点、最小度 7，恰有一个七度点 | 本轮新闭合，已接总装配 |
| 21 点、至少五个七度点 | 本轮新闭合，已接总装配 |

最后两支分别使用完整的 925 项和 3618 项局部容量分类。实际选点、计数重建、换标号、严格投影与最终染色都已经接通，公开分支定理没有留下局部表或证书前提。

更新后的总装配已构建通过；两份独立导入从裸五元 `Finset` 边集复述原 Bool 染色结论，合计八项传递公理检查只有 `propext`、`Classical.choice`、`Quot.sound`。这些检查证明了上述已完成范围，以及原目标与剩余义务的等价。

## Lean 还差多少

**当前总装配明确留下两组义务：21 点恰有 2、3、4 个七度点；以及 22–25 点的完整染色分支。** 后者已经有不少已通过的支撑模块，但还没有接成整支结论。

| 剩余部分 | 已有的可复用成果 | 还需完成 |
|---|---|---|
| 21 点，恰有 4 个七度点 | 四锁九残型及真实归一化已通过；第五锁的纸面分类已有 | 完整第五锁严格界、提升覆盖与实际调用；522 个纯代表目前仅首 16 个已构建，另有 4 个联合代表 |
| 21 点，恰有 3 个七度点 | 完整纸面论证及精确证书；共度、单位邻点与提升接口已通过 | 模式计数、五锁完整分类、残型到共同单位集合的连接，以及六锁收尾 |
| 21 点，恰有 2 个七度点 | 实际七度点选择、八度集合与单位集合界已通过 | 完整五／六锁分类、各类点数约束及最后的匹配结构矛盾 |
| 22 点 | 强共度实际排除、共享坏边对与混合布局接口已通过 | 其余全部度数分支的分类、真实输入和染色结论装配 |
| 23 点 | 六锁选择及等号外点、共同单位集合、强共度排除已通过；一／二低度分支的三锁到四锁完整连接新通过 | 继续处理四锁剩余的 22＋19 个残型，并连接其他全部度数分支到染色结论 |
| 24 点 | 实际八个匹配锁点选择已通过；完整纸面分类已有 | 完整目录的内核覆盖、严格界及实际染色装配 |
| 25 点 | 三类实际单位锁选择已通过；完整纸面九／十锁论证已有 | 完整数值与分类核验、九锁残型到第十锁的实际连接及整支装配 |

这不是“只差最后一次构建”。工作量应按数小时级规划，尚不能给出可靠的精确时长或完成百分比。最直接的下一步是复用四锁九残型，先关闭 21 点恰有四个七度点的分支；更大数值表优先共享计数系数，避免逐项重复展开。

逐项实现入口、已编译与未编译表的边界见 [21 点续接地图](context/propertyb34/round01/twentyone-lean/DEGREE_SEVEN_CONTINUATION.md)。25 点的共享系数方案及已通过的小型实际调用见 [形式化成本分析](context/propertyb34/round01/high-math/TWENTYFIVE_FORMALIZATION_COST.md)。

## 全局验收还需要什么

所有分支完成后，把它们装配成任意有限顶点集上的原命题，再独立导入展开后的染色声明、检查传递公理，并完成 Grok／Gemini 对最终源码和导出命题的审阅，最后生成可复现交接包。

目前的 [Assembly.lean](formal/Aris4Math/ThirtyFour/Assembly.lean) 证明的是原目标与 `RemainingGoal` 等价。无条件的 T34 主定理尚未完成；现有 `lake build` 默认仍指向旧题，不能用于宣布新目标完成。

## 完整自然语言稿的阅读入口

下列入口合起来覆盖整条文字证明。当前页面负责呈现结果与核验进度，详细数学论证保留在对应规范稿中。

| 内容 | 规范稿 |
|---|---|
| 原命题与全部分支地图 | [正式规格](FORMAL_SPEC_PROPERTYB_34.md)；[完整候选地图](context/propertyb34/round01/PAPER_CANDIDATE_MAP.md) |
| 通用概率与计数 | [概率引理](proofs/PROBABILITY_LEMMAS.md)；[联合布局与共享坏边对](context/propertyb34/round01/middle-math/CANDIDATE_TWENTYTWO_SEVEN.md) |
| 19–20 点 | [第一阶段证明与来源](context/propertyb34-hour1-20261013/REPORT.md)；[20 点度八简化](context/propertyb34/round01/twenty-lean/EIGHT_SIMPLIFICATION.md) |
| 21 点全部度数分支 | [完整 21 点证明地图](context/propertyb34/round01/twentyone-math/COMPLETE_TWENTYONE.md) |
| 22 点全部度数分支 | [完整 22 点论证](context/propertyb34/round01/middle-math/COMPLETE_TWENTYTWO.md) |
| 23 点，无六度点 | [最小度七论证](context/propertyb34/round01/twentythree-seven-math/N23_MIN_SEVEN.md)；[实际选点](context/propertyb34/round01/twentythree-seven-math/SELECTION.md) |
| 23 点，恰有一／二个六度点 | [一低与二低论证](context/propertyb34/round01/middle-math/CANDIDATE_ONE_TWO_LOW_23.md) |
| 23 点，恰有三个六度点 | [三低论证](context/propertyb34/round01/high-math/CANDIDATE_THREE_LOW_23.md) |
| 23 点，恰有四／五个六度点 | [四低与五低论证](context/propertyb34/round01/middle-math/CANDIDATE_FOUR_FIVE_LOW_23.md) |
| 23 点，至少六个六度点 | [低度分支论证](context/propertyb34/round01/middle-math/CANDIDATE_LOW_BRANCHES.md) |
| 24 点全部分支 | [完整 24 点论证](context/propertyb34/round01/high-math/CANDIDATE_TWENTYFOUR_COMPLETE.md) |
| 25 点全部分支 | [完整 25 点论证](context/propertyb34/round01/high-math/CANDIDATE_TWENTYFIVE.md)；[九锁通用引理](context/propertyb34/round01/high-math/NINE_LOCK_UNIVERSAL_LEMMA.md) |

## 本轮成果与复现记录

- [最后半小时收卷](context/propertyb34/round01/FINAL_30_MINUTES_REPORT.md)：两条新完整分支、23 点扩锁连接与剩余任务。
- [正式构建和审计索引](context/propertyb34/round01/twentyone-lean/CHECKPOINT.json)：One、Many、Assembly 与独立原题复述。
- [23 点四锁完整连接](context/propertyb34/round01/middle-lean/FOUR_PROMOTION_COVERAGE.md)：覆盖、实际计数、80 项严格排除和 41 个残型。
- [Lean 提速经验](context/propertyb34/round01/middle-lean/PERFORMANCE_NOTES.md)：稀疏查询、证书分模块与抽象分流，均附实际构建记录。
- [m(5) ≥ 34 的完整证明](M5_GE34.html)：已验收的前一项成果。
