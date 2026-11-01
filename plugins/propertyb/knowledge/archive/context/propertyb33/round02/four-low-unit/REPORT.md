# 23 点四低点的三个单位共度代表

本支处理四个互异六度锁点，任意锁点对的共度均为 1，实际类型计数属于 `TwentyThreeFourLowCatalog.counts` 的第 0、1、2 个代表。目标接口是 `TwentyThreeFourLowUnit.propertyB_of_counts`；它从实际超图、点对覆盖、四个六度锁点、单位共度和实际计数推出 `PropertyB H`。

每个六度点在 23 点的点对覆盖超图中都有真实坏边对。单位共度使两条边的锁点迹恰在中心相交；`ActualBadSlot.exists_actual_slot` 提取位置无关的实际输入。`slot_complete` 覆盖所有这样的可行类型槽。位置在实际槽确定后选择，`ActualBadSlot.slot_weight_lower` 在所选位置提供这对真实边两个方向的删除权重；其余坏对权重非负。

原始三个代表分别有 2401、16、448 种槽组合，共 2865 种。统一为每个中心 `Fin 7` 的槽域（较小域重复首项）后，共 7203 种输入；所有输入在 Lean 中完整验证。重复的选择合并后为 55 个代表/位置配置、383 个配置/扣除证明行。精确最大上界是 `4137/4199 < 1`。这里枚举的是局部类型槽，不是整图。

`counts_eq_catalog` 将本支的三代表直接连接根侧完整四低分类。`profile_valid`、`profiles_calculated`、`abc_exact`、`weights_exact` 检查实际类型剖面与有理数公式；`choice_exact` 检查槽选择，`strict_cached` 检查全部严格界。最终调用 `CustomDeletion.propertyB_of_custom_deletion`，接口不留下槽、位置、概率界或内部证书假设。

数据由 `computations/propertyb33/round02/generate_v23_four_low_unit.py` 从 `context/propertyb33/round01/large-math/FOUR_SIX_ALL_CODEGREES_V23.json` 的前三代表生成，精确复算与旧有界逐项一致；生成器和 JSON 不属于最终定理的信任前提，Lean 内核重新检查覆盖与算术。

## 验证记录

已完成：

- `lake build Aris4Math.ThirtyThree.TwentyThreeFourLowUnitNumeric Aris4Math.ThirtyThree.TwentyThreeFourLowUnitChoice`：exit 0，1002 jobs；日志 `data-build.log`。Numeric 317 秒、Choice 1765 秒（墙钟含同时构建带来的资源竞争）。
- `lake build Aris4Math.ThirtyThree.TwentyThreeFourLowComplete`：exit 0，1008 jobs；日志 `complete-build.log`。Unit 实际调用 6.7 秒、完整组合 2.5 秒。
- `lake env lean ../context/propertyb33/round02/four-low-unit/ImportAudit.lean`：exit 0；日志 `import-audit.log`，检查完整定理类型，并实际调用 Unit 与 Complete 两个接口。
- 最终定理、槽覆盖、槽选择、权重公式的传递公理只有 `propext`、`Classical.choice`、`Quot.sound`。本支无 `sorry`、`native_decide` 或新增公理。

完整四低分支的最终入口是：

```lean
TwentyThreeFourLowComplete.propertyB_of_four_sixes
  (H : Simple5Hypergraph (Fin 23))
  (cover : H.PairCovering) (edges33 : H.edges.card = 33)
  (many4 : 4 ≤ H.sixVertices.card) : PropertyB H
```

它调用已构建的 `TwentyThreeFourLowActual.propertyB_or_unit_counts`，将 47 个非单位代表和本支三个单位代表合并。接口不保留选点、计数代表或单位共度前提。此记录验证四低分支；完整 T33 由总装配另行验收。独立导入是在本机完成，不表示另一机器或外部人工重建。
