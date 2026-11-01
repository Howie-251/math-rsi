# aris4math 研究入口

**2026-10-21 13／14短试已停止：** 条件增锁引理修复M9544、v972、d=e81的特定三锁分支；M9564、v972在已选三个81度单位锁条件下，第四度81…128的288型／1134计数向量全过，但v813／最小度152等仍缺。13／14均无新完整下界，不继续扩表。13当前9539→统一9542／C.2 9564；14为19602→19606／19647。引理三项数学义务已获Grok有效静态讨论（未审288型数值），红图仍只到12；[恢复及条件工具](context/propertyb-general/locks-vs-uniform-20261021/STATUS.md)。以下旧v972停止点已由该局部补充细化。

**2026-10-21 锁点实例／共同基线：** k=12、M=4660完整691429局部型全过，给m(12)≥4661的计算机辅助证明候选；独立完整参数域、31个Fraction边界型及全部3348个零／一锁型已核，两／三锁未第二次全算、未Lean。新Grok只审一般准则迁移，不是最终M4660整表审阅。k13 M9544仅完整通过至v971，v972/d=e81留缺口，无新完整下界。共同基线k5…12为32,64,128,263,538,1085,2245,4633，增益3,1,2,3,4,27,30,28；k10/11旧GL增益+42/+62保留历史。全部k≥12蓝色统一增长Lean与verified状态保持。详见[共同恢复入口](context/propertyb-general/locks-vs-uniform-20261021/STATUS.md)。

**2026-10-21 当前成果：一般增长定理已完整覆盖全部k≥12，Δ≥2。** 同一RS全域最大预算与同一floor增长公式不变；完整解析证明、fresh7单位／37义务审计、指定Twelve主构建和原题独立导入、公理审计均已完成。新Grok最终回应有效完成并认可，无实质问题；本次不调用Gemini。旧17起点审阅和全部既有成果保留历史。未创建或恢复Goal，旧35Lean／36研究暂停。

## Problem Statement

对每个整数k≥12，B_RS(k)为精确RS积分判据接受的全部正整数预算的最大元。设Δ(k)=floor(√B_RS(k)/(8(1+ln k)))，则Δ≥2，任意有限简单k元超图在边数≤B_RS+Δ时都存在每条边含两色的Bool染色，故m(k)≥B_RS+Δ+1。原对象没有点数、点对覆盖、度数、共度或线性附加条件。当前[正式规格](FORMAL_SPEC_PROPERTYB_GENERAL.md)。

## What I'm Looking For

**2026-10-29 六元+3最新：** m(6)≥67的完整计算机辅助证明已装配，27–44全部实际分支及独立精确复算齐备；最后34点87型、35点306型均已接到原染色。Grok4.7-build/xhigh与Gemini4Argon/high整卷终审均有效接受（静态阅读，未执行程序）；audit为PASS、claim为sound-modulo-imports，M6_GE67.html已通过独立保真，尚无本参数Lean。正文 `context/propertyb-m6-67-progress-20261029/PROOF_M6_GE67.md`，方法沉淀 `research-wiki/PROPERTY_B_M6_GE67.md`。不继续扩已闭分支，不自动追68；旧五元35 Lean／36研究暂停，v2隔离。下方旧诊断为历史。

13／14短试收卷：新增条件增锁纸面引理及M9564/v972/三个81度锁条件下的四锁288型局部通过；13仍有v813/最小度152等缺口，14两预算仅筛查未过，无新全局下界，不继续扩表。该条件工具与Grok实际状态见[恢复末节](context/propertyb-general/locks-vs-uniform-20261021/STATUS.md)。

固定参数补充：k12 M4660的691429型完整锁点证书给m(12)≥4661候选，独立全域＋31边界＋3348零／一锁复核；未第二次全算两／三锁、未Lean。k13 M9544只通过v105…971，972/d81留缺口。共同基线的k10/11增益为+27/+30、k12为+28；[准确恢复入口](context/propertyb-general/locks-vs-uniform-20261021/STATUS.md)。

