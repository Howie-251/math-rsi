**N_sig(7,r,s)研究综合、结构审计与下一步方向**

截至2026年10月28日，覆盖R1–R27、其后14份记录，以及当天最新4份尾区间、最优交叠、lex覆盖和近容量重分块记录。核心结论是：现有研究已取得三类真正影响上界传播的结构工具，但近期有明显的局部优化倾向。应把下一阶段的研究单位从单个见证、人口标签或固定小模板，转为同一完整染色中多个近满核心的共同实现。当前可沿用的结构草稿链仍为40/50/80/81；新增四份记录没有降低这些界。

这里的审核是本会话的来源核查和数学策略审计，未重新认证所有历史证明。逐轮台账依托既有综合，并抽查承重原稿与最新四稿；有限结果和接受记录分别核对。独立Claude路由在[.aris/README.md](<D:/科研/math agent/erdos-szekeres-sat-main/.aris/README.md>)中标为disabled、activated=false，本次没有调用或重试；后续结构稿继续unreviewed/unaccepted。b25已有人工接受的状态与后续结构稿的状态分开。

**1. 模型与目前真正成立到哪一层**

N_sig(n,r,s)表示完整有序rank-3 signotope中，避免蓝r路径、红s路径与weak n的最大规模；路径长度计顶点，四点包abc/abd/acd/bcd至多一次变色。weak n由同一对实际端点的异色路径组成，长度和为n+2。诱导子配置的路径、秩和状态必须在内部重算。它不是几何强迫阈值；从这套界只能推出ES(7)≤N_sig(7,7,7)+1，因此81对应几何强迫82。

记a为747有效上界，b为756有效上界，C=N_sig(7,6,6)，Q=N_sig(7,6,7)，F=N_sig(7,7,7)。目前a=16、b=25。b25的C1–C10已人工接受，保证标记仍same-family/provisional；该上界证书本身不承担25点存在性。[R23](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md>)和[后续共同满核扩张稿](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_JOINT_EXTENSIONS_AND_H49_COMMON_CORE_20261027.md>)有完整25点构造材料，应单独引用。

证据层级：

- \(N_{\rm sig}(7,5,6)\le25\)：已有人工作出的正式接受，限指定模型。来源[C8正式接受记录](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md>)。
- R5/R6、R7、R20形成的结构传播：已有证明草稿，尚未独立接受；本报告不升级状态。
- Joint17：固定公式strict-RUP重放PASS，不能替代全部语义运输的独立审查。来源[Joint17原始结果](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/joint17/result.json>)。
- Closure：规则/schema核查通过，但actual_cnf_equality_checked=false、UNSAT_checked=false；获取停止回执为ABORTED_BUDGET_FEASIBILITY，source_acquisition_complete=false、CNF_binding=false。因此C≤49仍未闭合。来源[Closure规则结果](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/closure/result.json>)及[来源获取停止回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/closure_acquisition/abort_receipt.json>)。
- 最新有限实例核查：仅支持其完整小实例和接口；不证明全类上界。

**2. 先结构关系，后数值代入**

边界增广定理草稿在n≥4、4≤r≤n的边界s=n给出

\[
N_{\rm sig}(n,r,n)\le N_{\rm sig}(n,r-1,n)+N_{\rm sig}(n,r,n-1)-1.
\]

其严格一点来自真实覆盖增广和点对序，不是可任意移植的Pascal递推。特别不能无条件套到(7,6,6)。来源[R6 §6](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R6_OVERLAP_TWO_AND_766_TRANSFER.md>)。

平衡分解对p≥3给出

\[
N_{\rm sig}(n,p+1,p+1)\le2N_{\rm sig}(n,p,p+1).
\]

它把一个实际母体拆成受同一容量控制的两块。一般式本身没有严格缺额。

七点canonical分解给X=H⊔R，H属于766，R属于特殊残余类D7。R不仅禁蓝五和weak7，还满足红五末点与蓝四源点不相交的junction条件。对R的全部实际红六存在至多五点横截；删去后进入756，所以

\[
Q\le C+D_7,\qquad D_7\le b+5.
\]

