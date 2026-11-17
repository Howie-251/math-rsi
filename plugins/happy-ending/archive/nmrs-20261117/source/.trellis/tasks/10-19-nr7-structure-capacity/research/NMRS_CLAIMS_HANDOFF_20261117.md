# N(m,r,s) 研究交接：现用声明、结构进展与证据边界

截至2026年11月17日，九洞数值证据采用15:28封包。本文整理从七参数研究到八、九参数及一般受限容量族的现有结果，供汇报、引用和后续研究恢复。它是已有原件的综合交接，不是一次新的数学验收。11月17日午后的共同锁块、clean根与共同标签九洞证据已纳入；普通866的现用工作上界已从63经62到61。各项声明仍沿其原来的文献进口、有限核验和人工接受范围。

## 1. 可直接引用的摘要

我们研究完整有序rank-3 signotope中的受限容量 $N(m,r,s)$：同时避免蓝$r$点路径、红$s$点路径和weak $m$的最大人口。现有七参数工作上界为

$$
N(7,4,7)=16,\quad N(7,5,6)=25,\quad
N(7,5,7)\le39,\quad N(7,6,6)\le49,\quad
N(7,6,7)\le75,\quad N(7,7,7)\le76.
$$

其中25的上界已在限定模型的所有有限阶上获得人工接受，保留same-family/provisional说明；25点抽象染色见证也已单独核验。39、49、75、76来自后续结构工作证明，整条链尚未独立接受。经合法chart及平面包含关系，它们给出平面强迫工作推论 $ES(7)\le77$，不把这项工作推论写成已正式验收的公开纪录。[七参数原件对照](N7_STRATEGY_PRIMARY_INDEX_20261116.md)

以下 $C_m=N(m,m-1,m-1)$、$Q_m=N(m,m-1,m)$、$F_m=N(m,m,m)$；$D_m$ 为带额外路径交接排斥的真实残余容量。它们均为避免人口，平面 $ES(m)$ 另计强迫阈值。

八参数公开有限数据加本项目signotope迁移给 $C_8\le193,D_8\le124,Q_8\le317,F_8\le318$，相应平面阈值为319。193和124的公开有限部分已在Linux实际重放PASS；新增抽象packet桥仍待独立审阅。319本身已是Schroeder公开预印本的平面上界，本项目新增主张在于抽象模型迁移，并不认领新的平面319数值。不调用这两棵公开树的历史自主解析线为198／126／324／325，11月17日新九洞有限证书结合已有解析传递又给195／126／321／322的备用工作链，相应平面阈值323。九洞证书使普通 $N(8,6,6)\le61$，仍未降低进口型全局318。[八参数迁移](../../../../reports/n79-overlap-20261116/EIGHT-CYCLE-TRANSFER.md)、[历史自主线](../../../../reports/n79-overlap-20261116/EIGHT-LAST.md)、[九洞封包](../../../../reports/n866-joint-label-order-20261117/milestone9/README.md)

九参数原生迹整数证书给 $C_9\le688,D_9\le458$，经R7、R20装配得到 $Q_9\le1146,F_9\le1147$，相应平面强迫工作推论为 $ES(9)\le1148$。两份紧凑证书已由另写的标准库程序在Linux精确重建PASS；有限支持与整数算术已核，实际配置到必要行及整个几何出口仍由工作证明承担，尚无完整独立接受。688和458不调用八参数的公开有限树、新循环packet桥或977的222数值。[原生证书与装配](../../../../reports/n79-overlap-20261116/direct-cycle-lp/RESULTS.md)

结构上，研究已从独立估计小帽容量，推进到同一母体上的真实切片、共同匹配、替锁、物理横截、可提升标口流及共享缺态预算。最新七参数结果迫74点反设中至少五个clean根及相应真中性标口，并可把它们放进同一份全局最大流；八参数零缺额反设迫同一共同匹配中至少37个真中性I端点。它们是新条件结构，尚未给普适24点红六横截或新的无条件888界。[共同锁块](N7_N8_COMMON_LOCK_BLOCK_CAPACITY_20261117.md)、[clean根与矩形](N7_N8_CLEAN_ROOT_RECTANGLES_20261117.md)

## 2. 对象和单位

每个递增三元组都有红蓝两色之一；每个递增四点packet按 $abc,abd,acd,bcd$ 的顺序至多变色一次。路径长度计实际顶点数。weak $m$ 指同一对实际首末点之间的异色路径，顶点数之和至少 $m+2$。定义不额外加内部不交要求：packet使单色路径对子序列遗传，两色同端路径若再共一个内点，则同一个三元组须同时两色，所以在当前模型内其内点自动不交。

为避免把人口上界和强迫阈值混淆，统一记

$$
C_m=N(m,m-1,m-1),\qquad Q_m=N(m,m-1,m),\qquad F_m=N(m,m,m).
$$

$D_m$ 是R7分拆中带junction排斥的真实双侧残余：残余自身无weak $m$、无蓝$(m-2)$路径，且没有同一点既结束红$(m-2)$路径又开始蓝$(m-3)$路径。它不能用来替换普通 $N(m,m-2,m)$。R7给 $Q_m\le C_m+D_m$（$m\ge6$）；合法chart的删根与添根给 $F_m=Q_m+1$（$m\ge4$）。几何配置属于适用的抽象模型，再从最大避免人口加一，才得到

$$ES(m)\le F_m+1\le C_m+D_m+2.$$

因此三个“加一／相加”各有自己的数学连接：R7的不交真实分拆、R20的合法chart、以及避免人口到平面强迫阈值。不能从一个公开平面 $ES(8)\le319$ 倒推出所有signotope的 $F_8\le318$。平面重取根上向及“删根加一、强迫再加一”在Tóth–Valtr和Schroeder已有先例，抽象marked-pivot也有既有对应；本项目可归属的是从packet出发的自足chart证明及应用，不宣称首创这一恒等式。[R7](RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md)、[R20](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md)、[R20原件查新比较](R20_NOVELTY_COMPARISON_20261023.md)

本文以“工作上界”表示原件给出完整候选推导，但全链尚未独立接受；“checked”明确指相应固定有限证据经过实际checker。它不自动证明所有数学连接均已独立核验，也不代表取等可达。

## 3. 七参数：25的接受、后续下降及其来源

### 3.1 当前数值账

| 对象 | 现用值 | 主要来源与可引用范围 |
| --- | ---: | --- |
| $N(7,4,7)$ | =16 | Baek短帽基线与构造；它是后续代表域及clean根计数的输入。[基线及构造登记](N7_STRATEGY_SYNTHESIS_20261116.md) |
| $b=N(7,5,6)$ | =25 | 上界来自C1—C10限定域人工接受；下界来自另一份完整25点染色见证。两份证据分别承担两方向。 |
| $A=N(7,5,7)$ | ≤39 | owner区间、代表红团、第一端及五行求和排除所有40点输入；现用解析短证不依赖CNF。[owner §7.7](../../../../reports/n7-owner-intervals-20261116/PROOF.md) |
| $C=N(7,6,6)$ | ≤49 | 实际替末、安全增广及双色端点交替环排除给一般balanced严格容量 $2b-1$。[严格容量证明](../../../../reports/n766-strict-capacity-20261105/PROOF.md) |
| $Q=N(7,6,7)$ | ≤75 | 同一个中间匹配、临界共同根及替锁，排除 $3b+1$ 取等，给 $Q\le3b$。[最终替锁](N7_LOCK_REPLACEMENT_COMMON_ROOT_EXCLUSION_AND_7576_BOUND_20261103.md) |
| $F=N(7,7,7)$ | ≤76 | 由Q75及合法chart $F=Q+1$，不是另一次SAT排除。 |
| $ES(7)$ | ≤77（工作推论） | 76避免人口、几何包含和强迫再加一共同承担。 |

