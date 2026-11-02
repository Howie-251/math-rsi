# (26,3)：经典7514推论与7531候选的有限比较

检索日：2026-11-01 UTC。仅本格，已有primary公式＋2批窄web检索；没有读边表、构图、BFS、solver、Lean、安装或改冻结八图交付。

**本次最强找到的公开来源保证可推至7514，不应只用7225比较。未找到公开≥7531；global_record_confirmed=false，首创未认证。** 7514是公开构造与公开定理的直接数学推论，没有定位到单独发表的7514数值条目或边表。任务下达时7531仍未生成，本报告不将它计作新图。

## 一手几何与基图

[arXiv2608.27253v2 §3.4.2](https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2)的Delorme opposite-GQ公式在s=t=4给25度、D3、7225点。

[Delorme，Grands Graphes，EJC6(1985) §8(a)](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf)构造W(3,q)的q²+1线spread。[De Bruyn原论文§4.1及§4.2](https://arxiv.org/html/2309.01228v1#S4.SS1)对q偶数明确使用椭圆二次曲面及其tangent-line symplectic quadrangle；每条GQ线恰交ovoid一点。[Offer–Thas–Van Maldeghem2005 §2.1 pp376–377](https://cage.ugent.be/~hvm/artikels/139.pdf)给ovoid/spread的st+1基数，并由椭圆截面及q偶数时Q(4,q)≅W(q)另支持存在性。因此q4可用17点ovoid与17线spread。这里只是存在性来源，未检验producer的具体坐标嵌入。

## 7514：Delorme §7可直接用，但须用正确版本

设O为ovoid、R为line spread，取7225基图内S=O×R，|S|=289。对任意旧顶点(p,l)，raw cross-incidence下唯一的S邻点是

`(o(l),r(p))`，o(l)为l上唯一O点，r(p)为过p的唯一spread线。

**S不是距离≥3的独立中心集。** 写p_i为第i条spread线上的ovoid点，则S内的非平凡邻接为(p_i,l_j)与(p_j,l_i)，i≠j；所以G[S]为136个K2与17个孤立flag中心。

这恰可应用[Delorme §7 p297的一般诱导子图复制定理](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf)，取A0=S、A1=空：

- 条件(a)对空A1自动满足。
- 条件(b)：每个S外顶点恰有一个S邻点。
- 条件(c)：每个分量是单点或K2；选某端点的S外邻点z，分量内任意x,y均有d(x,z)+d(y,z)≤3。S内度至多1而原度至少24，故外邻点存在。

因此公开定理直接给`N=7225+289=7514，Δ≤26，D=3`。这个一般定理已发表；本次没有在所读原文找到显式O×spread配方，不能将此代入声称为已发表的特定7514图，也不能把通用复制机制称为本地首创。只引用“两两距离≥3中心”的特例反而不足，因为136对中心本来相邻。

## 是否已有更强公开保证

PolarStar合法IQ／Paley代入在cap26分别最大5526（q17,d8）与5219（q17,Paley17），均低于7514。检索遇到的8775点一般族明确最大度27、最小度26，不能混成cap26反例；这也与原q2×q8产品的度数27一致。2批窄检索未定位≥7531，一部分纯数字检索召回较弱，不能证明世界上没有更强构造。

上一轮Delorme原JGT1985全文缺口继续保留：opposite-product原文章仅取得出版社摘要，未重试；不能说原文未含ovoid×spread或其它增强规则。新source7242是本项目结果，不作为已公开外部基线倒推。

若producer生成并验收7531，其首先可支持的比较是**比上述公开来源推论7514多17点**。父级拟议的289个完整N克隆／97750边／度分布25:306、26:7225与固定7242源容量上界均由实际构造任务另验；本任务没有验证它们或认证全球纪录。机器摘要和检索词见[JSON](DEGREE26_EXTENSION_20261101.json)。