五点常数来自七点特殊结构，不能直接写成任意n的n−2。[R7](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md>)另给一般n≥7的较粗关系D_n≤N_sig(n,n−2,n−1)+N_sig(n,n−4,n)，并明确n≥8的阻断。

根归约草稿给n≥4时

\[
N_{\rm sig}(n,n,n)=N_{\rm sig}(n,n-1,n)+1.
\]

其关键是合法chart和weak保持，以及反向真实添根；不是任意pivot都保持短帽。此关系的几何前身和抽象chart工具已有文献，不能把本地传播下降自动称为新的文献纪录。来源[R20](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>)及[R20新颖性比较](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/R20_NOVELTY_COMPARISON_20261023.md>)。

最后代入a=16、b=25：

\[
N_{757}\le a+b-1=40,\quad C\le2b=50,\quad Q\le C+b+5\le80,\quad F=Q+1\le81.
\]

这正是用户提出的结构形态；下一步应改进其中承重结构项。

**3. 全部研究工作的贡献脉络**

将历史工作归为五组，完整逐轮来源表放在文末。

- 状态与基界：状态单射、ordinary/exceptional账本M=O+e−m；756的接受证明给m≥e，最终得到b25。一般参考O(n,r,s)=sum_{j=n−s}^{r−2} binom(n−2,j)，在max(r,s)≤n≤r+s−2下使用。757/766/767/777的参考数是26/30/31/32，不能当作已证明的全模型上界。
- 全局结构：R5/R6真实重叠、R7实际H–R残余和横截、R20精确根归约，确实改变传播。初始45/58/103/206，经R5的44/58/101/201、b28输入与R7后的43/56/89/177、b26后的41/52/83/165、R20后的41/52/83/84，到b25后的40/50/80/81。输入改善与结构改善分开计功。
- 联合饱和：R8–R19、R21–R27建立源末角色、全供应、锁定、fan/cut、prime、共同核及修复约束，排掉若干真子类，但没有完成全类进入或统一正缺额。
- 10月26–27日balanced49/D7：迁移、共享尾、共同赋值、满核扩张、Joint17、Closure等。Joint17有实际证据进展；Closure未闭合；D30完整分支超时为未决定。
- 10月28日：从canonical选择转向全部合法覆盖与分块，给出了全尾区间结构和完整交换判据，并发现新的路线边界；仍未得到全局严格改善。

最新四稿的增量：

| 原稿 | 已得到 | 尚未得到 |
|---|---|---|
| [UNIFORM_TAIL_INTERVAL_STABILITY](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_UNIFORM_TAIL_INTERVAL_STABILITY_20261028.md>) | 实际源核与每条尾的圈标记区间图，安全增广宽度≤核缺额；全路径分块障碍的精确横截对偶，最小不可满足族至少33条路径 | 四个近满核共同矛盾；更小的删除成本 |
| [OPTIMAL_OVERLAP_EXCHANGE_AND_CUT_INTERFACES](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_OPTIMAL_OVERLAP_EXCHANGE_AND_CUT_INTERFACES_20261028.md>) | 最优重叠ρ及全部暴露路径交换判据；实际小步贪心/私人族/最近点对反例 | 所有近满母体ρ≥1或更强 |
| [LEX_OPTIMAL_COVERS_AND_COUPLED_PARTITION_COST](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LEX_OPTIMAL_COVERS_AND_COUPLED_PARTITION_COST_20261028.md>) | 合法单交换的副势下降；两色正规化反例；联合分数及带净收益的回填条件定理 | 操作普遍存在；两项原定有限核查均NOT_RUN，不能记PASS |
| [NEAR_CAPACITY_COMPATIBILITY_AND_BIDIRECTIONAL_REPARTITION](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_NEAR_CAPACITY_COMPATIBILITY_AND_BIDIRECTIONAL_REPARTITION_20261028.md>) | 单点插入障碍等价私人路径的审计；真实b3端点化反例；完整双向搬移条件定理及16点正例 | 七点近48/78母体的存在性定理 |

[尾区间](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_tail_interval_stability_20261028/result.json>)、[最优交叠](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_optimal_overlap_20261028/result.json>)和near-capacity的[MAIN](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_near_capacity_20261028/main_result.json>)／[竞争](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_near_capacity_20261028/coupled_result.json>)原始result均标FINITE_CONSISTENCY_PASS_UNREVIEWED_UNACCEPTED；[lex稿科学核查未运行](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_lex_coupled_20261028/EXECUTION_UNAVAILABLE.md>)。本轮仅读取这些结果。

