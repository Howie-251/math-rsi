# ARIS meta 工作流复用与数学适配底稿

2026-11-02。只读检查了 MathRSI 的 `AGENTS.md`、`docs/ARIS_REUSE.md`、`base/ARIS_SNAPSHOT.json`、`docs/EVOLUTION_WORKFLOW.md`，以及 ARIS 两宿主的完整 meta-optimize／meta-apply、直接共享合同、模板及 helper 实现。未运行优化、安装 hook、调用 reviewer、改变任何研究 Goal 或写 ARIS 源仓库。本文件是实现底稿，不是已完成演化运行的报告。

建议新增有完整执行内容的 `mathrsi-evolve` 数学外层工作流，保留 ARIS 两技能的完整原件作为本仓可读底稿，逐项声明适配，而不是原样调用后声称完成数学演化。既有 `docs/EVOLUTION_WORKFLOW.md` 已提供正确设计边界；尚不能替代可调用技能的输入、调度、返回与恢复合同。

## 已核对版本与实际差异

MathRSI 当前快照固定 `c485faa59a68e51c6575dea67ca57abc7a6a2b9c`，207 文件、2,915,213 字节，selection 不含 meta-optimize 或 meta-apply。源 ARIS 当前 HEAD 为 `2927b40b2ea37774de53763338c5e8f91a7601e6`。本次列出的 45 个闭包文件在该固定提交与当前源工作树逐字节相同；已存在 MathRSI base 中的对应文件也逐字节相同。因此补充这两技能不需要顺带升级整个上游。

下列源码位置特别影响适配，不能只读 Claude 主线再假定 Codex 相同：

| 原件 | 实际机制及定位 |
| --- | --- |
| `skills/meta-optimize/SKILL.md` | 450 行；24–59 行明确只读 producer；265–323 行为 advisory pre-screen；369–389 行只 stage，交独立 meta-apply。 |
| `skills/skills-codex/meta-optimize/SKILL.md` | 361 行；frontmatter 仍开放 Write/Edit；292–305 行仍指导 `/meta-optimize apply` 并在本技能内 apply。这与下面 Codex applier 对 producer 的描述冲突。 |
| `skills/meta-apply/SKILL.md` | 152 行；29–31 行要求另一次人工显式调用；49–63 行为 fresh jury、KILL 不可被人覆盖、严格跨家族；91–115 行 backup/apply/stamp/log 后只建议下次测试。 |
| `skills/skills-codex/meta-apply/SKILL.md` | 166 行；34–36 行同样要求人工调用；54–69 行允许同家族 provisional 落地，跨家族或适用确定性验证才可 strict stamp；124–129 行落地后建议再测试。 |

这里确有可复用能力，也确有上游尚未解决或不适用于本次数学维护的合同；不能把它们合并成一个不存在的统一原版流程。

## 应实质保留的机制

**从使用证据找当前瓶颈，并记录它怎样转移。** meta-optimize 的 Step 1／1.5 不只是列建议；它读取既往事件、人工纠正、失败与模型变化，命名当前制约，消费上轮瓶颈再提出补丁。数学适配应从真实证明过程恢复“原目标—实际操作—失败或浪费—下一义务”，比较上轮修复是否解决原瓶颈。可有一个主要瓶颈，但不能强迫同时独立发生的数学缺口都归入同一标签。记录必须回答下一行动会因哪条证据改变。

**一项行为变化有一项实际 diff。** Step 2／3 的优先顺序、最小补丁、理由指向证据、允许删除无效脚手架，都值得保留。数学改动应落到真实 caller、被调技能、返回消费者或领域方法，而不是只添“应提高效率”说明。一次必要的跨文件契约修复可作为一个补丁包；“one patch per target”不应被机械解释为每文件一个。模型升级只能触发重读，不能单凭名字删除证明对齐、实际输入连接或验收义务。

**提案者的认可不替代实际补丁的独立检查。** Claude producer 的 advisory_screen 与 applier 自己读取实际 diff 的 fresh review 是有价值的职责分离。MathRSI 应把候选修改、独立跨模型设计审阅、未参与作者的受影响路径试用和 Root 接纳分开记录。Root 必须读回真实输出，不能消费作者代写的“PASS”。

**对抗审阅要读原件，并保留可恢复会话。** 复用 reviewer routing、paths-first 原件输入、actual identity／completion／scope、原始 prompt/response/session、定向续接。第一次独立判断后，reviewer 应能对具体反驳与修复继续判断；不能用 fresh jury 的“无历史”要求删掉整条证据对话。fresh 只用于确有独立性需求的新判断，不要求所有修复都重开模型。

