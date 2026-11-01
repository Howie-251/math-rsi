# Property B 数学知识层重建：实际阅读、产物与验证

2026-11-01。本次是MathRSI本地文档/技能开发；源Property B工作区只读。没有恢复旧Goal、执行旧研究driver、重新构建Lean、调用付费模型或修改原项目。数学结论、审阅与计算状态均按原材料准确范围保留。

## 交付

数学正文位于 `plugins/propertyb/skills/mathrsi-propertyb/references/mathematics/`：

|文件|实质内容|
|---|---|
|00-READING-AND-CALLING.md|按当前实际义务选择入口；从原H到染色的完整链及状态解释|
|01-reduction-and-selection.md|商/拉回、整数域、低度/共度超额、Caro–Wei和保留整数度数Q门的完整证明、低总度实际原边|
|02-actual-traces-and-coverage.md|真实迹恢复/投影/重标号/增锁、容量生成完整性、五锁packing、外点边际与共同自然连接；单位星恢复完整证明|
|03-permutations-bad-pairs-and-duality.md|真实greedy失败覆盖、联合无放回排列、避锁link坏对下界、弱对偶完整证明、多布局、活跃项、向外整数舍入|
|04-signed-repair-and-sources.md|从原边逐风险建立signed系统；随机横截全证与共同二重点预算；四正集参数全证；等度点族/加权唯一坏边全证；源选择及私有/owner原接口|
|04a-repair-gates.md|完整135行原修复门目录，含恰/至多、17/18点、负单/二集、混合正集与附录门，不只列几个例子|
|05-shared-structure-and-conditional-tools.md|共同Gram/wedge/容量的具体公式和caller；删点/最小能量完整证明；唯一例外点对完整容量证明；300行36研究条件工具及后继范围|
|06-general-k-rs-and-growth.md|原RS实际过程/必要事件/正关联/Jensen/精确积分/最小反例caller、整数最大预算和参数控制、公共点二分、k≥12增长、明确参考包络D及指定松弛E的完整四份规范证明|
|07-small-k-working-examples.md|六元67、七元131、八九元267/543、十二元4664方法/域/实际独核范围；原small-k迁移的完整选锁与舍入推导及五元失败边界|
|08-complete-lemma-inventory.md|L1–L117整份原库存保真全文、含所有后继状态及边界；避免主题摘录遗漏附录成果|

另完成可单独使用的 `plugins/propertyb/skills/propertyb-bound-lab/SKILL.md`（209行）：具体预算/一般k研究任务、恢复与原量词、完整必要域、连续/整数选锁、嵌套实际池、真实迹caller、排列坏对/dual、signed源与修复、共同结构回流、父分支关闭和实际输出。主流程共同规矩通过链接复用，主体直接给判断、操作和参数例，未要求读完全部archive。

没有编辑Root负责的主SKILL、source-map、效率文档，也没有改其它代理文件。

## 实际阅读范围

检索了全部13份 `research-wiki/PROPERTY_B_*.md`（合计2680行）的文件与标题；重点逐段阅读和抽取如下。长工具输出出现过截断，因此下表区分正文核读与库存保留，不把发出cat命令等同于全文核读，更不声称读完所有context。

- `PROPERTY_B_REUSABLE_LEMMAS.md`：L1–L23基本论证逐段读；L24–L58修复/共同预算主要段落逐段读；L59–L117按源态、Gram/森林、共同middle、例外共度和完整分支路线检索并抽读。长段中部分历史状态及个别工具未逐字复核；整份1241行原文无删减保留。没有把后95项概括为普适定理或统一验收等级。
- `PROPERTY_B_SMALL_K_TRANSFER.md`：完整阅读125行；Caro–Wei连续/整数r、向外舍入、k5失败边界用于正文01/03/07。
- `PROPERTY_B_GENERAL_METHOD_SYNTHESIS.md`：阅读当前k12/k17状态和一般骨架/共同坏对/Gram/wedge/源态/修复等正文；历史在途语句只作为历史。
- `PROPERTY_B_CONDITIONAL_TOOLKIT_36.md`：阅读六星W门、三划分、19-hit相容对、整数匹配、共同紧面、M17/r≥7及r6/24/23后继主要链，保留全部300行供实际caller查范围；并未重核每个长期附件。
- `PROPERTY_B_M6_GE67.md`、`PROPERTY_B_M7_GE131.md`、`PROPERTY_B_M8_M9_INCREMENT_20261029.md`、`PROPERTY_B_K12_GE4664.md`：完整阅读新进展、各自必要域与独核范围，正文07逐份保留。
- `PROPERTY_B_M6_GE66.md`、`PROPERTY_B_M6_GE67_DIAGNOSIS.md`：完整阅读；后者新Q门另追到原完整证明，不把诊断时未闭状态冒作最终六元状态。
- `PROPERTY_B_NEXT_BOUND_PLAYBOOK.md`、`PROPERTY_B_RESEARCH_LESSONS.md`、`PROPERTY_B_FAILURE_ATLAS.md`：按新M整数差分、实际caller、坏对方向/零槽/多布局、分类漏标、signed反例和共同结构失败范围阅读；部分长输出被截断，不在此承诺每条执行历史均已读完。效率层由Root/另一任务维护。

实际打开的规范数学源包括：

