# 一般增长定理与五项参考包络的起点可统一降至 $k=12$

**阶段衔接（2026-10-21）：** 下文保留本次推导／计算形成时的状态。后续已完成全部 $k\ge12$ 的统一解析证明、端到端Lean与Grok最终审阅；当前验收见 [REPORT.md](REPORT.md) 和 [审阅处置](REVIEW_DISPOSITION.md)。下文“尚未形式化／审阅”等是先前阶段描述，原证据未改。

## 命题、状态与范围

**状态：PROVABLE AS STATED。** 以下给出完整纸面推导，沿用既有实际超图与重染判据。本文是独立推导稿；尚未经过本轮指定跨模型审阅，也未新增或扩大 Lean 导出定理。

对每个整数 $k\ge12$，以原定义B.1的同一公式定义接受集合 $\mathcal A_k$ 及其最大元 $B_{\rm RS}(k)$。则最大元存在，且

$$
2^k\le B_{\rm RS}(k)<k2^k.
$$

置

$$
\Delta(k)=\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor.
$$

则 $\Delta(k)\ge2$，任意有限简单 $k$ 元超图，只要边数至多 $B_{\rm RS}(k)+\Delta(k)$，均有 Property B。因此

$$
\boxed{m(k)\ge B_{\rm RS}(k)+1+\Delta(k)\qquad(k\ge12).}
\tag{T12}
$$

若五项参考包络 $L_{\rm ref}$ 也按原定义D.1的同一公式延至 $k\ge12$，则

$$
\boxed{L_{\rm ref}(k)=B_{\rm RS}(k)+1,\qquad
m(k)\ge L_{\rm ref}(k)+\Delta(k)\qquad(k\ge12).}
\tag{D12}
$$

这里所有超图结论量化任意有限顶点集上的简单 $k$ 元超图；没有额外的点数、点对覆盖、度数、共度、正则性或线性假设。本稿未涉及比较定理E的起点或结论。

## 记号、策略与依赖

沿用规范源中的记号

$$
d=2^{k-1},\quad a_k(p)=1-(1-p)^k,\quad
J_k(p)=\int_0^p(1-y^2)^{k-1}\,dy,
$$

以及

$$
\mathcal A_k=\left\{M\in\mathbb Z_{\ge1}:\exists p\in[0,1],\quad
\frac{M(M-1)}{d^2}J_k(p)<a_k(p)^{M/d}\right\}.
$$

证明仍保留同一个接受见证 $p$，用实际单交图的团数削减吸收新增边。依赖如下：

1. [CORE_THEOREM.md](../../../proofs/propertyb-general/CORE_THEOREM.md) 的引理1、2、3.1，均已对 $k\ge2$ 证明：实际失败上界、最小顶点反例的点对覆盖约化、由团数控制实际有向单交对数。
2. [CLIQUE_REFINEMENT.md](../../../proofs/propertyb-general/CLIQUE_REFINEMENT.md) 的引理C.1与推论C.2，均已对 $k\ge2$ 证明：实际单交团的公共点二分，以及其无附加结构充分判据。
3. 原引理B.1的证明实际上只需 $k\ge2$、$M\ge2^k$；下文重述并核明。
4. 原引理B.4的可接受起点改用 $a_k(1/k)>3/5$。
5. 原定理C中不再要求 $\sqrt M\ge k^2$ 或 $r_k(M+s)\le2\sqrt M$，改证足够的 $r_k(M+s)\le3\sqrt M$。
6. 比较D只将所选 $v$ 的估计直接收紧到 $v>4k^2$；引理D.3的同参数支配论证不变。

## 引理1：接受见证的控制不需要 $k\ge17$

设整数 $k\ge2$、$M\in\mathcal A_k$、$M\ge2^k$，且 $p$ 是接受见证。记 $a=a_k(p)$、$J=J_k(p)$、$\kappa=M/d$。则

$$
p>\frac1{k^2},\qquad J\ge\frac1{2k^2},\qquad
\kappa<2k,\qquad\kappa\log a>-2\log k.
\tag{1}
$$