25的正式范围是**每个有限阶**的完整有序rank-3、禁B5／R6／weak7域。人工接受记录明确保留same-family/provisional、reviewer backend/model及实际effort不可核；它没有给不受限平面ES结论，也没有单独给25点存在性。[C8人工接受原件](../../09-03-35-state-cardinality-charging/research/c8-formal-acceptance-20261026.md)

25点存在性由[E21颜色表](../../../../reports/n756-professor-review-20261027/evidence/E21/color.tsv)和[便携核验](../../../../reports/n756-professor-review-20261027/evidence/E21/portable-verification.json)承担：2300个三元组、12650个packet、300对实际外端均检查，最长蓝路4点、红路5点，无weak7；状态注入有效，$e=m=9$。没有附平面坐标或可伸直性证明。因此可以在该抽象域写25精确，不能把此见证称为25点几何构造。

39的完整正面证明已在11月16日关闭40点层。许多较早757稿仍写“39未闭”，或只在某个蓝壳条件下给39；这两种历史描述不能覆盖现用owner §7.7。39点实际构造与≤38仍未得到。旧40点等号层的均匀15度、$D=E$、七洞禁同缺等结构，也不能原样搬到39点17洞层。[真正39层的重算](../../../../reports/n79-overlap-20261116/SEVEN-39-SOURCE.md)

当前构造下界按747／756／757／766／767／777依次为16／25／26／30／31／32。除25的独立完整色表外，这些下界的正面来源包括R12 §5递归join构造：它在明确递归类中构造实际packet合法配置，另给几何实现；不是从早期普通目录O的纯比较数自动推出存在性。只有747、756上下相合；后四项尚未确定精确容量。[下界登记](N7_STRATEGY_SYNTHESIS_20261116.md)、[递归构造原件 §5](RESET_R12_COMMON_REALIZABILITY_AND_UNIFORM_DEFICIT.md)

对外比较须分开：Schroeder v1公开平面结果为 $ES(7)\le81,ES(8)\le319$，其平面756容量25与本项目全部signotope域的25不是同一个断言；其heptagons中也已有平面balanced容量49。项目49的贡献是全抽象域和一般p的工作证明，77则是更强的**候选工作推论**，不是把公开81改写为已经外部接受的77。[公开几何原件](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/paper/geometry.tex)、[公开七边形原件](../../../../tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/paper/heptagons.tex)、[文献与项目口径](../../../../reports/n7-progress-talk-20261117/BOUNDS_AUDIT.md)

### 3.2 历史下降：哪些来自输入，哪些来自结构

| 阶段 | 当时757／766／767／777 | 实际变化 |
| --- | --- | --- |
| R1—R4 | 45／58／103／206 | 实际末对标签与状态注入建立人口目录；未把任意占态当实际模型。 |
| R5 | 44／58／101／201 | 同一实际覆盖的严格增广，兑现递推减一。 |
| R6，短帽28 | 43／56／98／195 | 交叠、766传播，同时含短帽输入变化。 |
| R7 | 43／56／89／177 | 真实不交H—R分拆、共同三链及残余junction限制。 |
| R8，短帽26 | 41／52／83／165 | 统一缺额传播；数字下降部分来自短帽输入。 |
| R20，同一短帽26 | 41／52／83／84 | Q不变，合法chart精确一点归约把F从165降到84。 |
| R23，短帽25 | 40／50／80／81 | 新基座25的传播。 |
| 10/29—11/03 | 最终40／50／75／76 | Q逐步79、78、77、76、75；共同中间匹配、共同根与最终替锁承担结构收益。 |
| 11/05 | 40／49／75／76 | balanced严格容量49；没有自动产生Q74。 |
| 11/16 | 39／49／75／76 | 完整owner解析证明排40；没有自动产生Q74。 |
| 11/17 | 39／49／75／76 | 分叉核、共同锁块、真中性流、clean根等条件结构加强；一般Q仍75。 |

前27轮的逐阶段来源见[R1—R27历史综述](../../../../RESEARCH_REVIEW_R1_R27_20261026.md)；后续共同匹配与替锁见[10/29综合](../../../../RESEARCH_SYNTHESIS_N7_20261029.md)及[11/13结构综合](N7_STRUCTURAL_SYNTHESIS_AND_ROADMAP_20261113.md)。历史表是定位，不是对每一轮全部推导重新认证。

### 3.3 为什么继续降低A或C不直接动Q

现有接口只共同给

$$Q\le\min\{3b,C+b+5,A+C-1,\lfloor9A/4\rfloor,\lfloor9C/5\rfloor\}=75$$

（代入 $b=25,A=39,C=49$）。A再降至38、C再降至48，均不能通过这组已知接口降低75。$Q\le C+b$ 尚是待证桥，不能当既有递推。因此新工作把目标转到**同一实际母体的总物理费用**。[11/16策略 §3](N7_STRATEGY_SYNTHESIS_20261116.md)

对任一767输入X，都有 $\tau_{R_6}(X)\ge|X|-49$。75点要有实际≤25点红六横截才可排除；74点要有实际≤24点横截才可排除并得Q≤73。排75只给Q≤74，不能同时认领Q≤73；反之排所有74点则由遗传性也排更大人口。人口反证还允许删后核更小的条件界，不强求所有证明都先产出24截。

## 4. 11月17日七参数后继：已关闭的核与仍缺的共同费用

### 4.1 分叉核64、双向核57与joint57

正向分叉是实际红六与从其第三点开始的实际红五的物理支持并，反向对偶。单向最小横截数记λ，正反联合族的物理最小横截记μ；μ必须在同一物理并内支付，不能当两份独立最优费用之和。

| 新结构 | 已得到的工作结论 | 当前边界 |
| --- | --- | --- |
| 单向无分叉核 | $\lvert Y\rvert\le64$，故 $\lvert X\rvert\le64+\lambda(X)$；无分叉补域重算第三点数k后，还有 $\lvert X\rvert\le49+\lvert D\rvert+\min(15,k,32-k)$。 | 实际λ≤9给人口≤73；74、75候选分别须λ≥10、11。一般九费或十费分叉横截未证。[九点fork](N7_74_NINE_POINT_FORK_CUT_EXCLUSION_20261117.md) |
| 双向无分叉核 | 有实际至多8点红六横截，$\lvert Y\rvert\le57$；原域 $\tau_{R_6}(X)\le\mu+8$、$\lvert X\rvert\le57+\mu$。 | μ≤16给实际24截；74、75候选分别须μ≥17、18。一般μ≤16未证。[双向红四](N7_74_BIDIRECTIONAL_RED_FOURS_20261117.md) |
| joint57取等域 | 两组红四锚各4点且严格有序，删后同一49点766核；共同Hall供给迫中央蓝五及极端伙伴容量。 | 排掉部分伙伴子类，未排整个57点域。即使排57，也还须处理μ≥18的费用。[joint57](N7_74_JOINT57_ORDERED_ANCHORS_20261117.md) |

