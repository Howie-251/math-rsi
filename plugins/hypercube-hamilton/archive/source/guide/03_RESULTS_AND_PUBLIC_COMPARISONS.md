# 成果、文献比较与准确范围

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

