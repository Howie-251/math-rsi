---
name: mathrsi-verify
description: 对已装配数学证明或明确局部义务执行验证子工作流：按需装配，核覆盖与独立精确复算，调用 ARIS proof-checker 自身修复循环，并在需要时接 Lean。输出准确范围的 VERIFICATION.md；实质数学缺口返回 mathrsi-prove，不用路线评分充当定理验收。
---

# MathRSI 装配与验证工作流

本技能接收一个候选解答或明确的局部义务，将证明、实际输入、计算和必要审阅接成可核验的证据。它对应研究主线的“装配验证”阶段，内部在需要时调用 [mathrsi-assemble](../mathrsi-assemble/SKILL.md)，再选择与疑问相符的核验。已有完整稿直接复用；不要求验证前再改写一次。

输出是工作区现有验证记录；没有约定时用 `VERIFICATION.md`。它引用真正执行得到的 `PROOF_AUDIT.{md,json}`、确定性核验结果、Lean 导出与审阅记录，说明它们各自支持什么。本技能不生成一份仿上游的 canonical audit，不自行给 wiki 新建“已验证”声明，不将模型分数或文件齐全当成原题证明。

**后继调度只由一个owner执行。** 组合调用在指定scope完成后返回原caller：局部验证回原prove义务，全局验证回主dispatcher，由它决定handoff或返回prove。本文的后继技能是结果建议，verify不同时替父流程启动它们；内部assemble、proof-checker及所需Lean仍由verify实际执行。独立调用只做用户授权的验证范围；若用户明确要求持续推进，由本agent接主调度一次后选择下一阶段，不在子验证与主流程两处重复派发。

## 进入、范围和恢复

读原规格、候选正文、当前义务和已有验证。先确定本次入口是完整原定理验收，还是“引理 L 的实际 caller”“参数域 D 的精确重算”“归约 R 的覆盖”等局部验证。局部入口是正常用法，不用每次审整个项目；但报告标题和结论保持该范围，不能将其汇总成原题已经通过。

若由 prove 为高风险子引理提前调用，调用方就是本次返回点：只装配/核验该义务实际需要的局部材料，跳过全主定理 assemble 和 handoff。收回准确结论、counterexample或未闭条件后，直接返回原 prove run 继续其下游 caller；即使局部完整通过，也不自行推进到“原题最终交付”。全局验收完成也先返回主dispatcher，建议是否进入handoff。

恢复时从最后一项具体未核事实进入。已有验证对哪个版本、哪个域、哪些声明有效，按实际材料确认；源声明、输入或算法变了，只重核受影响的义务和下游。上次服务不可用与上次数学失败分开保存。不要重开已完成的旧研究、重复未变的整卷审阅，或因一次交付中断重跑所有算术。

完整候选还散落在多份记录时，调用 assemble，交原题、已证引理、进口和证书，消费其正文和连接状态。它若指出缺实质数学，将缺口返回caller建议交prove；此时可以按原scope验证已有局部结果，但不能发起一个假定全证已齐的最终审计。已有完整稿则继续以下步骤。新稿已确定正式审计时可由assemble直接生成唯一 `PROOF.tex`，免去不必要的双载体；已有Markdown需要保留时才按下文适配。

## 1. 先处理本次真正未决的证据问题

沿原输入到结论检查关键接口，选择能解决实际疑问的检查。纯解析证明不需要制造算术表；计算机辅助证明不能省去数据含义和覆盖。至少分清下面三种对象，避免一个程序 PASS 被重复解释成三个结论。

第一是对象域与归约。检查全称对象进入必要域的论证、分类覆盖、规范化兼容和各分支的并集是否包含原域。程序遍历一份列表不证明列表完整；某筛选条件即使便宜，也要有不会误删所需对象的依据。对只要求一个见证的任务，完整检查该见证即可，不要求搜索过程穷尽。

第二是检查器实际判定的命题。读真实代码、输入和输出，核计数单位、索引、重数、顺序/无序、边界、取整、精度和共同对象约定。由任务或领域插件提供的可信 checker 优先复用；不要让作者改完 checker 后只凭自报通过。若需要独立复算，应使用能独立重建该数学量的方法，读取实际输入，比较准确结果和覆盖，并保存命令、退出码和差异见证。第二次执行同一程序可验证可重现性，但不能称第二概率实现或独立算法核验。

