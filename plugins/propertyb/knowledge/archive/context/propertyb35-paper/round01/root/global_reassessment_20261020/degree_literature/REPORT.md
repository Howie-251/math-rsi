# 有界度数／线性超图文献定位

核查日期：2026-10-20。结论：本次四个原始来源没有提供能直接排除当前八个开放分支的定理，也没有给出仅以“非线性点至多17个”为前提的可用五元定理。不建议把现有最大度或线性渐近定理作为新的闭合入口。这是限定四篇原文后的适用性判断，不是声称文献中不存在更强定理。

## 先核实际输入

设实际输入为25点、35条五元边、pair-cover、最小度6，恰有 $r>0$ 个六度点。

* 总度175。若其余点度数均至多7，总度至多 $6r+7(25-r)=175-r$，矛盾。因此 **实际最大度至少8**；即使找到一般 最大度6或7可二染色定理，也不能直接覆盖这里任何 $r>0$ 输入。
* 六度点 $z$ 的共度行满足 $\sum_{x\ne z}\lambda_{zx}=24$，24项均至少1，所以全部为1。所有重复点对都在其余 $h=25-r$ 个点内，这是输入的自动性质。
* 全部点对额外重数为 $\sum_{x<y}(\lambda_{xy}-1)=35\binom52-\binom{25}2=50$。因此全图不可能线性；线性25点五元图至多30边。
* $r\ge8$ 只使上述非线性点集合满足 $h\le17$，没有给最大度上界6或7，也没有使删去这17点后的约束仍为五元边。只取高点诱导子图会丢掉其余原边；把低点从原边删除则产生不同大小的边。两种操作均不能直接调用线性五元定理并把染色接回原图。

同样，21至24点、35边的平均度均大于7，故这些点数的实际输入也必有度至少8的点。以下最大度5的精确定理不覆盖八个开放分支。

## 四个原始来源及精确适用条件

| 原始来源 | 已核原定理位置／条件 | $k=5$ 的实际结论 | 对25点 $r\ge3$ 的覆盖 |
|---|---|---|---|
| C. Thomassen, *The even cycle problem for directed graphs*, JAMS 5 (1992), 217–229 | §5、Theorem 5.1，期刊p.227：极小非二染色且 $N=M$ 的超图，存在大小至多3的边或度至多3的点 | 配合该文介绍的极小非二染色边数至少点数事实，得五元最大度至多5可二染色；不是最大度6或7定理 | 无；实际最大度至少8 |
| A. Chattopadhyay, B. A. Reed, *Properly 2-Colouring Linear Hypergraphs*, APPROX–RANDOM 2007, 395–408 | 作者版Theorem 1，PDF p.2：固定 $1/2<\varepsilon<1$，线性 $k$-元图满足 $\Delta\le2^{k-k^\varepsilon}$，且 **$k\ge k_\varepsilon$**，有确定性多项式算法 | 不能删除充分大条件。机械代入5所得上限小于 $2^{5-\sqrt5}=6.79245\ldots$，并不证明五元最大度6的情形 | 无；既没有证明5达到阈值，实际图也非线性 |
| J. Kozik, *Multipass greedy coloring of simple uniform hypergraphs*, arXiv:1310.5984v2 | Theorem 1，PDF p.2：线性图的二染色最大度保证为 $\Omega(2^k/\log k)$。Theorem 4（p.3）推广至固定交叠上界的 $b$-simple 图；证明pp.17–19多次明确边长充分大 | 没有由这一定理确定的五元最大度6或7数值保证；不能把隐藏常数和起始阈值忽略 | 无；没有少数非线性点的有限五元结论 |
| J. Radhakrishnan, A. Srinivasan, *Improved bounds and algorithms for hypergraph two-coloring*, RSA 16 (2000), 4–32 | 本地作者版§4、Theorem 4.2，PDF pp.12–13：重叠参数 $D\le0.17\sqrt{k/\log k}\,2^k$，**$k$充分大**。$D$ 按引言包括边自身，不是顶点最大度 | 渐近公式不能代入5。保留证明中的有限充分不等式也不能处理 $D\ge6$，见下 | 无；实际 $D\ge\Delta\ge8$ |

