# 2026-10-06 项目记忆历史快照

以下是完整主定理闭合前的累积记录。当前事实以 AGENTS.md 和 context/FORMAL_VERIFICATION_PROGRESS.md 为准；旧的“未证明”“暂停”等描述仅适用于当时。

# aris4math 项目记忆与工作约定

## 目标与当前阶段

- **正式数学入口：`FORMAL_SPEC.md`**。主目标固定为：任意有限简单 5-uniform 超图，只要边数至多 32，就具有 Property B；等价于 `m(5) >= 33`。不预设顶点数、正则性、线性或均衡染色，也不要求证明等号或构造 33 边反例。
- 数学规格HTML阅读版：`FORMAL_SPEC.html`，使用ARIS `render-html`生成。Markdown仍是规范源；更新后运行 `export ARIS_REPO=/Users/rfy_naiveai/Desktop/aris_main`，再运行 `python3 context/rendering/render_formal_spec.py` 重建。HTML仅做展示，公式渲染使用MathJax CDN。
- 原始任务书：`ar4math_propertyb.pdf`。保留其正确的核心定义及研究方向；具体候选推导和数值不自动成为已证明前提。后续代码、证明与审阅对照 `FORMAL_SPEC.md` 的 D/T/E/R/F/M 编号。
- 用户特别要求：规格入口须经 Grok 与 Antigravity/Gemini 分别审查、交叉核对异议、修订后再次确认；保留实际记录。确认规格成立与证明目标定理是两件事。2026-10-06已完成Grok/Gemini各三轮规格核对；正式入口为v1.0（数学内容同已审阅v0.2），记录在 `context/reviews/SPEC_REVIEW.md`。这里只确认规格一致，主定理仍未证明。额外的Gemini单项措辞更正也已归档；原始意见保留，纠正结论见汇总。
- 规格中的 `v=19,...,25` 与点对覆盖条件来自最小顶点反例约化，不是对原问题悄悄加的限制。固定v时也可用未出现的五元边补到32（v>=8时容量足够；更小v本来都可染）。有限等价约化不需要B0：对至多32边的最小反例先界定v，再原点集补边，保持不可染与点对覆盖。任何目标、对象、量词或约化范围的实质改动都必须显式更新规格和审阅记录，不能靠下游实现默默改变问题。
- 用户已于2026-10-06启用持续Goal并授权正式解题：可并行文献搜索、推导、精确计算、结构枚举和反例探索，持续与Grok/Gemini讨论，使用ARIS证明与评审工作流。最终完成须为完整证明或独立验证的反例。
- 用户已明确授权并行子代理和这两个 MCP 的学术讨论。优先复用已安装的 ARIS Codex skills 和 `/Users/rfy_naiveai/Desktop/aris_main`，调用 helper 时在同一 shell 中设置 `export ARIS_REPO=/Users/rfy_naiveai/Desktop/aris_main`。

## 本项目的已知 agent 失误模式（用户特别要求保留）

**这个项目中的 agent 特别容易过早认为自己已经解出了问题。** 必须用 ARIS 的分离阅读、推导、精确复算、独立审阅和依赖闭合来约束这个倾向。

- “任务书写了”“程序得到一个小于 1 的分数”“多位模型赞同”分别是来源陈述、算术证据和讨论意见，不能自动升级为完整证明。
- 区分：文献已证明结果、项目中的候选引理、精确计算复现、待审查概率支配关系、最终证明。每个重要结论附来源/页码和适用条件。
- 在所有顶点数情形及其依赖链闭合前，不宣称已证明 `m(5) >= 33`。尤其 `v=22,23` 的 link 修正只是任务书中的待审计候选。
- 精确计算采用 `Fraction` 或等价有理数；计算程序验证其所实现的算术，不替代结构选点引理与概率上界的证明。
- 需要独立检查 `min{A_k,B_k,C_k}` 的实际变化；不能直接把非最小项 `C_k` 的扣除量当作总上界的下降量。核对有序/无序边对、方向权重、重复扣除、量词及适用顶点数。
- 同家族 Codex 审阅记录为 `review_independence: same-family`、`acceptance_status: provisional`；跨家族讨论也必须给出可核查推理，模型投票不是数学证明。
- 不为完成流程制造问题或无限追加审查；发现具体问题就定位到公式、类型、位置或依赖，并做与任务相称的修复。
- 用户进一步要求：一旦认为已证明，必须主动寻找反例，优先攻击最紧分支、零权重坏对、选点量词与整张超图；安排盲推导及独立实现。检索未找到反例、有限搜索未命中均不能充当不存在性证明。验证以解决具体疑问为停止点，不以模型一致赞同为停止点。

