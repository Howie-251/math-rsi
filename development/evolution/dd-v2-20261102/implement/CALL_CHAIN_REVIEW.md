# 调用链静态消费核查：B1 与 B2–B4

2026-11-03。按 Root 的有界核查委托，先读当前 [mathrsi-meta-evolve](../../../../base/skills/mathrsi-meta-evolve/SKILL.md)及 [BASE_FORMAL](BASE_FORMAL.md)，然后沿实际入口、子技能和已有原始材料检查返回链。本轮只写本报告；不改其他 owner 文件，不运行 Lean、solver、BFS、proof-checker 或付费审阅，不安排无历史全流程试跑。

**结论：在本次读取范围内未发现实际调用断口，认可 B1 与 B2–B4 的现有分流和返回契约。** 这是同家族作者的静态核对，不是新的数学验证、独立环境复现或跨模型终审。下列依据和未测范围使这一结论可直接消费。

## 1. B1：纯 Lean 输入确实能直接消费

全文读取 [verify](../../../../base/skills/mathrsi-verify/SKILL.md)、[assemble](../../../../base/skills/mathrsi-assemble/SKILL.md)、[固定Lean例](../../../../base/skills/mathrsi-verify/references/lean-target-entry.md)、[Codex lean-formalize](../../../../base/skills/skills-codex/lean-formalize/SKILL.md)。Claude版本通过全文差异对照读取其 frontmatter、默认reviewer和执行/运输差异；未把 Codex 的宿主工具约定搬给 Claude。research 的执行图、入口表、§2与§4的验收边界也实际读回。

按以下真实输入静态走链：

```text
scope = audit fixed F4 formula graph's existing Lean exports
original target = order3840, maximum_degree<=20, project Walk-D<=3 and not Walk-D<=2
source = actual Fin3840 graph definition and Exact module
build = historical Exact_RESULT(exit0) and independent-import Audit_RESULT(exit0)
trust = actual #print axioms output
current command authorization = read/reuse historical evidence; no new Lean run
prose formal audit = not requested
caller = prove/local obligation, or full verification's unique dispatcher
```

实际消费：

1. research 的起点表进入 verify 直接Lean分支；verify 图 B→K、进入段和§4都允许不经过 assemble／TeX／proof-checker。若误入 assemble，它的入口表和“仅形式目标”段直接返回 caller 建议 verify Lean 分支，不启动 writer 或第二个同级验证。
2. verify 给 lean-formalize 的输入含原声明、实际定义、固定工程、当前义务及已有证据。上游 scope 明确区分 audit/implementation/continuation，audit 不静默修目标；其§4明确 standalone Lean 不自动要求 paper-audit，故父子合同相容。
3. 由 lean-formalize 的实际声明／定义对齐与§5读取目标模块、导出、构建、独立import、公理和信任基础；verify§4同样要求实际输入供给全部证书与额外假设。只定义 Target、证明 `Target→Target` 或剩 `Certificate→Target` 都不能关闭原目标。
4. 在只授权历史消费的本例，读取已有构建可用，但必须写“静态消费历史构建，未运行Lean”；缺新的指定构建或公理证据则 pending。verify的§4、§5、例子和上游 continuation/hand-off 都保持该区分。
5. 收回 checked scope、实际 export/build/axioms和剩余后写现用 VERIFICATION，局部返回原prove caller；完整返回唯一主dispatcher。若来自原 proof audit，则 Lean 把结果交回原 audit，不递归调 proof-checker。数学缺口建议 prove，API／工程问题在形式化内部修，不先换原目标。

返回链不是“verify→Lean→自动assemble”。assemble 是需要组织自然语言正文时的独立步骤；已足够的形式证据直接返回原 caller，避免环形调用。出现需要补写原题连接时，由持有义务的 caller 决定 prove／assemble 的具体动作。

## 2. 对原始纯 Lean 对象、类型和收据的核查

本轮直接读取仓内 [DD archive](../../../../plugins/degree-diameter/archive/source/)中的：

- `formal/DegreeDiameter/Portfolio/F4Graph3840Exact.lean` 全文：两个真实导出及所调用的 degree、diameter、lower 入口；
- `formal/F4Graph3840Audit.lean` 全文：独立import、打印定义、类型与两项传递公理；
- `F4Graph3840.lean` 的 `stepVec/fiberStep/forward/graph` L40–60，以及 `SingleExtension.lean` 的 `DiameterAtMost` L13–16；这是节读，未称两份源全文审阅；
- `research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/formalization/` 的 `F4Graph3840Exact_RESULT.json`、`F4Graph3840Audit_RESULT.json` 和完整 `F4Graph3840Audit.log`。

这些材料相互匹配：

| 要核的连接 | 实际发现 |
| --- | --- |
| 载体和对象 | `graph : SimpleGraph (Fin 3840)`，Adj由实际有限域仿射forward步的对称化并去loop定义，不是未绑定的外部图certificate |
| 主类型 | `concrete_order_degree_and_D3` 给card3840、任意点degree≤20、`DiameterAtMost graph 3`，无用户待供的证书假设 |
| 原距离含义 | `DiameterAtMost` 是任意端点存在实际 `G.Walk u v` 且length≤D，包含零步；非只声明一个数值diameter字段 |
| 精确三的范围 | 第二导出为项目定义下 `D≤3 ∧ ¬D≤2`，没有声称 Mathlib ediam等式 |
| 目标构建 | Exact_RESULT记录实际Exact模块exit0、2.141916 CPU秒，未拿默认根构建冒充目标构建 |
| 独立import与公理 | Audit入口import实际Exact；RESULT exit0、2.132108 CPU秒；完整log打印两类型和各自仅 `propext, Classical.choice, Quot.sound` |

