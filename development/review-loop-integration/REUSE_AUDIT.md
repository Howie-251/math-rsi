# ARIS review-loop 的实质复用核查

核查日期：2026-11-01。范围为本仓 `AGENTS.md`、Codex 版 `auto-review-loop`、`research-review`、相关共享契约、真实 helper 源码与当前 `mathrsi-route-loop`。只做文件审查；未调用 reviewer、执行数学探针、恢复旧研究或修改技能。下列行号对应本次读取版本，章节名是后续修订时的稳定定位。

## 判断

用户的担心有实际依据。现稿保留了 ARIS 的原件读取、独立审阅、实际修复、计算结果消费和有新证据的针对性复核，不能说完全抛弃了 ARIS；但是将原版定位成“ML 完整循环”，又只明确列出取证、路由、first/reply、trace，确实削弱了对**完整改进回路**的复用。Reviewer Memory、逐轮累计记录、锁定恢复会话、终轮归档等原版能力没有同等明确的执行要求。“已完整复制”不能补足实际主流程没有调用的能力。

不必为了证明复用而套两层拥有轮次和终点的循环。最小修法是把 `mathrsi-route-loop` 明确写成 **ARIS auto-review-loop 的数学路线适配**：保留其初始化、审阅、解析关切、reviewer memory、证据回应、实际修复、等待/收回、逐轮记录、再审与终止交接这一整条动作链；由 route-loop 唯一持有本次轮次。`research-review` 提供完整的单次深审与同会话实质对话，不被缩减成 transport，也不额外开启另一个无界共识回路。数学适配改变评议对象、动作和结束含义，不删除恢复、记忆、实作与交接。

## 逐项对照

原版位置均在 [Codex auto-review-loop](../../base/skills/skills-codex/auto-review-loop/SKILL.md)（下称 ARL）、[Codex research-review](../../base/skills/skills-codex/research-review/SKILL.md)（RR）；现实现为 [mathrsi-route-loop](../../base/skills/mathrsi-route-loop/SKILL.md)（MR）。