**4. 局部最优审计**

判断：有明显、持续的局部优化倾向，但没有证明结构路线耗尽。问题在于“证明对象不断细化，真正减少全局容量的机制没有跟上”。

第一，恒等式和必要条件容易被误当新约束。最优覆盖中，每个角色点都有私人路径，所以每个外点插入受阻；这甚至只需包含极小性，不需要b25或近满性。将其改写成多个外点插入、目录或trace，并未新增容量信息。最新[NEAR_CAPACITY §3](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_NEAR_CAPACITY_COMPATIBILITY_AND_BIDIRECTIONAL_REPARTITION_20261028.md>)已明确证明这一点。

第二，局部反例越来越准确，但常未触及近极值。小例可否定不加前提的正规化、端点化或单调性，不能自动说明48/78甚至50/80不存在或存在。反过来，若每轮只拿远离容量的小例修补机制，下一轮又换一个局部标签，就会循环。

第三，条件操作定理不等于存在定理。完整暴露族、单向回填和双向搬移都是有价值的验证接口；“若找到合法D，就得到收益”之后，承重问题仍是为什么任意临界母体都存在这样的D，同时保证接收核合法。

第四，重复费用必须停止。同一核心的独立容量缺额η与最优交叠ρ只能取max，不能相加；不同分块、不同最优核、不同方向的预算不能拼成一个母体的净收益。路径见证可能共享支持，数量不等于独占资源。

第五，已被实际反例否定的捷径不应重开：空锁自动缩小D、红六路径两两相交、满25必全ordinary、私人族即可认证批量交换、最近边界点对足够、最优角色必可连续分色、合法回填必不损联合收益、人口余量保证接收核可吸收。反例的准确参数范围见原稿，不能扩大为对所有近满路线的否定。

第六，目标层级也需调整。直接选47/77/78再倒推所需缺额，容易继续做同一局部问题。先证明一个真正覆盖临界层的结构定理；由定理决定能下降几单位。757从40降39暂不进入Q≤C+b+5，777又由Q精确决定，故两者均不是当前主攻位置。已有25点构造材料也使继续压b低于25不合理，除非首先推翻其模型核验。

**5. 一个统一的结构推进框架**

对平衡X取不交实际横截U,V，分别命中全部红p、蓝p；令W=X∖(U∪V)，A=X∖V，B=X∖U，并令ρ(X)为全部合法对中最大的|W|。两核均受b控制，故

\[
|X|+\rho(X)\le2b.
\]

若|X|=2b−δ，定义d_A=b−|A|、d_B=b−|B|，则

\[
d_A+d_B+\rho=\delta.
\]

这把问题定位到两个近满核在同一完整颜色中的相容性；恒等式本身不算新成果。p3、n5已有真实C=2b=6，故不能无条件宣称所有n=p+2都有严格−1。七点需要真正使用同端R5+B4构成weak7的专属预算，并允许插入点是内部点。

对767的实际合法分块X=K⊔Y⊔Z，K∈766、Y∈756，在K内重算ρ，定义g=5−|Z|+ρ(K)。则

\[
|X|\le3b+5-g.
\]

若K的最优双核缺额为d_A,d_B，Y的缺额为d_Y=b−|Y|，更精确地

\[
|X|+g+d_A+d_B+d_Y=3b+5.\tag{*}
\]

这是已有计数关系的整理，不是新增排除；它说明“共同满核”应成为研究对象。旧分块定理保证可选|Z|≤5，因而g≥0。

统一临界层：要证明Q≤3b+5−γ，只需排除规模M=3b+6−γ的母体，因为诱导子配置保留禁形。在该规模上，(*)变为

\[
g+d_A+d_B+d_Y=\gamma-1.
\]

先写这条关系，再代b25：

| 临界规模M | 欲得Q界 | 三核与联合收益的总预算 |
|---|---|---|
| 80 | 79 | 0：g=0，K的两核及Y全部满25 |
| 79 | 78 | 1 |
| 78 | 77 | 2 |

