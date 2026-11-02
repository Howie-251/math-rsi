# D3三项public-dominated比较：原始来源与数值身份

2026-11-01，本次仅只读本地primary缓存及既有公式报告，没有联网、重验图、BFS、field/rank、Lean或新的参数数值扫描，也不改root/catalog/Wiki计数。13D5的88452来源不在本note重复。

**结论：三项都有适用的已发表构造依据；但35875、161650、169900在这里都是已发表方法的具体代入／组合推论，不能写成“已找到作者发布该点数的完整graph文件”。没有用STATE字段代替出处，也没有认证这些是当前全球最大值。**

| 本地合法图 | 比较保证 | 精确代入 | 数值的证据类型 |
|---|---:|---|---|
| max35，D3，20580点 | 35875 | q32极性商33825／max33；1025绝对点各加2个副本 | Delorme已发表定理的直接代入；未定位单独35875边表 |
| max65，D3，旧161150点 | 161650 | 160000＋1·(33·50) | 公开opposite-GQ源＋2007实际partial ovoid存在结果＋一般复制的组合推论 |
| max70，D3，旧166650点 | 169900 | 160000＋6·(33·50) | 同一组合推论；不是2007论文直接印的D3图点数 |

## 35度：回到Delorme原文，参数与D3没有混用

Charles Delorme，*Grands Graphes de Degré et Diamètre Donnés*，European Journal of Combinatorics6(1985),291–302。

- 原始PDF：[Comellas保存的全文](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf)。
- §2，印刷p292：q为2的奇数次幂时，极性商给最大度q+1、直径3、阶数(q+1)(q²+1)。这里q=32=2^5合法；不是把q16误放进这一族。
- §8(c)，印刷p299：删掉diagonal loops后，q²+1个absolute顶点degreeq、互距3，每个nonabsolute顶点恰有一个absolute邻点；原文明确说明对该集合可重复复制升度。
- §7，印刷pp297–298：复制的degree／diameter规则。

由这些实际原文，q32给33825点／max33／D3，absolute集1025点；每个absolute各添2个副本，非absolute旧点各增加2个邻居，maximum33→35，而absolute及副本degree32。最终33825+2·1025=35875，D3保持。它与本地F7/C60的20580点图是不同构造。

即使不使用两次复制的35875，已发表§2的33度33825图也满足maxdegree≤35，且33825>20580，已足以否定本地20580在cap35的纪录竞争性。没有依赖某个degree更大的图，也没有把D4／D5误作D3。

