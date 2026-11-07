# N(7,r,s)研究综合：最新工作界、局部最优风险与下一结构方向

日期：2026-11-03。最新可得承重原稿为2026-11-02。**当前结构工作链为757/766/767/777：40/50/77/78；建议先整理核对现有证明链，再以统一缺额稳定性争取76/77，保留完整路径重分划作为竞争方向。** 10月29日综合中的80/81已是历史状态，task.json及研究README也没有同步最新成果，不能据其判断当前数学进度。

本文是主会话确定的资料综合和策略判断，由指定原生gpt-6.1-sol/high文档执行者忠实整理。本轮依用户要求只在当前会话审计，没有调用外部Claude或外传研究材料；没有独立review、科研运行、求解或证明重放。除已有b25人工接受外，后续结构均保持 **unreviewed/unaccepted**。文档检查的`PASS_DOCUMENT_ONLY`不验证数学，也不升级旧接受或assurance。本文不宣称已完成所有历史证明的逐行复核。

## 1. 模型、输入和能主张到哪一步

记\(N_{\rm sig}(n,r,s)\)为完整有序rank-3 signotope中同时避免蓝r点路径、红s点路径和weak n的最大允许人口，**不是强迫阈值**。每个递增三元组完整染色；四点packet按abc、abd、acd、bcd至多变色一次。路径长度按实际顶点数计。weak7要求两色路径具有同一对实际首末点、长度和至少9，不要求内部不交。换诱导集后必须重算路径、rank、state及源终身份，ambient标签不能直接继承。

统一记

\[
A=N_{\rm sig}(7,5,7),\quad C=N_{\rm sig}(7,6,6),\quad
Q=N_{\rm sig}(7,6,7),\quad F=N_{\rm sig}(7,7,7).
\]

以\(a=16\)、\(b=25\)为有效上界输入，分别用于747和756。a的历史来源在[R5原稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R5_COVER_AUGMENTATION_CAPACITY.md>)指向Baek Theorem 2.7；本轮没有独立核定其精确性。b作为容量上界不要求先有达到实例；换色756共用该上界。

b25有两条不同的证据边。[C8人工接受记录](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md>)明确C1–C10均为human accepted，pending为空，限定完整有序rank-3、无B5/R6/weak7域；原same-family/provisional保证保持，未知reviewer backend/model及实际effort不补作核实。[实际25点存在性回执](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n756-professor-review-20261027/evidence/E21/verification.json>)另给完整颜色、packet及实际路径检查记录。上界接受本身不蕴含构造，本轮也未重跑该回执。

按现有结构工作证明，先写参数式：

\[
A\le a+b-1,\qquad C\le2b,\qquad Q\le3b+2,\qquad F=Q+1.
\]

代入才得40/50/77/78；沿对应几何转换\(\mathrm{ES}(7)\le F+1\)，条件性工作值为79。这里“条件性”指承重结构工作证明及其模型运输成立，不能把b25已接受扩展成整链已接受。

特别需要纠正一个递推读法：最新原稿直接给\(Q\le3b+2\)，**没有证明\(Q\le C+b+2\)**。由\(C\le2b\)不能倒推出后一更强响应式。目前也没有普适\(z\le2\)，新的加权式\(|X|+w\le3b+2\)尚未证明；可用的仍是\(|X|+w\le3b+3\)。三个“少一点”不能彼此替换。

因此，读“当前成果”要同时保留三层语义：有效输入允许后续推导使用；结构工作证明提出全模型结论；人工接受只覆盖其明确范围。报告采用工作结论，并不抹掉其未独审状态；保留未独审说明，也不等于把已经写出的全类工作定理降格为只有数值猜测。后续若发现承重接口缺口，应定位到那一边并修正传播，不能用旧输入的接受记录遮盖，也不应把所有独立证据一并作废。

## 2. 历史收益：哪些来自结构，哪些来自输入

按当时输入保留原账：初始45/58/103/206；R5首次严格减一后44/58/101/201；b29降28在R6传播为43/56/98/195；R7改变架构为43/56/89/177；b28降26在R8传播为41/52/83/165；R20精确根归约给41/52/83/84；b26降25在R23传播为40/50/80/81。这些是历史上界链，不能倒写成当时已经使用b25，也不是精确容量。

真正改变组织方式的三步是：R5用实际覆盖和合法增广兑现严格交叠；R7给实际不交H–R分解并用五点横截全部实际R6；R20证明精确\(F=Q+1\)，免去777独立双倍传播。b29→28→26→25则是上游输入改善，须单列记功。R1–R27逐轮索引见附录A，继承[10月26日复盘](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_REVIEW_R1_R27_20261026.md>)和[10月29日综合](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_SYNTHESIS_N7_20261029.md>)，不把条件族排除抹成“没有成果”。

