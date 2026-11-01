# 六点块族解析分类的 Lean 进展

本轮完成三个模块：

- `formal/Aris4Math/BlockClassification.lean`：一般线性块族的计数与标签同构原理。
- `formal/Aris4Math/K6Classification.lean`：六点大块族的九型完备分类、实际标签等价及二元块唯一恢复。
- `formal/Aris4Math/K6Traces.lean`：把分类接到实际超图的六点锁集和完整多点迹块族。

源码已冻结，供主代理与跨模型审阅者核对。没有修改冻结的主目标、Greedy、Reduction、SmallVertices、Structure、Traces 或 Numeric 模块。

## 已证明的最强接口

`Aris4Math.K6Traces.exists_full_labeled_six_good_locks`：对于任意有限顶点类型 `V` 上的实际 `Simple5Hypergraph V`，若 `H.PairCovering`、`H.edges.card = 32`、`Fintype.card V = 25`，则存在：

1. 真实顶点子集 `W`，大小为六，每点实际度数为六，且内部实际共度均为一；
2. 代表索引 `k : Fin 9`，满足 `k ≠ 2`、`k ≠ 3`；
3. 真实等价 `label : ↥W ≃ Fin 6`；
4. 精确集合等式：`(H.multiTraces W).image (labelBlock W label) = fullRepresentative k`。

这里 `labelBlock` 把真实块限制到 `W` 的子类型后沿 `label` 映射；`fullRepresentative` 包含纸面的大块及所有未被大块覆盖的二元块。分类、标签存在或覆盖结论均不是该定理的假设或某个证书字段。

## 数学证明路径

最大块为五时，由两块大小和至多为七，排除所有其他大小至少三的块。最大块为四时，其他大块必须是含两个外部点的三元块，且这样的块至多一个。

全部大块为三元块时，先将过某一点的三元块删去该点，利用余下二元集两两不交，证明每点至多属于两个三元块；双计数再给出三元块总数至多四。两个不交三元块填满六点，排除第三个三元块。因此三块及四块情形中，每对块都恰交一点。

标签唯一性由通用纤维匹配引理证明：每点出现次数至多二时，总点数、每块大小和每对块交数决定所有精确成员模式的点数。`exact_fibers_of_upper_fibers` 对子集余大小作强归纳，从上方纤维计数推出精确纤维计数；`Equiv.ofFiberEquiv` 再产生真实点集双射。三元块三块型及四块型据此映射到纸面三角形与 K4 对偶代表。

`classify_six` 实际涵盖九型。`classify_good_six` 利用已有 `¬ Avoidance.TwoTripleShape` 排除两个三元块的相交型和不交型。这比仅排除纸面 K6-4 更强，来源是已经证明的七点删点引理，不是额外的超图假设。

`recover_pairs` 从真实点对覆盖、块大小至少二及线性条件，证明所有二元块恰为尚未被大块覆盖的点对。`labeled_traces_recovered` 将它应用到真实的 `H.multiTraces W`。

## 标签约定

Lean 顶点标签为 `0,...,5`，对应纸面 `1,...,6`；代表索引 `k=0,...,8` 对应纸面 K6-1,...,K6-9。定义逐项使用 `proofs/STRUCTURE_24_25.md` 表中的九个大块代表。`k=2,3` 分别是纸面 K6-3、K6-4。

## 验证范围

固定 Lean 4.24.0 和项目已有 mathlib v4.24.0。`lake build Aris4Math.K6Traces` 成功，包含两个前置分类模块。三个文件合计 908 行；18 条关键 `#print axioms` 报告均只有 `propext`、`Classical.choice`、`Quot.sound`。没有 `sorry`、`admit`、新 `axiom` 或 `native_decide`。

`decide` 只检查显示的固定参考配置的块大小、交数、每点次数及固定索引算术；任意输入块族的九型完备性依靠上述解析论证，不枚举所有块族、超图、染色或排列。

最终构建与公理原始输出见 `.aris/traces/proof-checker/2026-10-06_run07/lean-block-classification-build.log`，结构化验证记录见同目录 `lean-block-classification-verification.json`。

## 尚待连接的原证明义务

本轮已闭合纸面六点分类及实际超图的标签桥，未证明原命题 `Target`。

需要继续将已标号的完整真实迹块族和度数，代入 `Traces` 已证明的单点、空集及大块精确计数恒等式，得到与 `Numeric` 表逐项相同的类型向量；再与真实锁定排列上的概率事件上界、删除修正和严格数值界衔接。19–24 点分支及最终顶层装配由相应模块继续推进。本文件不把已编译分类或外部审阅意见替代这些剩余证明。