**保留负结果与环境修复的区别。** `capture_filter.py`／capture-antipatterns 防止把一次网络或安装故障固化为“某模型不能用”。数学失败实例、反例、条件引理、重启条件则是正当知识，不应被过滤掉。把 durable 方法限制和当日服务故障分开，记录真实失败并修具体配置。

**可撤回版本与过程收据。** 保存旧文件或 Git diff、候选基点、实际合入变化、审阅与试用范围、采用时机。`provenance.py` 明说 stamp 是过程收据，不是正确性保证；沿用这一语义。旧研究不因新版本存在而自动采用，不借维护恢复暂停 Goal。

## 必须写入数学适配的变化

| 原机制或假设 | 数学工作流中的明确替换 |
| --- | --- |
| 必须 `.aris/meta/events.jsonl` 且 ≥5 complete runs | 接受有原件定位的历史证明、wiki、checkpoint、实际 caller、命令与回收记录。一个可复现的合同错误已经足以修复；无事件日志不造日志、不凑五次调用。多次频率／收益主张则仍须足量数据。原 shell 实际数的是 skill_invoke，不能称五次完整流程已被验证。 |
| 频率、OOM、投稿分数、轮次到阈值 | 检查完整义务是否减少、归约是否保真、实际输入是否接上、错误覆盖门是否及时暴露、结果回收是否延误、总 CPU／内存／墙钟／读回与模型成本。分数轨迹不是数学真值或维护接纳门。 |
| 仅优化 harness，不优化研究产物 | 先分类 workspace／plugin／base／defer。新证明与反例留工作区；可复用领域工具在插件；跨领域调度与返回合同才进 base；证据不足或依赖未备则 defer 并给重试条件。允许同一实例形成不同层次的独立变化。 |
| Codex producer 自己 apply | 适配入口排除原 Step 6 in-skill apply，统一候选写域与 Root 接纳职责。保留原件不改字节，同时明确执行的是数学适配。 |
| meta-apply 只有显式 `/meta-apply` 才可运行 | 不冒称本次已执行 upstream meta-apply。MathRSI 按用户现有维护授权完成可撤回候选实现、审阅、试用、Root 接纳；若实际另行调用原 meta-apply，必须遵守其人工调用要求。原件的新增许可门不能被无声移植来重复索取已给授权。 |
| reviewer PASS／KILL 具有最终否决权 | reviewer 提供可核的缺陷与条件，Root 对照原件裁定，误读可证据回应。服务失败不当认可；真实未解风险不抹去。但模型判断本身不能替代数学验证或成为数学真理否决权。 |
| after landing: test next run | 修改先留候选分支／独占副本，独立使用者实际走受影响路径，Root 读回后决定修订、拒绝或接纳。关键行为未运行只能记 pending，不能用静态认可或 stamp 冒充已验。 |
| raw score≥7 与统一 recommended 状态 | 用本提案的准确接纳问题：原错误是否消失、原量词与验收是否保持、caller/consumer 是否接上、引入哪些真实代价。无须新统一评分器。 |
| 不改变 artifact schemas、不能影响既有 workflow | 对普通参数改动保持最小；若证据表明错误来自返回合同或 schema，就允许显式版本化的必要修复并验证实际消费者，而非因 v1 禁令保留已证实缺陷。 |
| global hooks／canonical fallback resolver | 本轮不自动装 hooks，不改全局设置。所有 helper 显式指向本仓 `base/tools`；旧本地同名 helper 优先与 `~/.aris/repo` fallback 都不承担 MathRSI 版本绑定。 |

独立试用应把行为和数学状态分开。例如检查“局部 verify 返回 prove”就必须看到子返回、父读取、父执行具体下一步；检查规范化保真就用真实共同对象与原输入验证运输；检查恢复就从真实断点继续。已知答案可以用于调用行为试验，但不是盲测或通用 RSI 增益证据。无需为了维护重跑无关全表、旧 Lean 或暂停研究。

## 自包含依赖闭包与精确成本

最省维护的补充是在现有固定上游版本旁**增补原字节文件**，保留本地 MIT 与逐文件来源，数学差异全部写在 MathRSI 自己的技能／references。既有冻结 `base/ARIS_SNAPSHOT.json` 无须在本任务中改写；由整合 owner 决定用独立增补 manifest 还是明确的一次快照扩展，避免将新增文件伪称原207文件已有。不要为这两技能升级全部 ARIS，也不要把外部 `/aris_main` 链接当交付。

