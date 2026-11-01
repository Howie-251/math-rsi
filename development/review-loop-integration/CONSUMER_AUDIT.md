# 九项 MathRSI 技能的独立消费者静态回放

2026-11-01。执行者按一个没有本次开发聊天历史的接手者，读取本仓 AGENTS、`mathrsi-research`及八个子技能，然后沿四组具体输入追踪实际动作、产物、消费方和返回点。未修改技能，未调用付费模型，未启动 Goal、Lean、数学扫描或旧项目程序，也未访问 ECC 原工作区。

**结论：这四种输入都能从现有技能走到准确的下一动作，没有发现阻断执行的工作流缺口。** 技能已明确调用什么、读取什么返回、谁修以及回到哪一项原义务；并非只有技能名称或编号原则。特别是 ARIS route 的实质对话、修法、memory、复核与恢复并没有被单次 transport 调用代替。下面保留一项很小的恢复表述建议，供 Root 定向处理；不建议新加调度代码或重复旧数学。

这是 **static consumer/replay audit**。它证明的是本文所读材料下的执行路径可理解、路径与协议有实际实现，并不证明九项技能已经在新研究中全部实际运行、数学结论重新验收或通用效率改善。

## 阅读与机械检查范围

完整读取九个入口：`base/skills/mathrsi-{research,specify,survey,prepare,route-loop,prove,assemble,verify,handoff}/SKILL.md`。另读 route 的 `references/aris-review-adaptation.md`、verify 的 `references/proof-checker-inputs.md`、`docs/{ARIS_REUSE,REVIEWER_MCP}.md`、实际 ARIS `proof-writer`，定点核 `research-review`、`auto-review-loop`、`reviewer-backends`与路由器。领域层读取 Property B 主技能、literature、知识入口及下列案例对应的实际源和报告。

主要实证地图是 [REAL_PROJECT_TRANSITIONS](../workflow-redesign/REAL_PROJECT_TRANSITIONS.md)。其中 PB 前缀指 `plugins/propertyb/knowledge/archive/`；本文沿用该前缀。ECC 原交接指 `development/context/ecc-source/`，ECC 交流材料指 `PB/context/mathrsi-ecc-20261101/`。这些均在 MathRSI 内，不沿历史链接访问另一个项目。

实际执行的轻量机械检查只有：读取/列举路径；扫描九入口、其 references 和上述两份 docs 共16份文档的相对 Markdown 链接，没有发现缺失目标；运行本仓 `reviewer_route.py` 三次，只解析无 override、Grok、Antigravity 的 regular route，不联网、不调用模型。未重跑已有 MCP 协议测试；其61项离线测试证据见 [MCP_BUNDLE_REPORT](MCP_BUNDLE_REPORT.md)。

下文 `R` 表示当前 MathRSI 克隆，`W` 表示已获授权的单题工作区。`W` 的新题材料和中断断点是情景输入，不冒称本轮已创建这些文件。具体历史源均给出仓内真实路径。

## 情景一：一个新的 Property B 问题，只有题面 PDF 和旧 wiki

**输入与第一动作。** 读取 `W` 的任务约定、本轮用户题面、`W/ref/problem.pdf`、已有 `W/NEXT_SESSION.md`与 `W/research-wiki/query_pack.md`。由主 workflow 调 `mathrsi-prepare`，prepare 调 specify preliminary，先写清“有限简单 k 元超图、任意有限顶点集、边数至多 M、每边两色”的原量词和允许终点。PDF里的候选点对覆盖、锁点或平衡染色论证不能成为原题前提。

这里真正可回读的历史输入是 `PB/FORMAL_SPEC.md` 的 D1–D3、T、R1–R4，而非凭记忆写规格。该文件固定的是旧 T32，不是新题的默认参数。其原 `ar4math_propertyb.pdf` 没有随 archive 收入；如果新任务只指这份未提供的原 PDF，先用现有正式规格完成可做的恢复，并把原 PDF 标为未读取，不能声称已经逐页对齐。对新题，则必须实际取得用户所指的那份题面。这个输入依赖没有被技能隐藏成仓库自带材料。

