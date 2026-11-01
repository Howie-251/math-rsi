# Research Wiki Query Pack

_Auto-generated. Do not edit._

## Project Direction
**Problem**

对每个整数k≥12，B_RS(k)为精确RS积分判据接受的全部正整数预算的最大元。设Δ(k)=floor(√B_RS(k)/(8(1+ln k)))，则Δ≥2，任意有限简单k元超图在边数≤B_RS+Δ时都存在每条边含两色的Bool染色，故m(k)≥B_RS+Δ+1。原对象没有点数、点对覆盖、度数、共度或线性附加条件。当前[正式规格](FORMAL_SPEC_PROPERTYB_GENERAL.md)。

**Constraints**

旧36自然语言研究和35Lean继续暂停，不操作独立编码理论项目aris4math_v2。模型审阅与实际Lean核验分别报告：本次Grok最终grok-4.7-build/xhigh/end_turn有效，静态全文读取Twelve、原题复述与日志，无实质问题；未执行Lean、未重审旧核心全部证明体。Gemini本轮不调用，旧17范围Gemini记录不算新增12范围审阅。展示完成以本次 `.aris/traces/render-html/2026-10-21_general-bound-k12/` 实际记录为准。

**Direction**

**2026-10-29 六元+3最新：** m(6)≥67的完整计算机辅助证明已装配，27–44全部实际分支及独立精确复算齐备；最后34点87型、35点306型均已接到原染色。Grok4.7-build/xhigh与Gemini4Argon/high整卷终审均有效接受（静态阅读，未执行程序）；audit为PASS、claim为sound-modulo-imports，M6_GE67.html已通过独立保真，尚无本参数Lean。正文 `context/propertyb-m6-67-progress-20261029/PROOF_M6_GE67.md`，方法沉淀 `research-wiki/PROPERTY_B_M6_GE67.md`。不继续扩已闭分支，不自动追68；旧五元35 Lean／36研究暂停，v2隔离。下方旧诊断为历史。

13／14短试收卷：新增条件增锁纸面引理及M9564/v972/三个81度锁条件下的四锁288型局部通过；13仍有v813/最小度152等缺口，14两预算仅筛查未过，无新全局下界，不继续扩表。该条件工具与Grok实际状态见[恢复末节](context/propertyb-general/locks-vs-uniform-20261021/STATUS.md)。

固定参数补充：k12 M4660的691429型完整锁点证书给m(12)≥4661候选，独立全域＋31边界＋3348零／一锁复核；未第二次全算两／三锁、未Lean。k13 M9544只通过v105…971，972/d81留缺口。共同基线的k10/11增益为+27/+30、k12为+28；[准确恢复入口](context/propertyb-general/locks-vs-uniform-20261021/STATUS.md)。

当前主定理的数学与端到端Lean义务均已完成；恢复[本次总报告](context/propertyb-general/bridge-12-16-20261021/REPORT.md)、[进度](context/propertyb-general/PROGRESS.md)和[人工交接](HANDOFF_PROPERTYB_GENERAL.md)。阅读[完整数学正文](PROPERTY_B_GENERAL_BOUND.html)与[Lean阅读页](PROPERTY_B_GENERAL_LEAN.html)。比较D的五项准确参考包络在全部k≥12等于B_RS+1；比较E保持k≥256的指定必要数据松弛，两者均为纸面证明、未Lean，不泛化为全部文献或全部Grill方法。旧Goal完成记录保留，不新建Goal。

**Domain Knowledge**

复用同一真实超图、共同坏对、最小顶点商及单交图；以公共点／无公共点团界削减γ，再把同一严格RS见证接到增长整数预算。12起点以k⁴≤9·2ᵏ及√M≥64保留充分余量，有限有理种子不枚举超图。[方法综合](research-wiki/PROPERTY_B_GENERAL_METHOD_SYNTHESIS.md)与既有L1–L117／失败地图继续保留。

**Existing Results**

**2026-10-29 八／九元各增加一：** 新完整计算机辅助证明为m(8)≥267、m(9)≥543，固定参考263／538的增益4／5。分别覆盖47–120与57–195点（九元新增195点），全部2094／3450实际局部型已由另一下降阶乘注入实现独立精确重算，均与作者分数相等且严格；八元299组件配额另由递归DP匹配，九元完整决策树独立重建。正文与独核在context/propertyb-m8-267-20261029/和context/propertyb-m9-543-20261029/。Grok4.7-build/xhigh/end_turn与Gemini4Argon/high/SUCCESS均有效整卷静态接受，PROOF_AUDIT为PASS、claim为sound-modulo-imports；两者未执行程序，不替代实际计算，本参数无Lean。沉淀[八／九元增益与方法](research-wiki/PROPERTY_B_M8_M9_INCREMENT_20261029.md)。总图已更新为35,67,131,267,543,1112,2275,4664，固定基线增益3,3,3,4,5,27,30,31；总HTML及M8_M9_IMPROVEMENTS.html均已通过离线桌面／手机与fresh保真检查。旧35Lean／36继续暂停，无新Goal，不动v2。



