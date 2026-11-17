# N(m,r,s) 原件事实索引（截至2026-11-17）

> 导航（2026-11-17 15:29，新加坡时间）：本索引为当日较早快照；跨参数现用数字与后续证据请查[当日交接总稿](NMRS_CLAIMS_HANDOFF_20261117.md)。

本页只为主会话的综合和路线审核定位已有证据，不作独立评审、不提出新路线、不新运行研究代码／solver／checker，不改变接受状态。检索范围为现用10-19任务、其引用的根目录综合及 `reports/n7*`、`reports/n78*`、`reports/n79-overlap-20261116` 的现存原件。源稿所说“PROVABLE AS STATED”是作者相对于进口的候选声明，不是本页的独立认可。wiki OFF，未提交。

## 1. 当前数值及单位先对齐

完整有序rank-3 signotope的每个递增三元组完整染色；四点packet至多变色一次。$N_{\rm sig}(m,r,s)$ 是禁蓝$r$点路、红$s$点路及weak $m$的最大避免人口。路径长度计实际顶点；weak使用同一对实际首末点的异色路，长度和至少$m+2$。定义不另加内部不交条款，但packet使单色路径对子序列遗传：若两路还共一内点，则由共同首点、该内点、共同末点组成的同一三元组须同时两色，矛盾。因此在此模型内，两路内点自动不交。以下三位参数是这个定义的缩写，绝不把第三个数字认作几何阈值。

| 当前对象 | 已记录的较强工作上界 | 原件与范围 |
| --- | ---: | --- |
| 747／756／757／766／767／777 | 16／25／39／49／75／76 | [11/16原件对照§1](N7_STRATEGY_PRIMARY_INDEX_20261116.md)；757的39回[owner正面原稿§7.7](../../../../reports/n7-owner-intervals-20261116/PROOF.md)，Q75回[替锁原稿§§1—4](N7_LOCK_REPLACEMENT_COMMON_ROOT_EXCLUSION_AND_7576_BOUND_20261103.md) |
| 8：$C_8,D_8,Q_8,F_8$ | 193／124／317／318 | [循环迁移原稿§§1—8](../../../../reports/n79-overlap-20261116/EIGHT-CYCLE-TRANSFER.md)，公开有限数据实际重放＋新signotope桥；仍未独立接受 |
| 8：自主解析备用线 | 198／126／324／325 | [CASCADE-63§1](../../../../reports/n79-overlap-20261116/CASCADE-63.md)、[EIGHT-LAST§10](../../../../reports/n79-overlap-20261116/EIGHT-LAST.md)，不调用公开193／124有限树 |
| 9：$C_9,D_9,Q_9,F_9$ | 688／458／1146／1147 | [原生证书RESULTS：Final working upper bounds](../../../../reports/n79-overlap-20261116/direct-cycle-lp/RESULTS.md)，有限整数证书已另程序精确重建PASS，全链仍未外审接受 |
| 平面强迫阈值工作推论 | $ES(7)\le77$、$ES(8)\le319$、$ES(9)\le1148$ | 前两层人口及合法chart、几何包含、强迫阈值加一共同承担；8自主备用阈值326。参[大参数现用登记§§1—3](../../../../reports/n79-overlap-20261116/LARGER-PARAMETER-BOUNDS.md) |

此处 $C_m=N_{\rm sig}(m,m-1,m-1)$、$Q_m=N_{\rm sig}(m,m-1,m)$、$F_m=N_{\rm sig}(m,m,m)$；$D_m$ 是带R7 junction排斥的真实双侧残余，不能改名成普通受限容量。当前三个11/17新稿均明确**767无条件人口工作上界仍75**；尚无一般Q74或Q73。检索到的同目录及所引大参数原件未登记比进口型F8≤318更强的全局888界；不能将局部参数改进当成已降低318。

## 2. 历史阶段：输入收益与结构收益分开