| 调用与立即动作 | 实际输入路径 | 输出及准确范围 | 谁读取并继续 | 错误或返回分支 |
|---|---|---|---|---|
| specify preliminary：逐句反译原题，分离题面与候选解法 | `W/ref/problem.pdf`、已有规格/wiki；对照 `PB/FORMAL_SPEC.md` 的定义而不复制旧 M | `W/FORMAL_SPEC.md` 初步版；明确 k、M、全称/存在量词、终点与真实歧义 | prepare 读回量词，再启动唯一一次 survey | 只有目标含义的实质歧义才询问；不依赖它的来源定位继续 |
| survey：执行 propertyb-literature，由它持有共享 research-lit 发现 | 初步规格；`R/plugins/propertyb/skills/propertyb-literature/SKILL.md`；`PB/ref/`与任务 ref 显式清单；相关来源地图 | 领域子调用只写 `W/work/literature/propertyb/`或回内容；survey 唯一写 `W/LITERATURE.md`，记录实际查询、原文条件、勘误/反例和未读项 | survey 读回原文提取，合入报告并沿唯一 wiki owner 更新原库，再回 prepare | 外网不可用交“仅本地”；关键原文未得保留条件进口；不声称广搜完成。直接定理/反例及时回交 |
| specify final：消费已发生的调查 | 初稿、`W/LITERATURE.md`，影响目标含义的原定义/定理 | 同一规格定稿；文献进口含条件及版本/编号/页码；待证前提仍是义务 | prepare 读回后返主 dispatcher | 文献仅对受限子类成立，不能将限制塞入原题；只定向补查受影响来源 |
| route-loop：实际形成可行动路线 | 定稿、文献、失败记录及启用插件 | `W/ROUTE_REPORT.md`、真实 A–E trace/memory、已消费的探针与首批证明任务；不是原定理 PASS | 主 dispatcher 读取实际报告后调用 prove 一次 | 若调查已有直接解答，进入相应复述/验证，避免无用路线循环；若路线仍缺条件，交准确 open 义务 |

这一链实际复用 ARIS：research-lit 发现和提取，verify_papers 只核身份，research-wiki 维护原库，wiki-enrich 只补真实页，novelty-check 仅在已有候选 delta 时使用。它没有将关键词表当广搜，也没有让三个独立 writer 并写规格/文献。helper 都显式来自 `R/base/tools/`，旧任务 tools 的 resolver 优先级不会暗中换版本。

调查的实际数学消费可以直接用一般 k 历史锚点检验：从 `PB/context/propertyb-general/formal-exposition-20261021/SOURCE_MAP.md`和 RS PDF 交回 Claim A.1、Claim 2.4 证明积分的真实条件；`B_RS`是本文组合定义，不伪称原文定理。后继 route/prove 承担同一实际算法与 H 的组合，而不是把一条 citation 当成新增长定理。

## 情景二：路线中断，reviewer memory已在、模型仍pending、探针已经交付

为让恢复选择可以判定，取一个明确的回放输入：`W/ROUTE_REPORT.md`顶部记录 Round 2 / C、父 caller 为 prove 的“小点数整类义务”；Grok 的 route/session/cwd 已保存，Gemini的请求还没有确认终态，各自 memory保持原文；独核 worker 的结果已到但未消费。**这是假设的中断状态，不是说旧模型请求现在仍运行。**

已完成探针的真实内容使用 `PB/context/propertyb35-paper/round01/root/UNIQUE_SWAP_REPLAY.json`，其作者程序 `unique_swap_replay.py`也已收入；相关证明为 `PB/proofs/propertyb35/SMALL_VERTEX_SWAP.md`，旧 Grok 静态意见为 `PB/context/propertyb35-paper/round01/reviews/GROK_SMALL_SWAP_REVIEW.md`。本轮读取它们，不运行程序，不拿旧 session充当新任务 session。

**正确的第一动作是消费完成的 C 产物。** 读取 JSON五项交大小行与实际谓词，核它对应有标签交换、补色因子与完整固定边对域，把 `(50,1548,810,1320,990)`代入对应正文；核证明的重标号论证如何把代表边对覆盖到实际边对。得到的工具是“≤18点、≤36边可染”，并不关闭19–25点，也不证明整个 `m(5)≥36`。将这个范围写回原 caller/报告与原wiki，停止旧位置松弛在已闭小点数域的扩算。