### 仅缺七个原件：68,759 字节

| 相对上游路径 | 字节 |
| --- | ---: |
| `skills/meta-optimize/SKILL.md` | 24,917 |
| `skills/meta-apply/SKILL.md` | 8,983 |
| `skills/skills-codex/meta-optimize/SKILL.md` | 18,401 |
| `skills/skills-codex/meta-apply/SKILL.md` | 9,561 |
| `templates/claude-hooks/meta_logging.json` | 1,753 |
| `templates/claude-hooks/corpus_write_guard.json` | 837 |
| `templates/claude-hooks/corpus_write_guard.py` | 4,307 |

四个完整 SKILL 原件共61,862字节。三个模板是保留原版可读／可配置能力所需，数学适配无需默认启用；未启用就不宣称 hook 生效。若以原 snapshot 同格式扩展，净增后为214文件、2,983,972字节、selection从30项到32项；这是包装算术，不是本轮已修改的事实。

若要求一个完全独立、不复用现有 base 文件的复制目录，则完整**操作资源闭包**为45文件、472,445字节，加 MIT LICENSE（现有 base 已有）。这里的闭包含四个技能、28份递归相关共享 Markdown、10个直接／helper 导入依赖与样例、3个模板。不是把 integration-contract 的通用 helper 目录每一项都当作该工作流会调用的依赖。现有 base 对应38文件均已具备且字节相同，因此重复整包没有运行收益。

### 原有共享资源：保留两个宿主各自版本

以下11个文件在两套目录 `skills/shared-references/` 与 `skills/skills-codex/shared-references/` 各有一份，都是本流程直接点名或原件链接所需：

```text
acceptance-gate.md
capture-antipatterns.md
integration-contract.md
output-language.md
output-manifest.md
output-versioning.md
review-scope-limits.md
review-tracing.md
reviewer-backends.md
reviewer-independence.md
skill-governance.md
```

递归相关资源另有：两宿主各自的 `reviewer-routing.md`、`evidence-precheck.md`，以及 Claude 主线的 `effort-contract.md`、`output-composition.md`。合计28份共享 Markdown。Codex review-tracing 还有指向主线 reviewer-routing 的真实相对链接，不能只带 Codex refs 后声称闭包完整。上游 reviewer-routing 链接到的 `skills-codex/` 是目录导航，不是缺失可执行文件。

### 原有 helper／样例：10个，131,766字节

```text
tools/capture_filter.py
tools/provenance.py
tools/reviewer_route.py
tools/save_trace.sh
tools/review_gate.py
tools/copilot_native_evidence.py
tools/meta_opt/log_event.sh
tools/meta_opt/check_ready.sh
tools/meta_opt/trigger_eval.py
tools/meta_opt/trigger_evals.sample.json
```

`capture_filter.py`、`provenance.py`、`reviewer_route.py` 只用 Python 标准库。`save_trace.sh` 在实际路径导入相邻 `review_gate.py`，Copilot native 分支还用相邻 `copilot_native_evidence.py`；不能只复制顶层 shell。后三个 meta_opt 操作 helper 和样例不是数学历史证据导入的前置门；带全原件供按需使用，不默认执行。

`trigger_eval.py` 明确是已认证 Claude Code 的 `claude -p` 选择探针，无 Codex 对等实现。它测描述触发／混淆／遗漏，不测完整能力或数学收益；本任务不需要付费跑它。`check_ready.sh` 仅打印建议，不会执行优化。MCP 实际执行仍使用本仓现有 `mcp-servers/`、`docs/REVIEWER_MCP.md` 与宿主真实工具；`reviewer_route.py` 只是配置解析器，不是模型调用。

## 原样模板和 provenance 不能冒充的能力

`meta_logging.json` 的命令假定 helper 直接位于 `$CLAUDE_PROJECT_DIR/tools/meta_opt/`；MathRSI 的真实位置是 `base/tools/meta_opt/`。直接复制到任务 settings 不会自动修好路径。`log_event.sh` 不仅写项目 `.aris/meta/events.jsonl`，还写用户 `~/.aris/meta/events.jsonl`，不能在“本地维护取证”名义下无声启用全局采集。