16点完整767例实际有 $\tau_{R_6}=3,\lambda_+=\lambda_-=2,\mu=3$，可选两份完整认证支持不交的8点包；它反驳无人口限制的“两包必交”，不反驳74点临界命题。[实际复核](../../../../tmp/n7_bidirectional_four_20261117/REPORT.md)

joint57的有限必要投影中，70种锚交错排17、余53 SAT；私人边11种端点型排4、余7 SAT。余7尚未实现完整外部私人路，不能据其SAT登记57点真实模型或否定完整必要推论。[联合次序有限报告](../../../../tmp/n7_joint57_order_20261117/REPORT.md)

### 4.2 共同锁块：七参数合并至多四块

一份前向锁块由同一pair的三份实际见证构成：红$(m-1)$外端、蓝$(m-2)$首对、红$(m-1)$末对；反向锁块为完整反序。任意q份严格分离、允许混合两方向的块，各取红长路的m−3个内点，得到**同一个**无红$(m-2)$实际域Z，故

$$ (m-3)q\le N(m,m-1,m-2). $$

更强的提取保留每块一个整半块：每块恰m−2点全红，全部跨块红$(m-2)$均排除。七参数因此得到q份有序五点红块，无跨块红五、无蓝六。五块的精确必要CNF在Linux经生产Kissat与实际DRAT checker给VERIFIED，逐条编码审计覆盖331475子句。因此对满足该提取接口的两类caller，合并块数均≤4：canonical非through正反所选锁，以及R7同一共同匹配中的块型边。两个caller不能相加。[共同锁块 §§1—4、9](N7_N8_COMMON_LOCK_BLOCK_CAPACITY_20261117.md)、[五块原始报告](../../../../reports/n7-shared-arm-replay-20261117/lock-blocks/REPORT.md)

另有实际20点四块完整颜色，独立语义audit检查packet、全部单色路及weak7为零。故这个抽取投影的精确上限为4；它没有实现四份原始实锁的额外三证，不能当四锁母体构造，也说明只重复这些投影条件无法再降至3。

### 4.3 共同费用：叶中心、标口流、clean整类

共同锁块还证明：支付一个已认证锁，可以让相应半开区间内的全部旧非中性端点退出**所有幸存红六**的首末身份，允许同锁多owner并对物理标签去重。付费集J含全部贯穿点T，注销的未删端点为W；删后全路首末图二部。设原首末并人口u，$t=|T|$，已认证叶收益B满足 $|J|-|W|=t-B$。删后全端点最大匹配为ν，含孤点缺额 $d=|U_0|-2\nu$；可提升标口网络点割为κ，节省 $s=\nu-\kappa$。则**该构造费用**精确满足

$$2(|J|+\kappa)=u+t-B-d-2s.$$

因此 $B+d+2s\ge u+t-48$ 等价于这份费用≤24；在该恒等式保证的奇偶下也等价于阈值 $u+t-49$。一般74点是否总能生成足够的J、W与共同标口池，仍未证明。[锁块叶费用 §§5—5.2](N7_N8_COMMON_LOCK_BLOCK_CAPACITY_20261117.md)、[真中性流 §§1—5](N7_NEUTRAL_PATH_FLOW_20261117.md)

网络由全部实际红六生成；每条网络路径可提升成具有同一首末与标口的真实红六。Menger只给这些保护标签互异，未标中点仍可交，不能称完整红六顶点不交打包。标口删除和物理删除也是不同费用操作；物理删后须重算全部路，不能把较强物理删点结果无证明代入原网络κ。

最新clean根稿把单次匹配的中性右端提升为整类性质：block右点是全K图私叶，可在**同一**最大匹配同时规范；剩余clean根的每条ambient长红，其第二点都是真中性。七参数74点有至少5根、75点至少6根。取掉全部block根并保留K孤根得到实际域V，所有长红都从clean根开始，经真中性口；人口迫流给相同5／6供给。可把指定clean根子流增广到同一份全局最大流，74点中全局流至少25，同时保留至少5个clean根；预删J后，分别重算损失为 $25-|J|$ 与 $5-|J\cap V|$。[clean根 §§2—4、10—12](N7_N8_CLEAN_ROOT_RECTANGLES_20261117.md)

clean头在全存活口集合中有精确区间邻居，倒序头可以去交叉而保持同一尾流。共缝匹配迫真实阶梯及完整子矩形；完整I矩形满足 $L_B(A)+L_R(B)\le m-1$。这些是共同支持的新限制，尚未把大流量迫成一个足够小的点割。

同日后补整类端图结果进一步给：七参数真实红六首末图在 $K\times E$ 上无 $K_{5,5}$，故五个K根的共同实际末点至多4；终端互异、头区间共缝的真实三元流最多8条（七参数）、20条（八参数）。对至少五个K根的共同中性口，**全部口的全部尾末物理并**也至多4，给已闭条件费用 $|J|+|P|-|A|+|Z|+4$；若根域有红四，可把常数4换成1。一般输入能否把例外口Z控制到总费24仍开。[clean根 §§13—17](N7_N8_CLEAN_ROOT_RECTANGLES_20261117.md)

同日有限排除还覆盖七参数固定P3／C3长臂的共缝、分离等模板，以及一份允许全部候选路径的26点共缝端点／最终根骨架，均有各自checked收据。它们没有穷尽任意支持重合、任意物理大小及原74点输入；整类K5,5禁形允许每条边用不同长路，但仍要实际提取共同矩形。[固定模板、26点骨架及最新失败独审的准确范围](N7_N8_CLEAN_ROOT_RECTANGLES_20261117.md)

### 4.4 共享臂偏序是另一份准确费用接口

固定实际红六中边，左右二点臂构成精确笛卡尔积；同根候选按包含成线序，只须登记被指定方向的最大臂图。对预删D和中边定向σ，将所有登记臂边去重为同一物理图F，任一顶点覆盖C给 $D\cup C$ 的实际红六横截，并有

$$\tau_{R_6}(X)=\min_{D\subseteq M_X,\sigma}\bigl(|D|+\tau(F_{X\setminus D,\sigma})\bigr),$$

其中 $M_X$ 是原域所有实际红六第三／第四点的物理并。单根图是偏序比较图；全局过去／未来蓝扇偏序提供反链与分层人口证书。F未证二部，不能任意以匹配代替顶点覆盖；等式仍未给未知最优值，必须可生成地选D、σ和同一物理覆盖才兑现24费。[共享臂偏序](N7_SHARED_ARM_POSETS_20261117.md)