## MCP 约定

- 本次关键数学义务由Grok与Gemini跨模型家族审阅，频繁围绕具体定义、概率支配、结构选点和全局闭合讨论；Codex并行推导与复算只提供same-family/provisional辅助。外部审阅原文与主代理核对分开保存，发现reviewer自身错误也要纠正；不能靠投票判证明。实际循环状态见 `review-stage/REVIEW_STATE.json`，原文见 `context/reviews/research/`。
- Grok 首轮：`grok`，明确 `cwd`，请求 `model=grok-4.7`、`effort=xhigh`；续接 `grok-reply(threadId,prompt)`。实际返回型号和 effort 以工具元数据为准。
- Antigravity 首轮：`antigravity`，明确 `cwd`，请求 `model=gemini-3.8-flash-high`、`effort=high`；续接 `antigravity-reply(threadId,prompt)`。实际模型记录来自 CLI 选择，不冒充独立服务端证明。
- 让审阅者自行读取本项目内的材料；首轮 `cwd` 设为本项目。只读，不修改文件，不把两个独立 MCP 冒充已配置的 ARIS reviewer overlay。
- 用户于2026-10-06特别授权：Gemini断连或未完整返回时，可以额外重试最多两次；仍失败则保留日志、推进其他工作，稍后再调用。明确额度耗尽时告知用户。此项覆盖此前对Gemini失败调用不自动重试的约定；Grok仍不自动重试失败的付费调用。

## 当前交接状态

持续Goal已激活，原等待reset状态已解除。`PROOF_PACKAGE.md` 已汇总完整候选证明；多锁定公式、19–25点结构分支及23行精确算术均已成文并交叉复算，当前进入全局独立审阅。规范入口保持FORMAL_SPEC.md；候选论证未完成审阅前不宣告目标完成。`PROOF_SKELETON.md`列出依赖和具体义务。

2026-10-06本轮审阅进展：fresh Codex完整审阅PASS（provisional）；Grok与Gemini完整语义审阅均已成功返回，均判定依赖闭合，二者未亲自执行代码。第二轮三个fresh Codex专项分别独立检查概率、构造最不利link、重建全局结构，均未发现数学缺口；实际范围见 `.aris/traces/proof-checker/2026-10-06_run02/`。Gemini另完成未给候选公式的盲概率推导。整图SAT搜索已结束：120个不同候选均可染，所有运行因预算结束，没有目标UNSAT证书。广搜及具体历史漏洞审计已完成。Goal保持active，用户要求继续加强核验。

Gemini选点专项原调用及第1次续接均流中断，不算有效审阅；第2次以新会话重试SUCCESS，完整推导确认结构选择与三锁类型计数。记录以实际文件与REVIEW_STATE为准，未返回意见不填PASS。

用户要求广搜是否已有证明、反驳或明确反例；2026-10-06再次并行检索最新界和方法来源。必须区分本项目任务书已有步骤、已发表方法、候选新数值结论。Grill–Linzmayer v3第7页已明确多锁点、精确交集类型以及低度/共度1选点，不能声称这些通用机制是本项目首创。查新只表述已核查范围。

用户随后明确澄清：**文献检索的主要目的在于检查证明正确性，找前人踩过的坑或已知反例；不要求技巧原创，不把方法查新设成完成门槛。** 证明目标本身就是核心成果。来源准确保留即可，工作重点回到主动证伪、假设核对和依赖闭合；不因已有技术先例否定本证明。

