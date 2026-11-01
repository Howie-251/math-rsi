# ARIS 流水线的实际编排：输入、调用、产物与转移

本报告针对只读源码 `/Users/rfy_naiveai/Desktop/aris_main`，实际 HEAD 为 `c485faa59a68e51c6575dea67ca57abc7a6a2b9c`。目的不是枚举技能，而是辨认一个调用者怎样从研究方向推进到执行、如何消费下一阶段所需产物，以及遇到失败或未完成义务时怎样转移。没有执行研究程序、helper、模型调用、实验或构建，也没有修改上游、研究工作区或 MathRSI 技能源文件。

## 阅读范围与证据限度

**全文阅读的五个主线入口**：`skills/research-pipeline/SKILL.md`（413行）、`experiment-bridge`（389行）、`auto-review-loop`（1211行）、`paper-writing`（945行）、`research-refine-pipeline`（197行），合计3155行。长文件分段读完；不是只读头部、description 或 README。

**全文补读**：`AGENT_GUIDE.md`（252行）、`skills/experiment-plan/SKILL.md`（249行）、`skills/shared-references/resumable-runs.md`（109行）、`assurance-contract.md`（273行）、`reviewer-backends.md`（156行）。README 只读工作流总索引及 W1.5/W2/W3，即763–795、880–1144；没有宣称全文读完1805行README，也没有接管 Root 的 W1/idea-discovery 阅读。

**定向补读**：`research-refine/SKILL.md` 的恢复、原题锚、反馈解析、停止门、最终产物段（58–151、424–486、579–739）；`result-to-claim` 与 `ablation-planner` 的输入、判决、路由与不可用段；`acceptance-gate.md` 的前110行；`tools/run_state.py`、`tools/review_gate.py`、`tools/verify_paper_audits.sh` 中实际状态、停止条件和必需产物的源码片段。未全文审计这些 helper 或全部子技能。

**Codex 比较**：逐项查看指定入口的 mainline/Codex diff；另读 Codex `auto-review-loop` 的初始化、路由、状态、停止门与终止段，及 Codex `paper-writing` 的合同、forensics和最终验收段。不是声称全文读取全部 Codex 镜像，也没有据相同名称假设行为完全一致。

`AGENT_GUIDE.md` 明定自己是路由索引，SKILL.md 才规定行为。因此以下以实际子技能为准，README或父技能摘要与其冲突的地方单独列出。

## 1. `/research-pipeline`：主调度器如何消费下游输出

该入口接受研究方向，也可加载已有 `RESEARCH_BRIEF.md` 作为详细上下文；有 `— resume <run_id>` 时先找恢复点。它执行以下有依赖链，而不是把四个技能列给用户之后结束。

| 阶段 | 实际动作与调用 | 必须取得的产物；调用者下一步怎样用 |
|---|---|---|
| 预分流 | theorem-centered 且要求Lean时，先转 `/lean-formalize`；仅包含实证研究才继续实验路线。混合项目只形式化指定义务 | 返回实际证明范围和未闭义务；不能拿形式化子引理建立实证主张 |
| 1：方向变成候选 | `/idea-discovery "$ARGUMENTS" — AUTO_PROCEED: <resolved>` | `idea-stage/IDEA_REPORT.md` 的候选排序用于选一条路线；选定后 Stage2 依赖其已生成的 `refine-logs/EXPERIMENT_PLAN.md` |
| 2：计划变成执行结果 | `/experiment-bridge "<chosen-title>" — code review: …, base repo: …, compact: …` | 必须等 bridge 完成并收到 handoff；`EXPERIMENT_RESULTS.md`、已更新tracker、真实结果文件成为 Stage3 的研究材料，不能仅有“任务已提交” |
| 3：结果变成修订后的研究 | `/auto-review-loop "<direction + chosen-title>, difficulty: …"` | 消费实际代码、原始结果和当前主张；返回 `review-stage/AUTO_REVIEW.md` 的完整轮次、最终判决和仍存问题 |
| 4：建立写作交接 | 从 IDEA_REPORT、仓库实现、configs/最终results、AUTO_REVIEW 生成 `NARRATIVE_REPORT.md` | 包含问题、核心主张、方法、每项数字的证据、图表库存、限制与后续项；它是下一技能的输入，不是泛化“工作已完成”汇报 |
| 5：可选写作 | `/paper-writing "NARRATIVE_REPORT.md" — venue: …, AUTO_PROCEED: …` | 只有 `AUTO_WRITE=true` 且写作前置齐备才运行；产物是paper目录、PDF和改进记录，并回填主流水线报告 |

