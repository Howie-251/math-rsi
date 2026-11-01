# aris4math 研究入口

**2026-10-13 18:00 UTC，最后30分钟收卷。** 用户限定本轮截止18:06:37 UTC（北京02:06:37）；保存后暂停，不自动延长。新增21点唯一七度和至少五七度两个完整实际分支已Lean通过，接入Assembly并完成两份裸Finset/Bool独立导入，8项公理查询均标准三项。剩余精确为21点最小度7、恰有2/3/4个七度点，以及22–25完整染色。23点3→4实际分类与80项严格排除也已通过，保留22+19残型。T34 Main仍未完成，已验收下界仍为m(5)≥34。详细收卷见`context/propertyb34/round01/FINAL_30_MINUTES_REPORT.md`，21点续接见同轮`twentyone-lean/DEGREE_SEVEN_CONTINUATION.md`。


**T34恢复入口：** [既有Goal](GOAL_PROPERTYB_34.md)已运行并按用户要求暂停，恢复时继续该Goal；[最后收卷](context/propertyb34/round01/FINAL_30_MINUTES_REPORT.md)与[持续进度](context/propertyb34/PROGRESS.md)给准确剩余。本页2026-10-14修正了仍写“待启动/active”的旧导航；本轮只整理通用引理与经验，不恢复求解。

## Existing Results

T32与T33均已完成端到端Lean证明，分别得到m(5)≥33和m(5)≥34。T33的1138-job指定Main构建及裸Finite/Finset原题审计通过；两份既有证明保持完成状态。详细交付与原始证据见下文和`NEXT_SESSION.md`。

## What I'm Looking For

当前任务为提炼33、34及35候选中的通用数学、Lean验证和效率经验。T34求解Goal保持暂停；所有19–25点已有完整纸面候选。端到端Lean尚剩21点最小度7且恰有2/3/4个七度点、22–25点完整染色，以及主定理和最终验收。原T32/T33保持完成。用户恢复后按既有GOAL_PROPERTYB_34.md和最新收卷续行，不重复已完成分支。

## Domain Knowledge

复用[12组通用引理](/Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_REUSABLE_LEMMAS.md)、[三轮方法与效率](/Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_RESEARCH_LESSONS.md)、[15项失败地图](/Users/rfy_naiveai/Desktop/aris4math/research-wiki/PROPERTY_B_FAILURE_ATLAS.md)。数学层优先真实迹投影/增锁、容量完整性、避锁坏对配额和共享实际坏对的多布局弱对偶；一般参数纸面推广与已有Lean范围分开记录。性能改动须以非平凡真实caller的端到端实测为依据，25点公共系数缓存仍未完整实现。

迁移先重算整数度数预算和选点覆盖，再检查逐位置min(A,B,C−D)的实际收益。优先保留真实坏对关联、避锁配额与精确dual；局部分类必须绑定实际H。失败记录注明固定模型/窗口/预算及重试条件，不能把松弛反例当超图反例。先跑通真实caller，再扩表；重Lean核验按实测内存调度，由单一执行者维护正规构建。

## 已完成成果的详细入口

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
