# 截至2026-10-27的 N_sig(7,r,s) 结构研究综合与推进路线

日期：2026-10-27。范围：本地可检索材料中的 RESET-R1—R27、10月26—27日全部十份 BALANCED49／D7 隔离记录、最新 b25 人工验收及可读原始回执；不声称穷尽外界文献。历史主线入口停在R27，最新科研状态须以随后隔离稿更新。本文由主会话综合判断，指定 Sol 文档执行者忠实整理；不是逐条证明认证。独立 Claude 调用失败，状态 `REVIEW_UNAVAILABLE`，没有审稿正文或完成 threadId，不重试、不升级接受。新综合、路线判断和未验收结构稿均保持 unreviewed/unaccepted；b25 的既有人工接受另列。

**判断：研究已有明显局部优化倾向，但整条路线仍有价值。** 状态注入、边界增广、残余分拆、根归约都提供了可传播骨架。瓶颈已经转为同一母配置的联合可实现性、几项取等能否同时发生，而非继续增加局部状态。用户提出的目标链适合作为骨架；下一步应先写参数定理及其全量词入口，再代入16、25。本文只提出计划，不实施新科学工作，不重启旧任务。

## 1. 定义、证据等级与可用基例

`N_sig(n,r,s)` 是完整 ordered rank-3 signotope 中同时避免蓝路径 B_r、红路径 R_s、weak n 的**最大避免规模**，不是 forcing threshold。四元 packet 至多变色一次；路径长度按顶点数；weak 的两条异色路径共享实际左右端，长度和为 n+2。几何与 signotope 结论、上界与构造存在、主会话稿与正式接受必须分开。

记 a、b 分别为 N_sig(7,4,7)、N_sig(7,5,6) 的有效上界，当前取 a=16、b=25；C=N_sig(7,6,6)、Q=N_sig(7,6,7) 保留为实际容量。a=16来自 [Baek Theorem 2.7][baek]，其结论适用于更广的完整有序二染色配置。b=25来自 [charging 定理][charging] 与 [C8人工验收][c8]：2026-10-26 C8接受后，C1…C10全部正式人工接受，审查 assurance 仍为 same-family/provisional。上界验收本身既不给25点存在，也不给精确等号；已有实际25构造记录须另引构造证据。

D 表示 D7 残余容量，模型为 no B5／weak7，并要求内部 `EndR5∩SrcB4=∅`。它带额外 junction 条件，不能当作 N_sig(7,5,7)。普通状态基准25／26／30／31／32也不是全体模型的上界。文献核对还包括 [SoCG2025第3节 signotope、第4节可分集合][socg]；[Schroeder2026 V1发布页][schroeder]自称几何 ES7≤81，是发布者预印本主张，非外部同行审查，更不能充当本项目 C49 已接受的证据。

Src／End均指指定模型内部实际k链的起／终点。在canonical X=H⊔R中，H属balanced类、R属D7；W是ambient实际R6从H出发而落在R的终点集合。E是R内部全部R6终点，E5／E6指|E|=5／6；临界R30中取相应五点最小横截T，Y=R\T。

## 2. 已有结构骨架：先参数，后数值

状态注入和 charging 给精确记账 `M=O+e−m`，其中

\[
O(n,r,s)=\sum_{j=n-s}^{r-2}\binom{n-2}{j},\qquad
\max(r,s)\le n\le r+s-2.
\]

[R5][r5]／[R6][r6] 的一单位增广在 n≥4、4≤r≤n 的边界给

\[
N_{\rm sig}(n,r,n)\le N_{\rm sig}(n,r-1,n)+N_{\rm sig}(n,r,n-1)-1.
\]

它不能直接套给766。[R7][r7] 的平衡分割给 C≤2b，三链与 canonical `X=H⊔R` 给 Q≤C+D，五点横截给 D≤b+5。其残余域强于一般757，正是这一步的价值。[R20][r20] 通过合法径向 chart 和删／补根给 n≥4 时

\[
N_{\rm sig}(n,n,n)=N_{\rm sig}(n,n-1,n)+1.
\]

这是现有未独立接受稿，不称文献新发现。因而当前结构草稿链为

\[
N_{\rm sig}(7,5,7)\le a+b-1,\quad C\le2b,\quad
Q\le C+b+5,\quad N_{\rm sig}(7,7,7)=Q+1.
\]

代入16／25得40／50／80／81；这些含未接受结构依赖的数字不能与已接受 b25 混写。几何 forcing≤N_sig(7,7,7)+1=Q+2，所以当前草稿对应82；C49闭合后对应81，再有一单位净缺额才对应80。

## 3. 历史贡献与局部优化审计

