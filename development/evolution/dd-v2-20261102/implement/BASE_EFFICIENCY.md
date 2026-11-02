# B2–B4：现有 base 的返回消费修订

本次作者先读取已集成的 [mathrsi-meta-evolve](../../../../base/skills/mathrsi-meta-evolve/SKILL.md)，恢复 [EVOLUTION](../EVOLUTION.md) 的 B2–B4 范围，再修改现有五个技能。Root 是维护协调者；本记录供其及时消费，不设额外无历史全流程试跑或固定审阅层。没有修改源研究、原 ARIS、verify／research／assemble、DD 插件或原题规格。

DD 是历史依据，不是 MathRSI v1 解题实验。以下“消费”指本轮作者按候选指令处理已有输入后作出的具体决定；没有恢复历史队列、发出新数学作业或重新认证历史结论。Root 的本轮采用决定仍回主记录。

## 原执行方式与实际 diff

v1 已有原目标保真、增量回 survey、必要门不等于完成、共同对象、参数改变后重建必要域和未变证据复用。没有复制这些原则另造流程。补充的是它们被具体输入触发时，caller 应返回和执行的动作：

| 现有位置 | 原来已具备 | 本次原位增加的消费 |
| --- | --- | --- |
| [specify §3](../../../../base/skills/mathrsi-specify/SKILL.md) | 文献不能擅自换题；区分直接定理和近邻 | 区分竞争目标／用户固定目标；构造族合法代入参加比较；新门槛连到受影响候选，再回父流程改队列 |
| [prepare §3](../../../../base/skills/mathrsi-prepare/SKILL.md) | 读回实际基线和进口、保持用户题目 | 返回被支配任务、仍有价值任务及首项替代输入，父 caller 实际撤换竞争队列 |
| [survey §5](../../../../base/skills/mathrsi-survey/SKILL.md) | 原文纪录、代入数与新推论分开 | 对竞争判断核已知族的适用参数／组合条件；返回“旧比较→新保证→候选影响→新输入／缺源”，不止追加数值 |
| [route-loop Phase C](../../../../base/skills/mathrsi-route-loop/SKILL.md) | 原输入／共同对象、精确谓词、真实修法 | 修改对象后分别判断正结论的假设继承与负证据的限制失效；局部充分 rank 失败回原共同覆盖；必要门 PASS 继续共同赋值 |
| [route-loop Phase D](../../../../base/skills/mathrsi-route-loop/SKILL.md) | 增量 survey 回同一义务 | 新基线到达后撤掉只服务于旧竞争门槛的待派任务，消费新源条件；固定目标继续，在途结果与预算保留 |
| [prove §2、§4](../../../../base/skills/mathrsi-prove/SKILL.md) | 必要门／构造区分；新参数重建受影响域 | 从 rank 回实际像并及共同输入；基线回调改实际行动；源／生成规则改变后逐结论继承或重开，冻结定理所指的源数据 |

[实际 diff](BASE_EFFICIENCY.diff) 为上述五个 SKILL，共18条新增文本行（九段正文及空行）；不改原步骤编号和 ARIS 调用。没有在 base 放 DD 子空间公式、pair 分类证明、参数预算或 solver 默认值；长链统一指向本轮 [evidence-and-transfer](../../../../base/skills/mathrsi-meta-evolve/references/evidence-and-transfer.md)，其领域实质由 DD 插件承接。

## 按候选内容处理的具体输入与决定

下面输入保留决定所需原始量，便于 Root 直接使用同一案例核查；输出是本轮明确选择的后继动作，不是新搜索结果。

### 1. P33 更正实际改变竞争队列

输入：

```text
purpose = improve_public_bound
local = (degree=65, D=3, n=161150, valid=true)
old_public = 160750
primary = p140 / §4.3 / Table5: W(7), found=33, upper=43
known_source = (n=160000, degree=64); spread_size=50
pending = continue old O22 record campaign
new_search_authorized = false
```

消费决定：33是已发表构造下界，43是理论上界，不能互换。按已核组合条件代入得到161650，旧候选 margin 为−500。停止把 O22 竞争队列继续视为改善公开界；合法构造、原核验／形式化证据保留。下一动作改成读取 P33 与复制规则的实际条件，供 route owner 选择新输入；本次不启动新搜索。70／77度同样得到169900／181450，分别超过本地166650／条件175692。

准确原件：`A/research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md` L9–17、19–36、44–50。与 [效率输入案例1](../intake/EVOLUTION_INPUT_EFFICIENCY.md)复用同一链。若本轮指令只写“提高比较意识”，还让 pending 原样继续，便未满足新消费行为。

