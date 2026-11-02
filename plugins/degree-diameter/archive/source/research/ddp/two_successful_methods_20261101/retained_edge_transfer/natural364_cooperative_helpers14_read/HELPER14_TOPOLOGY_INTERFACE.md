# 自然364 / 14-helper单环：两个安全的拓扑必要门

状态：**支持，未枚拓扑或分配ports；尚不宣称整个k14为NO。** 只读了本目录READ_GATE及旧 `d4_D5_polarity_extensions/MULTI_VERTEX_PORT_BARRIER.md`、`helper13_tree_probe/REPORT.md` 与两个capacity summaries。旧R2/R3/R4、source D5及uniform good结论均继承，不重算。

## 固定范围与剩余H结构

源是自然364/714、28个degree3 ports、其余4度，非公开364/728全4正则图。保留所有源边，不加old-old边，max4。端口两两旧距5，R2(p)为28个不交13点cell并分割源；每port只能接一个helper。

旧论证迫28ports全用、H连通。k14时degree总账给 `13≤m(H)≤14`；tree已由本目录先前纸面结论关闭。故唯一剩余为simple connected unicyclic H，m=14，degree≤4，并且

`a_h=|P_h|=4−d_H(h)`，`Σa_h=28`。

全部P_h互不交、分割28ports。owner集合完全由拓扑决定：`O={h:d_H(h)≤3}`。H叶子必有恰3ports；degree4点不拥有port，不能强行把它当owner。

## 门一：所有helper到所有owner须≤4

任意helper h要在5步内到owner w的某个port q。若最后进入旧源的port不是q，旧后缀至少5步，加进入边已超5。不同ports之间的old excursion再回H至少 `1+5+1=7`；同port回H只能回同owner，不提供捷径。因此必要且对这个port目标精确的是

`d_H(h,w)+1≤5`。

应筛 **每个h∈V(H)、每个w∈O** 的距离≤4，不只是owner-owner，也不据此误写整个H直径≤4。

## 门二：parent度≥3的叶子到所有owner须≤3

取leaf ℓ，其三个ports为T；parent b若degree4则无port，若degree3则恰有一个port p。假设某owner w满足 `d_H(ℓ,w)=4`，取q∈P_w，令 `I_q=R2(q)\{q}`。

ℓ到旧点的≤5路线不可能先经不同old ports穿越又回H（至少7步），所以可按最后helper exit分类：

- ℓ自身的exits贡献R4(T)；parent只贡献R3(p)，或空；
- H-distance2的exit最多贡献其port的R2；distance3最多R1；它们的ports不是q，均在其它不交cells中，不能填I_q；
- distance4最多贡献port本身，包括w的q，但不包含I_q任何点；更远exit无预算。

所以若ℓ覆盖全部I_q，必须 `I_q⊆R4(T)`，或 `I_q⊆R4(T)∪R3(p)`。q不在T或parent port中，由port唯一归属保证。旧完整3276 triples的good(T)与81900 triple/parent pairs的good(T,p)均为空，给出矛盾。没有遗漏shared-old-pin回穿，因为每port只有一个owner。

结合门一，安全拓扑条件为：若leaf ℓ的parent degree≥3，则 `max_(w∈O)d_H(ℓ,w)≤3`。**不能**把该强门用于parent degree2；它有两个ports，旧单parent-port缓存没有排其R3两球合作。

## Cycle / attachment范围不会漏解

H的唯一cycle长c≥3。任一挂树leaf w在cycleroot r外深d，取cycle上离r最远的vertex h；单环没有第二条树间捷径，故

`d_H(h,w)=d+floor(c/2)≤4`。

若c≥10，任何owner到某cyclevertex已≥5，不可能；若c=8或9，不容深度≥1的leaf，而n14>c必须有挂树，仍不可能。因此只需c=3..7，挂树最大深度分别≤3、2、2、1、1。非leaf挂树点在某leaf祖先路上，也满足这个深度上界。

完整抽象域可取这些cycles及全部满足n14/maxdegree4/深度界的挂树；不能额外假设对称、均衡branch或特定owner位置。重复拓扑只影响效率，不能以未经证明的等价关系删形状。

## 数值返回后能说什么

这两个门均不依赖port assignment，因为旧good结论对所有实际T/p均统一成立。如果完整抽象域0survivors，可关闭固定自然源、保边/无old-old、k14这一整个类，无需再分配ports或BFS。若有survivor，只表示两个必要门未排；仍需helper-old cell覆盖、helper-helper D5及实际assignment，不能宣称可行图。

本paper未枚拓扑、port assignments或新数值；未改旧结果/源缓存、root/Wiki/页面，新增图/参数/Lean均0。root独占唯一拓扑枚举，本文不启动任何后续。