### 阶段转移

- `AUTO_PROCEED=true`（默认）使选择检查点成为**同轮继续**的进度告知：展示选择后立即调用下一技能，不提问、不等待沉默；false时才展示选项、结束轮次并等明确答复。该值必须显式传到嵌套工作流，不能子技能另取默认。
- Stage1若用户要求合并、修改或全拒绝，带着新约束重跑 `/idea-discovery`；若选择停下，保存当前 IDEA_REPORT。
- Stage3四轮后仍无正面判决，停止并列剩余问题；父技能Key Rules禁止为了赶流程强推Stage4/写作。主流水线不是“到了下一行就继续”的无条件脚本。
- `AUTO_WRITE=false`默认在叙述交接后结束；把paper-writing阶段记为skipped，防止resume永远指向未打算运行的写作。
- `AUTO_WRITE=true`但缺venue时不猜：自动模式在报告标“VENUE NOT SPECIFIED — paper writing deferred”，保留pending供以后恢复。需手工图而尚缺时同样defer；false模式才在此询问。
- `/render-html "NARRATIVE_REPORT.md" --no-review`是Stage4的派生阅读视图，失败只记录，不阻挡规范MD交接。源码有一处summary接受表写“written (+ rendered if RENDER_HTML)”；后面明确HTML non-blocking，因此不能把可选渲染解释成核心数学义务。

### 恢复不是重新生成一遍

主线用 `run_state.py start` 建立有序阶段：`idea-discovery, experiment-bridge, auto-review-loop, summary, paper-writing`；入阶段置running，产物写完置done，门通过再accept并留verdict_id/reviewer。`resume`返回首个非terminal阶段：running/failed重做执行，done未验收重新审查，accepted/skipped向前跳过。重要的是：**写了文件**与**该文件通过所属门**分别保存。

阶段所属门也不同：bridge记录实际jobs/results完成；summary是交接文件的机械完成；idea与review是有具体trace/session的语义门；paper-writing读外部audit verifier。不是统一用一个“Root认为完成”。Codex版新增同家族provisional，并在启动时使用 `--provisional-advances` 允许它作为该次run的恢复terminal；源码 `run_state.py` 默认仍只让accepted/skipped跳过。这是显式运行策略，不能把provisional改名为accepted。

无人值守heartbeat只看进程/文件进展并推动停滞阶段。`iteration_log.py note`的structural/human信号用于换结构或提示人，不能判论文够好或证明成立；该heartbeat并不是 `/auto-review-loop` 自身的外层重入计时器。

## 2. `/research-refine-pipeline`：先稳住方法，再建立可执行验证计划

该组合器明确调用两个已有工作流；它自己的工作是检查初始状态、安排顺序和保持同一组claims。

| 顺序 | 输入与实质动作 | 输出及其消费方式 |
|---|---|---|
| 0：triage | 从任务提取problem/approach/constraints/resources；检查现有FINAL_PROPOSAL是否仍匹配本次任务 | 缺失、过期或实质不一致→完整 `/research-refine`；已有强且对齐的方案→复用后直接规划，不重写有效产物 |
| 1：refine | `/research-refine` 固定Problem Anchor，读grounding材料、具体化机制、审阅、按证据修订完整方案 | `FINAL_PROPOSAL.md`是干净方案；`REVIEW_SUMMARY.md`是各轮关切/解决/剩余风险；`REFINEMENT_REPORT.md`保留全文和演化，三者供后续planner读取 |
| 2：planning gate | 明说method thesis、dominant contribution、主动拒绝的复杂度、仍需验证的关切、frontier primitive角色 | 答案不清晰则先收紧方案；即便refine尚REVISE，也只能在剩余弱点明确时带风险进入规划，不能把REVISE当READY |
| 3：plan | `/experiment-plan`读取上述三文件，冻结claims→设计证据块→给每块完整setup、成功/失败解释→排序 | `EXPERIMENT_PLAN.md`规定claim map、blocks、milestones、budget、stop/go；`EXPERIMENT_TRACKER.md`逐Run ID列variant/split/metric/priority/status，供bridge解析与回写 |
| 4–5：整合交接 | 核对方案、计划、摘要使用同组claims | `PIPELINE_SUMMARY.md`列READY/REVISE/RETHINK、Must-Prove Claims、首三次runs、主要风险和下一行动；指向 `/run-experiment`，并不自己冒称已执行 |

