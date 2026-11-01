# 实际锁点逐层提升接口

模块：`formal/Aris4Math/ThirtyFour/LockExtension.lean`。此接口为21点 δ7 和23点 few-low 的真实迹分类提供逐层覆盖恒等式，不产生新的数值表，也不预设某张局部表已覆盖实际输入。

对任意 `f : Fin (n+1) ↪ Fin v`，`restrict f = Fin.castSuccEmb.trans f` 保留前 n 个真实锁点。对旧迹 `T : Finset (Fin n)`，`promoted T` 是 `T.map Fin.castSuccEmb` 加上 `Fin.last n`；`promotion H f T` 定义为同一个真实 H 在该新迹上的边数。

`signature_without_iff` 与 `signature_with_iff` 在单条实际边上证明：新迹分别为旧标签集合、不含或含新增标签，当且仅当旧迹是 T，且新增实际顶点分别不属于或属于该边。这一步把类型转换与真实顶点成员关系连接起来。

随后按新增顶点的成员关系划分同一个旧迹纤维，得到：

```lean
count_split H f T :
  count H (restrict f) T =
    count H f (T.map Fin.castSuccEmb) + promotion H f T
```

直接推论为 `promotion_le_old`、`count_without_new`（旧计数减去提升数）和 `count_with_new`（含新增锁的计数恰为提升数）。减法是自然数减法，提升不超过旧计数已经由同一精确划分证明。

`sum_promotion_degree` 对全部旧迹求和，等于新增实际顶点的真实度数。求和**包含空迹**；新单点迹对应旧空迹。若局部表仅存非空旧迹的提升数，`count_new_singleton` 由实际度数减去这些提升数恢复新增单点迹的计数。

`promotion_eq_zero_of_large` 从 H 的五元性证明 `5 ≤ T.card` 时提升数为零：提升后的实际迹至少有六个互异锁点，不可能包含在一条五元边中。并未将这个零条件作为局部表的未证输入。

所有结论适用于任意 n、v，不需要点对覆盖、度数预算、34边条件或概率界。它们只建立真实输入到逐层迹提升参数的连接。后续调用者仍须证明有限提升分类的完备性、保留/拒绝分支的对应，以及严格证书如何推出原始 Property B。

## 核验状态

2026-10-14：唯一正规构建者执行 `lake build Aris4Math.ThirtyFour.LockExtension`，r19 PASS（969 jobs，新增模块1.4秒）。`count_split`、`sum_promotion_degree`、`promotion_eq_zero_of_large`、`count_new_singleton` 的传递公理均仅 `propext`、`Classical.choice`、`Quot.sound`。实际日志为 `../twentyone-lean/build-queue-LockExtension-r19.log`，本执行者已读取。原始33边模块均未修改；没有启动并行构建。

## 旧锁重标号与新增锁固定

新增 `LockLiftRelabel.lean` 用固定库的 `finSumFinEquiv : Fin n ⊕ Fin 1 ≃ Fin (n+1)` 共轭 `σ ⊕ id`，构造 `lift σ`。`lift_castSucc` 与 `lift_last` 分别证明旧标签按 σ 移动、新增末标签固定；`restrict_lift_trans` 证明这个操作在实际扩展嵌入 f 上限制为原 n 锁重标号，`new_vertex_lift_trans` 保留同一个新增实际顶点。此连接供23点4→5、5→6逐层分类调用。

唯一正规构建者r22核验通过（970 jobs，新增模块1.1秒），`restrict_lift_trans` 的传递公理仅 `propext`、`Quot.sound`。本执行者已读取 `../twentyone-lean/build-queue-LockLiftRelabel-r22.log` 的成功及公理记录。
