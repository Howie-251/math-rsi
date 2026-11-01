# 一般 k-uniform Property B 的锁点证书定理：k=10,11 的严格整数验证

**状态**：数学引理与参数分支的纸面证明，加上完全可复算的精确整数计算证书；尚未进行独立形式化（例如 Lean）或同行评审。此前 `PROOF_PACKAGE_FULL.md` 的 k=5 证明提供随机贪心和 critical-pair 思路，`propertyB_k8_k9_proof.md` 是本次所用一至三锁版本的前身。本文件使一般定理与新计算实例自足。

## 定理 A（统一有限证书准则，任意 k≥3）

设 k≥3，M≥1 为整数。定义顶点区间的条件

\[
 d_0(v)=\left\lceil\frac{v-1}{k-1}\right\rceil,
 \quad v d_0(v)\le kM,
 \quad M\frac{\binom{\lfloor v/2\rfloor}{k}+\binom{\lceil v/2\rceil}{k}}{\binom vk}\ge1.
\]

对所有满足这些条件的 v（并且 v≥2k−1），如下任一证书充分：

1. **0 锁证书**：利用全局多交边对下界得到的失败概率上界 \(U_0(k,M,v)<1\)。
2. **1 锁证书**：对每个整数 \(d_0(v)\le d\le\lfloor kM/v\rfloor\)，锁定一个度数为 d 的顶点在中心位置，所得概率上界 \(U_1(k,M,v,d)<1\)。
3. **2 锁证书**：对上述每个 d，\(s_d=2(v-1)-(k-1)d>0\)。令 \(B_d\ge d\) 为满足 \(vd+s_d(B_d+1-d)>kM\) 的最小整数。对每个 \(d\le e\le B_d\)，两锁点、共度1、度数 (d,e) 的概率界 \(U_2(k,M,v,d,e)<1\)。
4. **3 锁证书**：存在整数 \(D\ge d_0(v)\)，满足 \(Z=(D+1)v-kM>0\) 及 \(2(k-1)Z>[(k-1)(D+1)-v+2]^2\)。对全部 \(d_0(v)\le d_1\le d_2\le d_3\le D\) 及下述两类三锁截面，概率界 \(U_3<1\)。

如果每个候选 v 至少拥有一个此类证书，则每个至多有 M 条边的简单 k-uniform 超图都具有 Property B，因而 \(m(k)\ge M+1\)。

### 定理 A 的数学基础

**最小顶点反例约化**。取顶点数最少的非 Property B 反例。若有不共边两点，将它们合并会保持 k-uniform 和非可染性，并减少顶点数，矛盾。因此所有顶点对共边。
\((k-1)d(x)=\sum_{y\ne x}\lambda_{xy}\ge v-1\)，\(\sum_xd(x)\le kM\)，得 \(vd_0(v)\le kM\)。均衡随机染色在 \(Mp_{v,k}<1\) 时排除这个 v。允许在固定顶点集添加新 k-边至 M 条（当 \(\binom vk\ge M\)）；也可以直接把证书按实际 m≤M 遍历。本文的 k=10/11 候选区间满足 \(\binom vk\ge M\)。

**随机排列贪心**。初始全红；依次处理随机排列中各点，如果当前点是某条仍全红边的最后点就改蓝。最后不可能有全红边。若有全蓝边 B，取其排列中第一点 x；处理 x 时存在全红见证边 A，以 x 为最后点。所以 \(A\cap B=\{x\}\)，\(\max_\sigma A=\min_\sigma B=x\)。因而失败事件被有序单交 critical pair 覆盖。

**条件边类型与权重**。锁定点集 \(S=\{x_1,\dots,x_s\}\) 在位置 \(t=(t_1,\dots,t_s)\)，其余 \(N=v-s\) 点均匀随机排列。\(T(e)\subseteq[s]\) 为边和锁点的精确交集，\(\ell_T\) 为此类型边数，\(r_T=k-|T|\)。位置 h 前后自由位置数为 \(a_h,b_h\)；锁定点位置左右的类型掩码为 \(I_h^-, I_h^+\)。对真实单交有序边对的权重：

