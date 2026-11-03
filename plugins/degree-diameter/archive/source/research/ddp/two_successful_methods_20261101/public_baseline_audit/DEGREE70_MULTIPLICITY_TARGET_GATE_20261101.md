<!-- PUBLIC_W3F7_33_SUPERSEDES_TALLINI15_20261101 -->
> **当前公开比较已更正（2026-11-01）**：[原始33点证据与修订](W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md)实际读到Cimráková–Fack2007 p140 Table5的W(7)33点，公开一般复制保证65:161650／70:169900／77:181450。本地161150／166650分别少500／3250，条件175692少5758；图合法性与具体Lean/A/B/C不变。下文15点基线和正优势是保留历史，已被此处覆盖；不是独立公开数值边表／全球维护表。

# (70,3)：固定 multiplicity6 候选的公开来源门

核查日：2026-11-01 UTC。范围为一个参数 cap70/D3；复用本日已读 Delorme、PolarStar、2026产品论文、Ceria等原文及作者索引，新增一批4条窄检索。不重开 W(3,7) partial-ovoid22 的两批归属检索，没有图生成、边表读取、BFS、solver或Lean。

**本次定位到的最强公开来源保证为164500点、最大度70、恰D3。父任务拟议166650比它多2150点，未被本门定位的一手来源阻断。** 164500是经典构造、已报道存在性及公开复制定理的直接数学推论，没有定位到单独发表的该数值图或边表；全球纪录和首创均未认证。

## 164500 的来源与六次复制适用性

[2026产品论文 arXiv:2608.27253v2 §3.4.2](https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2)（v2日期2026-10-22）重述 Delorme opposite-GQ 公式：`n=(s+1)(t+1)(1+st)^2`，`Δ=(s+1)(t+1)`。s=t=7得到经典160000点、最大度64、D3源；去环后的flag点度63，其余点度64。它不是本项目补50点的160050源。

[Ceria–De Beule–Pavese–Smaldore，arXiv:2203.04553v1 §1及Table1](https://arxiv.org/html/2203.04553#S1)（2022-03-09）明确记录 Tallini 对奇q的 `2q+1` 点 partial ovoid 构造，因此 W(3,7) 中存在15点集O。该文的新 odd-square 条件不能代入7。Tallini原作是 Atti Accad.Peloritana66(1988),127–146(1989)，本门继承已读2022一手研究论文的明确记载，未取得Tallini原始坐标。

[Delorme, European J.Combinatorics6(1985),291–302，§8(a),p298](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf)给 W(3,q) 的 q²+1 条线spread，q7给50条R。在经典opposite源取 `S=O×R`，|S|=750。

原文 **§7 p297的一般诱导子图复制定理** 可用，不能仅以2026 §7.7所述“中心互距≥3”特例代替，因G[S]实际有 **105个K2及540个孤立点**。适用条件沿用已核65门：

- S外顶点至多有一个S邻点：其线至多含一个O点，其点恰落在一条R线上。
- S内每点至多一个不同的S邻点。15个O点落在15条不同spread线上，给105对交换中心；其余540个中心孤立。
- 每个分量满足原定理的D3条件。孤立点有S外邻点z，两次距离和为2；K2的两端u,v取u的S外邻点z，距离至多1和2。源最小度63、S内度≤1确保这样的z存在。

**可连续添六份S，保持每步最大度只升1。** 可直接反复应用公开的单步定理而无需猜测OCR中多重复制公式：始终以原始S作A0、A1为空。已有副本对原S至多一个邻点，所以每步条件(b)仍成立；原S诱导图及上述旧z均保持，条件(c)也保持。六步得到

\[
N(70,3)\ge160000+6\cdot750=\mathbf{164500},\qquad\Delta\le64+6=70.
\]

这项公开推论的复制包含S中K2的对应边；完成后每对K2两端的七份版本形成K7,7。因此该推论需要新副本之间的边；它没有证明父任务所提“0 new-new”的具体新图。K2端点原度64，复制后达到70；孤立中心及副本度不超过64，S外旧点加度≤6。旧源保留，直径仍至多3；阶数超过D2 Moore上界4901，故恰D3。

## 其它已读一手族在cap70的比较

| 族 | 相关合法代入 | 所得阶数 |
|---|---|---:|
| Delorme folded-GQ绝对点复制 | q32，degree33→70，1025绝对点各添37副本 | 71750 |
| opposite-GQ直接公式 | s=t=7，degree64 | 160000 |
| 2026 GQ×GQ极性产品及绝对点复制 | q1×q32，degree66/order135300；2050绝对点复制4次到70 | 143500 |
| PolarStar IQ | q49、d′20，degree70，2451·42 | 102942 |
| PolarStar Paley | q49、d′20，degree70，2451·41 | 100491 |
| Delorme §6 duality族 | q16，degree51 | 52428 |
| Cames van Batenburg–Korsky直接H₃,q | 最小q2已有2893695点，高于Moore(70,3)=338171 | 无cap70实例 |
| Suzuki-Cayley已读参数 | q32有31744点；下个q128有2080768点，高于Moore70D3 | 不改变此门 |

PolarStar使用[SPAA2024作者原文](https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf) Table2、Proposition2/Corollary1及§7.1，对全部合法prime-power q与supernode d′、`q+1+d′≤70`作标量公式代入。产品来自[2026论文§7.4与§7.7](https://arxiv.org/html/2608.27253v2#S7.SS4)。渐近族来源及Moore排除继承[arXiv:2608.03965v1 Proposition3.1](https://arxiv.org/html/2608.03965v1#S3)与[Suzuki作者预印本Theorem1](https://arxiv.org/html/1709.09760v1)。本门没有重生成任何公开图。

本次唯一4-query批未定位≥166650的cap70/D3一手保证；已读新作者索引也没有提供该参数更强实例。检索召回以无关数值结果居多，不能视为穷尽性证据，未使用Wikipedia或聚合页面建立数值结论。

## 与父任务的具体候选分账

父任务给定候选：以已接受160050/64正则源为不可变基图，O22×50spread的1100个base centers各添6个新点，每个只连接其原源64邻点；6600新点、0 new-new，条件目标 `n=166650,m=5544000,Δ≤70,D3`。本门没有复验这些有限前提或验收该新图，不能据此记已完成图、Lean或全球纪录。

比较差额是 `166650−164500=2150=50+6·(1100−750)`。本地O22仍不是已定位的外部已发表保证；归属门此前两批已经终态，本门不重搜。若将来取得可用于相同经典源的公开23点partial ovoid，六重复制将给166900并阻断当前目标；本门没有定位到该前提。

继承Delorme JGT9(1985),325–334全文缺口，没有认证原文不存在更强增强规则。任意诱导子图、多重复制组合与全部其它几何源未穷尽，完整当前70度维护表未取得。H(4,4)无full ovoid已由Ceria §1确认，不能再以假设的33点full ovoid提出既有54度数值反例；一般partial/induced-duplication缺口仍保留。

**终态：PUBLIC_GATE_NOT_BLOCKED_BY_LOCATED_SOURCES_INCOMPLETE。** best-located164500、条件目标166650、差2150；`global_record_confirmed=false`，`priority_confirmed=false`。本子任务在此返回，不扩展66..80参数或文献批次。
