# 真实条件排列试验到 Property B

## Claim / Status

[ConditionalUnion.lean](../formal/Aris4Math/ConditionalUnion.lean) 已把实际贪心算法、真实锁定排列概率、单边端点事件、有序不同边对事件、按位置取最小值，以及最终合法染色存在性连接起来。另已连接实际非单交坏边对的加权删除。

**这些一般连接定理已经 Lean 内核核查。** `lake build Aris4Math.ConditionalUnion` 成功；打印的六条主要定理均只依赖 `propext`、`Classical.choice`、`Quot.sound`。无 `sorryAx`、新增公理、`native_decide` 或全排列枚举。日志见 [lean-conditional-build.log](../.aris/traces/proof-checker/2026-10-06_run07/lean-conditional-build.log)。

主命题 T 仍需各顶点数的结构选点、类型与数值对应、坏对权重下界实例化；本模块不把这些结论冒充已知。

## Main Interface

命名空间 `Aris4Math.ConditionalUnion` 的 `propertyB_of_position_bounds` 接受：

- 原对象 `H : Simple5Hypergraph (Fin v)`，不额外要求正则、线性或点对覆盖。
- 真实锁定顶点与位置的两条单射 `vertices positions : ι ↪ Fin v`。
- 逐位置有理上界 $A_k,B_k,C_k$。
- 对每个 $k$，实际单边最后点概率和不超过 $A_k$，实际单边第一点概率和不超过 $B_k$，实际 `H.edges.offDiag` 中不同有序边对的 critical 概率和不超过 $C_k$。
- 严格不等式 $\sum_k\min\{A_k,B_k,C_k\}<1$。

结论是原定义 `PropertyB H`。这里的输入界都是尚需应用层核查的具体算术/结构义务；实际贪心失败覆盖、端点事件支配、union bound、取最小值、非空样本和最后染色存在性均已在模块内部证明，不作为外部假设。

`propertyB_of_weighted_position_bounds` 再接受每个位置的实际有序边对记账权重 $w_k(p)$、不同有序坏对的 Finset $D_k$，以及：

1. 每个实际 critical-pair 概率不超过其记账权重。
2. 全部记账权重之和不超过 $C_k$。
3. $D_k\subseteq H.edges.offDiag$，其中每个边对的原始交集大小不为一。
4. 实际被删除权重和至少为 $d_k$。
5. $\sum_k\min\{A_k,B_k,C_k-d_k\}<1$。

其结论仍为 `PropertyB H`。这里不假定“扣除 $d_k$ 就使最小值下降 $d_k$”，而是先使用 $C_k-d_k$ 再取最小值。Finset 保证同一位置的有序边对只删除一次；权重允许为零，也允许两个方向不同。

## Proof and Dependencies

1. `lockedRatio_union_bound` 在真实 `Locked` 样本上用有限事件覆盖和基数不等式证明 union bound，然后除以同一真实样本基数。
2. `critical_ratio_le_endpoint_sum` 使用已证 `critical_implies_endpoints`，分别选出实际 critical pair 的末端边、首端边。
3. `critical_ratio_le_pair_sum` 直接以原始不同有序边对 `E.offDiag` 覆盖 `Greedy.CriticalAt`，保持方向和原边身份。
4. `failure_ratio_le_critical_sum` 调用已证明的真实贪心 `failureAt_covered`，覆盖所有失败排列。
5. `failure_ratio_le_position_bounds` 将三种界施加于同一个位置事件，再求最小值、对全部位置求和。
6. `propertyB_of_failure_ratio_lt_one` 利用点锁样本的阶乘计数保证其非空。如果不存在合法染色，每个样本中的贪心输出都失败，失败概率必为一，与严格上界矛盾。成功排列到原 `PropertyB` 定义的转换使用 `Greedy.propertyB_of_successful_permutation`。
7. `pair_sum_le_weighted_deletion` 对已识别的原始非单交边对使用 `critical_ratio_zero_of_intersection`，从实际概率和中去掉这些零项，再调用已核查的通用加权删除不等式。

所有步骤对任意有限规模成立。代码未展开全部排列，也没有把数值计算结果或模型意见作为任何证明前提。

## Application Coordination

`NoLocks.lean` 负责无锁情况下真实自由部分/位置数与 Numeric 公式的对应，以及 v19 的具体 $32/992$ 系数和闭合数值。`LinkCounting.lean`、后续全局坏对计数负责实际坏对数目的结构下界；这些结果可以通过本模块的加权接口连接。

本模块未修改 `Numeric.lean`，没有与其形成循环依赖。导入链为 `ConditionalUnion → CriticalCounting → EndpointCounting/JointCounting/Greedy`。

## Reproduction

```sh
cd /Users/rfy_naiveai/Desktop/aris4math/formal
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
lake build Aris4Math.ConditionalUnion
```