- h 自由，\(T\subseteq I_h^-\), \(U\subseteq I_h^+\), \(r_T,r_U\ge1\), \(r_T+r_U-1\le N\)：
\[
w_h(T,U)=\frac{\binom{a_h}{r_T-1}\binom{b_h}{r_U-1}}{N\binom{N-1}{r_T-1}\binom{N-r_T}{r_U-1}}.
\]
- h 是第 j 个锁点位置，\(T\cap U=\{j\}\), \(T\setminus\{j\}\subseteq I_h^-\), \(U\setminus\{j\}\subseteq I_h^+\), \(r_T+r_U\le N\)：
\[
w_h(T,U)=\frac{\binom{a_h}{r_T}\binom{b_h}{r_U}}{\binom N{r_T}\binom{N-r_T}{r_U}}.
\]
- 否则权重为零。

单边终点概率 \(\mathrm{last}_h(T)\)：若 h 自由且 \(T\subseteq I_h^-\)，为 \(\frac{r_T}{N}\frac{\binom{a_h}{r_T-1}}{\binom{N-1}{r_T-1}}\)；若 h 是锁点 j 且 \(j\in T\), \(T\setminus\{j\}\subseteq I_h^-\)，为 \(\binom{a_h}{r_T}/\binom N{r_T}\)；否则零。首点概率 \(\mathrm{first}_h(T)\) 左右对调。

置
\[
A_h=\sum_T\ell_T\mathrm{last}_h(T),\quad B_h=\sum_T\ell_T\mathrm{first}_h(T),\quad C_h=\sum_{T,U}\ell_T(\ell_U-\mathbf 1_{T=U})w_h(T,U).
\]
真实 critical pair 只能是单交边对，所以其出现概率分别至多为 \(A_h,B_h,C_h\)。

**加权 link 扣除**。在任一锁点 j 处，令 \(q_j=\left\lceil\frac{(k-1)d(x_j)-(v-1)}{k-2}\right\rceil\)。该点有至少 \(q_j\) 个无序 incident-edge 对，除中心外还共享其他点，因而不可能 critical。类型对 \(\{T,U\}\) 的容量：T=U 时 \(\binom{\ell_T}{2}\)，否则 \(\ell_T\ell_U\)；单个无序对可删双向权重为 \(\delta_h(T,U)=w_h(T,U)+w_h(U,T)\)。将类型槽位按权重从小到大排列，取其中最轻的 \(q_j\) 个（含容量重复）之和 \(D_h\)。任何真实坏对分布至少有 \(q_j\) 对，故可扣的实际权重和至少为 \(D_h\)。自由位置设 \(D_h=0\)。于是
\[
\Pr(\mathrm{Fail})\le U=\sum_{h=1}^v\min\{A_h,B_h,C_h-D_h\}.
\]

**0 锁全局修正**。任意点对共边，\(\sum_{\{A,B\}}\binom{|A\cap B|}{2}=\sum_{\{x,y\}}\binom{\lambda_{xy}}{2}\ge M\binom k2-\binom v2\)。因为两条不同边交集至多 k−1，至少有 \(Q_v=\max\{0,\lceil[M\binom k2-\binom v2]/\binom{k-1}2\rceil\}\) 个无序多交边对。因此有序单交边对数至多 \(M(M-1)-2Q_v\)，用此数代入无锁 C_h。

**锁点选择**。1 锁取最小度点，度数 d 位于上述区间。2 锁：对最小度点 x，\(s_d=2(v-1)-(k-1)d\) 个以上顶点与 x 的共度恰为1。如果这些顶点度数都 ≥\(B_d+1\)，总度数就至少为 \(vd+s_d(B_d+1-d)>kM\)，矛盾。因而存在共度为1、度数 e∈[d,B_d] 的第二顶点。

