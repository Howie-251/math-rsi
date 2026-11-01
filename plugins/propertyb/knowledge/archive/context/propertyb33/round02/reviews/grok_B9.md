所读范围内没有满足假设的反例。`propertyB_of_low_bad_high` 的语句本身只保留点对覆盖、33 条边、恰好一个六度点和一个共度至少 2 的七度邻居；七度个数、禁止三元、分类和坏对配额都在证明内部消掉。四低定理只把 47 个非单位代表送到未修正严格界，3 个单位代表留在析取的右侧。`mem_enumerate` 的证明保住支持域上每一个容量合法的 `Finset`。六锁 611 目录仍不算完成。这不是 T33 的证明。本轮没有执行任何命令，也没有打开审计日志。

## 读的范围

报告：`context/propertyb33/round02/low-bad-high/REPORT.md`、`context/propertyb33/round02/four-low/REPORT.md`。

一低一坏高：`TwentyThreeLowBadHighComplete.lean` 全文，`Catalog` 的 `Forbidden`、`choice_exact`、`classify`，`Recovery` 的 `low` 与 `recovery_formula`，`TwentyThreeLowBadHigh.lean` 与 `Numeric.lean` 全文，`Facts` 全文，`ColoredSelection` 从闭集引理到 `exists_locks_low_bad_high_of_count`，`TwentyThreeSelection.six_seven_budget` 到 `indexed_six_excess_le_two`，`TwentyThreeHighPair.propertyB_of_high_pair` 全文，`TwoLowHighCatalog` 的 `pairDegree`、`Admissible`、`covers`。

坏对扣除：`RefinedDeletion` 从 `dual_bad_weight_lower` 到 `propertyB_of_refined_deletion`，`AvoidedLink.avoided_bad_pair_budget` 与 `avoided_bad_pair_lower`，`CustomDeletion.propertyB_of_custom_deletion`，`ConditionalUnion.propertyB_of_weighted_position_bounds` 与 `pair_sum_le_weighted_deletion`，`weighted_deletion_bound`，`ProfileDeletion.correctionDeleted_at`，`LinkDeletion.directedBadPairs`，`typeWeight`，`Numeric.pairWeight` 与 `validProfile`，`FiveProfiles` 的位置类型与 `realizes_profile`，`MultiLockRecovery` 的 `high_pair_budget` 与 `actual_recovered`。

四低：`TwentyThreeFourLowActual.lean` 全文，`Structure` 全文，`Catalog` 的 `pairBudget`、`co`、`highBudget`、`high_covers`、`classify`，`QuadProfiles` 的 `recovered` 与 `actual_recovered`，`Bare.propertyB_of_counts` 的语句。`Actual` 的导入只有 `Structure`、`Catalog`、`Bare`。

一般引理：`BoundedTraceFamilies.lean` 全文。六锁文件只读了类型、`cost`、`maximum` 和 `covers` 的语句，用来看引理的调用形状。

未逐格核对 130 组保存数组、47 条裸界分数、611 条家族字面量。`pair_covers_vector`、`high_covers`、`choice_exact`、`covers_vector`、`dual_exact`、`strict`、`recovery_formula` 都是 `decide +kernel`，没有重跑。

## 独立核算

度数和：每点至少 6 度，六度点在和式里补 2、七度点补 1，于是 \(8\cdot 23\le 165+2r+t\)，即 \(2r+t\ge 19\)。\(r=1\) 给出 \(t\ge 17\)。高于 8 的度数不破坏这个下界。`of_count` 用的就是这条，调用方不用再交 \(t\ge 17\)。

选点容量：六度点坏伙伴至多 2，去掉已选的 \(y\) 后 \(A\le 1\)；七度点坏伙伴至多 6，去掉 \(x\) 后 \(B\le 5\)；\(F=\operatorname{insert} y\,(A\cup B)\) 至多 7。从至少 17 个七度点里去掉 \(F\)，剩下至少 10 个，且都与 \(x,y\) 单位共度。10 点单位图里，非邻居落在「自己加上至多 6 个坏伙伴」中，所以最小度至少 3。颜色是过 \(y\) 的那条唯一边，去掉 \(y\) 后至多 4 个顶点。闭集 \(S\) 含在两个颜色类里，\(|S|\le 8\)；闭集引理给 \(|S|\ge 6\)，补集同样闭且至少 6，和为 10，矛盾。因此存在 \(a,b,c\)。锁是 \((x,y,a,b,c)\)，也就是标签 \(0,1,2,3,4\)。