| 阶段 | 实质贡献与边界 |
|---|---|
| 前置756 charging | 解决基例容量，为后续参数传播提供输入。 |
| RESET-R1—4 | 建立 D/U双向、理想区间、共同端点覆盖；未得全局改善。 |
| R5／6 | 首次可兑现−1，推广到一般n边界递推；766不在直接适用域。 |
| R7 | 引入带 junction 的残余D及+5，强于以一般757处理残余。 |
| R8—19 | 稳定性、owner、terminal、交换、递归目录及反例积累；无新统一正缺额。 |
| R20 | 根归约把旧777粗递推换为Q+1，局部框架大幅下降；非自动文献原创。 |
| R21—27 | 全ambient供应、任意满核、q／m整类排除、proper cut46／模块30界；新增全局收益0。R23数值变化是b26→25经旧公式传播。 |
| 10月26—27日 | balanced49共同语义、prefix固定表、Joint17绑定、Through14→U13连接；D7的E5／E6、完整反例及冻结构造帮助止损，尚无C49、D29、Q79等新无条件结论。 |

六类重复倾向应被明确识别：条件越分越细却没有进入定理；按路径／尾巴次数计费却遗漏共享；把取等恒等式当严格收益；小反例否定弱接口后仅继续增加局部条件；固定模板／clone已到天花板仍微调；把外部b更新掩盖成结构新收益。

反证资产足以说明风险：最小横截τ不具 matroid 基交换；完整26点单外根反例有τ1、Y25且e=m=2；满核分离两R5反例有e=m=10，否定“缺失即净亏”。R11合法clone冻结于τ2，公开D26冻结于τ1且无合法非空clone后继。H49／B0非空的共同S24／F25里，路径第二点已在S，新的source收费为0；7点canonical H5／R2真实共享同一H尾，否定通用供应单射。这些小例并未否定H49／R30临界命题。正确机制仍须完整经过：entry全覆盖→同一X真实操作→不重复预算→严格净差→全域传播。

## 4. 最新证据：已有连接与尚缺两条链

最新主源是 [COMMON_ASSIGNMENT][common]，较早“prefix没取得／必须四份证书”说法已经过时。

- **Through14。** 任意 no R6／B6／weak7 中 t=|SrcR5∩EndR5|≤13，是新研究结论，未审／未接受。[原始绑定][through] 对5077行有序literal检查PASS，接到同一CNF的历史strict-RUP回执；不是本轮新proof重放，也不能单独登记C容量下降。
- **Joint17。** 对假想balanced50的t≤8，59479行共同语义／公式绑定已完成（[回执][joint]）；同一公式的完整proof成功检查仍缺，不能据绑定PASS消去分支。
- **Closure与prefix。** 9≤t≤13须接实际Closure CNF及证书。129个prefix模式、3198规则检查已完成（[回执][prefix]）。190932规则检查整体 **FAIL**：控制程序预期sourceAttain行，而表内无该行，导致 `KeyError`（[回执][closure]）。不能把完成全表统计改报整体PASS；实际CNF／证明未接通。
- **依赖削减。** 固定表internalBound为0行，直接固定CNF路线可删Terminal20依赖，但须最终实际CNF绑定确认；完整原Lean Model仍保留相应字段义务。
- **D7判定。** 完整N30的E5／E6各180秒均为 `TIMEOUT_UNDECIDED`（[原始执行报告][endpoint]）；旧N30及n18τ5仍未决。超时不支持命题真伪，不建议在命题未变时仅续时。

## 5. 统一审计式与四个方向

以下只是已有分解的精确整理，不计作新定理进展。同一canonical X=H⊔R，取有效C上界c，令τ为最小R6横截数，α=max R6-free实际子集规模=|R|−τ≤b，则

\[
c+b+5-|X|=(c-|H|)+(b-\alpha)+(5-\tau).
\]

三项非负，真正目标是在任意X强制其和≥1。用c50排H50／R30只将80降79；c49先闭合后，再排H49／R30才将79降78，同一缺额不能计两次。

### P0：先闭合平衡满核不能共同实现

目标形态是参数式 C≤2b−1，b25即49；现有17／14／25有限证书路线专用于b=25，不暗示已证明任意n或可机械缩放的通用−1定理。由source／end四集合取等进入同一Z的through人口t，再穷尽 t≤8、9≤t≤13、t≥14 三分支；每个分支须从同一assignment导出矛盾，不从固定“50”算式开始。现有t≥14已连接；先完成Joint17证书链及Closure实际CNF／证书链，无需重开大CNF搜索。固定表路线已不必把Terminal20列为必要前置。这是最希望最快得到一步全局改善的方向，条件收益40／49／79／80；不自动代表原创或接受。下列P1／P2／P3均为未证候选。

### P1：共同极值禁嵌入，作为主数学方向