3 锁：下面的更通用 s 锁定理在 s=3 时给出。两两共度1的三个点的多点截面只有：单个三元块（triple），或三个二元块（separate）。若三点度数分别为 \(d_1,d_2,d_3\)，则
\[
\begin{array}{ll}
\text{triple:}&\ell_{xyz}=1,\ \ell_i=d_i-1,\ \ell_\varnothing=M-\sum_i d_i+2;\\
\text{separate:}&\ell_{xy}=\ell_{xz}=\ell_{yz}=1,\ \ell_i=d_i-2,\ \ell_\varnothing=M-\sum_i d_i+3.
\end{array}
\]

锁点位置取：一个点 \(\lfloor v/2\rfloor\)，两个点 \((\lfloor v/2\rfloor,\lfloor v/2\rfloor+1)\)，三个点 \((\lfloor v/2\rfloor-1,\lfloor v/2\rfloor,\lfloor v/2\rfloor+1)\)。这完成各个证书的全部数学约化。

## 定理 B（任意 s≥2 的锁点存在性）

对于任何点对覆盖的简单 k-uniform H，设 \(|V|=v\)，\(|E|=M\)。取 \(D\ge d_0(v)\)，记 \(Z=(D+1)v-kM\)，\(T=(k-1)(D+1)-v+2\)。若
\[
Z>0,\qquad 4(k-1)Z>(s-1)T^2,
\]
则存在 s 个度数至多 D、两两共度恰为1的顶点。

证明：令 \(L=\{x:d(x)\le D\}\)，\(r=|L|>0\)。在 L 上连辅助图边 xy 当且仅当 \(\lambda_{xy}\ge2\)。总度数预算给出
\[
2e(G)\le((k-1)(D+1)-(v-1))r-(k-1)Z=(T-1)r-(k-1)Z.
\]
Caro–Wei 及 Cauchy–Schwarz 给出
\[
\alpha(G)\ge\frac{r^2}{r+2e(G)}\ge\frac{r^2}{Tr-(k-1)Z}.
\]
由于
\[
r^2-(s-1)(Tr-(k-1)Z)=\left(r-\frac{(s-1)T}{2}\right)^2+(s-1)(k-1)Z-\frac{(s-1)^2 T^2}{4}>0,
\]
故 \(\alpha(G)>s-1\)，即存在大小至少 s 的独立集。\(\square\)