10月16日的状态可达性说明757的56个、766的70个形式downset各自可在小合法配置实现；不同状态使用不同母体，未证明近满共同实现。10月19日归档四轮留下源终缺额、hole运输等接口，但没有独立接受或全局下降。它们说明为何后续必须研究共同供应，而不能继续凭单个目录可达性推容量。

更早的负面资产和工程贡献也须归位：[9/01普通状态矩阵](<D:/科研/math agent/erdos-szekeres-sat-main/reports/state_charging_transition_ordinary_matrix_20260901.md>)记录50格中47个SAT、3个verified UNSAT；[Qeq精确分区](<D:/科研/math agent/erdos-szekeres-sat-main/reports/state_charging_qeq_exact_partition_20260902.md>)与[位置标记](<D:/科研/math agent/erdos-szekeres-sat-main/reports/state_charging_qeq_position_marked_20260902.md>)说明固定状态、位置继续细分仍有完整反例，位置标签数不能当作不同missing资源。10/12–15的bridges/F3以及双锚、终端支持候选，见[10/15方案](<D:/科研/math agent/erdos-szekeres-sat-main/idea-stage/IDEA_REPORT_20261015_150106.md>)，属于上游证明求解工程，本身不计作后继N的结构降界，也无需重启已封存756任务。

10月29日综合之后出现了三次全模型**工作界**下降，已不能沿用“近期完全停滞”的判断：

| 原稿与日期 | 参数成果及真实推进 | b25下Q/F与边界 |
|---|---|---|
| [三匹配障碍，10/29](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_SATURATION_THREE_MATCHING_OBSTRUCTION_20261029.md>) | 同母体三组实际匹配与单cut根链矛盾，排共同满角，\(Q\le3b+4\) | 79/80；第一次下降 |
| [联合through，10/30](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_JOINT_THROUGH_SATURATION_AND_ORDERED_CUTS_20261030.md>) | 从任意canonical缺额兑现实际增广，得\(\lvert X\rvert+w\le3b+4\) | 仍79/80；加权稳定性 |
| [亏一前驱压缩，10/31](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_DEFECT_ONE_PREDECESSOR_COMPRESSION_AND_GLOBAL_BOUND_20261031.md>) | 完整覆盖临界机制，\(Q\le3b+3\) | 78/79；第二次下降 |
| [接口审计与加权稳定性，10/31](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_7879_INTERFACE_AUDIT_AND_WEIGHTED_THROUGH_STABILITY_20261031.md>) | 任意w换核归一化，\(\lvert X\rvert+w\le3b+3\) | 仍78/79；同会话核查非独审 |
| [Hall缺额实际增广根，11/01](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_HALL_DEFECT_ROOT_AUGMENTATION_AND_ZERO_THROUGH_CLOSURE_20261101.md>) | Hall缺额成为实际增广根，关闭doublefull旧3/4根剩余类 | 无新增数值下降 |
| [实际端点对Hall，11/02](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ENDPOINT_PAIR_HALL_MISALIGNMENT_EXCLUSION_20261102.md>) | 一般q、d±、m门槛；统一关闭onefull与bothclean | 仍78/79 |
| [锁纤维换核，11/02](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_FIBER_NORMALIZATION_AND_DOUBLE_OMEGA_EXCLUSION_20261102.md>) | 真实消M，排oneΩ+clean及部分doubleΩ | 仍78/79 |
| [锁区间与临界全排，11/02](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_INTERVAL_AND_CRITICAL_CLOSURE_20261102.md>) | 七入口关闭，\(Q\le3b+2\)；未强化旧加权式 | 77/78；第三次下降 |

其余主稿的价值主要是支撑接口和反检，不另算全局saving。10/29的defect-one、tight-cut/joint-neutral把含Ω/M与完整供应的剩余窗口定位；10/30的六根骨架关闭指定双满五根τ5的q≥5子类，随后complete-core稿关闭双五根且任一τ5整类；共同根间隙、内部支持和任意次序product稿改进完整匹配、private及合法root结构。pure-core与private-repartition保留完整路径分划竞争；11/01 locked-port把最早/最晚owner及锁供应接入实际核。这些覆盖有重叠，不能每篇再记一次下降。

评价历史轮次也要区别“无全局下降”的原因。有些稿已完成一个真实全族排除，只是尚余其他分支；有些只给必要条件，离排除尚有一步；还有些用完整反例说明原设想根本不成立。前者可直接作为后续覆盖接口，中者只有在新增联合资源时才值得续投，后者应成为禁止误用的反检资产。把三者都压成新增零会丢失研究信息，把三者都称突破又会夸大实际进度。

## 3. 最新77的承重接口与尚未完成的核查

最新主线使用实际母体X的全部红六源S、终T，中性区\(D_0=X\setminus(S\cup T)\)，以及

