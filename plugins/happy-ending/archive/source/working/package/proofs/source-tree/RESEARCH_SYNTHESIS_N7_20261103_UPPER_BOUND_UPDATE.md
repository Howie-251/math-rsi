# N7 研究综述更新：统一闭合与人口工作上界

2026-11-03。完整低前驱补偿证明关闭了 \(n=3b+2\) 的最后人口临界层。以现行容量输入计，767、777 的无条件人口工作上界由 \(77,78\) 降至 \(76,77\)。新增工作证明仍为 **unreviewed / unaccepted**。本次推导、转写和逐项缺口核对均属同会话工作。早期综述的 \(77,78\) 与各阶段的残余目录按原样保留，作为当时的工作记录。[早期研究综述](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_SYNTHESIS_N7_20261103.md>)

## 本轮证明链

| 阶段 | 参数结果与覆盖范围 |
| --- | --- |
| 共同中间匹配 | 用实际首末点匹配将加权工作界降至 \(n+w\le3b+2\)。因此 \(n=3b+2\) 的反例必须满足 \(w=0\)。[加权界稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_MIDDLE_COMPATIBILITY_AND_WEIGHTED_BOUND_20261103.md>) |
| 双 clean 增广 | 同时扩张中间域与右修补核，关闭临界层的全部双 clean 配置，单独给该子类 \(n\le3b+1\)。[双 clean 排除稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_AUGMENTED_MIDDLE_CLEAN_CLASS_EXCLUSION_20261103.md>) |
| 有锁分阶段排除 | 关闭大缺额、带普通供给的相应有锁侧及一 clean 一有锁的混合类，留下双有锁、严格交错的纯 owner 类。[有锁临界类排除稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCKED_DEFECT_AND_ORDINARY_SUPPLY_CLASS_EXCLUSIONS_20261103.md>) |
| 完整低前驱补偿 | 在完整双向 M0 接口下统一排除 \(w=0,\ x<y\) 的整个人口临界层。既有 onefull 与非交错根序结果覆盖另外两条入口。由整数性得 \(Q\le3b+1\)，再经既有精确归约得 \(F=Q+1\le3b+2\)。[完整上界工作证明](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMPLETE_LOW_PREDECESSOR_COMPENSATION_AND_UPPER_BOUND_20261103.md>) |

原基底 \(W=S\setminus\Omega\) 同时限制实际末对的前驱与末根，因此落在左锁集 \(\Omega\) 的低末根未进入旧计数。统一证明改从 \(S\setminus A_H\) 收集全部普通低前驱，保留指向 \(\Omega\) 的实际低末对。将这 \(\tau\) 个前驱加入右修补核，原低帽及尾替换排除新增红六。左匹配因删除这些前驱至多损失 \(\tau\) 条边，右核增广使右匹配容量下界增加同一个 \(\tau\)。这两项在交会预算中精确抵消。

实际左扩域可以使用 \(A_H\) 中的 owner 作为末前驱。中间域取两个核的完整交集 \(D\sqcup A_H\sqcup B_H\)，首末容器分别按纤维的最早、最晚代表控制。两侧外供给沿同一份实际红五匹配运输，未覆盖端口统一扣除，至少得到一个交会。它给出同实际首末点的蓝四与红五，违反 weak7。该论证直接覆盖单代表和多 owner 纤维，也覆盖缺额 \(3\)。此前各类排除是本轮证明链的阶段成果，人口下降只计一次。

切分点 \(y\) 的处理决定最后一单位余量。左扩域允许使用不晚于 \(y\) 的左锁，只须避开右锁。右扩域则避开两侧锁，并可额外接入晚于 \(y\) 的实际右锁首对。若替代基底在 \(y\) 有末根，直接从左域删去 \(y\)。若保留 \(y\)，左匹配至多有一条以右 owner 为末前驱的边需要扣除，因为此类边只能终于 \(y\)。两种损失合计至多一，故交会余量仍为正。

统一闭合时仍须先用加权界将 \(n=3b+2\) 层压到 \(w=0\)，再分别对两侧实际换核消去 mixed 点。换核保持 \(D\)，缺额不增。在这个接口上，缺额为零由既有满侧排除处理，两个极端根相等或反序由既有非交错根序处理，剩余严格交错由完整低前驱补偿处理。这三步连起来才覆盖人口临界层。

## 参数账与下一步

沿用 \(A,C,Q,F\) 分别表示 757、766、767、777 的最大允许人口，\(a,b\) 是 747、756 的有效容量输入。现行参数工作链为

\[
A\le a+b-1,\qquad C\le2b,\qquad Q\le3b+1,\qquad F=Q+1\le3b+2 .
\]

代入 \(a=16,\ b=25\)，四项工作上界依次为 \(40,50,76,77\)。加权工作界仍为 \(n+w\le3b+2\)。\(Q\le C+b+1\) 和 \(Q\le C+b+2\) 仍待证明，\(C\le2b\) 只给 \(C\) 的上界，不能从 \(Q\le3b+1\) 反推这两个关系。几何运输本轮未重新审核。

下一步先对统一闭合及承重依赖做完整独立审计，重点覆盖 M0 归一化、普通点蓝五限制、外相邻对定位、实际中间匹配与既有精确归约。本轮工作限定在同会话核对。其后可探索补偿式能否推广到加权层，并检验临界边界根能否再节省一单位人口。