唯一可以不是单位共度的锁对是 \(01\) 与 \(23\)，而且它们不相交。任意至少 3 元的锁迹至少含一个其他对，所以大迹重数是 0 或 1。\(b\neq 1\) 时，没有边同时含标签 \(1,2,3\)，于是每个包含这个三元的更大锁迹也是 0。\(b=1\) 时禁止条件为真，三元可以出现。

重标号：新嵌入是 \(\sigma\) 后再接原锁，新标签 \(i\) 落在旧顶点 \(\sigma i\)。新标签集 \(T\) 的条数等于旧标签集 \(T.\operatorname{image}\,\sigma\) 的条数。`classify` 要求的也是 `highValue` 在这个像上等于代表的 `counts`。\(\sigma 0=0\)，六度点留在标签 0；`pairDegree` 在 \(\sigma\) 下不变，所以新标签上的共度矩阵仍是同一个 \(a,b\)。

位置：`positionFn` 是 0 起的 `Fin 23` 下标，剖面里的锁位置是这些下标加 1。配置 0 的 `![11,7,8,9,10]` 加 1 得 \(12,8,9,10,11\)。剖面中间的 `[8,9,10,11,12]` 是这五个数排好序，末尾 `[12,8,9,10,11]` 是按锁标签排列的修正中心。`centers_exact` 写的就是后者。两份清单是同一组五个位置。

坏对公式：地面是 \(m=v-1-|R|\)。`avoided_bad_pair_budget` 给出 \(4n\le 3B+m\)，所以 \((4n+2-m)/3\le B\)。这就是 \(\lceil(4n-m)/3\rceil\)。总配额的 \(R=\emptyset\)，\(m=22\)：六度 \((24-20)/3=1\)，七度 \((28-20)/3=2\)。纯配额的 \(R\) 是其余四把锁，\(m=18\)。两组配额都加在同一个无序坏对的 `quotaWeight` 上；双向权重只付一次，超出部分由每侧一半的罚项补齐。对角线用的是 \(n_t(n_u-[t=u])\)，对应 `offDiag`，边不与自己配对。权重非负，而且 \(D\) 不超过被删有序对的权重和，这个和又不超过全部有序对的权重和 \(C\)，所以 \(C-D\ge 0\)，再取 `min` 不会把概率上界减成负数。

四低盈余：每把六度锁对其他三把锁的 \((\lambda-1)\) 之和至多 2。六对的下标是 \(01,02,03,12,13,23\)。四个不等式分别是顶点 \(0,1,2,3\) 的三对。三元 \(T\) 满足 \((|T|-1)(m-1)\le 2\)，所以重数至多 2；四元是 \(3(m-1)\le 2\)，重数至多 1。六个大迹不等式是每条对上「两条三元加大四元」之和不超过该对的 \(\lambda\)。手算与 `highBudget` 的六行一致。真实共度是等式，不等式是它的超集，真实输入都落在这个全称语句里。

前三个四低代表手算都是全单位、每点度 6、总和 33。代表 0：空迹 15，四个单点各 3，六条二元各 1。代表 1：空迹 12，四个单点各 5，四元 1。代表 2：空迹 14，\(\{0\}\) 为 3，其余三个单点各 4，二元 \(01,02,03\) 各 1，三元 \(123\) 为 1。它们确实不该送进那 47 条非单位界。

`mem_enumerate`：候选表为空时，支持条件迫使 \(F=\emptyset\)。头元素 \(a\in F\) 时，非负成本和 `single_le_sum` 保证 \(a\) 的成本不超过容量；`sum_erase_add` 把剩下的和从容量里减去这份成本，自然数减法在这个前提下不截断；`insert_erase` 把 \(F\) 装回去。\(a\notin F\) 时只走左侧，元素留在尾部。候选重复出现也不会丢掉只含一次 \(a\) 的集合。引理不声称表外的集合、也不表示重数大于 1 的多重集。