\[
w=|\operatorname{Src}_{R5}(D_0)\cap\operatorname{End}_{R5}(D_0)|.
\]

最后稿在\(|X|=3b+3\)用旧加权式得到w=0，再用canonical归一化和真实消M进入双向\(\eta\le2\)目录；绝非预先只选一个有利见证。其§8七入口分别是：任一η0；双正且双Ω空；恰一Ω非空；双Ω至少一侧(2,1,1)；两侧饱和且x≤y；饱和x>y且任一η1；饱和x>y且双η2。封闭分别由endpoint、lock-fiber及最终lock-interval三稿承担。

最后两类的关键改进是按实际根占用扣loss，同一根支持多个owner最多占一条matching边；再用锁区间不能穿过反向角色，推出完整满核低尾与实际首pair不相容。它没有假设任意middle边都能扩成perfect，也没有把小核可加点推成大核可加点。更大人口通过取临界诱导集并重算全部角色处理，w不假定遗传。

最新77依赖的全actual路径链应沿上述八篇主稿、[11/01完整锁端口稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCKED_PORT_ABSORPTION_AND_COMPLETE_REPARTITION_20261101.md>)、R7与R20读取，保持各自保证层级。**本报告不依赖未闭C49的Closure或Joint17全类语义运输来认领77。** 旧Joint17固定公式strict-RUP通过是有价值的既有证据，但不是这条最新手写工作证明的证书。

旧证据仍须准确记账：Through14固定字节回执与Joint17固定公式结果不能抹去；Closure的schema PASS明确不含实际CNF相等与UNSAT检查，后续获取停止于预算可行性，没有闭合C49。公式反驳、规则有效性、全类运输、人工接受是不同证据边。任何文档PASS都不能补上缺失一边。

下一轮先把长依赖压成6–8个可检查接口：模型与共用容量；canonical全缺额账本；全port及真实换核；Hall缺额到实际增广根；全部相邻pair的容量matching；middle交会及同端weak；锁区间和满核尾；全类入口与R20传播。每个接口须写输入域、输出域、缺额范围、调用方向和退出条件，检查空matching、重合角色、全部新pair及诱导身份重算，防止循环依赖。本轮只给这份核查安排，没有声称已经完成全量证明复核。

压缩依赖的重点不是缩短篇幅，而是让读者看见每次调用究竟保留什么。例如实际扩域无蓝五，需要检查旧核点、新点以及跨二者的全部路径，不能只引用新点没有蓝五源。某点不是红六终点，也不表示它不能作为另一红六的末前驱。删除一个端口层时，匹配损失要与实际删除点对应；当两层角色重合，须说明删除计数为何仍有效。最新原稿已专门处理若干这类问题，接口版应保留其证明责任。

另一个核查重点是定理使用的层数。旧加权式负责把旧临界层送入零through，归一化负责送入有限缺额目录，局部排除负责关闭目录，遗传性才把临界排除升格成全体人口上界。每步都有不同量词；若只摘出最后数字，容易把有限目录的适用条件误写成任意近满配置性质。下一层研究应重新走这几步，不能只把最终式中的常数减一。

## 4. 局部最优风险：保留失败资产，也承认近期突破

此前存在明显局部优化倾向：不断细分q、端口和owner标签，推出更多必要条件，却迟迟没有让同一母体支付正净损失。最近三次下降说明这一倾向可以被打破，成功共同点是完整供应、三组实际匹配、Hall缺额的真实增广以及锁区间尾部矛盾。下一步应延续这些可兑现接口，而非仅延长分类稿。

主要风险是把η3/η4逐型长稿当进度；把图上匹配当作实际同端点路径；换诱导集不重算身份；把一个核的可加点偷渡到另一大核；按owner个数重复扣同根loss；把多个chart的预算相加；把同一saving在正反、匹配与缺额账本中各记一次。仅增加必要条件而不排完整族，也不能预记全局收益。

负面资产必须保留准确量词。[D26](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_JOINT_EXTENSIONS_AND_H49_COMMON_CORE_20261027.md>)否定“单外根加满25自动产生缺额”；[D12](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ALL_CLASS_RESIDUAL_AUDIT_AND_DISJOINT_R6_COUNTEREXAMPLE_20261027.md>)否定残余红六必两两相交；[满25内部private稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_FULL_CAPACITY_INTERNAL_INSERTIONS_AND_PATH_EXCHANGE_BARRIER_20261028.md>)否定单满核的普遍自动端点化。它们均未给近满双核共同反例。

