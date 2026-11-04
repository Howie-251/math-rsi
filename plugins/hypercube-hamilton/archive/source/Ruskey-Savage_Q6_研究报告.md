# 超立方体匹配的 Hamilton 延拓

## 1. Ruskey–Savage 猜想

设 $Q_n$ 为 $n$ 维超立方体图，即

$$
V(Q_n)=\{0,1\}^n,\qquad
E(Q_n)=\{xy:d_H(x,y)=1\},
$$

其中 $d_H$ 是 Hamming 距离。记 $p(x)=\sum_i x_i\pmod 2$，并记 $E_n,O_n$ 为偶、奇顶点集。匹配是两两不共端点的边集；对匹配 $M$，记

$$
H(M)=V(Q_n)\setminus V(M).
$$

$H(M)$ 中的顶点称为自由顶点，亦称孔。Hamilton 圈是恰好经过全部顶点一次的圈。

**猜想 1（Ruskey–Savage，1993）.** 对任意 $n\ge2$，$Q_n$ 的每个匹配都包含在某个 Hamilton 圈中。换言之，

$$
\boxed{\quad
\forall n\ge2\ \ \forall M\subseteq E(Q_n)\text{ 为匹配},\quad
\exists C\subseteq Q_n\text{ 为 Hamilton 圈},\quad M\subseteq E(C).
\quad}
$$

超立方体的 Hamilton 圈对应循环二进制 Gray 码。因此，猜想要求在保留任意一组互不冲突的指定相邻关系的同时，排列全部 $2^n$ 个二进制串，使相邻串只改变一位。困难在于把局部边约束与全局连通性同时满足：包含匹配的生成 2-正则子图可能有多个圈，而一般匹配也未必能在超立方体内补成完美匹配。

以下将一条边的唯一变化坐标称为它的**方向**，并以 $\operatorname{dir}(M)$ 表示匹配使用的方向集。

## 2. 文献进展

表中“延拓”均要求保留原匹配的全部边；2-factor 指覆盖全部顶点的若干个顶点不交圈。