80层还强迫|K|=50、|Y|=25、|Z|=5、ρ(K)=0。它比任意50点平衡母体多了一个满25接收核及五个残余点，因而是一个值得优先利用的结构入口；这不构成“80一定更容易排除”的证明。

**6. 最值得推进的方向**

方向一，首选：同一H–R中的共同取等不相容。先以符号有效上界c≥C、b写精确预算。R中红六最小横截τ≤5，最大红六自由子集α满足α=|R|−τ≤b，于是

\[
c+b+5-|X|=(c-|H|)+(b-\alpha)+(5-\tau).
\]

第一里程碑是证明在同一个canonical母体中H满c、α满b、τ满5不能同时成立；这会直接给Q≤c+b+4。c50、b25时就是Q≤79、F≤80。此目标不要求独立C≤49，也不要求所有D7≤29。

承重机制应使用已知真实接口：H内任意两端之间没有ambient红六；H达到2b时，每个残余点都启动一条其余五点在H的红六；extender之间的蓝/红同端预算限制共同供应。下一引理必须证明这些全部供应在三满核下产生同一实际端点的禁形，或迫出一个经过全部路径核验的增广。仅重新列出每个外点有供应不算进展。

完整双向搬移是该方向的一种可验证出口：T⊆Z、S⊆Y、D⊆K；新K=(K\D)∪T∪S，新Y=(Y\S)∪D，新Z=Z\T。D须命中扩展核心中的全部红六和全部避开原蓝横截V的蓝五，新Y须完整合法。则g的增量至少|T|−|D∩W|。80层W空，任何非空T且满足全部条件的操作都会造成矛盾；真正任务是从packet与共同取等强迫操作存在。满Y不能直接接收非空D，因此双向或其他全局重分块不可省略。不要把条件定理再写一遍当成果。

方向二，并行主线：756取等与近取等的内在相容性，导出平衡严格递推。目标先保持一般形式

\[
N_{\rm sig}(n,p+1,p+1)\le2b-\eta,
\]

η由结构引理得到；本次主攻(n,p)=(7,5)，不承诺对全部n,p成立。首个问题是两个满756核是否能以全局最优覆盖共同实现50点平衡母体。若能排除50，得C≤49；再研究缺额1层排49，才能得到48。不要强迫首篇引理一次排48。

有价值的前置成果应是b25等号/近等号的实际路径结构：哪些端点供应、内部插入位置或多核共享会必迫m>e，或出现同端R5/B4。不能假设e=0；已有满25的e=m=0/7/8/10目录。也不能把仅适用于源核的尾区间定理运输到任意最优核。产物必须是一条可用于共同实现的限制，不是更长的状态表。若仍只得到私人路径已保证的插入存在性，立即停止这一候选。

方向三，有限投入：残余扩张的取等稳定性。对R∈D7，取最小红六横截T，t=|T|≤5，Y=R\T，d=b−|Y|。寻求由实际扩张结构导出的函数f(t)使d≥f(t)，则

\[
D_7\le b+\max_{0\le t\le5}(t-f(t)).
\]

最小有用目标仅是t=5⇒d≥1，就足以D7≤b+4；不必证明更强的τ≤4。需要同一满25核和全部五外点的共同实现，保留多外点路径和全部目录类型。D26单外根反例与D12不交红六已经结束相应捷径。若出现完整D30构造，停止独立D≤29目标，但方向一仍可研究D30不能与满H共存。

方向四，长期储备：近极值母体的可分解性或不可约核容量。R12及后续proper cut/fan类确有强容量结论；所缺是全类进入。只有能证明近极值母体经有界删除进入这些类，或为所有不可约核给出独立容量上界，才值得升为主线。当前不能把未知母体改名prime，或继续在已知30点模块上加点当作突破。此方向与局部交换相对独立，但可行入口比前三者更少。

有边界的证据任务：补齐既有balanced49的Closure来源与语义/实际CNF/证明连接。全部闭合后才使用C49，并立即沿旧链得Q79、F80。这是近期最具体的证据台阶，但不替代新的结构研究，也不在本轮启动下载、运行或重放。

**7. 数值收益只在结构定理之后计算**