在c=2b−1后，证明不存在同一canonical X满足 |H|=c、|R|=b+5。C49会自动排H50，并迫H49时 `B0={r:H+r无R6}` 为空；不再主攻H49／B0非空。真目标是将H49的一单位内部预算、同一R30的Y25／T5全部私人及多外点路径、跨H／R真实供应合起来，推出混合禁形或严格真实交换。

入口W为空／单点，R末端人口E5／E6，四大实际分支必须全覆盖；两色预算不机械相加。若推导移除H49或R30仍成立，且没有新容量后果，应降为准备工具。成功才给 Q≤c+b+4=78、N777≤79、几何forcing≤80。

### P2：残余独立稳定性，作为竞争路线

目标 `τ6(R)=5⇒α6(R)≤b−1`；τ≤4时已有α≤b，故D≤b+4=29。它比普遍τ≤4弱，只排“τ5＋满核”共同取等，更适合当前问题。完整入口R30给E5／E6及同一个Y25／T5；所有A⊂T均有α(Y∪A)=25、τ=|A|。这只是临界刚性描述，不是新进展。须保全多外点R6和全部e=m=k、k=0…10。

最新命题A指出：任意安全满Y25及合法外点a、b，对每个y∈Y，26点 `(Y−y)+a+b` 都有R6，故这些R6在Y中的公共交为空。“删一加二”不能再当独立局部入口；须从更强全五外点条件迫出矛盾。不把小阶τ5判定当完整D29。单独成功给Q79／N77780，与C49合并给Q78／N77779。若发现完整R30 SAT并核验，独立D29路线失败，应回联合H／R，而非无限加条件。

### P3：低配额探索不可分块结构

[R12][r12] 在实际递归统一切分给精确O及望远镜式

\[
M-O_{\rm target}=\sum_{\rm leaf}(e_L-m_L)-\sum_{\rm internal}d_Y
-(O_{\rm target}-\Phi(X)),\quad d_Y\ge0.
\]

正超额只能在不可分叶；仅把未知容量改名prime不足以推进。[R26][r26] 的proper rootfan cut要求两侧≥2，AAB色不依右点、ABB色不依左点；其界 U=max(2a,h+6)，h为N757有效界，代16／40得46。

一个本次新拟、尚无证据的高风险候选是：任意假想balanced2b，删≤t点后强制出现这种cut；若U+t≤2b−1便排满2b。b25时t≤3可达49，t4无净收益。更广目标是近极值不可分块的强制禁形／分类。当前没有一般进入机制，故只是可选候选，不当最有把握主线，不推荐立即开实验，也不继续围绕固定16／30模板微调。

## 6. 投入定位、条件收益与停止规则

757的a+b−1=40是支线终点。当前最强 Q≤C+b+5 不经过N757，单独40降39不会自动改善Q／777；选择该线须先给把改善传到C／D的桥接定理。777等式已使其无独立必要工作，优先改善Q。也不建议再压b25：基例上界问题已解决且有实际25构造记录；精确存在仍要另引构造，不由验收推出。

| 前提／候选成功条件 | Q上界 | N777上界 |
|---|---:|---:|
| 当前草稿c50、D30 | 80 | 81 |
| 仅c49，或仅D29 | 79 | 80 |
| 仅R30⇒H≤48，仍用c50 | 79 | 80 |
| c49且D29，或c49后排剩余H49／R30 | 78 | 79 |

表中N757均保持40；它们是依赖相应结构稿和候选完成的条件传播，不是新接受记录。节奏上先补P0两条证据链，P1主数学、P2竞争、P3低配额。每轮只追一个全量词候选：先列已知反例，再写entry、具体净项、可能补偿、传播出口。若没有新严格式、完整反例或穷尽分类，不只换参数继续；不赋概率／工时，不续跑旧jobs。

## 7. 原始来源与本次失败review

主线定位：[初始基准][baseline]、[R5][r5]、[R6][r6]、[R7][r7]、[R8][r8]、[R12][r12]、[R20][r20]、[R23][r23]、[R26][r26]、[R27][r27]。历史按实质贡献综合，未逐条重新验收。

十份日期记录全部纳入，最新以COMMON_ASSIGNMENT为准：

| 日期 | 原始记录 |
|---|---|
| 10-26 | [TRANSFER][b1]；[SATURATED_Y][b2]；[SHARED_TAILS][b3]；[PAIR_RANKS][b4] |
| 10-27 | [D7_CRITICAL_ENDPOINTS][d1]；[D7_BATCH_CLONING][d2]；[D7_FULL_CORE][d3]；[D7_JOINT_EXTENSIONS][d4]；[D7_GLOBAL_EXCHANGE][d5]；[COMMON_ASSIGNMENT][common] |