用户进一步询问比有限反例搜索更强的验证，并担心Lean全形式化很难。当前决定是只做一个Lean有限事件/加权扣除语义模块的可行性试验，明确未形式化部分，不承诺本轮完成全T，也不将Lean设为主证明完成硬门槛。Grok/Gemini正在比较适合本证明的验证路线。Lean安装仅在本项目 `.tools/elan`，形式化试点在 `formal/`，不改变全局shell配置。

用户随后明确授权**慢慢推进Lean并持续跨模型审阅，最终交付可靠证明**。先前五个通用有限事件、加权扣除和min定理已真实编译通过，主定理T仅定义、未形式化。下一步推进真实贪心算法的失败覆盖、条件排列计数，以及从输入剖面重算的数值证书。不能将接口前提、`sorry`、最终分数比较或随机搜索冒充主定理形式证明。实际范围见 `context/FORMAL_VERIFICATION_PROGRESS.md` 及后续各模块进度。完整纸面证明、核验程序、部分Lean、完整Lean和人类专家评审分别记录；不宣称“模型一致”或“无反例”认证了完美无缺。

**用户最新完成要求覆盖先前“Lean仅试点、不作门槛”安排：持续做到约化、全情形结构覆盖、真实概率计数和严格数值界全部连接到原命题的Lean顶层证明，并反复进行Grok/Gemini针对性审阅。** 主目标仍是FORMAL_SPEC的T，不能通过改弱类型或附加结论假设完成。审阅“通过”仅解释为在实际检查范围内未发现错误，不保证没有尚未识别的错误。当前Goal保持active，局部Lean模块编译或纸面审阅不能触发完成。

2026-10-06形式化实绩：`Greedy.lean` 已证明真实算法P1及成功排列到原PropertyB；`Counting.lean` 已证明锁定像与单侧集合占位的一般排列计数；`Numeric.lean` 从剖面重算23个闭式（21成功、2诊断），84个定理完成公理检查；`SevenPoint.lean` 已证明七点三元块双计数的整数矛盾核心。这些尚未组成T。下一阶段在Reduction/JointCounting/Structure等模块补连接。

用户提供Archon-Horizon。已核实当前源码0df5571f…与网页缓存旧架构不同，详见 `context/ARCHON_HORIZON_ASSESSMENT.md`。选用其statement-alignment的盲回译和proof-review的真实依赖核对方法；未安装或启动另一套调度。盲译者只读完整Lean定义/声明，随后另一模型对照纸面；不因模型persona不同就声称跨家族。

已知非B正控制：51/66/126边五元超图及K9补孤立点至19–25点，共3908锁定配置、17129009次权重比较未发现矛盾，使用实际边对扣除而非32边专属假设。它是反向测试，非全称证明。Goldberg–Russell印刷Lemma5已找到明确反例并独立枚举复核；本证明没有采用其“同连通分量蕴含逐对阻染重叠”的错误推断。详情 `context/HISTORICAL_PITFALL_AUDIT.md`。

## 上下文入口

- 首先阅读 `FORMAL_SPEC.md`，再读 `RESEARCH_BRIEF.md`、`context/MAIN_TASK_READING.md` 和 `NEXT_SESSION.md`。先前的准备阶段已结束，当前Goal明确授权正式推导与开发。
- 原始46份PDF共207个物理页已分工阅读；索引 `context/READING_INDEX.md`，机器可读覆盖 `context/pdf_inventory.json`，抽取文本在 `context/extracted/`。图片页已按需视觉核对，不把文本抽取成功等同阅读或证明验收。
- `context/EARLY_HISTORY_AND_SOURCES.md`、`context/LATE_HISTORY_AND_BASELINE.md`、`context/BACKGROUND_AND_METHODS.md` 分别保存历史演进、来源纠正和随机贪心等方法。
- `ref/` 已下载验证15份原文PDF共313页。Grill、Aglave、Cherkashin–Kozik、Pluhár、Radhakrishnan–Srinivasan全文；Deutsch–Sagan的Catalan定理及证明精读、其余浏览；Goldberg–Russell现已全部10页视觉审读并做具体错误审计。其余新下载文献按实际范围阅读，不能把313页全部称为精读。具体见 `ref/README.md` 与 `context/reference_manifest.json`。
- 已核对的文献起点是 Grill–Linzmayer arXiv:2403.05674v3 Theorem 1 的 `m(5)>=32`，不是本项目的 `>=33`。2026年综述书章只读元数据和摘要，不据此声称已做穷尽查新。引用新结果前补做针对性查新。
- 历史纠偏：0818的部分v=23数值实为v=22；v=25完整证明在0825曾被撤回，之后的类型枚举仍需独立复现；0908的`>=34`属于另一个探索。Goldberg作者警告部分错误不可用原方法修复，只明确保留`m_9(4)>=19`的证明。

