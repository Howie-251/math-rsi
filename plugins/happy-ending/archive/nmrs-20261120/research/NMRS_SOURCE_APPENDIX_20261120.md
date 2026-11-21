<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# N(m,r,s) 现值与原件附录

2026-11-20。本页仅整理本地现存原件、读取既有回执并检查链接；没有运行研究程序、求解器、checker、SSH或外审，没有改变旧接受记录。本页优先采用各原稿的最后后补，不以旧综述正文覆盖新终态。

## 1. 对象与保证

下列三位缩写均指完整有序 rank-3 signotope 的最大避免人口：`mrs=N(m,r,s)`，禁蓝 r 点路、红 s 点路与同一实际首末的 weak m；路长计实际顶点。`C_m=N(m,m−1,m−1)`、`Q_m=N(m,m−1,m)`、`F_m=N(m,m,m)`。`D_m`保留 R7 的真实 junction 条件，不能改名为普通 `N(m,m−2,m)`。`ES(m)`为平面强迫阈值，较相应避免人口再加一。

“纸证”指原作者完整解析工作稿，仍同会话、未独审／未接受；“有限核验”只核所链接的固定域、整数证书或 CNF/proof。独立程序重建不等于独立数学审阅；两次同实现的实际 DRAT 不等于两种 checker。文献进口未在本次重放。未列参数仍可调用换色和小帽精确区，不能把空表项理解为无结果。

## 2. 六至九参数现值

### 六参数

| 对象 | 已登记值 | 原件与保证 |
| --- | ---: | --- |
| 646 | =11 | [四池稿§3.3](N866_59_FOUR_POOLS_AND_WEAK6_20261118.md)：Baek 短帽进口；精确值登记见[portfolio§1](NMRS_PORTFOLIO_AFTER_NOV18.md)。 |
| 655 | =14 | [四池稿§3.1](N866_59_FOUR_POOLS_AND_WEAK6_20261118.md)：Szekeres–Peters 同域17点计算定理，加两次合法点扩张给上界；[R12§5](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R12_COMMON_REALIZABILITY_AND_UNIFORM_DEFICIT.md)构造达14。公开枚举本次未重放。 |
| Q6／F6 | =15／=16 | [portfolio§1](NMRS_PORTFOLIO_AFTER_NOV18.md)登记同域17点进口、16点构造及 R20；不是本次新计算。 |

对 `2≤r,s≤m`、`r+s≤m+3`，已有精确式 `N(m,r,s)=binom(r+s−4,r−2)`；六参数的自动区也包含在内，来源为[R12§5](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R12_COMMON_REALIZABILITY_AND_UNIFORM_DEFICIT.md)。

### 七参数

| 对象 | 现用值 | 原件与保证 |
| --- | ---: | --- |
| 747 | =16 | [文献条件核对](../../nmrs-20261117/source/reports/n7-progress-talk-20261117/BOUNDS_AUDIT.md)、[构造与现值登记](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_STRATEGY_SYNTHESIS_20261116.md)。 |
| 756 | =25 | 上界为[C8人工接受原件](../../nmrs-20261117/source/.trellis/tasks/09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md)的指定756域，保留 same-family/provisional；下界另见[25点颜色核验](../../nmrs-20261117/source/reports/n756-professor-review-20261027/evidence/E21/portable-verification.json)，不含几何实现。 |
| 757 | ≤39 | [owner§7.7](../../nmrs-20261117/source/reports/n7-owner-intervals-20261116/PROOF.md)，纸证；非仅旧蓝壳条件界。 |
| C7=766 | ≤49 | [balanced 严格容量](../../nmrs-20261117/source/reports/n766-strict-capacity-20261105/PROOF.md)，纸证。 |
| 真实D7 | ≤30 | [R7§3.3五点横截](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md)给`N756+5=25+5`；不称最优，也不以此推出Q75。 |
| Q7=767 | ≤75 | [共同根替锁](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_REPLACEMENT_COMMON_ROOT_EXCLUSION_AND_7576_BOUND_20261103.md)，纸证。 |
| F7=777／ES7 | ≤76／≤77 | 上项接[R20合法 chart](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md)及几何包含，全链未独立接受。 |

757／766／767／777 的已登记构造下界为26／30／31／32，见[R12§5](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R12_COMMON_REALIZABILITY_AND_UNIFORM_DEFICIT.md)。11/18标记、批量、临界乘积等结果没有证明普适 Q7≤74 或≤73。

### 八参数

