# 下界比较表：原文定点核查

日期：2026-10-21。只读核查四篇本地原PDF的主结论；未修改生成器、Lean、wiki，未运行作者程序或发起模型审阅。

统一记号：$m(k)$ 为有限简单 $k$ 元非二染色超图的最少边数，$\log=\ln$。文献中的均匀度 $n$ 在表中改记 $k$，其别的参数不能随之混用。下表直接列 **$m(k)$ 的下界**，避免将可染边数预算与下界混写。

## 可直接用于正文的四列表

| 结果／方法 | $m(k)$ 的下界 | 参数范围 | 精确来源 |
|---|---|---|---|
| Radhakrishnan–Srinivasan（2000） | $m(k)>0.1\,2^k\sqrt{k/\log k}$；另有 $m(k)>0.7\,2^k\sqrt{k/\log k}$ 对充分大 $k$ 成立。其证明实际允许每个固定 $0<c<1/\sqrt2$ 取 $m(k)>c\,2^k\sqrt{k/\log k}$。 | 第一式全部整数 $k\ge2$；第二、三式各有相应的充分大起点。 | 作者稿 §2.1，Theorem 2.1及其前一段，p.7，[原PDF](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf#page=7)。 |
| Pluhár（2009） | $m(k)>2^{-1/2}\pi^{-1/4}e^{-1/(12k)}k^{1/4}2^k$。保留准确排列概率可定义 $B_{\rm pair}=\max\{M\ge1:M(M-1)\beta_k<1\}$，得 $m(k)\ge B_{\rm pair}+1$，其中 $\beta_k=((k-1)!)^2/(2k-1)!$。 | 符号Corollary由Claim证明适用于 $k\ge2$；如正文仅选共同一般范围 $k\ge17$ 也正确。 | 6页作者稿 §2.1，Claim 1及其证明，pp.2–3；Corollary 1，p.3。[正式书目／DOI](https://doi.org/10.1002/rsa.20267)。 |
| Cherkashin–Kozik（2015） | 对每个固定 $0<c<\sqrt2$，$m(k)>c\,2^{k-1}\sqrt{k/\log k}$。即在 $2^k$ 归一化下，每个固定常数 $c'<1/\sqrt2$ 都可取。有限充分判据为 $\kappa(1-p)^k+\kappa^2p<1$，$\kappa=M/2^{k-1}$。 | 各固定常数对应充分大 $k$；有限判据按其实际 $k,M,p$ 使用。 | **刊版** Theorem 1及其后常数说明，p.408；§2 proof，Eqs.(2.1)–(2.3)，pp.409–410。[刊版副本](https://mathsoc.spb.ru/prize/2022/1.pdf#page=2)。 |
| Grill–Linzmayer（2024） | $m(5)\ge32,\ m(6)\ge64,\ m(7)\ge128,\ m(8)\ge263,\ m(9)\ge538$。一般连续／离散贪心判据另见Eqs.(6)–(8)。 | Theorem 1的五项数值分别仅对应 $k=5,\ldots,9$。 | arXiv:2403.05674 **v3**，§3结尾，Theorem 1，p.7；§2，Eqs.(6)–(8)，pp.3–4。[原PDF](https://arxiv.org/pdf/2403.05674v3#page=7)。 |
| 本研究：增长主定理C | $m(k)\ge B_{\rm RS}(k)+1+\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor$。其中增量至少1。 | 全部整数 $k\ge17$；任意有限简单 $k$ 元超图。 | 本文定理C；完整Lean入口 `formal/Aris4Math/General/Growth/Main.lean`，验收见 `context/propertyb-general-lean-growth/REPORT.md`。 |
| 本研究：明确参考包络比较D | 令 $L_{\rm ref}=\max\{B_{\rm RS}+1,B_{\rm lin}+1,B_{\rm cont}+1,B_{\rm pair}+1,L_{\rm GR}\}$，则 $L_{\rm ref}=B_{\rm RS}+1$，故C相对此包络增加上述增长整数项。 | 全部整数 $k\ge32$。 | 本文 `proofs/propertyb-general/BASELINE_COMPARISON.md`，定义D.1、定理D。D为已审阅纸面结论；本次没有扩大Lean形式化范围。 |

若表格过长，保留前五行，并把D改为紧随表后的一段说明；无需把D当另一篇文献行。

## 原PDF实读与关键准确性

### RS2000：全域常数、渐近常数与严格取整

实际命令读取本地 `ref/radhakrishnan_srinivasan_2000_two_coloring.pdf` PDF pp.7–8。p.7 Theorem 2.1的第一部分给0.1，前段明确任意 $n\ge2$；同定理括号给充分大 $n$ 的0.7。紧前推导取参数 $\lambda=(1/\sqrt2)(1-\epsilon)\sqrt{n/\ln n}$，$p=(\ln n)/(2n)$，给每个固定正 $\epsilon$ 的充分大结论。因此“任意固定 $c<1/\sqrt2$”已经来自RS证明，不是CK2015首次改善常数。

若有实阈值 $X$，原文“至多 $X$ 边均可染”等价于所有整数边数 $M\le\lfloor X\rfloor$ 可染，故 **$m(k)\ge\lfloor X\rfloor+1$**，也可写 **$m(k)>X$**。不要在 $X$ 恰为整数时只写 $m(k)\ge\lceil X\rceil$ 并误当相同强度。

本文的 $B_{\rm RS}$ **由本文定义**：取RS §2.1 Claim 2.4 proof（作者稿p.7的未编号准确积分）与 Appendix A Claim A.1（pp.26–27）的FKG/Jensen端项用于同一过程，再以实际有向单交对数 $\gamma\le M(M-1)$ 组合。RS原文没有同名最大整数预算。表前应给：

\[
d=2^{k-1},\quad a_k(p)=1-(1-p)^k,\quad J_k(p)=\int_0^p(1-y^2)^{k-1}\,dy,
\]
\[
B_{\rm RS}(k)=\max\left\{M\in\mathbb Z_{\ge1}:\exists p\in[0,1],\quad
\frac{M(M-1)}{d^2}J_k(p)<a_k(p)^{M/d}\right\}.
\]

表注来源应准确指向“RS给出的两项估计＋本文组合及最大化”，而不是称“RS原定理 $B_{\rm RS}$”。

### Pluhár2009：原式和准确概率

实际读取本地 `ref/pluhar_2009_greedy_colorings.pdf` pp.2–3；另将p.3渲染为图片目读指数和系数，确认 Corollary 1 的 $2^{-1/2}\pi^{-1/4}e^{-1/(12k)}$，不是正的二分之一次幂。Claim 1 proof 对恰交一点的**指定有向边对**给准确排列概率 $\beta_k=((k-1)!)^2/(2k-1)!$，随后才使用Stirling放宽。

严格准确概率预算还可机械写为

\[
B_{\rm pair}(k)+1=
\left\lceil\frac{1+\sqrt{1+4/\beta_k}}2\right\rceil.
\]

该式保留 $M(M-1)\beta_k<1$ 的严格性；阈值恰为整数时仍按上述ceil处理。此最大化记号与闭式转换是本文定义/代数后果，不能称原文编号公式。

原文Corollary后另给“0.5268、$k\ge3$”简化句。显示的保守符号系数在 $k=3$ 约0.516575、$k=10$ 约0.526718，$k=11$ 约0.527117，因此该简化句不能仅由符号系数逐点比较推出；这里不判其数值命题为假。正文采用准确符号式即可，不必额外处理该简化句。

### CK2015：归一化与出处边界

实际读取刊版 `ref/general-propertyb/cherkashin_kozik_2015_published.pdf` PDF pp.2–4，即刊pp.408–410。p.408 Theorem 1明确归于RS参考文献[7]，随后给 $c<\sqrt2$；p.410 proof再次明确 $c\sqrt{n/\ln n}\,2^{n-1}$ 且充分大 $n$。因此表格可说“随机贪心的简短证明／有限线性判据”，不要说“将RS的0.7提升至 $\sqrt2$”——分母2不同，且RS已有极限常数。

原文 $\kappa$ 记号实际是 $k$，为避免与本文均匀度撞名才改为 $\kappa$。有限判据到 $m(k)$ 的下界，仍需按接受的**整数边数预算加1**。

### GL2024：五项小k数值与一般判据

实际读取本地 `ref/grill_linzmayer_2024_improved_lower_bounds_property_b.pdf` p.7，Theorem 1明确依次为32、64、128、263、538。不要把本页前面的中途数31、63、127、261、537或两锁中途数128、262混作最终定理。v3 §4的Theorem 2量化固定顶点数 $v=2k+1$，因此不将它直接当作全部有限顶点超图的同值下界。

五项数值对应可染边数预算31、63、127、262、537。它们与本文C的 $k\ge17$ 范围不重叠；正文应让读者看清适用范围，而不制造逐项大于关系。D比较的对象是五项明确定义的函数包络，不是“所有GL锁点方法／所有已知下界”。

## 书目信息与引用版本

* RS：Jaikumar Radhakrishnan and Aravind Srinivasan, *Improved bounds and algorithms for hypergraph 2-coloring*, RSA16(1), 4–32 $2000$。本次数学页码指27页作者稿的p.7，不是刊页7。
* P：András Pluhár, *Greedy colorings of uniform hypergraphs*, RSA35(2), 216–221 $2009$，[DOI](https://doi.org/10.1002/rsa.20267)。本次数学页码指6页作者稿pp.2–3，未假定与刊版逐页对应。
* CK：Danila D. Cherkashin and Jakub Kozik, *A note on random greedy coloring of uniform hypergraphs*, RSA47(3), 407–413 $2015$，[DOI](https://doi.org/10.1002/rsa.20556)。本次实际读取刊页408–410；不混用2013年arXiv稿编号。
* GL：Karl Grill and Daniel Linzmayer, *Improved Lower Bounds for Property B*, arXiv:2403.05674v3 $2024-06-20$，[v3](https://arxiv.org/abs/2403.05674v3)。本次数学页码p.7，与PDF页序相同。

原规范来源地图：`context/propertyb-general/formal-exposition-20261021/SOURCE_MAP.md`。本文C/D的已存在状态按项目最新正式报告引用；本次只核对文献下界及表格表达，没有重新执行Lean或审阅证明。
