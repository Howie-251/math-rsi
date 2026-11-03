# n62 现有 proof＋SAT 证明链闭合核验

日期：2026-10-11。任务依据：[当前唯一计划第三节](DD82_CONSTRUCTION_FIRST_GOAL_20261011.md)。本项是一次有终点的现有证据核验；不重新求解、不开展新数学研究、不新增 Lean 工作。

**结论：第一类——现有 proof＋SAT 已覆盖全部62点原图。** 在通常的外部精确计算与独立 LRAT 检查意义下，当前材料已经组成完整的计算机辅助不存在性证明：任意有限简单无向62点图，若最大度数不超过8且直径不超过2，必可映入两份已检查 UNSAT 的实际 CNF 之一，矛盾。未发现未闭合的数学覆盖义务、遗漏分支、循环依赖或不保全候选的附加条款。

因此本核验将**数学上的 n62 排除登记为完成**，n62 退出当前研究队列。结合本项目继承的经典63–65排除、Moore界和既有57点构造，数学区间为 **57≤N(8,2)≤61**；58–61仍待解决。该区间没有以新公理加入 Lean。

审阅出处分别记录：本次语义核验为 `review_independence: same-family`、`acceptance_status: provisional`，不是独立跨模型最终审阅。既有精确分类和 LRAT 检查是另行保存的确定性计算证据。完整任意原图到矛盾的 Lean 定理尚未完成，这与上述数学证明是否闭合是不同问题。主代理负责本次整合的 Gemini 复核与全局状态更新；本文件不将尚未发生的复核记为通过。

### 主代理最终装配补记

2026-10-11，本次 Gemini 跨模型复核已经完成并同意第一类结论，未发现数学覆盖缺口。原始回复和返回元数据保存于 [N62_EXISTING_PROOF_GEMINI_REVIEW_20261011.json](N62_EXISTING_PROOF_GEMINI_REVIEW_20261011.json)，thread `9cfb5739-5c30-44f5-b44d-616136923e37`。请求及 CLI 选择为 `gemini-3.8-flash-high` / `high`；元数据来自 CLI 选择，无独立后端模型证明。该补记更新前段的“尚未发生”状态；本地审阅的 same-family 属性保持不变。根代理据已核对的完整材料登记数学排除成立，不把模型同意替代图论证明或 LRAT 检查。n62 本次核验结束，无新增求解、Lean 或证明优化任务。

## 1. 核验范围与采用的最短依赖链

主入口是 [CONNECTED_CANONICAL_COMPUTER_ASSISTED_EXCLUSION.md](../../proofs/dd82/n62/CONNECTED_CANONICAL_COMPUTER_ASSISTED_EXCLUSION.md)。本次实际阅读承重推导与编码，没有以该整合稿的结论、旧审阅 PASS 标签或两个 UNSAT 状态替代证明。

采用的依赖顺序是：

1. 原图计数、实际矩阵恒等式，以及解析 triple-repeat 排除；
2. triangle pairing、D2/BIN 排除、D0组件结构及奇数 double 数，从而存在 D1；
3. hard-D1 与 C4 transport，H、K至少12点；实际组件商恒等式及短组件数界 c≤9；
4. c=3、5、7、9 的完整有限商分类和各存活商的原图矛盾，得到 repeat support 连通；
5. 连通性推出无原图三角形、全体 double 为 D1、奇数 d≤9；
6. 一次合法重标号进入 b=28 或41；实际图扩展到相应保存的 CNF；
7. 与这些输入对应的完整 LRAT 均已独立检查，得到矛盾。

较强的 H、K≥14、后续十二点组件排除链、纯解析替代路线和全套旧七模板 SAT 叶节点均不是本次闭合所需依赖。

## 2. 从任意原图到连通 D1 范围

### 原图基础、triple 排除与局部分类

