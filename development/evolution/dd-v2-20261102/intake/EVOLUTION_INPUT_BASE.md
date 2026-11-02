# 给 mathrsi-meta-evolve 的 base v1 演化输入

2026-11-03。本文是维护技能的真实输入，不是v2补丁、路线执行记录或接受决定。先使`mathrsi-meta-evolve`可独立执行，再由它消费证据、分类、修改现有base v1、取得真实review与独立受影响路径试用，最后决定接受版本。保留现有五个子工作流、ARIS适配与插件接口；本文作者未修改稳定skills，未恢复DD、Property B或ECC，未执行历史Lean、模型、solver或BFS。

## 可消费的原件与阅读边界

现有九份`base/skills/mathrsi-*/SKILL.md`均已全文读取，具体逐项判断见[EXISTING_SKILLS_AUDIT.md](EXISTING_SKILLS_AUDIT.md)。它们有输入、委托、回流、原件审阅、唯一dispatcher与恢复机制，不能以“都是薄SOP”为由重写一套主流程。

DD原件当前来源根为`/Users/rfy_naiveai/Desktop/aris4math/dd_research_full_handoff`。下文`DD/`代表该只读根，`MathRSI/`代表本仓。原件清单见[SOURCE_INVENTORY.json](SOURCE_INVENTORY.json)，原件审计见[formal-review/SOURCE_AUDIT.md](formal-review/SOURCE_AUDIT.md)，6116项精确读取等级见[READ_LEDGER.tsv](formal-review/READ_LEDGER.tsv)。2222份Lean只全部扫描声明/import（15364条语法级声明），关键证明与生成器/模板另按实际读法标记；没有把全扫描算全证明阅读。提取的157条真实模型返回正文已全部读完，含5个ERROR与READY连通性，只有154个不同正文，不是157次有效独立数学审阅。25份命名disposition全文、33份重复正文的独有处置尾部也全文读过。

`DD/research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md`共2682行/412289字节，连续1–1895实际全文已读，1896–2682未读。按最新指令停止扩库，未读余文不是本轮技能开发的前置条件。[逐段映射](formal-review/USER_CORRECTION_TIMELINE.md)区分用户逐字引语、作者“用户明确”转述、非新用户指令的执行记录。源包缺失或省略的原件仍按库存注明，不能声称已拥有。新DD插件应随仓保留源wiki及支撑原件，运行时新题wiki分离；本输入中的绝对路径只定位当前历史来源，不能成为可携带技能的运行依赖。

## 人类纠正：按时间与适用范围消费

下面均定位上述comments原文件，短引保留原话。后来的范围/恢复覆盖早先局部策略，但不授权今天重启旧数学任务。

| 原文件行段 | 原话与触发行为 | 演化时应保留的行为及边界 |
|---|---|---|
| 1209–1217 | “把尝试过的再并上与目标图的距离一并放到research wiki里面” | 具体方法终态及时回原wiki，保量词、失败域、目标差距、重启前提。148条混合记录/35家族不能称148方法；ordinary坏对、NB缺项、容量障碍与控制器量分开。 |
| 1226–1248 | “先做针对性的构造直觉研究，再集中攻关”；“允许在既有授权内增加样本、延长运行或深入同一机制” | 先给可推翻预测、让实际反馈改变生成规则。旧短窗口不是永久禁令；也不因剩预算就补满同样搜索。足够明确的新问题可续同一机制，普通工作不反复索权。 |
| 1256–1262 | “不要深陷…只提升几百点对” | 局部评分改善不等完整目标进展；取消未执行2520枚举记0次，转向有结构依据的新表示。不要自动升级为所有局部工具都无价值。 |
| 1300–1308 | “不必要过度验证之前的…尽可能的多产出结果…验证适量的就行” | 同族复用已验基图/未变代码/原证据；新步核新增degree、全部CURRENT基图覆盖及保边归纳。新机制/参数首次必要独核，具体矛盾再扩大检查。不降低完整目标标准，不逐图自动再全源BFS/模型/Lean。 |
| 1363–1373 | “比较有可能解出来的任务…其次…还没有深入试过…然后…难点攻关” | 未尝试不是自动最高优先；先结构预测再构造。该时点的最多两持续线/资源快照不固化成所有MathRSI任务的caps。 |
| 1391–1399 | “只要是在那个表上还没有close的，都可以…尝试构造” | 原27格变历史起始池，不能一直用旧摘要否掉新授权；旧D2/n61并未自动恢复。精确目标/比较基线变更进同一工作区恢复入口。 |
| 1495–1518 | “继续同一个Goal”；“若已应用…直接续接，不重复导入”；“完成最少必要同步后立即研究” | 历史导入说明不是每次重建计划/wiki的理由。每小时是反馈节点，不强迫换题/新结果；人类问状态不等resume。保留旧暂停记录，后明确resume覆盖等待步骤。 |
| 1810–1824 | “推广两种已成功…并在读取交接文档后立即开展实际研究” | 成功泛型的适用条件必须检查，不能把一般保边扩张定理误当任意源都有合格pins；跨q/维数推广仍未证。文档同步不是实际构造。 |