完整27轮定位见[原R1—27综述§3](../../../../RESEARCH_REVIEW_R1_R27_20261026.md)，10/29后归因见[11/13综合§2](N7_STRUCTURAL_SYNTHESIS_AND_ROADMAP_20261113.md)。下表保留原时点，不把旧上界当现用：

| 阶段 | 757／766／767／777 | 原件入口及承重变化 |
| --- | --- | --- |
| 初始R1—R4 | 45／58／103／206 | [R1](RESTART_SETTING_ANALYSIS.md)状态注入；R2—4未带来全局下降 |
| R5 | 44／58／101／201 | [实际覆盖与严格增广](RESET_R5_COVER_AUGMENTATION_CAPACITY.md)，严格减一 |
| R6，短帽28 | 43／56／98／195 | [交叠及766传递](RESET_R6_OVERLAP_TWO_AND_766_TRANSFER.md)，含短帽输入变化 |
| R7 | 43／56／89／177 | [共同见证§§3、8](RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md)，真实不交H—R分解、五点横截 |
| R8，短帽26 | 41／52／83／165 | [统一缺额原稿](RESET_R8_UNIFORM_DEFICIT_AND_JOINT_CAPACITY.md)，输入传播 |
| R20 | 41／52／83／84 | [合法chart§§0.2、2—4](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md)，精确加一 |
| R23，短帽25 | 40／50／80／81 | [R23](RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md)，基座传播 |
| 10/29—11/03 | Q依次79／78／77／76／75 | [10/29综合](../../../../RESEARCH_SYNTHESIS_N7_20261029.md)、[共同中间与加权界](N7_COMMON_MIDDLE_COMPATIBILITY_AND_WEIGHTED_BOUND_20261103.md)、[最终替锁](N7_LOCK_REPLACEMENT_COMMON_ROOT_EXCLUSION_AND_7576_BOUND_20261103.md)；末端正式工作账40／50／75／76 |
| 11/05 | 40／49／75／76 | [balanced严格容量](../../../../reports/n766-strict-capacity-20261105/PROOF.md)实际替末、交替环、安全增广 |
| 11/16 | 39／49／75／76 | [owner§7.7](../../../../reports/n7-owner-intervals-20261116/PROOF.md)全称排40；旧蓝壳条件39不是这个正面证明 |
| 11/17 | 39／49／75／76 | 下节三个新稿推进分叉费用、双向核及57点取等必要结构，未带来无条件Q下降 |

b25的保证必须单列：[C8人工接受原件](../../09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md)覆盖C1—10及所有有限阶的指定756域，保留same-family/provisional及backend／effort不可核说明。25点存在性另由[E21完整颜色](../../../../reports/n756-professor-review-20261027/evidence/E21/color.tsv)和[便携核验](../../../../reports/n756-professor-review-20261027/evidence/E21/portable-verification.json)承担；不附平面坐标／可伸直性。Q75、C49、A39整链仍为未独立接受的工作证明。

## 3. 75／74／73：原件究竟关闭哪一层

### 3.1 普适75与仍待证的费用出口

[替锁原稿§§1—4](N7_LOCK_REPLACEMENT_COMMON_ROOT_EXCLUSION_AND_7576_BOUND_20261103.md)的参数定理为 $Q\le3b$、$F=Q+1\le3b+1$。先用同一个中间匹配得到 $n+w\le3b+1$，再在临界共同增强根层交换右owner／锁、添共根，迫实际红六并回收共同覆盖费用。此稿是**所有767人口**的工作证明，不只是一个固定CNF或单个临界模板。

[11/16策略稿§3](N7_STRATEGY_SYNTHESIS_20261116.md)汇总现有响应：

$$Q\le\min\{3b,C+b+5,A+C-1,\lfloor9A/4\rfloor,\lfloor9C/5\rfloor\}=75$$

（代 $b=25,A=39,C=49$）。A38或C48单独均不改变Q75。$Q\le C+b$尚是待证普适桥，不是既有递推。75点要给实际红六横截≤25才得Q≤74；74点要≤24才得Q≤73。仅关闭75点母体不自动关闭74点。