[RECOVERED_REDUCTION.md](../../proofs/dd82/n62/RECOVERED_REDUCTION.md) Steps 1–3、6 已逐段核对。度数≤7的顶点至多在两步内覆盖57点，故原图八正则。实际矩阵 B=A²+A−7I−J 非负、对称、整值、对角为零，每行和3且 AB=BA；并且每个顶点至多处于一个原图三角形。B是由A定义的实际矩阵，未将可独立赋值的矩阵松弛当作图。

[TRIPLE_REPEAT_ANALYTIC_COMPONENT_EXCLUSION.md](../../proofs/dd82/n62/TRIPLE_REPEAT_ANALYTIC_COMPONENT_EXCLUSION.md) 的新解析论证闭合。旧 Steps 1–3 从一个 triple 构造五个 B-闭合 cell；N的(3,0,0)、(2,1,0)型由强制原图边与正 repeat 冲突直接排除。最后 N=J₄−I₄ 型中，同 ordered type 的两点共有两个固定原图邻点，迫使它们的 Q 条目恰为1；剩余标签边际再迫使三个各8点的**实际连通** repeat组件，每个原图内度为2。加上已分离的2点、4点组件及非空的32点补集，c≥6、tr R≥6，与 c+2tr R=17 冲突。

这里的商恒等式只使用实际 B 的行和、对称性、非负性、AB=BA及原图矩阵恒等式。它不需要 B≤2，故在排除 triple 时使用不循环。可以直接采用 [GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md §3](../../proofs/dd82/n62/GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md) 的解析证明；无需把该文其他章节的更强假设整体导入。旧 triple 有限矩阵/行支撑表完全不参与此闭合。

已核对 [S_TOUCH saturated-row](../../proofs/dd82/n62/S_TOUCH_SATURATED_ROW_EXCLUSION.md)、[triangle pairing](../../proofs/dd82/n62/TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md)、[D2排除](../../proofs/dd82/n62/D2_MATCH_SATURATED_ROW_EXCLUSION.md)、[BIN排除](../../proofs/dd82/n62/D0_EDGE_BIN_SATURATED_ROW_EXCLUSION.md) 和 [D0及D1 outlet](../../proofs/dd82/n62/D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md)。triangle pairing调用 S_TOUCH 的饱和行矛盾时，只需该实际局部父集和行和，不需要全局 B 简单；其三角形配对因此适用于任意当前原图。四圈计数给出 d−T≡1 mod2，三角配对给出T偶数，所以d正且为奇数。任意double端点的父集分类穷尽 D0/D1/D2及BIN/BOUT；D2、BIN已矛盾，若全无D1则各D0闭合四点组件各含两个double，导致d偶数。故D1确实存在。

### 组件数和有限分类的覆盖

[hard-D1](../../proofs/dd82/n62/D1_MATCH_HARD_BRANCH_REDUCTION.md) 与 [C4 transport](../../proofs/dd82/n62/D1_MATCH_C4_TRANSPORT_REFINEMENT.md) 的承重行、支持集和重选重边端点均已核对。它们没有假设 repeat support 连通，也没有假设原图全局无三角形。局部已知三角自由性通过 triangle pairing 传播；r在C4会重根成为D0并与B_ar=0冲突，剩下r在C2/C3的合法互换。没有将原图匹配和repeat匹配认作同一个匹配。

[D1_COMPONENT_MINIMUM_SIZES.md §§1–5](../../proofs/dd82/n62/D1_COMPONENT_MINIMUM_SIZES.md) 的 h=8、10排除及k≥12推导成立；其共同邻点非负预算的每项确实非负。[SHORT_COMPONENT_COUNT_BOUND.md](../../proofs/dd82/n62/SHORT_COMPONENT_COUNT_BOUND.md) 只需这些早期h,k≥12。H=K时内度至少4直接给c≤9；H≠K时packing只剩c=11需要排除，其(12,14)/(14,12)平衡不等式和(12,12)余下八个4点、一个6点组件预算均正确。