## Wiki 与后续工作

- `research-wiki/` 已按ARIS规范建立15个paper节点、4条有原文依据的关系、G1–G4项目待办；尚无claim节点。文献页注明本地原文、版本、页码、阅读深度和项目适用范围。
- 新增文献使用规范 `research_wiki.py ingest_paper`，关系使用 `add_edge`，然后维护log、重建index/query_pack；不手改图关系和自动Connections。重要新知识和下一步义务同步到项目记忆。claim节点遵循proof-checker契约，不因模型讨论正面就手写verified。
- 已有推导见 `proofs/PROBABILITY_LEMMAS.md`、`proofs/STRUCTURE_19_23.md`、`proofs/STRUCTURE_24_25.md`。主计算器及独立检验在 `computations/`；完整结果在 `results/`。下一项义务是核对跨模型实质异议及全局依赖闭合，具体状态在 `NEXT_SESSION.md`。
- 本轮实际采用research-lit、research-wiki、formula-derivation、proof-writer；proof-checker审阅与render-html输出进行中。auto-review-loop用于有明确对象与停止点的评审修订；不因安装齐全就启动论文写作、GPU实验或rebuttal流程。

2026-10-06新增形式化闭合：SmallVertices已通过均衡染色的一般排列计数证明≤18点全部可染，继而严格证明原T↔19–25点32边点对覆盖F；这是等价约化，F仍未完成。Reduction/Structure/JointCounting均已冻结交付；新连接在LowDegree、Traces、EndpointCounting/CriticalCounting与解析分类模块推进。用户不接受样例/整图穷举作为最终依据；局部分类用解析证明，数值不等式可作内核算术。

Argus已核验当前文档及源码，见context/ARGUS_ASSESSMENT.md。采用“命题忠实度独立检查、义务完成不等于目标证明、证据对应实际检查对象”的机制，复用现有ARIS记录；没有安装或启动Argus调度，也不把它描述为本题自动求证器。

**2026-10-06最新状态覆盖：用户明确暂停原研究Goal，工具状态paused。当前仅获授权为aris4math_v2写经验文档，不自动恢复PropertyB证明、搜索或MCP评审。恢复点见NEXT_SESSION.md顶部。**

**2026-10-06恢复覆盖：用户随后恢复原Goal，工具实时状态active。解除此前暂停；继续完整形式化原T。优先打通NoLocks的v19完整分支，并行推进K6解析标签分类、概率计数接口及LinkCounting。v2经验文档已完成，不替代原研究目标。**

## 最新形式化进展：19、20点已完整闭合（2026-10-06）

Goal继续active。NoLocks.nineteen_propertyB与TwentyVertices.twenty_propertyB均从真实H、≤32边直接推出原PropertyB，无额外点对覆盖或概率假设。20点948单交有序边对界由解析双计数证明。LowDegree、LinkCounting、K6完整标签分类、ConditionalUnion以及TypeCounting实际类型聚合均已编译。21–25点的类型/单事件权重/扣除实例化及最终Target尚未完成。具体状态以context/FORMAL_VERIFICATION_PROGRESS.md及run07实际日志为准，早期暂停和进行中描述仅作历史。Grok正审19点完整分支，Gemini正审K6解析分类；尚未返回的调用不记通过。