若独立证明C≤2b−η及D7≤b+5−ε，则Q≤3b+5−η−ε，F≤3b+6−η−ε。若另证联合缺额λ，必须相对于已改进的两容量重新证明，才能再相加。同一核心ρ与η仍只能取max。

| 条件性结构成果 | C界 | Q界 | F界 |
|---|---|---|---|
| 当前草稿链 | 50 | 80 | 81 |
| 仅平衡η=1 | 49 | 79 | 80 |
| 仅残余ε=1 | 50 | 79 | 80 |
| 仅共同取等不相容λ=1 | 50 | 79 | 80 |
| 独立η=1、ε=1 | 49 | 78 | 79 |
| 临界78层被完整排除 | 未必改善50 | 77 | 78 |

这些是条件推论，不是本报告宣布的新界。757仍为40；若要主投757，先给出它进入新767递推的桥梁。

**8. 下一轮具体交付与停止条件**

建议主投方向一，方向二作为可复用的并行结构主线；方向三限量备选，方向四保留。不要同时扩展多套状态目录。下一轮先选择一个明确临界层，优先80或50；用一般b/c写量词和结论，证明后再代25/50。首个交付应包含：目标母体的全类入口；实际共同实现限制；一次完整禁形或增广证明；净收益和传播。没有全类入口的子类定理、没有存在证明的操作判据、没有严格净值的修复，都不能登记新上界。

固定对抗资产包括满25多目录、D26单根、D12不交红六、任意残余加蓝右根的空锁嵌入、p3/n5满双核端点化反例、最新16点大余量仍接收失败的例子。反例必须按实际范围使用；低参数或小母体反例不否定七点近满目标。计算以后只服务于明确引理的反证或最小实例核验，不以越来越大的参数搜索代替结构入口。

**9. 历史逐轮来源台账**

下表保留历史当时输入与状态；最新四稿增量见本文第3段。两表共41个历史记录，另加最新4份，共45份研究记录。

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

| 原始稿 | 本次综合中的位置与边界 |
|---|---|
| [balanced49迁移与联合缺额](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/BALANCED49_TRANSFER_AND_JOINT_DEFICIT_20261026.md>) | 区分几何定理与signotope语义迁移；尚不能使用C≤49。 |
| [共同尾与终点障碍](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/BALANCED49_CONTINUATION_SHARED_TAILS_AND_TERMINAL_BARRIERS_20261026.md>) | 实际前后供与端点身份；完整闭合义务另计。 |
| [全见证点对秩与分叉反例](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/BALANCED49_ALL_WITNESS_PAIR_RANKS_AND_FORK_COUNTEREXAMPLES_20261026.md>) | 全见证校准；有限反检、形式化切片不等于联合容量。 |
| [饱和Y交换与横截障碍](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/BALANCED49_SATURATED_Y_EXCHANGES_AND_TRANSVERSAL_OBSTRUCTIONS_20261026.md>) | 私人路径和实际替换；不可按路径数重复收费。 |
| [共同赋值与剩余H49支](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/BALANCED49_COMMON_ASSIGNMENT_AND_REMAINING_H49_BRANCH_20261027.md>) | Through14接通原始证据；满核删一加二的R6由b25直接强迫；C49一旦闭合，H49的B0自动空。 |
| [D7批量复制与临界横截](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_BATCH_CLONING_OBSTRUCTIONS_AND_CRITICAL_TRANSVERSAL_TEST_20261027.md>) | 精确down-clone判据和整族冻结；全类目标仍开。 |
| [D7全局临界端点与完整决定](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_GLOBAL_CRITICAL_ENDPOINTS_AND_COMPLETE_DECISION_20261027.md>) | 端点后缀与非末端替换；完整30点决定超时。 |
| [临界满核与端点校准](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_CRITICAL_FULL_CORE_EQUALITY_AND_ENDPOINT_CALIBRATION_20261027.md>) | 完整25核允许两条分离R5加右根；内部条件不迫损失。 |
| [共同满核扩张与H49核心](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_JOINT_EXTENSIONS_AND_H49_COMMON_CORE_20261027.md>) | 完整D26为Y25+a，a同时入出R6、τ1/α25、Y内e=m=2；单外根机制已被反例否定。另有H49同一S24供应。 |
| [D7扩张与共同语义桥](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_GLOBAL_EXCHANGE_AND_BALANCED49_SEMANTIC_BRIDGE_20261027.md>) | E5/E6完整N30分支均超时未决；S24旧源不能再收费。 |
| [全缺额框架与Joint定理](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_GLOBAL_DEFICIT_FRAME_AND_JOINT_THEOREM_20261027.md>) | Joint17重放PASS、全类手写迁移及through缺额；Closure仍缺实际绑定。 |
| [全类残余与不交R6反例](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ALL_CLASS_RESIDUAL_AUDIT_AND_DISJOINT_R6_COUNTEREXAMPLE_20261027.md>) | 完整D12有两条不交R6；否定两两相交路线。 |
| [保端点扩张与R26联合预算](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_ENDPOINT_PRESERVING_EXTENSION_AND_R26_JOINT_BUDGET_20261027.md>) | 实际端点扩张条件与同一H的共同预算；无严格全局下降。 |
| [空锁普适与操作边界](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_EMPTY_LOCK_UNIVERSALITY_AND_OPERATION_LIMITS_20261028.md>) | 任意D_n均可嵌入单点H的空锁canonical母体；实际分块判据。 |

