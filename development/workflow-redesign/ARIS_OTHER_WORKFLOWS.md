# ARIS W4／W5／W6／M及共享编排契约：定向全文阅读

本页为2026-11-01 MathRSI编排修订的阅读底稿。来源是本机 `/Users/rfy_naiveai/Desktop/aris_main` 的主线 `skills/`，不是已安装Codex镜像的逐项比对。这里只提炼实际源文规定的组合、交接、失败与恢复机制；没有执行这些workflow、调用reviewer、启动Goal、编译或重跑数学计算。文中“可用于MathRSI”是设计建议，不是能力已经实现或验证的声明。

## 读取范围与引用约定

以下路径均相对上述ARIS根；行号定位本次读到的文件快照。`§`是标题／阶段名，后续上游改动可能移动行号。

| 文件 | 实际读取范围 | 范围限制 |
|---|---|---|
| `README.md` | 1145–1212：完整W4／W5／W6；1362–1445：完整W M | 没有读完整README；W5／W6的外链 `docs/RESUBMIT_AND_TALK.md` 未读 |
| `skills/rebuttal/SKILL.md` | 1–389，全文 | 没有递归读取其全部链接 |
| `skills/resubmit-pipeline/SKILL.md` | 1–458，全文 | 未执行示例命令，未核验每个child实现 |
| `skills/paper-talk/SKILL.md` | 1–392，全文 | 未读完整paper-slides／slides-polish实现 |
| `skills/meta-optimize/SKILL.md` | 1–450，全文 | 未读meta-apply源码／技能全文 |
| `skills/shared-references/output-composition.md` | 1–93，全文 | 其余output-*文件未读 |
| `skills/shared-references/resumable-runs.md` | 1–109，全文 | 未读／执行 `run_state.py`，关于代码强制的描述是文档声称 |
| `skills/shared-references/integration-contract.md` | 1–462，全文 | 未逐个审计表中helper |
| `skills/shared-references/assurance-contract.md` | 1–273，全文 | 未执行外部verifier |
| `skills/shared-references/review-tracing.md` | 1–502，全文 | 未读trace helper实现及全部backend契约 |
| MathRSI `AGENTS.md` | 全文 | 用于限制本页建议与写入范围 |

因此不能从本页推断“已完整阅读ARIS仓库”“所有源文与helper实现一致”或“这些workflow已在MathRSI运行通过”。

## W4：从外部反馈到可跟进的回应，不直接变成新的研究结论

`rebuttal/SKILL.md` §Required Inputs（88）、§Safety Model（97）、Phase 0–3（107–155）明确消费论文、逐reviewer原文、venue规则／输出方式、当前轮次。输入形状会改变最终产物：一个共用回复与逐reviewer独立线程分别走不同结构，后者每份必须自足，不能写“见另一位reviewer的回复”。它先保存 `REVIEWS_RAW.md` 原文，再给每个原子问题稳定 `issue_id`、`raw_anchor`、问题类型、严重性、回应方式与状态；`STRATEGY_PLAN.md`才据此决定共性主题与重点分配。`QUICK_MODE`在这一点停止，交付问题板与策略，不伪称已完成全文回复。

本workflow把几件容易混淆的事拆开：问题已回答不等于证据充足；证据存在不等于作者已授权承诺；不准备修改论文也不等于可以删除问题。每条问题最终需是已回答、有意延后或需用户输入；每项事实要有来源，每项承诺要有状态。Phase 4–5（184–280）的 `REVISION_PLAN.md`反向核对承诺：正文中每个隐含／显式论文修改都必须接到一个带issue ID的修改项，计划里也不能多出正文未支持的孤立承诺。它不是把“回答一段漂亮文字”当流程终点。

Phase 3.5（156–183）可按问题生成mini plan，写清要运行什么、成功判据与成本，再交 `experiment-bridge`；失败／不确定结果转为窄让步或未来工作边界，不冒写阳性证据。这里有一个不宜照搬的源文细节：它说completed experiments可标作 `user_confirmed_result`。这只是W4内部标签，不能在MathRSI中把worker完成或实验脚本结束等同于用户确认、原命题证明或验收；应保留真实执行者与验证范围。