[10/30全局根障碍稿§7](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ARBITRARY_ORDER_PRODUCT_AND_GLOBAL_ROOT_BARRIERS_20261030.md>)给完整12点rootcycle、所有合法删根chart均w0，否定无近满前提的positive-through与天然无环；另一完整12点交错R6否定通用uncrossing。这不否定带近极值联合条件的定理。完整路径约束族统一记\(\mathcal F\)，避免与F=N777混淆；其路线仍缺任意critical进入以及pure-red、multi-private等全类覆盖。最新同块换代表定理只关闭相应product子类，不能冒充全类入口。

这些负面资产对路线选择的作用，是逼迫下一定理把近满前提写进假设，并解释它在哪个实际步骤产生额外约束。如果加入近满前提后，推导从头到尾都没有用到它，那么原小反例仍是首先应该检查的对象。反过来，小例规模远离近满，确实不能替代对目标临界层的反驳。正确停止点是失败的引理接口，而非笼统宣称所有联合结构方法无效。

## 5. P1主攻：下一临界层的统一缺额稳定性

先核对现链，再争取参数目标\(Q\le3b+1\)，从而\(F\le3b+2\)；b25时是76/77，几何工作目标78。必须排除任意\(|X|=3b+2\)，不是再排已关闭的3b+3层。当前加权式在新层只给\(w\in\{0,1\}\)，不能继续沿用旧w0。

由旧任意缺额预算\(n+w\le3b+5-\eta\)，在新临界层直接得到

\[
\eta_L\le3-w,\qquad \eta_R\le3-w.
\]

这只是下一层账本的代数限制，不是新上界或新归一化定理。w0容许η3；11/02的η≤2四种Ω类型并不穷尽η3，也不能自动覆盖w1。优先交付应是处理所有亏损的actual cut定理与真实归一化/修补，或一个完整反例把失败接口钉死。

可扩展的现成起点是endpoint稿§2。q、d−、d+、m非负且m≤q；U、V各q点，有q−m条实际middle R5匹配；实际基础集\(|K_\pm|\ge b-d_\pm\)。扩域无B5，且**每条**R6的末pair准确落U×B、首pair准确落A×V，严格cut满足B<c<A。此时

\[
|A|+|B|>q+d_-+d_++m
\]

迫三图正交会，得到同实际端点R5+B4矛盾。这里字母A、B是该局部定理的根集，与容量A区分；参数符号必须随定义域阅读。现成定理的障碍是能否对下一层所有候选兑现全部pair定位，而非把门槛再写一遍。

最值得尝试的是用“实际escape二部图匹配数”界净损失，统一处理共享根、共享owner与重复供应；同一根对应多个owner最多损一条matching边。返回锁边时须证明与保留matching在根层、端口层均不冲突，不能直接把锁数加回。目标是每个近满候选或出现正cut交会，或在零预算等号下迫满核低尾矛盾；当前没有证明这一全类入口。

第一份下一层账本应把w零与一分开，再列两方向各自允许的缺额范围；此时不要先假设锁、异常纤维或middle规模仍等于旧层。每一次真实换核，都要说明母体是否保持、哪些ambient角色保持、缺额是否不增，以及新核有没有引入新的首末pair。若某机制只能在更小子类内成立，应直接写出该子类与未覆盖余项，避免靠连续更换“标准”名称获得表面穷尽。

实际cut路线的价值，是把供应存在性转化为可计量的全图交会；它的难点仍是全部路径的定位，而不是某张抽象图能否匹配。零预算也必须进一步兑现成实际结构：哪些根必被占用、哪些锁只能落在一侧、哪个满核可以合法加入前驱、所有强制尾如何仍在该核。若最终只得到一组可同时满足的整数等式，就应承认尚未关闭，不把等式复杂度当作逼近矛盾的证据。

现有局部引理还可作一般p的参数提取，见附录C。它提供可复用的实际路径接口，并未解决任意临界母体进入该接口的问题，也不把七点横截5或全局3b+2推广到一般p。

## 6. P2短期桥接口与P3竞争架构

P2是先研究更强响应桥\(Q\le C+b+2\)。对每个canonical\(X=H\sqcup R\)，α为R的最大R6-free子集大小，τ为最小R6横截数，\(\alpha+\tau=|R|\)。所需目标可等价写成

\[
(C-|H|)+(b-\alpha)+(5-\tau)\ge3.
\]

因α+τ=|R|，这只是原目标的计账方式，本身不是新引理。当前只有把C换2b的预算至少3；不能自动减掉2b−C。缺失的是证明在响应C变化后仍保留三单位联合损失，而不与平衡缺额重复计。桥若成立，未来\(C\le2b-\Delta\)才能兑现\(Q\le3b+2-\Delta\)；Δ1时为76/77。应先短期检验桥，之后才决定是否投入独立C49。单靠现有数值传播接口，C49不能改进77；若新证明能利用C49，须另证响应接口。

