<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# N(m,r,s)研究综合与下一轮上界路线

**2026-11-19本轮最新已核更新（只推进m≤10；下文历史正文与假设表保留）：**
平衡C8的人口189已由实际DRAT排除，另写完整几何编译器重建4936085句得到相同
CNF hash，第二实际DRAT也已退出0、唯一VERIFIED；全部来源行、两向复合图和真实
33点校准均已核。稳定入口及两份原日志、收据和hash见
[C8≤188主证](N8_C188_311_20261119.md)。再删全部复合容量与公开cycle行的
432183句纯原生/私面式也已独立重建及第二实际DRAT通过，含另验的47063句core。
普通858≤64的[稳定主入口](evidence/n8-d122-common-bridges-20261119/ORDINARY858_64_VERIFIED.md)及
[最终双检收据](../evidence/858/ordinary858-64-final-receipt.json)
已实际本地取回：两次checker0、唯一VERIFIED，完整独立重建CNF hash相同。
原R7同母体分区A为普通866、U为普通858，故真实D8≤57+64=121，得到
**C8≤188、真实D8≤121、Q8≤309、F8≤310；平面ES8≤311**。
相对上一轮F8≤315、ES8≤316分别净降5；C/D/Q/F是最大避免人口，ES是强迫阈值，
不作sharp性、全球优先或外审主张。

上游[普通866≤57](N866_57_GLOBAL_20261119.md)及其
[独立重建与第二回放](evidence/n8-total-deficit-313-20261119/ordinary866-h12-second-replay-20261119/README.md)
仍为真实进口；故普通867≤102。新普通858≤64的
[完整独立第二回放](../evidence/858/near65-independent-v1/second-result.json)
与[原输入数学桥](evidence/n8-d122-common-bridges-20261119/NEAR65_SEMANTIC_BRIDGE.md)
给普通868≤floor(10·64/4)=160。此前
[同母体D8≤122独立证书](N8_D122_312_20261119.md)及普通858≤65的旧证仍封存保留。
[共享物理桥与匹配稿](N8_JOINT_66_58_20261119.md)提供结构背景。
下文190/124/314/315、189/123/313、188/122/311及104/165等为历史版本，现值以上述入口为准。