| 原件 | 已闭范围／当前未闭 |
| --- | --- |
| [D23§9](../../../../reports/n7-owner-intervals-20261116/D23.md) | 一般767的全部红六首末并≤50；75点候选中性窗为25≤d≤28，旧22—28／23—28属阶段值。删后角色和全部幸存路须重算 |
| [EARLY_HALL§§10—12](../../../../reports/n7-owner-intervals-20261116/EARLY_HALL.md) | 同一满20原cut帽且饱和分配h=0（及镜像）有实际24截、条件人口≤73；无d28前提。未饱和帽、h≥3及一般母体未覆盖 |
| [整数横截](../../../../reports/n7-owner-intervals-20261116/INTEGER_COVER.md)、[净收益](../../../../reports/n7-owner-intervals-20261116/MATCHING_GAIN.md)、[退款](../../../../reports/n7-owner-intervals-20261116/PAIR_REFUND.md) | 实际cut帽、全部跨路和删后端图；一般费用≤25／24未证。固定匹配端点互异不等于完整路不交，删旧路后不能沿用原匹配 |
| [四路原稿](N7_74_FOUR_MAXIMUM_RED_PATHS_20261115.md)、[E1](N7_74_E1_COMMON_FIVE_FACE_20261116.md)、[单侧后继](N7_74_ONE_SIDED_ANCHOR_AND_POPULATION_20261116.md) | 四条最大不交红六分支中双方都无完整三点锚路已闭；恰一整侧有锚及至少五路仍开，不是全部四路已排 |
| [H17实际执行报告](../../../../reports/n7-blue-through-seventeen-20261113/execution-20261116-restored-route/REPORT.md) | 25点必要投影VERIFIED SAT；17标点只有4点具局部双向B5，既非17个ambient-through模型，也不排H17。旧SSH失败和冻结未执行描述须与后来这次实际执行分开 |

### 3.2 11/17九点fork：无分叉核64

原件：[NINE_POINT_FORK全文，尤其§§1、8—11](N7_74_NINE_POINT_FORK_CUT_EXCLUSION_20261117.md)。分叉是实际红六与始于其第三点的实际红五的物理支持并；$\lambda$为全部支持的最小物理横截数。作者闭合65点无分叉反设的末两尾型，给候选：

$$|Y|\le64\quad(Y\text{无分叉}),\qquad |X|\le64+\lambda(X).$$

因此有**实际分叉横截≤9**的输入人口≤73；74、75点候选分别须λ≥10、11。一般无分叉核若有k个实际红六第三点，另有

$$|Y|\le49+\min(15,k,32-k).$$

任一实际分叉删集D的补域重算k后，人口≤$49+|D|+\min(15,k,32-k)$。故d=10且k≤14或k≥18、d=11且k≤13或k≥19、d=12且k≤12或k≥20，也属73人口子类。64点无分叉核只余k=15、16、17。这里部分结论是人口反证，**没有统一构造24点红六横截**。

§10的认证前三点并 $H_+$（反向后三点并 $H_-$）若无红四，则可真实选九费分叉横截、人口≤73。一般还有 $|X|\le73+\tau_{R_4}(H_\pm)$。故74候选两侧均含红四，75候选两侧红四族横截数均≥2。此稿未证一般九费／十费分叉横截存在，不给普适Q73。

### 3.3 11/17双向红四：双向无分叉核57

原件：[BIDIRECTIONAL全文，尤其§§1—4及末端范围](N7_74_BIDIRECTIONAL_RED_FOURS_20261117.md)。正、反分叉联合支持横截数为μ，必须在同一物理并中支付；不等于两单向最优费用之和。双向无分叉域所有红六第三点红出秩4、第四点红入秩4；全部中位池里的廉价红四A、C给**实际至多8点红六横截**。因此

