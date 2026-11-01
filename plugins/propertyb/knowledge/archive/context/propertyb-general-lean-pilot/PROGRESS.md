# 一般RS核心Lean阶段进度

2026-10-21：本阶段全部验收已完成，Goal工具已返回status=complete。旧一般自然语言Goal保持完成；旧35 Lean和36研究暂停，不触碰v2。

阶段目标见 `GOAL_PROPERTYB_GENERAL_LEAN_PILOT.md`：从实际RS算法证明一般失败上界与原染色充分判据，再为任意有限简单17元、≤2^17边的超图提供完整调用。完整增长整数增益定理的Lean不在本阶段范围。一般P/C与17元Pilot已正式构建及独立原题审计；两家最终C均有效接受明确范围；最终HTML离线桌面／手机检查和fresh保真PASS，全部验收通过。

## 当前义务表

表示已固定为有限初始颜色、任意p的Bernoulli资格位和均匀全排列。源码均在 `formal/Aris4Math/General/RS/`。下表登记已闭合的实际模块、原结论及验收证据。

|义务|文件／已证接口|实际状态与证据|
|---|---|---|
|原边集、真实有向γ、原命题|Definitions|定义固定；已参与root正式lake构建|
|初始色触发与失败覆盖|Algorithm：`new_mono_pair_event`、`failure_covered`、`bichromatic_of_not_failure`|root正式lake构建通过；日志`integration-first.log`记录Algorithm实际Built|
|归一化Bernoulli权与任意p的正关联|Bernoulli：Harris、多事件Harris、实际原边hit、Jensen|局部编译及独立导入／公理审计通过；`bernoulli/REPORT.md`、`build-final.log`、`audit.log`|
|真实初始单色边均值与残留概率|InitialAverage：`initial_monoCount_average`、`initial_power_average`、`initial_residual_average`|`initial-average/build05.log`与`audit.log` exit0；独立审计实际调用Algorithm的ResidualEvent|
|活跃点相对次序和阶乘比例|OrderCounting：`relativeEvent_ratio`、`beforeAfter_ratio`|`order-counting/BUILD.log`与`CALLER.log` exit0，实际全排列位置caller通过|
|有限双和与精确J积分|Integral：`beta_nat`、`orderSum_eq_jk`、`finite_order_sum_eq_jk`|`integral/build06.log`与`audit-final.log` exit0；完整有限和等式已闭合|
|17元数值预算|PilotEstimates：`pilot_estimate_actual E hm`|`pilot-estimates/build03.log`与`audit.log` exit0；p=1/17、m≤2^17自动由实际γ≤m²给严格小于1|
|实际有限联合样本与概率到染色|Sample、SampleLaw|显式jointweight非负、总和1、与实际sampleExpect相等，已包含正式PilotMain构建|
|任意有限V与Fin n的真实传递|Lift|原边数、γ、uniformity及实际染色拉回已接至一般P/C和Pilot|
|单交原边对精确概率|PairProbability：sampleProb_pairEvent|任意k≥1、实际单交边对及指定色的精确J/2^(2k−1)公式；正式构建及独立caller通过|
|完整实际失败上界与充分判据|UnionBound、ProbabilityBound|rs_recoloring_failure_le、propertyB_of_rs_bound已正式构建，无外供概率／覆盖／证书假设|
|17元原命题与原题审计|PilotMain；根ReviewAuditGeneralRSPilot.lean|指定lake build成功2538jobs；独立裸Finite/≤131072原Bool染色与一般criterion均exit0；7项公理均标准三项，见final-*-result.json与final-audit.log|
|指定新编码终审与HTML|reviews/C；REPORT及离线页|Grok end_turn、Gemini SUCCESS均已接受，root已处置；最终HTML离线桌面／手机及fresh保真均PASS，零阻塞零警告|


已完成的各模块审计只使用 `propext`、`Classical.choice`、`Quot.sound`，没有将未证概率界或证书作为新增公理。独立import及caller属于本机核验，不表示第二台机器复现。源码编译、数学语义审阅和最终阶段验收分别记录。

## 新编码审阅

Checkpoint A的Grok/Gemini均有效完成，对固定Definitions/Algorithm快照作独立反译；目标量词、初始颜色触发、有向γ及排列时刻约定一致。确切型号、完成状态、读取范围和主代理处置见 `reviews/A/DISPOSITION.md`，两家均未执行Lean。快照当时缺少完整失败覆盖，后续补齐不借A意见自动扩scope。

B1 Grok原生completed/end_turn已恢复，在Algorithm/Sample实际范围确认一致，未执行Lean。Gemini B1未恢复，不记通过；准确处置见reviews/B1/DISPOSITION.md。Grok/Gemini最终C均有效完成，明确覆盖最终P/C/Pilot、全部关键有限计数／概率连接、正式构建和根审计。root完整读取并接受，无需源码修改；准确身份、静态读取范围及未执行Lean的边界见reviews/C/DISPOSITION.md。Gemini原调用正常返回、零retry，不追记缺失B1。

## 恢复顺序

先读本页及final-build-result.json、final-audit-result.json。数学链已经编译闭合，指定终审已经完成，REPORT和FUTURE_FORMALIZATION已生成最终离线页；最终fresh保真和五项阶段验收均PASS；阶段结束，下一步由用户决定，完整增长定理范围见FUTURE_FORMALIZATION.md。不要重新求解已验接口或恢复旧35/36。

环境保持Lean4.24.0和既有Mathlib锁定版本。root统一管理共享依赖和正式模块构建，各worker只局部编译自身模块，不并发全工程重编。先前共享缓存缺口已按明确模块补齐；不据历史缺缓存记录重复准备或升级依赖。

启动时的“各模块实施中、失败覆盖未完成、尚无新编码审阅”是本页此前快照，现由上表与A处置替代；准备资料仍保留在 `PREPARATION.md`。完整一般纸面claim `propertyb-general-growing-integer-gain`保持verified（无端到端一般Lean声明），本阶段只登记局部证明experiment，不擅自升级全阶段claim。
