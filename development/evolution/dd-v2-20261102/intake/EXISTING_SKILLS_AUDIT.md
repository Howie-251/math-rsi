# 现有九项 MathRSI 技能的执行粒度审视

2026-11-02，静态审视，未修改稳定技能、未启动数学或模型任务。九份 `base/skills/mathrsi-*/SKILL.md` 均已通读；两次输出截断的区间随后单独补读。范围记录在 `formal-review/READ_LEDGER.tsv`。本稿不以行数给技能打分，也不把本轮DD历史阅读改写成MathRSI v1实跑。

## 判断

现有九项已经包含真实调度、输入、调用任务、产物消费、回流、唯一writer和恢复职责，不能准确称作九个只有技能名称的薄入口。特别是route-loop、prove、verify和survey已经有长篇实作内容。当前应修具体接缝、补真实可携带案例和行为试用，而不是因ARIS原件篇幅更长就重写全部流程。

仍有一个真实执行歧义：verify把“完整候选／自足局部定理的正式审计”普遍送入以TeX为中心的proof-checker，而完整Lean见证的核验又在其后独立处理。对于DD那类唯一成果是已绑定的公式图、真实Walk定理和实际类型／公理审计的任务，现文本没有清楚写出“只验这个形式目标时，直接执行lean-formalize并返回”的完整分支。上游lean-formalize明确说 standalone Lean task 不自动要求paper-audit。若用户确实要可读证明的正式审计，当前checker路径正确；若只要求固定实例形式化，不能为了进流程另写TeX论文、再审一次已可由内核解决的有限命题。这应通过入口和返回分支明确，而不是删掉证明审计能力。

## 对照 ARIS 的方法

比较的是相应ARIS原件的执行颗粒：初始化／恢复、实际输入、模型或helper调用、逐轮实作、返回消费者、失败处理、审阅原文、终态与交付。已完整读取Codex research-review、lean-formalize以及本轮meta双端原件；auto-review-loop已读初始化及实际恢复/审阅入口，MathRSI适配reference也通读。proof-checker、research-lit、research-wiki、render-html的全部长文不在本次“重新全文阅读”声明内；以下相关判断依据仓内MathRSI调用合同、已读reference和实际入口段落，不冒称重做了全部ARIS技能审计。

ARIS完整流程值得保留的不是ML默认产物，而是每步真的有人执行和消费。MathRSI已明确把RR Step3的实验／投稿产物及Step4共识终点替换为数学义务，并保留同会话证据对话；这是一项实质适配，不是只换标题。ARIS原版24小时自动清状态、score/ready停止门及send_input示例没有被盲目搬过来，也是正确处理。

## 逐项审视

| 现有技能 | 已有可执行内容 | 尚需补清或实际试用的接缝 |
| --- | --- | --- |
| **mathrsi-research** | 恢复表、五阶段真实委托、成熟结果立即消费、局部verify回prove、文献回流、唯一父dispatcher、终轮继续。原题已齐／短证明可直接闭合。 | “完整形式见证直接verify”应能在verify选择Lean-only，而非被默认为TeX checker。新增演化入口不能成为每次handoff后的自动第六阶段。主入口结束应消费精确目标声明及实际证据，不能把新插件的成功receipt当全题状态。 |
| **mathrsi-prepare** | 初步specify→唯一一次survey→final定稿，含新题／增量／完整稿／已有路线不同起点。明确子返回点和缺进口只补该项。 | 需以DD目标变更真实场景试用：从exact N(8,2)转向已授权construction portfolio时，旧题保持open/paused，新任务量词、验收和允许进口另行固定；不能只改最新摘要。不是必须新增字段或所有任务强制分叉。 |
| **mathrsi-specify** | 原文逐句反译、存在／全称／算法／精确值拆分、原域与内部条件分离、调查后只修影响含义部分、复杂时独立反译。R(3,3)例子是可用的短执行示例。 | DD补充“公开比较门槛／数学合法性／形式实例／公开接收”四个不同终点，防止`maxdegree≤d`被升级为d正则、D≤D被升级为恰径、固定公式图被升级为ASCII解析器或世界纪录。现技能已有原则，缺的是第三领域的具体输入与返回实例。 |
| **mathrsi-survey** | 唯一发现owner、真实research-lit任务、Property B插件实接、实际helper参数、关键进口超出摘要的原文深读、身份核验、引用链/勘误、wiki读回。不是薄路由表。 | 全流程语境仍主要是论文；DD公开图源、作者代码、邻接表及实时表格也可承担不同进口。应具体说明发布页保证、解包字面对象、公式来源三者怎样比对，未取到CW条目不阻止固定构造合法性成立。复用现有来源存储，不造新文献平台。 |
| **mathrsi-route-loop** | 数学ARL的准备/A–E/终轮完整链；每reviewer原始memory；真实first/reply/status区别；证据反驳、实作、差异复核、精确phase恢复、三轮局部预算和父回收。 | 尚缺一次完整真实A→C修法→D复核→父消费的独立行为试用，旧静态场景不能补成已跑。DD M2和Q-line两次反驳很适合作输入：reviewer“100%exact”不是终态；反驳后仍可能有第二个遗漏，须消费真实新证据。现无须恢复旧付费会话。 |
| **mathrsi-prove** | actual caller先落草稿、formula/writer/领域程序完整委托、独占作者、立即回收、共同对象和运输、必要门够用即停、无增量接管、精确断点、局部验证回原run。 | DD说明“实现瓶颈”有可验证的结构转换：符号线性扩展＋小basis证书，必要时controller orbit覆盖，而非让作者只增timeout。需提供真实容量/耗时/失败归因的具体例子；全局调度规则已存在，不能再加固定硬caps。 |
| **mathrsi-assemble** | 反向依赖+正向原输入双核；writer实际任务；多分支并集；现稿复用；发现新数学回prove；正文和审计输入一致；返回原caller。 | DD终态装配应明确采用哪些完成module、哪些失败/试验module不在closure；原source身份、克隆旧源、recipe索引与标签equivalence一起接。`N62TripleActualBlock`与STATUS冲突说明必须以actual import+source+audit解决，不能只抄最后导航。 |
| **mathrsi-verify** | 覆盖／checker谓词／原结论三种义务分开；独立生成和重放区别；research-review与proof-checker不机械叠加；TeX输入适配、真实canonical audit、修复往返、实际Lean类型与公理、局部scope返回。 | 上述Lean-only分支是首要明确点。另需明确外部字面绑定：typed公式图定理+外部边表/recipe比较不等于Lean证明ASCII parser；审计输出省略81行时应只补打印可见性，不重复源图构建。形式验证、字面验证、reviewer静态阅读应各自返回精确证据。 |
| **mathrsi-handoff** | 真实正文/verification消费、只制所需格式、renderer真实脚本与offline语义、解压读回、独立目录命令、wiki与恢复、数学与交付状态分开。 | DD成千generated shard和attempt receipt不能一股脑要求普通读者全看。需要按实际目标导出闭包与可恢复失败，而非只给目录或全库打包；本技能已有按需包原则，可用DD补一个完整示范。通用复现scope不应因某批次只需要新根核验而升级为每图重做全BFS。 |