$$\tau_{R_6}(X)\le |D|+8,\qquad |X|\le57+|D|,\qquad |X|\le57+\mu(X).$$

μ≤16确实给原域实际≤24点红六横截；74、75候选分别须μ≥17、18。实际16点例原件为[REPORT](../../../../tmp/n7_bidirectional_four_20261117/REPORT.md)与[fixed16_audit](../../../../tmp/n7_bidirectional_four_20261117/fixed16_audit.json)：τ_R6=3、λ+=λ−=2、μ=3，且能选两份连完整认证路径都不交的8点包。这否定无人口限制的“正反红四／完整包必交”，不反驳74点临界版本。它是完整16点767核验，不是74点反例。

### 3.4 11/17 joint57：取等必要结构仍未排空

原件：[JOINT57全文，尤其§§1—3、8—11](N7_74_JOINT57_ORDERED_ANCHORS_20261117.md)。输入**已是57点双向无分叉域Z**。八截取等迫A、C物理不交且各4点，删后同一49点766核V。私人完整中边与packet迫严格A<C、混锚三元组全蓝；同一Hall供给、规范源末各24点、共享小核及交替Hamilton**端图**进一步迫实际中央蓝五。

§8的末端加强包括中央至少两个不同核点供同形蓝五、$(a_2,c_3)$窗口至少7核点；§8.3对**全部实际极端伙伴族**给中央每侧≤6、整族每侧≤10且至少一整侧内收，排“两侧各≥7伙伴”的满八匹配子类。它没有排完整57取等域。

§9不预设57人口，给任意双向无分叉域的真实费用接口：七角色覆盖或满八匹配结构二择；共同两池次序筛选截；任意双阈值实体截。联合先删17点后若可七截，或先删18／19／22点后满足原文相应筛选费用≤6／5／2，均可接原域24截；这些是**删后须逐项满足的条件**，非所有输入的免费结论。

§10读取[联合次序有限复核](../../../../tmp/n7_joint57_order_20261117/REPORT.md)：70个八锚交错原顺序只在必要投影排17、余53 SAT；私人边11种必要端点型排4、余7 SAT，但余7局部无红六，未实现完整外部私人路。不能把它们当57点模型，也不能把投影SAT说成真实见证推论被否定。§11明确一般μ≤16未证、一般24截未证、Q仍75。

## 4. 八参数：完整纸面与公开有限进口分账

后续较强登记为[11/16大参数页§2](../../../../reports/n79-overlap-20261116/LARGER-PARAMETER-BOUNDS.md)，优于11/15综合第一版888≤382、自主旧阶段327—331等。普通子参数如下：

| 848 | 857 | 866 | 858 | 867 | 868 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 22 | 51 | 63 | 66 | 109 | 165 |

逐项原证明入口：[THREE-COLUMN-STRICT§§1、6](../../../../reports/n79-overlap-20261116/THREE-COLUMN-STRICT.md)给857；[FIVE-ACTIVE866§6](../../../../reports/n79-overlap-20261116/FIVE-ACTIVE866.md)给866；[坐标删除§8](../../../../reports/n78-row-compression-20261115/PROOF.md)给858／868；[PROOF§§2—7](../../../../reports/n79-overlap-20261116/PROOF.md)给867；848沿Baek短帽。普通868≤165不能被真实残余D8≤124替换。

自主备用链198＋126→Q324→F325→ES326完整装配在[EIGHT-LAST§10](../../../../reports/n79-overlap-20261116/EIGHT-LAST.md)及[EIGHT-MOVE§§17—18](../../../../reports/n79-overlap-20261116/EIGHT-MOVE.md)。这些稿不用193／124公开大树；“自主”仍保留Baek短帽等基础进口。

进口链193＋124→Q317→F318→ES319，原数学连接为[EIGHT-CYCLE-TRANSFER§§2—6](../../../../reports/n79-overlap-20261116/EIGHT-CYCLE-TRANSFER.md)：新packet桥把经核准循环三元符号接到同端weak8，普通252态、真实残余154态、23个Baek压缩块及完整整数树分别对齐。原件是[octagons.tex](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/paper/octagons.tex)和[证书README](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/certificates/README.md)。