P3保留完整路径K/Y/Z重分划作为真正竞争。令z是使删去Z后可分为\(K\in766\)、\(Y\in756\)的最小|Z|；全部存活R6须同时碰K/Y，存活B5须碰K，其他帽须继承，不能只处理选定障碍。旧z≤5。若独立证明\(C\le2b-\Delta\)、\(z\le5-\epsilon\)，则

\[
Q\le\min\{3b+2,\ 3b+5-\Delta-\epsilon\}.
\]

要超过当前77须Δ+ε≥4。于是z4、残余D29、单独C49乃至C49+z4，都已不足当前数值改进；z2+C50仅追平77，z2+C49或z1+C50才给76。旧综合的优先级必须据此更新。较可行的交付可以只针对\(|X|=3b+2\)的critical证明适当容量分划，不必先求所有X的强z1。仍须覆盖全部实际路径、pure-red与多private；product小类不能代替任意critical入口。

P3与主线的竞争应落在实际分划上：同一原母体的每一条存活红六是否被切开，每一条存活蓝五是否确实遇到K，剩余两核是否满足各自所有帽。只证一个最小不可满足子族可处理，可能遗漏子族外路径；只修一个private见证，也可能产生另一条mixed路径。允许多private和整族替换是必要覆盖责任，不能因当前product定理漂亮就省去。若能仅在目标临界层完成全路径分划，它仍是有价值的全类进入方式。

## 7. 储备路线、收益核算与停止条件

合法rootcycle只作储备。由当前加权式，每个合法删根chart满足\(|Z|+w(Y_r)\le3b+4\)。要排当前F的临界\(|Z|=3b+3\)，须某chart的w≥2，只有w≥1不够。若先证明新的weighted3b+2，则某chart的w≥1才足够。不同chart不可相加预算，12点例说明必须使用近满前提。prime/split仅在有bounded接口或进入定理时投资；不重开b<25、无传播桥的75739、单独777。

下面全部未来项均为条件性，基线Q77/F78。旧\(Q\le C+b+5\)仍可用来核算，但已弱于最新直接式。

| 未来交付 | 对Q的参数核算或缺失接口 | b25下Q/F |
|---|---|---|
| P1统一下一层全排 | \(Q\le3b+1\) | 76/77 |
| P2响应桥+C49 | \(Q\le C+b+2\) | 76/77 |
| 单独C49 | \(\min(77,49+25+5)=77\) | 77/78 |
| 单独z4 | \(\min(77,50+25+4)=77\) | 77/78 |
| C49+z4 | \(\min(77,49+25+4)=77\) | 77/78 |
| C49+z2 | \(\min(77,49+25+2)=76\) | 76/77 |
| 单独weighted3b+2 | 仅排3b+2层的w1窗口，w0仍在 | 77/78 |

推荐一主线P1、一竞争P3，P2短期桥研究嵌入主线；不要同时铺开多条长分类。该排序来自现有传播价值和接口成熟度，不提供虚构成功概率或时间保证。

每轮验收应是一条全称定理、一个完整引理反例，或严格关闭完整族；必须有全类入口、同母体实际路径、全部新三元组检查、净损失和传播。若仅标签增长、选择有利见证、只增必要条件或净收益为零，应停止该机制并记录首断点。已经证出的条件覆盖保留，但不靠改名继续记功。先把现有长证明压成可核查接口，再扩新层，可降低沿未察觉缺口累积长稿的风险。

实际执行时，可先交付一页“目标层—完整入口—净损失—传播”说明，再决定展开哪一个机制。若主线在w零或η三处没有全类入口，应明确留下该分支，转用竞争架构检验，而非同时写多篇条件长稿。若竞争路线只能反复覆盖旧product子类，也应暂停其泛化承诺。这样的停止规则保留已完成工作，同时使下一次投入依据真实断点，而非根据稿件数量或标签深度。

## 8. 公开结果的短比较与本轮边界