[CONNECTED_REPEAT_REDUCTION.md](../../proofs/dd82/n62/CONNECTED_REPEAT_REDUCTION.md) 的有限分类，采用实际原图商必满足的整值、平衡、行和、迹及完整二次矩阵恒等式。已读分类源码与既有独立检查结果；没有重跑枚举。

| c | 精确分类域及保存结果 | 分类后原图排除 |
|---|---|---|
| 3 | 正偶数组件大小允许2；45种行、9,108个迹合格矩阵，18个标号解、3个轨道 | (6,24,32)、(8,24,30)、(12,20,30)各自矛盾 |
| 5 | 大小≥4；221个大小分拆，2个标号解、1个轨道 | 大小(4,8,10,20,20)，4点组件有原图内度1，强制不存在于列表的6点伴随组件 |
| 7 | 大小≥4；201个大小分拆，6个标号解、1个轨道 | 大小(4,4,4,10,10,10,20)，同一4点→6点论证 |
| 9 | 大小≥4；94个大小分拆，零解 | 商本身已不可能 |

源与结果：

- [check_three_component_quotients.py](../../computations/dd82/n62/check_three_component_quotients.py)、[完整检查结果](../../computations/dd82/n62/three_component_quotients_check.json)；
- [component_quotient_search.py](../../computations/dd82/n62/component_quotient_search.py)、[独立stars-and-bars检查源码](../../computations/dd82/n62/check_large_component_quotients.py)、[完整独立检查结果](../../computations/dd82/n62/large_component_quotients_check.json)；原始输出为同目录 `component_quotients_5.json`、`_7.json`、`_9.json`。

覆盖核对的关键处是：固定大小后，gcd参数遍历每个平衡非负行和对应列；行和及二次对角式的剪枝均为必要条件。列由平衡完全确定，所以两行被选中时检查完整有序非对角式不依赖未选行的猜测。独立程序用不同的行生成和前向过滤，保存了全部3,358个行域相等、全部大小分拆完成及最终矩阵等式检查。原程序的 `necessary_D1_pairs`/H,K≥14 只在接受矩阵后作注记，**没有用于筛掉候选**。此处不存在遗漏无D1标记商或额外组件数的补集。

[THREE_COMPONENT_EXCLUSION.md](../../proofs/dd82/n62/THREE_COMPONENT_EXCLUSION.md) 及三个独立证明均已读：

- [6/24/32](../../proofs/dd82/n62/THREE_COMPONENT_6_24_32_EXCLUSION.md)：唯一表示的父对及三步周期强制24点组件中的原图三角形，triangle pairing要求其repeat组件仅6点，矛盾。
- [8/24/30](../../proofs/dd82/n62/THREE_COMPONENT_8_24_30_EXCLUSION.md)：两四圈、对顶父对和零交叉repeat的唯一表示，使同一repeat行必须提供两个仅在零权匹配点相交的权重2集合，总权至少4而行和3，矛盾。
- [12/20/30](../../proofs/dd82/n62/THREE_COMPONENT_12_20_30_EXCLUSION.md)：采用整合文§3明示的短接口排除12点组件里的double，接源文§§1–4即可。辅助加权图连通性的商迹矛盾、incidence核至多一维、核方向的整值特征值、最终多项式迹导致−3重数7/2，均已核对。不使用源文旧的H≥14入口。

[FIVE_SEVEN_COMPONENT_QUOTIENT_EXCLUSIONS.md](../../proofs/dd82/n62/FIVE_SEVEN_COMPONENT_QUOTIENT_EXCLUSIONS.md) 只需D1重组件已有六个不同顶点、D0四点组件及其6点unit-prism伴随，不需后来的大组件下界。三角配对阻止4点组件中的顶点处于原图三角形；其原图内边权B=0迫使另一对为double，于是必须D0。这正确排除两个列出的商。

因此只剩c=1。原图三角形会产生闭合6点repeat组件，D0会产生闭合4点repeat组件，故此时两者均无。generated unit triangles两两不交，D1轻配偶不处于任何unit B三角形，且其完整行无double；故2d个D1端点的轻repeat incidence全部落入D和generated三角集合的补集。每点容量3给17d≤186，结合d为奇数，得到d∈{1,3,5,7,9}。这些是原图的推论，不是为SAT额外假定的条件。