| 原版功能及真实位置 | MR 现实现 | 应保留并数学适配的实质 | 真正不适用或不宜照搬的部分 |
| --- | --- | --- | --- |
| ARL `Initialization`、`State Persistence`，L63–90、112–135：恢复同一 run、累计文档、待完成任务、route/session/cwd，逐轮持久化 | §1 L31–37 要读旧报告、原始回复、真实任务状态；L69 要留 session。未明确保存/恢复 round、固定路由、cwd、下一动作及轮内中断位置 | 在唯一报告中写一个简短“当前断点”，每轮更新；恢复先收回已有产物，按已保存 reviewer route/session 继续；在修复中断时继续修复，不能机械跳到下轮审阅 | 不需要新 JSON 状态机；旧版“24小时后删状态并重开”不适合长期数学研究，可保留原件后据任务状态判断，不能仅凭时间清除有效研究 |
| ARL `Reviewer Memory and Debate`、`Phase B.5`，L34–61、222–251：所有难度都保留 reviewer 自己的持续怀疑、未解决项、反复模式，每次调用回传 | MR 保留 raw response，但没有 reviewer-owned memory、回传或终轮更新要求 | 给 reviewer 全部相关旧 memory 与准确变更路径，要求 `Memory update`；原文追加，不以作者“已解决”替代 reviewer 自己的判断。可放报告的独立 memory 节，不必强增文件 | “Score 回退”可改为关切重现/结论逆转；不需要为了记忆计算 hash |
| ARL `Phase A` L139–211；RR `Step 1–2` L30–82：读原件、自主挑战、具体最小修法 | MR §2–3 已有实际输入、进口、待证条件、失效原件和具体数学问题，保留程度较好 | 完整保留正文/代码/原始结果自主读取，区分原题、作者候选与审阅结论，保留最小可执行补证要求 | NeurIPS/ICML 角色、投稿贡献评分不必用于固定数学路线；不能因此省去审阅的 substantive prompt |
| RR `Step 3` L84–111：同 session 实质对话，回应、针对追问、请求可执行 deliverable | MR L24、69、91 允许续接，但“单slot”容易被理解为单个回复 | 明确 slot 是一项有范围的审阅任务，可包含初审、证据回应、必要追问和修订复核；请求准确新引理、反例、最小区分动作等实质产物 | 不要求每次审阅都讨论全文叙述或投稿故事；不必为了对话延长循环 |
| ARL `Phase B` L213–220：完整原始回复与行动项提取 | MR L69–71 保存原文并逐条处理 | 每个关切保留原话或准确引用、影响义务、最小行动、处理结果；完整原文在 trace，累计报告写可独立理解的摘要与链接 | 不需强抽取 1–10 分；保留 reviewer 实际给出的分数时也不能用它证明数学命题 |
| ARL `Phase B.6 Debate` L282–315；RR L102–103、145：以证据回应争议，再由原 reviewer 表态 | MR L53、71 可带证据驳回，L91 可复核；未明确保存 rebuttal/ruling 与双方不同结论 | 对关键争议保留作者回应、证据和原 reviewer ruling；区分“reviewer 接受”与“作者依据证据不同意”。若仍有实质分歧，交接剩余分歧，不能改写 raw response 为 PASS | 不把 reviewer 的同意设为数学真理否决权；无需每个小意见都启动固定三项辩论仪式 |
| ARL `Phase C Implement Fixes` L357–370、Key Rules L468；RR `Step 3` | MR §4、§5 已要求实际推导/反例/代码修复/必要复算，是现稿最实质的保留 | 让“意见→修法→实际修改→新证据”在同一轮可追踪，修正文稿、推导、程序和实际 caller，不能只产生下一轮建议 | GPU/模型训练/总要加指标不适用时换成真实数学工作；计算过贵可以记录并换足够的办法，不能悄悄跳过仍必要的证明义务 |
| ARL `Phase D Wait for Results` L372–377：监控、收回、检查真实结果 | MR L33、83–85 已覆盖任务回收和实际结果检查 | 保存真实任务/session标识、输入域、退出码、当前输出、需独核的具体属性，成熟结果立即消费，等待时做其它独立修复 | W&B、NaN/训练平台检查仅适用于确有训练的任务；数学计算要检查自己的运行/覆盖/精确性，不能只换名为 training-check |
| ARL `Phase E Document Round` L379–425：评议、完整回复、行动、结果、继续/停止，每轮更新 notes/findings | MR §6 给出最终报告内容，§1 恢复依赖旧报告；没有明确每轮落盘与每轮同等结构 | 每个实质轮次追加“问题/原审阅→回应→实际修复→原始结果→改变的判断→剩余/next”，并在轮末更新断点；不要只在子流程结束才写漂亮总结 | 不用造多份同内容 `findings.md`、`AUTO_REVIEW.md`、`ROUTE_REPORT.md`；一份报告可承担累计记录 |
| ARL L203、473–514：Round 2+ 读实际改动和新结果，再评未解关切 | MR §5 L91 明确保留针对性复核，但“一次复核通常就交接”可能弱化连续实质改进 | 以剩余问题与新增证据决定再审；修复后再审，仍不满足路线交接条件则在预算内继续实作，不把“已复核一次”当完成 | 不重复审未变材料；不为凑四轮或得到好评反复付费调用 |
| ARL `Stop-Evaluation Gate` L253–280、`Termination` L433–451 | MR 默认最多3个实质轮次，预算尽交准确缺口且不暂停总 Goal，边界合理 | 定义数学路线的停止：已有足以执行的路线/原输入连接、已完成当前必需审阅、关键异议有处理结果、未证条件和首批任务清楚；否则明确预算收卷/路线否定/审阅不完整，交上游判断 | 6分且 ready/almost 不能当定理真值。保留“路线可交接”的判断即可；不能把 max rounds 写成题解完成 |
| ARL `Append-Only Acquittal Receipt` L92–108、413–417：历史接受不能替新轮过关 | MR 有 scope诚实，但无本次接受与历史接受绑定的明确记录 | 在本次报告记录对应 round、确切 trace、范围、实际剩余与当前决定；旧审阅只复用未改变且同范围内容，不自动跨路线/新命题迁移 | 不必照搬 `ACQUITTAL_LOG.jsonl` 和评分收据；若省略，必须保留这项语义，不能省去“本次什么获得什么认可”的证据 |
| RR `Step 5` L119–134：逐轮总结、结论/claims矩阵、TODO/成本，显式 `— composed:` | MR 唯一作者/父消费已有，但示例未传 `— composed:`，没有明确接入 RR 现有组合接口 | 调用 RR 数学适配任务时显式传 `— composed: <绝对报告路径>`，由父写共享报告；返回独有内容、raw trace、剩余。结论矩阵转为“哪些证据支持哪一条条件结论、还缺什么” | 论文 outline 未讨论就不生成；不能把实验结果自动升级成已证明的 universal claim |
| ARL `Termination` L437–445：完成状态、最终方法、notes、剩余阻碍及交接 | MR §6 已有原题/瓶颈/首批任务/父调度，保留较好；缺本次 loop 状态/最后 reviewer memory 的终轮落盘要求 | 交接前写清本次完成的是路线子范围，最后一轮也归档；保留可复用方法、否定结果和重启条件，父读取后实际启动一次后续 | 不机械调用 ML `result-to-claim` 生成 proof claim；可用其结果约束主张思想，数学 claim升级继续服从 proof-checker |
| ARL L427–431；RR Step6；`review-tracing`：每次初审/续接/争议/独立攻击均保存实际 prompt/raw/identity/scope | MR L51、69、103 规定 trace，方向正确；依赖引用而没有本技能具体调用/消费例 | 保留真实 helper 执行和确切 call-level trace 路径；错误是错误；trace是恢复、解决分歧和决定再审的输入，不只是末尾链接 | 不必新建 trace平台；不需要 hash；未要求每轮新 fresh reviewer时复用同 session |
| ARL `hard/nightmare` L205–211：有需要时另开独立原件攻击 | MR 未明确该能力，但已要求原件读取 | 用户/风险义务确实要求独立攻击时保留新会话，重复scope并单独记录；其结论挂到具体义务 | 不必所有路线同时普通+hard+nightmare，也不把三个标签当质量等级评分 |
| ARL optional human checkpoint、Feishu、renderHTML、输出协议 | MR 没强套这些副作用 | 已有用户要求/配置才做对应动作；报告语言、已有历史、输出所有权应保留；HTML按交付需要做 | 不因发现Feishu配置就未经消息授权发送；路线阶段无需默认HTML、15件以下不造manifest；无需新增通知/定时器平台 |

