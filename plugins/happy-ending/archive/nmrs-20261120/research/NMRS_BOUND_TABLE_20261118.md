<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# N(m,r,s)现值事实附表

2026-11-18。机械核对既有原稿、有限证书日志与当日新原件；本表不产生新数学推导，不作独立证明验收。本次未执行项目代码、solver、checker、SSH或外审。

`N(m,r,s)`指完整有序rank-3 signotope中禁蓝r点路径、红s点路径及weak m的最大避免人口。`C_m=N(m,m−1,m−1)`、`Q_m=N(m,m−1,m)`、`F_m=N(m,m,m)`；`D_m`为额外满足R7 junction条件的真实残余，不能替代普通`N(m,m−2,m)`。`ES(m)`为平面强迫阈值。工作稿中的装配为`Q≤C+D`、合法chart `F=Q+1`、几何包含后`ES≤F+1`。

“解析工作稿”均保留同会话／未独审／未接受；“有限PASS”仅指所链固定有限证据已有真实核验，不升级其原输入连接及全链审阅。

## 七参数

| 对象 | 现值 | 保证与原件 |
| --- | ---: | --- |
| N(7,4,7) | =16 | Baek短帽进口及下界；[文献核对](../../nmrs-20261117/source/reports/n7-progress-talk-20261117/BOUNDS_AUDIT.md)、[构造登记](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_STRATEGY_SYNTHESIS_20261116.md)。 |
| N(7,5,6) | =25 | 上界为限定756域全部有限阶的[C8人工接受](../../nmrs-20261117/source/.trellis/tasks/09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md)，保留same-family/provisional；下界为独立[25点色表有限核验](../../nmrs-20261117/source/reports/n756-professor-review-20261027/evidence/E21/portable-verification.json)，未证明几何实现。 |
| N(7,5,7) | ≤39 | [owner解析原稿§7.7](../../nmrs-20261117/source/reports/n7-owner-intervals-20261116/PROOF.md)排全部40点层；解析工作稿，不依赖附带CNF。 |
| C7=N(7,6,6) | ≤49 | [balanced严格容量](../../nmrs-20261117/source/reports/n766-strict-capacity-20261105/PROOF.md)的`2b−1`，b=25；解析工作稿。 |
| Q7=N(7,6,7) | ≤75 | [最终共同根替锁](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_LOCK_REPLACEMENT_COMMON_ROOT_EXCLUSION_AND_7576_BOUND_20261103.md)的`3b`；解析工作稿。 |
| F7=N(7,7,7)；ES(7) | ≤76；≤77 | 上项接[R20合法chart](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md)及几何包含；工作推论，未独立全链接受。 |

后四个受限域的已登记构造下界依次为26、30、31、32，未与工作上界相合，见[R12§5递归join构造](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R12_COMMON_REALIZABILITY_AND_UNIFORM_DEFICIT.md)。11/18后补未证明一般Q7≤74或≤73；见[当日叶付原稿§§11—13](N7_POSTLEAF_EXCEPTION_ORDERS_20261118.md)。

## 八参数

| 对象 | 现用工作上界 | 保证与原件 |
| --- | ---: | --- |
| N(8,4,8) | =22 | Baek文献精确值，[核对说明](../../nmrs-20261117/source/reports/n7-progress-talk-20261117/BOUNDS_AUDIT.md)。 |
| N(8,5,7) | 51 | [三列严格族](../../nmrs-20261117/source/reports/n79-overlap-20261116/THREE-COLUMN-STRICT.md)，解析工作稿。 |
| N(8,6,6) | **61** | 70态至少九洞；[milestone9 README](../../nmrs-20261117/source/reports/n866-joint-label-order-20261117/milestone9/README.md)及[实际115行核验日志](../../nmrs-20261117/source/reports/n866-joint-label-order-20261117/milestone9/verification.log)PASS。原输入提升与整体数学审阅另列。 |
| N(8,5,8) | 66 | [坐标删除§8](../../nmrs-20261117/source/reports/n78-row-compression-20261115/PROOF.md)，由22的真实切片双计数；解析工作稿。 |
| N(8,6,7) | 109 | [普通行原稿§§2—7](../../nmrs-20261117/source/reports/n79-overlap-20261116/PROOF.md)，126态至少17洞；解析工作稿。 |
| N(8,6,8) | 165 | [坐标删除§8](../../nmrs-20261117/source/reports/n78-row-compression-20261115/PROOF.md)，普通容量，不用D8替换。 |
| C8=N(8,7,7) | 193 | [公开有限数据抽象迁移§§1—8](../../nmrs-20261117/source/reports/n79-overlap-20261116/EIGHT-CYCLE-TRANSFER.md)；有限重放PASS，新packet桥未独审。 |
| D8（真实残余） | 124 | 同一迁移原稿；154态至少30洞。[原始Linux receipt](../../nmrs-20261117/source/reports/n79-overlap-20261116/octagon-source-replay/replay-receipt.json)记录exit0/PASS、未重建Lean。 |
| Q8；F8；ES(8) | 317；318；319 | `193+124`及两次加一，见[迁移§8](../../nmrs-20261117/source/reports/n79-overlap-20261116/EIGHT-CYCLE-TRANSFER.md)。319本身已有Schroeder公开平面结论，不认领新平面数值。 |