**结构后继与边界（2026-11-20）：**
[普通866的真实根、统一尾帽与八点结构](N866_ROOTED_FAN_TAIL_20261120.md)和
[精确右延拓Horn闭包及后缀费用](NMRS_RIGHT_EXTENSION_HORN_20261120.md)为现用结构入口。
首七/尾六版08曾有“固定04被排除”的编号命名空间误判，现已
[正式纠正](../SOURCE_MAP.md#excluded-sources)：完整式有显式SAT，
其[全部3031103句的独立完整重建](../SOURCE_MAP.md#excluded-sources)
及[在独立CNF上的全句SAT回放](../SOURCE_MAP.md#excluded-sources)
均实际通过。未启动08重复求解；该SAT只是必要投影，不是57点实际色表，
也没有给普通866≤56。当前普通866已证上界仍是57；上述F8≤310不受此纠正影响。

2026-11-19。本文读取既有核验，把现有原件、实际有限证据与本次指定的数值装配接在一起；恢复应从所链最终章节进入，旧稿中的61、32、4749等阶段数值保留历史意义。本综合未新跑科研程序、solver或服务器任务；独立审阅请求未返回数学意见，封存证据和接受记录未变。

本次除接通普通866≤58到F8≤315的传播，还新增全宽度共同锚点窗口及相邻窗严格余量。对a=5、v=b−1≥8，同一非蓝洞数p、私洞数q满足5p−2q≥81·binom(v,4)/280；与普通行联合给 **N(50,7,47)≤2107453**，比旧命名通式配同一行式多省2155。单窗阶段2107540仍为有效中间界；完整原输入接口、推导与保证见§6，不称公开最优纪录。

## 1. 对象、精确基线与保证

`N(m,r,s)`是完整有序rank-3 signotope中，禁蓝r点路径、红s点路径及weak m的最大避免人口。每个递增四点packet至多一次变色；路径长度计实际顶点。weak要求同一实际首末的异色路径，长度和至少m+2，不另加内部不交假设。记C_m=N(m,m−1,m−1)、Q_m=N(m,m−1,m)、F_m=N(m,m,m)。真实残余D_m还带R7 junction条件，不能换成普通N(m,m−2,m)。[定义与原始状态接口](../../nmrs-20261117/source/reports/n79-overlap-20261116/PROOF.md)

小帽自动区3≤r,s≤m、r+s≤m+3有精确式N=binom(r+s−4,r−2)；r或s为2时退化为1。Baek短帽进口为N(m,4,m)=binom(m−1,2)+1。R12递归join在自动区达到二项式，并给757／766／767／777的真实下界26／30／31／32；抽象构造不自动几何可实现。[构造与基线](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R12_COMMON_REALIZABILITY_AND_UNIFORM_DEFICIT.md)、[文献条件](../../nmrs-20261117/source/reports/n7-progress-talk-20261117/BOUNDS_AUDIT.md)

以下“工作上界”包含未独审解析链；固定有限PASS只承担原绑定公式、支持、运输和算术，不替代原输入桥或外部验收。本轮深审job `0277771fb9e24a0dbf047306d9ff566b`实际CLI exit1、工具读取0、没有数学意见；[脱敏原回执](../SOURCE_MAP.md#excluded-sources)未给独审通过，backend／effort仍不可核。不自动重试，不升级旧b25或全链接受。

| 范围 | 现值或工作上界 | 原件与保证 |
| --- | --- | --- |
| 六参数646／655；Q6／F6 | =11／=14；=15／=16 | [四池稿§3](N866_59_FOUR_POOLS_AND_WEAK6_20261118.md)：Baek及Szekeres–Peters同域17点计算定理；公开枚举本轮未重放。 |
| 七参数747／756 | =16／=25 | Baek进口；756上界沿[C8人工接受](../../nmrs-20261117/source/.trellis/tasks/09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md)，仅限定756域、same-family/provisional；[25点下界色表核验](../../nmrs-20261117/source/reports/n756-professor-review-20261027/evidence/E21/portable-verification.json)。 |
| 757／766／767／777；ES7 | ≤39／49／75／76；≤77 | [owner短证§7.7](../../nmrs-20261117/source/reports/n7-owner-intervals-20261116/PROOF.md)、[balanced严格容量](../../nmrs-20261117/source/reports/n766-strict-capacity-20261105/PROOF.md)、[共同根替锁](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_REPLACEMENT_COMMON_ROOT_EXCLUSION_AND_7576_BOUND_20261103.md)及chart；下界分别26／30／31／32，全链未独审接受。 |
| 848／857／866／858 | =22／≤50／≤58／≤66 | Baek；[857五洞整层纸证](N857_SHARED_ROWS_NEXT.md)；[普通58完整主证](N866_ORDINARY_BOUND_PROOF_20261119.md)及[实际重建与DRAT](../source/reports/n866-ordinary58-20261119/VERIFICATION.md)；858为22的切片推论。857核验程序NOT_RUN。 |
| 867／868 | ≤104／≤165 | 前者为本综合§2从普通58的删除装配；后者沿[坐标删除§8](../../nmrs-20261117/source/reports/n78-row-compression-20261115/PROOF.md)。 |
| C8／真实D8／Q8／F8；ES8 | ≤190／124／314／315；≤316 | 本综合§2解析传播；不同于旧公开有限树迁移193／124／317／318及平面319。新装配未外审接受。 |
| 949／958／959 | =29／≤78／≤96 | Baek；[三列严格族](../../nmrs-20261117/source/reports/n79-overlap-20261116/THREE-COLUMN-STRICT.md)；[平移行§9.3](../../nmrs-20261117/source/reports/n78-shifted-rows-20261116/PROOF.md)。 |
| 967／968／969 | ≤117／≤185／≤264 | [GRAPH](../../nmrs-20261117/source/reports/n79-overlap-20261116/GRAPH.md)、[TRANSFER-NEXT](../../nmrs-20261117/source/reports/n79-overlap-20261116/TRANSFER-NEXT.md)、[已登记列算§6.1](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/NMRS_CLAIMS_HANDOFF_20261117.md)。 |
| 977／978／979 | ≤222／≤380／≤633 | [NINE29](../../nmrs-20261117/source/reports/n79-overlap-20261116/NINE29.md)、普通行与同一[列算入口](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/NMRS_CLAIMS_HANDOFF_20261117.md)。 |
| C9／真实D9／Q9／F9；ES9 | ≤688／458／1146／1147；≤1148 | [原生整数证书RESULTS](../../nmrs-20261117/source/reports/n79-overlap-20261116/direct-cycle-lp/RESULTS.md)：独立标准库支持重建及整数PASS；完整数学链未独审接受。 |

八、九的全小帽自动区和换色项由上述精确式补齐；D8／D9不是普通868／979。平面ES比避免人口再加一，不能从公开几何结果反推任意signotope容量。

| 更大受限参数 | 当前登记上界 | 入口 |
| --- | --- | --- |
| (10,4,10)／(11,4,11)／(12,4,12) | 37／46／56 | Baek公式；[具体参数总账](../../nmrs-20261117/source/reports/n79-overlap-20261116/LARGER-PARAMETER-BOUNDS.md)。 |
| (10,5,9)／(11,5,10)／(12,5,11)／(18,5,17) | 113／157／210／795 | [三列严格族](../../nmrs-20261117/source/reports/n79-overlap-20261116/THREE-COLUMN-STRICT.md)、[平移路径§5](../../nmrs-20261117/source/reports/n79-overlap-20261116/TRANSLATED-PATHS.md)。 |
| (10,6,8)／(11,6,9)；(10,7,7) | 198／314；237 | [FAMILY](../../nmrs-20261117/source/reports/n79-overlap-20261116/FAMILY.md)、[TEN-NEXT](../../nmrs-20261117/source/reports/n79-overlap-20261116/TEN-NEXT.md)。 |
| (12,6,10)／(13,6,11)／(14,6,12) | 474／689／970 | [四列严格族](../../nmrs-20261117/source/reports/n79-overlap-20261116/STRICT-FAMILY4.md)。 |
| (20,6,18)；(26,5,25)／(29,5,28)／(53,5,52) | 4747；2549／3590／23202 | [四列最终§§6—9](NMRS_FOUR_COLUMN_ORDERED_CUT_NEXT.md)、[三列最终§13](NMRS_ORDERED_THREE_COLUMN_STABILITY_NEXT.md)。 |
| (22,5,21)／(245,5,244) | 1506／2416117 | [最新综合§§3.1—3.2](NMRS_GLOBAL_ADVANCE_NEXT.md)，P(18)=24勘误及新批量代入。 |

这些都是受限容量，1077≤237不表示ES10≤238。最新固定族覆盖4749、2553／3594／23213及中间稿；净收益不能跨版本相加。

固定宽度的最强既有通式也应保留。[三列最终§13](NMRS_ORDERED_THREE_COLUMN_STABILITY_NEXT.md)取v=m−4≥4、T=floor((v−1)²/4)，给

$$H\ge\left\lceil T/3+3v/4-8\right\rceil;
\qquad v\ge22:\quad H\ge\left\lceil(T+2v-2)/3\right\rceil.$$

与旧有效洞界取最大，再从binom(m,3)扣除；后式在26／29／53参数给51／64／224洞。前式给H≥m²/12−m/12−O(1)，245参数一次给4973洞。[四列最终§8](NMRS_FOUR_COLUMN_ORDERED_CUT_NEXT.md)的有限13点进口版为

$$H\ge\frac{\tau(56/143)}{24}(m-2)^3-O(m^2),
\qquad\tau(\alpha)=3+4\alpha-\tfrac32\sqrt{3+12\alpha}.$$

其主系数严格强于旧7/429，有限20参数主值为4747。另有可选K_4^(3)密度进口版系数>1/54；没有于本轮重放该进口的证书／Lean，有限4747及上述13点版不依赖它。下文a=5的高度脸对象为K_5^(4)，须与四列K_4^(3)区分。

## 2. 普通58怎样真正传到八参数

[坐标删除§7](../../nmrs-20261117/source/reports/n78-row-compression-20261115/PROOF.md)对同一原输入保留含／避坐标的实际点，保持原顺序、颜色与weak禁制。压缩标签虽不必是重算最长秩，逐色增长仍排掉相应长帽，故人口可用普通子模型上界。每点恰出现在指定数量的切片中，因而

$$U_m(a,b)\le\min\{\lfloor(a+b)U_m(a,b-1)/b\rfloor,
\lfloor(a+b)U_m(a-1,b)/a\rfloor\}.$$

对867的4×5域，九份避坐标切片均为普通866，每点被计五次；故5n≤9·58，得到867≤104。这里不选择九份互不相容的极值见证。

设普通866≤70−t。C8的5×5目录有252态、70条遗传平移行，每行至少三洞，总需求210。两类私有端态各经删除压成866；它们是同一母体内物理状态不交的两份切片，各至少t洞，故私洞P≥2t。内部洞至多服务五行，私洞至多一行，于是

$$210\le5(H_C-P)+P\le5H_C-8t,
\qquad H_C\ge\left\lceil\frac{210+8t}{5}\right\rceil.$$

真实D8的154态宇宙满足10∈W⇒9∈W，按双缺9、10，含9缺10，双含分成70／56／28态；洞数α、β、γ属于同一实际输入。A层是866，α≥t；短帽给γ≥6。两份重叠普通行及九个含坐标短帽切片共同给

$$1498\le79H_D-51\alpha-35\gamma-21u,
\qquad H_D\ge\left\lceil\frac{1708+51t}{79}\right\rceil.$$

还可直接按是否含9分拆：不含9者也不含10，压成866；含9者压成普通858≤66。两部分物理不交并覆盖残余，故D8≤(70−t)+66，等价H_D≥t+18。[原始共同消元](../../nmrs-20261117/source/reports/n79-overlap-20261116/CASCADE-63.md)、[双侧响应§7](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/NMRS_STRUCTURAL_ROADMAP_20261117.md)

取

$$h_C(t)=\left\lceil(210+8t)/5\right\rceil,
\quad h_D(t)=\max\{\lceil(1708+51t)/79\rceil,t+18\},$$
$$C_8\le252-h_C,\quad D_8\le154-h_D,\quad Q_8\le406-h_C-h_D,\quad F_8\le407-h_C-h_D.$$

| t | 普通866 | h_C／h_D | C8／D8 | Q8／F8／ES8 |
| ---: | ---: | ---: | ---: | ---: |
| 12（现有） | 58 | 62／30 | 190／124 | 314／315／316 |
| 13（目标响应） | 57 | 63／31 | 189／123 | 312／313／314 |
| 14（目标响应） | 56 | 65／32 | 187／122 | 309／310／311 |
| 15（目标响应） | 55 | 66／33 | 186／121 | 307／308／309 |

只有首行上游已经获得；后面三行不登记为现值。t14同时消费直接残余分拆，F8出口是310，比现有315再省五；只抄旧单式响应会漏掉这一点。本传播不需193／124两棵公开有限树的数值，但继承删除、普通行、Baek及R7／R20的数学保证。

## 3. 方法系统与已经兑现的结构

[R7](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md)在同一X、同一个pivot及真实长路上分成H与残余，给Q≤C+D；[R20](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md)用合法chart、实际删添根给F=Q+1，再由几何包含得ES≤F+1。固定旧Q≤83时，它把旧F≤165改为84；这项81点收益只记一次，后来b25／匹配收益另算。

实际pair最长秩生成终态理想；若x<y，pair标签属于P(y)\P(x)，故点到理想单射。真实坐标删除、遗传平移行、Hall和共享标签必要式在同一占态图上迫洞；11/19[普通58主证](N866_ORDINARY_BOUND_PROOF_20261119.md)全域预算H≤11的源核、运输、公式和DRAT已核，区别于只排某个mask或固定中央的子查询。[中央全域检查](../source/reports/n866-scalar-grid-20261119/ENCODING_AND_STATUS.md)又结合富色／双序覆盖和真实补全，证明中央容量恰30。

七参数共同匹配、critical取等、post-leaf用的是全部真实替代路径与物理删除集；[标记14点共同返回](N7_MARKED_14_SHARED_RETURN_20261118.md)、[叶付正例](../source/reports/n7-postleaf-examples-20261118/REPORT.md)给可用条件。HKH14真例的ν由3经支付一个真中性点降至1，展示共同路径收益；它无蓝五，没有活动真K供给，不能据此覆盖任意74点。固定宽度路线保留同一洞在高度脸、普通行、自然序窗口上的联合支付，已得4747及三列常数误差式；九参数则由原生迹的加权整数证书，用超载罚项将浮点搜索转成精确236／124洞。

三项方法边界必须继续消费：[全部遗传坐标人口松弛](N7_GENERAL_CAPACITY_NEXT.md)最优恰87，加入主帽75后仍容75态，不是真signotope；[D9全部47635行分数点](../../nmrs-20261117/source/reports/n79-overlap-20261116/direct-cycle-lp/RESULTS.md)锁定同族纯LP上取整124，不锁整个D9；真实36点C30例的Δ=28说明全域中央30已达到，不能继续追无前提C≤29，也不能把它当近临界人口反例。

## 4. 第一优先：同一母体的共同缺额与中央—外端费用

**先试八参数四子域的共同亏损。** 在同一个Q8母体X的R7分拆中，balanced部分两份不交私有866面人口分别为58−d1、58−d2；真实残余的A层、B∪C层人口分别为58−d3、66−e。四项缺额均非负。置d=d1+d2，f(d)=ceil((4d−4)/5)≥0。两私面比§2基线多d洞，普通行共同支付给

$$H_C\ge\lceil(306+4d)/5\rceil=62+f(d),
\quad |R|=124-d3-e,$$
$$\boxed{|X|+1\le315-[f(d)+d3+e].}$$

故要得到F8≤313，只需对全部原输入排除或补偿两类：d3+e=0且d≤2；或d3+e=1且d≤1。补偿也可来自上述计数未捕获的额外balanced洞，不必强迫每个子域各降一。e=0迫B∪C的九个848面都恰22；e=1时九面总短缺仅为9·22−3(66−e)=3，给共同取等／近取等接口。四子域的物理不交不提供跨域共点；新增冲突必须来自同一父母体的点序、pair和路径，不把独立极值相加当作耦合。这个有限共同亏损出口与下面普通56宏观路线并列优先。

**另一独立出口是普通866≤56／55。**

[Schroeder原文的经典受限构造登记](../../nmrs-20261117/source/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/paper/formalization.tex)给平面M_8(6,6)≥50，故其signotope也给普通866真实下界50。现有区间为50≤N(8,6,6)≤58；56／55目标须容纳这份校准，不追不可能的任意小容量。

在同一原普通866输入，以正反态不含22格的实际点定义低池L⁻、L⁺；各≤16，中央C=X\(L⁻∪L⁺)，c=|C|。定义

$$\Delta=(17-|L^-|)+(17-|L^+|)+|L^-\cap L^+|\ge2,
\qquad n=34-\Delta+c.$$

[中央富色原件§1](N866_CENTRAL_RICH_PERMUTATION_NEXT.md)提供这一恒等式。目标普通≤56准确等价于对全部原输入证明c≤22+Δ；≤55对应c≤21+Δ。现有c≤30已自动处理前者Δ≥8、后者Δ≥9，因此下一轮只需分别覆盖Δ=2…7、2…8，不能把旧Δ28校准与这些近临界输入混合。

首选4×4宏观块及其真实外侧宿主兼容性：每块保留原点序、同pair双色三／四臂、中央富色、跨块五路和全部外端供应。要么给出一份能共同承担费用的宿主分配；要么从失败子族提取同一母体的缺额下界。任何Hall方案都须对任意块子族同时控制共同可用物理宿主与净费用，且证明任意原输入进入这些块或补充分支；逐块各选最优宿主再相加不成立。

若采用条件补全，必须保留低Δ和外池规模；[富色核通用六锚补全](../source/reports/n866-scalar-grid-20261119/ENCODING_AND_STATUS.md)只给Δ28，已能把C30真正实现，却没有实现低缺额补全。所有新宏观不等式先过[36点真校准](N866_LARGE_CENTRAL_CALIBRATION_NEXT.md)，再比较是否推出c≤22+Δ／21+Δ；新增局部洞而没有减少全域余口，不算推进。

## 5. 互补路线与明确停止点

**八参数残余与联合取等。** 当前D8≤124若取等，直接分拆迫A层恰58点，即α=12，B∪C恰66点。九个含坐标848面均须恰22点；84态中18枚缺三元组各坐标度恰6，并同时满足原重叠行式、洞度与原pair顺序。先检查这份共同达到性，而非独立拼九个精确面。[858双极端刚性](../../nmrs-20261117/source/reports/n79-overlap-20261116/RESIDUAL.md)。以更新c8=190、d8=124定义δ_C=190−|H|、δ_D=124−|R|，联合目标δ_C+δ_D≥2已在§4具体化为四个原子域的两类低亏损，而非另开一个无选择接口的抽象缺额猜想。

**九参数。** 保留普通688、真实D9≤458；新整数目标为D9至少126洞，即≤456，接现有C9给Q9≤1144、F9≤1145。也可在同一分拆上迫联合多两洞。[共同标口原件§8](NMRS_GLOBAL_STRATEGY_20261118.md)另给|Y|≥131−δ；三条任意预定颜色的物理不交六路只在δ≤1保证。若排掉这两层共同角色，亦给F9≤1145，不能将其扩大到全部δ。停止原47635行纯LP的重复优化；新行需从原输入证明，整数分支需完整覆盖，solver UNKNOWN不作排除。

**七参数。** 既有不同接口取优仍为Q7≤min{75,79,87,87,88}=75。对任意74点767母体找到击中全部实际红六的≤24点物理截，删后至少50点为766，违49，才有Q7≤73、F7≤74。预付F、f=|F|后必须按全部幸存红六重建物理分量C_i（包括孤点）；若各选截T_i，则

$$3|T|=74+2f-\sum_i(|C_i|-3|T_i|).$$

需要共同节省至少2f+2。两临界谱、九／十点标记核与叶付真正例服务这条接口；它们没有覆盖删点后仍有大分量的所有输入。既有共根失败例、分叉反例和混合外迹正例都须保留，不能用代表路打包代替全支持物理截。[最新全域余口](NMRS_GLOBAL_ADVANCE_NEXT.md)

**一般宽度。** a+b=m、v=b−1≥a，p为非蓝洞、q为私洞，k=a−1。下一受控入口先取a=5：自然序四窗极值g4、四面体高度脸及普通行必须在同一p、q上共同结算。[全宽度窗口式§10](NMRS_FOUR_COLUMN_ORDERED_CUT_NEXT.md)为

$$a(p-q)\ge\binom vk-g_k(v)-\min\{(v-k)q,\sqrt{\binom v{k-1}(v-k)q}\},
\quad ap-(a-1)q\ge T(v,a,a-1).$$

对v≥t≥k，无相邻k窗族在每个有序t子集上的限制仍无窗；每个k集被计binom(v−k,t−k)次，双计数给

$$\frac{g_k(v)}{\binom vk}\le\frac{g_k(t)}{\binom tk}.$$

这是合法有限种子传播，本式本身尚不产生新的a5人口数值。下面给另一个已完成的有限窗口推论；后继更强g4／T进口仍须接回联合式、消去同一p、q，再与现有容量及渐近系数比较。

## 6. 本次新增解析贡献：任意a≥5的共同端脸窗口

本节是主会话新推导、由本文装配的工作推论，区别于前面的既有结果清点；它以[四列稿§10](NMRS_FOUR_COLUMN_ORDERED_CUT_NEXT.md)及[平移路径§5.2](../../nmrs-20261117/source/reports/n79-overlap-20261116/TRANSLATED-PATHS.md)已给的原输入到高度标脸接口为前提，未独审、未接受，没有有限程序或solver信用。

设a+b=m、b≥a≥5、v=b−1、k=a−1、V=binom(v,k)。原端脸引理说：对每个a集S，或者其两个端部k脸之一有红标记，或者其中某个k脸有私标记。任取整数a≤h≤v及有序h集U，同时选择其中包含min U、max U的全部a集，共binom(h−2,a−2)个请求。每个请求的红端脸恰含一个锚；给定该脸后加另一锚就唯一确定请求，所以一个红标脸至多支付一个请求。任一私标k脸最多包含于h−a+1个所选a集。若r_U、q_U分别数U内两类不同标脸，则

$$r_U+(h-a+1)q_U\ge\binom{h-2}{a-2}.$$

对全部U平均，每个k脸被计binom(v−k,h−k)次。全部不同红脸、私脸数为R、P，且同一洞集给R≤a(p−q)、P≤q，于是

$$\boxed{a(p-q)+(h-a+1)q\ge B_a(h)V,\qquad
B_a(h)=\frac{\binom{h-2}{a-2}}{\binom h{a-1}}
=\frac{(a-1)(h-a+1)}{h(h-1)}.}$$

B_a(h+1)−B_a(h)的符号是2a−3−h。因此当v≥2a−3，h=2a−3最优，h=2a−2可用时与它并列；得到推荐的共同窗口式

$$\boxed{ap-2q\ge\frac{(a-1)V}{2(2a-3)},\qquad
p\ge\left\lceil\frac{(a-1)V}{2a(2a-3)}\right\rceil.}$$

当a≤v<2a−3时直接取允许域中的最大B_a(h)，不越域使用最优h。h=a+1给局部a−1请求系数，已经强于[TRANSLATED-PATHS式(7e+)](../../nmrs-20261117/source/reports/n79-overlap-20261116/TRANSLATED-PATHS.md)的ceil((a+1)/2)（a≥5）；最佳h再加强它。结论针对这个命名通式，不声称超过所有其它方法；保留q比只取p下界更有信息。

一个完整数值出口是N(50,7,47)：a=5、b=45、v=44，V=135751，binom(48,4)=194580。同一[普通行计数§4.4](../../nmrs-20261117/source/reports/n78-shifted-rows-20261116/PROOF.md)在m=a+b时给

$$bH\ge\binom{m-2}{a-1}+(b-a)p+(a-1)q
\ge\binom{m-2}{a-1}+(b-a)p.$$

旧(7e+)给p≥5431，代同一行式得H≥9152；新式取h=7给p≥ceil(2·135751/35)=7758，得到

$$H\ge\left\lceil\frac{194580+40\cdot7758}{45}\right\rceil=11220,
\qquad\boxed{N(50,7,47)\le2118760-11220=2107540.}$$

旧命名通式配同一行式的比较值为2109608，故本次同方法收益2068。对整个a=5、b→∞族，p系数由1/25变成2/35；配相同普通行后，保证缺额的增加为

$$\frac3{175}\binom{b-1}4+O(b^3)=\frac{b^4}{1400}+O(b^3).$$

这是相对于该命名解析公式的整族改进，不是相对于所有可能上界的最优性认证；下面相邻窗口还严格加强它。具体数值不是取等构造或ES50阈值，没有启动求解。

### 6.1 相邻窗口必有一份严格余量

取a+1≤h<v。在每个有序h集U内定义整数余量

$$s(U)=r_U+(h-a+1)q_U-\binom{h-2}{a-2}\ge0.$$

断言任意有序(h+1)集W至少有一份h面U满足s(U)≥1。反设全部h面取等，记W两端为l、r。对任一有标记的(a−1)脸F，可选包含F及l、r的h面：其并最多a+1点，h≥a+1保证能在W中删去外点。取等迫红标F恰含l、r之一，否则它没有可支付请求；私标F必须含两端，否则至多支付一个请求，低于计入的h−a+1≥2。

因此W\{r}没有私标，其红标全含l。选同一个(a−2)集T，避开W的前两点和后两点；可选点数h−3≥a−2。在W\{r}中，请求{l,倒数第二点}∪T只有端脸{l}∪T可能有红标，故该脸必被标记；对称地W\{l}迫{r}∪T有红标。再取包含{l,r}∪T的h面，其对应请求同时获得两份红支付，违反取等。断言成立。

对全部W平均，每份h面恰出现v−h次，故平均s(U)≥1/(h+1)。重复上一节双计数得到

$$\boxed{a(p-q)+(h-a+1)q\ge
\frac{\binom{h-2}{a-2}+1/(h+1)}{\binom h{a-1}}V.}$$

对a=5、h=7、v≥8，即

$$5p-2q\ge\frac{81}{280}V,
\qquad p\ge\left\lceil\frac{81}{1400}V\right\rceil.$$

v=44时p≥7855，仍用同一普通行，有

$$H\ge\left\lceil\frac{194580+40\cdot7855}{45}\right\rceil=11307,
\qquad\boxed{N(50,7,47)\le2118760-11307=2107453.}$$

相对旧同方法2109608省2155，比单窗阶段再省87洞。整族p系数的最终增加是81/1400−1/25=1/56，因此相同普通行的保证缺额增加为binom(b−1,4)/56+O(b³)=b⁴/1344+O(b³)。单窗2068及b⁴/1400收益均保留为中间结果，不与最终收益相加。

本节仍是以原端脸桥为前提的同会话新解析推论，未独审接受。下一具体问题是能否对每个(h+1)集迫超过一份严格余量，或共同优化多类标脸的服务上限；“至少一个不取等h面”已经证明，不再作为待办。近对角宏观、残余取等、七参数全支持与固定宽度各有独立出口，不能用扩表数量代替其数学优先级。

当前结论是普通866≤58及其八参数315避免人口工作出口已经接通；进一步56／55、残余联合排除和七参数24点截仍开。所有后继数字保持目标响应，本文不启动求解或自动接受流程。