## 最小实质修改方案

只改 MathRSI 自己的技能与复用说明，不动 ARIS 快照字节，不写新 Python 调度器。应修改的是操作合同，而非把现有“slot”一词换个名字。

**第一处：改开头的复用定义。** 将 MR L10 的“独立循环、只借鉴动作顺序”改成明确“以 ARIS auto-review-loop 的完整改进回路为基础作数学适配”，逐项说保留初始化/记忆/实作/收回/逐轮记录/复核/交接。避免用“不嵌套”承担主要解释；只说明轮次归 route-loop 唯一拥有，避免父子各运行四轮。RR的Step1–6按数学上下文执行和消费，明确其slot含必要同会话对话，而非只调用一次后就算复用完成。

**第二处：在恢复节补实际断点。** 不需 `REVIEW_STATE.json`；报告顶部保留本次 invocation/范围、当前round与轮内动作、预算余量、已解析route（请求model/effort）、实际session/cwd、最近call trace、待收回任务ID/路径、下一条命令或精确义务。每次审阅发出后先记录真实session与完成状态，轮末更新；恢复先读断点、memory、上一轮原文、新结果。会话固定项改变须另开并记录过渡，不能因为项目配置改了就默换。恢复不是无条件 `round+1`：上次修复未完先完成修复。

