# 实际迹计数与 Numeric 类型表的连接

`formal/Aris4Math/TraceProfiles.lean` 已完成 v25 分支并冻结，共 402 行。最终接口：

```lean
exists_realized_bounded_profile25
  (H : Simple5Hypergraph (Fin 25))
  (cover : H.PairCovering) (edges32 : H.edges.card = 32) :
  ∃ p : Numeric.Profile, ∃ vertices : Fin 6 ↪ Fin 25,
    TypeCounting.RealizesProfile H vertices positions25 p ∧
    p.emptyPairCap = none ∧ p.correctionCenters = [] ∧
    Numeric.totalBound p < 1
```

`positions25 i` 的零基位置为 `i.val + 9`，对应 Numeric 的一基位置 10,...,15。`lockVertices W label i = (label.symm i).val`，即来自真实六点锁集和已证明的标签双射。

证明没有把表中类型数作为假设。`actual_recovered_count` 对任意实际迹类型推导：大小至少二的类型由共度一给出 0/1；单点类型由实际度数减去实际多点块次数；空类型由真实总边数扣除所有非空类型。`numeric_counts_match` 只验证九个固定参考配置的 64 个类型与已有 Numeric 表一致。此固定数据验证使用 `decide +kernel`，不枚举任意超图、染色或排列。

`actual_entry_count` 证明每个现有 Numeric 列表条目的真实边纤维数等于 `t.count`；`actual_entries_cover` 证明每条真实边的类型都在该列表中。列表标签不重复、合法锁位和排序来自固定表的内核证明，并转换为共享 `TypeCounting.TableRealization`。随后 `realizes_profile_of_representative` 给出完整的共享 `RealizesProfile`。

本模块直接复用 `TypeCounting.lockSignature`，自己的 `lockedLabels` 只是缩写。实际类型以 `Finset (Fin 6)` 表示，经过一基位置映射并规范排序后与 `TypeCounting.positionType` 完全相等。

从 `K6Traces.exists_full_labeled_six_good_locks` 得到真实代表，排除不合格类型后，`profile25_lt_one` 复用现有 Numeric 精确有理数证书。没有重新假设 Numeric 概率公式对实际随机实验有效。

验证：`lake build Aris4Math.TraceProfiles` 成功，最后实际模块编译 11 秒；8 条关键公理审计均只有 `propext`、`Classical.choice`、`Quot.sound`。未使用 `sorry`、`admit`、新公理或 `native_decide`。最终构建与审计存放在 `.aris/traces/proof-checker/2026-10-06_run07/lean-trace-profiles-*`。

本模块负责真实结构与类型表的连接；后续主代理已在 `LargeVertices.twenty_five_propertyB` 中通过通用概率模块接到原 Property B，顶层假设只剩该分支的 H、点对覆盖和 32 边。原 Target 的全局装配仍由主代理汇总。

v24 后续桥也已完成，见 `context/FORMAL_K4_PROFILES_PROGRESS.md` 与 `formal/Aris4Math/K4Profiles.lean`；两个分支向概率桥提供相同的 `RealizesProfile` 接口。