| 对象 | 现用值 | 原件与保证 |
| --- | ---: | --- |
| 848 | =22 | [Baek条件核对](../../nmrs-20261117/source/reports/n7-progress-talk-20261117/BOUNDS_AUDIT.md)。 |
| 857 | ≤50 | [五洞整层排除](N857_SHARED_ROWS_NEXT.md)，纸证；不把未运行核验程序记为 PASS。 |
| 858 | **≤64** | [稳定主入口](evidence/n8-d122-common-bridges-20261119/ORDINARY858_64_VERIFIED.md)、[最终双检回执](../evidence/858/ordinary858-64-final-receipt.json)；两次实际 DRAT、完整独立重建 hash 相同；原输入桥另见[NEAR65](evidence/n8-d122-common-bridges-20261119/NEAR65_SEMANTIC_BRIDGE.md)。 |
| 866 | **≤57** | [全域H12主证](N866_57_GLOBAL_20261119.md)、[独立重建及第二实际回放](evidence/n8-total-deficit-313-20261119/ordinary866-h12-second-replay-20261119/README.md)。 |
| 867／868 | **≤102／≤160** | [C188主证首段及§2](N8_C188_311_20261119.md)登记同输入删除传播 `floor(9·57/5)`／`floor(10·64/4)`；普通容量，不用真实残余替换。 |
| C8=877 | **≤188** | [C188主证](N8_C188_311_20261119.md)；完整式双检，另有删除复合容量及公开 cycle 行后的纯原生／私面式双检，见[第二回放](../SOURCE_MAP.md#excluded-sources)及[47063句core回放](../SOURCE_MAP.md#excluded-sources)。 |
| 真实D8 | **≤121** | 同一 R7 母体物理分区为普通866与普通858，`57+64`，见[C188现行总界](N8_C188_311_20261119.md)；不声称普通868≤121。 |
| Q8／F8／ES8 | **≤309／≤310／≤311** | `188+121`、合法 chart 加一、几何包含再加一；现用装配见[C188主证](N8_C188_311_20261119.md)。全链未独审接受，不主张 sharp 或全球优先。 |

旧193／124／317／318（平面319）是[公开有限树迁移](../../nmrs-20261117/source/reports/n79-overlap-20261116/EIGHT-CYCLE-TRANSFER.md)阶段；190／124、189／123、188／122及其总界也是历史版本。[D122独立联合证书](N8_D122_312_20261119.md)仍封存有效，但当前真实D采用121。普通858的66／65、866的61／58、867的109／104、868的165／164均已被本表覆盖，不累计阶段收益。

### 九参数

| 对象 | 现用值 | 原件与保证 |
| --- | ---: | --- |
| 949／958／959 | =29／≤78／≤96 | [Baek核对](../../nmrs-20261117/source/reports/n7-progress-talk-20261117/BOUNDS_AUDIT.md)、[三列严格族](../../nmrs-20261117/source/reports/n79-overlap-20261116/THREE-COLUMN-STRICT.md)、[平移行§9.3](../../nmrs-20261117/source/reports/n78-shifted-rows-20261116/PROOF.md)。 |
| 967／968／969 | ≤117／≤185／≤264 | [GRAPH](../../nmrs-20261117/source/reports/n79-overlap-20261116/GRAPH.md)、[TRANSFER-NEXT](../../nmrs-20261117/source/reports/n79-overlap-20261116/TRANSFER-NEXT.md)、[已登记坐标列算§6.1](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/NMRS_CLAIMS_HANDOFF_20261117.md)；纸证及其推论。 |
| 977／978／979 | ≤222／≤380／≤633 | [NINE29](../../nmrs-20261117/source/reports/n79-overlap-20261116/NINE29.md)、[普通行§9.3](../../nmrs-20261117/source/reports/n79-overlap-20261116/PROOF.md)、[列算§6.1](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/NMRS_CLAIMS_HANDOFF_20261117.md)。 |
| C9=988／真实D9 | **≤688／≤458** | [最终RESULTS](../../nmrs-20261117/source/reports/n79-overlap-20261116/direct-cycle-lp/RESULTS.md)：924态≥236洞、582态≥124洞；[988独立整数日志](../../nmrs-20261117/source/reports/n79-overlap-20261116/direct-cycle-lp/run-988-d2/standalone-check.log)及[D9日志](../../nmrs-20261117/source/reports/n79-overlap-20261116/direct-cycle-lp/run-d9-d3/standalone-check.log)均 PASS。 |
| Q9／F9／ES9 | **≤1146／≤1147／≤1148** | [RESULTS装配](../../nmrs-20261117/source/reports/n79-overlap-20261116/direct-cycle-lp/RESULTS.md)，全链未独审接受。 |

两个整数日志分别核883／532条正权原生迹，分母10⁶，扣超载后的分子235971673／123539361。其 PASS 核支持重建与整数算术，不代替原输入迹引理、R7／R20及全链接受。

## 3. 更高受限参数与固定宽度

以下均为受限容量；例如1077≤237不表示 ES10≤238。除注明整数核验者外为解析工作稿或已有文献公式代入。

| 参数 | 当前登记上界 | 原件 |
| --- | ---: | --- |
| (10,4,10)／(11,4,11)／(12,4,12) | 37／46／56 | [Baek短帽总账§4.1](../../nmrs-20261117/source/reports/n79-overlap-20261116/LARGER-PARAMETER-BOUNDS.md)。 |
| (10,5,9)／(11,5,10)／(12,5,11)／(18,5,17) | 113／157／210／795 | [三列严格族](../../nmrs-20261117/source/reports/n79-overlap-20261116/THREE-COLUMN-STRICT.md)、[平移路径§5](../../nmrs-20261117/source/reports/n79-overlap-20261116/TRANSLATED-PATHS.md)。 |
| (10,6,8)／(11,6,9)；(10,7,7) | 198／314；237 | [FAMILY](../../nmrs-20261117/source/reports/n79-overlap-20261116/FAMILY.md)、[TEN-NEXT](../../nmrs-20261117/source/reports/n79-overlap-20261116/TEN-NEXT.md)。 |
| (12,6,10)／(13,6,11)／(14,6,12) | 474／689／970 | [STRICT-FAMILY4§6](../../nmrs-20261117/source/reports/n79-overlap-20261116/STRICT-FAMILY4.md)。 |
| (20,6,18) | **4747** | [四列最终§§6—9](NMRS_FOUR_COLUMN_ORDERED_CUT_NEXT.md)、[两私脸修复](N20_ORDERED_REPAIR_NEXT.md)；4759／4749为旧阶段。 |
| (22,5,21)／(26,5,25)／(29,5,28)／(53,5,52) | 1506／2549／3590／23202 | [现用总入口§3](NMRS_GLOBAL_ADVANCE_NEXT.md)、[三列最终§13](NMRS_ORDERED_THREE_COLUMN_STABILITY_NEXT.md)；旧2553／3594／23213不再作现值。 |
| (245,5,244) | 2416117 | [现用总入口§3.2](NMRS_GLOBAL_ADVANCE_NEXT.md)，P(18)=24勘误后的代入。 |
| (32,6,32)／(32,7,32)／(32,8,32) | 43570／304990／1829939 | [严格递推主稿§1](NMRS_GLOBAL_WINDOW_AND_SATURATION_20261119.md)、[有理／整数回执](../SOURCE_MAP.md#excluded-sources)；比较对象是命名旧短帽删除式。 |
| (50,7,47) | **2103267** | [真实请求并集费用§9.3](NMRS_WINDOW_INTEGER_LIFT_20261119.md)、[union证书核验](../SOURCE_MAP.md#excluded-sources)：861脸型、123410四端型，H≥15493。 |
| (51,7,48) | **2332173** | [共同运输§2.1](NMRS_GLOBAL_WINDOW_AND_SATURATION_20261119.md)、[精确有理数回执](../SOURCE_MAP.md#excluded-sources)：合用原式(35)/(41)，H≥16887，无新增LP／SAT。 |

50参数旧2107453、2106981、2104743、2103293均为中间结果；51参数2332194也已覆盖。有限并集种子和整族种子用途不同：整族现用系数 `c=62043237111/678755000000`，来源为[归一化种子及合法44子集运输§8.4](NMRS_WINDOW_INTEGER_LIFT_20261119.md)、[逐脸整数核验](../SOURCE_MAP.md#excluded-sources)。不能将有限并集收费无损搬到任意更大高度；准确边界见原稿§§9.2、9.4。

## 4. 基础、历史与通式索引

| 索引 | 可调用内容与原件 |
| --- | --- |
| H1 | [R1](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESTART_SETTING_ANALYSIS.md)：真实pair秩、理想及状态注入；[R1—R27综述](../../nmrs-20261117/source/RESEARCH_REVIEW_R1_R27_20261026.md)作历史导航，不覆盖后来数值。 |
| H2 | [R5](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R5_COVER_AUGMENTATION_CAPACITY.md)、[R6](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R6_OVERLAP_TWO_AND_766_TRANSFER.md)：同一实际覆盖的严格递推；短帽输入变化与新增结构收益须分账。 |
| H3 | [R7§8.4](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md)：同一pivot真实分拆 `Q≤C+D`；[R12§5](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R12_COMMON_REALIZABILITY_AND_UNIFORM_DEFICIT.md)：构造与精确自动区；[R20](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md)：合法chart `F=Q+1`。 |
| H4 | [R23](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R23_GLOBAL_EXTREMAL_ARCHITECTURE_AND_CRITICAL_REALIZABILITY.md)：b25基座传播；[10/29后归因](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_STRUCTURAL_SYNTHESIS_AND_ROADMAP_20261113.md)、[原件索引§2](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/NMRS_SOURCE_LEDGER_20261117.md)区分输入收益、匹配收益与chart收益。 |
| G1 | [坐标删除§7](../../nmrs-20261117/source/reports/n78-row-compression-20261115/PROOF.md)：真实含／避坐标切片；[平移行§4.4](../../nmrs-20261117/source/reports/n78-shifted-rows-20261116/PROOF.md)：普通行计数；[TRANSLATED-PATHS](../../nmrs-20261117/source/reports/n79-overlap-20261116/TRANSLATED-PATHS.md)：高度脸与一般宽度。 |
| G2 | [严格坐标递推§1](NMRS_GLOBAL_WINDOW_AND_SATURATION_20261119.md)：两层以上含坐标饱和不能取等；一层只保留普通floor，不能套严格减一。 |
| G3 | [三列最终§§11—13](NMRS_ORDERED_THREE_COLUMN_STABILITY_NEXT.md)：`v=m−4≥4`时 `H≥ceil(T/3+3v/4−8)`；`v≥22`时 `H≥ceil((T+2v−2)/3)`，`T=floor((v−1)²/4)`，与其他有效洞界取最大。 |
| G4 | [四列最终§8](NMRS_FOUR_COLUMN_ORDERED_CUT_NEXT.md)：13点有限进口版严格三次系数；可选近期四面体密度进口另列，不混入4747。 |
| G5 | [全宽度端窗§6](NMRS_SYNTHESIS_AND_UPPER_BOUND_ROUTES_20261119.md)、[整数提升稿](NMRS_WINDOW_INTEGER_LIFT_20261119.md)：共同p、q的端脸窗口、逐层取整、模余数、有限权重及实际请求并集。最终数值取本附录§3。 |

## 5. 已知边界与验收范围索引

| 索引 | 边界、校准与原件 |
| --- | --- |
| B1 | [N7一般容量](N7_GENERAL_CAPACITY_NEXT.md)：遗传坐标人口松弛恰87，加入主帽75仍可容75；它不是实际signotope见证。 |
| B2 | [标记14点共同返回](N7_MARKED_14_SHARED_RETURN_20261118.md)、[批量红六](N7_74_BATCH_RED6_TRANSVERSAL_20261118.md)、[临界分量](N7_74_CRITICAL_COMPONENT_DELETION_20261118.md)：保留全部实际路径、删后重算及共同物理费用；没有普适24截。 |
| B3 | [D9最终RESULTS](../../nmrs-20261117/source/reports/n79-overlap-20261116/direct-cycle-lp/RESULTS.md)：47635行精确分数点只锁该纯LP族洞数上取整124；不证明458可达，也不排更强真实约束。988深三时限无证书不覆盖成功深二688。 |
| B4 | [中央30真例](N866_LARGE_CENTRAL_CALIBRATION_NEXT.md)、[scalar-grid编码状态](../source/reports/n866-scalar-grid-20261119/ENCODING_AND_STATUS.md)：36点校准确实达到C30，但Δ28不覆盖低缺额57点余域；不能追无前提C≤29。 |
| B5 | [首七版08正式纠正](../SOURCE_MAP.md#excluded-sources)、[独立全式重建](../SOURCE_MAP.md#excluded-sources)、[独立全句SAT回放](../SOURCE_MAP.md#excluded-sources)：编号命名空间误判已撤回；该必要式SAT不实现真实57点，也不证明≤56。 |
| B6 | [11/20真实根与尾帽](N866_ROOTED_FAN_TAIL_20261120.md)、[右延拓Horn](NMRS_RIGHT_EXTENSION_HORN_20261120.md)：结构及真实50点校准；短两端边界未产生新收费。普通866现值仍57。 |
| B7 | [共同桥最终§4](N8_D122_COMMON_BRIDGES_NEXT.md)：A57、U64下两向饱和匹配可合并，给9个同码双纤维；较早单向纤维界不足以单独承担9。 |
| V1 | [公开八边形来源回执](../../nmrs-20261117/source/reports/n79-overlap-20261116/OCTAGON-SOURCE-RECEIPT.md)、[实际有限重放](../../nmrs-20261117/source/reports/n79-overlap-20261116/octagon-source-replay/replay-receipt.json)：固定15文件子包PASS，没有本次Lean重建；新抽象packet桥与全链接受分别承担。 |
| V2 | [普通866第二回放原receipt](../SOURCE_MAP.md#excluded-sources)：checker0、唯一VERIFIED；[858最终receipt](../evidence/858/ordinary858-64-final-receipt.json)同时保存两份完整短日志、源码及CNF/proof哈希。 |
| V3 | [C188主证](N8_C188_311_20261119.md)逐列完整式、删复合式、纯原生／私面式、core及本地转回绑定；封包校验是字节证据，不是第三次DRAT或独立数学审阅。 |

[Operational connection details omitted from this publication excerpt.]