当前主定理的数学与端到端Lean义务均已完成；恢复[本次总报告](context/propertyb-general/bridge-12-16-20261021/REPORT.md)、[进度](context/propertyb-general/PROGRESS.md)和[人工交接](HANDOFF_PROPERTYB_GENERAL.md)。阅读[完整数学正文](PROPERTY_B_GENERAL_BOUND.html)与[Lean阅读页](PROPERTY_B_GENERAL_LEAN.html)。比较D的五项准确参考包络在全部k≥12等于B_RS+1；比较E保持k≥256的指定必要数据松弛，两者均为纸面证明、未Lean，不泛化为全部文献或全部Grill方法。旧Goal完成记录保留，不新建Goal。

## Constraints

旧36自然语言研究和35Lean继续暂停，不操作独立编码理论项目aris4math_v2。模型审阅与实际Lean核验分别报告：本次Grok最终grok-4.7-build/xhigh/end_turn有效，静态全文读取Twelve、原题复述与日志，无实质问题；未执行Lean、未重审旧核心全部证明体。Gemini本轮不调用，旧17范围Gemini记录不算新增12范围审阅。展示完成以本次 `.aris/traces/render-html/2026-10-21_general-bound-k12/` 实际记录为准。

## Domain Knowledge

复用同一真实超图、共同坏对、最小顶点商及单交图；以公共点／无公共点团界削减γ，再把同一严格RS见证接到增长整数预算。12起点以k⁴≤9·2ᵏ及√M≥64保留充分余量，有限有理种子不枚举超图。[方法综合](research-wiki/PROPERTY_B_GENERAL_METHOD_SYNTHESIS.md)与既有L1–L117／失败地图继续保留。

## Existing Results

**2026-10-29 八／九元各增加一：** 新完整计算机辅助证明为m(8)≥267、m(9)≥543，固定参考263／538的增益4／5。分别覆盖47–120与57–195点（九元新增195点），全部2094／3450实际局部型已由另一下降阶乘注入实现独立精确重算，均与作者分数相等且严格；八元299组件配额另由递归DP匹配，九元完整决策树独立重建。正文与独核在context/propertyb-m8-267-20261029/和context/propertyb-m9-543-20261029/。Grok4.7-build/xhigh/end_turn与Gemini4Argon/high/SUCCESS均有效整卷静态接受，PROOF_AUDIT为PASS、claim为sound-modulo-imports；两者未执行程序，不替代实际计算，本参数无Lean。沉淀[八／九元增益与方法](research-wiki/PROPERTY_B_M8_M9_INCREMENT_20261029.md)。总图已更新为35,67,131,267,543,1112,2275,4664，固定基线增益3,3,3,4,5,27,30,31；总HTML及M8_M9_IMPROVEMENTS.html均已通过离线桌面／手机与fresh保真检查。旧35Lean／36继续暂停，无新Goal，不动v2。



2026-10-29小参数更新：6元67完整计算机辅助证明、独核与Grok/Gemini整卷终审已通过（sound-modulo-imports，无Lean）；7元131完整候选独核通过但无新增外审；12元4664完整候选有域重建与边界复核及Grok审阅。分别沿AGENTS最新条目和原始证据恢复，不把旧65／130／4661快照当当前前沿。各自Lean状态不变。

新[claim:propertyb-general-growth-k12](research-wiki/claims/propertyb-general-growth-k12.md)为verified。指定 `Aris4Math.General.Growth.Twelve` build2576jobs exit0（15.64秒，含缓存依赖），`ReviewAuditGeneralGrowth12.lean`构建后独立原题复述exit0（7.70秒），六项核心导出及两个原题声明公理仅propext、Classical.choice、Quot.sound；[实际证据](context/propertyb-general/bridge-12-16-20261021/lean/VERIFICATION.json)为本机主执行者记录，不是第二台机器复现。T32／T33既有端到端Lean分别给m(5)≥33／34；35纸面候选尚无完整Lean，36未解，仍暂停。旧k≥17增长定理及RS17元pilot已完成，证据保留。

## 既有导航与阶段记录（历史）

