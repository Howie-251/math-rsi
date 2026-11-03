# (64,3) spread target：定向公开机会门

检索日：2026-11-01 UTC。此文件是文献门，不是新图或构造验收。已先保存同名前缀 `PRED.json`。本任务未生成几何、边表或源代码，未运行 solver、Lean、BFS；未联系作者、安装软件或更新全局计数。

**结论：本次 best-located 公开来源保证是 160000 点；未定位到最大度数 ≤64、直径 ≤3、阶数 ≥160050 的一手保证。该参数未被本次公开门阻断，但检索不完整，不能认证全球最高或优先权。** 160000 是已发表一般公式的代入，不是本次找到的单独公开 160000 点边表。160050 仍只是尚未构造、尚未验收的预测。

## 已读 primary 与适用范围

| 一手来源 | 对 degree 64 的具体读出 | 与目标的关系 |
|---|---|---|
| [Isham–Lakhotia–Monroe–Petrini，arXiv:2608.27253v2，2026-10-22，§3.4.2](https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2) | Delorme opposite-GQ：`N=(s+1)(t+1)(1+st)^2`、`Δ=(s+1)(t+1)`；允许全部 prime-power 的 `(s,t)=(q,q)`。取 `(7,7)` 得 `Δ=64,N=160000`。同节 Payne 参数 `(6,8)` 给 `Δ=63,N=151263`，在cap64内但阶数较低。 | 当前最大已定位保证。原始归属是 Delorme JGT1985，而非2026论文首创。 |
| [Delorme，Grands Graphes，EJC6(1985),291–302，§2、§6–8](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf) | §2单GQ极性商要求 `q=2^(2a+1)`，`Δ=q+1,N=(q+1)(q²+1)`。`q=32` 源33825、33度，复制1025个绝对点到cap64给 `64×1025=65600`。§6允许全部2幂的另一D3构造在 `q=16` 给51度52428。 | 均低于160000。`q=64` 既不满足§2奇指数条件，名义 `q+1=65` 也超过cap64，不能拿它阻断本目标。 |
| [同2026 primary，Corollary7.9、Lemma7.10、§7.5、§7.7](https://arxiv.org/html/2608.27253v2#S7.SS4) | 新双极性产品要求各GQ本身有极性，已知厚GQ参数为1或奇指数2幂；不是任意q7。degree≤64的GQ×GQ直接产品最大为 `(q,r)=(2,8)` 的27度8775；允许GQ×三角形的混合产品时，`(8,5)` 为54度18135。 | 未给160050；固定绝对点复制的公式代入仍低于目标。未把小度Table3当全球分类，也未把任意诱导子图复制优化穷尽。 |
| [Lakhotia et al.，PolarStar，SPAA2024，Proposition2、§7、Figure7](https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf) | Figure7明确列出64度IQ为79506点、Paley为77613点；IQ满足 `q` prime power、`d'≡0,3 mod4`。具体IQ是 `q=43,d'=20`，`1893×42=79506`。 | 是明确公开数值，低于目标。2024图中的“largest known”限定该文时间与比较范围，不能用作2026全球认证。 |
| [Bachratý–Šiagiová–Širáň，JCTB134(2019),203–217，预印本Theorem1](https://arxiv.org/html/1709.09760v1) | `q=2^(2n+1),n≥1`，阶数 `q²(q−1)`。可能相关的q8/q32阶数仅448/31744；下一q128阶数2080768已经大于 `Moore(64,3)=258113`，不可能是cap64的D3图。 | 该具体近Moore渐近族没有更强64度实例；没有仅凭度数上界误判。 |
| [Cames van Batenburg–Korsky，arXiv:2608.03965v1，Proposition3.1、§4](https://arxiv.org/html/2608.03965v1#S3) | 直接D3族最小 `H(3,2)` 已有2893695点，大于上述Moore界。其§4线图变体取D2底图：最小 `H(2,2)` 有1085点，大于 `Moore(32,2)=1025`，故其实际底图度数≥33，`L(B(H))` 度数为其2倍、至少66。 | 两个具体入口均不适用于cap64；渐近定理不直接给64度新下界。 |

上述都是来源与小整数公式比较，不是新构图实验。2026产品的绝对点复制：GQ2×GQ8给 `8775+37×325=20800`；GQ8×PG(2,5)给 `18135+10×390=22035`。这些仅解释已读通用复制为何没有阻断本目标；一般任意诱导子图复制仍未做最优性断言。

## balanced GQ + spread flags 的既有性边界

[Delorme EJC1985 §8(a)，pp298–299](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf)已经明确用不可约二次多项式的矩阵构造，将 `W(3,q)` 的点分成 `q²+1` 条互不交迷向直线；因此 q7 的400点、400线、每线8点和50线spread属于经典几何。§8(a)随后用于**直径4的关联图升一度**；§7和§8(c)的复制也是升度规则。它们并没有在已读陈述中明确写成当前“opposite图保持度数、用incident flags余度补hub”的规则。

需要追查的具体命题/公式是：有spread的 balanced GQ(q,q) 的 opposite 图，能否在保持 `Δ=(q+1)²,D=3` 下，加入 `q²+1` 个hub并覆盖全部incident-flag余度，从而

`N=(q+1)²(q²+1)²+(q²+1)=(q²+1)[(q+1)²(q²+1)+1]`。

q7代入是160050；基图的3200个incident flags度63，其余156800点度64；50个hub若各接64个pins，恰好用完3200余度。这是待核接口和计数预测，不是本文新验收的通用定理，也不把已有条件式Lean接口视作q7具体实例。

**本次未定位上述同度数增强命题的公开出处，不能据此声称首创。** 重要缺口继承：原始 opposite-product 来源 [Delorme，Large bipartite graphs with given degree and diameter，JGT9(1985),325–334](https://doi.org/10.1002/jgt.3190090304) 全文此前未取得，出版社入口仅回摘要；本次没有重复盲取。2026 §3.4.2只给基图公式，全文检索“spread”无命中。

## 检索回执与停止建议

本次只做两批窄web查询，之后仅打开已定位的primary和在文内查找：

1. `"degree" "64" "160000" graph diameter`；`graph diameter 3 "160050"`；`Delorme generalized quadrangle spread diameter three degree construction flags`；`"diameter 3" "64" graph largest generalized quadrangles`。
2. `"graph" "160,050" diameter`；`"diameter" "160000" Delorme`；`"diameter 3" "spread" Delorme`；`"generalized quadrangle" "diameter" "flags" "spread"`。

没有返回可定位的160050相关构造；召回包括PolarStar、维护者Comellas的D3说明页和无关spread几何。未把无命中当不存在证据。PolarStar在线PDF本次直接open超时，读出由此前已保存的primary全文和本次web索引的Figure1/7信息共同支持；未重复下载大包。[Comellas维护页](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g3.html)仅作引用链检查，未取得覆盖64度的完整维护主表。

建议：**公开门暂时保留q7/64这一单一机会；如继续，仅先做400点几何/50线spread与50步current-pin-cover的有界具体门。** 本报告不授权本子任务继续构图，也不宣称成功概率。若后续定位任何cap64、D3、`N≥160050`的一手保证，立即停止此参数。q5/36已被继承的公开35度35875保证压过，不重开；本任务不接q8/q9或其它模板。

机器摘要见同名 `.json`。全球纪录、优先权、明确公开数值、公式存在性推论与本地合法图继续分账。