六锁若按这个引理用：41 个候选是六元集的 3、4、5 元子集，\(20+15+6=41\)；五元边的迹至多 5 元，全集不该在里面。15 条对里，容量 2 的是下标 0 的 \(\{0,1\}\) 和下标 9 的 \(\{2,3\}\)，其余为 1。这两对不相交，每个 3 至 5 元集至少还含一条容量 1 的对，所以大迹重数至多 1，`Finset` 没有漏掉合法的重复迹。这只说明引理的类型和这条预算匹配。`enumeration_exact` 把枚举表等同于长度 611 的字面量，那个 `decide` 没有跑，611 不算已经核完。

## 实际问题

没有一条能同时满足所读定理假设的反例。

两处按分支自己的语句就不能算做完：

- `propertyB_or_unit_counts` 是析取。\(k<3\) 时得到四把六度锁、全部对共度为 1，以及对应的真实迹重数；这里没有 `PropertyB`。`Actual` 没有调用 `TwentyThreeFourLowUnit`。
- `TwentyThreeLowUnitSixHighCatalog.covers` 虽然写成先用 `mem_enumerate`、再用 `enumeration_exact`，但六锁 41 大迹、最大预算、611 这一步仍在计算途中。不把 `enumeration_exact`、611 字面量或它后面的概率界当作已完成。

228 和 464 没有对应的基数定理。228 是报告里「满足 `Admissible` 且 `Forbidden` 的标记输入」的个数；证明域是 \(a\in\{2,3\}\)、\(b\in\{1,2,3\}\) 和 55 个布尔向量上的蕴含，空槽是空蕴含。464 只出现在模块注释和四低报告里。覆盖义务是 `covers`、`classify`、`pair_covers`、`high_covers` 这四个全称语句。它们的 `decide` 没有在本轮重跑，这不是已经发现的漏项。

## 无问题的范围

`propertyB_of_low_bad_high` 没有留下剖面、分类、重数或配额前提。恰好一个六度点、且它有共度至少 2 的七度邻居时，五把锁就是 \((x,y,a,b,c)\)，度型 \((6,7,7,7,7)\)，\(2\le\lambda(x,y)\le 3\)。标签 \(23\) 的共度至少 4 时，直接调用 `propertyB_of_high_pair`：两顶点都是七度、共度在 4 到 7 之间、33 条边；语句里没有「没有六度点」这一条。共度不超过 3 时，\(b\in\{1,2,3\}\)，禁止条件由染色结论送进 `actual_forbidden`。

130 个代表是 `Config = Fin 130` 的上域。每个满足预算和禁止条件的 0-1 大迹先被 `covers` 收进 55 个布尔向量之一，再由固定标签 0、保持共度矩阵的置换送到某个代表。代表没用完只是超集，不影响这条全称覆盖。恢复用的是同一个 \(H\) 的 33、五把锁的度和两条特殊对的共度；`actual_recovered` 对全部子集给出条数等式，`recovery_formula` 再把它收成保存的 `counts`。

实际坏对扣除用的是同一张剖面：避开集是 \(\emptyset\) 和其余四把锁，中心不在避开集里，两个乘数非负，配额不超过上面的整数公式，`dualLoss` 不超过加权配额减 `penaltySum`。`correctionDeleted_at` 在五个修正中心上取的就是该锁点的有向坏对，两个顺序都在；中心以外损失为 0。零权重的几何槽留在 `pairWeight` 的 0 分支里，不能用来支付配额。

四低的真实盈余推进到完整的四星预算和高迹预算；三元重数域含 0、1、2，四元含 0、1。`actual_representative` 把任意四把不同的六度锁送到 50 个代表之一，重标方向与一低分支相同。47 个非单位代表进入 `Bare.propertyB_of_counts`：未修正、`emptyPairCap = none`、修正中心为空、严格界小于 1。这 47 条分数本身没有重算。
