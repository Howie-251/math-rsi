# T33 的完整有限归约已在 Lean 验证

日期：2026-10-07。范围：新目标的定义、≤18点排除、最小反例及19–25点归约；不包含尚未解决的七个有限分支。

## 实际结果

新增源码：

- `formal/Aris4Math/ThirtyThree/Target.lean`：`Aris4Math.Target33` 定义任意有限顶点类型上的简单五元超图、≤33边、Property B 的原始全称命题。
- `formal/Aris4Math/ThirtyThree/Reduction.lean`：证明原命题与 `Aris4Math.ThirtyThree.FiniteGoal` 等价。FiniteGoal 是19–25点、恰33边且覆盖点对时的可染性，当前仍是未证明的命题。

新代码没有修改旧源码或默认构建目标，不依赖旧 `Aris4Math.Main` 的主定理。恰33边通过同顶点集补入不同五元边得到，不要求调用旧T32。

## 实际输入与归约连接

| 声明（均在 `Aris4Math.ThirtyThree`） | 实际前提 | 已证明结论 |
|---|---|---|
| `card_le_twenty_five` | 原始H、点对覆盖、≤33边 | 顶点数≤25 |
| `balanced_count_strict` | 9≤v≤18 | 33倍单边单色事件计数小于v! |
| `propertyB_of_vertices_le_eighteen` | 任意Fin v上H、v≤18、≤33边 | Property B，无点对覆盖前提 |
| `exists_minimal_counterexample` | 任意有限V上H、≤33边、不可染 | 最少顶点的Fin v反例 |
| `minimal_counterexample_pair_covering` | 上述最小性 | 每个不同点对在某边中 |
| `exists_extension_33` | v≥8、≤33边 | 相同顶点集上的33边超图，包含原边集 |
| `exists_nineteen_to_twenty_five_counterexample` | 任意有限V上H、≤33边、不可染 | 19≤v≤25、恰33边、覆盖点对、不可染的实际K |
| `target_of_finite_goal` | **FiniteGoal仍是显式前提** | Target33 |
| `target_iff_finite_goal` | 无 | Target33 ↔ FiniteGoal，含任意宇宙层数的正向提升 |

整数度是上界归约的关键：若v≥26，则点对覆盖给出v−1≤4d(x)，自然数算术推出每点d(x)≥7。求和得到7v≤5m≤165，与v≥26矛盾。代码没有用不足以排除26的v(v−1)≤660替代此步。

小顶点证明复用旧模块中不绑定32的真实排列事件计数引理。新标量定理直接内核计算v=9,…,18的10个整数不等式；它没有枚举超图、染色或排列。

## 运行证据

在项目根目录启动：

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
cd formal
lake build Aris4Math.ThirtyThree.Reduction
lake env lean ../context/propertyb33/round01/reduction/ImportAudit.lean
```

- `build.log`：新模块构建成功，退出码0。
- `ImportAudit.lean` / `import-audit.log`：单独导入新模块，打印实际Target33与FiniteGoal的定义、归约声明类型及传递公理；通过真实caller把有限分支前提连接到展开的Bool染色结论，退出码0。
- 核心归约的传递公理仅 `propext`、`Classical.choice`、`Quot.sound`；纯标量定理只依赖 `propext`。
- `build-initial-error.log` 保存第一次编译时自然数自强制转换未化简造成的算术错误；补 `Nat.cast_id` 后修复。该失败日志中的临时 `sorryAx` 是Lean在报错后生成的占位错误结果，不属于已成功构建的当前声明。

这是现有锁定环境上的增量构建和独立导入，不宣称干净缓存重建或另一台机器独立复现。没有新增公理、`sorry` 或 `native_decide`。

## 下一义务与审阅状态

需要证明 `FiniteGoal`，即为19、20、21、22、23、24、25各分支给出33边的新实际证明；本归约不能自行提供这些证明。随后将新 `finite_goal` 交给 `target_of_finite_goal`，才能得到全称Target33。

本实现为同家族代理完成，代码及真实日志已交主代理作为跨家族A/B审阅材料。此报告不自行记Grok或Gemini审阅通过；主代理应保存它们对实际源码的回应和处置。