**第三处：补 reviewer memory 与逐轮记录的硬动作。** 在报告独立 memory 节追加 reviewer的 `Memory update` 原文（或已有独立文件，沿用即可），包含旧疑点是否消除、新疑点与未解项；每次给 reviewer完整相关memory。终轮也写。对每轮落盘评议摘要、raw trace、争议回应、真实修复、结果、判断变化、剩余和next。报告只留摘要与链接，不复制一份全trace。出现逆转先比较原始回复定位判据变化，再决定是否需新审。

**第四处：把实作与再审链写完整。** 保留现有§4的实质工作，增加“每项重要关切都有实现/证明/反例或明确未处理原因；承诺不能充当修复”的记录。按新产物重审相应关切；若仍有阻止交接的关键问题，在预算内继续修复和复核。模型错时可用证据驳回，但分别记“作者结论”与“reviewer ruling”。不为获取认可反复问，也不把指定一次复核当完成条件。

**第五处：直接用 RR 的组合交付。** 传 `— composed: /task/ROUTE_REPORT.md`；调用参数再写清“数学路线适配、当前具体义务、所需独有返回、由route-loop拥有轮次”。RR 返回逐轮意见/回应、证据到条件结论的关系、优先实际任务/成本、原session和trace；父作者即时合入并继续实作。`— composed:`解决重复文件和唯一写者，不是取消 RR 内容。若用户单独调用原RR，仍按原技能 standalone；不能因为某个报告存在就推断 composed。

**第六处：在终止节补本次状态与消费。** 明确区别“路线交接就绪”“预算收卷仍有阻碍”“该候选被否定”“指定review不完整”，写最后memory和逐轮结论。把本次决定绑定确切call trace与本次实际证据，历史接受保留原scope。父调用者读新报告与首批任务后继续一次；现有父子调度边界保留。完整证明验收留给verify，但不能用这个分工省掉本阶段路线质量审阅。

## 可直接复用的 helper 和准确边界

以下是接口说明，未在本次执行。真实来源为 [reviewer_route.py](../../base/tools/reviewer_route.py)、[save_trace.sh](../../base/tools/save_trace.sh)、[review_gate.py](../../base/tools/review_gate.py)、[review-tracing](../../base/skills/skills-codex/shared-references/review-tracing.md) 与 [output-composition](../../base/skills/skills-codex/shared-references/output-composition.md)。各 shell 调用重新显式设置当前克隆 `base` 的绝对路径，从**任务工作区**执行，不 fallback 全局ARIS。

### 路由解析与恢复

```bash
export ARIS_REPO="/path/to/MathRSI/base"
python3 "$ARIS_REPO/tools/reviewer_route.py" \
  --project "$PWD" --host codex --tier regular --reviewer grok
```

已存在的CLI参数为 `--project`、`--host {codex,claude-code,copilot}`、`--tier {deep,regular}`、`--reviewer`、`--model`、`--effort`、`--default-reviewer`。上例仅示意本次显式选Grok；未指名时不强加 `--reviewer`。auto-review-loop原常规审阅是 regular，research-review原深审是 deep；按所调用slot说明tier，不能无声更换用户要求。JSON返回 backend、host、source、model、effort、transport、fresh_tool、continuation_tool。解析不调用模型，也不检查工具可用。首次保存此返回及后续实际session；恢复使用保存值，不再次套新默认。Native continuation在当前宿主实际可能是 `collaboration.followup_task`，不能将返回的协议字符串 `send_input` 当已加载工具。

### 每次初审/续接/争议的trace