`corpus_write_guard.py` 使用相对 `skills|shared-references|tools|templates|plugins` 的正则黑名单，不覆盖 MathRSI 的所有 `base/...` 写法与绝对路径；自身 docstring 仍有“STRUCTURALLY unable”过强句，但同文件也承认 obfuscated writes 可绕过，Claude 技能更准确承认不是 sandbox。仅带模板不能宣称具备 OS 写隔离。开发合作场景直接用明确写域、Root检查diff与可撤回候选即可；没有当前问题就不补造一套安全平台。

`provenance.py` 实际只验证模型家族字段、记录类型及当前内容匹配等收据条件；它不验证 reviewer 是否确实完成指定审阅，也不执行受影响路径试用。CLI 没有完整 corpus integrity-check 子命令／pre-push verifier，TTL和behavioral revoke仍只是文中建议。不要因旧文中提到哈希就再加新指纹体系；版本与实际原件足以支撑本轮判断。

## 建议实现形态与消费顺序

一个有实质正文的 `mathrsi-evolve/SKILL.md`，附少数按需长 references，足以承载整个外层；不需要再造 Python 调度器。技能开头给可读执行地图，再展开这些阶段的实际输入、动作、返回和回退：

1. **恢复与取证。** 读取维护授权、原规格、既往维护结论与真实研究断点；定位原始失败／成功转折，说明当前瓶颈、历史因果和仍缺证据。缺数据不制造统计。父维护 owner 安排下一动作，子作者只返自己的 scope。
2. **分类与提案。** 对每条经验选择 workspace、plugin、base或defer。写清旧行为、新行为、实际路径、为何适用该层、接受后将怎样观察到区别；可单条开始，不要求凑清单。保护原量词、进口、共同对象和目标难度。
3. **真实候选实现。** 按已授权独占写域修改实际文件，保存可读diff和基点。必要时同时改caller/consumer。原ARIS原件仍按来源固定；数学适配不是静默改上游字节。
4. **跨模型设计审阅与修法。** 用仓内research-review完整原件＋数学composed任务，交真实来源、diff、接口和待解决问题；保留同会话证据回应。外层owner独占修法和下一轮派发。审阅失败不阻塞独立任务，不能记PASS。
5. **独立受影响路径试用。** 未参与作者从真实输入执行候选指令，交实际产物、下一消费者、错误与成本；作者不能代写结果。Root立即回收并读文件／输出，局部失败回到具体修法；连续两轮无增量则接管或缩小提案。
6. **接纳与采用。** Root按证据接纳、缩小、拒绝或待测；记录实际版本／未提交状态、保留审阅差异和未测范围。候选行为未经实际运行不能冒作整体接纳。只在本次授权范围提交／发布；原研究由协调者明确采用新版本与切换点，从旧断点续接。

这条链与 ARIS 原版的具体差别应写进技能，而不是藏在本底稿。最终日志可以是现用维护记录的连续正文：事实、diff、原始review、真实trial和Root决定均可直达，无须再造评分表或每个阶段一套空目录。下一轮首先消费本轮尚未解决的瓶颈及拒绝／重试条件，才形成真实的经验到版本演化。

## 初轮底稿检查的准确范围

执行了源码读取、依赖引用定位、文件清单与字节比较。初轮未运行 meta-optimize／meta-apply、未安装或验证 hooks、未调用付费模型、未试运行新 mathrsi-evolve，未修改 vendored snapshot、源ARIS或宿主发现别名。

## 后续获授权的原件补包已完成

父协调者随后明确授权本执行者加入上述七文件并更新快照。已从固定提交 `c485faa59a68e51c6575dea67ca57abc7a6a2b9c` 用 Git 对象读取原始 bytes／mode／blob，写入 `base/` 相同路径；保留已有来源字段，并将 `base/ARIS_SNAPSHOT.json` 更新为214文件、2,983,972字节、两宿主各32项技能。新增文件68,759字节，逐项来源见同目录 `ARIS_META_PACKAGING.json`。

`base/tests/smoke_bundle.py` 从 manifest 动态读取库存，无需修改测试代码或历史 `base/tests/evidence/`。已实际运行一次既有 smoke，`bundle-smoke/RESULT.json` 为PASS：214源文件 Git blob全部匹配，搬移副本后的9条离线调用通过，涵盖wiki／未证claim、reviewer参数解析及两宿主HTML模板。此检查不执行新meta技能、hook或受影响路径的数学维护试用；不能据此称 mathrsi-evolve 已通过行为验收。没有安装hooks、调用模型、修改源ARIS、别名或其它文档。
