所读范围内未发现满足假设的反例或具体缺口。两个最终定理都回到原 Property B，顶层没有留下剖面、槽、位置、配额或代表编号前提。整个 T33 仍未完成，本轮不是最终验收。

## 两低

`propertyB_of_two_sixes` 的假设只有：`H` 是 `Fin 23` 上的 5-一致简单超图、点对覆盖、`|E|=33`、六度点恰好 2 个。

调用顺序与类型一致。`exists_two_sixes_three_sevens_of_count` 用 `six_seven_budget` 从 `2r+t≥19` 得到七度点至少 15 个，再取出两个六度点 `f 0, f 1` 和三个七度点 `f 2, f 3, f 4`。八个交叉或相邻对的共度被证成 1；未强制的只有互不相交的 `{0,1}` 与 `{2,3}`。`λ(f 2, f 3)≥4` 时走 `propertyB_of_high_pair`，该定理只要求这两个点度数为 7。否则两个例外共度都落在 `{1,2,3}`。

九个预算就是这两组取值。`covers` 把任一 `a,b≤3` 的可行 16 维布尔向量归到最大预算 `(3,3)` 的 55 个标号配置；`choice_exact` 的定义域是 `Fin 3 × Fin 3 × Fin 55`，只在 `Admissible` 时给出 `Fin 208` 中的一个代表。412 是报告里的可行输入计数，208 是代表类型，本轮没有重数象。

任意至少三点的锁迹都含一对异于 `{0,1}` 和 `{2,3}` 的点对，因此重数至多 1。16 个大迹类型就是 5 点集的全部 3、4、5 元子集，列表完整。计数为 0 的大迹留在布尔向量里，`highValue` 取 0。`pairSum` 只加这些大迹，`high_pair_budget` 给出它不超过共度，恰是可行条件的方向。

12 个置换是 `{0,1}` 与 `{2,3,4}` 各自的置换。新嵌入是 `σ.toEmbedding.trans vertices`：新标签 `i` 落在旧顶点 `σ i`。`count_relabel` 与 `classify` 使用同一方向，`T` 在新嵌入上的计数等于 `T.image σ` 在旧嵌入上的计数。`choice_exact` 在输入可行时同时要求度数块与共度矩阵被保持。

低阶计数由 `low` 从 33、度数 `(6,6,7,7,7)` 和两对例外共度恢复；`|T|>2` 的 `low` 不进入恢复。`propertyB_of_counts` 把每个中心至多两个避开锁点子族送进已证明的 `RefinedDeletion`。`dual_exact` 对每个代表、每个中心要求乘数非负、中心不在避开集、配额不超过整数公式，且 `lossAt` 不超过加权配额减 `penaltySum`。`dualPenalty` 用同一无序坏对两个方向的权重，缺口各记一半；权重为 0 的槽仍留在求和中，没有另设删除例外。

## 四低

`propertyB_of_four_sixes` 的假设只有点对覆盖、33 条边、六度点至少 4 个。它对 `propertyB_or_unit_counts` 分两边：左支是 B9 已闭合的 47 个非单位代表；右支把三个单位代表交给 `TwentyThreeFourLowUnit.propertyB_of_counts`。`counts_eq_catalog` 用 `castLE` 把 `Fin 3` 的下标原样接到根目录第 0、1、2 个计数函数。

三个计数函数的正迹支持可以手算：

- 代表 0：每点 4 条正迹，可行无序槽 `C(4,2)+1=7`，四中心共 `7⁴=2401`。
- 代表 1：每点只有单点与四元两条正迹，`2⁴=16`。`Fin 7` 的后五项重复首项 `({j},{j})`。
- 代表 2：中心 0 仍是 7 槽；中心 1、2、3 各有单点、过 0 的二元、三元 `{1,2,3}` 这三条正迹，可行槽 4 个，共 `7×4³=448`。中心 3 的四元组 `({3},{3}), ({3},{0,3}), ({3},{1,2,3}), ({0,3},{1,2,3})` 已在 `slot` 中读到。

合计 2865 个真实槽组合。统一成 `Fin 7` 后，`choice_exact` 覆盖全部 `3×7⁴=7203` 个输入，包括重复首项。`slot_complete` 对每个可行 `(T,U)` 给出某个下标，存储顺序或相反顺序均可。

槽先于位置。`exists_actual_slot` 只从真实坏边对提取锁点迹，不提位置。度数 6 时下界 `(4×6-22+2)/3=1`，坏边对非空；单位共度迫使两条迹只在该中心相交。`actual_slot` 先固定 `b : Fin 7`，并证明后来每个同族配置都满足权重不等式。随后 `choice` 才选出 `Row`，`configOf` 才给出位置。`choice_exact` 在四个下标确定后证明该行的族等于 `k`，且四个中心的 `rowLoss` 等于这些下标的存储权重。

`weights_exact` 把同一槽的两个有序 `pairWeight` 相加。`slot_weight_lower` 对任意后选位置成立，并用其余有向坏对权重非负只保留这一对。存储顺序相反时调用处用 `add_comm`。`CustomDeletion` 在每个中心只减这一次损失。`strict_cached` 对全部 `Fin 383` 行给出严格小于 1 的界；383 是行类型，多组槽可以共用一行，覆盖来自全称的 `choice_exact`。

B9 对 `FourLowActual` 与 `BoundedTraceFamilies.mem_enumerate` 的结论保持不变。六锁 611 目录不在本轮，仍不视为已完成。

## 范围

已读两份报告，以及 `TwentyThreeTwoLowComplete`、`TwoLow`、`Catalog`、`Facts`、`Numeric`、`TwoLowHighCatalog`、`Selection` 中本支使用的选点与预算定理、`HighPair`、`RefinedDeletion` 的对偶定义与调用定理、`CustomDeletion`、`ActualBadSlot`、`FourLowUnit`、`UnitFacts`、`UnitNumeric`、`UnitChoice`、`Complete`，以及槽表、三个计数函数、`largeTypes`、`high_pair_budget`、`upper_eq_of_low_data`、`correctionDeleted_at`。`FourLowActual` 只重读了与 47+3 分岔直接相关的结尾。

手算了八个强制单位对、16 个大迹是否列全、三点迹必含单位对、六度坏边对下界 1，以及 `2401`、`16`、`448`、`2865`、`7203` 和 `family` 向量的 24+7+24。没有逐代表重算剖面、对偶分数或 `7292/7293`、`4137/4199`。

本轮没有运行命令，没有打开日志，没有重跑 `decide`。报告文本写明：两低对 Numeric、包装层、Complete 和独立导入的直接 `lake env lean` 均为 exit 0，正式 Lake trace 仍在排队；四低指定 `lake build` 为 exit 0（1002 与 1008 个 job），独立导入 exit 0。