2026-10-29小参数更新：6元67完整计算机辅助证明、独核与Grok/Gemini整卷终审已通过（sound-modulo-imports，无Lean）；7元131完整候选独核通过但无新增外审；12元4664完整候选有域重建与边界复核及Grok审阅。分别沿AGENTS最新条目和原始证据恢复，不把旧65／130／4661快照当当前前沿。各自Lean状态不变。

新[claim:propertyb-general-growth-k12](research-wiki/claims/propertyb-general-growth-k12.md)为verified。指定 `Aris4Math.General.Growth.Twelve` build2576jobs exit0（15.64秒，含缓存依赖），`ReviewAuditGeneralGrowth12.lean`构建后独立原题复述exit0（7.70秒），六项核心导出及两个原题声明公理仅propext、Classical.choice、Quot.sound；[实际证据](context/propertyb-general/bridge-12-16-20261021/lean/VERIFICATION.json)为本机主执行者记录，不是第二台机器复现。T32／T33既有端到端Lean分别给m(5)≥33／34；35纸面候选尚无完整Lean，36未解，仍暂停。旧k≥17增长定理及RS17元pilot已完成，证据保留。
## Open Gaps
# Gap Map

## G8 — 一般k统一下界：当前覆盖全部k≥12

2026-10-21最新：[独立新claim](claims/propertyb-general-growth-k12.md)已登记verified。保持同一RS全域最大预算与Δ=floor(√B_RS/[8(1+ln k)])，现对全部k≥12得到Δ≥2及任意原始有限简单k元超图的两色结论。指定Twelve主模块实际构建、ReviewAuditGeneralGrowth12独立原题复述、公理审计均通过，见[Lean证据](../context/propertyb-general/bridge-12-16-20261021/lean/VERIFICATION.json)。fresh解析审计覆盖7单位／37义务，PASS_WITH_DECLARED_IMPORTS、same-family/provisional。五项明确参考包络纸面比较D也覆盖k≥12；E仍≥256纸面，二者均未Lean。新Grok最终审阅已有效end_turn（grok-4.7-build/xhigh），静态全文读取新源码／原题／日志，认可且无实质问题，未执行Lean、未重审旧核心全部证明体，见[本次处置](../context/propertyb-general/bridge-12-16-20261021/REVIEW_DISPOSITION.md)，本次不调用Gemini；旧k≥17的双模型仅作历史。无新Goal，旧35Lean／36研究暂停。

恢复：[本次总报告](../context/propertyb-general/bridge-12-16-20261021/REPORT.md)、[解析扩展](../context/propertyb-general/bridge-12-16-20261021/ANALYTIC_EXTENSION.md)、[当前规格](../FORMAL_SPEC_PROPERTYB_GENERAL.md)、[人工交接](../HANDOFF_PROPERTYB_GENERAL.md)。

### 原k≥17阶段（历史，以下范围与展示数不覆盖当前结果）