### 4.5 旧分支仍须按准确范围保留

| 分支 | 现状与恢复时不能省的条件 |
| --- | --- |
| 原cut退款与Hall | 满20原cut帽、饱和分配h=0及镜像已有实际 $12+9+3=24$ 截；无d28前提。h≥3、未饱和帽及一般母体仍开。[EARLY_HALL §§10—12](../../../../reports/n7-owner-intervals-20261116/EARLY_HALL.md) |
| 75点中性窗 | 全部红六首末并≤50，现用 $25\le d\le28$；旧22—28、23—28为中途值。74点必须依自身人口重算。[D23 §9](../../../../reports/n7-owner-intervals-20261116/D23.md) |
| 四最大红六后继 | 双方都无完整三点锚路的分支已闭；恰一整侧有锚及至少五路仍开。54点弱化核可有5截，不能只凭人口排除完整54层。[E1](N7_74_E1_COMMON_FIVE_FACE_20261116.md)、[单侧锚](N7_74_ONE_SIDED_ANCHOR_AND_POPULATION_20261116.md) |
| H17 | 恢复后的25点必要投影实际VERIFIED SAT；17标点仅4点具局部双向B5，并非17个ambient-through模型，不排H17。旧SSH失败与后来成功执行分列。[实际报告](../../../../reports/n7-blue-through-seventeen-20261113/execution-20261116-restored-route/REPORT.md) |
| 小反例 | 21点贯穿例否定无条件内部无B5；25点互补例否定无条件h−i≤10。均非74／75点或几何反例，不否定带临界人口条件的命题。[21点](../../../../reports/n7-blue-through-local-20261112/full-k21/REPORT.md)、[25点](../../../../reports/n7-h-minus-i-complement-20261112/REPORT.md) |

## 5. 八参数：普通子参数、三条出口与11月17日的新缺额

### 5.1 现用子参数全表

以下列出超出经典自动区且在现用材料中单独登记的全部八参数行；换色对称的行不重复。文献组合基线仅用公开输入，星号表示组合得到、未必印在原论文中的值。

| 对象 | 文献或文献组合基线 | 项目现用值 | 来源及保证 |
| --- | ---: | ---: | --- |
| $N(8,4,8)$ | 22 | **=22** | Baek v2取等定理与抽象上界；精确性来自文献，不是项目新结果。 |
| $N(8,5,7)$ | 56 | ≤51 | [三列严格族](../../../../reports/n79-overlap-20261116/THREE-COLUMN-STRICT.md) |
| $N(8,6,6)$ | 70 | **≤61** | 11/17共同标签115必要行，≤8洞真实DRAT检查；封包重建及九洞向量PASS。[九洞封包](../../../../reports/n866-joint-label-order-20261117/milestone9/README.md) |
| $N(8,5,8)$ | 78* | ≤66 | 由22的真实含坐标切片双计数。[坐标删除 §8](../../../../reports/n78-row-compression-20261115/PROOF.md) |
| $N(8,6,7)$ | 126 | ≤109 | 126态至少17洞，排尽16洞边界。[总PROOF §§2—7](../../../../reports/n79-overlap-20261116/PROOF.md) |
| $N(8,6,8)$ | 204* | ≤165 | 由66的真实切片双计数；普通容量，不能换成残余124。 |
| $C_8=N(8,7,7)$ | 252 | ≤193／备用≤195 | 公开迁移／新九洞证书加解析传递分账；历史纯解析198保留。 |
| 真实 $D_8$ | 148* | ≤124／自主≤126 | 148是公开输入的残余二分组合；154仍是原证书状态宇宙大小。 |
| $Q_8=N(8,7,8)$ | 456* | ≤317／备用≤321 | 同参数真实C、D经R7装配；历史纯解析324。 |
| $F_8=N(8,8,8)$ | 457* | ≤318／备用≤322 | 合法chart加一；历史纯解析325。 |
| 平面 $ES(8)$ | 319（已公开） | ≤319／备用≤323 | 抽象到几何及强迫加一；历史纯解析326，进口线没有新的平面数值下降。 |

除22的直接文献精确性及明确checked有限证据外，上表项目解析与迁移连接均沿未独立接受的工作稿。旧[BOUNDS_AUDIT](../../../../reports/n7-progress-talk-20261117/BOUNDS_AUDIT.md)中的866工作上界63是午前截面；本表采用同日后继61，其余基线算术沿原审计。

### 5.2 历史自主线、新证书备用线与公开迁移线

自主线 $198+126\to324\to325\to326$ 的完整装配见[EIGHT-LAST §10](../../../../reports/n79-overlap-20261116/EIGHT-LAST.md)、[EIGHT-MOVE §§17—18](../../../../reports/n79-overlap-20261116/EIGHT-MOVE.md)及[CASCADE-63](../../../../reports/n79-overlap-20261116/CASCADE-63.md)。“自主”仅指不调用公开193／124有限树，仍使用Baek短帽等明示基础进口。

新九洞输入t=9代入同一双侧解析式给C8至少57洞、D8至少28洞，因此本次直接算术得 $C_8\le195,D_8\le126,Q_8\le321,F_8\le322,ES(8)\le323$。这是**有限证书加既有解析传递的备用工作链**，不使用Schroeder193／124两棵树，不称纯解析新证明；实际原输入到共同标签核的必要性仍是其前提。它加强历史备用325，但仍弱于进口型318。[新输入及双侧传播](N7_N8_CLEAN_ROOT_RECTANGLES_20261117.md)、[封存核验](../../../../reports/n866-joint-label-order-20261117/milestone9/verification.json)

较强线 $193+124\to317\to318\to319$ 的本项目新增部分，是把经核准循环三元符号通过packet接到原实际顺序的同端两色路；再核普通252态、真实残余154态、23个Baek压缩块和两棵完整整数树的接口。[迁移原稿 §§2—8](../../../../reports/n79-overlap-20261116/EIGHT-CYCLE-TRANSFER.md)

其保证应分三层阅读：

1. 公开原包、manifest及作者封存finite／Lean回执的字节身份已绑定。原Lean几何接口含native evaluation信任，不能称kernel-only。
2. 本项目Linux实际重放有限checker所需15文件子包，exit0、PASS、8.538秒，结果除耗时外与作者回执相同；没有重建Lean或运行native evaluator。
3. 新signotope桥、R7/R20接回及完整抽象链仍待独立审阅接受。

原件与实际回执为[OCTAGON-SOURCE-RECEIPT](../../../../reports/n79-overlap-20261116/OCTAGON-SOURCE-RECEIPT.md)、[replay-receipt.json](../../../../reports/n79-overlap-20261116/octagon-source-replay/replay-receipt.json)、[finite-result.json](../../../../reports/n79-overlap-20261116/octagon-source-replay/finite-result.json)。193、124不归为本项目原创的平面数值；有限PASS不替代新增抽象桥。

### 5.3 866从63经62到61：新约束、checked证书与当前停止点