以下原稿逐段保留，其17／32范围、pilot“当前”、展示数与待启动描述仅代表当时快照，不覆盖上方12起点的完整成果。

# aris4math 研究入口

**2026-10-21：一般RS核心与17元调用的Lean阶段已完成全部验收，Goal工具已返回status=complete。** 一般实际RS失败上界、原二染色充分判据及任意有限简单17元／≤131072边的原Bool染色命题已经闭合。指定PilotMain构建成功，构建后独立原题审计exit0，七项传递公理均仅propext、Classical.choice、Quot.sound；无未证概率、证书或结构前提。Grok4.7-build/xhigh与Gemini4Argon/high最终C均有效接受（静态读源码／日志，未执行Lean）；最终离线HTML桌面／手机与fresh保真PASS。已完成范围是RS核心和17元调用，完整k≥17增长整数增益仍待后续形式化；不自动启动下一阶段，旧35／36暂停，v2隔离。 恢复[最终验收](context/propertyb-general-lean-pilot/COMPLETION_AUDIT.md)，阅读[离线报告](PROPERTY_B_GENERAL_LEAN_PILOT.html)。

以下一般纸面成果保持完成；本次RS核心Lean阶段的验收证据另列，不将其范围扩大到完整增长定理。

2026-10-21 round02：一般下界数学证明与指定终审已完成，全部交付已完成，Goal工具已返回status=complete；Goal工具已实际返回status=complete。旧m(5)≥36自然语言研究和m(5)≥35 Lean继续暂停，v2保持隔离。

## 历史：Problem Statement

当前阶段是[一般RS核心Lean试点](GOAL_PROPERTYB_GENERAL_LEAN_PILOT.md)：从实际重染算法证明一般失败上界及原染色充分判据，再完成任意有限简单17元、≤2^17边的Bool染色caller。三个最终导出、独立根审计、两家终审与展示交付均完成；完整一般增长定理的Lean不在本阶段范围。

已完成纸面阶段的原目标：寻找明确整数范围K及统一预算B(k)，证明每个k∈K的任意有限简单k元超图在边数≤B(k)时均具有Property B，并对准确的适用基线取得实际改进。顶点数、度数、共度等只能作内部完整分流。完整目标为[GOAL_PROPERTYB_GENERAL_BOUND.md](GOAL_PROPERTYB_GENERAL_BOUND.md)，本轮规格为[FORMAL_SPEC_PROPERTYB_GENERAL.md](FORMAL_SPEC_PROPERTYB_GENERAL.md)。

## 历史：What I'm Looking For

本阶段全部验收完成；ProbabilityBound／PilotMain、独立原题与公理总审计、两家最终C及HTML交付均通过。恢复[Lean试点进度](context/propertyb-general-lean-pilot/PROGRESS.md)。后续完整增长形式化须另行决定，不自动启动。

已完成的一般纸面阶段：数学与规定审阅已闭合，最终展示／交付已完成，Goal工具已实际返回status=complete。全k≥17的任意原H定理已正式审计并经Grok/Gemini核心终审，[主claim](research-wiki/claims/propertyb-general-growing-integer-gain.md)为verified（纸面证明，无新Lean）。明确五项L_ref在k≥32等于B_RS+1；完整比较尾K={k≥256}另包含指定零锁必要数据松弛对全部M>B_RS不通过，两项均已合并审计及有效跨家族比较终审。恢复[PROGRESS](context/propertyb-general/PROGRESS.md)，阅读[离线单卷](PROPERTY_B_GENERAL_BOUND.html)，人工交接[HANDOFF](HANDOFF_PROPERTYB_GENERAL.md)。比较不扩大为全部潜在Grill法或实际H见证。

## 历史：Constraints

旧36自然语言与35 Lean保持暂停，已验收全局下界仍为m(5)≥34。不运行旧Lean，不读取或干扰独立编码理论项目aris4math_v2。优先严格自然语言证明与离线内联HTML；模型认可、局部计算和条件引理须与最终定理验收分开。

## 历史：Domain Knowledge