## 3. 两个规范输入没有遗漏候选

[D1_MATCH_CANONICAL_DIAGNOSTIC_COVERAGE.md](../../proofs/dd82/n62/D1_MATCH_CANONICAL_DIAGNOSTIC_COVERAGE.md) 与 [对应JSON](../../proofs/dd82/n62/d1_match_canonical_diagnostic_constraints_20261011.json) 已与实际归档D1_MATCH父映射比较。

先用2↔3将r送到C2；再用5–8的父类置换将c送到C5；再用剩余6–8置换规范b的父类。这给b=W4、W5、W6三种覆盖代表。各普通类内只固定已有证明相异的有序点对，故可以同时得到JSON中的r=16、u2=17、p=22、u3=23、q=29、c=35等标号。这里使用图的重标号，没有要求原标号图存在所称自同构。

b=W5被共同邻点方程排除：B_5r=A_5r=0且N(5)={0}∪C5，使r在C5恰有一个原图邻点；但b,c是两个相异邻点，不能同时在C5。故只剩 **b=28、41**。s、t、g和允许范围内的f仍自由；尤其未偷偷固定s=p、s≠p、t=q，或识别两个匹配。b=28下可进一步推出t不在C4，但实际JSON保留较宽范围，属于安全弱化。

## 4. 实际原图确能满足所保存CNF

已核对 [CNF_BRIDGE_OBLIGATIONS.md](../../proofs/dd82/n62/CNF_BRIDGE_OBLIGATIONS.md)、归档 `code/n62/n62_ab_cnf.py` 的所有承重子句函数、实际D1_MATCH模板、[旧canonical driver](../../computations/dd82/n62/d1_hard_diagnostic.py) 和 [connected driver](../../computations/dd82/n62/d1_connected_diagnostic.py)。独立的短只读子审阅 `/root/n62_existing_proof_check/cnf_evidence` 也检查了同一接口并未发现误剪枝，已结束释放代理槽；其结论仍是same-family/provisional。

正向赋值是具体的：edge变量取实际邻接，B1/B2取实际repeat值的指示，tau取实际三角状态，所有AND、XOR和前缀阈值辅助变量取其定义值。89个固定pair与1,802个动态pair穷尽所有无序点对。实际D1模板满足剩余度数=8−父数、singleton classes等于实际单父类；此结论针对这份具体JSON，不泛化为任意通过有限schema检查的JSON。

基础编码的共同邻点拆分包括所有例外父集。repeat行计数中B2重复两次是正确权重；B1/B2互斥保证各guard状态完备。guarded exact counter的所有调用都达到所需阈值深度：core target≤3而保留到4，triangle target≤2而保留到3。第四共同邻点阈值为假的单位条款来自B≤2，未额外剪枝。D1模板没有simple-B分支的奇三角XOR。

旧driver的完整行确实把未列项置零；部分行仅在明确支持集之外置零、在每个互不交组里要求恰一个B1，且B2为假。它另加的B(C1,其余非C2/3/4点)=0、B[C2]=0、B(C3,C4)=0分别由hard-D1和C4文稿导出；A[C1]至A[C4]为零来自对应父顶点三角自由性，指定十二个tau-false也有局部证明。

新driver只再加两项：全62个tau为假；无序double总数d≤9。固定89对中的唯一double是(0,9)，每个动态pair有一个B2 selector且只计一次，故d=1+∑B2，所加动态界∑B2≤8正确。新鲜阈值变量以标准前缀计数递推定义，否定最终第九阈值；任意满足该界的实际selector赋值都有辅助变量扩展。没有增加连通性编码、未证明的奇偶条款或历史symmetry breaker。

