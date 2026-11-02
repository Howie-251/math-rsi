# Proof Package: 全图匹配零行的五步闭游走同余障碍

## Claim

设 $G$ 是59点、最大度至多8、任意两不同点有长至多二路径的有限简单无向图。令 $A$ 为邻接矩阵，$B=A^2+A-7I-J$。

若 $G$ 三角形自由，且每点 $B$ 行均为2211匹配行（两个重二支撑点相邻、两个重一支撑点相邻、异权支撑之间无边），则矛盾。

更一般地，若只对零三角形点具有上述匹配行条件，记三角形总数为 $T$，五圈数为 $C_5$（不要求诱导），

$$s_v=\sum_uB_{vu}^2,\quad Q_2(v)=\frac12(B\mathbf e_v)^{\mathsf T}A(B\mathbf e_v),\quad e_v=Q_2(v)-s_v+5.$$

则必须满足

$$5C_5=209\cdot59+\sum_{t(v)>0}e_v-54T,$$

特别地

$$\sum_{t(v)>0}e_v+T\equiv4\pmod5.$$

## Status

PROVABLE AS STATED。完整纸面证明，尚未独立审阅或 Lean 核验。主代理提出迹矩路线，本子代理独立重算并补齐闭游走计数；不把同模型协作算作跨模型审阅。

## Assumptions and scope

原图由两步球界自动八正则。$B$ 为实际整数矩阵，$B\ge0$、$B\mathbf1=6\mathbf1$、$AB=BA$。只对 $t(v)=0$ 的行使用匹配条件；非零点的行型未加假设。不依赖父交集 RAW、c1 连通性、R2 循环分类或所有点 $t\le2$。

H5 结合已接受 N15 可以调用此结论，因此 H5 中至少存在一个真实三角形。这里只排除 H5 的全图三角形自由子范围；没有证明 H5 本身不可能。

## Notation

$\mathbf e_v$ 表示第 $v$ 个标准基向量；不加粗的 $e_v$ 是上述标量余项。

$n=59$，$s=\operatorname{tr}(B^2)=\sum_vs_v$，$w=\operatorname{tr}(AB^2)=\sum_v(B\mathbf e_v)^{\mathsf T}A(B\mathbf e_v)=2\sum_vQ_2(v)$。

五圈是由五个不同顶点按循环顺序形成的无向圈，按反向和循环移位识别；允许额外弦。

## Proof Strategy

用 $A^2+A=7I+J+B$ 逐级求迹，避免不可检查的高次展开。另一方面直接数长度五的闭游走。零行的两个迹贡献均固定为十，留下仅由非零行承担的精确同余。

## Dependency Map

1. 原图八正则，$A\mathbf1=8\mathbf1$、$B\mathbf1=6\mathbf1$。
2. 三角形闭游走 $operatorname{tr}(A^3)=6T$。
3. 矩阵乘法与迹循环不变性推出 $operatorname{tr}(A^5)$ 恒等式。
4. 真实五步闭游走分解：$operatorname{tr}(A^5)=10C_5+210T$。
5. 零行匹配条件给该行的 $s_v=10$、$2Q_2(v)=10$。

## Proof

**Step 1. Basic traces.** 八正则给 $\operatorname{tr}(A^2)=8n$、$\operatorname{tr}(AJ)=8n$、$\operatorname{tr}(B)=\operatorname{tr}(A)=0$。因此

$$\operatorname{tr}(AB)=\operatorname{tr}(A^3)+\operatorname{tr}(A^2)-7\operatorname{tr}(A)-\operatorname{tr}(AJ)=6T.$$

用 $B=A^2+A-7I-J$ 乘以 $B$ 并取迹，及 $\operatorname{tr}(BJ)=6n$，得到

$$\operatorname{tr}(A^2B)=s-6T+6n.\tag{1}$$

同一个式子由定义展开成 $\operatorname{tr}(A^4)+6T-120n$，故

$$\operatorname{tr}(A^4)=126n+s-12T.\tag{2}$$

**Step 2. Fifth trace.** 使用 $A^2=7I+J+B-A$，以及 $AB$ 行和四十八，

$$\begin{aligned}
\operatorname{tr}(A^3B)
&=7\operatorname{tr}(AB)+\operatorname{tr}(ABJ)+\operatorname{tr}(AB^2)-\operatorname{tr}(A^2B)\\
&=48T+42n+w-s.
\end{aligned}$$

于是再乘一次同一恒等式，且 $A^3$ 行和 $8^3=512$，

$$\begin{aligned}
\operatorname{tr}(A^5)
&=7\operatorname{tr}(A^3)+\operatorname{tr}(A^3J)+\operatorname{tr}(A^3B)-\operatorname{tr}(A^4)\\
&=428n+w-2s+102T.\tag{3}
\end{aligned}$$

**Step 3. Count five-step closed walks.** 若五步闭游走的五个循环位置互异，它正是一个五圈，按起点五种及方向两种共贡献十次。

若不是五个不同点，则因无自环，它必有循环意义下相隔两步的重复位置，产生一次立即回退；删去该两步后得到一个三步闭游走，即一个三角形。原五步游走的支撑只能是这个三角形自身，或者三角形附加一条走去又走回的边。因此每个非五圈闭游走归属唯一三角形。

固定一个三角形。若附加边在三角形内部，选择哪条边被走三次有三种；每种对应一个循环五步词的两个方向和五个起点，共十次。因此此类贡献三十次。若附加边通向三角形外，三个三角形点各有 $8-2=6$ 条这样的边，共十八条；每条同样贡献两个方向乘五个起点，即十次。即使外部端点还邻接三角形的其他点，当前游走没有使用那些边，也不会产生重复归属。

每个三角形总贡献 $30+18\cdot10=210$，故

$$\operatorname{tr}(A^5)=10C_5+210T.\tag{4}$$

**Step 4. Universal exact identity.** 比较 (3)、(4)：

$$10C_5=428n+w-2s-108T.\tag{5}$$

所有计数均为精确整数，没有谱近似或浮点步骤。

**Step 5. Contributions from matching zero rows.** 对零点 $v$，行平方和为 $s_v=2^2+2^2+1^2+1^2=10$。向量 $B\mathbf e_v$ 支撑上的诱导原图恰为两条同权边，故

$$(B\mathbf e_v)^{\mathsf T}A(B\mathbf e_v)=2(2\cdot2+1\cdot1)=10.$$

这里是向量二次型，对应整个 $\operatorname{tr}(AB^2)$ 中的一项；没有把它误当成 $AB$ 的单个条目。

若全部点为零，$s=w=10n$、$T=0$。(5) 给 $10C_5=418n=24662$，右边不被十整除，矛盾。

**Step 6. Nonzero-row remainder.** 一般情况下把零点各贡献的 $w_v-2s_v=-10$ 从 (5) 拆出：

$$10C_5=418n+\sum_{t(v)>0}\bigl(2Q_2(v)-2s_v+10\bigr)-108T.$$

除二即得主张的精确恒等式。模五时，$209\cdot59\equiv1$，$-54\equiv1$，故 $\sum_{t(v)>0}e_v+T\equiv4\pmod5$。∎

## Corrections or Missing Assumptions

零行矩量固定值不能套给非零行；它们全部以 $e_v$ 保留。三角形自由假设只用于直接的全零矛盾，后面的同余适用于有三角形情况。

## Open Risks

迹恒等式和闭游走系数待独立审阅与形式化；不要求重新运行历史 RAW。最有价值的下一义务是由同一图的非零行、三角形结构及零行相互作用，限制 $e_v$ 的可能值并与同余合用，而不是默认其无法满足。