```bash
export ARIS_REPO="/path/to/MathRSI/base"
bash "$ARIS_REPO/tools/save_trace.sh" \
  --skill mathrsi-route-loop --purpose round-1-initial-review \
  --backend grok --tool "$ACTUAL_TOOL" --executor codex \
  --executor-model "$ACTUAL_EXECUTOR_MODEL" \
  --requested-reviewer-model "$REQUESTED_MODEL" \
  --reported-reviewer-model "$REPORTED_MODEL" \
  --effort "$ACTUAL_EFFORT" --thread-id "$REVIEW_SESSION_ID" \
  --prompt-file "$PROMPT_FILE" --response-file "$RESPONSE_FILE" \
  --status ok --verdict "$RAW_VERDICT" \
  --review-completed --review-scope-complete
```

变量来自真实调用；未知reported身份/effort就省掉对应参数，不能用request值冒填。只有完成和覆盖均核实才传两个布尔flag；失败传 `--status error`，不传完成/积极flag，原始失败照存。`--verdict`接受原始文本，不要求ready/almost；本helper不从分数或词语推断正面。明确达到**本次数学路线审阅的正面结论**时才另加 `--review-positive`，其accepted字段只表示这次scope内的审阅接受，不是定理证明。若要避免把未判定路线标为接受，可以不传该flag，正文仍如实记录意见。

该脚本在当前cwd写 `.aris/traces/<skill>/<date>_runNN/`，每次产生request、response、meta，首次还有run.meta；并向 `.aris/meta/events.jsonl`追加。stderr返回 `Trace saved: <具体call前缀>`，报告应记录**确切call文件**，不能只链接目录。脚本没有 `--run-id`、`--cwd` 或 `--out-dir` 参数；不要虚构。当前源码会复用已有同日同skill的首个含run.meta目录，不能把其目录名视为不同route-loop invocation的唯一绑定；在已有报告断点和purpose写明本次范围/轮次，引用精确call即可，不必为此另造平台。若helper不可用按原forensic契约直接保存四类文件与事件；应修包或准确报缺失，不静默跳过trace。

### `review_gate.py` 的可用部分与不适用部分

CLI强制 `--score <float>`、`--verdict {ready,almost,not ready}`，还有backend、executor/reviewer model、完成/覆盖/status等flag。它实现原版评分停止策略，**不是一般数学路线判定器**。MR没有采集该评分/词汇时不要编造6分或ready来满足CLI。身份家族计算函数 `derive_model_family(model)`已经被save_trace复用；所需身份/完成/范围记录通过原trace helper即可取得，无需重写第二套。

若某个实验型路线明确选择完整原ARL并保留其评分，则可按原合同执行gate，但其stop只结束改进子循环，不证明数学命题。数学route-loop用上文的自然语言交接判断；不需新 `route_gate.py`。

### 组合交付和展示

RR真实支持 `— composed: <canonical-report-path>`，并规定 `— standalone`覆盖。明确给父报告路径即可复用，不需要写dispatcher。可选展示复用 `base/skills/skills-codex/render-html/scripts/render_html.py`，CLI为输入文件加 `--template`、`--out`、`--title`、`--state`、`--offline`等；原ARL示例里的 `/render-html ... --no-review --state ...`是技能调用合同，其中 `--no-review`并非Python CLI参数，不能把整段原样搬成Python命令。没有展示需求时不强制生成；不为路线阶段复制ML claims或paper outline。

## 验收这次修改应看什么

用一份已有历史材料演示离线消费即可：恢复某轮未解决关切，带上原reviewer memory与session记录，定位已经完成的实际修复和新结果，把对应复核结论及准确未解项交给父。此演示只验证流程材料能被消费，不需付费再审、不重跑Property B/ECC数学。技能文本里应能逐项找到上述动作的拥有者、产物和下一消费点；能从一轮结尾实际恢复下一动作，才算补齐，不以目录完整、链接检查或“已复用ARIS”声明代替。