补读子技能可见这不是“拿一段idea直接开大实验”：`experiment-plan`先问primary/supporting/anti-claim及最低证据，再按main anchor、novelty isolation、simplicity、frontier necessity、failure analysis删减块；每个块写明失败意味着什么。milestone先sanity，再baseline/main/decisive/polish，must-run与nice-to-have分开。这些字段直接成为bridge的运行顺序和成功标准。

`research-refine`自己的恢复粒度比主流水线更细：`REFINE_STATE.json`保存最后完成phase（anchor/proposal/review/refine）、round、审阅session、score/verdict。24小时内in_progress从下一phase继续；completed或超过24小时则fresh start（这是原规则，数学长战役不应照搬这一短时过期策略）。READY停止要求score≥9、READY、无未解drift三者同时满足，否则最多5轮。READY→experiment-plan；REVISE→修机制后重新refine；RETHINK→重看核心机制、可能回idea-creator。到轮数上限也写当前最佳FINAL_PROPOSAL，**文件存在不等于READY**。

## 3. `/experiment-bridge`：为什么它是执行桥，而非实验建议

### 输入和执行顺序

输入优先 `EXPERIMENT_PLAN.md`，再配tracker/proposal/idea摘要；一个都没有才向用户问要实现什么。phase1实际抽取milestones、每块dataset/split/task、variants、metrics、hyperparameters/seeds、成功准则、must/nice和GPU预算；如 `idea-stage/docs/research_contract.md` 缺失，从选定idea及plan建立它，供result-to-claim/ablation-planner用作“本来声称什么”的来源。

接下来按依赖执行：

1. 如果给BASE_REPO则clone；否则先检索本地已有脚本与实现，复用后补训练、评估、数据、baseline、参数入口、可控seed、JSON/CSV结果及日志。按sanity→baseline→main→ablation实现。
2. `CODE_REVIEW=true`时把**plan+method+实现**交给独立code reviewer，对照其是否实现目标、使用真实ground truth和正确metric。主线无CRITICAL则前进；有CRITICAL修后再审，至多2轮。
3. `/run-experiment [smallest sanity command]`；等完成，读指标输出、内存和格式后才进入全量。不只确认进程创建成功。
4. 按milestone部署：明确规则是≥10 jobs或teacher→student依赖走 `/experiment-queue [manifest]`，其余走 `/run-experiment [commands]`；每批监控 `/monitor-experiment` 并**随着完成立刻回收**结果。≤5只是常见小批示例，6–9不必形成无人接管的空档。
5. 解析JSON/CSV/logs；可用W&B时 `/training-check`；回写tracker实际Status/Notes；按原plan成功准则写 `refine-logs/EXPERIMENT_RESULTS.md`。COMPACT时另把每个run的config/result/verdict/reproduce追加 `EXPERIMENT_LOG.md`。
6. main结果positive才进入ablation规划；negative/inconclusive跳过并记录；最后handoff列Implemented/Deployed/Completed/Main result和结果、tracker位置，交 `/auto-review-loop`。

### 失败、预算和恢复

- 主线sanity失败先读traceback/stderr/log，诊断后改再跑；预算是2次patch、最多2次clean reimplementation。第2次后可用 `/codex:rescue` 看原代码与log；两次clean重写同样失败或总预算耗尽，停止并报告plan/environment问题，不带坏代码全量部署。
- clean重写只替换该尝试生成的代码，plan、tracker、用户源、data/results保留。这个“回到plan重实现”的动作比只写“遇错调试”具体。
- `AUTO_DEPLOY=false`有实现后部署检查点。代码中的检查点位于phase4段落后部；其语义是先人工检查再deploy，不能按文本位置等到提交后才问。
- 超过估计耗时2倍的run标记后推进其它milestone；累计GPU预算接近上限告警。queue由自己的 `queue_state.json` 恢复，bridge本身没有独立的通用phase-state，主流水线只是记录bridge阶段。
- 主线CODE_REVIEW不可用有“skip silently”旧降级；与文件头新route契约的“selected unavailable=REVIEW_UNAVAILABLE”存在张力，不能据此声称通过审阅。Codex版是无法委派时本地同清单并标`[local-only]`，也不是独立审阅通过。
- bridge将positive main直接送ablation-planner，而后者明确要求先过result-to-claim（yes/partial）。bridge没有显式补这个调用；稳妥消费方必须查已有判决，没有就先走result-to-claim，不能把作者的positive叙述当成该前置已满足。