**10. 来源与审计范围**

承重来源与本轮增量：

- [旧综合：RESEARCH_SYNTHESIS_N7_20261028.md](<D:/科研/math agent/erdos-szekeres-sat-main/RESEARCH_SYNTHESIS_N7_20261028.md>)。
- [R6：边界覆盖增广与766传播](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R6_OVERLAP_TWO_AND_766_TRANSFER.md>)。
- [R7：实际H–R分解与残余横截](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md>)。
- [R20：根归约与全局证明架构](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>)及[R20 novelty comparison](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/R20_NOVELTY_COMPARISON_20261023.md>)。
- [统一尾区间](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_UNIFORM_TAIL_INTERVAL_STABILITY_20261028.md>)、[最优交叠](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_OPTIMAL_OVERLAP_EXCHANGE_AND_CUT_INTERFACES_20261028.md>)、[lex覆盖与联合成本](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LEX_OPTIMAL_COVERS_AND_COUPLED_PARTITION_COST_20261028.md>)、[近容量相容性与双向重分块](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_NEAR_CAPACITY_COMPATIBILITY_AND_BIDIRECTIONAL_REPARTITION_20261028.md>)。
- [C8人工接受](<D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md>)；b25接受范围见本文第1段。
- [Joint17原始结果](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/joint17/result.json>)、[Closure规则结果](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/closure/result.json>)及[Closure来源获取停止回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_global_proof_completion_20261027/closure_acquisition/abort_receipt.json>)。
- 最新三套有限核查：[尾区间result](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_tail_interval_stability_20261028/result.json>)、[最优交叠result](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_optimal_overlap_20261028/result.json>)、near-capacity的[MAIN result](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_near_capacity_20261028/main_result.json>)与[竞争result](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_near_capacity_20261028/coupled_result.json>)；另列[lex未运行回执](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_lex_coupled_20261028/EXECUTION_UNAVAILABLE.md>)。

外部a16可引用[Baek官方形式化仓库](https://github.com/jcpaik/erdos-tuza-valtr)。本轮搜索结果返回作者README，主会话读取，其中E(n,4,n)≤binom(n−1,2)+2为forcing口径；最大避免减1，n7为16，组合模型范围仍按本地引用。其他外部原文直连本轮503，未据此认证最新外部纪录或文献新颖性。

独立审核范围：[.aris/README.md](<D:/科研/math agent/erdos-szekeres-sat-main/.aris/README.md>)原文“Both project MCP routes disabled; review-runtime activated=false.”；[research-review技能](<D:/科研/math agent/erdos-szekeres-sat-main/.agents/skills/research-review/SKILL.md>)要求唯一Claude路由且不可回退，原文“No silent model/effort/provider fallback.”，所以本次只完成主会话策略审计，未产生外部review、未提升数学接受状态。本次没有求解/科学实验/证明重放，也没有改旧稿、任务状态、接受、证书或运行。
