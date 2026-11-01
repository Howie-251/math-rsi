# 一般k下界研究进度

**2026-10-21 13／14短试已停止：** 条件增锁引理修复M9544、v972、d=e81的特定三锁分支；M9564、v972在已选三个81度单位锁条件下，第四度81…128的288型／1134计数向量全过，但v813／最小度152等仍缺。13／14均无新完整下界，不继续扩表。13当前9539→统一9542／C.2 9564；14为19602→19606／19647。引理三项数学义务已获Grok有效静态讨论（未审288型数值），红图仍只到12；[恢复及条件工具](locks-vs-uniform-20261021/STATUS.md)。以下旧v972停止点已由该局部补充细化。

**2026-10-21 锁点实例／共同基线：** k=12、M=4660完整691429局部型全过，给m(12)≥4661的计算机辅助证明候选；独立完整参数域、31个Fraction边界型及全部3348个零／一锁型已核，两／三锁未第二次全算、未Lean。新Grok只审一般准则迁移，不是最终M4660整表审阅。k13 M9544仅完整通过至v971，v972/d=e81留缺口，无新完整下界。共同基线k5…12为32,64,128,263,538,1085,2245,4633，增益3,1,2,3,4,27,30,28；k10/11旧GL增益+42/+62保留历史。全部k≥12蓝色统一增长Lean与verified状态保持。详见[共同恢复入口](locks-vs-uniform-20261021/STATUS.md)。

## 当前：完整主定理C及五项包络扩展至全部k≥12（2026-10-21）

同一B_RS及Δ=floor(√B_RS/[8(1+ln k)])不变；所有k≥12均有Δ≥2，任意有限简单k元原超图的边数≤B_RS+Δ即得每条边两色，故m(k)≥B_RS+Δ+1。完整解析扩展、7单位／37义务fresh审计和本次Lean实际核验均已完成：[本次总报告](bridge-12-16-20261021/REPORT.md)、[解析证明](bridge-12-16-20261021/ANALYTIC_EXTENSION.md)、[PROOF_AUDIT](bridge-12-16-20261021/PROOF_AUDIT.md)、[Lean报告](bridge-12-16-20261021/lean/REPORT.md)、[VERIFICATION](bridge-12-16-20261021/lean/VERIFICATION.json)。审计为PASS_WITH_DECLARED_IMPORTS、same-family/provisional，Lean指定Twelve构建2576jobs exit0，独立ReviewAuditGeneralGrowth12原题复述exit0，传递公理仅标准三项；均为主执行者本机实际记录。

五项明确参考包络现对全部k≥12等于B_RS+1，当前定理严格超过至少2；比较D仍为纸面证明，E的纸面范围保持k≥256，二者均未Lean。新Grok最终审阅已有效end_turn（grok-4.7-build/xhigh），全文静态读取Twelve、原题复述与日志，认可且无实质问题；未执行Lean、未重审旧核心全部证明体，见[REVIEW_DISPOSITION](bridge-12-16-20261021/REVIEW_DISPOSITION.md)。本次不调用Gemini，旧17起点的双模型有效终审只作历史证据。当前HTML证据放在 `.aris/traces/render-html/2026-10-21_general-bound-k12/`，不沿用旧数量／检查。本次未新建Goal，旧35Lean／36研究继续暂停，v2隔离。以下各阶段17、32起点与公式数均为当时历史快照。

## 比较定理D起点收紧至17（2026-10-21）

用户追问17…31是否有参考界尚未超过，核查发现D.2原证明在17即成立：`2^(17/2)>16·17`与单调性给出同一q、v估计。D.3已有全部k≥17，故五项包络在整个范围为B_RS+1，增长定理C严格突破其包络。规范、文献表和HTML/图同步；32仅保留数值样点。独立核对及具体Grok/Gemini回应在 `bound-figure-20261021/GR_CUTOFF_*`。未扩大主定理C的Lean范围（本已≥17），没有形式化D/E，E的≥256不变；以下32比较记录保留历史。

## 后续形式化：完整增长主定理C已构建通过

2026-10-21，全部k≥17的主定理C已接成端到端Lean，指定主构建和独立原命题/最大预算/七项公理审计均通过。实时形式化与交付状态见[增长阶段PROGRESS](../propertyb-general-lean-growth/PROGRESS.md)，证据见[VERIFICATION](../propertyb-general-lean-growth/VERIFICATION.json)。本文以下保留原纸面Goal完成时的历史记录；其中“无新Lean”仅描述当时范围。比较D/E仍为纸面证明，旧35/36继续暂停。

