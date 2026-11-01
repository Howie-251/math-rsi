# 五元、最大度7/8：原始定理的短范围核查

本轮没有找到能直接推出“任意五元、最大度7或8超图可二染色”，或能直接覆盖22–24点35边及最小度6局部星的原始定理。这个结论只描述下列实际阅读范围，不声称穷尽文献，也不声称上述最大度命题已知为假或仍公开未解。

最重要的数学界线是：**Thomassen的均匀度=正则度定理不能换成五元、七度或八度；已读的有限常数稀疏定理在本参数也确实不足。**

## 实际覆盖回执

先检索现有`research-wiki/papers/`、`ref/README.md`及本地相关论文；随后沿regular/maximum-degree原始来源定位。定理核对固定为五份材料：

| 原始来源 | 实际阅读范围 | 本轮结果 |
|---|---|---|
| C. Thomassen, *The even cycle problem for directed graphs*, JAMS 5(2) (1992), 217–229, DOI 10.1090/S0894-0347-1992-1135027-1 | 作者上传原文的引言、§5 pp.226–227，特别Theorem5.1；未重读全部有向图主证明 | 等边点数临界结构，不能套35>24 |
| M. A. Henning, A. Yeo, arXiv:1611.08850v1 | pp.1–5、10中的定理声明与NAE接口；未审完整14页证明 | 明确regular假设、free-vertex及NAE3的适用条件 |
| A. Pluhár, *Greedy colorings of uniform hypergraphs*, RSA35 (2009), 216–221 | 本地PDF pp.2、4–5，Theorem4及其证明、Corollary6 | 五元时最大边相交数D≤7，当前δ≥7实际图不能满足 |
| J. Radhakrishnan, A. Srinivasan, *Improved bounds and algorithms for hypergraph 2-coloring*, RSA16 (2000), 4–32 | 本地PDF引言及§4，尤其Theorem4.2/证明尾部 | sufficient-large-uniformity，不能把0.17直接代入5 |
| D. Karpov, N. Gravin, *On proper colorings of hypergraphs*, arXiv:1111.1558v1 | pp.1–5，Theorem1、image定义及Lemma1的交替链证明 | Δ7/8时只给3/4色；有可借鉴的整体配对表示 |

