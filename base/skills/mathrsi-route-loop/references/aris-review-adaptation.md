# ARIS数学适配的执行材料

这是 `mathrsi-route-loop` 的操作补充。先执行主技能的完整准备、A–E和终轮交接；本页给恢复、memory、真实调用、trace和wiki的具体写法，不另起一套循环。ARIS原件保持不变。实际MCP依赖与成功条件按 [REVIEWER_MCP](../../../../docs/REVIEWER_MCP.md)，宿主技能按 [auto-review-loop](../../skills-codex/auto-review-loop/SKILL.md) 与 [research-review](../../skills-codex/research-review/SKILL.md) 完整读取。

## 一份报告如何接住中断

以下是假定任务路径的格式示例，不能当成实际完成记录。写入时换成本次真实值，只有必要字段，没有固定JSON要求：

```text
当前断点
execution: math-adapted-auto-review；scope: joint-majorant-route；父: prove/obligation-J。
Round 2 / Phase C：已收Grok复核，修正文稿尚未接回caller；本次还余一次实作。
Grok route: 由首次真实解析结果填写；请求model/effort: 实际值；cwd: /task。
session: 真实返回ID；最近call: .aris/traces/.../004-round-2-recheck.meta.json。
实际reported身份/effort与来源: 真实返回；review完成/读取范围: 真实检查。
在途任务: 独核job实际ID，输入/task/work/joint/input，输出/task/work/joint/check。
下一动作: 查同job状态；结束后读取report并核对坏对计数，将caller连接补进ROUTE_REPORT。
open义务: J.2共同选点；wiki: research-wiki/ideas/joint-majorant.md。
```

如果恢复时job已完成，就收回它并续写C；不再做一份相同独核，不直接Round3审阅。若只有一个未知是否已分发成功的MCP请求，保留请求时间、工具返回和已有job/session，按后端可用状态接口查询；没有可查询标识时记录“结果未知”，继续独立工作，不能把失联当未发出而自动重试。只有明确新授权或已查明原请求未执行，才可新调度。

此处的状态查询按实际后端区分：Claude后台接口有jobId/status；Grok与Antigravity是同步调用，没有同名轮询工具，先收宿主保存的原调用结果或查可用原生记录，无法确认就保留未知。不能发一条reply来“查询是否完成”，因为reply本身就是新的付费推理。模型session与宿主在途调用句柄分别保存。

“本次已完成”只关闭当前路线scope。新范围不能拿旧round正面意见作为自己的审核结果；未改变的同一义务可以引用已有证据，并明确复用范围。当前断点与每次call分别记录身份，不能继承上次review-completed或reported model。

## Reviewer memory与累计轮次

报告可用 `Reviewer Memory / Grok / Round N`、`Reviewer Memory / Gemini / Round N` 分节。每项贴该reviewer返回的原文更新和确切call链接，保留旧更新。下次传给同一reviewer：

```text
## Your Reviewer Memory (persistent across rounds)
[该reviewer前几轮相关Memory update原文；不要混入另一reviewer或Root结论]

本次修订文件: /task/work/joint/DERIVATION.md
真实diff: /task/work/joint/round2.diff
原始结果: /task/work/joint/RESULT.json
请自己读取；检查旧疑点是否真正解决而非移到未证假设。
请分别说明已解决、仍开、新发现，给最低后继证据，并给Memory update。
```

轮次正文追加“本轮问题—reviewer意见—Root证据回应—实际动作—原始结果—判断—剩余/next”。例如reviewer认为两次规范化不相容，Root给出的正确回应应是一个保持第一次对象不变的证明或严格反例；写“将考虑统一表示”不算修复。复核后记录reviewer是否接受，以及Root独立依据的结论；仍有分歧保留双方原话与证据。不要求整理成评分表。

## 首次解析路由、真实调用、返回消费

从任务工作区执行本副本helper；以下路径是可替换占位。只在新会话解析，恢复用已保存route：

```bash
export ARIS_REPO="/path/to/MathRSI/base"
python3 "$ARIS_REPO/tools/reviewer_route.py" \
  --project "$PWD" --host codex --tier regular --reviewer grok
```

只有本次确实指定Grok才传上例的 `--reviewer grok`；也支持 `--model`、`--effort`，只传真实override。JSON解析器返回配置与协议名，不会调用模型、不检查登录。`regular`对应原auto-review的常规审阅；明确安排RR深审则用 `deep`。选好后发现宿主实际工具并执行，不能凭 `fresh_tool` 字符串宣称已加载。Native Codex要按其授权和fresh-context合同；Grok/Antigravity首轮传prompt、包含材料的cwd、已解析model/effort，续接只传原threadId与新prompt。其它路由按自身真实schema，不混传参数。

research-review的调用任务必须有 `— composed: /task/ROUTE_REPORT.md`，并把当前A或D、具体问题、已有memory与返回要求写明。composed只决定报告归属，**不能代替对RR Step3/4的明确数学适配**。调用者另传：Step3的ML实验设计、论文outline、投稿claims等产物换为准确引理/反例/必要条件和最低可执行补证动作；Step4原本的双方共识、实验方案与论文叙事收敛在本scope内替换为以下返回条件。

Phase A先收集原件、实际审阅，必要时同session追问具体证据；一旦关切、最低修法和下一实作清单足够准确就返回caller。Phase D带真实修复、diff和新原始结果沿原session复核，裁定旧关切已解决/仍开/新增问题并给条件后返回。两者可有多次有信息量的证据对话，不设“只能一个reply”；但都不另行调用proof-writer、计算探针、修法或下一轮，也不等双方同意或论文叙事完成。若reviewer直接给一个准确证明或反例就如实返回，不能用职责分工拒收有价值的数学内容。