| 年份 | 作者 | 已证明的结果 | 限制及在 $Q_6$ 中的含义 | 文献 |
|---|---|---|---|---|
| 1993 | Ruskey–Savage | 提出任意匹配的 Hamilton 圈延拓猜想 | 对全部 $n\ge2$ 的任意匹配作出断言 | [原论文](https://doi.org/10.1137/0406012) |
| 2007 | Fink | 每个完美匹配可延拓为 Hamilton 圈，解决 Kreweras 猜想 | 在 $Q_6$ 中覆盖含 32 条边的完美匹配 | [作者 PDF](https://kam.mff.cuni.cz/~fink/publications/kreweras1.pdf) |
| 2014 | Wang–Zhang | $n\ge2$、$\lvert M\rvert\le2n-1$ 时，可延拓为 Hamilton 圈 | 代入 $n=6$，覆盖至多 11 条边的匹配 | [论文](https://arxiv.org/pdf/1301.2931) · [DOI](https://doi.org/10.1016/j.disc.2013.12.014) |
| 2019 | Fink | 任意匹配可延拓为 2-factor | 覆盖全部顶点，但可能由多个圈组成 | [作者 PDF](https://ktiml.mff.cuni.cz/~fink/publication/west.pdf) · [DOI](https://doi.org/10.1007/s00493-017-3731-8) |
| 2025（预印本 2024） | Fink–Mütze | 任意匹配可延拓为至少经过 $\frac23\,2^n$ 个顶点的圈 | 不保证遍历全部顶点 | [论文](https://arxiv.org/abs/2401.01769) · [DOI](https://doi.org/10.1137/24M1670093) |
| 2025 预印本；2026 正式章 | Fink–Hotmar | 至多五方向的匹配可延拓为 Hamilton 圈；建立有限维到方向数的提升框架 | 在 $Q_6$ 中要求 $\lvert\operatorname{dir}(M)\rvert\le5$，不限制匹配大小 | [本文采用的 v1](https://arxiv.org/pdf/2501.19029v1) · [正式章 DOI](https://doi.org/10.1007/978-3-032-11835-6_19) |
| 2025 | Ali–Yang–Ali–Popa–Mitu | 满足额外顶点覆盖条件的 $Q_6$ 匹配可延拓为 Hamilton 圈，并推广至六方向 | 定理 12–13 带有涉及距离为 3 的顶点对的覆盖条件；不是任意匹配结论 | [原文，定理 12–13](https://doi.org/10.3390/sym17070995) |
| 2025 在线 | Ali–Ali–Yang | $Q_6$ 中每个至多含 **20 条边**的匹配，都可延拓为 Hamilton 圈¹ | 要求 $\lvert M\rvert\le20$；公开摘要未声称覆盖全部匹配，全文尚未取得 | [公开摘要](https://www.researchgate.net/publication/396201366_On_Extension_of_Matchings_to_Hamiltonian_Cycles_in_6-Cubes) · [DOI](https://doi.org/10.1142/S0219265925500227) |
| 2026（预印本 2025） | Ali–Ba–Yang | 在 $Q_6$ 中，给定异奇偶端点 $x,y$，若匹配至多含 **5 条边**且 $xy\notin M$，则存在包含匹配的 Hamilton $x$–$y$ 路 | 一般结论为 $n\ge5$、$\lvert M\rvert\le3n-13$；代入 $n=6$ 得 5。允许两个指定端点都已覆盖 | [预印本，定理 1.3](https://arxiv.org/pdf/2506.21432) · [DOI](https://doi.org/10.1007/s10878-026-01418-3) |

¹ 此项依据公开摘要，未取得全文核查证明。

## 3. 我们的成果

**本文通过计算辅助证明解决了 Ruskey–Savage 猜想的六维情形，并进一步得到任意维数中的六方向 Hamilton 圈延拓。** 三项成果及其逻辑关系如下；证明稿的审计状态见文末。

### 3.1 主定理：六维自由端点路径延拓

**定理 2（六维自由端点延拓，$P_6$）.** 设 $M\subseteq E(Q_6)$ 为匹配，$u\in H(M)$，且 $p(u)\ne p(v)$。则 $Q_6$ 存在 Hamilton $u$–$v$ 路 $P$，满足

$$
\begin{array}{c}
M\subseteq E(Q_6)\text{ 为匹配},\quad u\notin V(M),\quad p(u)\ne p(v)\\
\Longrightarrow\quad
\exists\text{ Hamilton }u\text{–}v\text{ 路 }P\subseteq Q_6,\quad M\subseteq E(P).
\end{array}
$$

端点 $u$ 必须自由，$v$ 可以已覆盖。除这些端点条件外，不限制匹配的大小、方向数或覆盖形状；由于存在自由点，自然有 $\lvert M\rvert\le31$。原匹配始终由超立方体边构成。

### 3.2 六维圈结论：解决 Ruskey–Savage 猜想的六维情形

**推论 3(a)（完整六维圈延拓）.** $Q_6$ 的每个匹配都包含在某个 Hamilton 圈中，即

$$
\begin{array}{c}
\forall\,M\subseteq E(Q_6)\text{ 为匹配},\\
\exists\text{ Hamilton 圈 }C\subseteq Q_6,\quad M\subseteq E(C).
\end{array}
$$

非完美匹配取自由点 $u$ 及其短邻点 $v$，由 $P_6$ 得到 Hamilton $u$–$v$ 路，再加 $uv$ 闭圈；完美匹配使用 Fink 的已有定理。因此，圈结论覆盖全部 $0\le\lvert M\rvert\le32$，这正是 Ruskey–Savage 猜想在 $n=6$ 时的完整断言。

相对于 Ali–Ali–Yang 的至多 20 条边结论，本文还覆盖其范围之外的 21 至 31 条边匹配；32 条边的完美匹配情形已有 Fink 的定理，不计为本文新增贡献。21 至 31 条边中的部分子类此前也已有结果，因此这里的加强是得到**不附加大小或覆盖条件的完整六维结论**。

### 3.3 任意维数的六方向圈延拓

**推论 3(b)（六方向延拓）.** 对任意 $n\ge2$ 及匹配 $M\subseteq E(Q_n)$，有

$$
\begin{array}{c}
\lvert\operatorname{dir}(M)\rvert\le6\\
\Longrightarrow\quad
\exists\text{ Hamilton 圈 }C\subseteq Q_n,\quad M\subseteq E(C).
\end{array}
$$

这一提升使用 Fink–Hotmar 的定理 5：本文补上六维自由端点命题，将无额外覆盖限制的方向数从五推进到六。相对于 Ali–Yang–Ali–Popa–Mitu 的六方向结果，本文去掉其额外顶点覆盖条件。结合已有低维结果，Ruskey–Savage 猜想在 $2\le n\le6$ 时成立。

与 Ali–Ba–Yang 的路径定理相比，在 $Q_6$ 且至少一个指定端点自由的共同范围内，本文去掉了其五条边的限制；但其定理允许任意 $n\ge5$ 和两个已覆盖端点，故本文不包含其完整适用范围。

本文采用计算辅助证明：解析归约将定理 2 化为九个完整孔层，局部构造由有限森林及矩阵秩证书保证。新增证明的核心是五维辅助命题、十四孔的极大匹配还原与十六孔的双源转移。本文不涉及七个及以上方向的任意匹配，也不主张六方向任意两个已覆盖端点的完整路径分类。所有有限证据的原件见文末补充资料。

### 3.4 从自由端点路径到圈延拓的逻辑

**（1）六维猜想的目标：对任意匹配找到一个圈。** 六维 Ruskey–Savage 猜想要求

$$
\begin{array}{c}
\forall\,M\subseteq E(Q_6)\text{ 为匹配},\\
\exists\text{ Hamilton 圈 }C\subseteq Q_6,\quad M\subseteq E(C).
\end{array}
$$

这个圈必须经过全部 64 个顶点，并保留匹配的全部边。圈没有指定端点，因此证明时可以自行选择辅助端点。

**（2）我们建立的是一个带指定端点的路径命题。**

$P_6$ 说：

$$
\boxed{
\begin{array}{c}
M\subseteq E(Q_6)\text{ 为任意匹配},\\
u\notin V(M),\qquad p(u)\ne p(v)\\
\Longrightarrow\quad
\exists\text{ Hamilton }u\text{–}v\text{ 路 }P\subseteq Q_6,
\quad M\subseteq E(P).
\end{array}
}
$$

量词很重要：

- 对**每个**匹配 $M$；
- 对**每个**自由顶点 $u$；
- 对**每个**与 $u$ 异奇偶的顶点 $v$，即使 $v$ 已被匹配覆盖；
- 都能找到满足要求的路径。

这比“存在某条包含匹配的 Hamilton 路”强，因为我们可以事先指定符合条件的端点。

**（3）非完美匹配：选择相邻端点，先得路再闭圈。** 任取非完美匹配 $M$，可选自由顶点 $u\notin V(M)$，再取 $u$ 的任意邻点 $v$。相邻保证 $p(u)\ne p(v)$，由 $P_6$ 得到包含 $M$ 的 Hamilton 路

$$
P:\quad u\longrightarrow\cdots\longrightarrow v.
$$

因 $uv\in E(Q_6)$，可以加上这条边，得到

$$
C=P+uv.
$$

该圈经过全部 64 个顶点并保留 $M$。由于 $u$ 自由，$uv\notin M$；由于 Hamilton $u$–$v$ 路还必须经过其余 62 个顶点，$uv$ 也不可能已是该路径的一条边。因此闭圈合法，得到

$$
P_6\ \Longrightarrow\ Q_6\text{ 的每个非完美匹配都可延拓为 Hamilton 圈}.
$$

**（4）完美匹配：使用已有定理，补齐全部匹配。** $Q_6$ 的完美匹配有 32 条边，没有自由点，使用 [Fink 的完美匹配定理](https://kam.mff.cuni.cz/~fink/publications/kreweras1.pdf) 得到 Hamilton 圈。所有匹配恰好分为非完美匹配与完美匹配，两类均已处理，故

$$
\begin{array}{c}
P_6+\text{Fink 完美匹配定理}\\
\Longrightarrow\ \text{完整的六维 Ruskey–Savage 猜想}.
\end{array}
$$

因此，“至少一个指定端点自由”是构造路径时的条件，最终的六维圈结论覆盖任意匹配，不附加自由顶点要求。

**（5）任意维数的六方向结论：再应用提升框架。** [Fink–Hotmar 定理 5](https://arxiv.org/pdf/2501.19029v1) 给出：若自由端点路径命题在 $Q_d$ 中成立，则对所有 $n\ge d$，至多使用 $d$ 个方向的匹配都可延拓为 Hamilton 圈。取 $d=6$，得到

$$
\begin{array}{c}
P_6+\text{Fink–Hotmar 提升定理}\\
\Longrightarrow\ \forall n\ge6,\ \text{至多六方向的匹配可延拓为 Hamilton 圈}.
\end{array}
$$

其构造将 $Q_n$ 分成六维子立方体。因原匹配只使用六个方向，其每条边都位于某一块内部。在各块内安排路径，再沿其余坐标连接，得到一个大圈。对于非完美匹配，只需在含自由顶点的一块中用 $P_6$ 完成最后的指定端点连接，其余块可以从包含局部匹配的 Hamilton 圈中删去一条非匹配边而得到路径，因而不要求每块都有自由点；全局完美匹配仍使用 Fink 定理。具体拼接及奇偶性验证见第 7 节。

这两步推导各自有明确输入：完整六维圈结论由 $P_6$ 与完美匹配定理得到；任意维数的六方向圈结论进一步使用有限维路径命题的提升框架。

## 4. 五维局部引理

在局部论证中，允许规定匹配属于顶点集上的完全图，但新增边必须属于超立方体。后者称为短边。局部 Hamilton 路、圈在此约定下理解：其长边只能来自规定匹配。

**引理 4（森林秩判据）.** 设 $K$ 是 $N\ge4$ 个顶点的偶数阶集合。对 $K$ 上的完美匹配 $P,F$，定义

$$
\mathcal H_N(P,F)=
\begin{cases}
1,&P+F\text{ 为一个交替圈},\\
0,&\text{其他}.
\end{cases}
$$

这里 $+$ 表示保留边标号的并。设 $r=2^{N/2-1}$ 个合法短森林的端点配对为 $P_1,\ldots,P_r$。若存在 $r$ 个完美匹配 $F_1,\ldots,F_r$，使

$$
\operatorname{rank}_{\mathbb F_2}
\bigl(\mathcal H_N(P_i,F_j)\bigr)_{i,j=1}^{r}=r,
$$

则对任意 $K$ 上的完美匹配 $F$，至少一个所选森林与 $F$ 合成单圈。

**证明.** 完美匹配连通矩阵的秩定理给出
$\operatorname{rank}_{\mathbb F_2}\mathcal H_N=r$
（[Cygan–Kratsch–Nederlof](https://doi.org/10.1145/3148227)）。故所选完整行张成整个行空间。任取 $F=\{a_i b_i:1\le i\le N/2\}$，将 $b_i$ 与 $a_{i+1}$ 循环相配可得一个与 $F$ 合成单圈的匹配，因此 $F$ 对应的列非零。所选行在该列不可能全为零。展开相应森林路径即得结论。$\square$

这里的合法森林在规定匹配端点上度数为 1，在待补入的孔上度数为 2，在省略孔上度数为 0，且无圈。验证只需检查短边、度数、无环性、端点配对及有限矩阵的秩。若某个森林端点配对被强迫含边 $pq$，则先证明实际规定匹配 $F$ 不含 $pq$，再将 $F$ 在 $p,q$ 处的两条边收缩；引理应用于少两个端点的矩阵。

**有限引理 5（五维避孔圈）.** 对 $1\le t\le5$，设 $F$ 是 $K(V(Q_5))$ 中的匹配，两类孔数分别为 $t-1,t+1$。给定多数类中的任意孔 $z$，存在包含 $F$、恰好经过 $V(Q_5)\setminus\{z\}$ 的圈，且新增边均为短边。

此命题记为 $A_{2t}$。其有限证明使用四维路径与避孔圈分类，以及引理 4。$A_8$ 的非邻接孔几何有 2,700 个；$A_{10}$ 有 55 个，分成大小为 $30,20,5$ 的三轨道，最后一轨道使用 1,024 阶满秩证书。完整构造与有限输入见 [五维 $A_8$](research/six_directions/Q5_A8_FULL_CLOSURE.md)、[五维 $A_{10}$](research/six_directions/Q5_A10_FULL_CLOSURE.md) 及其所引基础引理。

**引理 6.** $A_{2t}$ 对所有可行的 $t$ 成立。

**证明.** $Q_5$ 任一奇偶类中任意五点至少有 11 个邻点；该有限邻域性质由全部 $\binom{16}{5}=4368$ 个五元组核验。若 $t\ge6$，少数类至少有五个孔，多数类除 $z$ 外至少有六个孔。由于 $11+6>16$，两者间存在短边。将其加入规定匹配，保持 $z$ 自由，并使两类孔数各减一。重复后应用引理 5 即可。$\square$

**引理 7（五维平衡孔路径）.** 设 $F\subseteq E(K(V(Q_5)))$ 为匹配，且两类孔数相等。给定自由顶点 $r$ 及异奇偶顶点 $y$，存在包含 $F$ 的 Hamilton $r$–$y$ 路，新增边均为短边。

**证明.** 令 $P_m,C_m$ 分别表示两类孔数均为 $m$ 时的上述路径命题与生成圈命题。Fink 的完美匹配定理给出 $C_0$，包括完全图规定匹配、仅添加短边的形式。设 $C_{m-1}$ 已知。

若 $y$ 自由，对 $F\cup\{ry\}$ 应用 $C_{m-1}$，再删去 $ry$。若 $yh\in F$，令

$$
F'=(F\setminus\{yh\})\cup\{hr\}.
$$

$F'$ 的孔数为 $(m-1,m+1)$，多数类包含 $y$。由引理 6 得到避开 $y$ 的圈；删去 $hr$ 并接回 $hy$，即得所需路径。因此 $P_m$ 成立。取自由根及其短邻点为端点，再将所得 Hamilton 路闭合，得 $C_m$。归纳完成。$m=16$ 时匹配为空，只需自由目标分支。$\square$

## 5. 六维归约与有限孔层

**引理 8（孔数上界）.** 对任意 $M\subseteq E(Q_6)$ 及 $u\in H(M)$，存在匹配 $L\supseteq M$，使

$$
u\in H(L),\qquad 23\le |L|\le31.
$$

**证明.** 在 $Q_6-\{u\}$ 内将 $M$ 补成包含极大的匹配 $L$。Havel–Křivánek 的定理断言，完整 $Q_6$ 中每个包含极大的匹配至少有 24 条边（[1982，定理 2](https://dml.cz/bitstream/handle/10338.dmlcz/106137/CommentatMathUnivCarol_023-1982-1_10.pdf)）。若 $u$ 的全部邻点均已覆盖，则 $L$ 在完整 $Q_6$ 中极大，故 $|L|\ge24$。否则，取自由邻点 $a$；$L\cup\{ua\}$ 在完整 $Q_6$ 中极大，故 $|L|+1\ge24$。又因 $u$ 自由，$|L|\le31$。$\square$

令 $\mathcal P_h$ 表示定理 2 对恰有 $h$ 个孔的匹配成立。引理 8 将问题归约为

$$
\mathcal P_2,\mathcal P_4,\ldots,\mathcal P_{18}.
$$

**引理 9（前层增广）.** 设 $k\ge2$ 且 $\mathcal P_{2k-2}$ 成立。平移后令 $u=0$，并写

$$
H(M)=\{0\}\cup Z\cup W,\qquad
Z\subset E_6\setminus\{0\},\quad W\subset O_6,\quad
|Z|=k-1,\quad |W|=k.
$$

证明 $\mathcal P_{2k}$ 时，若 $v$ 已覆盖，只需处理 $Z\cup W$ 独立的情形；若 $v$ 自由，只需处理 $H(M)$ 独立的情形。

**证明.** 若 $v$ 已覆盖且有短边连接 $Z,W$，加入该边后应用前层。若 $v$ 自由且存在孔间短边 $xy\ne uv$，加入后 $u,v$ 至少一个仍自由，以此点为根应用前层。若该边为 $uv$，令 $M'=M\cup\{uv\}$，取 $M'$ 的另一自由顶点 $r$ 及其短邻点 $s$。前层给出包含 $M'$ 的 Hamilton $r$–$s$ 路；加 $rs$ 成圈，再删 $uv$。$\square$

坐标置换进一步将 $v$ 规范为 $1,7,31$，分别代表距离 $1,3,5$。对剩余孔几何沿一坐标切为 $A,B\cong Q_5$，记 $\bar x$ 为 $x$ 在另一侧的短邻点。构造分为三步：

1. 在 $A$ 侧将原跨边端口与所选自由桥源补成辅助匹配 $D$，利用引理 7 得到规定端点路径。
2. 删去 $D$，接入原跨边及桥源短边 $s\bar s$，将产生的路径压成 $B$ 侧的完全图匹配 $F_B$。
3. 对 $F_B$ 应用五维平衡孔圈命题（引理 7 证明中的 $C_m$）、引理 6，或精确标记的森林秩证书，再展开路径并删去编码端点的辅助边。

各模板须保证辅助边最终删除、压缩无内部圈，且所有强迫配对的避障条件对实际 $F_B$ 成立。若所选方向没有原匹配跨边，直接使用五方向自由根路径定理。不可实现的孔几何则由 Hall 见证 $|N(S)|<|S|$ 排除。完整转移条件见 [近乎平衡切分引理](research/six_directions/HIGHER_Q5_FULL_NEARBALANCED.md) 与 [强迫配对转移](research/six_directions/HIGHER_FORCED_CHERRY_TRANSFER.md)。

**有限引理 10（完整孔层）.** 对每个 $h\in\{2,4,\ldots,18\}$，$\mathcal P_h$ 成立。

**证明（计算辅助）.** 双孔层由近完美匹配端点定理给出。其后按 $h$ 递增使用引理 9；对每一规范孔几何，证书给出上述切分构造、合法的局部森林证书，或不可实现的 Hall 见证。表中列出各层的完整证明入口及最终构造。

| 孔数 $h$ | 匹配边数 | 闭合该层的构造 | 完整证明 |
|---:|---:|---|---|
| 2 | 31 | 近完美匹配的自由根端点定理 | [双孔](research/six_directions/GENERAL_NEAR_PERFECT.md) |
| 4 | 30 | 两次坐标切分，排除唯一边界情形 | [四孔](research/six_directions/FOUR_HOLE_FULL.md) |
| 6 | 29 | $A_4$ 与自由、覆盖两类目标的转移 | [六孔](research/six_directions/SIX_HOLE_CLOSED.md) |
| 8 | 28 | $A_6$；最后 50 个几何的七轨道邻域构造 | [八孔](research/six_directions/EIGHT_HOLE_FULL_CLOSURE.md) |
| 10 | 27 | 最后 4,096 个几何分为 $2598+1036+462$ 个互斥构造域 | [十孔](research/six_directions/TEN_HOLE_FULL_CLOSURE.md) |
| 12 | 26 | 最后 235 个几何的六轨道极大匹配构造，完整局部域共 3,620,052 个输入 | [十二孔](research/six_directions/TWELVE_HOLE_FULL_CLOSURE.md) |
| 14 | 25 | 最后 25 个几何的两轨道构造，完整局部域共 805,006 个输入 | [十四孔](research/six_directions/FOURTEEN_HOLE_FULL_CLOSURE.md) |
| 16 | 24 | 最后 148 个几何分为 30 个根星形与 118 个双源切分 | [十六孔](research/six_directions/SIXTEEN_EIGHTEEN_FULL_CLOSURE.md) |
| 18 | 23 | 完整十六孔归约后，80,805 个几何由 $73605+7050+150$ 个构造或 Hall 见证覆盖 | [十八孔](research/six_directions/SIXTEEN_EIGHTEEN_FULL_CLOSURE.md) |

有限验证包含两项独立义务：几何域被精确穷尽；每个几何的构造适用于实现它的**任意**原匹配。前者由规范化、集合划分及完整枚举验证；后者由引理 4 的全称结论或极大匹配域的逐项正证书保证。极大域的完整性由输入合法性、互异性和独立计数相等确认。每层均包括自由目标与已覆盖目标，且只调用已建立的较小孔层。表中证明及所附证书给出了上述全部验证；两个末端构造的解析论证在下一节展开。$\square$

## 6. 两个末端构造

### 6.1 十四孔：从极大匹配还原到任意匹配

最后 25 个几何分为大小 20 与 5 的两轨道。以整数表示二进制顶点，其代表为 $u=0,v=31$ 及

$$
\begin{aligned}
Z&=\{39,43,45,51,53,57\},\\
J&=\{1,2,4,8,16\},\\
W_0&=J\cup\{14,32\},\qquad W_1=J\cup\{32,62\}.
\end{aligned}
$$

沿坐标 32 切分，令 $A=\{0,\ldots,31\}$、$B=A+32$，以及

$$T=\bar Z=\{7,11,13,19,21,25\}.$$

设 $L=M\cap E(A)$。由于 $\bar T=Z$ 为孔，$L$ 必须覆盖 $T$；第二轨道还必须覆盖 30。将 $L$ 在原覆盖顶点诱导图中补成包含极大的 $L^*$。两轨道的完整极大域分别有 291,743 和 513,263 个元素。

有限证书为每个 $L^*$ 给出自由偶点 $q$、$t\in T$、不同的 $w,b\in J$，以及 $A\setminus\{0,31\}$ 上的短森林 $S_A$：其在 $q,b$ 处度数为 2，其余顶点处为 1，并含边 $qt$。若 $31h^*\in L^*$，将其改为 $wh^*$，否则保持不变；记所得匹配为 $L^{*\prime}$。证书保证 $S_A+L^{*\prime}$ 无圈。

对实际匹配作相同的目标改接：原目标边为 $31h$ 时，将其换成 $wh$，内部部分记为 $L'$。若目标跨边，则 $h=63$，实际辅助跨边始终为 $w63$。于是

$$L'\subseteq L^{*\prime}.$$

确实，目标内部匹配时两次改接使用同一伙伴；目标跨边时 $L'=L$，而 $L^{*\prime}$ 至多删除一条不属于 $L$ 的补全边。

图 $S_A+L^{*\prime}$ 的路径端点在两奇偶类中各有 $14-|L^*|\ge3$ 个。偶偶端点路径与奇奇端点路径等数，将二者交替连接，再插入异奇偶端点路径；若全为异奇偶路径，则一致定向后循环连接。由此得到异奇偶辅助匹配 $D^*$，使 $S_A+L^{*\prime}+D^*$ 为单圈。令

$$
D=D^*\cup(L^{*\prime}\setminus L').
$$

两部分端点不交，故 $D$ 为匹配，且

$$
\boxed{\ S_A+L'+D=S_A+L^{*\prime}+D^*.\ }
$$

这将极大匹配的证书还原为实际 $L$ 的证书。由于 $t$ 已被实际 $L$ 覆盖、$q$ 不属于 $D$，可删去 $D$ 及 $qt$，接上全部实际或虚拟跨边，以及

$$
s\bar s\quad(s\in W_i\cap A\setminus\{w,b\}),\qquad t\bar t.
$$

得到端点位于 $B$ 的路径系统。与原 $M_B$ 合并时，度数为 2 的冲突点恰是桥源镜像；它们同奇偶，而其原匹配伙伴为异奇偶悬挂端点，故无内部圈。压缩后得到 22 个端点上的完美匹配 $F_B$。

局部森林强迫配对 $\bar w\bar b$。这两个顶点的原内部短匹配边在压缩中原样保留，而 $\bar w,\bar b$ 同奇偶，故 $\bar w\bar b\notin F_B$。五个精确标记输入各有 512 阶满秩证书，应用引理 4 的收缩形式即得 $B$ 侧单圈。展开后得到 $Q_6\setminus\{0,31\}$ 上的生成圈，含实际辅助边 $wh$。删去 $wh$，接上 $0w$ 与 $h31$，即得所需 Hamilton $0$–$31$ 路。

上述 805,006 个局部输入及两轨道覆盖的有限证据见 [十四孔末端构造](research/six_directions/FOURTEEN_FINAL25_PROOF.md)。其中极大域的独立计数按未匹配奇点集 $U$ 分类：其余奇点注入匹配到短邻偶点，所用偶点必须包含 $N(U)$；这恰好等价于包含极大性。

### 6.2 十六孔：双源切分的避障

最后 148 个几何中，30 个由根星形构造处理，另 118 个归约到如下五维输入：

$$
\begin{aligned}
H_E&=\{0,3,5\},\quad H_O=\{1,2,14,22,25,26,28\},\\
U&=\{1,2\},\quad e=\{30,31\},\quad R=\{13,21\}.
\end{aligned}
$$

**局部命题.** 令 $K=V(Q_5)\setminus(H_E\cup H_O)$。对每个 $K$ 上的完美匹配 $F$，若 $e\in F$ 且 $R\notin F$，则存在恰好经过 $V(Q_5)\setminus U$、包含 $F$ 且仅新增短边的圈。

**证明.** 有限证书给出 256 个合法短森林，其端点配对为 $P_i$。向 $P_i$ 加入 $e$ 并压缩 30、31，所得 20 端点配对 $Q_i$ 均包含 $R$。令 $Q_i^-=Q_i\setminus\{R\}$；这些行在其余 18 个端点上的连通矩阵秩为 $256=2^{18/2-1}$。

给定 $F$，令 $F_{20}=F\setminus\{e\}$。设 $a,b$ 分别是 13、21 的伙伴。由于 $R\notin F$，可用 $ab$ 代替 $13a,21b$，得到 18 端点匹配 $G$。逐次收缩给出

$$
P_i+F\text{ 连通}
\iff Q_i+F_{20}\text{ 连通}
\iff Q_i^-+G\text{ 连通}.
$$

由引理 4 选择相容行并展开森林即可。$\square$

在六维应用中，取含目标的侧 $A$，其孔数为四偶三奇；根 $u$ 位于 $B$。选两个偶孔作桥源 $S$，取 $r\in S$，将原端口与 $S\setminus\{r\}$ 配成 $D$。引理 7 给出包含 $M_A+D$ 的 Hamilton $r$–$v$ 路。删去 $D$，接上原跨边、两条源桥及标签边 $uv$，再压缩至 $B$。

精确几何证书保证 $e$ 是保留下来的原内部边，$R=\{p,q\}$ 与源镜像同奇偶，且 $u\notin R$。只需证明实际 $F_B$ 避开 $R$。若 $p,q$ 中有非原端口，其原短匹配伙伴与源镜像异奇偶，因而在源镜像集合外；该原边在压缩后原样保留，不能形成 $R$。压缩只将源镜像处的端点移至与 $R$ 异奇偶的伙伴，故只有二者均为原端口时才可能形成 $R$。此时设其 $A$ 侧伙伴为 $\alpha,\beta$，在 $D$ 中规定 $\alpha\beta$。从一条路径删除该边将两端分离；继续删边并添加不同的叶子不能重新连接它们。因此压缩后不含 $pq$。目标为端口时，其孤立片段接到 $u\notin R$，结论仍成立。

应用局部命题，展开并删除标签边 $uv$，得到包含 $M$ 的 Hamilton $u$–$v$ 路。30 个根星形与 118 个双源几何恰好互补，故十六孔层成立；详见 [双源转移及有限证书](research/six_directions/SIXTEEN_SMALLCUT_PROOF.md)。

## 7. 主定理与六方向推广的证明

**定理 2 的证明.** 给定 $M,u,v$，由引理 8 取 $L\supseteq M$，使 $u$ 自由且 $23\le|L|\le31$。于是

$$
h=|H(L)|=64-2|L|\in\{2,4,6,8,10,12,14,16,18\}.
$$

由有限引理 10，存在包含 $L$ 的 Hamilton $u$–$v$ 路，因而也包含 $M$。各孔层均允许 $v$ 已覆盖，故补全过程不影响定理的适用性。$\square$

**推论 3(a)、3(b) 的证明.** 先考虑 $Q_6$。若 $M$ 完美，应用 Fink 的定理；否则取自由顶点 $u$ 及其短邻点 $v$。由定理 2 得 Hamilton $u$–$v$ 路，加边 $uv$ 即成所需圈，证明推论 3(a)。

设 $n>6$。置换坐标后可设 $M$ 只使用后六个方向，并写

$$Q_n=Q_{n-6}\mathbin{\square}Q_6.$$

若 $M$ 完美仍应用 Fink 的定理。否则取自由顶点 $v_1$，令 $c_1,\ldots,c_k$ 为 $Q_{n-6}$ 的循环 Gray 次序，其中 $k=2^{n-6}$，且 $v_1$ 位于纤维 $Q_6[c_1]$。当 $n=7$ 时取两个顶点的循环次序即可。

对 $i=2,\ldots,k$，令 $u_i$ 为 $v_{i-1}$ 在第 $i$ 个纤维的对应顶点。在该纤维取包含局部匹配的 Hamilton 圈 $C_i$，选 $u_iv_i\in E(C_i)\setminus M$，删去此边得到 Hamilton 路 $P_i$。令 $u_1$ 为 $v_k$ 在第一纤维的对应顶点。

每次由 $u_i$ 至 $v_i$ 翻转后六坐标的奇偶性，而纤维间对应保持这些坐标。由于 $k-1$ 为奇数，$u_1,v_1$ 在第一纤维中异奇偶。由定理 2，以自由点 $v_1$ 为根得到包含局部匹配的 Hamilton $u_1$–$v_1$ 路 $P_1$。于是

$$
\bigcup_{i=1}^{k}P_i
\ \cup\ \{v_i u_{i+1}:1\le i<k\}
\ \cup\ \{v_k u_1\}
$$

为包含 $M$ 的 Hamilton 圈。$n\le5$ 的情形由已有五方向定理得到。$\square$

## 补充资料

本文是组会用证明正文。有限构造、完整枚举域与验证记录集中于 [证明资料汇编（HTML）](Ruskey-Savage_Q6_证明资料汇编.html)／[Markdown](Ruskey-Savage_Q6_证明资料汇编.md)；总证明入口为 [P6 总装证明](research/six_directions/P6_FULL_CLOSURE.md)。计算辅助证明目前通过项目内 ARIS 同族模型审计，尚未经外部同行评议或证明助手形式化验证。
