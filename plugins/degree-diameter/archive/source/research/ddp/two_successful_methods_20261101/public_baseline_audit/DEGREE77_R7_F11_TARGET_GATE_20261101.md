<!-- PUBLIC_W3F7_33_SUPERSEDES_TALLINI15_20261101 -->
> **当前公开比较已更正（2026-11-01）**：[原始33点证据与修订](W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md)实际读到Cimráková–Fack2007 p140 Table5的W(7)33点，公开一般复制保证65:161650／70:169900／77:181450。本地161150／166650分别少500／3250，条件175692少5758；图合法性与具体Lean/A/B/C不变。下文15点基线和正优势是保留历史，已被此处覆盖；不是独立公开数值边表／全球维护表。

# Degree77 / D3：r7–F11唯一公开竞争门

核查日2026-11-01 UTC。本任务先读已保存Delorme／PolarStar原文、已核q7与duality-product比较证据，再完成唯一一次四条primary-source查询；不重验任何旧图，不选定新controller。

**当前best-located可核公开方法保证为N(77,3)≥169750。** 对F11³纤维大小1331，严格超过该保证需要控制器 **H≥128**；如另要求三base且deck阶m为偶数，H=3m须为6的倍数，门槛为 **H≥132、m≥44**。这不是控制器存在或局部chart足够的断言。H132仅给条件阶数175692，较该保证多5942；未生成或验收图。

## 169750的公开来源与适用范围

1. [Isham–Lakhotia–Monroe–Petrini，arXiv:2608.27253v2 §3.4.2](https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2)重述Delorme的opposite-GQ公式：order=(s+1)(t+1)(1+st)²，degree=(s+1)(t+1)。q7、s=t=7给经典160000点／max64／D3源；3200个incident flags去自环后度63，其余度64。
2. [Ceria–De Beule–Pavese–Smaldore，2022 §1、Table1](https://arxiv.org/html/2203.04553#S1)明确报告Tallini对奇q的2q+1点partial-ovoid构造，q7因此给15点O。该论文自己的odd-square新构造不能代入7；Tallini原始坐标仍未取得，未冒称已读原构造全文。
3. [Delorme，EJC6(1985),291–302，§8(a)](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf)给同一symplecticGQ的q²+1条spread，q7为50条R。取A=O×R，|A|=750，使用该文**一般§7诱导子图复制**，重复13次得到

```text
n = 160000 + (77−64)·(15·50) = 169750,
maxdegree ≤ 64+13 = 77,     D=3.
```

这里继承[70度已核的同一public规则适用性](DEGREE70_MULTIPLICITY_TARGET_GATE_20261101.md)，只将6份改成13份，不使用本项目未公开160050源或O22。A外顶点至多有一个A邻点，A内诱导105K2＋540isolates。单边／孤点分量均有外邻点给§7的距离和≤3条件；以原A作A0、其余层为空，旧副本对原A仍至多一个邻点，条件可逐步保持。

复制包含matching对应边；每对原matching端点的14份版本形成K14,14。此时每份仍只有原外邻居再加14个partner版本，degree至多77。孤立center副本和A外点也不超过cap。不能套“center互距≥3”的独立集特例，不能把此公开matching recipe混成本项目0newnew规则。阶数169750超过degree77/radius2界5930，故在已知D≤3下实际恰D3。

169750是公开方法、公开存在性前提的直接组合推论；未定位到单独发表的169750数字图或边表。它作为当前竞争门，不是全球最大或优先权认证。

## 其他已读一手族的全部合法标量比较

[PolarStar作者原文](https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf) Table2、Proposition2／Corollary1和§7.1允许host q为prime power。对每个q+1+d′≤77，IQ要求d′≡0或3(mod4)、n=(q²+q+1)(2d′+2)；Paley要求d′偶且2d′+1为prime power、n=(q²+q+1)(2d′+1)。本次穷尽这些**公式的合法小整数代入**，没有图或参数拓扑搜索：

| 已读机制 | 相关最大代入 | 可核阶数 |
| --- | --- | ---: |
| PolarStar IQ | q53,d′23,degree77 | 137424 |
| PolarStar Paley | q49,d′26,degree76≤77 | 129903 |
| opposite-GQ直接公式 | q7,(s,t)=(7,7),degree64 | 160000 |
| Payne opposite-GQ直接公式 | q7,(6,8),degree63 | 151263 |
| 其他已知GQ(s,t)直接族 | (q,q²)、(q²,q³)及dual均计入 | 小于160000 |
| 2026 GQ×GQ polarity产品＋绝对点复制 | q1×q32,degree66/order135300，再添11×2050 | 157850 |
| Delorme §6 q16 duality/std12＋matching复制 | source52428/51，1028centers添26份 | 79156 |
| Delorme q32 folded-GQ＋绝对点复制 | source33825/33，1025centers添44份 | 78925 |

q7复制为该已读范围的最强保证169750。标准12控制器替换及duality/spread/general matching复制的依据继承[已完成的公开补强](DEGREE54_55_DUALITY_PRODUCT_REPLICATION_20261101.md)，不重新核144三词；其中D1绘图仍未识别。2026产品继承§7.4／§7.7的实际极性参数条件，未把任意q7几何冒作有极性；mixed GQ×projective-triangle合法标量也包含在JSON，未超过上述产品值。

已知opposite-GQ参数族来自§3.4.2明列的(q,q)、(q−1,q+1)、(q,q²)、(q²,q³)，q为prime power；超过cap的实例不计。Payne(6,8)只使用其已核直接公式，没有假设其存在本次未核的full-ovoid／spread packing来制造更大复制值。任意诱导复制的优化仍是公开核查缺口，未声称全部可能增强已穷尽。

## 控制器阶数门槛与执行决策

```text
1331·127 = 169037 < 169750,
1331·128 = 170368 > 169750.

三base + even m: H=3m∈6Z，因此最小门槛H132 (m44),
1331·132 = 175692，条件margin5942。
```

7正则简单controller本来要求H偶数，H128满足该计数要求；这不提供所需A³覆盖、特殊2factor或固定inverseport兼容。r7/F11局部PASS不能直接视作完整图。旧r6固定六port的m容量排除不能移植到新七port拓扑。本门仅把可信竞争尺度交给root，未自行派controller、degree列表或F11大图。

## 查询、成本和保留边界

本次唯一四查询batch为：degree77／diameter3；Payne-derived／ovoids；W(3,7) partial-ovoid；degree77／Delorme，限定primary作者/机构与arXiv域。没有定位到该77参数更强的明确一手数值，主要召回仍是[Comellas官方≤16维护表](https://web.mat.upc.edu/francesc.comellas/delta-d/taula_delta_d.html)、作者索引和不相关网络论文；无命中不是不存在或穷尽性证明。查询后只打开已经明确的Ceria和2026 primary以核对适用条件，未增加查询batch。

完整合法PolarStar代入、GQ与复制标量在JSON中；可复算源为`DEGREE77_R7_F11_TARGET_GATE_20261101_scalar_check.py`。实际标量CPU为0.020526023秒，低于5CPU，单个可执行批次终态；0大图生成／读取、BFS、Lean、solver或额外外审。源码撰写、文献阅读和网络时延不冒作该本地标量CPU。

仍未认证全球最高或优先权：没有完整77度维护表，Delorme JGT1985全文缺口仍保留；更大published W(3,7) partial-ovoid／其他诱导集合、Payne源及任意复制组合、未召回公开图未穷尽。已明确排除把本地160050/O22与新U10结果用作“公开来源”。本门不计任何新完整图或Goal完成。