Phase 6（281–308）只在完整draft上先审一轮，再对关键reviewer的回应做有针对性的追问；无新增实质问题即可停，总计硬上限五轮。Phase 8（342–353）接收到新意见时追加原文、接回原issue或创建新issue，写delta reply并原地更新revision plan，而非整套重生成。Phase 0通过 `REBUTTAL_STATE.md`恢复，但此SKILL没有把它自动等同于后述 `run_state.py` accepted协议。

Phase 9（354–369）的HTML失败是非阻塞：记录失败，保留plain／rich canonical回复。这里显示“内容工作完成”和“展示增强失败”应分别汇报；不能让可选渲染消耗全部研究预算，也不能因渲染失败否认已完成的内容。

对MathRSI可复用的是：把外部数学质疑定位到原句与具体义务，再决定补推导、补进口核查、补计算还是只澄清；对新增反馈只处理delta；没有采取动作的问题保留处置理由。venue字数分配、作者承诺与提交接口不是数学研究默认阶段，也不应在每个局部引理后强加。

## W5：编排器的职责是使已有工具在当前限制下真正接得上

`resubmit-pipeline/SKILL.md` §Why This Exists（23–33）直接解释了独立编排层的价值：auto-improvement已经会逐轮改稿，但它不会替用户选择底稿、转venue、冻结可改范围、接入旧评审并决定哪些要求不能做。W5不发明另一套写稿器，而是补这些上下游责任。

三个必需输入是已打磨的源稿目录、目标venue／模板、旧review corpus（56–72）。Phase 0（75–104）建立独立新目录，禁止覆盖旧submission；Phase 0.5（105–146）先确认新形状能编译，再记录页数、匿名性与标注残留。只有这个baseline存在，后续“改进”与回归才有对象。物理隔离来自这个workflow的不可覆盖合同，不意味着所有数学局部尝试都需要复制整个工程。

Phase 1（147–190）把三个detect-only audit和旧review原子问题一起交给Phase 2。关键不是child名字，而是它们的实际模式：bibliography冻结时，`citation-audit`必须用 `soft-only`，使发现转成逐次引用语句的修订建议，不让普通FIX／REPLACE结果暗示改bib。旧评审项有稳定W ID和addressability：能用文本修、只能部分处理、在现有限制下不能处理。这一步决定后续是否仍适合microedit，而不是不顾结果一律进入改稿循环。

Phase 2（191–277）把allowed／forbidden paths、forbidden operations写成whitelist，并要求每个edit引用W ID或audit finding ID。它特别纠正曾经设想的child调用：`auto-paper-improvement-loop`没有 `--rounds`、`--reviewer-model`或 `--resume-after-round-checkpoint`这些CLI旗标。真正的调用是一次进入已有loop，再利用其 `HUMAN_CHECKPOINT`让orchestrator看每轮diff。这个案例说明，写一个看似合理的调用名称并不构成集成；必须核对child真接口与谁控制循环。

回归检查针对实际修改触发：定理相关diff再审proof，数值相关diff再审claims；每轮有snapshot作为后续比较底稿。正文修改不是靠“reviewer提出过”就自动授权，仍受whitelist约束。具体rsync／regex示例未经本次执行，不应当作可靠实现承诺。

Phase 3（278–297）的 `kill-argument`是残余风险分流，不是“收到攻击就盲目多改一轮”：critical且可文本修的入extra-round queue；需要新框架／实验且被用户禁止的入escalation queue。§Convergence（370–381）要求同时满足无新增critical／major可修问题、页数通过、相关audit无阻塞；默认两轮没有解决就报告checkpoint，不能靠无限循环宣称自动收敛。

Phase 4（298–357）在最终改动后再编译、再核数值，明确发布／Overleaf写入沿用 `overleaf-sync`既有边界，不造平行推送机制。恢复后发布前要重新检查CURRENT参数和freshness，旧opt-out不自动迁移。§Failure Modes（397–417）把 `USER_DECISION`作为运行期等待状态，与BLOCKED／ERROR／FAIL分开，并为每种reason_code写恢复动作。§Master Ledger（382–396）集中链接子产物、逐轮trace和用户决策，让新venue目录成为可交付整体。

