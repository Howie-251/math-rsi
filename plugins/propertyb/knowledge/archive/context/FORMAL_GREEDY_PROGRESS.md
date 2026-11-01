# P1 贪心算法的 Lean 核验

2026-10-06。**实际算法、P1 失败覆盖以及成功输出到 Property B 的接口均已编译通过。**
源文件已冻结供跨模型审阅；本记录不将主目标 T 标为已形式化证明。

源文件：[formal/Aris4Math/Greedy.lean](../formal/Aris4Math/Greedy.lean)。
最终成功日志：[lean-greedy-build.log](../.aris/traces/proof-checker/2026-10-06_run04/lean-greedy-build.log)。

## 实际定义与正文对应

顶点为 `Fin v`，以 `0,…,v−1` 表示扫描位置；正文 `1,…,v` 仅相差位置标签。
`blueAfter E 0 = ∅` 表示初始全红。
从时刻 `t` 到 `t+1`，若 `t<v`，只检查顶点 `x=t`：当且仅当存在
`A∈E` 满足 `x∈A`、`∀y∈A,y≤x` 且 `∀y∈A,y∉blueAfter E t` 时，将 `x`
插入蓝点集；否则状态不变。超过最后一个顶点后，状态保持不变。
这是正文的全红起点、只向蓝翻色、以当前全红边的末点为翻色条件的算法。

该数学定义使用 Lean 的 `noncomputable` 与经典可判定性，不把计算机实际运行的
某个染色输出当作证据。全部后续性质从递归方程证明；这里无需执行遍历所有超图。

`σ : Equiv.Perm (Fin v)` 的方向固定为**原顶点到位置**。
`orderedEdges E σ` 将每条边的顶点映到对应位置，随后运行上述已证明的有序扫描。
`FailureAt E σ` 是这个实际输出存在单色边。
最后的 Property B 接口把位置颜色通过 `σ` 拉回原顶点，没有增加均衡染色条件。

## 已完成的证明链

| 定理 | 已证内容 |
|---|---|
| `blueAfter_step_subset`、`blueAfter_mono` | 蓝点集随扫描单调增加 |
| `blueAfter_mem_before` | 蓝点一定已经被扫描：`x.val < t` |
| `blueAfter_of_flip` | 满足翻色条件的当前点确实进入蓝点集 |
| `blueAfter_mem_witness` | 任意蓝点都有在自己被扫描时成立的真实全红见证边 |
| `no_all_red_edge` | 每条非空边最终含有蓝点；不需要均匀性 |
| `all_blue_implies_critical_pair` | 大小至少2的全蓝集合取首点后，真实翻色见证给出临界边对 |
| `critical_pair_endpoints` | 临界对中的顺序条件确实等价于所需 `max A=x=min B` |
| `uniform_failure_covered` | 对任意 `n≥2` 的均匀超图，算法失败推出不同的两条边及其单交中心 |
| `orderedEdges_uniform`、`failureAt_covered` | 顶点按任意排列重标后，均匀性及 P1 保持；结论保留原边身份 |
| `failure_event_cover` | 对任意有限排列样本 `sample`，真实失败事件包含于各位置临界对事件之并 |
| `propertyB_of_successful_permutation` | 五元超图的成功排列产生原 `PropertyB` 定义要求的每边1至4个红点 |

`CriticalPair A B x` 明确包含：`A≠B`、`x∈A∩B`、
`∀y∈A,y≤x`、`∀y∈B,x≤y`、`A∩B={x}`。
不同边这一点由全蓝边大小至少2和交集为单点推出，没有省略 `n≥2`。

`failure_event_cover` 的样本空间可以是任意固定锁点条件筛出的排列集合。
它不要求样本包含所有排列，也不要求样本非空；因此条件化不需要额外假设事件覆盖。
样本的非空性与大小计数属于后续概率应用。

形式证明没有将失败覆盖作为输入。
`uniform_failure_covered` 的输入只有超图、均匀性、`n≥2` 和实际算法失败；
`propertyB_of_successful_permutation` 的输入是实际算法不失败，
再在证明中构造布尔染色并证明每边红点计数，未假设存在合法染色。

## 编译证据与剩余范围

从 `formal/` 运行：

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
lake build Aris4Math.Greedy
```

最终新模块编译耗时3.2秒。十个关键定理的 `#print axioms` 均仅列出
`propext`、`Classical.choice`、`Quot.sound`。
源码不含 `sorry`、`admit`、新增公理或 `native_decide`。
沿用 Lean 4.24.0 与先前固定的 Mathlib v4.24.0；本轮没有更换工具链。

尚未由此文件证明的内容是：P2–P4 条件排列精确权重、P5 类型计数、
P6/P8/P9 具体删除输入、19–25点的结构选点与全部数值分支，
以及任意有限顶点类型到 `Fin v` 的最终规格桥。
其他模块可能正在推进这些义务，本文件的范围不据此扩大。
整个 T 仍需完成其余依赖的形式化拼接与语义核对。