### 实证专用边界

MAX_PARALLEL_RUNS=4、GPU-hour、OOM/batch size、gradient checkpoint、W&B、Vast/Modal生命周期都属于该执行域。数学程序可借用“最小真实caller→实际退出码和产物→按依赖全量执行→边完成边回收”，不应被强制包装成训练、baseline、seed或ablation。

## 4. `/auto-review-loop`：每轮真正怎样改变下一步

这是内部自带轮次的循环；主线明确禁止把它直接再套 `/loop`/Cron：时钟重入会丢失reviewer session memory、在材料未变时重复付费判决。它应在外部等待（如实验完成）后被调用一次，再由内部按产物变化调度。

### 单轮依赖链

1. **初始化/恢复**：读取REVIEW_STATE和AUTO_REVIEW；COMPACT可先findings+EXPERIMENT_LOG；恢复pending_experiments并查它们真实状态；读代码/原始结果/当前主张及上一轮未闭TODO。
2. **A：review**：给primary paths、raw results、changed-file/diff。medium普通审；hard附审阅者原始记忆并可辩；nightmare追加直接读仓库的独立验证。reviewer选择按 invocation→project `.aris/reviewer.json`→host default，保存route/session/cwd。
3. **B/B.5：解析并保存原文**：完整raw response先落盘，再解析Score、ready/almost/not ready、ranked minimum fixes；将该审阅者自己的原话追加REVIEWER_MEMORY，不让执行者重新概括旧关切。
4. **B.5.1：候选停止转移**：读取 `review_gate.py` 的结构化decision/next_backend，而非自行解释其reason prose。score≥6 **且**ready/almost才可能stop；“高分但not ready”继续。
5. **B.6：hard/nightmare反驳**：执行者最多选3条实质关切，写accept/partial/reject及证据；原reviewer判sustained/overruled/partially sustained；按最终裁决重算门，不能早先positive跳过待裁决项。
6. **人工点**：HUMAN_CHECKPOINT开启才等用户选择实施/改指令/skip/stop；否则自动继续。
7. **C：真的修**：按剩余action list改代码、分析、论文，必要时部署；资源过大或外部材料不可得的项明确flag；能以已有分析解决则优先，不承诺修完就直接再审。
8. **D：等新结果**：监控本轮新jobs、回收log/output，配置W&B时查训练质量；>30分钟的job运行期间继续其它独立fix。
9. **E：文档/状态**：在AUTO_REVIEW追加raw review、debate、actions、results、status；写当前run_id、round、session、路由、实际model/effort、completion/scope、score/verdict、pending jobs；只有在这一步才持久化最终stop/receipt。否则round+1回A。

### 后端细节与停止语义

主线含大量Copilot native marker/challenge/evidence与compatibility drive→external finalizer路由，这些是host身份/协议需要，不是可移植的数学推理步骤。Antigravity/Grok/Claude route须检查真实成功、读完所需范围及返回model；positive同家族只能provisional，跨家族完成范围后可accepted。Codex镜像使用fresh native reviewer+后续continuation，同样保留provisional。审阅失败/unknown identity/范围未完成不能被当成negative后继续刷分或模型PASS。

循环正常终止有两类：**达到正面门**与**MAX_ROUNDS=4耗尽**。两者都把state记completed，但后者必须列剩余blockers和pivot/manual建议。`status=completed`表示这一轮次流程结束，不是研究已解。用户stop也是收卷，不是提升判决。

终止后还做一个实质handoff：在AUTO_REVIEW写final method/data flow，供paper-illustration读；调用 `/result-to-claim`生成 `CLAIMS_FROM_RESULTS.md`，供paper-plan消费，避免planner重新从叙述中臆造已验证claims。若技能缺失可省略文件；若返回第一行 `verdict: REVIEW_UNAVAILABLE`，必须原样保留并标UNADJUDICATED，下游不能把文件存在当validated。

补读result-to-claim可见该门怎样向后和向前路由：读取原claims contract及原results；不存在的value/path确定性拒绝；`no`写postmortem和未来禁重试约束，然后换idea或方法；`partial`先收窄working claim、记录gap、补证据后重跑，反复partial考虑换线；`yes`且仍缺ablation才进入ablation-planner，全部证据齐才写作。可选wiki记实验与supports/contradicts关系，不能把empirical support改成proof-verified claim。