现代primary复述：[Isham–Lakhotia–Monroe–Petrini，arXiv:2608.27253v2](https://arxiv.org/html/2608.27253v2#S7.SS7)，§7.1／§7.3给极性商参数与直径，§7.7给absolute集k次复制。它是对原规则的交叉出处，不能说该文明确发布35875这个数字的边表，也不是Mizuno35package。

本地可复核：`delorme1985_primary_text.txt`中§2／§7／§8(c)原始提取文本；`../f7_c60_d35/PUBLIC_COMPARISON.md`是最初此具体35比较的归档；`DEGREE54_ROUTE_TARGET_GATE_20261101.md`重复核了同一q32基线；`Q4_NEW_ROLE_REPLICATION_WINDOW27_34_20261101.md`明确澄清35875不是新找到的Mizuno35图。

## 65／70度：原始33点对象＋公开构造组合

决定性小对象来自Miroslava Cimráková、Veerle Fack，*Clique Algorithms for Finding Substructures in Generalized Quadrangles*，JCMCC63(2007),129–143。

- [出版社论文页](https://combinatorialpress.com/jcmcc-articles/volume-063/clique-algorithms-for-finding-substructures-in-generalized-quadrangles/)。
- [出版社扫描PDF](https://combinatorialpress.com/article/jcmcc/Volume%20063/vol-063-paper%2012.pdf)，印刷p140／§4.3／Table5（PDF第12页）。
- W(7)行列出(s,t)=(7,7)、400points、st+1=50、理论bound43，以及程序实际找到的largest partial ovoid **33**，不等价最大对象数1。此次再次直接读了已有p140扫描图，未使用OCR猜列，没有把43当构造。
- p131／§1的W(q)是PG(3,q)的symplectic quadrangle，即W(3,q)。这是W(3,7)的partial OVOID，不是Q(4,7)partial ovoid对偶后得到的partial SPREAD。只需论文已找到33点对象的存在性；本次未复跑作者穷尽或取得作者的原坐标列表。

公开opposite-GQ源公式由[arXiv:2608.27253v2 §3.4.2](https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2)明确重述Delorme的另一项1985构造：

    n0=(s+1)(t+1)(1+st)^2,  maxdegree=(s+1)(t+1),  D3.

取s=t=7，得160000点／max64／D3。q7作为prime power的GQ参数合法；这个opposite-product构造不要求q7有极性，不能与上面q=2^odd的单极性商条件混为一谈。这里使用公开未填补160000源，不偷用本项目160050源或O22。

Delorme EJC1985 §8(a)，p298，给同一symplectic W(3,q)的q²+1条spread，q7为50条。取已发表partial ovoid O33与spread R50，C=O×R有1650中心。其复制条件具体如下：

- C外点(p,L)的C邻点要求O中心落在L且spread线含p。partial ovoid令每条L至多含一个O点，spread令p只在一条R线上，故外点至多一个C邻点。
- C诱导图是matching加isolated vertices，而非独立集。每个matching分量或孤点均可用原源C外邻点满足§7的分量距离条件；源最小度63，C内至多一个邻点，故该旧外邻点存在。
- 必须用Delorme原始§7的一般INDUCED-SUBGRAPH复制定理。它包括匹配中心副本间的对应边，不能只引用“中心互距≥3”的独立集特例或删掉所需new-new边。
- 每步原C不变，新增副本对原C仍至多一个邻点，因此可重复k次，maximum每次至多升1，D3保持。

所以既有公开方法直接推出

    N(Delta,3) ≥ 160000+(Delta−64)·1650.

既有比较代入Delta65、k1给161650；Delta70、k6给169900，分别超过旧本地图161150／166650。它们由D≤3及大于相应D2 Moore数得到精确D3。并未把原regular程度或不同diameter误用。

opposite公式原出处是Delorme JGT9(1985),325–334，和上面的EJC6(1985),291–302是两篇不同论文。本地未取得JGT全文，故该源公式在本audit中实际根据2026primary论文§3.4.2的明确复述，不假装直接读过缺失原文。一般复制与spread则已直接读到EJC原文。这个来源层级须保留，但当前已读数学前提足以支持上述特定保证；它不证明JGT原文没有更强方法。

本地可复核：

- `w3_f7_threshold25_sources/CIMRAKOVA_FACK_JCMCC63_2007.pdf`及`jcmcc-page12-0-FXX1.png`保存实际p140Table5。
- `arxiv_2608_27253v2.html/.txt`保存opposite公式及[20]原始citation。
- `delorme1985_primary_text.txt`保存§7与§8(a)。
- `W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.{md,json}`逐项区分33、43、ovoid/spread和组合归属。
- `DEGREE70_MULTIPLICITY_TARGET_GATE_20261101.md`最早主体使用15点保守前提；顶部后续修订已被33覆盖。不能继续取其旧164500与正优势段落当当前比较。

## 给用户清单的准确措辞

这三例宜标为“已发表方法可推出更大保证”，并附上本note的公式与原文位置；不宜只写“已找到某个作者发布同数字的大图”，也不能把35875／161650／169900称为全球最优记录表值。用户直接搜这三个具体点数，可能找不到独立package，原因正是这些具体数字是本项目做的合法代入／组合，而不是所引论文的单独数值图清单。

在现有缓存证据下无需撤回35的非竞争判断：原始§2的33度33825已直接超过20580。65／70也有上述具体公开前提链，但必须保留其“组合推论”身份；若希望交付完整可下载边表，需另外实际生成或定位公开文件，本note不声称已经做了这件事。三张本地图的合法性与Lean状态不因public比较改变。

本次只保存这个来源追溯说明，无新计算、图、计数更改或Wiki／冻结包修改。

本note写入进程CPU：2.8321999999997294e-05秒；本轮无新数学数值实验。