**证明。** 有 $\kappa\ge2$、$M\ge2$，故

$$
\frac{\kappa^2}{2}J
\le\frac{M(M-1)}{d^2}J<a^\kappa.
\tag{2}
$$

若 $p=0$，接受不等式两边均为零，所以 $p>0$。若 $p\le1/k^2$，则在 $0\le y\le p$ 上，由 Bernoulli 不等式

$$
(1-y^2)^{k-1}\ge1-(k-1)y^2\ge1-\frac{k-1}{k^4}\ge\frac12.
$$

因而 $J\ge p/2$，且 $a\le kp$。由(2)除以正数 $kp$ 得

$$
\frac{\kappa^2}{4k}<(kp)^{\kappa-1}\le kp\le\frac1k
\le\frac{\kappa^2}{4k},
$$

矛盾；其中中间一步使用 $0<kp\le1/k\le1$ 及 $\kappa\ge2$。故 $p>1/k^2$。在 $[0,1/k^2]$ 上积分同一被积函数下界，得 $J\ge1/(2k^2)$。再由(2)，

$$
1\ge a^\kappa>\frac{\kappa^2}{4k^2}\ge\frac1{k^2}.
$$

于是 $\kappa<2k$；又 $a>0$，对最后一个严格不等式取自然对数，即得 $\kappa\log a>-2\log k$。∎

## 引理2：$k\ge12$ 时接受预算最大元存在

对整数 $k\ge12$，集合 $\mathcal A_k$ 含有 $2^k$，其全部元素均小于 $k2^k$。因此 $B_{\rm RS}(k)=\max\mathcal A_k$ 良定，最大元本身有 $p\in(0,1]$ 的严格接受见证。

**证明。** 取 $M_0=2^k$、$p=1/k$。由二项式展开的前三项，

$$
\left(1+\frac1{k-1}\right)^k
\ge1+\frac{k}{k-1}+\frac{k}{2(k-1)}
>\frac52.
$$

所以 $(1-1/k)^k<2/5$，从而 $a_k(1/k)>3/5$。又 $J_k(1/k)\le1/k$，故

$$
\frac{M_0(M_0-1)}{d^2}J_k(1/k)
<\frac4k\le\frac13<\frac9{25}<a_k(1/k)^2.
$$

这证明 $M_0\in\mathcal A_k$。若 $M\in\mathcal A_k$ 且 $M\ge2^k$，引理1给出 $M/d<2k$，即 $M<k2^k$；其余元素满足 $M<2^k<k2^k$。故该非空正整数集合有限，有最大元。最大元属于接受集合，因而有见证；引理1保证该见证非零。这里未假定接受集合下闭，也未假定连续优化的最优值可达。∎

## 引理3：足够的团数界与整数余量

设整数 $k\ge12$、$M\ge2^k$，并令

$$
t=\sqrt M,\qquad s=\left\lfloor\frac{t}{8(1+\log k)}\right\rfloor,
\qquad N=M+s.
$$

则 $2\le s\le t\le M$，并且推论C.2中的 $r=r_k(N)$ 满足

$$
k\le r\le3t,\qquad
(2+2\log k)s+2<\frac{M}{r}.
\tag{3}
$$

**证明。** 先用 $\log2=\int_1^2dt/t>1/2$。对 $x\ge12$，

$$
\frac{d}{dx}\log\frac{2^{x/2}}{x^2}
=\frac{\log2}{2}-\frac2x
>\frac14-\frac2{12}>0.
$$

起点 $12^2=144<3\cdot2^6=192$，故

$$
k^2-k+1\le k^2<3\cdot2^{k/2}\le3t.
\tag{4}
$$

另有 $\log12<3$，例如 $e^3>1+3+9/2+27/6=13>12$。对 $x\ge12$，