已复用的方法链是：保留同一实际超图与共同坏对对象，经最小顶点商约化接到真实单交图；以公共点／无公共点的经典线性交族团界削减γ，再把同一个严格RS参数见证转为统一增长的整数预算。这是覆盖全部原始对象域的解析证明，不是样例归纳。

复用[一般方法综合](research-wiki/PROPERTY_B_GENERAL_METHOD_SYNTHESIS.md)、[L1–L117库存](research-wiki/PROPERTY_B_REUSABLE_LEMMAS.md)、[条件工具](research-wiki/PROPERTY_B_CONDITIONAL_TOOLKIT_36.md)、[研究经验](research-wiki/PROPERTY_B_RESEARCH_LESSONS.md)及[失败地图](research-wiki/PROPERTY_B_FAILURE_ATLAS.md)。重点保留实际原边索引、单交图、共同坏对、Gram主矩阵和同一源的共享容量；局部有限表和五元常数不直接外推一般k。新候选先与RS原始FKG／精确积分以及同范围内更强适用结果比较。

## 历史：Existing Results

T32与T33均已完成端到端Lean证明，分别得到m(5)≥33和m(5)≥34。m(5)≥35有完整纸面候选、端到端Lean未完成；m(5)≥36仍有实质缺口。旧36准确剩余见[暂停交接](context/propertyb35-paper/PAUSE_HANDOFF_20261021.md)与[范围审计](context/propertyb35-paper/REMAINING_AUDIT.md)。

## 历史：当前恢复与证据

当前依据为[COMBINED_AUDIT](context/propertyb-general/round02/formal-audit/COMBINED_AUDIT.md)、[核心终审处置](context/propertyb-general/round02/reviews/CORE_DISPOSITION.md)与[比较终审处置](context/propertyb-general/round02/reviews/BASELINE_DISPOSITION.md)。核心18/18源单位、78项义务闭合；清洁比较源及增量审计已闭合。Grok比较原生completed终稿有效，原MCP envelope缺失如实保留。全部数学证明不依赖模型投票；最终HTML及交付验收已由root完成，Goal工具已实际返回status=complete。

首轮来源恢复记录（历史）：

一般研究首轮入口为[round01](context/propertyb-general/round01/)。Grok的SINGLE_INTERSECTION_TURAN既有请求已从原生会话恢复完整终稿，身份grok-4.7-build/xhigh，完成事件2026-10-21T03:28:01Z；它只作静态审阅，不替代主代理核验。原文和恢复元数据见[round01/reviews](context/propertyb-general/round01/reviews/)。其它审阅状态以本轮恢复报告与PROGRESS为准。

2026-10-21：数学、指定终审、离线HTML和人工交接均已完成交付；Goal工具已实际返回status=complete。最终验收入口为context/propertyb-general/round02/COMPLETION_AUDIT.md；最终HTML含532条内嵌公式，离线桌面／手机检查PASS，已用Microsoft Edge打开。旧36与35Lean暂停、v2隔离保持原状。

## 历史：历史导航

round02较早方向快照（历史，已被上方当前状态替代）：一般下界Goal继续收尾，恢复[PROGRESS](context/propertyb-general/PROGRESS.md)。全k≥17的原H接口与增长整数增益已过正式纸面审计及Grok/Gemini核心审阅，见[已登记定理](research-wiki/claims/propertyb-general-growing-integer-gain.md)。五项明确参考包络比较（k≥32）与指定零锁松弛比较（k≥256）已有完整证明及正式增量审计，跨家族比较终审与最终HTML保真在途。主定理不以样例或模型认可代替证明，不宣称世界最优；尚未标记整个Goal完成。

本页2026-10-20及更早的完整快照保存在[RESEARCH_BRIEF_BEFORE.md](context/propertyb-general/round02/recovery/RESEARCH_BRIEF_BEFORE.md)，其中active均指当时状态。原35 Lean精确暂停入口为[PAUSE_CHECKPOINT_20261015.md](context/propertyb34/round02/PAUSE_CHECKPOINT_20261015.md)。以下为已完成T32/T33的既有交付入口，不是当前Goal。

## 历史：已完成成果的详细入口