## DD原件已支撑的具体改法，不先造新技能

**从证据区分实现失败与数学失败。** Brown57初版在87秒后失败的是`change`与classical neighbor定义不一致；后来的`Brown57Verified`先用可计算邻接内核证明完整degree/diameter，再用`Brown57`桥接classical枚举。证明目标未改。这能补进prove/verify的实际调用例。

**先证明缩域接口，再检查较小数据。** F4Graph3840DecoderInterface将路线噪声的加法与标量性连接到basis；F9Graph56862再用169种实际model、507个basis检查和5616个pair绑定支持全域Walk，而不是全顶点对Lean枚举。F3Graph15552用实际controller symmetry覆盖192层，再装配8个代表行。应将它们保留为有条件的技术实例，不能变成所有数学题一律要做对称性商。

**新增实例应复用已完成泛化。** FullNeighborhoodClones保留原边并给出旧—旧bounded-Walk的双向等价；因此克隆不能修好一个本来D不合格的旧源。具体新构造只需证明固定源、真实邻域load及recipe绑定；中心互不相邻或中心映射单射不是该泛型的普遍前提。此处扩展现有prove的“条件是否过强”段比另开一套workflow合适。

**版本和当前基图是数学输入。** Redei顺序试验的覆盖失败只针对当时基图，后来的helper可能改变R4；度数已满在只加边过程中才有对应单调性。一般“试过就永不重试”会丢失合法机会。现有停止/重启段应以真实前提和改变的基图给恢复例，而不是新固定次数门。

**审阅输出要逐断言消费。** M2原评议错误地丢掉两步within-block jumps，续接又丢掉target-head分支；Q-line评议将充分证书失败写成实际不可能，后续明确撤回。Root保留正确部分、给实际路径反例、继续修实际推导，既不服从错误否决，也不把整次review改成PASS。route/prove已有此合同，DD补充更具体的操作链和独立试用材料。

## 后续验收顺序

按最新授权，先建立可独立执行的mathrsi-meta-evolve；本稿只作为其输入，不由作者直接修改base v1。该技能消费原件、分类并提出增量diff，真实讨论与独立试用后才决定接受。第三领域技术例进入相应reference或DD插件，单题状态留历史材料。由未参与写作的使用者从真实输入走受影响路径：至少覆盖Lean-only固定见证、局部结果回父、失效reviewer公式的证据回应、以及有旧源复用的recipe绑定。各试用只验该路径，不恢复DD旧Goal、旧模型请求或重跑旧Lean。

本稿是九技能文本的静态审视与DD已读原件驱动的候选改法。157条已提取真实模型返回正文现已全部读完（含ERROR/READY，非157次独立数学接受）；其它未逐项读的人工审计、所有generated shard语义审读、comments1896–2682及新行为试用，均不能用本稿代替；精确剩余见`formal-review/READ_LEDGER.tsv`。
