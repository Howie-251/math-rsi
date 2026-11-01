## 文献下界与本文结果对照

以下统一使用 $m(k)$ 表示不可二染的有限简单 $k$ 元超图的最少边数。为便于比较，记

$$F(k)=2^k\sqrt{\frac{k}{\log k}},\qquad c_P(k)=\frac{e^{-1/(12k)}}{\sqrt2\,\pi^{1/4}}.$$

### 论文原文给出的下界

|论文／结果|下界|适用范围|与本文的关系|
|---|---|---|---|
|Radhakrishnan–Srinivasan（2000）|$m(k)>0.1F(k)$；对每个固定 $0<c<1/\sqrt2$，有 $m(k)>cF(k)$|第一式对所有 $k\ge2$；第二式对充分大 $k\ge k_0(c)$|建立 $2^k\sqrt{k/\log k}$ 量级。原文 Theorem 2.1 用常数0.7表述充分大范围，其前段给出任意 $c<1/\sqrt2$。[作者稿p.7，Theorem 2.1及其前段](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=7)|
|Cherkashin–Kozik（2015）|对每个固定 $0<c<1/\sqrt2$，有 $m(k)>cF(k)$|充分大 $k\ge k_0(c)$|用随机贪心染色简化同一渐近下界的证明。原文使用 $2^{k-1}$ 归一化，常数写为 $c'<\sqrt2$；此处 $c=c'/2$。[刊版p.408，Theorem 1及其后段](../../ref/general-propertyb/cherkashin_kozik_2015_published.pdf#page=2)，[DOI](https://doi.org/10.1002/rsa.20556)|
|Pluhár（2009）|$m(k)>c_P(k)\,k^{1/4}2^k$|所有 $k\ge2$|随机贪心法的四次根下界；准确单交对概率还给出下表的阶乘判据。[作者稿p.3，Corollary 1](../../ref/pluhar_2009_greedy_colorings.pdf#page=3)，[DOI](https://doi.org/10.1002/rsa.20267)|
|Grill–Linzmayer（2024）|$(m(5),m(6),m(7),m(8),m(9))\ge(32,64,128,263,538)$，逐分量比较|$k=5,6,7,8,9$|这是该文锁点分析给出的具体小参数结果；一般 $k$ 的连续式和覆盖式另外列于下表。[v3 p.7，Theorem 1](https://arxiv.org/pdf/2403.05674v3#page=7)|
|本文：增长主定理C|$m(k)\ge B_{\rm RS}(k)+1+\Delta(k)$|所有 $k\ge17$|在明确的RS组合整数基线上统一增加 $\Delta(k)\ge1$；主定理已完成端到端Lean。[定理C](#clique-theorem-c) · [完整形式证明](../../PROPERTY_B_GENERAL_LEAN.html)|

表中严格实数界 $m(k)>X$ 对应整数界 $m(k)\ge\lfloor X\rfloor+1$。RS与CK的渐近结论没有在这里指定统一的有限起点；本文的改进是精确有限预算之上的加性整数增益；该加性项不改变 $B_{\rm RS}$ 基线的领先渐近项。

### 同一有限参数下的精确比较

下面各 $B$ 都是**本文从所引分析定义的最大整数可染预算**，对应 $m(k)$ 的下界为 $B+1$；这些记号及最大化约定不冒充原论文的定义。令 $d=2^{k-1}$、$\kappa=M/d$，$a=a_k(p)$、$J=J_k(p)$，并令

$$\beta_k=\frac{((k-1)!)^2}{(2k-1)!}.$$

|文献来源|本文比较的有限判据／下界|已证明的关系|
|---|---|---|
|RS的正关联端项＋精确积分|$B_{\rm RS}$：存在 $p\in[0,1]$ 使 $M(M-1)J/d^2<a^\kappa$|作为统一比较基线；组合的原始来源为 [Claim A.1](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=26) 与 [Claim 2.4证明中的积分](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=7)|
|CK刊版式(2.3)，亦为RS优化的线性式|$B_{\rm lin}$：存在 $p\in[0,1]$ 使 $\kappa(1-p)^k+\kappa^2p<1$|$B_{\rm lin}\le B_{\rm RS}$，$k\ge17$。[CK刊页410](../../ref/general-propertyb/cherkashin_kozik_2015_published.pdf#page=4)|
|Pluhár Claim 1证明的准确排列概率|$B_{\rm pair}$：$M(M-1)\beta_k<1$|$B_{\rm pair}\le B_{\rm cont}\le B_{\rm RS}$，$k\ge17$。[作者稿pp.2–3](../../ref/pluhar_2009_greedy_colorings.pdf#page=2)|
|GL式(6)–(7)，取平凡有向边对上界|$B_{\rm cont}$：存在 $p\in[0,1]$ 使 $\kappa(1-p)^k+M(M-1)J/d^2<1$|$B_{\rm cont}\le B_{\rm RS}$，$k\ge17$。[GL §2](https://arxiv.org/html/2403.05674v3#S2)|
|GL式(3)–(5)重述的Goldberg–Russell型界|$L_{\rm GR}=\min_{v\ge2k-1}\max\{S_k(v),\lceil R_k(v)\rceil\}$；$S_k,R_k$定义见[引理D.1](#comparison-lemma-d1)|$L_{\rm GR}\le2^k<B_{\rm RS}+1$，$k\ge17$。[GL §1](https://arxiv.org/html/2403.05674v3#S1)|

这些支配关系的证明见[引理D.2](#comparison-lemma-d2)、[引理D.3](#comparison-lemma-d3)。因此对所有 $k\ge17$，上述五项明确下界的最大值恰为

$$L_{\rm ref}(k)=B_{\rm RS}(k)+1,$$

而本文得到

$$\boxed{m(k)\ge L_{\rm ref}(k)+\Delta(k),\qquad \Delta(k)=\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor\ge1.}$$

这是[定理D](#comparison-theorem-d)中已证明的逐参数比较。GL的小参数多锁定理保留其原范围；对 $k\ge256$ 的指定零锁必要数据方案，另有[定理E](#comparison-theorem-e)的比较。主定理C已形式化，比较D、E仍由正文的完整纸面证明支撑。