$$
\frac{d}{dx}\log\frac{2^{x/2}}{8(1+\log x)}
=\frac{\log2}{2}-\frac1{x(1+\log x)}
>\frac14-\frac1{12}>0.
$$

起点 $2^{12/2}/[8(1+\log12)]>64/32=2$，从而定义 $s$ 的实数商大于2，故 $s\ge2$。分母大于1，故 $s\le t\le M$，于是 $N\le2M$。

记 $v=v_k(N)$。根据该整数的定义，$v\ge k$ 且 $v(v-1)\le k(k-1)N$，故

$$
\frac{v-1}{k-1}\le\sqrt{\frac{kN}{k-1}}\le2t.
\tag{5}
$$

最后一步用 $N\le2M$ 及 $k/(k-1)\le2$。由 $r_k$ 的定义、(4)、(5)，得到 $k\le r\le3t$。最后

$$
(2+2\log k)s+2\le\frac t4+2
<\frac t3\le\frac{M}{r},
$$

其中严格不等式等价于 $t>24$，而 $t\ge2^{k/2}\ge64$。∎

## 定理1：相同增长增益公式对全部 $k\ge12$ 成立

命题(T12)成立。

**证明。** 先取任意 $M\in\mathcal A_k$、$M\ge2^k$，取其接受见证 $p$，并用引理1、3的记号。因为 $M\ge2$、$r\ge k\ge12$、$a>0$，以下对数均有定义。初等不等式 $\log(1+u)\le u$、$\log(1-u)\le-u$ 给出

$$
\begin{aligned}
\log\frac{N^2(1-1/r)}{M(M-1)}
&=2\log\left(1+\frac sM\right)+\log\left(1-\frac1r\right)
+\log\left(1+\frac1{M-1}\right)\\
&\le\frac{2s+2}{M}-\frac1r\\
&<-\frac{2s\log k}{M}\\
&<\frac{s\kappa\log a}{M}=\frac{s\log a}{d}.
\end{aligned}
\tag{6}
$$

第二行使用 $1/(M-1)\le2/M$；第三行是引理3的(3)除以 $M$ 后重排；第四行用引理1和 $s>0$。由于 $g_k^*(N)\le N^2(1-1/r)$，由(6)及指数函数单调性，

$$
\frac{g_k^*(N)}{M(M-1)}<a^{s/d}.
$$

与同一个 $p$ 的严格接受不等式相乘，得到

$$
\frac{g_k^*(N)}{d^2}J_k(p)<a_k(p)^{N/d}.
\tag{7}
$$

引理1保证 $p>0$，所以(7)满足推论C.2的全部假设。该推论把(7)作用于任意假定的原始非B超图：内部选择边数不增加的最小顶点反例，内部证明点对覆盖及实际单交图的团界，再以实际重染失败概率小于1得到矛盾。故任意至多 $N$ 边的原始有限简单 $k$ 元超图均可二染。

由引理2取 $M=B_{\rm RS}(k)$。此时 $s=\Delta(k)\ge2$，即得(T12)。∎

## 引理4：五项参考包络比较也可降至 $k=12$

对整数 $k\ge12$，原定义D.1中的 $L_{\rm GR}$ 满足 $L_{\rm GR}(k)\le2^k$。

**证明。** 仍取

$$q=2^{\lfloor k/2\rfloor},\qquad v=(k-1)q.$$

首先证明 $v>4k^2$。两个奇偶起点分别是

$$
(12-1)2^6=704>576=4\cdot12^2,
\qquad
(13-1)2^6=768>676=4\cdot13^2.
$$

令 $F(k)=(k-1)2^{\lfloor k/2\rfloor}/k^2$。对于整数 $k\ge12$，

$$
\frac{F(k+2)}{F(k)}
=\frac{2(k+1)k^2}{(k-1)(k+2)^2}>1,
$$

因为分子减分母为 $k^3-k^2+4>0$。以两个起点分别按步长2归纳，即对全部 $k\ge12$ 得到 $v>4k^2$，也保证 $v\ge2k-1$ 是原式(B5)的合法输入。这里仅核两个解析归纳起点，没有逐 $k$ 枚举。