保证有三层，不能合并：

1. [OCTAGON-SOURCE-RECEIPT§§1—3](../../../../reports/n79-overlap-20261116/OCTAGON-SOURCE-RECEIPT.md)：公开原包SHA、manifest及作者封存finite／Lean回执；原Lean几何接口含native evaluation信任，不是kernel-only。
2. [同稿§5](../../../../reports/n79-overlap-20261116/OCTAGON-SOURCE-RECEIPT.md)、[实际replay-receipt](../../../../reports/n79-overlap-20261116/octagon-source-replay/replay-receipt.json)、[finite-result](../../../../reports/n79-overlap-20261116/octagon-source-replay/finite-result.json)：本项目Linux实际重放15文件子包，exit0、PASS，8.538秒，与作者结果除耗时相同；**没有重建Lean**。本页读了实际receipt，不只转述综述。
3. 本项目新signotope packet桥及整链仍未独立审阅接受。有限PASS并不把公开几何319直接变为全抽象模型定理；抽象应用由迁移稿承担。

原生D8深二LP只给130，弱于自主126及进口124，见[RESULTS的停止点](../../../../reports/n79-overlap-20261116/direct-cycle-lp/RESULTS.md)。未定位现成自主≤318或进口后≤317的完整888证明。

## 5. 九参数：最终原生证书取代旧阶段值

| 949 | 958 | 959 | 967 | 968 | 977 | 978 |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 29 | 78 | 96 | 117 | 185 | 222 | 380 |

原件入口依次为[平移行§9.3](../../../../reports/n78-shifted-rows-20261116/PROOF.md)、[三列严格族](../../../../reports/n79-overlap-20261116/THREE-COLUMN-STRICT.md)、同平移行切片、[GRAPH§§2—5](../../../../reports/n79-overlap-20261116/GRAPH.md)、[TRANSFER-NEXT§§5—10](../../../../reports/n79-overlap-20261116/TRANSFER-NEXT.md)、[NINE29](../../../../reports/n79-overlap-20261116/NINE29.md)、[总PROOF§9.3](../../../../reports/n79-overlap-20261116/PROOF.md)。

最终C9≤688、真实D9≤458的原件为[RESULTS首两节](../../../../reports/n79-overlap-20261116/direct-cycle-lp/RESULTS.md)。988在924态中至少236洞；D9在真实允许582态中至少124洞；正权行883／532，$\Lambda=10^6$，精确$D-P$分别235971673／123539361。证书只用普通坐标删除后的原生迹，不用公开循环表、新packet桥、977的222或968的185。

本页直接读了[988 standalone日志](../../../../reports/n79-overlap-20261116/direct-cycle-lp/run-988-d2/standalone-check.log)和[D9 standalone日志](../../../../reports/n79-overlap-20261116/direct-cycle-lp/run-d9-d3/standalone-check.log)，均status=PASS；对应[988紧凑证书](../../../../reports/n79-overlap-20261116/direct-cycle-lp/run-988-d2/compact-certificate.json)、[D9紧凑证书](../../../../reports/n79-overlap-20261116/direct-cycle-lp/run-d9-d3/compact-certificate.json)与[独立标准库checker](../../../../reports/n79-overlap-20261116/direct-cycle-lp/compact_certificate_final.py)。本轮未重跑。实际输入的数学迹引理、坐标删除与R7／R20装配仍由纸面连接，全链无独审接受。

旧成功C9≤691及D9≤463曾给F9≤1155／ES9≤1156，保留在RESULTS后半；1171／1172／1177也属更早阶段。988深三触时限且无证书，不能由Python进程exit0冒称PASS；成功深二688继续有效。D9深三所有47635行的精确分数可行点总缺额123539833/10^6，与整数证书一起只把**该纯LP族的缺额上取整**锁在124，不证明真实容量458可达，也不排新路径条件或整数分支。公开977特定矩阵LP值28同样不推出221人口界。