旧完整通用循环族的63种支撑与原生迹相同，七洞mask能满足全部行；仅对固定七洞mask检查362对、917单pair单cell分支，没有找到所寻条件循环证书。这些负结果不证明实际共同标签或染色存在。[通用行报告](../../../../reports/n866-joint-holes-20261117/REPORT.md)、[共同pair报告](../../../../reports/n866-joint-holes-20261117/common-pair/REPORT.md)

新共享枢轴手证从同一个pair的所有cell分支产生30条十三态必要行，与63旧行合成93行。精确≤7洞CNF有602变量、1150子句；独立重建必要行、计数与CNF绑定PASS，Kissat exit20，drat-trim exit0且`s VERIFIED`。于是普通866至少8洞、人口≤62。该矩阵有八洞向量

$$1248,1258,1278,1358,1368,2347,3567,4567,$$

已逐行整数核验，所以**该93行矩阵**最小洞数恰8；它不是62点实际signotope，也不证明容量取等。这是11/17较早阶段，后续共同标签约束已继续切掉八洞预算。[必要行手证](../../../../reports/n866-joint-holes-20261117/SHARED_PIVOT.md)、[八洞阶段报告](../../../../reports/n866-joint-holes-20261117/pivot-rows/REPORT.md)

15:28的最终封包从实际Ferrers cell集合、同pair标签、颜色增长、packet和同端异色五路构造11个checked共享标签核，将必要行增加到115。真实输入的状态注入保留理想包含序与原pair标签，故可赋给该必要模型；核UNSAT再投影为有效缺态行。精确≤8洞预算的CNF有664变量、1295子句，实际Kissat exit20、外部checker exit0；封包核验重建115行、逐核proof及最终proof，PASS。同时九洞向量

$$1238,1458,1468,1568,2347,2357,2367,3567,4567$$

通过全部115行的整数检查，故**新矩阵**最小洞数恰9，给 $N(8,6,6)\le61$ 的计算工作声明。向量仅是必要矩阵取等，不是共同标签赋值、61点实际染色或几何构造。新预算没有达到11／12洞，继续相同115行也不能越过9。[封包README](../../../../reports/n866-joint-label-order-20261117/milestone9/README.md)、[真实seal回执](../../../../reports/n866-joint-label-order-20261117/receipts/milestone-seal-run.json)、[核验原件](../../../../reports/n866-joint-label-order-20261117/milestone9/verification.json)、[必要模型源码](../../../../reports/n866-joint-label-order-20261117/build.py)

令t为866已保证洞数。既有双侧传递为

$$H_C\ge\left\lceil\frac{210+8t}{5}\right\rceil,\qquad
H_D\ge\left\lceil\frac{1708+51t}{79}\right\rceil.$$

与进口洞数59／30逐侧取较强，$F_8\le407-H_C-H_D$。旧t=8给55／27，当前t=9给57／28，仍被59／30覆盖，故进口型F8仍318。t=10也不能跨线；t=11若以后成立，可借进口残余30洞给317；t=12则两侧纸面给62／30洞，可给315。后两项仍是**条件响应**，没有已证明的新866输入。[双侧杠杆推导](NMRS_STRUCTURAL_ROADMAP_20261117.md)、[最新传播 §16](N7_N8_CLEAN_ROOT_RECTANGLES_20261117.md)

### 5.4 带余量共同匹配的最新连接

同一R7分拆 $X=H\sqcup R$ 中，令 $|H|=193-\delta_C,|R|=124-\delta_D$。全K两型真实见证图的Hall回添给

$$\nu_{\rm all}\ge58-\delta_C-\delta_D.$$

I型pair同时为蓝六末对和红七首对；II型为G源到其固定第二点的红七外端。11/17后继已将旧“II层状”加强为严格分离；红末I型也成为反向实锁。**同一个匹配**的两类块型边合并仍严格分离，内点域给 $5q\le N(8,6,7)\le109$，故块型合计≤21。109既有解析来源，现在也能独立由九洞证书及 $5N(8,6,7)\le9\cdot61$ 重得。余下至少 $37-\delta_C-\delta_D$ 条I边，其右端都是真中性，并共同组成一个实际866域；clean根侧也有相同人口下界。[区间分离](N8_JOINT_MATCHING_DISJOINT_20261117.md)、[共同锁块 §§6、9](N7_N8_COMMON_LOCK_BLOCK_CAPACITY_20261117.md)、[clean整类及最新传播](N7_N8_CLEAN_ROOT_RECTANGLES_20261117.md)

零缺额时这批中性I子匹配至少37条，必有七个依次分离区间或同缝七条匹配边。后续已找到两份真实23点Q8域，分别实现这两类七条真中性I边，含完整蓝六／红七臂、同一全局点对序p和实际K/L身份；全I图分别43边／7边，匹配数均7。它们**反驳无人口限制的七边禁则**，不是193／124近饱和输入，不排利用共同缺额的新命题。它们的长红尾可共享末点，因此也不违反终端互异三元流的w≤20定理。[完整实际反例及独立有限audit](../../../../reports/n8-neutral-seven-orders-20261117/REPORT.md)

中性域删任意一点仍有两色五路，且其中蓝五末点对应I红七的第三点须在L。共缝阶梯、完整I矩形的双色预算及全ambient中性出口仍可用，但新反例说明必须把它们接到大人口／余量，而不能再单独排七个I头。

若以后能对所需**全部低缺额实际母体**统一把该中性子匹配压到36／35／34，才分别得到F8≤317／316／315。只排零缺额不够认领两点、三点改进。八参数七块42点基础投影虽SAT，但有weak8；后续1437个有效weak cuts耗尽预算，既无weak8-free见证也无UNSAT，不能用它降低21。[七块实际报告](../../../../reports/n8-common-lock-blocks-20261117/REPORT.md)

## 6. 九参数：最终原生证书及其完整装配

### 6.1 子参数全表

| 对象 | 文献或文献组合基线 | 现用工作值 | 原件 |
| --- | ---: | ---: | --- |
| $N(9,4,9)$ | 29 | **=29** | Baek文献精确性；[项目调用 §9.3](../../../../reports/n78-shifted-rows-20261116/PROOF.md) |
| $N(9,5,8)$ | 84 | ≤78 | [三列严格族](../../../../reports/n79-overlap-20261116/THREE-COLUMN-STRICT.md) |
| $N(9,5,9)$ | 113* | ≤96 | $\lfloor10\cdot29/3\rfloor$，真实切片。 |
| $N(9,6,7)$ | 126 | ≤117 | [GRAPH §§2—5](../../../../reports/n79-overlap-20261116/GRAPH.md) |
| $N(9,6,8)$ | 210 | ≤185 | [TRANSFER-NEXT §§5—10](../../../../reports/n79-overlap-20261116/TRANSFER-NEXT.md) |
| $N(9,6,9)$ | 323* | ≤264 | 本次列算 $\lfloor11\cdot96/4\rfloor$，由同一坐标删除定理。[§7.2](../../../../reports/n78-row-compression-20261115/PROOF.md) |
| $N(9,7,7)$ | 252 | ≤222 | [NINE29](../../../../reports/n79-overlap-20261116/NINE29.md) |
| $N(9,7,8)$ | 462 | ≤380 | [总PROOF §9.3](../../../../reports/n79-overlap-20261116/PROOF.md) |
| $N(9,7,9)$ | 785* | ≤633 | 本次列算 $\lfloor12\cdot264/5\rfloor$，由同一坐标删除定理。[§7.2](../../../../reports/n78-row-compression-20261115/PROOF.md) |
| $C_9=N(9,8,8)$ | 924 | **≤688** | 原生整数证书，924态至少236洞。 |
| 真实 $D_9$ | 575* | **≤458** | 原生整数证书，582态至少124洞；575比较基线不改变582证书宇宙。 |
| $Q_9=N(9,8,9)$ | 1709* | **≤1146** | 同一R7真实分拆，688＋458。 |
| $F_9=N(9,9,9)$ | 1710* | **≤1147** | 合法chart加一。 |
| 平面 $ES(9)$ | 1508，另有1501* | **≤1148**（工作推论） | 几何包含及强迫再加一。 |

