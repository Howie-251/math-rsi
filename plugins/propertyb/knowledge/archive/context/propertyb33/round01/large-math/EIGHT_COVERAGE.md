# 八点14型的覆盖：解析归一化与255叶证书

日期：2026-10-08。继V25_EIGHT_LOCK_ROUTE.md；本文件说明怎样从任意真实局部三元族走到有限证书，而不是仅复查14个代表。

## 原始局部命题

设X有8点，T⊆binom(X,3)，不同三元块交集至多1，|T|≥5，且每个x∈X至少属于一块。则存在双射X≃Fin8，把T映为14个代表之一。代表为EIGHT_LOCKS.json中全部大块是三元块、数量≥5的14组，与实际概率表一一对应。

线性自动推出每点的三元块度≤3：经过x的每块在X\{x}留下两个互不相交点，故2d_T(x)≤7。再数总关联得3|T|≤24，因此5≤|T|≤8。真实六度超图的八点截面满足覆盖：若某点没有三元块，7个其他点必须通过7条二元块覆盖，超过其6度。

## 解析步骤A：必有两个不交三元块

反设T内任意两块都相交。取A∈T。至少4个其他块，各恰与A交1点。由于A只有3点，抽屉原理给出不同的B,C∈T\{A}，且A∩B=A∩C={x}。由线性，B∩C={x}。

x已经属于A,B,C三块，由每点度≤3，不属于其他块。集合U=A∪B∪C大小恰为3+2+2=7。

任意其他D∈T，同时与A、B、C相交。三个交点必须互异：若其中两个相同，该点位于两者的交集{x}，但x∉D。D恰有3点，因此它的全部点就是这三个交点，都属于U。

所以所有T块均包含于7点集合U，与T覆盖X的8点矛盾。故存在不交A,B。

这个论证只用真实集合、线性、覆盖和块数，不依赖Python表。

## 解析步骤B：存在连接两块的第三块

固定不交A,B∈T，令Z=X\(A∪B)，|Z|=2。其他块D与A、B分别交至多1点。

若D没有同时与A、B相交，则D必须包含Z的全部两点：它在A∪B中至多有1点，而总大小为3。两个这样的不同D会共享Z，违反线性。所以至多一个其他块不是连接块。

T\{A,B}至少3块，因此存在C，满足|C∩A|=|C∩B|=1，其第三点在Z中。可选择标签使

\[
A=123,\qquad B=456,\qquad C=147.
\]

重标号是实际双射。可以直接分别标记交点、A剩余两点、B剩余两点、C的外点和最后一个点；也可以复用BlockClassification.exists_equiv_map_blocks：三个块的每点incidence≤2、块大小3、交集矩阵(AB=0,AC=1,BC=1)与标准seed相同，地集基数都是8，因此存在保留全部块的顶点双射。

## 归一化后的完整候选集

另一个三元块D必须与seed每块交至多1点。全部允许候选恰为：

```
158 168 248 257 258 267 268 278
348 357 358 367 368 378 578 678
```

来源可按是否包含7、8拆分，也可由一个仅遍历Fin8子集的内核有限引理证明。Lean中的`compatible_triple_is_candidate`针对任意Fin8子集、card=3以及与seed的真实线性条件，推出其属于seed或16候选之一。因此用户/下游不需要额外假设“类型在表中”。

## 完备递归而非代表自检

函数`extensions candidates chosen`对下一个候选B保留两条分支：

1. 不加入B，递归余下候选；
2. 若B与chosen中每个不同块交至多1点，则加入B，递归余下候选。

候选列表长度每步减少，终止时返回chosen。首轮chosen为实际三块seed。

已证明的通用Lean定理`extensions_complete`：对于任意线性target，若chosen⊆target⊆chosen∪candidates.toFinset，则target必属于递归输出。归纳每一步根据**B是否属于target**选正确分支。加入分支的兼容性由target真实线性保证；排除分支保持剩余覆盖。不以运行日志或生成器正确性作为公理。

这个16候选递归恰有255个叶子，按加入块数分布为：0→1、1→16、2→72、3→108、4→54、5→4。其中满足总块数≥5且覆盖8点的叶子为236个。其余19个因真实目标前提不满足而无需分类。