## 6. 一般公式与更高参数：可调用入口

以下均沿原稿条件及工作证明状态，本页不新推导，也不宣称公开最优。

| 公式／参数域 | 原件与限制 |
| --- | --- |
| $N(m,r,s)=\binom{r+s-4}{r-2}$，$2\le r,s\le m,r+s\le m+3$ | [R12§5](RESET_R12_COMMON_REALIZABILITY_AND_UNIFORM_DEFICIT.md)、[11/16策略§1](N7_STRATEGY_SYNTHESIS_20261116.md)：weak自动区，上下界相合 |
| 普通状态目录 $U_m(a,b)\le\binom{a+b}a$ | [R1§1](RESTART_SETTING_ANALYSIS.md)：实际末对标签注入，不是任意占态可实现 |
| $N(m,r,m)\le N(m,r-1,m)+N(m,r,m-1)-1$，$m\ge4,4\le r\le m$ | [R5](RESET_R5_COVER_AUGMENTATION_CAPACITY.md)、[R6](RESET_R6_OVERLAP_TWO_AND_766_TRANSFER.md)：同一实际覆盖的严格性 |
| $F_m=Q_m+1$，$m\ge4$；$Q_m\le C_m+D_m$ | [R20§0.2及§§2—4](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md)、[R7§8.4](RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md)；D保持真实junction条件 |
| $U_m(a,b)\le\min\{\lfloor(a+b)U_m(a,b-1)/b\rfloor,\lfloor(a+b)U_m(a-1,b)/a\rfloor\}$ | [坐标删除§7](../../../../reports/n78-row-compression-20261115/PROOF.md)：真实切片逐一对应 |
| balanced $c_p\le2b_p-1$，$p\ge4$ | [严格容量PROOF](../../../../reports/n766-strict-capacity-20261105/PROOF.md)：实际替末、安全增广、端图交替环 |
| $N(m,4,m)\le\binom{m-1}2+1$（现用m≥8） | [大参数登记§4.1](../../../../reports/n79-overlap-20261116/LARGER-PARAMETER-BOUNDS.md)记录Baek v2 Thm2.7已核进口；m=8／9／10／11／12为22／29／37／46／56 |
| 三列 $N(m,5,m-1)\le\binom m3-(m-3)$，m≥8 | [THREE-COLUMN-STRICT式(1)](../../../../reports/n79-overlap-20261116/THREE-COLUMN-STRICT.md)，后续平移加强见下文 |
| 四列 $N(m,6,m-2)\le\binom m4-\lfloor(m-3)^2/4\rfloor$，m≥8；m≥12再减1 | [FAMILY式(2)](../../../../reports/n79-overlap-20261116/FAMILY.md)、[STRICT-FAMILY4式(1)](../../../../reports/n79-overlap-20261116/STRICT-FAMILY4.md)，特例须与后续取较强 |
| $N(m,a+2,b+2)\le\binom La-\left\lceil(L-m+1)\binom{L-2}{a-1}/\max(a,b)\right\rceil$，a,b≥2，L=a+b≥m≥4 | [平移行§4.4](../../../../reports/n78-shifted-rows-20261116/PROOF.md)，不等于全参数精确公式 |
| $|X|\le L+(m+1)\nu_{\rm split}$，$L=\sum_{j=m-r+2}^{s}\binom{m-2}{j-2}$ | [11/16策略§5](N7_STRATEGY_SYNTHESIS_20261116.md)、[11/15综合§5](N7_STRUCTURAL_SYNTHESIS_AND_PRIORITIES_20261115.md)：Baek–Balko split-free进口＋最大不交支持并；767的ν≤5未证 |