主会话本轮公开核实的[Schroeder伴随页](https://michaelschroeder.ai/research/ErdosSzekeres/companion)Version 1报告ES7≤81，并明确尚无external peer review。本项目条件性工作79在数值上低于这一特定主张；本轮没有完成全球最新纪录检索，也不宣称新的公认纪录。[Baek–Balko SoCG 2025](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2025.13)涉及的分解类、更宽超图与这里完整signotope不能混同，不能跳过模型运输便迁入数字。

当前最合理的继续方式，是把近期成功的实际增广、全pair matching和根占用计损推广到下一临界层；竞争路线则承担检验架构是否过度锁定canonical分解的责任。所有新目标保持待证，77/78也保持工作证明层级。本文只新增综合和文档回执，不修改旧稿、任务元数据、接受、证明绑定、runtime或运行，不提交、不归档。

## 附录A. R1–R27历史简表与原始入口

以下保留10/29综合的历史原表；“新增0”只指当轮没有新增全局数值下降，不能否定条件覆盖、反例和表示价值。数字按当时输入阅读，原稿入口用于追溯，不以本表代替承重证明。

| 轮次与原始稿 | 主要工作与留下的东西 | 全局数值或准确边界 |
|---|---|---|
| [R1](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESTART_SETTING_ANALYSIS.md>) | 状态单射、径向切口、共同外端目录；指出压缩后纤维容量未知 | 45/58/103/206；新增 0 |
| [R2](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R2_COMMON_START_CAPACITY.md>) | 共同起点纤维非 Markov；777 中 $K=N-1$ 仍未给容量下降 | 新增 0 |
| [R3](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R3_BIDIRECTIONAL_IDEAL_INTERVALS.md>) | 双向理想区间精化，投影容量未降 | 新增 0 |
| [R4](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R4_BIDIRECTIONAL_COVER_DEFICIT.md>) | 实际覆盖与缺额取等；缺严格正值 | 新增 0 |
| [R5](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R5_COVER_AUGMENTATION_CAPACITY.md>) | 全局点对序、无环支持、合法增广，首次严格 −1 | 44/58/101/201，结构收益真实进入全局草稿 |
| [R6](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R6_OVERLAP_TWO_AND_766_TRANSFER.md>) | 一般 n 推广；第二单位仍不普适 | b28 输入传播为 43/56/98/195；固定旧输入的新数值收益 0 |
| [R7](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md>) | 真实不交 H–R 残余和五点横截，改变相加架构 | b28 下 43/56/89/177 |
| [R8](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R8_UNIFORM_DEFICIT_AND_JOINT_CAPACITY.md>) | 联合资源预算，未强迫新缺额 | b26 外部输入传播为 41/52/83/165 |
| [R9](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R9_RESOURCE_STABILITY_AND_TRANSVERSAL_COST.md>) | 可达簇与资源稳定性；粗容量 300 不能兑现 | 新增 0 |
| [R10](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R10_EXIT_WITNESSES_AND_CORE_TRANSVERSALS.md>) | 共同尾窗、出口替换；有条件改善，无一般入口 | 新增 0 |
| [R11](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R11_OWNER_CERTIFICATES_AND_JOINT_DEFICIT.md>) | owner 证书、全源至多 15 等限制；未迫正需求 | 新增 0 |
| [R12](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R12_COMMON_REALIZABILITY_AND_UNIFORM_DEFICIT.md>) | 可分类精确 O；一般正超额定位到 prime 叶 | 新增 0；全类 prime 容量仍未知 |
| [R13](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R13_GLOBAL_STRUCTURE_AND_JOINT_CAPACITY.md>) | 边界超图与 mixed triples 强制必要修复需求 | 缺修复成本上界；新增 0 |
| [R14](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R14_JOINT_REALIZABILITY_AND_GLOBAL_DEFICIT.md>) | 双锚点、完整空侧修复优化恰回 $M-J$ | 该预算路线无净收益；新增 0 |
| [R15](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R15_GLOBAL_COMPATIBILITY_AND_UNIFORM_DEFICIT.md>) | 全端点 frontier 与 Σ 上界；没有正需求下界 | 新增 0 |
| [R16](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R16_TERMINAL_FRONTIERS_AND_JOINT_STATE_REALIZABILITY.md>) | 桥匹配条件、真实十点 Σ=0 校准 | 条件性收益无普适前提；新增 0 |
| [R17](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R17_GLOBAL_CO_SATURATION_AND_CAPACITY_TRADEOFFS.md>) | 匹配数与真实删除成本可相差大；节省抵消旧 slack | 反例族 $p\ge4,n\ge2p-1$，不是766反例；新增 0 |
| [R18](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R18_GLOBAL_SATURATION_AND_IRREDUCIBLE_CAPACITY.md>) | 真实22点需两次修复；特定 fan 强迫三个缺态 | fan 前提未覆盖全类；新增 0 |
| [R19](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R19_GLOBAL_REALIZABILITY_AND_CAPACITY_ARCHITECTURE.md>) | 共同26核与全部最小横截，暴露重用及多供应 | 新增 0 |
| [R20](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>) | 全 chart 精确一点归约；H–R 全路径接口 | b26 下 41/52/83/84，777 从165降84；不等于文献新纪录 |
| [R21](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R21_GLOBAL_CAPACITY_AND_SUPPLY_REALIZABILITY.md>) | D 双核与 sweep；自由规范化、短帽保持均不成立 | 新增 0 |
| [R22](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R22_GLOBAL_ARCHITECTURE_AND_CAPACITY_REALIZABILITY.md>) | 可逆 root chart 与 record 表示 | 表示完整不等于新增排除；新增 0 |
| [R23](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md>) | 非平凡中点类精确30、经典满容量 pair 供应、25点多目录 | b25 工作输入传播 40/50/80/81；本轮结构新增 0 |
| [R24](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R24_GLOBAL_COMPATIBILITY_AND_EXTREMAL_REALIZATION.md>) | 排除整个 X80 的 q=11 人口支；非中点30族全插入临界 | q=1…10 保留；新增 0 |
| [R25](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R25_GLOBAL_EXTREMAL_STRUCTURE_AND_JOINT_REALIZABILITY.md>) | 排除 X80 嵌入 m 或 m′=11…15；旧 fan 模块整类仍30 | m,m′=5…10 与 $m+m'+q-w\ge15$ 无矛盾；新增 0 |
| [R26](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R26_GLOBAL_BREAKTHROUGHS_AND_EXTREMAL_COUNTERTESTS.md>) | 全 X 内禀锁定预算、proper cut 类46、critical16 等价 | 正反预算不能相加；临界16开放；新增 0 |
| [R27](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R27_GLOBAL_REALIZABILITY_AND_SATURATED_CORE_COUNTERTESTS.md>) | 任意经典满核两整族的全合法 chart 排除；十点 lacing 反例；完整 π/e 表示 | canonical 删除零净收益；一般 critical16 未闭；新增 0 |

## 附录B. 辅助主稿与证据原件索引

承重最新稿及八篇时间链已在§2–3链接；以下补齐辅助结构和旧证据入口。历史综合中对过期开放项的描述按其日期阅读，最新关闭状态以11/02最终稿§8为准。

| 辅助原稿 | 保留的用途与范围 |
|---|---|
| [N7：缺额一的联合稳定性与完整链接紧割](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_DEFECT_ONE_JOINT_STABILITY_AND_LINKAGE_CUTS_20261029.md>) | 亏一机制目录与mixed锁定；不另记全局saving |
| [N7：紧割纯核供应、联合neutral预算与完整重分划二分](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_TIGHT_CUT_JOINT_NEUTRAL_AND_REPARTITION_DICHOTOMY_20261029.md>) | 紧割、joint-neutral与完整重分划二分 |
| [N7：六根骨架、外部 private 供应障碍与覆盖审计](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_SIX_ROOT_SKELETON_AND_EXTERNAL_PROVIDER_OBSTRUCTIONS_20261030.md>) | 指定六根骨架及完整外供位置障碍 |
| [N7：双五根共同饱和禁形与完整路径重分划](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMPLETE_CORE_PROFILES_AND_PRIVATE_REPARTITION_20261030.md>) | 双五根τ5整类排除、全路径窗口与private整族分划 |
| [N7：共同根间隙、内部切点校准与内支持分离拟阵障碍](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_COMMON_ROOT_GAP_AND_INTERNAL_SUPPORT_OBSTRUCTIONS_20261030.md>) | 共同根间隙、内部插入及分离支持限制 |
| [N7：任意次序 product 禁形、全局根障碍与完整外供边界](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ARBITRARY_ORDER_PRODUCT_AND_GLOBAL_ROOT_BARRIERS_20261030.md>) | 任意次序product、全ambient perfect与两项12点反例 |
| [N7：纯核根严格分离与交错重分划](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_PURE_CORE_ROOT_SEPARATION_AND_INTERLEAVED_REPARTITION_20261030.md>) | 纯核分离、交错分划及完整private竞争接口 |
| [N7：空锁定分支的全残余普适性与实际分块的费用边界](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_EMPTY_LOCK_UNIVERSALITY_AND_OPERATION_LIMITS_20261028.md>) | 空锁普适与实际操作范围限制 |

10/28–29辅助十稿按历史范围保留如下；表中未闭项不覆盖11/02后的新关闭：

| 主稿 | 新的实质或准确停止处 |
|---|---|
| [统一全尾区间稳定性，10月28日](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_UNIFORM_TAIL_INTERVAL_STABILITY_20261028.md>) | 全尾结构、区间条件与完整路径障碍对偶被明确化；小规模有限一致性通过。没有四近满核共同不相容、严格缺额或z4。 |
| [最优交叠交换与切口接口，10月28日](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_OPTIMAL_OVERLAP_EXCHANGE_AND_CUT_INTERFACES_20261028.md>) | 完整实际暴露族与切口判据；小例否定局部贪心完备、private-only认证和最近点对压缩。需要批量交换，未迫全类正收益。 |
| [lex最优覆盖与耦合成本，10月28日](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LEX_OPTIMAL_COVERS_AND_COUPLED_PARTITION_COST_20261028.md>) | 等成本交换和净收益公式成立于明确前提；全类正规化、安全回填单调性被纸面完整反例否定。本稿有限机器执行未完成，不填作通过。 |
| [近容量兼容与双向重分配，10月28日](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_NEAR_CAPACITY_COMPATIBILITY_AND_BIDIRECTIONAL_REPARTITION_20261028.md>) | 逐位置插入与双向搬移保留完整路径；小规模母体可核查。人口headroom不自动保证接收核安全，全类存在性仍缺。 |
| [满容量内部插入与路径交换屏障，10月28日](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_FULL_CAPACITY_INTERNAL_INSERTIONS_AND_PATH_EXCHANGE_BARRIER_20261028.md>) | 满25也有仅内部private见证；同端路径可能须同时替换p−1个内部点。否定单满核自动端点化与普遍小步交换，未排双满临界类。 |
| [饱和接口匹配与临界支持，10月28日](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_SATURATED_INTERFACE_MATCHINGS_AND_CRITICAL_OBSTRUCTION_SUPPORTS_20261028.md>) | 实际端点图与完整MUS内部某些区间共享签名被约束。Hall不等于独占支持；未证明一般MUS进入这些签名，纯红分支仍开。 |
| [完整pair扇与紧核二分，10月29日](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_FULL_PAIR_FAN_BOUNDARY_AND_TIGHT_CORE_DICHOTOMY_20261029.md>) | 完整支持上的紧／严格Hall二分及缺角接口具体化；没有证明临界母体必有低边界载体，也未迫所有实际边进入某完美匹配。 |
| [H50–R30共同饱和与全支持，10月29日](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_H50_R30_COMMON_SATURATION_AND_FULL_SUPPORT_BARRIERS_20261029.md>) | 同母体共享P的两个满25核及mixed路径定位，三有序R5支持由旧工具组合。缺同一实际pair；内部插入曾漏新三元组，已修正。 |
| [neutral-through残余增广与MUS，10月29日](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_NEUTRAL_THROUGH_RESIDUAL_AUGMENTATION_AND_MUS_SUPPORT_20261029.md>) | canonical满H下实际增广给条件loss=w，排共同等号全部w≥1支；完整MUS unique-private支持也有真排除。仍无一般z4或X80排除。 |
| [残余端点刚性与强制等号，10月29日](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_RESIDUAL_ENDPOINT_RIGIDITY_AND_FORCED_ROLE_EQUALITIES_20261029.md>) | 强制双角色预算取等；正反残余均恰五端点；全B4第二点图Hall与另一合法残余得到认证。五端点双等号仍开，补集未证766。 |

旧证据绑定入口：

- [Through14固定字节回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_abstract_port_20261026/through14_replay_result.json>)；[Joint17完整固定公式结果](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/joint17/result.json>)。
- [Closure schema结果](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/closure/result.json>)；[获取停止回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/closure_acquisition/abort_receipt.json>)；[全缺额联合旧稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_GLOBAL_DEFICIT_FRAME_AND_JOINT_THEOREM_20261027.md>)。
- [10/16状态可达性](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/757-766-mathematical-structure-20261016.md>)；[10/16红六端点](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/757-red-six-fan-gap-20261016.md>)；[10/19四轮归档](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/archive/2026-10-19-paused-route-rounds-1-4/README.md>)。

## 附录C. 实际端点对Hall的参数提取

这是本轮主会话从endpoint稿§2抽取的局部接口推导，不是独立审阅结论，不宣称原创或新的全局上界。令p≥3，\(b_p\)为\(N_{\rm sig}(p+2,p,p+1)\)的有效上界。母体禁\(B_{p+1}\)、\(R_{p+2}\)、weak\((p+2)\)。U、V各q点，完整实际\(R_p\)端点图含q−m条matching，其中q、d±、m非负且m≤q。

实际基础集K−含U、K+含V，规模分别至少\(b_p-d_-\)、\(b_p-d_+\)。根集B、A在对应核外且与对应端口层不交，严格B<c<A。扩域K−∪B、K+∪A均无\(B_p\)，其**全部**\(R_{p+1}\)的末pair、首pair分别在U×B、A×V。则

\[
|A|+|B|\le q+d_-+d_++m.
\]

确实，任意pair图vertex cover删除后击中全部\(R_{p+1}\)，余域无\(B_p\)且继承weak禁形，人口至多\(b_p\)。König给左右matching至少|B|−d−、|A|−d+；沿middle运输至多失m，三图交会至少两根总数−q−d−−d+−m。若此数为正，真实链给u<r<c<s<v，两条\(R_{p+1}\)的\(R_{p+2}\)帽迫\(B_4(u,r,s,v)\)，与\(R_p(u\to v)\)具有同一实际端点，长度和\(p+4=(p+2)+2\)，违反weak\((p+2)\)。路径内部允许共享。p=5恢复现有七点接口；没有从该局部推导获得新的全类入口或人口下降。