### 数学可复用与不可照搬

可复用的是“当前精确主张＋原始证明/程序产物→针对未闭义务审阅→证据化反驳/真修→只针对变化复核→保留结果→实际范围裁决”。需要换掉的是NeurIPS/ICML评分、6/10即ready、最多四轮就有机会submission这些产品目标。定理成立的停止门应是原命题所有义务已闭合及指定核验完成；轮数/预算只能触发保存未解状态与路线决策。

## 5. `/paper-writing`：产物是一篇论文，数学结论是写作前置

输入优先NARRATIVE_REPORT；也接受方向+results先补narrative；已有PAPER_PLAN可跳过phase1，但仍须phase1.5合同。它不重新发明研究题目，也不以PDF编译成功证明定理。

| 顺序 | 调用/动作 | 实际输出；后续怎样消费 |
|---|---|---|
| 0 | 从invocation assurance或effort推导draft/submission，写 `paper/.aris/assurance.txt` | 最终门重推导并对照此值，避免恢复时沿用旧宽松等级 |
| 1 | `/paper-plan "<input>"` | `PAPER_PLAN.md`：Claims-Evidence Matrix、sections、figure/data位置、citation scaffold；图表和正文按它工作 |
| 1.5 | 从plan+narrative提出10–20条可检查合同，fresh reviewer交涉，最多3轮 | `PAPER_ACCEPTANCE_CONTRACT.md`保存accepted/contested、原始争议、session；accepted后冻结，phase2–5执行，phase6逐条看final PDF/results是否满足 |
| 2 | `/paper-figure "PAPER_PLAN.md"` | `figures/` plots/tables、generation scripts、`latex_includes.tex`；phase3插入真实图和引用 |
| 2b | 需结构图时按mode调 `/figure-spec`、`/paper-illustration`、`/mermaid-diagram`等 | 图文件及可编辑spec；手工缺图先补齐再写，不以占位图当完成 |
| 3 | `/paper-write "PAPER_PLAN.md"` | `paper/main.tex`、sections、references.bib、math_commands；按plan和已生成图写完整正文，来源正确的bib，不是随机生成引用 |
| 4 | `/paper-compile "paper/"` | `paper/main.pdf`，自动多遍编译/有限修复；引用、页数、字体等实际检查完成后才进改进 |
| 4.5 | 有theorem/lemma/proof调 `/proof-checker "paper/"` | PROOF_AUDIT；FATAL/CRITICAL先修；不能让后面的语言润色遮蔽数学错误 |
| 4.7 | 有raw results调 `/paper-claim-audit "paper/"` | 逐数字对原results；FAIL先修；WARN记录 |
| 5 | `/auto-paper-improvement-loop "paper/"` | 两轮fresh审阅→实际修订→重编译，保留round0/1/2 PDF及PAPER_IMPROVEMENT_LOG；写作worker设置与reviewer设置分别传递 |
| 5.5 | 检测numeric claims+raw evidence后**再跑**paper-claim-audit | 最终文本变了就需要最终对应审计；有数字而无raw evidence则不能声明完成 |
| 5.6（主线） | 理论/scope-heavy调 `/kill-argument "paper/"` | KILL_ARGUMENT.md/json；把局部证明均正确但标题scope仍夸大的问题单独判；submission无适用内容也发NOT_APPLICABLE |
| 5.8 | `/citation-audit "paper/"` | CITATION_AUDIT核真实性、metadata、引用语境；按其结果修/人工处置，不把只存在的论文当支持正确 |
| 5.9 | 主线submission默认integrity-forensics；Codex默认关，仅opt-in deterministic slice | BLOCK阻止最终化，具体义务送数字/引用/证明/范围的修复门；Codex slice可报flag，不能称CLEAN |
| 6 | 看合同、运行 `verify_paper_audits.sh paper/ --assurance submission`及适用forensics门 | 读audit-verifier-report的exit与overall_assurance，才写final report；exit0但provisional必须仍标provisional |

### 写作回退和停止

plan checkpoint若需要改就改后重呈；AUTO_PROCEED=false才按phase等待。主流水线没有venue时defer，而单独paper-writing常量默认ICLR，因此**调用者必须绑定实际venue**，不能以子技能默认值替用户决定刊物。