对MathRSI最有用的不是“把研究固定成两轮”，而是：每次委派明确当前允许改什么、输入哪个版本、输出供谁消费；处理结果必须回到具体问题；遇到现有授权下做不了的要求给出可继续的分流。关键数学证明不能用文本微改或弱化目标冒充闭合；不应把W5的严禁新定理、页数控制、默认人工checkpoint带进自主研究阶段。

## W6：真正的复用可能需要形状适配，且必须保留原内容对应

`paper-talk/SKILL.md` §Prior Skill Relationship（378–383）组合paper-slides、slides-polish、claim／citation audits，并明确不默认跑kill-argument：上游智识压力测试与下游deck QA解决不同问题。已完成deck只需polish时直接调用polish，避免重建整个pipeline（§When NOT to Use，371–377）。

§Inputs／Output Layout（69–119）和Phase 2（163–185）规定orchestrator是 **non-renaming consumer**：接受child实际产物名 `presentation.pptx`、`main.tex`、notes与script，下游绑定这些路径；返回后检查产物是否存在，不把自己希望的命名当child已承诺接口。原paper只读，baseline deck保留，polish写新版本；内容／顺序／notes受既定不变量约束。

最具体的可借鉴机制在Phase 4.0–4.3（208–291）。paper audits期待 `main.tex + sections + results + bib`，而slide deck没有这个形状，于是W6建立 `audit-input/`：把可见slides、notes、完整讲稿分别抽出成sections，并连接原始results／bib／figures。audit后将synthetic section路径回译为slide K，最终报告引用用户实际认识的对象；临时staging可清理，audit与原始artifact保留。它也有意覆盖口头notes／script，避免只审可见bullet而漏掉真正对外讲的断言。

这可对应数学任务中的适配：例如有限表checker需要规范化输入，原研究对象不是该格式；编排器必须说明原对象如何进入checker输入、结果如何回指原义务。只“把文件转成checker能读”还不够，运输／覆盖正确性仍是数学义务。W6的文本staging本身不是这种数学保真的证明，不能以此给数学适配器自动背书。

§Assurance Ladder（27–40）、Phase 5–6（292–338）清楚说明降级：draft、polished、conference-ready运行不同阶段；最终导出按实际final PPTX检查页数、比例、空白与notes。conference-ready必须要求的audit全PASS／适用时N/A且export integrity PASS；WARN也要降级，并指出具体audit。effort与assurance独立（339–355），低成本并不意味着可以漏掉用户要求的检查。

对MathRSI应采用的是“所需义务没过就报告实际最高状态”及“外观／结构检查不升级数学状态”。talk workflow默认major phase等待用户批准，是这个产品约定；不能借此制造MathRSI已有授权任务的重复确认。

## W M：维护核心是另一项工作，不能被单题局部成功偷偷触发

`meta-optimize/SKILL.md` §Privilege Boundary（23–60）把producer与landing分开：本skill读取usage data、提出patch、写 `.aris/meta/`中间产物，单独human-invoked `meta-apply`负责最终fresh jury与应用。Step 4（265–325）的review是advisory_screen，不能被producer转述为真正landing验收。源文也诚实承认无Write／Edit和hook blacklist不是完整OS隔离，未完成的provenance verifier不能冒称已防住恶意Bash写入。

Step 0–1.5（87–215）先看是否有足够日志、上轮瓶颈是否真的解除、目前瓶颈移到哪；日志不足就停止优化，不为维护而维护。Step 1指出usage log只知道哪些skill被用了，看不到本来应触发却遗漏的skill；如果要判断description漏触发，要用独立probe并看confusion而不是只看总体rate。它也允许删掉新模型已无需的scaffold，但模型更新本身不是证据，必须有该step的能力／运行证据。

Step 2–3（216–264）要求每个patch针对一个有证据的目标，最小化修改；不把一次网络失败或“某工具不能……”固化为长期拒绝。Step 5–6（326–390）报告changes not made、需要什么更多数据、哪些patch可stage，清楚写下一步由谁执行。§Triggering（416–436）中的session-end readiness只是提醒，不会自动执行优化。

