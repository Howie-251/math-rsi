# 766严格容量：证明与计算证据范围

2026-11-05。新一般定理及p5应用由Root、`global_cover`、`overlap`三路逐项解析自查，文档Sol忠实转写；仍为 **same-session、unreviewed/unaccepted**。没有外部评审或接受升级。[PROOF.md](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n766-strict-capacity-20261105/PROOF.md>) 的完整工作证明给C49，仅直接更新40/49/75/76。

## 1. 主证明的准确依赖

| 接口 | 已写出的证明 | 保证边界 |
|---|---|---|
| 实际路径替末 | 同端R_p/B4、B_p/R4的weak矛盾迫两个桥色，保留原路径内部点替换末点 | p≥4，替末点须在原固定子域；容量b不与实际端点b0混淆 |
| 完整双色端点交替环 | 最小源与最短环压缩；只删除抽象端点，不删除母体物理点 | 余路径可经过被删端点，不增加避让要求；不要求L全在U之前 |
| 全配置安全增广 | 规范短帽覆盖已有交叠，或“全部单点增广都失败”的完整实际端点图处处有出边，成环矛盾，故至少一个增广全路径安全 | 对任意X兑现覆盖交叠≥1，再用短帽容量得到2b−1；四原子/Hall匹配只在附录保留 |
| p5数值 | b25作为原完整signotope756及换色范围的有效容量输入，得到C≤49 | 原b25人工接受及same-family/provisional保证不升级为新C49接受 |
| 无through的767型桥 | S无B_p、I空迫S无R_(p+1)，余域balanced，得到n≤b+C；两位作者与Root已核对闭合 | p5整个I空类≤74，任何75候选须I非空；不是全局Q74 |

本证明无需Through14、Joint17、Closure、SAT/UNSAT结果或经典15/20核分类。下面的计算只提供独立于主定理的实际反例诊断，不承担C49推导。

## 2. 实际双through反例：有SAT见证，不依赖UNSAT

权威Linux目录为 `/data/ktqiu_hdd/math_agent/tmp/n7_dual_through_probe_20261105`，使用外部AE Kissat受控进程。实际两次solver调用均未超时，每次约2.07秒，无proof输出、无checker、无外审或自动重试。[README](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_dual_through_probe_20261105/README.md>)。

| case | 实际状态 | 可以主张的范围 |
|---|---|---|
| A：p4、n16 | exit20，raw UNSAT，2.0698486629407853秒，预算120秒 | 固定CNF未有成功checker，不作不存在性证明或一般定理 |
| B：p5、n24 | exit10，SAT，2.0697280468884856秒，预算600秒；实际完整染色/路径语义核查通过 | 下述完整有限反例成立；不是新容量上界 |
| C：固定端点交替四边 | Root给解析排除后，在launch前取消 | 没有生成CNF或调用solver，不作一次运行计数 |

B的零基实际角色与内部见证为

\[
\begin{aligned}
T_R&=\{4,5,6,7,8,13,16,18,19\},\\
T_B&=\{10,11,12,14,15\},\\
R_5&=(4,5,6,7,8)\subseteq T_R,\\
B_5&=(10,11,12,14,15)\subseteq T_B.
\end{aligned}
\]

全部2024三元组完整给定，10626个packet合法；实际最长红/蓝路径均5，同实际首末点的最大长度和8，因此是实际balanced766。全部路径按全三元组单色子集独立枚举，并与连续三元组扫描比较；长度2/3/4/5/6的红路径数为276/845/713/125/0，蓝路径数为276/1179/1730/760/0。实际源、末、through角色从这些完整路径重算，再与全部角色literal核对。全部323856 DIMACS子句与solver完整赋值相符，辅助值与由颜色规范求值得到的exact gate值相符。

因此，“766中两色through域不可能分别包含本色p路径”的普适猜想被实际24点例击穿。它没有反驳本稿C49：24点小于49，主证明也不使用该反例。此前提议的through主攻不能继续按该普适版本推进。

原始入口：[B.result.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_dual_through_probe_20261105/B.result.json>) · [B.semantic.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_dual_through_probe_20261105/B.semantic.json>) · [B.paths.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_dual_through_probe_20261105/B.paths.json>) · [A.result.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_dual_through_probe_20261105/A.result.json>) · [C_CANCELLED.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_dual_through_probe_20261105/C_CANCELLED.json>)。