第三是核验输出如何用于主证明。即使算术全部严格，也仍要核实际对象确实给出该公式或证书、该界确实改变目标、计算范围与分流条件相合。样本、启发式浮点和小域实验保持发现证据；用于临界严格结论的数值用整数、准确分数或有证明的定向误差依据。并非所有项都必须换成 Fraction，已有正确的整数或区间方法可以复用。

把结论写进原有报告或 `VERIFICATION.md`：本次检查的精确谓词、输入和完整范围、使用方法、实际结果、仍需数学连接。若只是源代码/索引的小缺陷，修复并重跑受影响范围；若某个归约或覆盖引理根本未证，将那个义务交回 [mathrsi-prove](../mathrsi-prove/SKILL.md)。

## 2. 区分局部对抗审阅与完整证明审计

一个新归约、代码与公式接口、候选反例或局部共同约束，可以复用 [research-review Codex](../skills-codex/research-review/SKILL.md)／[Claude 主线](../research-review/SKILL.md)的取证、reviewer路由和trace机制执行一个数学审阅slot。输入是原始局部证明、定义、实际 caller、代码与具体疑问。先读相应技能和backend/trace合同，实际调用选定reviewer并保存原始回应、读取/执行范围；这个slot由当前verify持有范围和返回点，不启动原版论文评分/共识循环，也不声称已跑完整research-review。修真实问题，必要时仅复核新增证据；本地短义务可用独立agent，相应同家族范围如实provisional，用户指定外部reviewer的要求不被替换。

要验收完整自然语言证明，或对一份自足局部定理运行正式 proof audit，使用 [proof-checker Codex](../skills-codex/proof-checker/SKILL.md)／[Claude 主线](../proof-checker/SKILL.md)。它拥有 proof skeleton、完整义务审计、反例检查、修复和复审循环。不能只取它的 reviewer prompt 然后自造 `PROOF_AUDIT.json`，也不在外面再套一个 route-loop 或定时循环来替代它的内部状态。

**实际输入适配必须先做对。** 当前两端 checker 的准备与 detector 以 `.tex`、定理/引理/proof 环境和 source-unit 为中心，不能声称任意 `PROOF.md` 能直接获得等价全证审计。完整 Markdown、独立局部证明或带代码的证明，调用前读 [proof-checker 输入与范围适配](references/proof-checker-inputs.md)。已有 LaTeX 直接用原输入；Markdown 需要有原句对应的无损审计用 TeX，审阅同时读取原文与依赖。不要把无 TeX theorem 的 detector-negative `NOT_APPLICABLE`当成数学已审。

## 3. 执行 checker 本身的流程并消费它的真实结果

向 checker 指定本次实际 proof 入口、原命题、允许进口、必要源码与证据位置、准确 scope，以及已选 reviewer。helper 通过本仓 `base/tools`实际调用；先完整读当前宿主技能及它在该阶段要求的参考，不改复制的上游源。新选择或项目 reviewer 由它的路由解析，已建立的授权不重复询问；选定服务缺失也不假装已审或悄悄改 provider。

执行其准备、source-unit 抽取与覆盖回执、全局义务 ledger、首次完整审阅、反例 pass、真实修复、复审、整体 closure 和必要 blind review。source-unit coverage 只是执行覆盖，不证明义务发现完整。精确复算、完整域证明与 reviewer 各承担各自职责，不能把其中一个核验字段扩成整个数学 PASS。

checker 的修复包含补推导、加假设、弱化结论或补准确引用。对已证明内容的漏写、错误索引、局部实现与陈述不一致，可在这次验证内修好，检查受影响调用和数据，再按 checker 自己的合同复审。加假设或弱化仅产生显式变体，不替换原目标；需要新数学定理、关键选取或大段新分类时，记录原 audit 的实际状态和 blocker，交回 prove。无需先把整个方法再评分一轮。

若checker修的是由Markdown转换的审计TeX，将实质修复同步回原正文，再核对源对应记录与最终审计输入；交付前确认两者是同一个论证。短稿可将对应写在已有audit说明，复杂转写再用SOURCE_MAP。转换稿通过不能认证尚未同步的旧正文，具体往返由上述输入适配说明执行。

跨轮合同以**对应宿主的实际技能**为准：当前 Claude 主线 Phase 3 使用保存的 reviewer thread 回查修复；Codex mirror Phase 3 每轮 fresh agent。Codex 同家族为 provisional；真实跨家族完成、scope 和身份另记。主线当前有 `--deep-fix` / `--restatement-check`，Codex mirror没有对应完整模式，不能给两个宿主统一虚构 flags。被选外部 route 的 first-call/reply 合同也不互换。