对MathRSI可直接借用这种责任边界：插件研究中发现base问题，留一个有失败路径／当前影响／建议改动的独立开发项；研究继续使用当前明确版本，不现场改变验收或重定义目标。用户本轮若已授权开发核心修复，则Root可在该开发任务中推进，不必照抄ARIS的人类手动invoke语法重复索权。日志量阈值、hook安装、review打分不应成为所有数学方法提炼的统一门槛。

## 五份共享契约各自补了哪个编排缺口

### 输出组合：owner与合并方式是调用参数，不由磁盘残留推断

`output-composition.md` §§Two states／Composed-mode signal／Fold in／Orchestrator responsibilities（18–85）要求调用者明确传 `composed: <canonical-report-path>`；没有就standalone，`standalone`覆盖冲突。旧报告文件恰好存在不触发composed，避免单独调用child的结果被静默吞掉。composed时独有结论交给owner写入唯一canonical report或明确管理的stage文件；review traces仍各自保留，报告只链接，复用脚本／结果也保留。临时重复summary和已合并scratch可以清理。

对MathRSI的含义：总控必须写清哪个文件归谁、child回交哪段内容、哪些真实证据留下。多个agent不应同时修改canonical报告；它们交回结果后Root吸收。无需为几个文件再造MANIFEST或把原始证据复制成三份“汇总”。

### 可恢复：从第一个尚未可信闭合的阶段继续，而非从“写完了”跳过

`resumable-runs.md` §§One idea／Who may call accept／Integration pattern（14–96）把执行 `done`与有记录验收的 `accepted`分开；resume跳过accepted／按配置不适用的skipped，重跑running／failed，对done但未accept的phase补验收。accepted需durable verdict ID与reviewer／确定性checker身份；gate结果独立记录，不能冒充phase acceptance。一个run一个orchestrator，外部调度只触发resume，不拥有结论。

这份文档写的是预定义phase列表；它不能直接代表开放数学研究每条路线都须走固定状态机。MathRSI可以在现有checkpoint中用自然语言说清“已完成什么、哪项验证未完成、下一具体动作”，按义务接回成果，而不强制新建Python状态管理。确定性检查能accept的也仅限它真实检查的义务；compile exit0不能验收没有接到原目标的整个数学阶段。

### 集成失败：不是所有helper缺失都应阻塞，也不是所有都可忽略

`integration-contract.md` §2（48–359）区分：A关键gate缺失即阻塞；B可选副作用警告后继续；C取证helper缺失直接按schema写证据，不能漏trace；D1多源按优先级取首成功；D2聚合所有可用源并记录贡献／失败；E诊断的非零退出记录而不传播成研究失败。相同helper在不同角色可用不同policy，如wiki ingest对paper summary是副作用，对research-wiki本身是核心功能。

§§1、3–6（37–47，360–423）要求显式activation predicate、可见receipt、长流程入口列出应做项、明确backfill／repair输入，以及承重处的外部verifier。其要解决的是真实静默no-op：口头说“接入wiki”但papers为空；说“高effort”但全部audit跳过。并不意味着每次推理都加一个schema、hash或脚本。MathRSI当前本机AGENTS要求自包含helper指向 `base/tools`，因此不能照抄ARIS回退作者 `aris_main`／`~/.aris/repo`的resolver链。

### 验收：child报告事实，parent决定当前交付是否能继续

`assurance-contract.md` §§Verdict State Machine（63–92）、Subskill Contract（198–214）区分六态：PASS、WARN、FAIL、NOT_APPLICABLE、BLOCKED、ERROR。N/A是阶段确实检查过且内容不适用；BLOCKED是本来适用但缺证据／依赖；ERROR是调用异常。child总要留下verdict，parent按当前交付要求决定blocking，不让十个child各自发明停止政策。