### 2. 同一新基线不能替换用户固定任务

输入沿用案例1，但 `purpose = construct fixed (degree=65,D=3,n=161150)`，用户要求完整对象与验证，无纪录终点。

消费决定：继续固定构造／交付义务，不把 n 改成161651；修正“公开改进”措辞，保留合法性与比较状态分别输出。调查只更新知识，不取得换题权限。specify 的原有固定目标规则继续有效，本次补的是与竞争队列决策的分流。

F7提供另一已读原件：`A/.../f7_c60_d35/PUBLIC_COMPARISON.md` L9–25、33–38。20580点35正则D3图合法，但 Delorme q=32 给35875保证；这只否定其纪录资格，不否定图。没有单列边表不妨碍已知族的合法代入参加比较，35875也不称全球最优。

### 3. 正向继承必须绑定定理所指的源

输入：

```text
old_theorem = frozen full-neighborhood clones, source G, D>=3, no isolates
new_object = retain old edges; each clone connects exactly to saved N_G(center)
variant = subsequent clones read current(center), including earlier clones
```

消费决定：第一种生成规则可继续使用已有保距定理，但仍须供给当前 G 的假设和独立负载条件；不重跑未改的源结论。variant 已不等于定理对象，不能复用原 caller；先修为冻结源，或把已增点图明确作为新源重新满足条件。若下一层复制 first-clone／hub，源必须是实际 G1，不能仍读取旧 GQ center。没有把任意改图都变成重跑全部源点。

