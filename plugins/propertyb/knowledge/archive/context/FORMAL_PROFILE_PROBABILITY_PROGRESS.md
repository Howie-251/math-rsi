# 实际锁定排列概率与 Numeric 公式的通用连接

2026-10-06；源码 `formal/Aris4Math/ProfileProbability.lean`。

核心接口位于 `Aris4Math.ProfileProbability`：

- `endpoint_ratio_numeric`：真实五元边的首端/末端事件概率 **等于** `Numeric.edgeWeight p t (k.val+1) last`。
- `free_critical_ratio_numeric`：实际单交边对的交点及目标位置均自由时，真实临界概率 **等于** P3 的 `Numeric.pairWeight`。
- `locked_critical_ratio_numeric`：实际单交点为某锁定顶点，目标为其锁定位时，真实临界概率 **等于** P4 的 `Numeric.pairWeight`。
- `critical_ratio_le_numeric`：任意不同真实边对的临界事件概率 **至多** 为其 Numeric 类型权重。

所有接口接受真实超图 `H`、两份单射 `vertices positions`、`hp : TypeCounting.RealizesProfile H vertices positions p`、实际边成员关系，以及 `t.locks = positionType vertices positions A`（第二条边同理）。不要求 `t.count` 或 `u.count` 非零，因此可直接使用类型聚合层的 count-0 虚拟参数；这些参数只承载已经由实际边导出的锁定位置列表。

`RealizesProfile` 是实际几何和计数的规格：顶点数一致、位置列表有效且对应实际单射、表覆盖实际边且具有准确重数。它没有概率假设，不能凭数值表成立就擅自假设任意超图具有该 realization；各结构分支仍须构造它。

## 已完成的语义对应

1. 实际类型的成员正是“某锁定顶点在边中，标签为其从 1 开始的位置”。位置标签单射，类型长度等于边中锁定顶点数。
2. 实际自由顶点数为 `p.v − p.positions.length`；一条五元边的自由部分基数为 `5 − t.locks.length`。
3. 目标位置前后的实际自由槽数等于 `Numeric.leftCount/rightCount`，包含从 `Fin v` 的 0 开始位置到 Numeric 的 1 开始位置转换。
4. `List.all` 的先后条件、删去锁定中心后的先后条件，分别等价于实际 `LocksBefore/LocksAfter` 条件。
5. 自由单交点使两类型不共享锁；锁定单交点使类型的共同位置列表恰为该位置的单元素列表。证明依靠实际边交集和位置单射。
6. P3/P4 中自由顶点容量限制来自实际自由部分的并集基数上界；没有把公式中的兼容 guard 当额外前提。
7. 非单交边对的临界事件为零。单交点与目标位置的锁定状态不匹配时，利用排列单射和实际锁约束证明事件为空。这些分支再由 Numeric 权重非负性得到统一上界。

整个模块没有使用 `decide +kernel` 枚举、超图穷举、`native_decide` 或外部计算假设；证明使用有限集对应、基数恒等式、自然数算术和已核验的排列计数公式。

## 验证及边界

全部 26 个定理已通过真实 Lean 编译和导入后 `#print axioms`；重编译 5.168 秒、导入审计 4.372 秒，退出码均为 0。只依赖标准 `propext`、`Classical.choice`、`Quot.sound`，无 `sorry` 或新增公理。

构建与审计证据在 `.aris/traces/proof-checker/2026-10-06_run07/`，文件前缀 `lean-profile-probability-`；包括实际命令、退出码、完整输出和全部定理的导入审计。

本模块实现概率公式的语义连接。每个顶点数分支还须提供实际 `RealizesProfile`、必要的 link 扣除以及最终严格总界；完整原目标由最终组合模块另行证明。