早期comments406–417已明确“不盲目重试”不等禁止有依据的新计算；544–561明确自然证明推进优先、Lean后置、明确UNKNOWN由Root消费即可，不为状态再开模型；169–173与1219–1225强调本地HTML路径不是可转交专家的自含交付。这些都有现有技能承接点，不宜新造全局政策。

## 候选改变：由技能判定并形成实际diff

下面分级不是先验接受。已正确实现的原则优先补具体实例/独立试用；只有实际缺口才改行为。DD过去由ARIS完成，不冒称MathRSI v1实跑。

### B1：明确固定Lean见证的直接验证入口（base，首要行为候选）

现有位置：`base/skills/mathrsi-verify/SKILL.md:20–39,81–91,125–139`；verify的主图将完整正文送proof-checker，再于汇合之后接Lean。§2对“完整候选仍进入checker”有泛化读法，§4虽允许直接组织Lean，却没有完整的独立Lean入口/返回示例。上游`base/skills/skills-codex/lean-formalize/SKILL.md`已有standalone Lean不自动要求paper-audit合同。保留自然语言完整证明正式审计路径，只澄清用户仅要固定形式目标时的真实分支。

原件：`DD/formal/DegreeDiameter/Portfolio/F4Graph3840Exact.lean`及`F4Graph3840DecoderInterface.lean`、实际audit；comments1872–1895。成果是3840阶、最大度≤20、实际Walk中恰径3，不含ASCII parser、恰20正则、全部参数通用构造或全球纪录。源实例C的有效静态审阅也不自动涵盖后续clone。

建议diff：verify进入时先消费目标/材料/用户所需结论。形式目标直接运行或复用lean-formalize，取得actual export、展开定义、目标模块build、独立import/传递公理、已指定reviewer状态后返回原caller；若Lean暴露新数学缺口回prove，API问题留形式化内部。若同时要求可读证明正式audit，另按原checker合同执行，不互相递归。research主入口只需对该返回分支同步，避免大改九技能。

独立试用输入片段：
```text
只验收固定F4公式图的Lean出口，不要求论文/TeX审计；历史构建与原题审计作为输入，禁止重跑旧Lean。
读取原定义、Exact、audit和当前verify；返回该历史证据能支持的准确声明、缺少的证据及下一动作。
```
合格观察：独立使用者实际读取导出/定义/audit，给出准确Walk/degree目标，区分“本次静态消费历史构建”与“本次执行Lean”；不制造TeX、canonical PROOF_AUDIT、fresh PASS或全题完成。这个受限试用验证路径选择/证据消费，不声称测过新Lean执行能力。若新增实际Lean执行是新技能验收另有授权范围，必须真实跑其受影响小目标并保命令/结果，不能以本片段替代。