原文链接：[Thomassen DOI](https://doi.org/10.1090/S0894-0347-1992-1135027-1)，[作者上传的原文扫描及全文](https://www.researchgate.net/publication/239064875_The_Even_Cycle_Problem_for_Directed_Graphs)；[Chattopadhyay–Reed作者PDF](https://www.tcs.tifr.res.in/~arkadev/linearNew3.pdf)；[Kozik原文v2](https://arxiv.org/pdf/1310.5984v2)；[Radhakrishnan–Srinivasan作者PDF](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf)。后者已有本地 [PDF](../../../../../../ref/radhakrishnan_srinivasan_2000_two_coloring.pdf)，没有重新下载。

这里后三篇所说的“simple”／“nearly-disjoint”通常指任意两条不同边交至多一点；不能换成本项目仅无重复边的simple。

## 两个容易误套的有限参数核查

**Thomassen。** 若五元 $\Delta\le5$ 图不可二染色，取极小不可二染色子图，去除孤点后记点边数为 $N,M$。由该文所述极小不可二染色计数 $M\ge N$，而 $5M\le5N$，故相等，且全部点度5。Theorem 5.1给出大小至多3的边或度至多3的点，矛盾。这里等式靠 $\Delta\le5$ 得到；把5换成6或7，等式步骤即消失。没有将平均度7当成正则度5。

**慢重染色的局部有限条件。** 原文Claim 4.1和Claim 4.2的证明，在使用渐近选择前给出可逐参数检验的充分条件

\[
 4D2^{-k}(1-p)^k+8D^2 2^{1-2k}p\le\tfrac14,
 \qquad 0\le p\le1.
\]

在 $k=5$ 时左端为 $F_D(p)=\frac D8(1-p)^5+\frac{D^2}{64}p$。其 $D=6$ 的最小值为

\[
 \min_p F_6(p)
 =\frac9{16}\left[1-\frac45\left(\frac3{20}\right)^{1/4}\right]
 =0.2824501602\ldots>\tfrac14.
\]

函数对 $D$ 单调，所以所有 $D\ge6$ 均过不了这个充分条件。它在 $D=5$ 时最小值约0.2048114；这既不是反例，也不是不可染性结论，只是所核充分门的准确边界。无需重跑现有完整局部表。

## 现有材料、实际阅读范围与覆盖收据

先检索了 `research-wiki/papers/`、失败图册和 `ref/` 文件名；已有Radhakrishnan–Srinivasan与Ferber–Shapira条目。后者现有“singleton边对”工具已在项目使用，不是新的最大度或少数非线性点定理，因此未再打开其PDF或列为第五个候选。

本次冻结的深入候选恰为上表四篇，四篇均完成所列定理条件核对，无未读候选冒充已核。实际范围为：Thomassen引言及§5（期刊pp.226–227；作者上传扫描的全文转录，未重证此前有向图定理）；Chattopadhyay–Reed摘要、Theorem 1和线性定义（PDF pp.1–3）；Kozik摘要、定义、Theorems 1/4及Theorem 4参数证明（pp.1–3、17–19）；Radhakrishnan–Srinivasan本地作者版pp.1–3及12–14。没有声称逐页审完四篇全文。

规范arXiv metadata helper已针对Kozik标题调用一次，HTTP 429退出；未重试，改用已读取的arXiv原始版本元数据及PDF。未下载新PDF，未修改wiki、claim、导航或任何数学证明。

**可供下一步使用的判断：** 本轮没有新增可闭整类范围。若另寻文献，应要求原定理显式处理至少最大度8、有限边长5及一个承载所有重复点对的至多17点集合；单纯线性渐近阈值或最大度6／7改进仍不能绕过当前实际义务。