基线1508是Mojarrad–Vlachos原论文通式在n=9的代入值，近期文献也明确写出该数值；1501是已公开平面transfer定理与公开输入的组合 $924+575+2$，不是该原论文印出的值，不宣称已有外部先例或全局最优。项目1148及全表贡献分账见[BOUNDS_AUDIT](../../../../reports/n7-progress-talk-20261117/BOUNDS_AUDIT.md)。旧1155／1156、1171／1172／1177均为更早阶段。

其中969的264、979的633为本次整理调用既有真实含位切片定理的直接算术，非另获独立证明或新证书，不进入几何1148链。与自动区精确公式及换色合用，七、八、九三表覆盖各自全部 $2\le r\le s\le m$ 的非经典参数，不把未单列的经典行误作空白。

### 6.2 证书究竟检查了什么

| case | 状态数 | 完整矩阵行数 | 正权行数 | 整数缺态下界 | 人口界 | $D-P$（$\Lambda=10^6$） |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 普通988，depth2 | 924 | 90891 | 883 | 236 | 688 | 235971673 |
| 真实D9，depth3 | 582 | 47635 | 532 | 124 | 458 | 123539361 |

加权必要行给 $D\le\sum_W\ell_Wh_W\le\Lambda H+P$，其中每个实际洞变量 $h_W\in\{0,1\}$，P为逐列超载罚项。精确分子分别严格大于 $235\Lambda$、$123\Lambda$，故H至少236、124；浮点LP目标不进入结论。D9从792个五元态限制为 $12\in W\Rightarrow11\in W$ 的582允许态，原行需求精确减去支撑落在宇宙外的态数。

独立标准库checker从q/p差分格、两条合法链、固定坐标映射重建每条原始支撑，重算禁止态扣除、需求与全部列负载，两份单独重放均PASS。成功日志、退出码与紧凑文件SHA已绑定。大矩阵仍在Linux，紧凑重放不需要它们、SciPy、优化器或网络。[RESULTS](../../../../reports/n79-overlap-20261116/direct-cycle-lp/RESULTS.md)、[988日志](../../../../reports/n79-overlap-20261116/direct-cycle-lp/run-988-d2/standalone-check.log)、[D9日志](../../../../reports/n79-overlap-20261116/direct-cycle-lp/run-d9-d3/standalone-check.log)

有限整数核验、新原生迹引理、真实坐标删除、R7分拆、R20及几何包含是不同义务。两份PASS不能单独替代后五项的完整数学审阅，也不能把458称为实际可达值。

### 6.3 已知方法停止点

D9全47635行有精确分数可行点，总缺额 $123539833/10^6\le124$，全部不等式经整数复核。与对偶证书合用，只锁定**该纯原生LP族的缺额上取整恰124**；它不排整数分支或新路径条件。988深三触时限且无证书，Python进程exit0不等于checker成功；成功深二688继续有效。D8原生depth2仅给130，弱于自主126及进口124。公开977特定矩阵LP值28也不推出221人口界。[停止点原件](../../../../reports/n79-overlap-20261116/direct-cycle-lp/RESULTS.md)

## 7. 一般参数：精确区、递推与统一缺额

### 7.1 可直接调用的接口

| 声明 | 适用域与实际意义 | 原件 |
| --- | --- | --- |
| $N(m,r,s)=\binom{r+s-4}{r-2}$ | $2\le r,s\le m,r+s\le m+3$；weak自动区，上下界相合，换色可交换r、s。 | [R12 §5](RESET_R12_COMMON_REALIZABILITY_AND_UNIFORM_DEFICIT.md) |
| $U_m(a,b)\le\binom{a+b}a$ | $U_m(a,b)=N(m,a+2,b+2)$；真实pair标签给状态注入，不是任意占态实现定理。 | [R1](RESTART_SETTING_ANALYSIS.md) |
| $N(m,r,m)\le N(m,r-1,m)+N(m,r,m-1)-1$ | $m\ge4,4\le r\le m$；减一来自同一个实际覆盖的严格性。 | [R5](RESET_R5_COVER_AUGMENTATION_CAPACITY.md)、[R6](RESET_R6_OVERLAP_TWO_AND_766_TRANSFER.md) |
| $N(p+2,p+1,p+1)\le2N(p+2,p,p+1)-1$ | $p\ge4$，两个对偶短帽有同一有效整数人口上界即可，不要求该上界可达。 | [balanced严格容量](../../../../reports/n766-strict-capacity-20261105/PROOF.md) |
| $Q_m\le C_m+D_m$；$F_m=Q_m+1$ | 前者 $m\ge6$，D保留真实junction条件；后者 $m\ge4$，使用合法chart。 | [R7](RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md)、[R20](RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md) |
| $U_m(a,b)\le\min\{\lfloor(a+b)U_m(a,b-1)/b\rfloor,\lfloor(a+b)U_m(a-1,b)/a\rfloor\}$ | 两向真实坐标切片双计数；逐片来源须为同一母体。 | [坐标删除 §7](../../../../reports/n78-row-compression-20261115/PROOF.md) |
| $N(m,4,m)=\binom{m-1}2+1$ | $m\ge4$；Baek v2 Definition 1.4、Theorem 1.6给几何下界，2.7给抽象上界。m=7、8、9分别精确16、22、29。 | [本次文献核对](../../../../reports/n7-progress-talk-20261117/BOUNDS_AUDIT.md) |

公开基本规则另给无严格减一的Pascal递推 $N(m,r,s)\le N(m,r-1,s)+N(m,r,s-1)$。它用于本文文献组合比较，不偷用项目51、109等加强。真实残余也有有效组合 $D_m\le N(m,m-2,m-2)+N(m,m-3,m)$，所以D8文献比较为148、D9为575；这不重写既有154、582状态宇宙。[基线完整算术](../../../../reports/n7-progress-talk-20261117/BOUNDS_AUDIT.md)

### 7.2 普通平移行的广域式

当 $a,b\ge2,L=a+b\ge m\ge4$，真实同端两色迹与坐标删除给

$$N(m,a+2,b+2)\le\binom La-
\left\lceil\frac{(L-m+1)\binom{L-2}{a-1}}{\max(a,b)}\right\rceil.$$