- `proofs/propertyb-general/{CORE_THEOREM,UNIFORM_INTEGER_GAIN,CLIQUE_REFINEMENT,BASELINE_COMPARISON}.md`：分段读取核心定义/定理/证明、D/E范围和一般k真实caller；四份完整正文放入06，不重造更短但丢前提的证明。
- `proofs/propertyb35/RANDOM_TRANSVERSAL_REPAIR.md`：完整读取、包括耦合、共现点对、完整容斥、原H正负双角色及二重点共同预算。
- `proofs/propertyb35/UNIT_STAR_RECOVERY.md`：完整读取、包括块大小≤k−1及多个投影同源。
- `proofs/propertyb35/ONE_EXCEPTIONAL_POINTPAIR_CAPACITIES.md`：完整读取两个一般引理及21点caller范围。
- `proofs/propertyb35/UNIQUE_BAD_EDGE_FAMILY_MOMENTS.md`：完整读取原矩/精确计数/唯一坏边及加权版本，保持源与修复区别。
- `proofs/propertyb35/FOUR_POSITIVE_AT_LEAST_THREE_REPAIR.md`：完整读取参数证明及真实禁点边界。
- `proofs/propertyb35/REPAIR_GATE_CATALOG.md`：完整读取原135行，全部保留于04a。
- `context/propertyb-m6-67-diagnosis-20261029/DERIVATION_PACKAGE.md`：完整读取Q门原证明及42–44实际换点；抽取Q门全证入01。
- `context/propertyb-k12-4664-20261029/PROOF_M12_GE4664.md`：打开整体134行，重点核定完整域91–782、共同池条件增锁/两三锁迹、自适应分流、整数取整及独核未全概率复算范围；长调用输出末段曾截断，未将其当作所有关联代码全文审计。

## Lean源码抽核

用rg实际确认声明存在，并打开以下具体声明或完整短文件：

- `formal/Aris4Math/ThirtyFour/MixedLayoutDual.lean`完整代数文件：`quota_repair`在ℚ、任意有限索引；`min_split`、`average_le`、`exists_strict_of_average`的精确假设。
- `formal/Aris4Math/ThirtyFour/MixedLayoutApplication.lean`的 `propertyB_of_mixed_layouts`：五元真实宿主、counts/covers/profile、nocap、correctionCenters、非负乘子、实际配额和strict等完整参数。
- `formal/Aris4Math/JointCounting.lean`的 `locked_joint_subset_ratio`：一般有限锁类型、真实锁排列空间、不交自由点/槽、联合分母。
- `formal/Aris4Math/General/Growth/Twelve.lean`开头种子及参数控制、440行顶层 `propertyB_of_general_growth_twelve` 和等价非B边数下界：输入裸Finite/Finset/Uniform/k≥12与预算，内部取得RS接受见证。
- `Reduction/Structure/Greedy/ConditionalUnion/SevenPoint`、`ThirtyThree/{MultiLockRecovery,FiveLockClassification,AvoidedLink}`、`ThirtyFour/{LockExtension,PromotionCatalog,PromotionReconstruction,BoundedAllocations,LockRelabel,LockProjection,WeightedThreePartition}`：实际rg确认文中对应声明名与所在文件；未全文逐条重新审核证明体。

此次没有执行Lean，没有把源码存在升级为新构建成功；保留原构建/原题审计路径，由宿主按具体数学任务决定是否实际重放。

## 本地实际试用与检查

`BOUND_LAB_LOCAL_TRIAL.json`保存8个通过的精确小fixture：M66/v44与M65整数端点差；37点Q60/Z122保证三锁；不活跃扣除收益0；四正s3/D7精确8/9；单位三锁迹恢复总边数/三个度；五点排列枚举8/120=1/15的归一化；frontmatter必需字段；新SKILL全部相对链接存在。

这些小fixture测试技能给出的具体判断和公式，不是恢复原研究，也不是宣称技能已在未知原问题上求解成功。没有调用原作者driver或重新生成旧数学结果。

官方skill-creator的 `quick_validate.py` 已尝试系统Python与现有math-python，两者均缺PyYAML，报 `ModuleNotFoundError: yaml`。没有伪报官方验证通过；本地独立检查通过frontmatter两个标量字段、技能命名和所有SKILL相对链接。Root可在已有带PyYAML环境补跑官方检查。

所有抽取段落的Markdown链接已从源文件相对路径转换到本地插件archive。曾检测到一处LaTeX `[(k−1)/(k−2)](1−epsilon)`误当Markdown链接，已恢复原公式。HTML展示链接改为本地完整Markdown数学源，避免增加大型展示文件依赖。

41个精确JSON依赖见数学目录 `EVIDENCE_JSON_DEPENDENCIES.txt`，已交Root负责archive复制。ZIP中的k10/11 certified模块亦已提醒Root补齐；verified.py不能单独运行。当前链接检查缺失项主要为这批archive依赖；补齐后Root再做整仓检查，不能把此刻文件缺失写为最终全通过。

## 未声称完成的工作

未全文阅读数千context文件、全部程序或整个formal工程；未逐条独立重证L1–L117；未重新审阅所有历史模型回应；未独立重放各参数的全部概率/分类；未新证明更高下界；未升级原成果、candidate、drafted或跨家族状态。完整本地archive保留上述可继续深读与复算的输入，而不是用这一报告替代它们。