caller读取原始意见、最低修法和memory，执行C，再用D对新成果复核；是否继续修、换线或交接由外层唯一决定。这样实际执行RR收集/对话/记录的实质职责，且没有两个fix owner。单独调用原RR仍按原文件执行，本适配不改它的默认合同。

每次返回先检查完成信号和必读文件覆盖，保存session、原始response和实际身份来源；真正的任务ID可能是异步job，不能把jobId当最终threadId。在途状态先写断点，最终返回后才填完成。静态文件review未执行命令，就在报告注明。所需能力不足或付费调用失败时记录真实错误，不自动重试、不冒作PASS、不降成主代理自审；其它无依赖的动作继续。

## 用现有save_trace保留每次调用

```bash
export ARIS_REPO="/path/to/MathRSI/base"
bash "$ARIS_REPO/tools/save_trace.sh" \
  --skill mathrsi-route-loop --purpose scope-joint-round-2-recheck \
  --backend "$BACKEND" --tool "$ACTUAL_TOOL" --executor codex \
  --executor-model "$ACTUAL_EXECUTOR_MODEL" \
  --requested-reviewer-model "$REQUESTED_MODEL" \
  --reported-reviewer-model "$REPORTED_MODEL" \
  --effort "$ACTUAL_EFFORT" --thread-id "$SESSION_ID" \
  --prompt-file "$PROMPT_FILE" --response-file "$RESPONSE_FILE" \
  --status ok --verdict "$RAW_VERDICT" \
  --review-completed --review-scope-complete
```

变量来自本次真实返回；未知reported身份或effort就省该参数，不用请求值补填。只有实际完成/覆盖才传对应flag。失败用 `--status error` 且不传成功flag；原文照存。`--verdict`保留真实文本，helper不会从ready/分数推断positive；只有本次数学路线scope确有正面结论且所需审阅完成，才另传 `--review-positive`。即使trace为跨家族accepted，也只表示该scope的模型审阅，不能替代证明。

脚本从当前cwd写 `.aris/traces/<skill>/<date>_runNN/` 和 `.aris/meta/events.jsonl`，stderr给具体call前缀。记录确切request/response/meta，不只链接目录。现脚本没有 `--run-id`、`--cwd`、`--out-dir`，且同日同skill可复用已有目录；本次scope/round在purpose和报告断点绑定，不能猜目录等于唯一研究run。helper不可用按review-tracing的forensic合同直接写run.meta、request、完整response、call.meta及事件，并准确报缺失；不fallback另一份ARIS。

`review_gate.py`要求数值score与 `ready/almost/not ready`，实现原版ML停止策略；本适配不编造分数来调用它。身份家族计算已由save_trace复用。路线能交接的实质判断由主技能E执行，原始reviewer判断与Root判断分别保留，不新增route_gate或平台。

## 终轮wiki与下一义务

先读任务现有wiki和 [research-wiki](../../skills-codex/research-wiki/SKILL.md)。已有方法/idea只补本轮新条件、结果、失败与重启条件，留证据到报告/原始产物；不要用helper覆盖已有丰富正文。确实缺少idea节点时，可用真实接口创建未判定路线节点：

```bash
export ARIS_REPO="/path/to/MathRSI/base"
python3 "$ARIS_REPO/tools/research_wiki.py" upsert_idea research-wiki/ \
  --slug joint-majorant --title "共同对象的联合上界路线" \
  --stage active --outcome pending \
  --thesis "准确写本轮候选及实际下游用途" \
  --risks "准确写尚未证明的共同选点条件；证据见ROUTE_REPORT.md"
```

默认skip-on-exist不会改旧页；已有页先读取并保留正文，按原wiki技能更新需要的短字段与材料。候选仍pending不表示没有完成探针；数学探针可以在该页链接原始结果与输入域。已有合法experiment节点就复用；没有可据证据给出的实验verdict时，不为写wiki把默认 `no` 当实际判决。图关系只用 `add_edge`，不手改自动Connections或edges.jsonl。

```bash
export ARIS_REPO="/path/to/MathRSI/base"
python3 "$ARIS_REPO/tools/research_wiki.py" rebuild_index research-wiki/
python3 "$ARIS_REPO/tools/research_wiki.py" rebuild_query_pack research-wiki/
python3 "$ARIS_REPO/tools/research_wiki.py" log research-wiki/ \
  "joint-majorant路线更新：记录准确新增条件、证据路径和仍开义务"
```

这些是实际写入动作，不是仅在报告推荐wiki更新；执行后读回页面和导航，报告给真实路径及新增内容。没有新增可复用知识就明确“本轮无新增，沿用这些既有入口”，不制造空页面。canonical proof claim继续按proof-checker真实audit产生/升级，路线意见或探针不能升级为verified。

最终返回例如“open J.2 → research-wiki/ideas/joint-majorant.md → prove作者在/task/work/joint-caller/证明共同选点并接原caller，已有DERIVATION可用”。父调用者读报告和完整产物，消费后执行一次下游。若同一任务来自prove重判，next是回该prove义务；若需要补文献，survey返回后仍回这条义务，不重跑整个prepare。终轮的memory、实际wiki更新与明确下一动作都先落盘再交接。