2026-10-21，round02。数学证明与指定终审已完成，最终展示／交付已完成，Goal工具已实际返回status=complete。规范FORMAL_SPEC_PROPERTYB_GENERAL.md；旧36与35Lean暂停，无新Lean或v2工作。

## round02 当前状态：数学与指定终审已完成

- **主定理：** 对每个整数k≥17，任意有限简单k元超图只要边数≤B_RS+Δ即可二染，Δ=floor(sqrt(B_RS)/(8(1+log k)))；因此m(k)≥B_RS+Δ+1。主claim `propertyb-general-growing-integer-gain` 已按proof-checker登记verified，纸面证明，无新Lean。
- **比较范围：** 明确定义的五项L_ref在全部k≥32等于B_RS+1；Goal的完整比较尾K={k≥256}另含指定零锁必要数据松弛对每个M>B_RS不通过。松弛点不是实际H，结论不覆盖所有潜在Grill法。
- **正式依据：** 四份规范源已通过核心、增量及合并审计，`round02/formal-audit/COMBINED_AUDIT.*`为PASS；核心18源单位／78义务、清洁比较源均已核。same-family审计仍按provisional记录，主claim的正式纸面验收及有效跨家族证据分别保存。
- **指定终审：** Grok/Gemini核心及比较均有效完成，处置在`round02/reviews/CORE_DISPOSITION.md`、`BASELINE_DISPOSITION.md`。Grok比较依据同次调用原生completed终稿，MCP envelope及其stopReason缺失，保持缺失；未新请求或付费重试。两家为静态审阅，没有运行计算。
- **恢复与交付：** 阅读`PROPERTY_B_GENERAL_BOUND.html`，人工交接`HANDOFF_PROPERTYB_GENERAL.md`，方法手册`research-wiki/PROPERTY_B_GENERAL_METHOD_SYNTHESIS.md`。最终展示／交付已完成，Goal工具已实际返回status=complete。

已复用的方法链是：保留同一实际超图与共同坏对对象，经最小顶点商约化接到真实单交图；以公共点／无公共点的经典线性交族团界削减γ，再把同一个严格RS参数见证转为统一增长的整数预算。这是覆盖全部原始对象域的解析证明，不是样例归纳。

2026-10-21：数学、指定终审、离线HTML和人工交接均已完成交付；Goal工具已实际返回status=complete。最终验收入口为context/propertyb-general/round02/COMPLETION_AUDIT.md；最终HTML含532条内嵌公式，离线桌面／手机检查PASS，已用Microsoft Edge打开。旧36与35Lean暂停、v2隔离保持原状。

## 调度与较早推进快照（历史，以下不覆盖当前状态）

2026-10-21用户已清除旧调度条目并建立新一般Goal，get_goal实查active。当前round02已启动，旧36及35 Lean仍暂停。以下为启动前调度历史：首轮已授权研究完成收卷；当时新工具Goal尚未登记。完整objective超过工具4000字符限额，改为规范文件引用后又因同线程仍有paused旧36 Goal被拒。用户选择在本线程继续，并自行在界面清除旧调度条目、保留全部暂停文件；最新要求先准备启动prompt，由用户手动Goal。本次实查旧36仍paused。可粘贴文本：`START_GOAL_PROPERTYB_GENERAL.txt`，完整规范仍为`GOAL_PROPERTYB_GENERAL_BOUND.md`。不把旧题标为完成来腾位置。

## round02 较早推进快照（历史）