Python仅为每个有效叶子寻找一个映到14型的明确8点置换，并生成255项见证列表；不承担最终正确性。Lean从自己的递归输出逐项检查：

- 若见证为none，实际该叶子不满足覆盖/块数条件；
- 若见证为(k,f)，f确实双射，并且**完整叶子**经f的像恰为第k个代表；
- 递归输出与见证列表同时耗尽，不能静默截断或遗漏末尾。

`checkWitnesses_sound`将这一布尔检查的真值变成对任意递归成员的分类结论。`classify_seed_eight`再连接实际三元族、seed包含、线性、覆盖及数量条件。

因此内核中的有限计算仅是255个明确小对象和置换的局部证书，不涉及整图超图或全部染色枚举。

## 当前实现边界

文件`formal/Aris4Math/ThirtyThree/EightClassification.lean`现已包含完整解析归一化与分类。`exists_disjoint_triples`落实步骤A；`exists_seed_blocks`落实步骤B；`label_seed_blocks`复用原incidence双射引理，构造实际标签。最终`classify_eight`只接受三元性、线性、覆盖和至少5块四项数学前提，输出14型及真实`Fin8≃Fin8`，没有seed或候选表假设。

实际执行`lake build Aris4Math.ThirtyThree.EightClassification`，退出码0，输出`Build completed successfully (909 jobs)`。最终`classify_eight`及全部依赖打印的传递公理均仅为`propext`、`Classical.choice`、`Quot.sound`。完整最新日志是`eight-normalization-build.log`；早先仅seed阶段的日志`eight-classification-lean.log`保留。没有使用sorry或native_decide，编译后的模块已可供25点装配导入。

因此**八点局部14型的完整Lean覆盖已经完成**。尚未由本模块承担的是超图实际多点截面到该输入的绑定、33边类型重数、概率计数及最后25点PropertyB结论；这些由25点结构/装配模块继续连接。本模块不重定义超图、unit-codegrees或trace。

生成器：`computations/propertyb33/round01/normalized_eight_certificate.py`。其输出计数为`NORMALIZED_EIGHT_CERTIFICATE.json`；生成的置换数据副本保存在`EIGHT_CERTIFICATE_DATA.lean.txt`，编译源中的同一数据由Lean检查。

## 实际超图输入连接（2026-10-08）

`formal/Aris4Math/ThirtyThree/EightTraceClassification.lean` 已构建通过。
其 `exists_full_labeled_eight H S eight unit small many covers` 将
`TwentyFiveStructure` 第二分支给出的真实八点集合 S 转换为：

```lean
∃ k : Fin 14, ∃ label : ↥S ≃ Fin 8,
  (H.multiTraces S).image (TraceRecovery.labelBlock S label) =
    K6Classification.pairCompletion (EightClassification.representative8 k)
```

具体连接为：把真实三元迹族经任意 S≃Fin8 标签映射；证明其基数、线性与覆盖保持；调用完整 `classify_eight`；将返回双射与原标签复合；调用旧 `labeled_traces_recovered`，得到全部二元/三元块。最终前提就是八点、单位共度、每块至多三点、至少五个三元块且覆盖 S，不含剖面证书或类型表归属前提。

核验：`lake build Aris4Math.ThirtyThree.EightTraceClassification` exit 0，日志 `eight-trace-build.log`；传递公理只有 `propext`、`Classical.choice`、`Quot.sound`。本模块输出可直接接 `TraceProfileBridge.realizes_of_recovered_counts`。33边具体数值剖面及最终概率装配由另一代理实现。

## 下游装配状态（2026-10-08）

`formal/Aris4Math/ThirtyThree/TwentyFive.lean` 的实际25点分支已由reduction代理连接并构建通过；项目AGENTS当前记录19、20、21、25点已完整Lean闭合，随后22点也已完成。八点分类与本文件的真实迹族接口已经成为该已完成25点证明的一部分。核验入口见 `context/propertyb33/round01/twentyfive-complete/build.log`；本文件上文的“概率装配待接”仅是此前分工阶段。