2026-10-21：全k≥17的任意原H定理及增长整数增益已正式纸面审计并经Grok/Gemini核心终审；[主claim](claims/propertyb-general-growing-integer-gain.md)为verified，无新Lean。明确五项L_ref在k≥32等于B_RS+1；Goal完整比较尾K={k≥256}另含指定零锁必要数据松弛对全部M>B_RS不通过。比较合并审计PASS及两家有效终审均完成，见[BASELINE_DISPOSITION](../context/propertyb-general
## Failed Ideas (avoid repeating)
- **已知不足：T32裸COVER LP与均匀分数解**: Lesson: 先将均匀分数解代入候选新约束；只有新结构、整性或高阶约束排除了该解时，才值得重启这个LP路线。
完整范围和原始证据见上方Thesis及对应失败地图条目。
新路线改变了这些条件时应重新判断，不能把本条当成通用禁令。
- **已知不足：T33的22点77双锁普通配额界**: Lesson: 固定22点77表示及旧普通配额仍>1；只有新增结构、真实坏槽关联或更强有效配额才值得重试，相同输入重算没有增量。
完整范围和原始证据见上方Thesis及对应失败地图条目。
新路线改变了这些条件时应重新判断，不能把本条当成通用禁令。
- **已知不足：T33的25点K7固定窗口路线**: Lesson: 失败仅限固定K7窗口与旧界；可用新选点定理避开坏型，或强化该型真实概率界，不能删除目录中的未过型。
完整范围和原始证据见上方Thesis及对应失败地图条目。
新路线改变了这些条件时应重新判断，不能把本条当成通用禁令。
- **无参数五元次三度图像桥梁**: 
- **Property B：36至40的结构与参数诊断**: 
## Key Papers (19 total)
- [paper:aglave2020_improved_bounds_uniform] Improved Bounds for Uniform Hypergraphs without Property B: 以多核心和块构造改善若干上界，并用覆盖约化、单交边对计数与RS重染色界证明 m(5)≥29。
- [paper:akhmejanova2025_fractional_hypergraph_coloring] Fractional hypergraph coloring: 将超图二染色的概率方法推广到每顶点取多色、边上无公共颜色的 (a:b)-coloring。
- [paper:burgess2026_colourings_uniform_group] Colourings of Uniform Group Divisible Designs and Maximum Packings: arXiv2510.05375v1的Thm4.4对TD(k+2,g)且k>ceil(g/2)给组均衡二染；当前a5非TD且TD(5,5)也缺严格阈值。点对唯一锚点机制为可迁移启发。
- [paper:cherkashin2015_note_random_greedy] A Note on Random Greedy Coloring of Uniform Hypergraphs: 用随机贪心的冲突有序边对重证渐近下界，并给出可直接核验的有限参数充分条件。
- [paper:cherkashin2023_small_nonuniform_hypergraphs] On small non-uniform hypergraphs without property B: 研究非均匀超图的边长加权极值，给出小阶构造及渐近上界改进；不直接排除32条五元边。
- [paper:deutsch2006_congruences_catalan_motzkin] Congruences for Catalan and Motzkin Numbers and Related Sequences: Theorem 2.1 精确给出 ν₂(C_t)=s₂(t+1)−1；本项目采用其Catalan算术，不把它本身当成概率改进。
- [paper:doyen1967_sur_nombre_despaces] Sur le nombre d’espaces linéaires non isomorphes de n points: 有限线性空间的小规模同构分类包含本项目四点三型与六点九型所需的历史枚举。
- [paper:ferber2019_quantitative_lovász_criterion] A quantitative Lovász criterion for Property B: 确定不可二染色均匀超图所需的有序单交边对最少数，并刻画等号时的完整子超图。
- [paper:gao2026_peeling_hypergraphs_structural] Peeling Hypergraphs: A Structural Sufficient Condition for Property B: 可按边顺序持续加入新顶点的 peeling 条件保证超图具有 Property B。
- [paper:goldberg1995_toward_computing] Toward Computing m(4): 作者警告若干旧证明有误；本次全页审读还给出了印刷 Lemma 5 的明确反例。
- [paper:grill2024_improved_lower_bounds] Improved Lower Bounds for Property B: 通过有限顶点数的离散随机贪心与锁定低度顶点，证明 m(5)≥32 等小均匀度下界；未排除本项目的32边情形。
- [paper:grill2024_some_upper_bounds] Some Upper Bounds for Property B: 通过启发式搜索研究小均匀度超图的上界；摘要未给具体数值。
## Recent Relationships (151 total)
  idea:propertyb36-common-marked-root-excess-20261020 --tested_by--> exp:propertyb36-twentythree-r13-restricted-three-low-20261020
  idea:propertyb36-common-marked-root-excess-20261020 --tested_by--> exp:propertyb36-r5-three-k5-complete-exception-20261020
  idea:propertyb36-common-marked-root-excess-20261020 --tested_by--> exp:propertyb36-r5-complete-candidate-20261021
  idea:propertyb36-common-marked-root-excess-20261020 --tested_by--> exp:propertyb36-r4-unit-nine-paused-20261021
  idea:propertyb36-common-marked-root-excess-20261020 --tested_by--> exp:propertyb36-r3-nine-lock-selection-paused-20261021
  idea:propertyb-restricted-k-general-bound --inspired_by--> paper:cherkashin2015_note_random_greedy
  idea:propertyb-restricted-k-general-bound --inspired_by--> paper:grill2024_improved_lower_bounds
  idea:propertyb-restricted-k-general-bound --inspired_by--> paper:radhakrishnan2000_impro