据此可消费“已有固定公式图的历史形式出口证据”。未证明／未核的是外部ASCII边表解析与一致性、恰20正则／38400边、全参数族、世界纪录、新clone图或本机新构建；新例与 BASE_FORMAL 均没有把这些范围并入 Lean 结论。未逐体重审全部传递imports，不重新认证历史数学。

## 3. 自然语言 proof-checker 没有被绕过

将同一输入改成 `prose formal audit = requested` 后，verify进入段明确同时执行§2–3，并将Lean证据送回相应audit；research§4也明确两项分别完成。只有形式入口无需造TeX；已经要求正式正文审计的任务仍须按原 checker 的输入、source-unit／义务、反例、修复、复审及closure合同完成。verify§5明确没有调用checker就不制造canonical PROOF_AUDIT。

已存在 Lean 出口并不授权把未审正文称为已审。失败或缺失的指定review保持pending，与kernel结果分开；上游lean-formalize也说明正文／HTML需要自己的对应核查。反方向，纯Lean任务无paper-audit要求时，没有凭空新增一次checker前置。两条分支都可执行且没有互相替代。

## 4. B2–B4 与 evidence 引用、父消费一致

读回本轮五技能的实际新增段与 [BASE_EFFICIENCY](BASE_EFFICIENCY.md)；对照 meta 的 [evidence-and-transfer](../../../../base/skills/mathrsi-meta-evolve/references/evidence-and-transfer.md)§2–5的原始量词、领域／base分层及后继动作。未发现把必要／充分方向或正负证据倒置。

- **基线返回**：survey给旧比较、新保证、候选影响及新输入／缺源；prepare/specify保留用户固定目标；route-loop/prove持有实际队列，撤换只服务于旧竞争门槛的待派任务，保留在途预算与合法产物。没有让survey越权改规格，也没有重复启动prepare。
- **对象改变**：route/prove先写新旧对象关系，满足假设的正结论可继承；旧否证依赖解除则只保原域。冻结源例要求实际生成输入绑定原定理；不是一句缓存提醒。matching修好旧点对仍不关闭新共同义务，未把修复反例当成功图。
- **局部rank／共同覆盖**：先看门在本固定族是否已证明必要，局部充分工具失败可转同源像并；有严格必要性与全域拒绝则可关闭准确族。必要PASS仍回共同赋值／覆盖。保留同一个起始输入，不以各路线另选源点拼成虚假并覆盖。
- **返回权**：这些新增段没有赋予文献worker、局部门或插件启动同级prove／verify的权力。原route-loop／prove的唯一caller与已有回流继续生效。领域公式保留在插件／参考，base没有复制DD固定预算或永久禁重试政策。

此前的新增本地文件与section锚点解析已保存于BASE_EFFICIENCY的核查范围；本次不为未变链接重复造测试，也不把静态引用一致性当新数学实验。

## 5. 已成熟 DD 技能的有界接口核查

全文读取当前 [dd-obstruction-certificate](../../../../plugins/degree-diameter/skills/dd-obstruction-certificate/SKILL.md) 与 [dd-transfer-diagnosis](../../../../plugins/degree-diameter/skills/dd-transfer-diagnosis/SKILL.md)；只核这两个技能的输入／消费／返回，不声称全插件终审。

`dd-obstruction-certificate` 开头指定父prove／verify义务；§1区分必要门、放松可行和构造，§3区分UNKNOWN／数值infeasible／严格dual，§5给actualcarrier、Adj、label、finaltype、caller、模块收据与公理，最后准确返回父调用处。没有让kernel公理无新增替代原目标语义，也没有要求所有历史图重算。

`dd-transfer-diagnosis` §1与§4对应 B3、B2；§2对多word恢复共同像并；§5返回首项义务、输入、预算和消费者，明确不另启动route-loop、不改base或原验收。route-loop／prove收到它的修法后仍由父唯一派发，和当前base契约一致。

两个技能返回均可被既有base直接消费；未发现必须新增adapter／调度平台才能接通的缺口。其专门程序、完整数学参考和所有archive文件没有在本轮逐个核验；由插件owner的具体运行和Root验收分别报告。

## 结论及未测范围

本核查没有待修的实际断口，认可当前分流和返回。未运行数学检查命令、未发新模型审阅、未实际编译Lean或审计新自然语言证明；历史RESULT和log只承担历史证据消费。Root 可回收这份结论纳入本轮采用判断，无需为没有发现的问题增加一层独立整流程试跑。

## 后续集成发现与修复：静态核查边界的收窄

[Gemini集成审阅](../reviews/GEMINI_V2_INTEGRATION.md)问题1找到了本次先前有界核查未覆盖的真实断口：两个DD子技能自己的返回契约虽正确，base的prepare/survey/prove却未明确派发进DD。故“返回可消费”不等于“入口已全部接通”；本文先前认可只支撑所读返回和B1分流，不应外推为整插件派发验收。

Root委托本作者只修原owned的prepare/survey/prove，已补真实DD分支和输入／返回消费，详见[BASE_EFFICIENCY后续修复](BASE_EFFICIENCY.md)。实际静态走“prepare→survey DD分支→唯一research-lit/LITERATURE→原caller”以及“prove→construction／obstruction→原prove”后，原来会落入通用分支的DD输入现有明确入口。归档wiki只读、新wiki属于任务，竞争比较与固定目标分开；既有材料只补缺口，不重开无关广搜。全仓90文档／1351目标链接检查0缺失，diff检查通过；未执行数学搜索或完整外网调查。