checker 未过其轮次上限时，消费它的 unrecoverable report：具体阻塞、保留的有效部分、可行修复。`FAIL`是当前证明或声明有问题，不能自动解释为原题为假；`ERROR`/`BLOCKED`是实际未审完或缺材料，也不是反例。把本次 raw verdict、acceptance 元数据、具体未闭义务与下一动作保留，不能把它们重标为 PASS 来继续交付。

## 4. 需要时接 Lean，完成它真正负责的义务

用户要求 Lean、继续现有形式工程，或具体关键连接值得形式检查时，读 [lean-formalize Codex](../skills-codex/lean-formalize/SKILL.md)／[Claude 主线](../lean-formalize/SKILL.md)并执行。提供原命题、实际定义、固定工程、关键 proof route、当前待证接口与已有证据。它可以在证明推进中早已运行；本阶段复用当前有效结果，不要求把 Lean 永远拖到全文完成之后。

若从 checker 内部调用 Lean，返回其 checked scope、exported declaration、语义对齐、build 与传递公理证据给原 audit；不由 Lean 再调用 checker。若是 verify 直接组织两项工作，也保持各自产物与 scope，不新造相互递归的验证栈。

Lean 完成需从任意原输入装配出主命题的证明项，实际构建目标模块，展开类型和定义，检查传递公理；multi-module 另作实际入口的独立 import，短单文件按原技能不额外新建工程。`Certificate x → Target x`需要构造所需证书，定义 `Target : Prop`不是证明它。A/B/C 依它的语义对齐、关键论证和最终 export 流程；未变化的证据复用，明确指定的 reviewer 缺失保持 pending。

保存实际命令/退出码/输出，区分增量构建、干净重建和他人独立复现。信任基础按任务允许值说明，不把某个旧项目的 native_decide 禁令变成所有数学通用要求。形式 theorem 已核与某项交付/跨模型复核尚缺可以同时成立，不能因服务失败撤销已经成立的形式结果。

## 5. 写出能驱动下一步的 VERIFICATION.md

复用已有验证记录，没有时写 `VERIFICATION.md`。至少让读者能找到以下事实，按任务自然组织即可，不要求填一张统一评分表：原题及本次准确 scope；正文与源版本/具体改变；域覆盖和原输入连接；实际确定性检查与结果；真正上游 audit 的路径、raw verdict和未决项；Lean 的实际 export/build/axioms（若适用）；reviewer 实际阅读/执行范围与 pending；当前原题状态和下一步。

完整 `PROOF_AUDIT.json`在原 audit 目录，局部 audit 在它自己的 scope 目录。报告链接它们，不把多个局部 PASS 拼成一个假的全局 audit，也不把文字报告命名为上游 canonical JSON。checker 自己触发的 wiki hook 沿其真结果运行，本技能只引用该记录；不会为了进入交付自行造一个 verified claim。

组合调用最后返回原caller：局部scope交回原prove；全局scope交回主dispatcher。完成原目标所需数学与已约定核验均成立时，建议后继 [mathrsi-handoff](../mathrsi-handoff/SKILL.md)；关键数学缺失时建议返回prove，并附最小义务、actual caller、已有证据和可复用成果；只有prove判断需要重选方法才回route-loop。verify本次不另启动这些后继。已闭局部结果也可以作为局部交付，主目标仍open。文档或服务不可用则返回准确pending，交主调度继续无依赖工作。独立调用的持续授权按入口的单一调度规则处理。

## 实际调用与返回例

```text
读取本仓 mathrsi-verify/SKILL.md 并执行。
原题 FORMAL_SPEC.md，完整稿为现用 PROOF.tex 或 PROOF.md，
计算证据 work/exact/REPORT.md。
先沿用现稿，检查原输入到必要域的覆盖与独立准确重算；
已有TeX直接审；需保留Markdown时按reference保留原句对应并作审计TeX，
再实际执行当前宿主 proof-checker，将其真实产物链接到 VERIFICATION.md。
已有 formal/ 工程是原任务要求：复用并按 lean-formalize 核对实际主声明。
完成后返回本次caller，附建议handoff或返回prove的依据，不重复启动后继。
发现新的实质数学缺口准确保留，勿降低原题要求。
```

局部调用可以是“只验证 L 在 caller C 的假设供给及参数域 D；不要重审其余章节”。此时返回准确局部结论，列明是否进入 research-review 或自足局部 proof-checker、实际结果与剩余全局义务。恢复时先读 VERIFICATION 的 next obligation和对应源，不从全证审计第一轮重新开始。
