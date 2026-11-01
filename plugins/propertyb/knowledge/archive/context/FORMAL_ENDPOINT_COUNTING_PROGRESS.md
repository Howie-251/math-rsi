# 真实端点与 critical-pair 事件的 Lean 计数

## Claim / Status

`EndpointCounting.lean` 与 `CriticalCounting.lean` 已核查真实锁定排列样本上的 P2 单边端点、P3 自由中心固定单交边对、P4 锁定中心固定单交边对的概率公式。**这些计数定理已证明；主命题 T 尚未由它们单独得到。**

最终命令 `lake build Aris4Math.EndpointCounting Aris4Math.CriticalCounting` 成功。两文件导出声明的公理检查只含 `propext`、`Classical.choice`、`Quot.sound`；无 `sorryAx`、新增公理、`native_decide` 或全排列枚举。实际日志位于 [lean-endpoint-build.log](../.aris/traces/proof-checker/2026-10-06_run06/lean-endpoint-build.log)。冻结源文件：[EndpointCounting.lean](../formal/Aris4Math/EndpointCounting.lean)、[CriticalCounting.lean](../formal/Aris4Math/CriticalCounting.lean)。

## Sample and Events

原顶点与排列位置均以 `Fin v` 表示，排列方向为原顶点到位置。任意有限锁标签类型 `ι` 对应两条 embedding：`vertices positions : ι ↪ Fin v`。`Locked vertices positions` 的元素是满足全部点像条件的真实原排列。

`lockedRatio vertices positions P` 定义为该样本中满足原排列事件 $P$ 的个数除以样本总数。计数公式没有被当成该定义的前提。

- `EndpointAt A σ k true/false` 表示 $A$ 的最后点/第一点位于 $k$。`endpointAt_true_iff`、`endpointAt_false_iff` 已证明它们分别等价于 $k\in\sigma(A)$ 加全部点位置不大于/不小于 $k$。
- `SeparatedAt A B x σ k` 表示 $\sigma(x)=k$，$A\setminus\{x\}$ 的点全在 $k$ 前，$B\setminus\{x\}$ 的点全在 $k$ 后。
- 在 $A\ne B$、$A\cap B=\{x\}$ 下，`separated_iff_critical` 证明它恰好等价于已经核查的 `Greedy.CriticalPair (A.map σ.toEmbedding) (B.map σ.toEmbedding) k`。因此 P3/P4 的左端是贪心证明实际使用的事件，不是代理定义的另一个事件。

## Proved Interfaces

`Aris4Math.EndpointCounting` 提供：

- `extraLockEquiv`：原样本中的 $\sigma(x)=k$ 纤维与增加一条锁后的样本显式双射。
- `extra_lock_ratio`：自由点落到指定自由位置的精确比为 $1/N$。
- `extraLockEventEquiv`、`extra_lock_event_ratio`：任何强制 $\sigma(x)=k$ 的真实事件，原样本概率等于新样本概率乘 $1/N$。
- `lockedRatio_congr_on`、`lockedRatio_zero`：仅在实际锁定样本上验证事件相等或不可能，即可搬运概率或证明为零。

`Aris4Math.CriticalCounting` 提供：

| 定理 | 已核查内容 |
|---|---|
| `all_before_iff` / `all_after_iff` | 真实全边位置不等式等价于锁点顺序兼容加自由点占位条件 |
| `locked_critical_ratio` | P4：中心是指定锁点的真实固定单交边对概率；锁点顺序不兼容时为零 |
| `free_critical_ratio` | P3：共同点和中心位置均自由时的真实固定单交边对概率；不兼容时为零 |
| `fixed_free_endpoint_ratio` | 固定一个实际自由端点时的概率，没有端点选择倍数 |
| `endpointFibersEquiv` | 单边端点事件按其唯一原顶点作不交分割 |
| `free_endpoint_ratio` | P2a：通过该分割产生恰好 $r$ 个端点选择倍数 |
| `fixed_locked_endpoint_ratio` / `locked_endpoint_ratio` | P2b：核查锁中心属于该边及其他锁点顺序后得到单侧二项式比 |
| `critical_implies_endpoints` | 实际 critical pair 蕴含对应的单边最后点和第一点事件 |
| `critical_intersection_card` / `critical_ratio_zero_of_intersection` | 非单交原始边对的实际 critical 事件概率为零 |

## Formula Meaning

令 $N=v-|\iota|$。P3 中用 $r_0,q_0$ 表示两条边删除共同点后各自剩余的自由点数；$a,b$ 为中心前后自由位置数。`freeLocationWeight` 是

$$
\frac{\binom a{r_0}\binom b{q_0}}
{N\binom{N-1}{r_0}\binom{N-1-r_0}{q_0}}.
$$

这与纸面 P3 的 $r_0=r_T-1$、$q_0=r_U-1$ 一致。共同点由固定单交边对唯一决定，因此推导中只有一次额外点锁的 $1/N$；没有 $r_T r_U$ 倍数。

P4 中 $r,q$ 为自由边部分大小；`locationWeight` 是

$$
\frac{\binom ar\binom bq}{\binom Nr\binom{N-r}q}.
$$

P2a 中 $r$ 为单条边的自由部分大小，$a$ 为所需一侧自由位置数。`free_endpoint_ratio` 得到

$$
\frac{r\binom a{r-1}}{N\binom{N-1}{r-1}}.
$$

倍数 $r$ 来自已形式化的端点纤维分割，不能移植到固定边对的计算。P2b 为 $\binom ar/\binom Nr$。公式前的兼容判断与真实锁点顺序对应；P2b 还要求锁定中心实际在边内。

## Dependency and Remaining Integration

证明复用已冻结的 `Counting.lean` 和 `JointCounting.lean` 的一般双射与精确计数；P3 的额外锁推导还证明增加中心锁不改变严格前后允许位置数，以及不改变已删除共同点后的自由边部分大小。最终概率是这些已证等价、计数和阶乘归一化的组合。

当前尚未导入 `Numeric.lean`。后续必须核查：

1. `Fin v` 的零基位置与 Numeric 一基位置列表的对应；实际锁点集合、自由边部分基数与 `5 - t.locks.length` 的对应。
2. 将实际顺序兼容条件、真实单交所强制的条件，接到 Numeric 所有 guards，包含共同点与已锁中心不一致时事件为空的分支。
3. 将实际 `CriticalAt` 的概率按单边、不同有序边对、位置逐层取 union bound；接入类型分组、坏对扣除、结构选点和闭合数值证书。

下一独立模块为 `ConditionalUnion.lean`，负责真实锁定样本的 union/min 到 Property B；`NoLocks.lean` 将由另一代理负责无锁概率识别及 v19 数值桥，避免重复实现。

## Reproduction

```sh
cd /Users/rfy_naiveai/Desktop/aris4math/formal
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
lake build Aris4Math.EndpointCounting Aris4Math.CriticalCounting
```

仍使用项目固定 Lean 4.24.0 / Mathlib 版本，没有修改 Numeric、主模块或依赖版本。