接着只处理当前 pending 的真实请求：已有 completed response就进入B保存完整原文和该 reviewer 的 Memory update；仍运行按原后端可用状态接口等待/查询；失联且执行状态未知保持 unknown，继续无依赖数学，不自动重发。只有C实作与对应 evidence均已消费，且D所需前提齐了，才沿原会话给修改文件、实际 diff及JSON作定向复核。D回复再走B，最后E追加真实轮次。不能因新会话进入就启动下一轮A，不能重跑已交探针，不能将Root的判断写成reviewer自己的memory。

| 后端/参数 | 在此情景的实际动作与返回消费 |
|---|---|
| Grok 已有 session | 首轮原请求若是 `model=grok-4.7, effort=xhigh, cwd=W`，D仅调实际 `grok-reply`，传 `threadId`与 `prompt`。不重传/改变model或cwd，不因当前项目默认变了重解析 |
| Antigravity 已有 session | 同理，首轮所选 `gemini-4-argon-high/high`固定，reply仅 `threadId,prompt`。若旧session实际首轮是Gemini3.8，续接仍是3.8；要迁4就明确新首轮并带旧memory，不改旧身份 |
| Claude-review 后台 job | 用原 `jobId` 调 `review_status({jobId,waitSeconds:20})`；done后检查error/正文/终态并提取真正 `threadId`。reply重复cwd/tools/显式model；不能把jobId当threadId |
| Grok/Antigravity未知同步调用 | 当前服务没有 `*_status(jobId)`工具。查已有宿主调用/原会话证据；如果已没有可查询标识，保留unknown。不能借Claude schema构造不存在的状态调用 |
| 请求/实际身份 | 分别记录请求值与CLI报告值及来源。未知actual model/effort为null；旧Grok返回的 `grok-4.7-build`不是请求参数 `grok-4.7`的别名替填 |

**输出与消费方。** route-loop唯一writer追加真实 report/trace/memory，交回原 prove 的小点数义务；它随后继续准确剩余。当前指定review未完成则报告“所需审阅不完整”，不改成接受，也不自动暂停整个Goal。新模型调用没有在本轮发生。

此情景可按现有正文执行。唯一小的可读性建议见末节：把同步无status这一分支放到“沿原job检查”旁边，让消费者不必先沿另一文档推断服务差别。

## 情景三：局部PB24 caller审计，与全局T33完整候选分别怎样走

### 3A. 局部caller输入

精确输入是 `PB/formal/Aris4Math/ThirtyThree/TwentyFourRefinedExample.lean` 的 `propertyB_of_mixed_quad_trace`，连同它的 actual_profile、certificates和上下游说明。立即动作是按 mathrsi-verify **局部scope**读取真实签名和依赖：五个真实顶点、33边、度 `(6,6,7,7,7)`、单位共度，以及 `large`大迹前提。读取恢复公式怎样构造实际profile，真实avoid配额怎样进入返回 `PropertyB H`。局部数值 `75163/75582`只作为其中一项，不独立承担caller。

**返回产物**放本次局部验证记录/独占audit目录，列“这个分支的 actual H caller已接通；large仍是分支前提；没有替任意H构造五锁”。消费方仍是原prove的选点/分类义务。若只需具体接口疑问，可做有范围的research-review；若要求正式局部 proof-checker，就准备自足局部定理、允许依赖和caller，而不是启动全T33审计。发现large/选点无法取得则回原prove补该连接，不给主定理加假设。

再看 `PB/context/propertyb33/round02/mixed/REPORT.md`与 `twentyfour-complete/REPORT.md`，才可以将范围扩大到完整24点：32个带标签大迹、实际两坏槽、48配置和2048 padding输入被接回原H。这个时点的真实返回是 `Target33 ↔ RemainingGoal`，仍余23点。**局部verify返回prove继续23点，不能启动最终handoff。**

### 3B. 全局T33完整候选输入