原件部分核读：`A/formal/DegreeDiameter/Portfolio/FullNeighborhoodClones.lean` L8–25图定义、L51–67旧点路径继承；声明索引 L85–89、L127–156定位保距假设与负载。本轮未重读整份 Lean 证明体或重新构建；完整条件及 G1 修正复用 [对象改变链](../../../../base/skills/mathrsi-meta-evolve/references/evidence-and-transfer.md#3-链二对象变了哪些旧证明保留哪些旧失败已越界)。

### 4. 负记录的限制解除，不等于新构造成功

输入：

```text
old_rule = Exoo72 fixed source, delete adjacent u,v, retain others, A-B matching only
old_NO = every unique old cross pair must be directly matched; contradiction
new_rule = arbitrary boundary matching, allows A-A and B-B
deleted = [0,45]; matching = [[51,59],[62,71],[15,18],[56,58]]
repaired_route = [51,59,36,18]
remaining_failed_pair = [51,62]
```

消费决定：旧 must-directly-match 证明的 A–B 限制已解除，不能用它排新域；实际同侧路径确实修复旧 cross 点对。原 cross-only 排除仍保留。新 matching 仍漏另一点对，所以不是正构造；下一动作是消费新规则的完整边界路线条件，合并旧24与新81类的严格排除，停止准确的固定源／删相邻两点／保留其余边／max5操作，任意70点控制器继续不在结论域。

原件：`A/.../f4_c72_nucleus_C4/controller70_pair_surgery/PROOF.md` L77–111、117–130；`controller70_general_matching/PROOF.md` L26–64、87–111、113–135。本轮全文读了两份原证明，未运行其搜索／BFS。旧结果没有被覆写，新失败也没有外推。

### 5. 局部满秩失败，回到原共同覆盖

输入：

```text
source = fixed published d15 / order15552 / D4 source
original local tool = one rank4 word for each controller pair
missing_from_tool = 3648 pairs
new_interface = same starting x, actual words, common reference, image/coset union
results = 33216 inherited full-rank pairs; 3648 coset-covered pairs
groups = 91 used; 6 first-reference failures retained
```

消费决定：不再把每对必须有一条满秩 word 当成原D4必要条件。保留33216对的原证据，针对3648对读取同一源 x 的路线像与公共参考代数，检查量词及贡献是否可共同覆盖；91组证书只支持其已给的参考选择，六次失败不抹去。下一义务是将共同覆盖接真实图路径，不能因各路线 rank 不满就排原构造，也不从 x=0样本外推所有 x。

原件全文读：`A/.../retained_edge_transfer/published_d15_15552_D4_source_gate/GLOBAL_COSET4_NOTE.md` L9–29、37–54、56–84；其 L86–143明确本批未做 Lean 与新 clone 形式化。本轮没有重跑程序或重核全部7371份覆盖见证，复用历史算术范围。具体子空间公式未进 base。

### 6. 必要门 PASS 继续共同义务；确为必要的门 NO 可停止

输入A：F4 unique-route 必要门全部通过，但没有共同 chart；global projective 57600组失败，逐边选择后才有 SAT实例。

消费决定：门 PASS 的返回是存活输入和共同 chart 义务。当前局部门不得写“图已找到”，也不能把全局参数族的失败外推到逐边选择域。route-loop／prove 继续原共同赋值；具体模型与方向由插件提供。

输入B：同一固定 pure-linear controller 族已有证明，在 x=0 时全部短路像并的大小不足，故每对至少一条 rank3 路线在该族确为必要；全域枚举无选择覆盖全部所需对。

消费决定：接受这个已证必要门的准确全域拒绝，停止对应族，不误读新 B4 为“rank 失败永远不能排除”。不要求继续巨大图 BFS。两种方向来自 [数学提炼§4](../intake/DD_MATHEMATICAL_EXTRACTION.md#4-mechanism-iii--prove-a-shared-parameter-failure-then-release-exactly-that-sharing)及 [覆盖／门链](../../../../base/skills/mathrsi-meta-evolve/references/evidence-and-transfer.md#5-链四必要门unknown精确证书与实际构造分别消费)，本轮复用已读证据，未重新枚举57600组。

## 本次实际核查与限制

2026-11-03 实际运行：

- `git diff --check`：exit0；五技能 diff 18新增行，没有替换原有步骤。
- 五个技能的 frontmatter、全部新增参考的本地文件和 Markdown section 锚点逐项解析通过；技能源无作者 Mac 路径。
- 少量 Python 整数运算重新得到65／70／77度基线161650／169900／181450、margin −500／−3250／−5758，以及 q32 的35875；只核比较算术，不认证文献／几何条件。
- `python3 tools/check_links.py` 当时检查75文档、1174本地目标，7缺链，全部为另一作者正在写的 DD 插件入口。五个本域技能及其新增参考无缺链。最终全仓结果由 Root 在插件交回后收束。

本次是候选指令的作者实际消费和针对改动的结构／算术核查，不称无历史独立测试、完整数学新研究、外部检索或跨模型终审。未运行旧 solver／大型搜索／BFS／Lean，没有新性能实验，不能由这份记录宣称通用效率提升。

`A` 为本轮只读源交接根；具体原件将由 DD 插件 owner 按原档案关系随仓保存。本记录不把作者绝对目录写为技能依赖。未新增测试框架或通用状态 schema。已提交给 Root 的成熟 diff 可在当前维护中直接使用；DD 插件正式入口完成后，可由 Root 选择是否把这些开发来源链接替换为稳定领域入口，不阻塞本轮基于现有参考的消费。

## Gemini 集成问题1：把 DD 接入真实派发段

后续 [Gemini 集成审阅](../reviews/GEMINI_V2_INTEGRATION.md)问题1指出：首批 B2–B4 虽已写明 DD 行为例，但 prepare/survey 的实际领域派发仍只识别 Property B，prove只具体点名 Property B；docs契约不足以确保走进DD。接受这一真实缺口，在原三个技能中修复，不改主干或DD公式：

- prepare§3的实际调用块和领域段增加DD入口与transfer§4，传 `(d,D,n)`、最大度／正则、固定／竞争目标及原caller，要求survey走DD分支。
- survey§2增加启用DD分支，实际读取领域入口／transfer公开比较段／调用地图，使用随仓原wiki和public_baseline_audit为本地种子。survey持有唯一research-lit与LITERATURE writer；DD返回领域关键词、条件和合法族代入，不再平行重广搜。既有同范围结果补差异，新的外部查漏按真正缺口执行。
- prove§2增加construction／obstruction／transfer的明确选择和可执行调用材料：实际源、标签、改边规则、进口、独占写域及原caller；接回图定义／degree／全部pair连接，或必要门、完整域、证书和准确失败。必要PASS与严格NO按原范围消费，未闭条件回原义务，插件不启动第二条同级链。

按修改后文字静态处理“启用DD、竞争型(d65,D3)、O22旧比较、已核P33来源”的入口：prepare交当前参数与比较目的→survey先读DD种子、共享原research-lit结果→LITERATURE记录合法代入保证与受影响候选→返回原caller改队列。固定目标则不换规格。对固定4192 clone义务，prove选construction并给source/centers/labels/旧D证据；实际图属性或source条件需核时选obstruction对应scope，回同一prove；没有重开旧搜索。此次仅静态入口消费，未新做外部调查或图生成。

实际检查：`python3 tools/check_links.py`检查90文档、1351本地目标，0缺失；`git diff --check` exit0。本次新增base→插件链接均使用 `../../../plugins/...` 并实际解析通过。此前7处插件在途缺链现已补齐，不能将先前失败收据改写为当时成功。实际diff附件已更新包含本次接线修复。主入口／docs由Root同步，不在本作者写域。