实际文件对应也已有完成证据：[regeneration_verification.json](../../computations/dd82/n62/d1_connected_diagnostic/regeneration_verification.json) 与 [再生成源码](../../computations/dd82/n62/verify_d1_connected_regeneration.py) 保存了从完整归档编码器经两个driver生成后，与全部七份base/canonical/connected/added文件**逐字节比较**一致及完整map一致的结果。程序的比较确实读取双方直到文件末尾，并非只比header、变量数或条款数。该记录于既有任务中5.244秒完成；本次复用，不重跑。

## 5. 完整证书与相同输入的对应

证据目录为 [d1_connected_diagnostic](../../computations/dd82/n62/d1_connected_diagnostic/README.md)。原求解JSON保留历史 `RAW_UNSAT_WITH_UNCHECKED_LRAT`；当前证书状态来自另存的 [certificate_checks/results.json](../../computations/dd82/n62/d1_connected_diagnostic/certificate_checks/results.json) 和两份完整检查日志，不能由早期RAW字段推断当前仍未核验。

| 代表 | 实际CNF header | 完整 `.bounded120.lrat` 大小 | 保存的独立检查 |
|---|---|---:|---|
| b=28 | 444,839变量；1,633,418条款 | 86,914,031 bytes | exit20，`s VERIFIED`；检查1,344,762个新增条款 |
| b=41 | 444,839变量；1,633,419条款 | 109,304,664 bytes | exit20，`s VERIFIED`；检查1,463,908个新增条款 |

两份现存CNF及完整LRAT存在；当前header、文件大小与保存记录吻合。日志明示读取对应CNF路径和对应`.bounded120.lrat`，以官方arminbiere/lrat-trim 0.2.0 `--no-trim`检查全部新增条款，不是仅做proof trimming。[检查driver](../../computations/dd82/n62/check_d1_connected_certificates.py) 同时要求exit20与完整行`s VERIFIED`才记录成功。[来源与构建记录](../../.tools/dd82-lrat-check/source_and_build.json) 保存官方release、版本及带assertions构建/上游测试成功信息。

这里调用的是已完成、分别约1.106与1.459秒的独立证书检查。五秒profile的22,765,568-byte部分LRAT不作为证书；没有把UNKNOWN、CPU_LIMIT、solver exit20单独当作证明。本次没有重放检查器或求解器，也没有重新审计外部检查器的全部C实现；这是普通外部LRAT证明检查的证据范围，而不是Lean内核求值。

结合§4的正向扩展，若任意原图存在，则两份具体CNF之一可满足；本节的已检查UNSAT与之矛盾，完成全称排除。

## 6. 旧路线、文稿旧状态与剩余正式验收

已读归档 `interrupted_ab_pilot_progress.json` 和 `final_s_disjoint_progress.json`：前者45/56、`global_result=UNRESOLVED`，后者80/80、`ALL_SELECTED_RAW_UNSAT`。这些是旧执行记录，不是当前完整证书；旧提取包中缺失的原DIMACS/maps/叶条件/proof不由汇总JSON补造。**缺少旧材料不等于旧证明错误**，本次也不就未取得的旧完整路线作否定判断。

本次闭合采用的是已经具备现行数学归约、具体输入再生成对应和完整已检查LRAT的较短新路线。它不要求补齐旧七模板RAW档案，也不把新canonical两份证书冒充旧七模板证书。若干分支文稿中的“尚未排除全order62”“待独立审阅”以及bridge文稿早期工具可用性描述是其各自写作时的范围/状态快照；当前整合结论由本文件给出的组合证据支撑，无需修改旧证明内容来成立。

没有发现需要新数学、新求解或更强组件界才能补上的义务。需要后置的工作是完整Lean连接：实际原图归约和有限分类接口、canonical图到确切子句列表、这些确切LRAT的内核检查与主定理装配。未完成Lean不构成本次计算机辅助数学证明的缺口。

本项已到终点。除非出现新的具体相关错误或实质文件变化，不再重复开启n62现有证据核验或n62证明优化；本文件不分派新的n62任务。