精确输入改为 `PB/proofs/propertyb33/PROOF_PACKAGE.md`、T33正式规格、`PB/context/propertyb33/round02/final-assembly/INTERFACE_MAP.md`及 `PB/formal/Aris4Math/ThirtyThree/Main.lean`。立即读取实际23点六支怎样供给 `twenty_three_propertyB`，再沿 Main 的 `remaining_goal → finite_goal → Target33`消去RemainingGoal和内部结构条件。这里已有完整正文就复用，不为“实际调用assemble”重写一遍。

若它是一个尚未正式验收的新全局候选，主dispatcher调用一次verify：

1. assemble只补缺的正文连接；需要新数学就返caller建议prove。
2. 原正文为Markdown且需要正式checker，按reference在 `W/verification/full-proof/main.tex`无损转写并保留源对应，审阅同时读原Markdown、原题和依赖；不能因detector没发现TeX定理而判无需审计。
3. 实际执行本宿主proof-checker完整合同，保留它自己的source-unit、ledger、首次审阅、反例pass、修复/复审/closure与真实 `PROOF_AUDIT`；上层verify只链接这些产物。审计TeX修了正文时同步回canonical Markdown。
4. 有原任务Lean要求，指名 `Aris4Math.ThirtyThree.Main`与 `ReviewAudit33.lean`，读取真实导出/原题复述/传递公理。默认旧T32 build和conditional caller不是这个验收。

**历史已有完成证据则直接复用其真实范围**：`PB/context/propertyb33/round02/final-audit/PROOF_AUDIT.md`已经记录最终PASS、实际新Main构建与独立复述、标准三项公理，且正文两项说明已改为3292/3315与1796/844。阅读/交付请求不因此重跑Lean或全部checker；不能将本文静态读录说成我重新执行这些验收。

**返回与错误分支。** 全局verify回唯一主dispatcher，原题及约定核验齐备才建议handoff。只出现两处说明错误就定向修正文与受影响映射，不重开route；需要新选择定理则带actual caller回prove。Grok/Gemini仅静态阅读的历史范围保持原样，不替本机Lean执行，也不升级为他人复现。最终结论是 `m(5)≥34`，不串到35 Lean或36研究。

## 情景四：ECC旧43/10全域不存在性，已知完整扫描证据，应装配/验证/交接

输入是已完成 `[43,10,17]₂`不存在证明，不是新 `[45,11,17]₂`研究。先读 `development/context/ecc-source/HANDOFF_FOR_REVIEW.md`§1–6与 `MATH_RSI_DOMAIN_HANDOFF.md`§3.3、4.1–4.2；再读交流源 `PB/context/mathrsi-ecc-20261101/sources/ecc/results/NONEXISTENCE_43_10_17.md`和 `proof-contract/EVIDENCE.md`§1、§5。它们是本仓实际可用输入；历史生产脚本和1.68GB见证不因链接出现就视作本仓可执行载荷。

**立即动作是还原并消费已有闭合链，不发起新扫描**：任意目标矩阵→偶扩展→三列独立→选重量4对偶支撑→满支撑母码→实际172目录→完整偶商F→必要pair→图无边→原矩阵不存在。装配者分别检查下列真实依据的用途，而不是调用构造verifier接受不存在性：

| 既有材料/事实 | 装配/verify实际消费 | 不能替代什么 |
|---|---|---|
| E1 no[41,8,18]、E2满支撑[40,7,18]至多172类；原文版本/页码在原handoff | 任意目标归约与分类进口适用性；结合实际172合格互异代表闭目录 | 不声称本轮重新证明原作者分类；不从hull分布推出完整 |
| 每母码两套全 `2^32`，共同规范下完整集合相等 | F无遗漏；保存A/B输入映射和各自完成范围 | 保存成员都合法不证明无遗漏；不重做已有效的发现过程 |
| 全619,053,789 pair实际低权消息与绑定、严格EOF的历史重放 | 全部必要pair拒绝；图无边已排所需三角形 | `F_domains_rerun=0`不能说又做全F；不继续更强三行组合 |
| manifest、生成基、F顺序与坐标置换 | 数学对象与实际执行输入一致 | 不只比较数量、哈希、重量谱或类名 |