### B2：按实际改变选择复核范围（base示例；已有原则，避免重复改造）

现有位置：verify§1、§4；route-loop§C/D；prove已有实际caller/成本/停止恢复段；handoff§复现。原话1300–1308及comments1711–1789说明“观察timeout”与“重启solver”不同；旧证据允许复用不等跳过新对象完整覆盖。

原件：`DD/formal/DegreeDiameter/Portfolio/SingleExtension.lean`证明保边与pins radius r推出新图D≤max(D,r+1)；`DD/reviews/ddp/redei15_20261027.raw.json`与comments1300–1308、1810–1824的实际生产链。42399→42402每步使用各自current graph；独立代表验至42377并不等每个后来图都全源独核。raw写85=4+23+57的账目错一项，实际4+23+58，不能复制reviewer数字。

建议：增加可执行例，写清“什么变了→哪个旧证明可复用→必须新增核什么→结果回哪个原义务”。禁止把DD特定取舍变所有任务独核豁免，也不新增每图全栈审计。

独立试用：给已验G、保全部旧边、S覆盖CURRENT G全部点、旧邻点余度/新degree证据及一个只针对早先基图失败的候选。使用者应装配扩张结论；指出earlier失败不自动约束changed-base，但只有新base真实改变相关条件才能重启。若新步coverage不全，保持该图未验收；不启动旧全BFS。

### B3：模型意见逐断言裁定并真实修法（base具体实例，现有合同不删）

现有位置：`mathrsi-route-loop/SKILL.md:70–117`、verify:83–87已有原回应、同会话证据澄清、实际修法、memory与父消费。缺一次完整独立A→C→D→caller试用，不缺“允许反驳模型”的原则。

原件：`DD/reviews/ddp/m2_coset_tower_review_raw_20261026.json`、`m2_coset_tower_review_correction_raw_20261026.json`；`h9_quadric_rule_20261027.raw.json`、`h9_quadric_42343_final.raw.json`。前者漏两步H jumps后撤回，又漏target-head分支；q41路径0→247→516→207→822→2只有5步，另一820→205→750→955→1037→914补16targets，最终实际覆盖式HW3H∪KW1H∪HW1K。后者把旧core充分证书失败误作675batch不可能，最终撤回；core41356与986extras职责须分开，不能用core代替全旧图。

建议：原回复连同正确部分、错误断言、路径反例、新公式/代码和真实scope同仓保留，route-loop实例逐次消费，不把整封retraction改成PASS。若仅补实例，不改现有调度语义。

独立试用：给两份真实M2回复、实际路径/源码，要求先定位哪项覆盖声明失效，再提交修正推导并回父。静态fixture试用只能证明识别/修订路径；若测试真正同会话review续接，必须发新授权的review调用并保真实raw/session，不能复活旧付费会话或假造回应。外层版本接受仍需另一个未参与写作的受影响路径使用者。

### B4：目标、比较、证据的不同终点（base具体实例 + DD插件技术内容）

现有位置：specify原量词/进口、prepare恢复、assemble实际输入、verify证据、handoff状态已有原则。comments1519–1540、1801–1809、1834–1862给可核误差：合法104/4与保存主表改善103/3、最新全球比较pending不相同；F7合法却被公开表支配，数学合法性不撤销；旧51418–51457后来被88452支配也不抹历史基线。

建议：DD插件提供一份真实spec/return示范，base仅补通用消费点。新上界/下界、maxdegree≤d/正则、D≤D/恰径、公式图/字面文件/解析器、比较表日期/公开采用分开。不要统一变成每任务必须填的字段表。

独立试用：给`F4Graph3840Exact`的形式出口、旧表条目和一个较新公开支配记录。使用者应准确保留形式结果，把当前纪录问题留为待查/已支配，不能凭旧2783称全球SOTA，不能用模型SUCCESS补公开来源。

