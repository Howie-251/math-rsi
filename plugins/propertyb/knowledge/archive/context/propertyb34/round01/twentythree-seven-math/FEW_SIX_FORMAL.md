# 23点恰一六度分支：五点残图到全局矛盾

本页记录 `formal/Aris4Math/ThirtyFour/TwentyThreeFewSixSelection.lean` 的局部形式接口。原题 T34 仍未完成；本模块不声称已实现真实迹分类。

## 已实现的连接

`residualGraph` 在 `Fin 5` 上显式给出三种图，编号依次为 `2K2+K1`、`K3+2K1`、`K3+K2`。`residual_no_path`、`residual_no_clique` 和 `residual_no_independent` 用 `decide +kernel` 核验这些固定五点图没有诱导三点路径、四团或独立四点。它们不枚举全体超图，也不枚举任意大小的图。

`IsResidual R` 的全部内容是一个三选一图形编号和一个 `Fin 5` 的置换，以及两图关系逐对等价。它没有将全局九点上界放入定义。三个运输引理从实际同构拉回上述禁形。

`exists_five_containing` 将任意至多五点的实际子集扩充为五点子集，再给出五个互异顶点的标号。`no_path_of_every_five` 对实际三点路径应用此扩充；`no_four_of_every_five` 同时处理实际四团与独立四点。所有扩充都在原有限顶点域内部。

`card_le_nine_of_every_five` 接入已核验的 `FiveVertexClusterBound.card_le_nine`：一个有限简单无向关系，若每个实际五点诱导图都满足 `IsResidual`，则全域至多九点。少于五点的情形由整数界直接闭合。

`propertyB_of_five_residuals` 使用真实 `Simple5Hypergraph H` 的边共度定义 `nonunit H x y := x ≠ y ∧ H.codegree x y ≠ 1`。对任意真实顶点集 `U`，只要 `|U| ≥ 10`，且在 `¬PropertyB H` 下每个从 `U` 选出的五锁的非单位图都属于三残图，就推出原始 `PropertyB H`。关系对称性来自实际边共度交换性，非自反性来自显式排除对角；子类型到 `V` 的嵌入保证五锁仍是同一个 H 的实际顶点。

## 调用者仍须提供什么

这里没有把 JSON 表或数值分数作为已形式证明的分类。恰一六度完整分支仍需：

1. 从真实23点、34边、点对覆盖及恰一六度点构造七度点集 `U`，证明各点与六度点共度一且 `|U| ≥ 10`。这项已在下述新增 `TwentyThreeLowUnitSelection.lean` 实现，并通过正规构建。
2. 为每个真实五锁构造其实际迹重数，证明逐级扩锁/投影分类覆盖。
3. 将严格局部证书接回同一个 H 的 Property B；因此在 `¬PropertyB H` 下只能剩下三种非单位图，并给出 `IsResidual` 所需置换。

现有纸面依据为 `middle-math/CANDIDATE_ONE_TWO_LOW_23.md`。其中残型的异点共度只有1或2；因此其按共度2记录的图与本接口的非单位图相同。这个一致性也属于实际分类调用者的证明范围。

调用入口为：

```lean
propertyB_of_five_residuals H U
  (many : 10 ≤ U.card)
  (classify : ¬ PropertyB H → ∀ f : Fin 5 ↪ V,
    (∀ i, f i ∈ U) →
    IsResidual (fun i j => nonunit H (f i) (f j)))
```

`IsResidual` 的置换将实际五锁标签映到上述固定图形标签；选择相反方向的轨道代表时，应传入逆置换。实际 H 始终不变。

## 核验状态

2026-10-14：唯一正规构建者 `t34_19_lean` 执行 `lake build Aris4Math.ThirtyFour.TwentyThreeFewSixSelection`，r16 成功（906 jobs，新增模块3.4秒）。两条导出结果的传递公理均只有 `propext`、`Classical.choice`、`Quot.sound`，无 `sorryAx` 或 `native_decide`。实际日志为 `../twentyone-lean/build-queue-TwentyThreeFewSixSelection-r16.log`。本执行者已读取该日志，没有运行第二个并行构建。

首次 r13 的有限量词 Decidable 合成限制保留在对应旧日志，已通过局部1000上限和复用关系的 DecidableRel 解决。

跨家族纸面审阅沿用本轮已记录的具体 cluster 论证范围；这不冒充新增 Lean 源码的已执行核验。T34 原题、23点完整分支和真实迹分类均没有因本页变为已完成。

## 真实一/二六度点的共同单位集合

新增模块 `formal/Aris4Math/ThirtyFour/TwentyThreeLowUnitSelection.lean` 从任意有限顶点类型 `V`、`Fintype.card V = 23`、真实五元超图 H、恰34边及点对覆盖出发。

`six_seven_budget` 用实际总度数170重新证明 `14 ≤ 2*r+t`，其中 r 为 H 的六度点数、t 为七度点数。它没有调用旧33边的165预算。`unitSevens H` 复用旧 `commonUnitSevens H H.sixVertices` 定义；只复用其不依赖边数的坏邻居删除、度数和共度引理。每个六度点的总共度超额为2，所以 `t ≤ |U|+2*r`，合并给出 `unitSevens_budget : 14 ≤ |U|+4*r`。

直接得到：

- `unitSevens_card_ge_ten_of_one`：恰一六度点时 `|U| ≥ 10`。
- `unitSevens_card_ge_six_of_two`：恰二六度点时 `|U| ≥ 6`。
- `exists_five_unit_sevens`：两分支均可选出真实 `Fin 5 ↪ V`，五点均为七度点，且与 H 的每个六度点互异、共度一。没有假设七度点之间的图形。

最终 `one_six_propertyB_of_residual_classification` 内部使用实际 U、十点下界及前一模块的图论矛盾。剩余前提恰为：在 `¬PropertyB H` 下，任何五个互异七度点若与每个六度点共度一，则其真实非单位图满足 `IsResidual`。因此调用者不再负责提供 U、其大小或全局 cluster 界；仍须用实际迹覆盖及严格染色证书证明这条局部分类型。

当前核验状态：同一正规构建者执行 `lake build Aris4Math.ThirtyFour.TwentyThreeLowUnitSelection`，r17 首编通过（911 jobs，新增模块1.4秒）。两个 U 下界、五高选择和一低条件染色入口的四项传递公理均只有 `propext`、`Classical.choice`、`Quot.sound`。实际日志 `../twentyone-lean/build-queue-TwentyThreeLowUnitSelection-r17.log` 已读取；没有生成新的数值表或更改旧T32/T33文件。
