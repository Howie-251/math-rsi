# v24 四锁标签与 Numeric 类型表桥

已完成并冻结：

- `formal/Aris4Math/TraceRecovery.lean`：任意 `n` 个同度锁点的真实迹计数恢复和完整块族恢复。
- `formal/Aris4Math/K4Profiles.lean`：实际四锁集的三型标签、准确类型表和现有 Numeric 证书连接。

关键最终接口：

```lean
Aris4Math.K4Profiles.exists_realized_bounded_profile24
  (H : Simple5Hypergraph (Fin 24))
  (cover : H.PairCovering) (edges32 : H.edges.card = 32) :
  ∃ p : Numeric.Profile, ∃ vertices : Fin 4 ↪ Fin 24,
    TypeCounting.RealizesProfile H vertices positions24 p ∧
    p.emptyPairCap = none ∧ p.correctionCenters = [] ∧
    Numeric.totalBound p < 1
```

`positions24 i` 是零基位置 `i.val + 10`，对应 Numeric 的一基位置 11,12,13,14。`profile24` 按三个索引选择已有 `v24_K4_1`、`v24_K4_2`、`v24_K4_3`，没有改写 Numeric 数据。

`Structure.exists_four_six_degree_codegree_one` 先产生真实四点锁集。`Traces.classify_four_lock_traces` 给出三种实际块族；`classify_four_labels` 构造真实等价 `label : ↥W ≃ Fin 4`，使完整多点迹块族恰好等于相应标号代表。三元块的标号由一般纤维同构定理给出，二元块通过真实点对覆盖唯一恢复。

通用 `TraceRecovery.actual_recovered_count` 证明实际超图所有空、单点和多点类型的重数公式。`numeric_counts_match` 仅对三个固定参考型的 16 个类型核对公式与现有 Numeric 表；此数据检查不替代真实超图计数证明。`actual_entry_count` 与 `actual_entries_cover` 再给每个表项的真实纤维重数和实际全部边的覆盖，构成共享 `TableRealization` / `RealizesProfile`。

严格小于一的结论复用已有三个 Numeric 有理数证书。未使用抽样、任意块族穷举、超图穷举、`sorry`、`admit`、新公理或 `native_decide`。

验证：`lake build Aris4Math.K4Profiles` 成功，最后模块实际编译 4.2 秒。两个新增文件的 8 条关键公理审计仅 `propext`、`Classical.choice`、`Quot.sound`，构建无警告。日志及结构化记录在 `.aris/traces/proof-checker/2026-10-06_run07/lean-k4-profiles-*`。

本模块闭合 v24 的结构到精确类型表、再到数值严格界的链条。后续主代理已在 `LargeVertices.twenty_four_propertyB` 中通过通用概率模块接到原 Property B，顶层假设只剩该分支的 H、点对覆盖和 32 边。原 Target 的全局装配仍由主代理汇总。