最新三列通式在[TRANSLATED-PATHS§5.3式(7g)](../../../../reports/n79-overlap-20261116/TRANSLATED-PATHS.md)。令$n=m-2,b=m-3,p_0=\lfloor n/4\rfloor$、$f(p)=\lfloor(1+\sqrt{1+24p})/2\rfloor$、$P_*=\max\{p_0,\lceil\lfloor(b-2)^2/4\rfloor/3\rceil\}$，则

$$N(m,5,m-1)\le\binom m3-\max\{n-1,n+p_0-4,n+P_*-f(P_*)\}.$$

m=12另取特例210。四列m≥14加强在同稿§6式(8)：令$g=\lfloor(m-3)^2/4\rfloor$，$c_n=n+2$（n偶）或n（n奇），$P_4=\max\{\lfloor n/5\rfloor,\lceil3\binom{n-3}3/40\rceil\}$，有

$$N(m,6,m-2)\le\binom m4-g-P_4+\lfloor12P_4/c_n\rfloor.$$

同稿§§1—5.2给a,b≥3、m=a+b的非蓝洞 $p\ge\lfloor(m-2)/(a+1)\rfloor$，及在所列大b条件下的组合装箱加强；三、四列优先使用已连接普通行的强式。三列、四列缺额主项分别$n^2/12-O(n)$、$n^3/80-O(n^2)$，不宣称最优常数。

| 更高具体参数 | 现用工作上界 | 原件 |
| --- | ---: | --- |
| (10,5,9)／(11,5,10) | 113／157 | THREE-COLUMN-STRICT式(1)代入 |
| (10,6,8)／(11,6,9) | 198／314 | [FAMILY§8](../../../../reports/n79-overlap-20261116/FAMILY.md) |
| (10,7,7) | 237 | [TEN-NEXT§§1—5](../../../../reports/n79-overlap-20261116/TEN-NEXT.md)；不是ES(10)≤238 |
| (12,5,11)／(18,5,17)／(26,5,25) | 210／795／2554 | TRANSLATED-PATHS§§5.3—5.4，替代211／801／2577及2574 |
| (12,6,10)／(13,6,11)／(14,6,12) | 474／689／970 | STRICT-FAMILY4§6，12参数替代475 |
| (20,6,18) | 4759 | TRANSLATED-PATHS§6，替代4772 |

没有在这些现用原件中定位到已装配的m≥10新平面ES数表／统一显式改进公式；通用出口仍为 $ES(m)\le C_m+D_m+2$，须提供同参数真实C、D输入。

## 7. 版本冲突、失效描述与索引使用顺序

* [11/15 N7／N8综合](N7_N8_SYNTHESIS_20261115.md)头已指向11/16登记；其A40、857≤53、866≤67、888≤382及“未重放”是历史快照，不能覆盖A39、857≤51、866≤63及后来LinuxPASS。旧数字仍可用于说明演进。
* 同目录很多757稿处理的是已由owner正面证明排除的40点等号层；“39未闭”的旧末段须服从[SEVEN-39-SOURCE](../../../../reports/n79-overlap-20261116/SEVEN-39-SOURCE.md)及owner§7.7。39点层本身无实际构造、≤38未证。
* 旧STAGE_SUMMARY、README、幻灯片及较早综合只负责导航和阶段史。7的当前源优先11/16原件对照加11/17三稿；8、9及更高参数优先LARGER-PARAMETER-BOUNDS的最终章节链接，再读真正原证明／receipt。
* 11/17的64／57是**无分叉受限核人口**，不是767无条件上界；标题“74”标目标输入，标题“九费闭合”不表示一般九费横截已存在。joint57只给必要结构及条件实际费用。
* author归档Lean PASS、本项目finite PASS、新抽象桥、本项目原生整数certificate PASS、独立全链接受五者分列。当前相关独立深审失败／零读取回执不提供数学意见，不能登记审阅通过。

本页新增的只有资料索引。原件部分为全文、部分按明确章节及最终段落定位，不声称对所有推导作逐行复核。没有改旧任务入口、证明、封存CNF／proof、求解器、运行或人工接受记录。
