# 从 Property B 与 ECC 实际研究提炼的六条跨阶段转折

2026-11-01。本文只读 MathRSI 已收录的项目材料，给工作流重设计提供实证动作。没有启动研究、调用模型、运行数学计算或工具链，也没有访问 `aris4math_v2`。下文“实际执行”均指明确引用的历史记录，不是本轮复现。

## 阅读边界与材料位置

为避免历史绝对链接把读者引回旧工作区，下文统一用两项仓内前缀：

- **PB/** = [`plugins/propertyb/knowledge/archive/`](../../plugins/propertyb/knowledge/archive/)。这是实际证明、Lean源与过程报告的只读归档；其中各文件自己的相对链接可能保留源项目路径，本报告只引用本仓确实存在的入口。
- **ECC/** = [`PB/context/mathrsi-ecc-20261101/sources/ecc/`](../../plugins/propertyb/knowledge/archive/context/mathrsi-ecc-20261101/sources/ecc/)。现收录9份交流源材料，包括旧43/10结论、ECC经验、新题规格/进展及九尾压缩报告；不是全部生产计算证据。
- **ECC原交接/** = [`development/context/ecc-source/`](../context/ecc-source/)。后来补入两份原样快照：独立领域交接 `MATH_RSI_DOMAIN_HANDOFF.md`与旧题人工查验 `HANDOFF_FOR_REVIEW.md`；本文已回读其原命题、覆盖、全域补验、转折与复现边界段，案例1–2现在优先直接引用它们。

本轮完整读了仓内 [`development/context/MATH_RSI_ECC_COMPARISON.md`](../context/MATH_RSI_ECC_COMPARISON.md)、ECC旧题结论与经验、`PB/context/mathrsi-ecc-20261101/proof-contract/EVIDENCE.md`、独立交接核对/增量，以及下文各过程报告和短证明；对较长的 Property B 一般证明读取了与本次转折有关的定义、算法、RS/FKG/积分连接、最小反例、团界和主定理段，另读相关进度与完成记录；对Lean只静态读取具体caller及导出，不声称逐行审完整工程。

本报告初稿依据已有交接核对与9份ECC交流源；两份原件补入后已静态回核原件相应段落，没有沿其中绝对链接访问v2。ECC全生产扫描、pair流与原始全部运行日志仍未随这些阅读材料带入，不能把本次阅读升级成43/10数学复验。原件中的运行命令是历史复现说明，本轮没有执行；`proof-contract/EVIDENCE.md` §5补充说明交流包和生产现场证据的差别。

这六例不证明新工作流已经有通用提速；它们说明：实际哪些行动使旧研究向原题推进，哪种返回点不能被一张技能名称表替代。每条最后的操作是应写入 MathRSI workflow 的提炼建议。

## 1. ECC 43/10：把“文献有172类”变成任意原目标到实际172输入的覆盖

### 原对象和当时缺口

原题是：是否存在GF(2)秩10的 `10×43` 矩阵，使全部1023个非零消息重量≥17。原域允许零列、重复列与任意坐标顺序，没有循环结构、hull或固定种子限制。项目最终由规格允许的不存在性分支解答，不能把目标换成“这批候选矩阵都不行”。

文献分类结果给满支撑 `[40,7,18]` 的172个坐标等价类。它本身既没有说明任意43/10目标能进入这个对象域，也没有把抽象类变成程序实际可读的目录。这里必须先完成数学归约，再证明目录覆盖，而不是先跑172份文件就称全题穷尽。

### 实际做了什么

假想目标先偶扩展为 `[44,10,≥18]`。利用E1 no`[41,8,18]`与Griesmer证明任意三列独立；用MacWilliams与精确四次多项式推出对偶重量4数量 `B4≥12`。选择**一个重量4对偶字的支撑**，其四列秩恰3，缩短得到 `[40,7,18]`。还证明母码满支撑：外列若落在尾列张成空间会违反三列独立。这一步使E2的对象/前提实际适用。

随后核172份实际矩阵的秩、全部127个非零重量、偶性与满支撑；用完整码字—坐标关联图证明两两坐标不等价。**实际172个合格互异类＋文献至多172类**才推出目录覆盖。代表的发现可以是启发式，完整性依靠这个组合，不靠搜索器自报“找完了”。

### 实物与范围

优先直接依据[旧题原始HANDOFF](../context/ecc-source/HANDOFF_FOR_REVIEW.md) L11–25的原量词、L41–66的完整归约/分类/两项进口，以及[独立领域原交接](../context/ecc-source/MATH_RSI_DOMAIN_HANDOFF.md) §3.1、§3.3。补充入口：[ECC旧题结论](../../plugins/propertyb/knowledge/archive/context/mathrsi-ecc-20261101/sources/ecc/results/NONEXISTENCE_43_10_17.md) L3–20；[证明合同/实际证据读录](../../plugins/propertyb/knowledge/archive/context/mathrsi-ecc-20261101/proof-contract/EVIDENCE.md) §1的原矩阵→偶目标→三列独立→重量4→满支撑母码→实际目录，及§2进口定位。后者记录原完整证明§7–15、历史`COMPUTATIONAL_COVERAGE.json`与`manifest_check.json`的准确职责，不是本轮生成的新证书。

E1原文核读的是Bouyukliev学位论文Theorem6.3、印刷p.147/PDF149；期刊对应结果并不意味着同一个定理编号可搬到期刊。E2所需的是满支撑类上限，项目没有重新证明原作者历史分类完备性。成员合法、互异、原始矩阵到母码的归约和文献类上限，是四项不同事实。

### 尚未解决什么，以及workflow应执行什么

到目录闭合时，还没有排掉任何母码的全部延拓，更没有得到原题不存在。下一动作是从**同一个**目标构造合法尾扩张与完整陪集域。最终43/10完成保持文献与普通软件信任，不是全链Lean。

**落到准备/文献与 prove：** 文献读取产物必须返回“所用准确命题及前提”，随后prove安排“任意原对象是否满足这些前提”和“实际目录能否吃进抽象对象”的连接义务；文献发现不是在准备阶段存完PDF即结束。得到实际完整目录立即交给下一个延拓caller，不继续重做代表发现。

**落到 verify：** 验证目录时分别消费成员核验、互异性、外部上限与归约覆盖；不能给整个ECC领域挂一个统一verifier布尔值。这是已解项目实际采用的覆盖方式，不应被“所有生成器都必须穷尽”的新规则否定。

## 2. ECC 43/10：成员检查不足，补第二全域F后又在“无边”处及时收束

### 原对象和当时缺口

对每个已覆盖的母码K，清零7个枢轴后，偶陪集商空间恰有 `2^32` 个唯一代表。新增三行需满足单行/两行阈值16、三行阈值14，尾基是偶 `[4,3,2]`。合法单行集记 `F_K`。检查保存的F元素都合法，仍不能证明生成器没有误删一个未来可扩张的元素。

### 实际做了什么

独立领域原交接§4.2明确记录：早期独立检查只核保存的成员与部分区块，跨家族审阅指出它不能支持“两套独立全域”的说法；当时没有发现真实漏项，欠的是针对漏删的独立完整执行。项目随后补做第二套**重新遍历完整域**的实现，使用不同主元、不同偶商基、Gray遍历与实际40位距离；完整阶段不借旧F决定接受或拒绝。首个全域实例实测11.536726CPU秒，确认可行后扩到所有172例。每母码两套都完成全部 `2^32`，转到共同规范后比较完整向量集合。每套总计 `738,734,374,912` 个代表，最终共留下429,024个F代表。

接着把三行条件改成同一个F集合上的兼容图：两代表之和距离≥16才连边。任何合法三行延拓必须给三个不同顶点与三条边。实际全部172图**无边**，因此比“无三角形”更强的便宜必要条件已经结束整条延拓义务；不再扩算三重和或三行组合。

全部619,053,789个无序pair各保存母码真实消息，使该pair和加对应码字重量<16。统一checker逐pair重算、检索顺序/生成基绑定、验证严格EOF；它重放拒绝事实，不需要相信搜索器最小值。第二全域F补“没漏”，逐pair低权见证补“拒绝正确”，都核完后才回到原43位量词收束。

### 实物与范围

直接过程依据是[独立领域原交接](../context/ecc-source/MATH_RSI_DOMAIN_HANDOFF.md) L99–113（§4.1–4.2）：从完整分类到便宜联合门、早期独立核验范围不足、首例实测与整172例修复。实际复现合同见[旧题原始HANDOFF](../context/ecc-source/HANDOFF_FOR_REVIEW.md) L98–107（只读回绑定）、L111–161（完整F和全pair不同操作）、L163–175（review具体贡献及未执行范围）。补充[旧题结论](../../plugins/propertyb/knowledge/archive/context/mathrsi-ecc-20261101/sources/ecc/results/NONEXISTENCE_43_10_17.md) L22–36写尾阈值、完整域、图、两实现规模与全部pair见证；[证明合同](../../plugins/propertyb/knowledge/archive/context/mathrsi-ecc-20261101/proof-contract/EVIDENCE.md) §1、§3、§5分清逐例绑定、full-F scans、pair replay与当前阅读包。

原生产全pair见证流约1.68GB，不在本仓9份ECC源中。本轮没有重放它。历史`DELIVERY_CHECK`/dry-run没有启动扫描，不可当真实全域执行；历史pair native result则确实执行172例全部pair，但 `F_domains_rerun=0`。这些不同记录不互相覆盖。

### 尚未解决什么，以及workflow应执行什么

这些工作与案例1组合才完成不存在性；单独F完整或pair证书都不能代替原目标归约。结合已验 `[43,10,16]` 构造得到 `d₂(43,10)=16`，信任基础仍是sound-modulo-imports-and-computation。后来的45/11参数问题未由此解决。

**落到 prove→局部verify→prove：** 主代理提出具体“无遗漏”疑问后，verify只补足该义务，交回完整F与绑定供pair caller使用；不重选研究路线、不重做文献、不提前进入handoff。第二程序必须解决缺口，不能仅再次循环已有F来冒充无遗漏。

**落到 prove/assemble：** 一旦所有兼容图已无边，立即用已证明的必要条件返回原题，停止更贵的三行搜索。工作流应有“当前较弱必要条件已足够推出目标，就消费并结束更强子任务”的动作，而不是要求固定菜单做到底。

## 3. Property B T33：混合24点数值通过后，先建真实caller，再回仅余23点的原题

### 原对象和当时缺口

T33目标是所有有限简单五元超图、边数≤33均可二染，即 `m(5)≥34`。内部24点分支取恰33边、点对覆盖。早期五锁局部型取两个六度、三个七度点、两两共度1。局部Fraction证书或“所有这种profile算过”尚不能保证原H确实给出这些profile、实际坏对与配额。

### 实际做了什么

先实现一个非平凡真实caller `TwentyFourRefinedExample.propertyB_of_mixed_quad_trace`：输入实际 `H`、五个真实点、实际度数/共度与大迹分支，构造完整真实profile，证明avoid-quota和容量罚项，返回 `PropertyB H`。其精确界是 `75163/75582`；它没有把profile、numeric loss或quota留给调用者假设，**但还留有真实大迹分支前提**，必须由selection/classification供给。

随后完成整个混合五锁分支：单位共度使大迹最多两个，完整32个带标签可能；从同一H的总边数、度数和10个共度恢复所有重数；给实际六度中心选真实坏对，映入完整8-slot列表；**两份实际坏槽先固定，再选48个配置中的位置**；用真实双向权重、avoid配额、dual罚项接回原H。完整选择映射覆盖 `32×8×8=2048` 个padding输入，48个profile、210条loss行，最大严格界 `75421/75582`。

24点最终caller闭合后，构建Assembly和独立Fin24导入。此时没有宣称T33完成，而是明确 `Target33 ↔ RemainingGoal`，remaining只要求23点、恰33边、点对覆盖实际超图可染。原题推进回23点真实六分支，不停在24点审阅或文档上。

### 实物与范围

直接源码：[TwentyFourRefinedExample.lean](../../plugins/propertyb/knowledge/archive/formal/Aris4Math/ThirtyThree/TwentyFourRefinedExample.lean) L5–8、36–50、104–146；输入与输出的实际类型尤其在L127–146。完整分支实物：[mixed/REPORT.md](../../plugins/propertyb/knowledge/archive/context/propertyb33/round02/mixed/REPORT.md) L9–73，记录1010jobs及独立import、完整带标签域、实际槽、Fraction与kernel职责。下一转折：[twentyfour-complete/REPORT.md](../../plugins/propertyb/knowledge/archive/context/propertyb33/round02/twentyfour-complete/REPORT.md) L3–26，明确1065jobs、原染色和仅余23点。

这些仓内报告链接的历史logs没有全部随归档复制；本轮核对的是完整过程报告和实际caller源，不声称重新执行或逐表二次复算。历史1010/1065jobs指具体增量构建，不是整题从零构建时长。

### 尚未解决什么，以及workflow应执行什么

单个mixed-quad caller不覆盖全部24点；完整24点caller也不证明23点。`Target33 ↔ RemainingGoal`是准确剩余，**不是RemainingGoal的证明**。T33后来确实完成，见案例6；不能用后来的完成回写这一中间产物“当时已解”。

**落到 prove：** 在批量表/模块投入前，先拿一个非平凡原H caller试通“实际输入→重数/配额→结论”。它暴露并固定接口，之后才批量复用。这不是把所有数学都编Lean，而是用真实调用检验当前方法到底有没有可消费的输出。

**落到 verify：** 高风险局部核验通过就返回原prove，连带给出明确remaining。不要把局部完成提升为全主定理验收，不要自动handoff；同时不要因主定理未闭而贬低这个完整分支的长期价值。

## 4. Property B 36研究：停止旧位置松弛，改用唯一坏边与平衡交换，只关闭≤18点

### 原对象和当时缺口

新研究目标是任意有限简单五元超图、边数≤35均可二染，即 `m(5)≥36`。旧18点局部双锁/三九度位置松弛未消去完整小点数义务。继续为同一松弛加更多布局并不等于原域缩小；这里缺的是能处理整类的论证。

### 实际做了什么

转到全部平衡染色状态 `Ω={R⊂V:|R|=9}`。假定每个状态都有单色边，从总事件数S得到唯一事件状态下界 `U≥2N−S`。对唯一单色边e做标签交换 `(x,y)`，45个交换都破坏e；原反例假设保证目标状态至少新生一条单色边，给带标签变换的双计数矛盾。

按两边交大小 `t=0…4`，精确算新事件计数 `K_t=(50,1548,810,1320,990)`。对 `m≤36`，`45(97240−1430m)≥2059200`而`1548m(m−1)≤1950480`，相差至少108720；得到18点平衡二染，再添孤立点/限制回原域，覆盖全部≤18点。两份直接计数程序独立检查固定交大小代表的715个全红源状态和45交换；完整实际边对的覆盖由重标号双射证明，**没有枚举全部超图**。

### 实物与范围

完整自含证明：[SMALL_VERTEX_SWAP.md](../../plugins/propertyb/knowledge/archive/proofs/propertyb35/SMALL_VERTEX_SWAP.md) L5–39是一般修复双计数，L41–109是原超图caller，L111–121说明独立计数和模型静态范围。由旧方法转到新方法的过程依据：[PROPERTY_B_RESEARCH_LESSONS.md](../../plugins/propertyb/knowledge/archive/research-wiki/PROPERTY_B_RESEARCH_LESSONS.md)开头“2026-10-19具体换线经验”。原研究准确未完成状态：[PAUSE_HANDOFF_20261021.md](../../plugins/propertyb/knowledge/archive/context/propertyb35-paper/PAUSE_HANDOFF_20261021.md) L8–22、43–74。

### 尚未解决什么，以及workflow应执行什么

这个局部定理实际上处理≤36边、≤18点，足够服务目标≤35边的小点数分支，但**不覆盖19–25点**；36全题仍有八类主要数学义务，暂停交接明确“不是只差排版/Lean/最后小引理”。小点数新法无Lean，不能据其它T33/一般定理Lean迁移其形式状态。

**落到 route-loop：** 连续试验只在旧松弛内局部变好时，用整体义务重新提问，改变状态对象和计数机制（从位置坏对界到唯一坏边的有标签交换），做足以区分可行性的短精确复算。该动作应产生可交prove的具体定理与caller，而不是只让reviewer打分或增写计划。

**落到 prove：** 证明新小点数定理后，立即从全局剩余中删去≤18点并继续19–25；保留旧失败边界。route-loop只选方法，局部verify只验新定理，二者都不能把八类剩余隐去。

## 5. Property B 一般k：回原文发现RS已有精确项，再改实际单交图获得统一增益

### 原对象和当时缺口

目标由逐个小k扩成某个明确整数范围K内**每个k、全部有限简单k元超图**的更强下界。早期有无锁/一锁包络数值、修复路线与相对旧RS判据+1候选，但“比一个宽松旧式好”不等于比适用文献界强，有限数表也不证明统一k命题。

### 实际做了什么

先重读RS原算法与证明，确认FKG初态项和精确单交积分原文已有；不能把保留这些项当作本项目新贡献。正文准确拼合Appendix A ClaimA.1与Claim2.4证明中的未编号积分，作用在**同一个实际slow recoloring算法**，保留实际有向单交边对数γ(H)。这是本文组合估计，不冒称文献某条原名定理。

再取原假想反例的最小顶点商，使点对覆盖成为内部结论，得到顶点数上界。将同一实际边族构成单交图S(H)，用关联矩阵Gram证明团数限制，再用公共点/无公共点的经典线性交族二分加强：有公共点时`q(k−1)+1≤v`，无公共点时`q≤k²−k+1`。团界经图论边数界给γ(H)真正削减，代回**同一严格RS参数见证**。随后证明RS最大整数预算B_RS非空有限、整数增益Δ的统一严格性，回到所有原超图。

### 实物与范围

早期未闭与下一步：[propertyb-general/PROGRESS.md](../../plugins/propertyb/knowledge/archive/context/propertyb-general/PROGRESS.md) L51–73；这里明确首轮已有FKG/积分，浮点/Decimal未作严格证书，停止扩大扫描，完整实际连接/强基线比较尚缺。

实际规范：[CORE_THEOREM.md](../../plugins/propertyb/knowledge/archive/proofs/propertyb-general/CORE_THEOREM.md) 定义3及引理1.1–1.3、L181–220的同一算法组合与原输入约化，L248–311的Gram/实际单交图及无附加结构定理；[CLIQUE_REFINEMENT.md](../../plugins/propertyb/knowledge/archive/proofs/propertyb-general/CLIQUE_REFINEMENT.md) L8–79完整公共点二分及实际H调用，L81起统一增益。该规范后来已经更新到k≥12，不能把它的当前头部误读成早期首轮即证明12起点。

纸面完成时的准确实证：[round02/COMPLETION_AUDIT.md](../../plugins/propertyb/knowledge/archive/context/propertyb-general/round02/COMPLETION_AUDIT.md) L7–29，记录当时k≥17的主定理、18源单位/78义务审计、实际原H连接与模型范围；93个小图/618304重染等只是查错，统一定理由解析论证承担。后来完整主定理C的Lean见[形式化验收](../../plugins/propertyb/knowledge/archive/context/propertyb-general-lean-growth/COMPLETION_AUDIT.md) L3–12；更后k≥12范围见[general/PROGRESS](../../plugins/propertyb/knowledge/archive/context/propertyb-general/PROGRESS.md) L7–19。

### 尚未解决什么，以及workflow应执行什么

首次新γ候选没有自动完成B_RS优化最大性、严格整数增益或文献包络比较。纸面一般结果完成时Lean尚非该Goal前提；后来另完成主定理C形式化，比较D/E仍纸面（E仍k≥256）。不得把C的Lean说成整个比较也已Lean，也不得把限定的零锁必要松弛失败写成所有潜在Grill方法不可能。

**落到准备/文献→route-loop：** 文献搜索不仅找支持，还要回证明核当前“新改进”是否已被原文保留；修改baseline与贡献判断，再带着同一原对象提出真正新结构。关键进口的具体适用性需要prove接，不是只存书目信息。

**落到 route-loop→prove：** 数值包络停算之后，交付的应是“哪个实际量可加强、需要哪些精确lemma、如何用同一参数回原结论”的路线，不是下一批k扫描清单。prove再完成解析统一量词和整数严格性，assemble/verify各自核全链与比较范围。

**落到 verify/handoff：** 保留纸面数学验收、主定理Lean、比较纸面、查错计算及展示的不同范围；最终实际强结果已经成立时，不为统一最高验证级别重开旧研究。

## 6. Property B T33最终：真正消去RemainingGoal、指名新Main，再只修正文的两处说明

### 原对象和当时缺口

案例3之后原题尚余23点实际超图。条件caller已能路由，但把unfinished branch proposition当参数的 `TwentyThreeConditionalCaller`、`FinalStatementConditionalCaller`只是接口探针；它们能编译，不是原目标的无条件证明。默认Lake目标仍是旧T32 Main，不能用它宣布新T33完成。

### 实际做了什么

23点由实际总度预算分r=0、1、2、3、≥4个六度点。r=1继续按是否存在七度坏伙伴分两支：从实际低点集合取顶点；有坏伙伴直接用已证分支，无坏伙伴则结合点对覆盖和共度<2证明所有相关共度=1，供全单位分支。六支分别返回原 `PropertyB H`，组合成只剩H、pair coverage、33边的 `twenty_three_propertyB`，交Assembly再去除内部条件。

新 `ThirtyThree/Main.lean`最终导出 `propertyB_of_at_most_thirty_three : Target33`，没有点数、pair covering、度数、profile、probability、certificate或RemainingGoal前提。显式执行 `lake build Aris4Math.ThirtyThree.Main`，1138jobs exit0；构建后 `ReviewAudit33.lean` 从裸 `[Finite V]`与`Finset (Finset V)`复述原Bool染色、每条边两色出现及不可染≥34，exit0；8项传递公理仅标准三项。

完整正文fresh审查又发现两处**说明性**错误：21点最大界应为3292/3315；三低完整有标签域是1796，844仅规范低预算域。先确认Lean实际覆盖全11×3×131，修正文与对应差异，不修改正确Lean、不重开数学路线。原frozen-input WARN保持原始记录，最终问题处置与当前完成分开；Grok/Gemini最终静态阅读范围、第一次Gemini失败亦原样保留。

### 实物与范围

最终分支地图：[round02/REPORT.md](../../plugins/propertyb/knowledge/archive/context/propertyb33/round02/REPORT.md) L9–23。实际23分派与原题归约：[final-assembly/INTERFACE_MAP.md](../../plugins/propertyb/knowledge/archive/context/propertyb33/round02/final-assembly/INTERFACE_MAP.md) 的23-point partition、Whole finite domain、Independent spelling；最终[REPORT.md](../../plugins/propertyb/knowledge/archive/context/propertyb33/round02/final-assembly/REPORT.md)记录命令、原始目标、默认旧入口、conditional probes与增量构建范围。正文修正及最终审阅：[final-audit/PROOF_AUDIT.md](../../plugins/propertyb/knowledge/archive/context/propertyb33/round02/final-audit/PROOF_AUDIT.md) L3–40。

本仓归档含实际Lean源、接口与完成报告，未带这里所引全部运行log；这是本轮阅读证据的限度。历史报告明确本机增量构建与独立复述，不声称第二台机器或他人独立复现。Grok/Gemini没有执行Lean；HTML1049公式/9表及手机桌面检查只证明展示保真。该题确实完成的是 `m(5)≥34`，不是等号，也不是后来35/36目标。

### 尚未解决什么，以及workflow应执行什么

此T33原命题和其规定交付已经完成；不能因保留的条件probe或早期“23点未闭”快照重开搜索，也不能把模型review或12.5秒增量Main的时长当成从零证明成本。后来T34纸面候选/35Lean暂停与T35→36未解是别的任务，不能自动接着启动。

**落到 assemble：** 消费实际六分支而不是分支数目或条件类型，逐一核上游如何供给前提，最后消去RemainingGoal；这是完整装配的实物标准。

**落到 verify：** 指名当前新模块并独立原题复述/type/axioms；抽象Target符号、默认build或无sorry文本搜索都不够。正文小错据实际已核数学定向修复，检查受影响处；不要因审计指出“数目说明错误”就把所有数学重新送route-loop。

**落到 handoff：** 完成记录替换导航中的在途状态，旧错误/失败保留原记录但不作为当前状态；对外说明已证明范围、实际review/build/reproduction层级和复现入口，然后结束这道题。

## 最该补进主workflow的行为

最重要的是**带着剩余义务返回调用方**。真实项目不是“提出方法→证明→验收→交付”走一遍：T33局部实际caller通过回prove，再闭整个24点后回仅余23点，最后才进入全局Main；ECC独立F核验回pair caller、pair无边后直接原题收束。每次返回必须使当前原命题的下一行动改变，而不是让主代理再开一轮架构讨论。

其次，路线改进必须给出一个可以马上检验的数学操作：用固定真实坏对选择位置、以唯一坏边交换覆盖整类、用文献原算法中的实际γ连接团结构。证明推进负责把这种操作接到真实输入；验证负责核具体缺口，不能在每次验证前重新做全路线评审。

最后，完成与继续取决于**本次产物解决了哪个量词义务**：完整目录不等于扩张排除，第二全域F不等于pair拒绝，完整24点不等于全T33，≤18点交换不等于36。相反，已完成原题要及时收束，不为了更强的三行计算、更多模型同意或另一验证级别继续消耗。

这些动作有原项目路径和准确前后状态支撑，宜分别写入准备、route-loop、prove、assemble、verify、handoff的具体返回与消费步骤。领域公式留插件；通用workflow负责让它们真正接棒。