合同三轮后仍no时保存争议，标contested；原文同时写“pause人工裁决”和“无人响应则继续，但最终Submission-ready:no”。这是一个无人值守语义存在张力的规则，不应复制成等待沉默后自动批准。可借鉴的只是保留争议、未争议义务继续、不能把争议藏掉。

phase6有三个独立门：合同未争议assertions无violated；audit verifier绿；适用forensics门绿。verifier只检查审计JSON、schema、freshness、trace等，**不读合同也不亲自证明定理**。非零时按MISSING/STALE/BLOCKING_VERDICT/SCHEMA_INVALID定位重跑或修真实问题。draft可产出reviewed draft；submission需always-emit各audit，适用内容不存在写NOT_APPLICABLE而非静默跳过。

MathRSI可以将这一写作链作为研究闭合之后的可选发布路线。定理规格、依赖、实际caller、确定性覆盖与Lean状态应来自研究材料，进入claims-evidence关系；不应反过来为了完成论文固定章节或提升review score改变原题。用户指定Root事实/Gemini主写的分工可以直接对应其writer/reviewer独立设置，事实与最终核验仍归Root。

## 6. 读取实际消费方揭示的源码差异

这些不是本次修改建议或已复现运行故障，只是所读修订中会影响编排的静态证据：

1. **父摘要弱于子技能停止门。** Codex `research-pipeline` Stage3写score≥6即可停止，实际Codex `auto-review-loop` 常量及PhaseB.5.1仍要求score≥6 AND ready/almost。README W2也只强调score。正确消费以子技能完整门为准。
2. **sanity预算摘要过期。** `research-pipeline` Stage2摘要写up to3 attempts，主线bridge Phase3实际是2patch+2clean reimplementation。MathRSI需在具体执行动作处定义恢复，不依赖父概览的旧数字。
3. **Codex paper-writing到共用verifier有具体断接。** 主线存在Phase5.6并要求KILL_ARGUMENT.json；Codex镜像删除该phase，Phase6只列三项audit，但共用 `tools/verify_paper_audits.sh` 第38–43行 `MANDATORY_AUDITS` 固定含PROOF_AUDIT、PAPER_CLAIM_AUDIT、CITATION_AUDIT、KILL_ARGUMENT四项。新的Codex submission运行若无已有KILL_ARGUMENT产物，会留下verifier必需输入未由该caller创建。这里没有运行helper或宣称发现所有相关问题；只是调用/消费源码之间的可定位缺口。
4. **README部分仍为旧默认。** 其W3写illustration默认为gemini、mandatory audits为三项；当前主线SKILL默认figurespec并有四audit和forensics。README可找入口，不能充当操作规格。
5. **通过bridge不等于结果支持主张。** 主调度接受bridge的deterministic jobs完成，只表示执行完成；result-to-claim才科学判决支持程度。两者不能合并成同一个“experiment PASS”，数学里同理：程序正常退出、全域覆盖、概率界严格、原题推论是不同义务。

## 7. 给 MathRSI 主技能的编排启发

真正应带回主技能的是以下一条能够被agent照着执行的骨架，而非把ARIS全套ML阶段改名：

> 读取原题与最近真实断点 → 决定下一未闭数学义务 → 选已有技能/领域程序/人工推导作为本次动作 → 明确交付物和何种结果会改变决策 → 实际产出或反证 → 用所属验证接口检查 → 将结果运输回原命题及分支图 → 继续、补条件、重实现、换表述/换路线或带未解状态收卷。

每个箭头都应说明**调用者拿什么输入、谁做什么、写出什么、Root读到哪个字段/见证后采取什么动作**。例如“局部分类程序跑完”交给下一步的应是已证明覆盖域、实际输入对应、规范代表与原对象运输、结果/失败见证；不能只交一张成功计数表。原题caller不闭合时明确返回这一义务，不能留在最后才发现条件定理没有调用者。

可复用的具体工程取舍是：正文技能负责编排和判断、领域程序负责既有确定性工作；已有有效方案先复用；小真实输入先贯通；每轮只对新材料和未闭关切动作；完整产物先回收再派下一步；语义判决、机械完成和资源预算各自命名；缺外部审阅时保留真实证据及未审状态；最终交付从原命题消费证明链，绝不由文件数量、分数或耗尽轮数推断完成。

本报告只提取这五类编排器可迁移部分。W1候选生成/文献探索、数学证明技能及MathRSI现有源文件的具体重写由Root其它阅读与设计负责；这里没有把未阅读模块伪装为已覆盖。