- 完整核心稿：`proofs/propertyb-general/CORE_THEOREM.md`。同一RS算法的FKG端项、精确有向单交积分、最小顶点商、实际m≤M与原染色结论已写全；Sol独立对照原稿审计未发现问题。
- 整数比较：`proofs/propertyb-general/UNIFORM_INTEGER_GAIN.md`，全k≥17定义非空有限B_RS并给至少+1。
- 更强候选：`proofs/propertyb-general/CLIQUE_REFINEMENT.md`。团有公共点／无公共点二分，把团上界从约k√M压至约√M；完整解析增益为floor(√B_RS/[8(1+log k)])，无需逐k扫描。独立稿与核查在`round02/clique-refinement/`；尚未正式验收或升级wiki claim。
- fresh ARIS proof-checker `/root/general_full_proof_check`已完成上述三源全文审计：PASS，18/18源单位、78项数学义务全部核销，未修改源稿；审计目录`round02/formal-audit/`。同家族审阅仍provisional，不替代跨家族终审或文献比较。
- Grok与Gemini4核心A/B/C均有效返回，认可全k≥17增益；原包、正文和主代理处置在`round02/reviews/`。Grok仅要求展开J下界来源的一句话，已改，公式不变；正式审计已定向确认。新比较终审正在续接：Grok线程a7072949-9c27-49c9-90ca-ea16d7ece030原生04:00:27起的turn仍live（用户暂停/恢复后旧cell1430丢失，回收代理观察原进程，未付费重试）；Gemini同线程续接exec cell1437。
- 强基线比较：`round02/baseline-comparison/REPORT.md`已给k≥256、每个M>B_RS的Grill零锁／明确必要数据松弛不通过证明；`SOURCES_FINAL.md`给k≥32时GR覆盖／平衡包络≤2^k。独立审计`round02/baseline-independent/REPORT.md`认可上述精确范围，无blocking；必要度数据不是实际超图，未宣称所有潜在锁方法均被压住。最终来源查漏在`round02/final-literature/`推进。
- 单卷候选`PROPERTY_B_GENERAL_BOUND.html`已内联四份完整源，531处公式离线内嵌，桌面／手机检查通过；fresh展示保真审阅在途。新完整比较源`proofs/propertyb-general/BASELINE_COMPARISON.md`也已通过正式增量及合并审计`round02/formal-audit/COMBINED_AUDIT.md`，same-family/provisional。最终有界文献查漏`round02/final-literature/REPORT.md`未发现具体更强适用新界，实际阅读范围另列。旧36／35Lean保持暂停，不触碰v2。

本轮的真正剩余：正式审计／跨模型问题处置；准确强基线对比；冻结新规格与主定理；全文HTML保真；最终wiki/交接。不得把相对指定RS的推导自动写成所有适用文献已经比较完毕。

## 首轮数学状态（历史）

以下为首轮快照；当前具体候选与审计状态见上方round02。没有新增最终验收的一般下界。

|义务|当前状态|负责人／入口|
|---|---|---|
|RS／CK／Grill及后续一般基线|首轮文献报告已完成；RS已有FKG与精确积分，不能把二者当新改进。完整适用基线包络仍待比较|round01/literature/BASELINE.md|
|实际单交图的统一γ削减|root已写Gram团界＋Turán＋最小反例点数约化候选，并读RS原证明；完整接口及新下界验收待核|round01/root/SINGLE_INTERSECTION_TURAN.md|
|统一整数增益|Sol已保存解析候选：k≥32、M≥2^k时，指定旧RS判据严格成立可推出新cap判据在M+1严格成立；待root全文核算及基线比较，same-family/provisional|round01/comparison/UNIFORM_GAIN.md|
|无锁／一锁参数化包络|已保存一锁解析候选与数值诊断；浮点／Decimal结果未作为严格数值证书；停止扩大扫描|round01/discrete/REPORT.md|
|一般初态及随机横截修复|已保存实际可染单中心阻塞族与修复路线边界；不是原命题反例，不据此否定其他修复法|round01/repair/REPORT.md|
|跨家族审阅|已发出针对新γ候选的两份请求并保存prompt；收卷时未见RAW最终回应，旧exec cell1382无法恢复。状态为未收回有效结果，不计通过，不自动重发|round01/reviews/|

启动已恢复完整Goal、最新项目记忆、一般综合、原讨论范围／来源、失败经验、query_pack及旧暂停入口。其余数学源按上述分工定向核查，复用上一轮117组库存，不重放旧103190型。

发现自动query_pack仍将旧36写成执行方向，后续修正其RESEARCH_BRIEF源段并用规范helper重建，旧历史不删除。

## 新Goal恢复时的优先义务（历史，已由上方核销）

1. 核查`UNIFORM_GAIN.md`的全参数解析证明，并把单交图上界和RS失败概率接到任意原始超图。首轮候选尚未完成正式审计。
2. 证明候选适用预算区间非空，明确优化判据到整数B(k)的定义及严格性；与相同k范围内的有效强基线比较。相对指定RS判据的+1不自动等于超越所有适用结果。
3. 查找本轮两模型调用是否留下可恢复的完整结果；只记录实际有效范围。需要新增审阅时，给出这两份明确义务和完整候选，避免重做旧五次方向讨论。
4. 完整链成立后再形成正式定理、proof-checker审计和单卷HTML。当前没有新增已验收的一般m(k)下界，不恢复旧36或35 Lean。