本次review仅一次：jobId `0927b8f3b06e42d0abe1ba8cd6ee2303`，18:04:56发起、18:05:00失败（+08:00）。请求semantic Claude fable 5.1、wire `claude-fable-5-1-reversed`、配置deep/max、工具Read／Grep／Glob；实际backend与effort不可核实，返回model为null。`review_independence=requested-cross-family-unverified`、`acceptance_status=unreviewed`。完整 [request][review-request]、[原始start／status响应][review-response]、[run meta][review-run]、[call meta][review-meta] 已隔离保存；[sanitized receipt][receipt] 不等于成功审稿。没有独立审稿结论可供接受，本文判断不能替代它。

[baek]: https://arxiv.org/pdf/2206.04260
[socg]: https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/html/LIPIcs.SoCG.2025.13/LIPIcs.SoCG.2025.13.html
[schroeder]: https://michaelschroeder.ai/research/ErdosSzekeres/companion
[charging]: <D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/cardinality-layer-theorem.md>
[c8]: <D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md>
[baseline]: <D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/INITIAL_BASELINE.md>
[r5]: <D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R5_COVER_AUGMENTATION_CAPACITY.md>
[r6]: <D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R6_OVERLAP_TWO_AND_766_TRANSFER.md>
[r7]: <D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md>
[r8]: <D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R8_UNIFORM_DEFICIT_AND_JOINT_CAPACITY.md>
[r12]: <D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R12_COMMON_REALIZABILITY_AND_UNIFORM_DEFICIT.md>
[r20]: <D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md>
[r23]: <D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md>
[r26]: <D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R26_GLOBAL_BREAKTHROUGHS_AND_EXTREMAL_COUNTERTESTS.md>
[r27]: <D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R27_GLOBAL_REALIZABILITY_AND_SATURATED_CORE_COUNTERTESTS.md>
[b1]: <D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/BALANCED49_TRANSFER_AND_JOINT_DEFICIT_20261026.md>
[b2]: <D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/BALANCED49_SATURATED_Y_EXCHANGES_AND_TRANSVERSAL_OBSTRUCTIONS_20261026.md>
[b3]: <D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/BALANCED49_CONTINUATION_SHARED_TAILS_AND_TERMINAL_BARRIERS_20261026.md>
[b4]: <D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/BALANCED49_ALL_WITNESS_PAIR_RANKS_AND_FORK_COUNTEREXAMPLES_20261026.md>
[d1]: <D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_GLOBAL_CRITICAL_ENDPOINTS_AND_COMPLETE_DECISION_20261027.md>
[d2]: <D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_BATCH_CLONING_OBSTRUCTIONS_AND_CRITICAL_TRANSVERSAL_TEST_20261027.md>
[d3]: <D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_CRITICAL_FULL_CORE_EQUALITY_AND_ENDPOINT_CALIBRATION_20261027.md>
[d4]: <D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_JOINT_EXTENSIONS_AND_H49_COMMON_CORE_20261027.md>
[d5]: <D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/D7_GLOBAL_EXCHANGE_AND_BALANCED49_SEMANTIC_BRIDGE_20261027.md>
[common]: <D:/科研/math agent/erdos-szekeres-sat-main/.trellis/tasks/10-19-nr7-structure-capacity/research/BALANCED49_COMMON_ASSIGNMENT_AND_REMAINING_H49_BRANCH_20261027.md>
[through]: <D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_remaining_hr_20261027/through14_binding/result.json>
[joint]: <D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_remaining_hr_20261027/joint17_binding/result.json>
[closure]: <D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_remaining_hr_20261027/closure_rules/result.json>
[prefix]: <D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_remaining_hr_20261027/prefix_check/result.json>
[endpoint]: <D:/科研/math agent/erdos-szekeres-sat-main/tmp/d7_global_exchange_semantics_20261027/r30_endpoint/EXECUTION_REPORT.md>
[review-request]: <D:/科研/math agent/erdos-szekeres-sat-main/.aris/traces/research-review/2026-10-27_n7_structural_synthesis/001-structural-review.request.json>
[review-response]: <D:/科研/math agent/erdos-szekeres-sat-main/.aris/traces/research-review/2026-10-27_n7_structural_synthesis/001-structural-review.response.md>
[review-run]: <D:/科研/math agent/erdos-szekeres-sat-main/.aris/traces/research-review/2026-10-27_n7_structural_synthesis/run.meta.json>
[review-meta]: <D:/科研/math agent/erdos-szekeres-sat-main/.aris/traces/research-review/2026-10-27_n7_structural_synthesis/001-structural-review.meta.json>
[receipt]: <D:/科研/math agent/erdos-szekeres-sat-main/.aris/review-state/claude-review-deep/evidence/c78ec113027f496783886d331528d2ad.json>