这是一条必要缺态上界，未称全参数精确公式。[平移行 §4.4](../../../../reports/n78-shifted-rows-20261116/PROOF.md)

对 $a,b\ge3,m=a+b$，非蓝洞数还满足 $p\ge\lfloor(m-2)/(a+1)\rfloor$。若 $b-1\ge a$，可取 $p\ge\lceil\binom{b-1}{a-1}/a^2\rceil$；若 $N=b-1\ge a+1$，进一步可取

$$p\ge\left\lceil\frac{\binom N{a-1}\lceil(a+1)/2\rceil}{a\binom{a+1}2}\right\rceil.$$

这些适用下界取最大，可从 $\binom ma$ 扣除；三、四列应优先使用下面已经接到普通行的较强式。[TRANSLATED-PATHS §§1—5.2](../../../../reports/n79-overlap-20261116/TRANSLATED-PATHS.md)

### 7.3 三列族与二次缺额

对 $m\ge8$，令

$$n=m-2,\quad b=m-3,\quad p_0=\lfloor n/4\rfloor,\quad
f(p)=\left\lfloor\frac{1+\sqrt{1+24p}}2\right\rfloor,$$
$$P_* =\max\left\{p_0,\left\lceil\frac{\lfloor(b-2)^2/4\rfloor}{3}\right\rceil\right\}.$$

现用统一式为

$$N(m,5,m-1)\le\binom m3-
\max\{n-1,n+p_0-4,n+P_*-f(P_*)\}.$$

第一项保留原严格族 $\binom m3-(m-3)$，不让新式覆盖小参数较强旧值；m=12另取特例210。缺额主项达 $n^2/12-O(n)$，没有最优渐近常数声明。[三列严格族](../../../../reports/n79-overlap-20261116/THREE-COLUMN-STRICT.md)、[现用加强 §5.3—5.4](../../../../reports/n79-overlap-20261116/TRANSLATED-PATHS.md)

### 7.4 四列族与三次缺额

令 $n=m-2,g=\lfloor(m-3)^2/4\rfloor$。全部 $m\ge8$ 有 $N(m,6,m-2)\le\binom m4-g$；$m\ge12$ 可再减一。八至十一参数另取较强特例61、117、198、314；十二、十三用474、689。八参数61为同日有限证书输入，其余见[FAMILY](../../../../reports/n79-overlap-20261116/FAMILY.md)、[STRICT-FAMILY4](../../../../reports/n79-overlap-20261116/STRICT-FAMILY4.md)。

对 $m\ge14$，记

$$c_n=\begin{cases}n+2,&n\text{偶},\\ n,&n\text{奇},\end{cases}\qquad
P_4=\max\left\{\left\lfloor\frac n5\right\rfloor,
\left\lceil\frac{3\binom{n-3}3}{40}\right\rceil\right\}.$$

则

$$N(m,6,m-2)\le\binom m4-g-P_4+\left\lfloor\frac{12P_4}{c_n}\right\rfloor.$$

该式在其域内至少保留g＋1洞，缺额达 $n^3/80-O(n^2)$。普通覆盖松弛的精确g不等于实际signotope容量可取等；上式也不越域覆盖m=12、13。[现用四列加强 §6](../../../../reports/n79-overlap-20261116/TRANSLATED-PATHS.md)

### 7.5 更高参数的具体结果

| 参数 | 现用工作上界 | 来源 |
| --- | ---: | --- |
| $(10,4,10),(11,4,11),(12,4,12)$ | 37／46／56 | Baek短帽公式代入，文献进口。 |
| $(10,5,9),(11,5,10)$ | 113／157 | 三列严格通式。 |
| $(10,6,8),(11,6,9)$ | 198／314 | FAMILY §8。 |
| $(10,7,7)$ | 237 | [TEN-NEXT §§1—5](../../../../reports/n79-overlap-20261116/TEN-NEXT.md)，252态至少15洞。 |
| $(12,5,11),(18,5,17),(26,5,25)$ | 210／795／2554 | TRANSLATED-PATHS §§5.3—5.4，取代211／801／2577及2574。 |
| $(12,6,10),(13,6,11),(14,6,12)$ | 474／689／970 | STRICT-FAMILY4 §6；14参数与后继式同值。 |
| $(20,6,18)$ | 4759 | TRANSLATED-PATHS §6，取代4772。 |

这些是受限容量；1077的237不等于 $ES(10)\le238$。现有登记未装配出 $m\ge10$ 的新平面数表或统一显式ES改进式；仍需同参数真实C、D输入。[现用大参数总账](../../../../reports/n79-overlap-20261116/LARGER-PARAMETER-BOUNDS.md)

另有Baek–Balko split-free进口接实际完整split支持：若L为split-free容量、$\nu_{\rm split}$ 为最大顶点不交完整支持数，则 $|X|\le L+(m+1)\nu_{\rm split}$，其中 $L=\sum_{j=m-r+2}^{s}\binom{m-2}{j-2}$。767的L=31；若能普适证 $\nu_{\rm split}\le5$ 可给71，但这项打包上界尚未证明。[split路线及条件](N7_STRATEGY_SYNTHESIS_20261116.md)

## 8. 证据强度、停止点与未闭义务

| 已有证据 | 它支持的结论 | 它不自动提供的连接 |
| --- | --- | --- |
| C8人工接受＋E21完整色表核验 | 限定756域全有限阶上界25，与抽象25点存在性分列。 | 后续39／49／75整链接受、几何实现。 |
| Q75、C49、A39完整解析工作稿 | 相应一般人口工作上界及明确结构进口。 | 新的人工／独立全链接受、取等存在性。 |
| 五锁块CNF审计＋实际DRAT VERIFIED | 精确有限投影排五块，接提取得共同块≤4。 | 原74点母体已排；四块投影就是四份实锁。 |
| 866九洞封包逐核／预算proof重放PASS | 115必要矩阵≥9洞，接原状态／共同标签必要接口给普通866≤61工作声明；九洞向量证明该矩阵最小恰9。 | 61点实际构造、11／12洞、全局318下降；旧93行矩阵精确8仍限于旧矩阵。 |
| 公开八参数finite重放PASS | 已绑定有限目录、压缩块和完整整数树。 | 重建Lean、新抽象packet桥的独立接受。 |
| 九参数紧凑整数重建PASS | 所选原生迹支撑、禁止态扣除与整数列负载。 | 全链数学审阅、458可达、988深三成功。 |
| 小例、必要投影SAT、精确分数可行点 | 相应模型或松弛的具体可行／反例范围。 | 未编码的ambient路径、完整临界母体存在性或几何实现。 |

当前最小未闭义务可以按四条恢复：