前两篇的精确来源链接分别为[Thomassen作者上传原文](https://www.researchgate.net/publication/239064875_The_Even_Cycle_Problem_for_Directed_Graphs)、[Henning–Yeo原稿](https://arxiv.org/pdf/1611.08850)。Thomassen的AMS原文链接本轮读取未成功，未把失败读取当成成功；实际核对的是作者上传的同一原文。后两份本地PDF仍保留原样；只在本目录保存文本抽取。

## Thomassen究竟保证什么

原文Theorem5.1（p.227）的内容是：若H是**极小不可二染色**超图且|V(H)|=|E(H)|，则H有大小至多3的超边，或有度数至多3的顶点。这里的≤3同时出现在两侧，并非“所有最小度至少4的均匀超图均可染”。[原文§5](https://www.researchgate.net/publication/239064875_The_Even_Cycle_Problem_for_Directed_Graphs)

通常引用的推论是：k≥4时，每个k-uniform、k-regular超图都可二染色。Henning–Yeo原稿pp.1–2先定义H_k正是均匀度和正则度都等于k的类，再于Theorem2准确陈述此结果。本轮由这一明确接口核验，未尝试将它推广为最大度7/8。[Henning–Yeo，Theorem2](https://arxiv.org/pdf/1611.08850)

对本题：五元五正则可以覆盖，五元七正则、五元八正则及五元最大度7/8均不在这个statement内。22–24点且恰35边时175>7n，事实上最大度≤7连度数和都不可能；真正可能的入口是最大度8及更高。原图35边、至多24点也不满足Theorem5.1的等数假设。

两个看似省事的转换有具体障碍：

- 若将35条五边各缩成四边，再想套四元最大度4/四正则，保留35条带标签约束需140次关联，至多24个点容量仅96，不可能。缩边重合后删除重复约束可能改变此计数，但必须另证明足够多重合，不能直接套定理。
- 将H对偶可得到最小边大小7/8、最大顶点度5的另一超图；其顶点二染色对应**原H的边二染色、每个原顶点见两色边**，不对应原H的顶点二染色。不能借对偶偷换目标。

## 有限最大边相交数判据的精确代入

Pluhár Theorem4：若H是r-uniform，每条边至多与D条其他边相交，且

2e(2D²−D)((r−1)!)²/(2r−1)!≤1，

则H可二染色。该statement和两链依赖计数的证明已实读本地原文pp.4–5；[原稿来源入口](https://doi.org/10.1002/rsa.20267)。这里D是**边的相交度**，不是顶点最大度。

r=5时条件精确为

e(2D²−D)/315≤1。

D=7成立，因为e<3给91e<273<315；D=8不成立，因为e>8/3给120e>320>315。故这个有限充分条件只保证整数D≤7。

对实际简单五元H，固定边f有

Σ_{v∈f}(d(v)−1)=Σ_{g≠f}|f∩g|≤4D_f。

若δ(H)≥7，则左侧≥30，因此D_f≥8。于是当前最小度7/8分支的每条边都违反该充分条件，不能期待通过更准确计算平均D补救这份现成定理。最小度6时只迫D_f≥7，故它仅可能覆盖另有独立结构保证“每条边相交至多7次”的极窄支；本轮没有从真实预算推出该条件。

普通随机二染色的对称Local Lemma更弱：坏边概率1/16，仅由相交依赖图得到e(D+1)/16≤1，保证D≤4。把顶点最大度Δ换算成D≤5(Δ−1)对Δ7/8远远不足。

## 渐近常数为何没有提供五元门

Radhakrishnan–Srinivasan原文Theorem4.2（本地稿p.13）保证：对充分大的r，若最大overlap D至多

0.17 sqrt(r/ln r)·2^r，

则可二染色；这里采用原文引言定义的overlap，计入本边。原文statement明确有充分大r，证明尾部也选随r渐近的参数。本轮没有获得其可取r=5的有限阈值，因此不将数值代入5用作证书。[作者原稿](https://www.cs.umd.edu/~srin/PDF/Older/hypercol-jou.pdf)

同样，带绝对存在常数c、以2^r/sqrt(r ln r)控制最大顶点度的概述，若不给可用于r=5的常数和范围，就不能排Δ7/8。本轮不把渐近阶数当成小参数定理。

## 最接近的可借鉴整体结构

Karpov–Gravin Theorem1：若最大顶点度Δ、每边至少r点，令q=ceil(2Δ/r)，则可用q+1色；r≥3且q≥3时可用q色。因此r5、Δ7只给3色，Δ8只给4色，均非Property B。[原文Theorem1](https://arxiv.org/pdf/1111.1558)

其Lemma1更有结构价值：每条超边可选一个内部点对，所得带重图image的最大度≤ceil(2Δ/r)。证明用交替链移动被选点对，把高负载沿同一实际H传递，而不是独立选各局部视图。对Δ8就是最大度4图；若能进一步使image二分即可二染色H，但论文并未保证这一点。任何“无奇圈image”的新引理仍需证明，不能把它当已发表结论。这是本轮最接近整体降复杂度的现成表示。

Henning–Yeo的NAE接口也准确但不直接覆盖：Theorem4要求连通非空NAE-3-SAT、子句数<变量数、每变量出现至多3次，推出可满足且有free变量；Lemma5将其用于三元超图。若某个局部星修复能真实化到这样的低出现实例，可调用它；当前原始五元35子句、22–24变量且出现7/8次同时违反三个数值接口，尚无合法转换。[原文Theorem4及Lemma5](https://arxiv.org/pdf/1611.08850)

本轮未找到能仅由“最小度6”及局部link大小推出所需二染色的外部结构定理。继续搜索同义最大度关键词的信息增益已低，故在此停止，不扩大文献清单或局部算表。