又 $\lceil(v-1)/(k-1)\rceil=q$，所以原覆盖项满足

$$
S_k(v)=\left\lceil\frac{(k-1)q^2}{k}\right\rceil\le q^2\le2^k.
\tag{8}
$$

记 $a=\lfloor v/2\rfloor$、$b=\lceil v/2\rceil$。对 $t\in\{a,b\}$ 及 $0\le j\le k-1$，

$$
\frac{t-j}{v-j}\ge\frac12\left(1-\frac{2k}{v}\right).
$$

因此均匀平衡染色中一条指定边的单色概率满足

$$
P=\frac{\binom ak+\binom bk}{\binom vk}
\ge2^{1-k}\left(1-\frac{2k}{v}\right)^k
\ge2^{1-k}\left(1-\frac{2k^2}{v}\right)>2^{-k}.
\tag{9}
$$

其中 Bernoulli 不等式适用，因为 $0<2k/v<1$；最后使用 $v>4k^2$。于是 $R_k(v)=1/P<2^k$，故 $\lceil R_k(v)\rceil\le2^k$。将该具体合法 $v$ 的(8)、(9)代入外层最小值，即得 $L_{\rm GR}(k)\le2^k$。∎

## 定理2：相对五项明确参考界的严格增益

命题(D12)成立。

**证明。** 引理4和引理2给出 $L_{\rm GR}(k)\le2^k\le B_{\rm RS}(k)$。原引理D.3的论证只需 $k\ge2$ 和已有 $B_{\rm RS}(k)\ge2^k$，故在当前范围仍给出

$$
B_{\rm pair}(k)\le B_{\rm cont}(k)\le B_{\rm RS}(k),
\qquad B_{\rm lin}(k)\le B_{\rm RS}(k).
$$

具体说，连续判据的同参数恒等式(B8)仍成立；当 $M\ge d$ 时，用 $1-(1-z)^{M/d}\le(M/d)z$ 比较其端点项，用 $J_k(p)\le p$ 比较线性判据，即把每个接受见证传给RS判据；当 $M<d$ 时直接由 $M<B_{\rm RS}(k)$ 控制。坏对Beta积分判据的连续支配逐点成立。这三个集合都非空，并受有限的 $B_{\rm RS}$ 约束，因而最大值存在。将这些支配关系代入原五项包络的最大值定义，便得到 $L_{\rm ref}(k)=B_{\rm RS}(k)+1$。与定理1合用得到(D12)，其增益至少2，因而严格为正。∎

## 改动规模与待完成范围

1. 数学上只需放宽引理B.1的参数说明、改写B.4的起点估计、以本稿引理3替换定理C的团数与余量估计，并以引理4替换D.2的强中间估计。原B.2与B.3的旧弱团界加一转换无需延伸；新的定理1已直接蕴含当前范围的加一结论。
2. 本稿完整覆盖 $k=12,13,14,15,16$，并与既有 $k\ge17$ 定理合为 $k\ge12$。未依赖这些五个参数的额外结构证书或新的大规模搜索。
3. 现有 Lean 实际导出仍为 $k\ge17$；本稿没有更改规范源、Lean、旧35/36 Goal或编码理论项目。若将该延伸写入最终成果，应按本轮用户范围决定是否追加Lean实现与指定审阅，不能把当前纸面推导表述成已完成的新Lean范围。
4. 数值图若要直接展示严格包络增益，可对 $k=12..16$ 复用同一精确RS见证数值流程。该计算用于给显式样点，不是(T12)/(D12)的证明前提。

## 复核记录与未决项

本稿逐项检查了接受集合最大元、非零参数、正分母、整数增益、实际超图调用和五项包络量词。全部新解析估计均在文内给出；(T12)/(D12)无未闭合数学义务。剩余为主代理验收、按实际要求的跨模型审阅与可能的形式化扩展，不能以本稿作者自核代替这些项目级验收。
