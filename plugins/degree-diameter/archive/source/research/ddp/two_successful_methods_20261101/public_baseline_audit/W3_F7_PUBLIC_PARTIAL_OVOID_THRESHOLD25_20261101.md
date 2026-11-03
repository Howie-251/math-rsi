# W(3,7)公开partial-ovoid门：已发表33点例阻断本地65／70及条件77目标

核查日2026-11-01 UTC。**当前实际读到的primary计算下界为33点，超过所问25点阈值。** 因而只使用已核公开opposite-GQ源、spread和Delorme一般复制，就可推出65度161650、70度169900、77度181450。旧比较160750／164500／169750须修订；本地161150／166650仍合法，但已被这套公开方法组合推论超过。条件H132／175692不再有公开竞争优势。

## 决定性原始出处

Miroslava Cimráková、Veerle Fack，*Clique Algorithms for Finding Substructures in Generalized Quadrangles*，JCMCC **63** (2007), 129–143。实际读到[出版社论文页](https://combinatorialpress.com/jcmcc-articles/volume-063/clique-algorithms-for-finding-substructures-in-generalized-quadrangles/)及[原始扫描PDF](https://combinatorialpress.com/article/jcmcc/Volume%20063/vol-063-paper%2012.pdf)。出版社页标2007-11-30；首页印刷页码为129–143，UGent索引的129–144不用于本报告定位。

印刷**p140、§4.3、Table5**（PDF第12页）W(7)一行实际为：

| GQ | (s,t) | collinearity图点数 | st+1 | 理论上界列 | 程序得到的最大partial-ovoid大小 | 不等价对象数 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| W(7) | (7,7) | 400 | 50 | 43 | **33** | **1** |

本次直接看扫描页，未用OCR猜列。[本地p140页图](w3_f7_threshold25_sources/jcmcc-page12-0-FXX1.png)保留该表。§4.3及表题说明这是作者穷尽算法得到的最大对象和分类；我们在本公开比较中只需其**实际已找到33点对象的计算下界**，无需把作者最大值报告重新跑一遍，更没有把理论上界43当构造。未取得作者33点的独立坐标列表；未复跑其搜索。

几何对象也已核清：印刷**p131、§1**明确把W(q)定义为PG(3,q)所有点及symplectic polarity的全迷向线，即这里的W(3,q)。[本地p131页图](w3_f7_threshold25_sources/jcmcc-page3-0-FXX1.png)与[PDF](https://combinatorialpress.com/article/jcmcc/Volume%20063/vol-063-paper%2012.pdf)相同。故该W(7)行正是所需对象，不是Q(4,7)点ovoids的误代。

## 从已发表33点下界得到的比较修订

继承已实际核定的公开公式和一般复制接口，详见[原70度适用性](DEGREE70_MULTIPLICITY_TARGET_GATE_20261101.md)与[旧77报告](DEGREE77_R7_F11_TARGET_GATE_20261101.md)中的原始Delorme§7／§8(a)来源。将partial-ovoid存在性参数由15换为33，仍用公开160000点／64度opposite-GQ(7,7)和50条spread，不用本项目160050源或O22：

```text
O size = 33, R size = 50, |O×R| = 1650.
N(Delta,3) >= 160000 + (Delta-64)*1650.
```

这一步是本次从已发表前提组合出来的推论，**不是声称2007论文列出了这些diameter-3图数值或独立公开边表**。原中心集合诱导matching，重复复制包含相应新新边；仍须使用一般§7规则，不能改成独立中心／距离≥3／本项目0newnew特例。

| degree,D | 此前使用15的公开保证 | 本次33导出的公开保证 | 本地或条件目标 | 目标减新保证 | 结论 |
| --- | ---: | ---: | ---: | ---: | --- |
| 65,3 | 160750 | **161650** | 已接受161150 | −500 | 图合法，当前比较已非改善 |
| 70,3 | 164500 | **169900** | 已接受166650 | −3250 | 图合法，当前比较已非改善 |
| 77,3 | 169750 | **181450** | 条件175692 | −5758 | H132目标无竞争优势；未产完整图 |

F11³=1331。单纯点数门现在要求H≥137（136给181016，137给182347）；若controller必须7正则，则H须偶，故H≥138。原三base／even-m要求H∈6Z，最小H138/m46；当前四base／3|m要求H∈12Z，最小H144/m36。这些只是条件规模门，**不授权相应搜索或证明controller存在**。

## 为什么Ceria2022的15没有回答这个小参数问题

实际阅读[Ceria–De Beule–Pavese–Smaldore，arXiv:2203.04553，§1、Table1及§3.1](https://arxiv.org/html/2203.04553#S1)。其奇数非平方域条目给Tallini的通用构造2q+1及上界q²−q+1，代7为15与43；该表不是q7计算最大值表。其新增构造要求q为奇平方且3不整除q，不能代入7。故继承15可给保守下界，却不足以维持本项目旧公开比较。此次已用明确primary小q表将缺口落实为33，不能继续只写“更大partial ovoid未穷尽”。

另实际读了[De Beule等EJC2008原文](https://biblio.ugent.be/publication/434883/file/481181.pdf)的对偶说明及相关上下界，随后沿原小q计算作者文献追到上述2007表。已核[Coolsaet–De Beule–Siciliano，arXiv:1201.5967，§3](https://arxiv.org/html/1201.5967v3#S3)中Q(4,7)的48点例对偶成W(3,7)的partial **spread**；它不能当本任务的W partial **ovoid**。相反，W partial ovoid对偶成Q partial spread。q7不是偶数自对偶情形。

## 实际动作与边界

本轮只一次3条primary-domain查询，之后打开明确文献、引用和出版社PDF；没有第二批查询。部分旧作者PDF链接404、Euclid服务页/旧2007全文访问不可用，最终出版社JCMCC全文可读，决定性p131/p139/p140均已实际检查。检索词和原始数值在同名JSON。

本地仅下载、提取扫描页与少量整数运算；没有几何/最大团搜索、生成controller或完整图、BFS、Lean、solver或新外审。未安装工具、未计算哈希。图合法计数不由此改变；root负责更新公开支配分类与当前恢复入口。旧冻结专家包保持字节不动，需另行显式勘误而非悄改历史快照。

33是本轮已读primary给出的更强、且该文报告为穷尽最大值的计算结果；不把本轮阅读冒作独立复核该穷尽证明，也不认证全球图最优或优先权。本次足以**明确阻断三个目标的旧竞争主张**。
