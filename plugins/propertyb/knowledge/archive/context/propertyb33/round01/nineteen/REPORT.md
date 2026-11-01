# T33 的十九点分支：已完成实际 Lean 连接

日期：2026-10-07。范围：任意 `Simple5Hypergraph (Fin 19)`，边数至多 33。

## 导出结果

```lean
Aris4Math.ThirtyThree.Nineteen.nineteen_propertyB
  (H : Simple5Hypergraph (Fin 19))
  (hE : H.edges.card ≤ 33) : PropertyB H
```

没有点对覆盖、类型表、概率界、结构证书等额外前提。它连接实际边集的计数、实际无锁排列中的临界事件、严格概率界和原对象的 Bool 染色见证。该分支完成，不表示其他顶点数或完整 T33 已完成。

新源码：

- `formal/Aris4Math/ThirtyThree/GlobalPairs.lean`
- `formal/Aris4Math/ThirtyThree/Nineteen.lean`

原源码、旧 Main 与旧 32 边结果均未修改。使用 ARIS `lean-formalize` 的实际输入连接和导入/公理审计流程。当前属于实现者核验，外部 Grok/Gemini 对新源码的审阅仍由主代理安排。

## 数学连接

令 S 为所有有序不同边对 (e,f) 的 `choose(|e∩f|,2)` 总和。原 `GlobalPairs` 的真实双计数和整数不等式给出：

`20 |E| ≤ S + 2 choose(v,2)`。

新 `intersection_sum_lower` 已对任意有限顶点类型证明此式。若 v=19、|E|=33，则 S≥318。不同五元边的交集至多4，单交贡献0，其余每对至多6，故至少53个有序不同边对不是单交；总有序不同边对1056，于是单交对数至多1003。

这里采用足够的较松界 **1003**，不把准备阶段更强的纸面奇偶性取整 **1002** 冒充已形式化。边数≤32时，总有序不同边对本来就≤992，因此统一得到≤33边的单交对上界1003。

复用 `NoLocks.endpoint_ratio`、`NoLocks.critical_ratio_le` 和非单交概率为零的结果，对实际边集逐位置得到 A、B、C：

- A、B 的乘数为33；
- C 的乘数为1003；
- 在每个位置重新取 min(A,B,C)。

新的内核精确算术声明 `nineteen_sum_value` 得到：

`sum min(A,B,C) = 228354 / 230945 < 1`，余量 `2591 / 230945`。

该数比准备稿 cap1002 所得 `228291/230945` 略松，仍严格小于1。内核计算仅涉及十九个明确有理数公式，没有枚举超图、染色或排列。

最后使用原 `ConditionalUnion.propertyB_of_position_bounds`，其实际失败事件覆盖、随机空间非空和染色拉回均已证明。没有经过写死32边的 `Numeric.validProfile` / `TypeCounting.RealizesProfile` 接口；所以此分支不需要先泛化整个锁点引擎。

## 执行证据

在项目 `formal/` 下，设置项目本地 ELAN_HOME/PATH 后：

```sh
lake build Aris4Math.ThirtyThree.Nineteen
lake env lean ../context/propertyb33/round01/nineteen/import-audit.lean
```

构建成功：`build-r1.log`、`build-final.log`。独立导入成功：`import-audit.log`。导入文件另将命题直接重述为任意不同五元边集 E，|E|≤33，存在每条边红点数介于1与4之间的 Bool 染色。

实际导出定理、精确分数声明和独立重述的传递公理均只有：

`propext`, `Classical.choice`, `Quot.sound`。

没有 `sorry`、`sorryAx`、新增未证公理或 `native_decide`。这是本机增量构建和独立导入，不代表另一机器独立重现或外部模型已经审阅新源码。

## 剩余义务与下一步

本分支没有剩余数学假设。主代理可以将 `nineteen_propertyB` 接入新有限目标的 v=19 分支。其他20–25点分支、全称归约及 T33 主定理仍各自待完成。cap1002 的奇偶性加强可按后续实际用途决定，本分支不需要它。
