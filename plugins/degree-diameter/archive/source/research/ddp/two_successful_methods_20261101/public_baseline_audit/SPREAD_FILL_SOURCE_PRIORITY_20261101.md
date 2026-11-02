# Opposite-GQ同度数spread-fill：本轮未取得已发表同规则证据，优先权仍未解决

2026-11-01 UTC。**本次已读材料不足以把P33十五图的公开比较再提高50点，也不足以认证该50点填补为新构造。** 已确认公开的是opposite-GQ源、spread存在性及一般复制引理；尚未定位到同度数加入st+1个新点、给出本项目相同fill pins与D3覆盖的已发表规则或已建立直接推论。关键原始JGT1985正文仍未取得，而非已读后排除。

目标规则为：在degree Δ=(s+1)(t+1)、order Δ(st+1)²的无自环opposite-GQ源上，保留旧边，沿spread加入st+1个fill点，degree仍≤Δ、diameter≤3，阶变为

```text
Δ(st+1)^2+(st+1).
```

本项目已实际验证的(s,t)=(7,7)实例是160000→160050／degree64。本报告仅查归属，不重验这张图，也不声称该公式对所有有GQ参数自动成立。

## 已实际阅读的原文，以及各自能支持什么

| 材料 | 实际读到的内容 | 对目标fill规则的归类 |
| --- | --- | --- |
| [Delorme，EJC6(1985)291–302，§7，p296–298](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf) | 诱导子图复制、邻接/分层条件及升degree的结论 | **only general lemma**；没有opposite-GQ同度数fill pins |
| 同文§8(a)，p298–299 | symplectic GQ的q²+1线spread；在其incidence图上应用复制，升degree1、加q²+q+4点 | **explicit spread ingredient**；是D4 incidence图的增广，非所问D3 opposite源同度数加q²+1 |
| 同文§8(c)，p299 | 极性quotient的绝对点复制；q8给585/9→650/10等 | **different explicit recipe**；degree增加，非81度源加65点 |
| 同文§8(e)，p300 | 特征2的projective-plane quotient单点复制可保持degree | **different explicit recipe**；D2及另一邻域，未给GQ目标pins与覆盖 |
| [Isham–Lakhotia–Monroe–Petrini，arXiv:2608.27253v2，§3.4.2](https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2) | opposite-product polarity quotient，删loops，阶Δ(st+1)²及degreeΔ；列出已知GQ参数 | **explicit unfilled source**；该段没有新增fill点规则 |

Delorme全文本地存于[已保存原文文本](delorme1985_primary_text.txt)，本次实际读§7、§8全部子节，并检查后续§9以免漏掉同度数插点：§9是hexagon incidence边细分、把diameter升至7，不是目标D3规则。矩阵图片处没有用缺失OCR代替结论；决定性degree/order变化亦由原始PDF正文核读。

2026原文另读§2.3的loops约定：比较时删除self-loops，保持原顶点集；没有把loop替换成新顶点。其缓存全文中没有spread/augmentation条目，本报告用这个检索定位段落，不把关键词未命中当不存在证明。[本地HTML](arxiv_2608_27253v2.html)及[文本](arxiv_2608_27253v2.txt)保留实际内容。

## 为什么一般lemma＋spread不能直接登记为相同构造已经发表

§7的直接操作是复制已有诱导顶点并继承其邻接。本项目fill点用的是spread线所辖incident-flag pins，随后还须证明它们只消耗源的余度，以及所有当前点对的短路线覆盖；它不是仅把某个原opposite顶点的整个N原样复制。§8(a)给spread，却把它用于原incidence图的另一增广。将这些材料合在一起尚缺**目标opposite图上的具体pin集合、负载及覆盖论证**。

因此，本轮没有建立“这条fill规则是上述已发表lemma的无需额外结构判断的直接推论”。另一方面，不能从这项区分反推该规则新颖：同一pin规则可能位于尚未取得的原始论文或另一明确出处。本项目自己的证明、计算和Lean证明合法性，不证明最早归属。

## 最关键的精确文献缺口

2026 §3.4.2的opposite-source实际引文是 **C. Delorme, *Large bipartite graphs with given degree and diameter*, J. Graph Theory9(3)(1985),325–334，DOI [10.1002/jgt.3190090304](https://doi.org/10.1002/jgt.3190090304)**，并非上表已读的EJC论文。

本次正常打开其官方PDF URL，实际重定向到[摘要及参考文献页](https://onlinelibrary.wiley.com/doi/abs/10.1002/jgt.3190090304)；官方ePDF入口不可取得。Comellas原source描述页所给链接也只指回同一DOI。因此只确认题名、页码和原source引用，**没有冒称已读JGT正文，更不能断言正文没有fill增强**。这个十页正文中opposite-product的构造段／后续增强段，是专家下一步最值得直接查的具体缺口。

## 一次有界精确查询的结果

只有一个3-query batch，限定primary研究/出版社及已用官方机构来源：

1. `"160050" "graph" diameter`
2. `"327744" OR "342290" "graph"`
3. `Delorme "Large bipartite graphs with given degree and diameter" spread vertices`

未召回明确的目标数值图、同一fill recipe或上述order增强定理。召回JGT原始元数据后，后续只沿官方论文/明确引文打开页面，没有第二批搜索。327744对应degree80 GQ(7,9)的327680+64；342290对应degree81 GQ(8,8)的342225+65，仅用作检索哨兵，不是本次确认的公开构造数值。

未命中不作新纪录证据；没有改任何当前公开数字或root计数。

## 若后续确认，十五图比较如何改变

若取得明确公开的**同一filled160050源规则**，并确认其连接可接现有P33×50的一般复制接口，则当前各degree65..79的公开组合保证应由160000+1650k提高至 **160050+1650k**，与本地十五端点相等。各+50优势将归零；所有图、具体Lean和独验仍合法。只找到一般扩张引理、单独spread存在性或另一source，尚不满足这个条件。

四类状态在同名JSON中分别记账：explicit unfilled source=已找到；published exact fill recipe=未找到；published fill direct corollary=本轮未建立；only general lemma=已找到；fill priority=仍未知。不存在“因为未找到，所以原创”的结论。

给专家的具体问题：**JGT1985第325–334页或其直接后续文献，是否已经定义把每条spread对应的incident-flag类接到一个新点，并在opposite-GQ上保持degree与D3？若有，请给定理/页码、pins及覆盖论证所在位置；如只是§7的一般复制操作，请指出到该fill规则还需的结构步骤。**

本地只有材料读取、定点文本检索及整数哨兵计算，CPU见同名JSON。0图/field/BFS/Lean/solver/外审或Wiki helper；不改冻结包/rootcounts，专家十五图文档仍应保持draft并注明这一优先权边界。本报告不影响合法图留档，也不自行延伸研究。