### B5：从生成器、证明模板到实际出口的闭包（DD插件为主；base只补handoff/assemble示例）

原件：`DD/formal/DegreeDiameter/Portfolio/FullNeighborhoodClones.lean`、相应F4/F3/F9/OppositeGQ inputs/exact；`DD/formal/STATUS.md`与`DegreeDiameter/N62TripleActualBlock.lean`冲突，actual import/source/audit显示该局部接口已完成，不能继续抄“未完成”，更不能顺势称全部n62闭合。细节与成本见SOURCE_AUDIT的27家族地图。

建议：插件随仓保留源wiki、真正证明/程序/失败例/reviews/复现入口，按真实目标给阅读闭包。大生成shard按生成器→共用模板→导出依赖→实例数据绑定组织，不要求普通读者人工逐个数字；全声明扫描和实例抽读必须分开登记。clone定理需要固定source、load与recipe索引equivalence；它保旧图bounded-Walk双向等价，不能修好坏source，generic并不要求中心独立/映射单射。接口规则可复用，具体几何/字段/labels进插件。

独立试用：让未写作者从指定clone Exact追出实际旧source、recipe/newlabel、load≤k和主定理；指出哪些ASCII/labeltransport只外部检查、哪些进入Lean。给过时STATUS时应对照实际import与audit，而不是只选最新日期。交付仅包含真实闭包与必要恢复资料，不要求整2222文件每个全文读完，不把缺件称已携带。

## 不进入base的内容和暂缓内容

DD有限域GF9(w²=−1)、controller行路由、q8打包、GQ几何/clone负载定理、具体图counterexample进入DD插件；其原件随插件提供，不把技术细节硬编码入通用调度。某图当前n/degree/比较状态、哪条旧Goal暂停、作者本机资源/cgroup、模型会话身份是历史工作区状态，不升为base默认。跨q/全部source存在合格pins、全体n61排除、全库Lean原题验收、全球最优/公开采用缺证的部分defer；仍保留有条件工具及重启用途。没有MathRSI v1真实运行日志，不设人工“至少5事件”门槛，不伪造历史event。

ARIS原版meta-optimize/ meta-apply已随base自含，精确来源与闭包见[ARIS_META_ADAPTATION.md](ARIS_META_ADAPTATION.md)、[ARIS_META_PACKAGING.json](ARIS_META_PACKAGING.json)。两宿主授权存在实际矛盾：Claude optimize只提案交apply，Codex optimize Step6可自身落地。新的数学外层技能必须明确本次授权/改动范围、真实patch、crossmodel review、**修改后独立受影响路径实际试用再接受版本**；不能静默照抄任一边，或用landing后的链接测试冒新版本行为验收。upstream文件保持原样。

## 供新技能独立执行的任务包

给执行者的最小自然语言任务如下；应由Root在技能可调用后发出，本文作者不先代做：

```text
读取mathrsi-meta-evolve，针对现有base v1消费本EVOLUTION_INPUT_BASE.md、九技能审视及其所引必要原件。
先判断B1是否确为行为歧义，其余哪些已有正确实现、仅需实例/试用；不要把全部候选机械做成补丁。
将接受候选归base/plugin/workspace/defer，给原执行→源证据→具体diff→验收的对应。
在独占开发目录形成可审阅真实补丁；与指定跨模型讨论真实差异并修；保留原回应。
由未参与写作的使用者从真实输入执行受影响路径，记录实际读源、调用、产物消费、返回及失败修法。
禁止恢复旧Goal、旧模型/solver/Lean批次；使用上述受限fixture时如实报告其静态范围，不能冒实际编译。
试用发现问题回修并补受影响检查；通过后才给准确接受范围及版本落地记录。
未改动路径复用既有证据；不另造主workflow、全库重读门或每项全栈审计。
```

此输入没有替代新技能的实际执行。当前接受状态：全部为待判定候选；稳定base无本作者改动；独立行为试用未执行。