**T33 成果（2026-10-13）：任意有限简单五元超图，至多 33 边均具有 Property B，因此 m(5)≥34。** [新主定理](formal/Aris4Math/ThirtyThree/Main.lean)已完成端到端 Lean 证明；显式 `lake build Aris4Math.ThirtyThree.Main` 完成 1138 jobs、exit 0，构建后的[独立原题复述](formal/ReviewAudit33.lean)也为 exit 0。19–25 点所有实际分支、真实输入和原染色见证内部闭合，8 项顶层传递公理仅标准三项。

[单卷离线 HTML](PROOF_PACKAGE_33.html)及[规范证明正文](proofs/propertyb33/PROOF_PACKAGE.md)内联完整数学论证。[形式核验记录](context/propertyb33/FORMAL_VERIFICATION.md)说明实际声明、构建和复现；[人工审查交接](HANDOFF_FOR_REVIEW_33.md)及 `aris4math_t33_review_bundle.zip` 为交付入口。证明、审计、转交包与 wiki 均已完成；[实时进度](context/propertyb33/PROGRESS.md)为恢复入口。

Grok 与 Gemini 最终 C 均有效返回，在各自读取范围内未发现实质问题；均只读源码和现有日志，没有执行 Lean。fresh proof-checker 的两处正文说明已修正，HTML 保真检查通过。详见[证明审计](context/propertyb33/round02/final-audit/PROOF_AUDIT.md)与[模型审阅处置](context/propertyb33/round02/reviews/REVIEW_DISPOSITION.md)。内核证明、模型意见和他人独立复现分别记录。

正式目标仍为 [T33 规格](context/propertyb33-preparation/FORMAL_SPEC_PROPERTYB_33.md)，不宣称 m(5)=34。旧 T32 及同一份 research wiki 继续保留；启动前准备和中途导航已存入[历史快照](context/propertyb33/round02/final-audit/NAVIGATION_HISTORY.md)。下方为已完成的原 T32 成果。

**原目标 m(5)≥33 已有完整 Lean 证明：任意有限简单五元超图，只要边数至多32，就存在每条边均含两色的二染色。** [Main.lean](formal/Aris4Math/Main.lean) 已将任意有限顶点集的约化、19–25点全部结构分支、实际条件概率计数及严格数值界接成主定理。默认构建和独立导入审计均成功，主定理的传递公理依赖只有 Lean 的标准三项。

- [完整证明阅读版](PROOF_PACKAGE.html)及[完整 Markdown 阅读稿](PROOF_PACKAGE_FULL.md)：单页内联数学规格、三份引理全文、结构覆盖、精确算术和 Lean 核验；公式已嵌入，离线可读。阅读稿由规范源自动合成，原简版汇总仍在 `PROOF_PACKAGE.md`。
- [正式数学规格](FORMAL_SPEC.md)：对象、量词与原目标；没有附加顶点数、正则性或均衡染色要求。
- [形式核验记录](context/FORMAL_VERIFICATION_PROGRESS.md)：实际主定理、完整模块对应、构建证据和复现命令。
- [项目交接](NEXT_SESSION.md)：交付与最终审阅的实时状态。
- [Research wiki](research-wiki/index.md)：文献、来源关系与已闭合的证明义务。

证明采用一般计数与解析分类，不依赖整图穷举。Grok 与全新 Gemini 会话 r10 均已完成最终装配审阅，在各自读取范围内未发现具体问题；两者阅读源码与现有构建日志，没有亲自执行构建。Gemini 此前 r8、retry1、r9 的地区报错仍保留为失败记录。模型审阅和前期反例搜索用于查错，实际记录见[审阅汇总](context/reviews/research/REVIEW_NOTES.md)。

已核查的文献起点为 Grill–Linzmayer arXiv:2403.05674v3 的 m(5)≥32；该文献基准不是本证明的前提。通用方法已有文献先例，本项目结果是上述下界证明，不宣称 m(5)=33 或构造了33边反例。原始46份PDF及15份补充原文的实际阅读范围分别见 [阅读索引](context/READING_INDEX.md)和[参考文献目录](ref/README.md)。