1. **七参数费用。** 在每个实际74点母体，生成联合删集／叶中心与标口池／共享臂定向，使同一物理费用≤24，或用更小删后核人口完成反证。57点取等、四路条件支及clean流均作为该共同选择过程的子接口。
2. **八参数耦合。** 在所需全部低缺额预算，控制同一批中性I见证，或给跨C、D部分的联合洞预算；不能把两份单侧最优矩阵相加当新收益。
3. **866更强洞。** 新必要条件须切掉现有115行矩阵的九洞向量，并证明从每个原输入有效；11／12洞杠杆是目标，不是已得输入。冻结九洞milestone，后续更高预算另开附录，保留每条新行的原输入提升及实际checker绑定。
4. **全链接受。** 对39／49／75、八参数迁移、九参数原生装配及11/17后补结构，仍缺相应完整独立数学审阅。现存deep review失败／零读取／空意见回执没有数学结论，不登记PASS，不自动重试。

本轮方向报告的失败独审回执见[原始脱敏证据](../../../../.aris/review-state/claude-review-deep/evidence/27f0c71d864b471a89e81bb54b9786a9.json)；后续总括记录见[锁块稿 §8](N7_N8_COMMON_LOCK_BLOCK_CAPACITY_20261117.md)。requested路由、CLI报告和backend／effort证据分列；未报告后两者仍不可核。本文没有发新外审。

## 9. 恢复和复核入口

### 9.1 接手阅读顺序

先读本交接的对象、数值及保证表，再按实际义务进入原件。7的正面源是owner §7.7、balanced严格容量、最终替锁；8的较强链是EIGHT-CYCLE-TRANSFER与真实finite回执，新的866输入以milestone9为准；9的最终源是direct-cycle-lp/RESULTS及紧凑证书。11/17结构以共同锁块、clean根、真中性流和共享臂原稿末端为准。[事实索引](NMRS_SOURCE_LEDGER_20261117.md)、[结构路线](NMRS_STRUCTURAL_ROADMAP_20261117.md)、[11/16原件索引](N7_STRATEGY_PRIMARY_INDEX_20261116.md)负责导航，不能替代后来更强的原件。

旧STAGE_SUMMARY、11/15综述、幻灯片及较早源索引保留其历史意义；A40、86663、888382、自主327—331、九参数1155／1171等不覆盖本页现用值。尤其同日脚本、排程、receipts或标题本身不是最终研究结果；先检查实际终态、checker及原输入提升。

### 9.2 原有Linux复核命令（本文未执行）

项目代码与solver的执行目标始终为Linux `/data/ktqiu_hdd/math_agent`；以下是已存在的最小复核入口，不是本次重跑记录。它们不重新优化，也不恢复旧求解任务。运行前读取对应REPORT及本地／远端证据存放说明。

九参数紧凑证书只需标准库Python，从Linux项目根执行：

```bash
cd /data/ktqiu_hdd/math_agent/reports/n79-overlap-20261116/direct-cycle-lp
/opt/anaconda3/envs/forktqiu3/bin/python3.12 -B compact_certificate_final.py --check run-988-d2/compact-certificate.json
/opt/anaconda3/envs/forktqiu3/bin/python3.12 -B compact_certificate_final.py --check run-d9-d3/compact-certificate.json
```

预期两项各PASS、exit0；范围是固定证书重建，不是重搜整个目录或另一人复现。[checker源码](../../../../reports/n79-overlap-20261116/direct-cycle-lp/compact_certificate_final.py)、[两份紧凑输入](../../../../reports/n79-overlap-20261116/direct-cycle-lp/run-988-d2/compact-certificate.json)、[D9输入](../../../../reports/n79-overlap-20261116/direct-cycle-lp/run-d9-d3/compact-certificate.json)

五锁块必要投影，按已封存CNF和实际proof复核：

```bash
cd /data/ktqiu_hdd/math_agent/reports/n7-shared-arm-replay-20261117/lock-blocks
/data/ktqiu_hdd/math_agent/cadical-sc2025/build/drat-trim q5/formula.cnf q5/solver-proof.drat
```

预期checker `s VERIFIED`及exit0；逐条编码audit读取[已有原件](../../../../reports/n7-shared-arm-replay-20261117/lock-blocks/q5/encoding-audit.json)。`audit_core.py`会重写部分产物，如要再生审计应复制到独立副本执行，保留封存原目录。[报告及完整范围](../../../../reports/n7-shared-arm-replay-20261117/lock-blocks/REPORT.md)

866共享枢轴八洞证据也在副本重建，因为审计脚本会写核验输出。先从报告目录复制到新的复核工作目录，再在副本运行：

```bash
cp -a /data/ktqiu_hdd/math_agent/reports/n866-joint-holes-20261117/pivot-rows ./pivot-rows-replay
cd ./pivot-rows-replay
/opt/anaconda3/envs/forktqiu/bin/python3.10 check.py
/opt/anaconda3/envs/forktqiu/bin/python3.10 check_bound.py
/data/ktqiu_hdd/math_agent/cadical-sc2025/build/drat-trim budget7/formula.cnf budget7/proof.drat
```

预期30行及84枢轴分支重建PASS、bound audit PASS、DRAT VERIFIED；不把矩阵八洞见证作为实际signotope。[证据原件](../../../../reports/n866-joint-holes-20261117/pivot-rows/REPORT.md)

现用九洞封包主入口：将[milestone9包](../../../../reports/n866-joint-label-order-20261117/milestone9.tgz)解到独立复核目录，进入其milestone9后运行：

```bash
/opt/anaconda3/envs/forktqiu/bin/python3.10 verify.py --directory . --checker /data/ktqiu_hdd/math_agent/cadical-sc2025/build/drat-trim
```

预期PASS，重建115行、11个核、旧93行、最终≤8预算和九洞向量；另含双cell共享pair的两分支单位重放。40件manifest及实际Linux核验已封存。包SHA256为 `33ee393ee26594b805f18d4ea8803ef4a5c5ac382ec2b45a9b29c9c23fd1dad7`，本地与Linux一致。[README](../../../../reports/n866-joint-label-order-20261117/milestone9/README.md)、[原核验日志](../../../../reports/n866-joint-label-order-20261117/milestone9/verification.log)

公开八参数finite的已执行命令及15文件子包身份在[receipt](../../../../reports/n79-overlap-20261116/octagon-source-replay/replay-receipt.json)，原作者入口为 `tools/check_octagon_finite.py --output finite-result.json`；工作目录是Linux `reports/n79-overlap-20261116/schroeder-octagon-replay-20261116/source/es7_es8_bounds_81_319_v1`。输入获取与有界driver见[原件收据 §5](../../../../reports/n79-overlap-20261116/OCTAGON-SOURCE-RECEIPT.md)。未随交接复制完整240MB原包或所有远端大矩阵，本文不是完全离线自包含复现包。

### 9.3 本次交接实际完成的范围

本次对照读取Baek、Baek–Balko、Schroeder、Mojarrad–Vlachos原件及明确写1508的近期文献，未作穷尽查新。本文编写者读取现有证明、最终段落、有限报告及成功／失败回执，用相对链接形成综合稿；没有另运行研究代码、solver、checker、SSH、Lean或外审，科研执行与审阅均沿原始记录。本次新增本文，并由主会话在既有原件索引补入导航；未修改旧证明、原接受记录、任务指针、wiki、Goal、封存CNF／proof或作业，未提交。本次文档交接完成不代表未闭数学目标完成。