不调用公开193／124树的历史自主解析线是198／126／324／325（平面326），见[EIGHT-LAST§10](../../nmrs-20261117/source/reports/n79-overlap-20261116/EIGHT-LAST.md)。新九洞输入沿现有解析传递给备用195／126／321／322（平面323），见[九洞双侧传播](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/N7_N8_CLEAN_ROOT_RECTANGLES_20261117.md)及[NMRS既有列算§5.1](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/NMRS_CLAIMS_HANDOFF_20261117.md)；仍弱于进口型318避免人口。

[271行后继delivery核验](../SOURCE_MAP.md#excluded-sources)也为PASS，但[九洞向量](../SOURCE_MAP.md#excluded-sources)继续存活；该必要矩阵的最小洞数仍恰9。11／12洞及相应F8≤317／315均未获得，不能列为现值。

## 九参数

| 对象 | 现用工作上界 | 保证与原件 |
| --- | ---: | --- |
| N(9,4,9) | =29 | Baek文献精确值，[核对说明](../../nmrs-20261117/source/reports/n7-progress-talk-20261117/BOUNDS_AUDIT.md)。 |
| N(9,5,8) | 78 | [三列严格族](../../nmrs-20261117/source/reports/n79-overlap-20261116/THREE-COLUMN-STRICT.md)，解析工作稿。 |
| N(9,5,9) | 96 | [平移行§9.3](../../nmrs-20261117/source/reports/n78-shifted-rows-20261116/PROOF.md)，解析双计数，依赖29。 |
| N(9,6,7) | 117 | [GRAPH§§2—5](../../nmrs-20261117/source/reports/n79-overlap-20261116/GRAPH.md)，解析工作稿。 |
| N(9,6,8) | 185 | [TRANSFER-NEXT§§5—10](../../nmrs-20261117/source/reports/n79-overlap-20261116/TRANSFER-NEXT.md)，排全部24洞；解析工作稿。 |
| N(9,6,9) | 264 | [既有NMRS§6.1列算](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/NMRS_CLAIMS_HANDOFF_20261117.md)：`floor(11·96/4)`，调用[坐标删除§7.2](../../nmrs-20261117/source/reports/n78-row-compression-20261115/PROOF.md)；解析推论。 |
| N(9,7,7) | 222 | [NINE29](../../nmrs-20261117/source/reports/n79-overlap-20261116/NINE29.md)，排29洞；特定循环LP值28不是221人口界。 |
| N(9,7,8) | 380 | [普通行原稿§9.3](../../nmrs-20261117/source/reports/n79-overlap-20261116/PROOF.md)，462态至少82洞。 |
| N(9,7,9) | 633 | [既有NMRS§6.1列算](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/NMRS_CLAIMS_HANDOFF_20261117.md)：`floor(12·264/5)`，调用同一[坐标删除§7.2](../../nmrs-20261117/source/reports/n78-row-compression-20261115/PROOF.md)；解析推论。 |
| C9=N(9,8,8) | **688** | [原生整数证书RESULTS](../../nmrs-20261117/source/reports/n79-overlap-20261116/direct-cycle-lp/RESULTS.md)：924态至少236洞；[988独立标准库重建日志](../../nmrs-20261117/source/reports/n79-overlap-20261116/direct-cycle-lp/run-988-d2/standalone-check.log)PASS，883正权行。 |
| D9（真实残余） | **458** | 同一RESULTS：582态至少124洞；[D9独立标准库重建日志](../../nmrs-20261117/source/reports/n79-overlap-20261116/direct-cycle-lp/run-d9-d3/standalone-check.log)PASS，532正权行。 |
| Q9；F9；ES(9) | **1146；1147；1148** | [RESULTS装配](../../nmrs-20261117/source/reports/n79-overlap-20261116/direct-cycle-lp/RESULTS.md)：`688+458`及两次加一；全链仍未独立接受。 |

988／D9精确分子分别为235971673／123539361，λ=10^6，严格大于235λ／123λ；日志只核固定原生迹支持与整数算术。D9全部47635行有总缺额123539833/10^6≤124的精确分数可行点，只锁定这族纯LP的上取整124；不能说458可达。988深三时限无证书，成功深二688继续有效，见[RESULTS停止点](../../nmrs-20261117/source/reports/n79-overlap-20261116/direct-cycle-lp/RESULTS.md)。

## 更高参数和精确小帽区

下表为受限容量，均不能直接改写为同参数ES强迫阈值；除Baek短帽进口外均为解析工作稿。

| 参数 | 已登记上界 | 原件 |
| --- | ---: | --- |
| (10,4,10)／(11,4,11)／(12,4,12) | 37／46／56 | [Baek短帽公式登记](../../nmrs-20261117/source/reports/n79-overlap-20261116/LARGER-PARAMETER-BOUNDS.md)；`binom(m−1,2)+1`。 |
| (10,5,9)／(11,5,10) | 113／157 | [三列严格族](../../nmrs-20261117/source/reports/n79-overlap-20261116/THREE-COLUMN-STRICT.md)。 |
| (10,6,8)／(11,6,9) | 198／314 | [FAMILY§8](../../nmrs-20261117/source/reports/n79-overlap-20261116/FAMILY.md)。 |
| (10,7,7) | 237 | [TEN-NEXT§§1—5](../../nmrs-20261117/source/reports/n79-overlap-20261116/TEN-NEXT.md)，不是ES(10)≤238。 |
| (12,5,11)／(18,5,17)／(26,5,25) | 210／795／2554 | [TRANSLATED-PATHS§§5.3—5.4](../../nmrs-20261117/source/reports/n79-overlap-20261116/TRANSLATED-PATHS.md)。 |
| (12,6,10)／(13,6,11)／(14,6,12) | 474／689／970 | [STRICT-FAMILY4§6](../../nmrs-20261117/source/reports/n79-overlap-20261116/STRICT-FAMILY4.md)。 |
| (20,6,18) | 4759 | [TRANSLATED-PATHS§6](../../nmrs-20261117/source/reports/n79-overlap-20261116/TRANSLATED-PATHS.md)。 |

上表4759是本轮前基线；本轮新增的有限高度面及经典三角密度连接给未独审工作上界4749，完整推导、4750／4754等进口层级与保证见[新综合主文§4](NMRS_GLOBAL_STRATEGY_20261118.md)。

小参数不应误记为没有结论：对`2≤r,s≤m`且`r+s≤m+3`，已有精确式`N(m,r,s)=binom(r+s−4,r−2)`，包含六参数的weak自动区，见[R12§5](../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R12_COMMON_REALIZABILITY_AND_UNIFORM_DEFICIT.md)。本次未找到可据原件另登记的六参数非自动区新强界。一般三列二次缺额、四列三次缺额的完整适用域保留于[TRANSLATED-PATHS](../../nmrs-20261117/source/reports/n79-overlap-20261116/TRANSLATED-PATHS.md)；未已有m≥10的新平面数表装配。

## 漏项与历史／当前状态校对

本次在两份NMRS综述之外，**未检出更强的无条件7／8／9数值上界**；这是本地相关原件的核对结果，不是全仓穷尽证明或文献查新认证。实际差异如下。

| 来源与差异 | 历史／当前状态 |
| --- | --- |
| [LARGER-PARAMETER-BOUNDS](../../nmrs-20261117/source/reports/n79-overlap-20261116/LARGER-PARAMETER-BOUNDS.md)及[BOUNDS_AUDIT](../../nmrs-20261117/source/reports/n7-progress-talk-20261117/BOUNDS_AUDIT.md)仍写866≤63 | 已被11/17九洞61覆盖；两份NMRS已收入61。这是旧总账滞后，不是NMRS漏掉更强界。 |
| [HKH14／13点叶付正例](../source/reports/n7-postleaf-examples-20261118/REPORT.md) | 当日新实物局部事实：J=W=∅、ν3，删真中性第二口4后ν1；13点诱导域的合法完整扇给κ2、s1。基于旧Linux完整路径作新手验，未新机器重建；不是活动真K头或普适74点结论。两份综述未展开这份正例，不能因此下调Q7。 |
| [HAND_BRANCHES§§3—6](../source/reports/n866-global-order-20261118/HAND_BRANCHES.md)及[14角DIAMOND](../source/reports/n866-overlap-order-20261118/DIAMOND_INTERFACE.md) | 当日新增条件标签运输、精确前驱有符号行和真实8点同末对精确达到性例；未关闭61态，未形成新总洞界。14角为可容理想标签，8点例实现真实pair秩(4,4)，两者均未实现指定61态。 |
| 三个当日目录的执行状态 | [postleaf§6](../source/reports/n7-postleaf-examples-20261118/REPORT.md)、[global STATUS](../source/reports/n866-global-order-20261118/STATUS.md)、[overlap STATUS](../source/reports/n866-overlap-order-20261118/STATUS.md)：科研程序未到Linux或仅源码准备，无新solver/checker结果；既有封存证据未变。 |

本表只新增本文件，未改旧证明、原数值账、接受记录、任务指针、wiki、Goal、CNF／proof或运行作业。

## 本轮分层证明

[866同域秩与人口稿§§15—16](N866_Z8_JOINT_RANK_20261118.md)及[中性桥稿§§10—12](N866_Z8_NEUTRAL_BRIDGES_20261118.md)给现用25进口下的 `n+z≤65`，并将59点反设压到z≤5：六高中性与两枚同类洞的共同扫列迫双末≤12；全S、五内部洞且至少六中性时双末≤13，均低于最后59点z6反设的实际14。

[七参数临界乘积稿](N7_CRITICAL_PRODUCT_RETURN_20261118.md)仍保留 `6×12+1`、`5×12+13` 两谱，未闭的是孤点／13块配w的14点增广及真正跨块五迹的共同选择。上表普通数值保持不变；上述新增均为纸证、同会话未外审，未升级既有验收。

### 后补：z5层的新完整人口界

[共同终洞稿§16](N866_Z5_COMMON_TERMINALS_20261118.md)完整排除60点、z5，给现用25进口下的新分层工作界 **z=5⇒n≤59**。两方向H=5−3C迫各C≤1，可选择满S方向；C1的四洞分配分别由同类严格H界、四高中性t≤12、双向五高中性t≤13排除；C0的五洞分配分别由三高无洞t≤11、四高一洞t≤12、五高两洞t≤14或低222的H≥6排除。再由[同域联合秩稿§15](N866_Z8_JOINT_RANK_20261118.md)的n+z≤65排更大人口；无需删点保持Z。

此项只更新分层结论及原件指针，**不改上表普通866≤61等旧数值或验收记录**。八参数新原件为[共同终洞稿§§9—16](N866_Z5_COMMON_TERMINALS_20261118.md)与[联合秩人口稿§§15—16](N866_Z8_JOINT_RANK_20261118.md)；[七参数稿§12](N7_CRITICAL_PRODUCT_RETURN_20261118.md)仍准确列其已减义务与两类剩余14点增广。均为纸证、同会话未外审，59点z5以及一般866≤58仍未闭合。

### 59点z5的最新准确终态

[共同终洞稿§§17—18](N866_Z5_COMMON_TERMINALS_20261118.md)把满S、四内部洞、至少五实际中性提升为普适t≤12；配[穿孔初态稿§12](N866_Z5_PUNCTURED_INITIAL_20261118.md)的满S五内部洞t≤13，任何59点z5候选只剩两型：δ_I=δ_O=s_I=s_O=0、两向满S、k6、t15，各为3+3有效洞与五高中性；或者δ_I=δ_O=1、s_I=s_O=0，两向各缺一个S、k4、t14，洞分配为3+1或2+2且各向都须有低中性。前型没有排掉；后型也没有排掉。

双缺型的唯一初洞位置必须逐方向、逐颜色读取：三红一蓝时H∈N0∪{346,356,456}；三蓝一红时H∈N0∪{247,257,267}；两红两蓝时H∈N0，其中N0={347,357,367,457,467,567}。这只是必要位置，未构造实际模型或证明两向相容。普通上界及既有保证状态仍保持原记录。

[共同终洞稿§§19—21](N866_Z5_COMMON_TERMINALS_20261118.md)用同一物理点的真实顺逆时间，先证明全满型漏567与反向漏347只能互配，再用同方向T234占缺冲突排掉两端点，最后用真七点支撑和共享pair帽证明纯源p必须早于纯末q。结合原Hall表，方向漏态组合依次从20/36降到11/36、9/36，再到当前 **4/36**：仅(357,467)、(467,357)、(367,367)、(457,457)。未排这四型或双缺型，也未改变普通人口数值。

同一实序还锁出物理中性极点u=(正347、反567)、v=(正567、反347)，u<v；u早于全部15个纯双色末、v晚于全部15个纯双色源。两向唯一中间高漏态分别由不同纯双色源p、纯双色末q占用，并且u<p,q<v；这是共同真实区间，尚未确定p、q先后。

后补§21把上述区间强化为u<p<q<v，并从七点必有单色四迫出同一原pair的两向角秩(1,4;4,1)或换色：原X有异色五路分别终于／始于(p,q)，且所有x<p、y>q的χ(x,p,q)、χ(p,q,y)分别常色且相反。全部真实五路前后缀的乘积还满足§21.6式(60)的weak8阻碍；实际七点克隆校准说明首末规则自身可存活，不把这条全母体接口当59点闭合。

§21.8另给普适异常pair图α≤6及带入／出rank下界的子域路径容量；§21.9把全部真实红／蓝三迹直积接到同色格二部图，每对迹至少一条同色格边，并给不同实际格数与共同物理横截下界。它们保留同一原角对及全部支持，不将格数直接替代人口费用。

§21.10再锁两个指定物理端口的完整T态：四个漏态对依次给(T^-(q),T^+(p))=(235,246)、(246,235)、(236,236)、(245,245)。两端都实际取全4×4旋转补极性等号，相应占T行又迫35/46、46/35、36/45或45/36的蓝洞／红补洞二择一；未据这些必要条件宣称四类或59点全排。

### 后补：z4整层由61降至60

[61点z4完整表证§§1—8](N866_61_Z4_FOUR_HIGH_TWO_HOLES_20261118.md)排尽费用C1及满S五洞的5+0、4+1、3+2全部分配：最后四高中性两蓝洞以45对人工穷尽压到12行，11行由同一普通覆盖容量排除，唯一余型由真实转置后357源的八终洞扫列排除。因此 **z=4⇒n≤60**；原件总接口亦已追加于[联合秩稿§17](N866_Z8_JOINT_RANK_20261118.md)。这是按原母体实际Z的分层结论，没有删样本保持Z的假设；普通866≤61保持，61点z0—3仍未排。纸证同会话、未独审／未接受，无科研程序或checker运行。

### 七参数本轮14点标记及跨块复活原件

最新原件为[14点标记共同返回稿§5](N7_MARKED_14_SHARED_RETURN_20261118.md)的单标记九点核／十点候选及唯一缺坐标分组、[同稿§9](N7_MARKED_14_SHARED_RETURN_20261118.md)的饱和红六精确秩与全域同一尾对秩切、[同稿§12](N7_MARKED_14_SHARED_RETURN_20261118.md)的全选择跨块复活上界及外迹乘积覆盖；不应只回读旧临界乘积稿§12。

固定其它41点最大选择后，每个临界12块至多三个本地红六首点可以没有混合出红五；故整个V中严格首／末的12块被排，任意四个指定首点的混合外迹必须覆盖全部外最大选择乘积，镜像亦然。标记十点局部返回、兼容避迹证书及共同50点判据均有完整条件；一般74点的全部跨块同时返回尚未证明，767／777普通数值及原保证状态不变。第一谱严格首末条件计入固定孤点z；不能仅按活动块次序忽略z端四点迹。