源与输入绑定：[PREPARED.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_dual_through_probe_20261105/PREPARED.json>)、[FILE_MANIFEST.json](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_dual_through_probe_20261105/FILE_MANIFEST.json>)。其中源码SHA256为 `cab419d63d219a354b328a29a581a7ae77013209ef0e2b329a8dd36e19fb281d`；B语义见证为 `36ce2785b6787d2f5151a4ff91dfdb35c7ad648438540ca6b66cb1287b32eaad`；全部实际路径为 `9ca65cc61024e3ebf48f1b249e1bef0937e17615883aab58469fc44267f2aa7f`。原数据与生产C_r builder、campaign、封存证明和作业保持。

## 3. 当前验收与开放义务

C49是本轮完整工作证明的新数值结果，尚无独立外审或人工接受；原b25接受、assurance和proof绑定保持。当前全模型工作链为40/49/75/76，另已闭合整个I空767类≤74。一般75临界层到balanced50或净收益的桥、普适Q≤C+b、Q74/F75及75739仍未证明。

文档执行者只读取原证据、写新三份文档并检查文字、链接与公式；没有科研重跑、review/status调用、旧报告修改、task metadata/wiki/Goal变更。恢复动作见 [NEXT_SESSION.md](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n766-strict-capacity-20261105/NEXT_SESSION.md>)。

## 附录：p≥7双色through两链的解析反例族

此为`critical_hall`作者与Root逐packet、逐高度核对的解析诊断，无单独计算回执，不参与49主证明。取p≥7，令H_p=L_(p−1)<A_p<R_(p−1)，各块内部全红；不含A的跨L/R三元组全蓝；涉及A与外块时，当且仅当中间点属于A为蓝。即LLA红、LAA蓝、AAR蓝、ARR红、LAR蓝、LLR蓝、LRR蓝。

全部四点块型归入下表，故packet至多一次变色：

| 块型 | packet |
|---|---|
| LLLL、AAAA、RRRR、LLLA、ARRR | RRRR |
| LLLR、AAAR、LLAR | RBBB |
| LLRR、LAAR | BBBB |
| LRRR、LAAA、LARR | BBBR |
| LLAA | RRBB |
| AARR | BBRR |

H_p红高p、蓝高4；A全体点各由L+a与a+R获得入/出R_p，且A本身为红p链。L/A或A/R端点的两色长和至多p+3，A/A至多p+2，L/R至多6，其余更小，所以无weak(p+2)。

取Y=H_p，Z为H_p换色副本，Y<Z；跨块YYZ染蓝、YZZ染红。本附录为此混色join，不能与全红产品规则混用。新packet分别为(c_Y,B,B,B)、(B,B,R,R)、(R,R,R,c_Z)，均合法。跨块红路径只能含一个Y点、其Z段红高至多4，故长至多5；蓝色对偶。两色全局高度均p，跨块同端长和至多10<p+4，块内沿用H_p及其换色预算，故所得6p−4点母体禁R_(p+1)、B_(p+1)、weak(p+2)，同时保留红/蓝through域中的本色p链。

此族不作为p5/6反例：取Y的蓝4源u和Z的红4末v，两条跨块拼接分别给同端B5(u,v)、R5(u,v)，长度和10，在p5或p6已触发weak禁止。p5的实际24点反例由本文件§2的独立SAT见证与语义核查提供，两者范围分开。

## 附录：30点neutral等号的解析阻断

Root与`overlap`核对如下解析族，无机器回执，不用于49主证明。取S为全蓝5点，K为任意经典满20点、无R5/B5的完整核（两色高均4），E为全红5点，S<K<E。先作H1=S⊖K，再作H=H1⊖E；本段每次join的跨LLR全红、LRR全蓝。新packet为(c_L,R,R,R)、(R,R,B,B)、(B,B,B,c_R)，均合法。

H1红高4、蓝高5，从S出发的红路径至多3。最终H两色高均5。同端跨S→K的红/蓝长上界为3/5，S→E为4/3，K→E为5/3，内部预算也不超过8，所以H是实际30点766。

每个s∈S与K内一条B4连接为B5，而K自身无B5、最终跨向E的蓝路径至多3，故全部Src_(B5)(H)恰为S。对偶地，K内R4后接任意e∈E为R5，H1无R5，所以全部End_(R5)(H)恰为E。因此

\[
Z=H\setminus\bigl(\operatorname{End}_{R_5}(H)
\cup\operatorname{Src}_{B_5}(H)\bigr)=K,
\qquad |H|+|Z|=30+20=50=2b.
\]

这否定通用strict-neutral式n+|Z|≤2b−1，不否定C49。它也不满足M0额外owner身份所需的直接运输：K内确有ambient B5末点，而最早owner没有ambient B5入路径，不能将不同实际角色标签直接等同。经典20核只为此诊断构造使用，不进入49主证明。