**更一般的结构输入（s≥4）**：若选出 s 个两两共度1的点，则原 k-边与锁点集的大小至少2的截面恰形成 \(K_s\) 的团分解，块大小在2与 \(\min\{k,s\}\) 之间。对任意块 B，\(\ell_B=1\)；单点类型 \(\ell_i=d(x_i)-\#\{B:i\in B\}\)；空类型 \(\ell_\varnothing=M-|\mathcal D|-\sum_i\ell_i\)。因此定理 B 与条件排列概率公式构成一个对任意 k,s 的有限计算准则（一般 s 需枚举这些团分解，非三锁的两型简化）。

## 定理 C（本次的实例）：m(10)≥1112，m(11)≥2275

选取 \((k,M)=(10,1111)\) 与 \((11,2274)\)。极小反例约化给出候选区间：

| k | M | 候选顶点数 | 0锁 | 1锁 | 2锁 | 3锁 |
|---|---:|---|---|---|---|---|
| 10 | 1111 | 67–316 | 67–207 | 208–229 | 230–266 | 267–316 |
| 11 | 2274 | 79–500 | 79–332 | 333–368 | 369–429 | 430–500 |

三锁分支的 D(v) 取满足定理 B(s=3) 严格判据的**最小**整数。示例：k=10,M=1111,v=267,D=46 时 Z=1439,T=158，\(2\cdot9Z-T^2=938>0\)；k=11,M=2274,v=430,D=62 时 Z=2076,T=202，\(20Z-T^2=716>0\)。其余位置亦在证书中逐项验证。所需 D(v) 在整个三锁区间分别从46降低到35、从62降低到50。

### 严格整数验证结果

取统一分母 \(S=2^{52}=4503599627370496\)。对于精确概率 p，在其**作为上界**的所有出现处使用 \(\lceil Sp\rceil\)；对于可删坏对权重的**下界**，使用 \(\lfloor Sp\rfloor\)。因此所有程序输出的 \(U_{\rm cert}/S\) 都是原真实失败概率的严格数学上界，不依赖于机器浮点舍入误差。

| k | 锁数 | 候选 v | 枚举参数数 | 最大整数上界分子 / S | 最大值出现处 |
|---|---:|---|---:|---|---|
| 10 | 0 | 67–207 | 141 | 4501312395478588 / S | v=207 |
| 10 | 1 | 208–229 | 588 | 4502044576409510 / S | v=229, d=26 |
| 10 | 2 | 230–266 | 8516 | 4503357407813370 / S | v=266, (30,30) |
| 10 | 3 | 267–316 | 19300 | 4493247203031996 / S | v=316, (35,35,35), separate |
| 11 | 0 | 79–332 | 254 | 4502853105575820 / S | v=332 |
| 11 | 1 | 333–368 | 1315 | 4502832786566168 / S | v=368, d=37 |
| 11 | 2 | 369–429 | 23409 | 4503118681525936 / S | v=429, (43,43) |
| 11 | 3 | 430–500 | 45494 | 4490963595772447 / S | v=500, (50,50,50), separate |

全部分子均严格小于 S。共检查 k=10 的 28545 个参数、k=11 的 70472 个参数；每个分支的锁点存在性由上面的普适组合引理保证，不是任意采样完整超图。由定理 A，得到
\[
\boxed{m(10)\ge1112,\qquad m(11)\ge2275.}
\]

### 可复现性与程序正确性接口

运行：
```bash
python3 propertyB_k10_k11_verified.py 10
python3 propertyB_k10_k11_verified.py 11
```

程序需要 Python 3.10+、NumPy。NumPy **仅用于加速 signed int64 的确切整数乘加**，不用浮点数。程序在每个 (v,s) 检查：

- 每个单项上界计数的乘加中，总的非负整数和不超过 \(M^2\max_{h,T,U}\lceil Sw_h(T,U)\rceil\)，严格小于 \(2^{63}-1\)，所以无 int64 溢出。
- 单边端点总量不超过 \(M\max_{h,T}\lceil S\Pr(\text{endpoint})\rceil\)，也严格小于 \(2^{63}-1\)。
- 被扣减的无序坏对项采用权重向下舍入且数量不超过 \(\binom M2\)，其总量也低于上述乘加安全阈值。
- 最终逐位置最小值之和由 Python 无界整数 `sum` 计算。

`propertyB_k10_k11_certified.py` 提供未使用 NumPy 的纯 Python 大整数版本，完成了 k=10 全部及 k=11 的0–2锁分支交叉复核；`propertyB_fast_exact_triple.py` 另以不同的 \(2^{40}\) 尺度复核三锁分支。它们对分界配置的比较方向一致。日志分别见 `propertyB_k10_verification.log` 与 `propertyB_k11_verification.log`。

**文献对比的边界**：Grill–Linzmayer 2024 年论文的表格只列出 k=5..9，此处不能据此声称 k=10、11 的数值已经打破截至 2026 年的最佳发表纪录。当前成果应称为「独立可复算的计算机辅助证明候选」，尚待第三方核验、公开的代码审查及可能的 Lean 形式化。

参考：[Grill–Linzmayer, Improved Lower Bounds for Property B (arXiv:2403.05674v3)](https://arxiv.org/html/2403.05674v3).