**assemble返回**沿用/组织一份完整正文，准确写 imports-and-computation，不加Lean要求；若没有当前任务可读的正文就写到W，引用已收录的证明链和证据读取范围，不能把历史未随包附带文件伪写成现成附件。**verify返回**已有最终审计、完整扫描/重放的真实历史范围及现包可访问性；本轮只是恢复/交付就不重复全证付费审阅或数学计算。若用户真的提出某条归约新疑问，再定向核那个义务，仍保留其它有效结果。

**handoff消费**准确原题、证明入口、verification与包需求，产出 `W/HANDOFF.md`和 `W/NEXT_SESSION.md`，说明旧题完成、E1/E2与普通软件信任、非全链Lean。本轮未复现必须明说。只有用户要求完整计算复现时，先取得并重定位原manifest所指F/输入/1.68GB流；本仓交流源缺这些载荷，就把这个复现项pending，而不访问未授权v2或自动跑原命令。没有完整复现要求就不把缺载荷变成阻止阅读交付的新门槛。

回交唯一主dispatcher后结束旧43/10题；`d₂(43,10)=16`还要引用已有距离16构造，不能仅从上界推等号。后来的45/11开放状态与本文交付隔离。这个情景的工作是消费已证闭合链，而不是重新开始ECC插件草案开发。

## MCP与ARIS源码接点核对

`base/tools/reviewer_route.py`仅解析配置的说明与实际源一致。三次本地解析结果分别为：无override得到Codex native / gpt-6-astra / xhigh；显式Grok得到grok-4.7 / xhigh；显式Antigravity得到gemini-4-argon-high / high。无项目 `.aris/reviewer.json`。所以不能只注册Gemini/Grok服务就认为任意新任务自动双模型；当前docs已经将它们写为本项目用户选定配置，其它任务仍按实际覆盖项/项目/宿主解析。

读取 `mcp-servers/{grok-exec,antigravity-exec,codex-exec}/server.py`相关schema和续接分派，Grok/Antigravity确实拒绝reply改变固定参数，Codex MCP确实通过 `config.model_reasoning_effort`施加effort。Claude-review的tools、后台job和解析差别由docs明确给出。桥接源码和来源、测试在本仓有实际路径；没有假想统一 `review()` API。当前宿主服务是否指本克隆、CLI是否登录仍需实际环境证据，本文没有拿全局已加载工具替本包做真实连通声明。

技能调用入口按宿主分开，MathRSI适配没有改ARIS快照。route-loop的composed不仅指定报告writer，还明确覆盖RR Step3/4：reviewer读原件并作有信息量证据对话，外层唯一负责修法，收到新证据再同session裁定关切；不是省略RR对话，也没有让RR另开fix owner。全证checker另有自己的修复/复审合同，局部接口咨询没有伪装成全证审计。

## 一项定向建议与无需修改的地方

**非阻断的恢复用语建议。** 在 `mathrsi-route-loop/SKILL.md`“恢复先读断点”段的“仍运行就沿原job检查”之后，直接加一句：

> Claude-review异步job用review_status；Grok/Antigravity为同步调用，没有job status工具。宿主调用失联且没有可查询标识时保留unknown，继续独立动作，不按Claude schema轮询或自动重发；见REVIEWER_MCP。

这是对现有规则的就近澄清，不增加新门槛。reference已经明确unknown不重发，docs也给了各后端schema，因此本轮不能把这项用语分散记作缺失执行能力或虚构blocker。Root可用该一句关闭接手者在情景二的最后一处查找成本，不需要另写客户端、状态机或付费探测。

未发现需要改动的地方：prepare内部调查唯一调度；specify preliminary/final职责；Property B唯一research-lit发现；完整原文进口到caller的消费；route C完成结果回收与逐reviewer memory；prove局部verify返回；全局checker与TeX适配/回写；当前实际Lean模块而非默认旧build；ECC已足够必要门处收束；handoff分开历史接受、现包载荷、当次复现与展示范围。这些具体接点已可执行，保持即可。
