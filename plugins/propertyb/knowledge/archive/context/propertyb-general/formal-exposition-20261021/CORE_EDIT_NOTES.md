# CORE 正式数学表述编辑说明

本次仅编辑 `proofs/propertyb-general/CORE_THEOREM.md`，并在此记录差异。原命题、解析充分判据与结构上界未改变；规范规格和 Lean 源码未改。

## 排版与论证结构

1. 新增定义1–3，显式给出有限简单 $k$ 元超图、Property B、$m(k)$、有向单交对（含 $f\ne g$）、$d_k,a_k,J_k,v_k,g_k$ 以及实际 RS 随机过程。
2. 保留稳定主编号定理A、引理1／2／3及公式(A)、(1)–(4)。每条先陈述完整假设和结论，紧接“证明”与结束符 $\square$；定理A放在已证引理之后，证明直接调用引理1／2／3。
3. 原引理1的实质证明拆为引理1.1（正关联）、1.2（残留概率）、1.3（新单色边必要事件），再组装为完整RS上界。图论随机排列计数独立为引理3.1。原有归纳、Jensen、必要条件、精确积分、Gram正定性、Cauchy–Schwarz及最小顶点商论证均保留。
4. 主定理单列空边集情形；引理1显式要求整数 $k\ge2$、$0<p\le1$、实际边数 $m\ge1$。没有增加结构性假设。
5. 新增 `core-theorem-a`、`core-lemma-1`、`core-lemma-2`、`core-lemma-3` 及各子引理HTML锚点。

## 事件与 Lean 对齐

已逐项核对 `formal/Aris4Math/General/RS/Algorithm.lean` 与 `ProbabilityBound.lean`：

- 定义3的残留事件对应 `ResidualEvent`。
- 必要事件 $\mathcal N_{f,g}^{q}$ 对应 `PairEvent`，目标颜色 $q$ 的对色写作 $1-q$；原来的“$f$ 经 $g$ 最后变蓝”不再作为未定义概率事件。
- 引理1.3的覆盖对齐 `failure_covered`／`new_mono_pair_event`；$k\ge2$ 确保交点单例蕴含 $f\ne g$。
- 新文对必要事件给出精确概率等式，并据覆盖关系给实际失败概率上界；这与 `pair_probability_sum` 以及 `rs_recoloring_failure_le` 的角色区分一致。

这是表述核对，不是新增 Lean 验收；本次没有运行 Lean 或新增数学结论。

## 原始来源

文献代理核对作者稿后统一使用 [RS2000]：

- §2 “Slow recoloring”，第4页“The Algorithm”：实际算法。
- §2.1，Lemma 2.1（第5页）与 Claims 2.1–2.3（第6页）：失败覆盖及单交必要事件。
- Claim 2.4证明（第7页）：未编号精确积分；原文随后作进一步放宽。正文没有将精确积分误标成原文编号公式。
- Appendix A “Exploiting positive correlation”，Claim A.1（第26–27页）：正关联／Jensen残留界。式(31)只作为条件平均等式说明，没有冒称它本身就是最终概率上界。
- 引理1明确说明本文把上述估计用于同一实际算法并保留有向单交对，并非原文某一命题的逐字转述。

## 自检

已核主判据和(1)–(4)的系数、量词及不等号方向；原有实质论证均保留为显式引理或证明步骤。当前共八个定理／引理陈述，八个紧接证明与结束符；没有遗留工作流状态节、风险节、未定义概率事件或未决引用编号。