§Required Audit Schema／Verifier（93–197）规定原始输入对应、trace、actual模型／effort与scope；same-family positive仍provisional。外部verifier既查artifact存在又查freshness，并输出overall_assurance；exit0在provisional情况下也可能出现，不能直接当submission-ready yes。它明确禁止把四种semantic paper audits标deterministic以绕过要求；这个paper-specific限制不意味着Lean内核验证不具备数学价值。数学任务要看checker究竟验证了原命题、局部算术、覆盖还是文件形状。

对MathRSI不宜默认复制完整paper assurance JSON与全文件hash。本项目HERO和薄Python约定优先：只有当前真实freshness问题会影响下一步时才复用这些机制；已有Lean／独核结果按对象、义务与输入版本说明，不追求装饰性统一证书。

### 审阅trace：一次调用有多重事实，不能压成“模型通过”

`review-tracing.md` §§When to Trace／Completion and assurance（10–21，137–194）分别保存调用是否成功完成、所需范围是否覆盖、skill自己的positivity判定、raw verdict、requested与实际reported model／effort来源。backend名不代表model family，选择provider更不代表acceptance；run初始meta不代表后续每轮的整体结论。failed fallback每次单列，不能只留最后一次成功。trace accepted也不代替实质proof／claims gate。

§Debugging With Traces（458–497）要求遇到审阅反转先对比原始request／response，找出实际判断变化或阅读范围差异，再决定是否重审。它把trace当后续决策输入，不是存完即忘的合规附件。MathRSI应保留指定跨模型讨论的真实范围与未完成调用，不机械重审未变材料；生成正文worker与reviewer也需分别记录，不能因为Gemini写过某段就称Gemini独立审过该段。

## 源文内部差异：采用机制时须逐项核对，不能整段搬运

1. README W M（usage）仍举 `meta-optimize apply 1`，现行 `meta-optimize/SKILL.md`明确没有in-skill apply，另交meta-apply。设计采用现行职责拆分，不从README示意恢复旧直接apply语义。
2. integration-contract开头要求六项齐备，§6又限定verifier／diagnostic在承重时才需要；MathRSI应按影响范围理解，不为不承重的文字交接写外部验证器。
3. assurance总契约允许WARN非阻塞，paper-talk的conference-ready要求全PASS／N/A，resubmit convergence也比总契约严格。必须保留**具体workflow**交付含义，不能用一个全局PASS／WARN规则覆盖。
4. `resumable-runs.md`一般化说deterministic verifier可accept；assurance对semantic paper audits另有限制。两者接合时以义务范围解释，不得把file-exists或compile结果泛化到语义证明。
5. rebuttal §Scope说不自动跑新实验，Phase 3.5允许显式AUTO_EXPERIMENT；Phase 9默认render rich draft，而per-reviewer mode没有同形rich artifact。借鉴前应先确认启用条件和当前输出分支，不是照字面强制跑。
6. resubmit的§Inputs把缺review corpus视BLOCKED，Failure Modes又把检测到无旧review的新稿视N/A；两者可按“输入缺失”与“工作类型不适用”区分，不能合并成继续正常改稿。它的Phase 4把diff写 `.aris/DIFF_REPORT.md`，Output Contract又列根级 `DIFF_REPORT.md`；实际实现需要选一处canonical路径。
7. resubmit Phase 0说新目录独立组成，但bibliography示例仍引用 `../references`。这是作者为特定文件布局写的组合例，不证明任意源稿搬运后自包含。paper-talk staging中的symlink也仅适用于临时audit适配，不应复制为MathRSI最终可携带包方案。

## 对本轮MathRSI修订最直接的落点

总控正文应在每个实际交接处解释：现在有什么原始输入与既有结果、为何选择这个child、child接受哪种形状／具体参数、回交什么独有产物、这些产物怎样接回原问题、出现哪类失败时换哪一步。以上几份workflow的价值就在这些连接，而不是共同拥有“计划→执行→检查”的相同标题。

研究任务可以保持自主选线与自然语言checkpoint。它至少应让下一个agent直接区分“发现了条件工具”“真实输入已经满足工具假设”“局部表已验”“完整域已覆盖”“最终原题已闭合”，并从尚缺的那个连接开始。文件名、状态数和review轮数无需统一；责任owner、输入输出对应、真实下一步与准确结论范围需要一致。
