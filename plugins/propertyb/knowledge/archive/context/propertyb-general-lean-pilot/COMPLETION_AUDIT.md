# 一般 RS Lean 阶段验收核对

**结论：PASS，本阶段五项验收全部满足。** 一般RS概率核心与17元完整调用已通过本机指定构建、原命题独立导入和公理审计；Grok/Gemini最终C有效接受，最终离线HTML及fresh保真审计通过。完整一般增长整数增益定理的Lean仍留待另行启动。

最初源码核对：2026-10-21 05:15:55 UTC；root完成最终证据验收：2026-10-21T05:35:09.491339+00:00。范围为[阶段 Goal](../../GOAL_PROPERTYB_GENERAL_LEAN_PILOT.md) §2、§4、§7、§8、§10。此次核对读取实际定义、最终证明源码、正式构建及审计日志；未重新构建，未发起模型调用。解释性核对属于 same-family／provisional；Lean 检查记录和跨家族审阅分别列示。

## Goal §10 五项

|要求|状态|实际证据与范围|
|---|---|---|
|1. 从真实算法证明一般 P 和原染色判据 C|PASS|`rs_recoloring_failure_le` 与 `propertyB_of_rs_bound`，见下方逐项反译；概率界、覆盖、正关联和单交计数均已在证明内部连接。|
|2. 任意有限 17 元、≤2^17 边的完整 Pilot，经同一 RS 判据调用|PASS|`propertyB_seventeen_of_at_most_two_pow : PilotTarget`；证明直接调用 `propertyB_of_rs_bound` 和 `pilot_estimate_actual`。裸原题 caller 同样通过。|
|3. 指定模块构建、独立原题导入、实际类型及传递公理审计|PASS|正式 `lake build Aris4Math.General.RS.PilotMain` 成功；构建后运行 `formal/ReviewAuditGeneralRSPilot.lean` exit 0；七项公理均为标准三项。|
|4. Grok 与 Gemini 对本阶段新编码和最终导出的有效审阅及处置|PASS|两家最终C均有效接受P/C/Pilot，root已全文核读并处置，无需源码修改。Grok返回grok-4.7-build/xhigh/end_turn，Gemini返回gemini-4-argon-high/high/SUCCESS；均静态读取而未执行Lean。原回应与精确范围见`reviews/C/DISPOSITION.md/json`。缺失Gemini B1不追记，最终C实际覆盖全部相应连接。|
|5. 可复现交接、简洁 HTML、实测成本及完整增长定理剩余工作|PASS|`REPORT.md`含完整复现与实测成本；`FUTURE_FORMALIZATION.md`列真实剩余及不可可靠估时部分。最终HTML包含两份完整正文，11个内嵌SVG公式、6张表，离线桌面／手机均通过；fresh保真PASS、零阻塞零警告（same-family/provisional）。|

## 三个主导出的独立反译

**P：** [ProbabilityBound.lean](../../formal/Aris4Math/General/RS/ProbabilityBound.lean) 的 `rs_recoloring_failure_le` 量化任意类型 `V` 和裸 `[Finite V]`、实际 `E : Finset (Finset V)`、整数 `k≥2`、所有原边恰有 k 点，以及 `0<p≤1`。结论恰为

\[
\operatorname{rsFailureProbability}(E,p)
\le 1-[1-(1-p)^k]^{|E|/2^{k-1}}
+\frac{\gamma(E)}{(2^{k-1})^2}\int_0^p(1-y^2)^{k-1}\,dy.
\]

`rsFailureProbability` 用 `Fintype.ofFinite V` 与顶点等价 `Fintype.equivFin V` 重标号同一 E，再调用实际 `failureProb`；`failureProb` 是同一样本上的 `Failure E` 指示函数期望。`Failure` 明确定义为该 RS 算法的 `finalColor` 在某条实际原边上单色。`gamma E` 明确定义为 `(E×E)` 中不同且交集基数为 1 的**有向**原边对数。`Lift.singlePairs_relabel`、`gamma_relabel` 与 `relabel_card` 证明这里的 m、γ 就是原始 E 的数，不是外部替代参数。

**C：** `propertyB_of_rs_bound` 的前提仅为同一原始对象条件和上式显式右侧严格小于 1。结论展开是存在 `V→Bool` 的总染色，使每条原边分别有 true 与 false 见证。数值不等式是 Goal 允许的充分条件；失败概率界、事件覆盖、独立性、正关联、计数公式及算法成功性没有留作额外前提。证明先使用已证 P，再从实际成功样本取得 `finalColor` 并沿同一顶点等价拉回。

**Pilot：** [PilotMain.lean](../../formal/Aris4Math/General/RS/PilotMain.lean) 的主类型展开为：任意 `[Finite V]` 及简单边族 E，只要每条边 17 点且 `E.card≤2^17`，就存在上述两色染色。没有概率、内部证书、点数、度数或点对覆盖前提。`formal/ReviewAuditGeneralRSPilot.lean` 另以 `E.card≤131072` 和显式两色见证复述原题并实际调用该主定理。数值证明取 p=1/17，使用已证 a>1/2、J≤1/17、m/d≤2 和实际 γ≤m²，得负项>1/4、正项≤4/17<1/4；该较粗 pair bound 已有足够严格余量，空边族也在同一调用域内。Goal 所写 m(m−1) 是可选估计，不需要为验收额外补用它。

## 原始样本与证明连接

[Definitions.lean](../../formal/Aris4Math/General/RS/Definitions.lean) 用有限集合表示互异边；不添加正则性、点对覆盖或点数限制。[Algorithm.lean](../../formal/Aris4Math/General/RS/Algorithm.lean) 按 `σ.symm t` 扫描，故 σ 是顶点到处理时刻。翻转要求资格位 true，并存在**初态**单色且尚无点翻转的实际触发边；没有换成“当前单色就翻”。`finalColor` 仅按实际翻转集合取反。

[SampleLaw.lean](../../formal/Aris4Math/General/RS/SampleLaw.lean) 明确给出共同联合权

\[
w_p(c,b,\sigma)=\frac{w_{1/2}(c)\,w_p(b)}{|\operatorname{Perm}(\mathrm{Fin}\,n)|}.
\]

这里各 Bernoulli 权为逐点乘积；`sampleWeight_nonneg` 给 0≤p≤1 时非负，`sum_sampleWeight` 给共同样本总权 1，`sampleExpect_eq_sum` 证明实际 `sampleExpect` 就是这个联合权的有限和。主入口已导入此模块。

|关键义务|已接入的实际声明与数学内容|
|---|---|
|完整失败覆盖|`Algorithm.failure_covered`、`UnionBound.failure_covered_singlePairs`：实际失败属于残留事件或某个真实有向单交原边对及颜色。|
|重叠边正关联与指数项|`bernoulli_harris`、`bernoulliProb_all_edges_hit`、`initial_monoCount_average`、`initial_power_average`、`initial_residual_average`：任意 p 的乘积权、实际初始单色边均值及 Jensen，不把边事件假设为独立。|
|相对次序与精确积分|`beforeAfter_ratio` 对任意不交 A、B 和枢轴计实际全排列比例；`beta_nat`、`jk_rescale` 以及 `sampleProb_pairEvent` 把同一实际事件接到 J。没有排列／超图枚举作为证明。|
|有向／颜色因子及并界|`pair_probability_sum` 对实际 `singlePairs E` 和两个 Bool 颜色求和，系数正好 γ/d²；`rs_union_bound` 接回同一 `failureProb`。|
|任意有限 V 与原染色|`Lift` 保持边数、uniformity、真实单交对及 γ，`propertyB_relabel_iff` 拉回成功染色；最终 P/C/Pilot 已消去传递接口前提。|

## 正式验证与可复现证据

固定环境为 `formal/lean-toolchain` 的 Lean 4.24.0 和既有 `formal/lake-manifest.json`；本核对未更换依赖。

- [final-build-result.json](final-build-result.json) 记录指定 `lake build Aris4Math.General.RS.PilotMain` exit 0；[首次正式日志](final-build.log) 与[确认日志](final-build-confirm.log) 均显示 `Build completed successfully (2538 jobs)`。这是包含缓存／依赖的 Lake 任务数，不是成果数或完成比例。
- [final-audit-result.json](final-audit-result.json) 和 [final-audit.log](final-audit.log) 记录**正式构建后**独立导入 exit 0；[审计源码](../../formal/ReviewAuditGeneralRSPilot.lean) 打印实际定义、P/C/Pilot 类型，并以原始词汇写出 Pilot 与一般积分判据 caller。
- 七项被审计声明分别为 `sum_sampleWeight`、`sampleWeight_nonneg`、P、C、Pilot、`GeneralRSPilotAudit.original_seventeen_statement`、`GeneralRSPilotAudit.general_rs_criterion`；其传递公理全部恰为 `propext`、`Classical.choice`、`Quot.sound`。
- 本次实际执行 `rg` 扫描 `formal/Aris4Math/General/RS/` 和根独立审计源码中的 `sorry`、新增 `axiom/constant` 声明及 `native_decide`，exit 1 且零匹配。传递公理记录另直接确认最终链无 `sorryAx`。不将旧探索日志中的失败当作已验入口内容。

从项目根设置项目本地 `ELAN_HOME` 和 PATH 后，进入 `formal/` 执行：

```sh
lake build Aris4Math.General.RS.PilotMain
lake env lean ReviewAuditGeneralRSPilot.lean
```

[REPORT.md](REPORT.md) 提供完整环境命令与实测成本；[FUTURE_FORMALIZATION.md](FUTURE_FORMALIZATION.md) 提供后续最小反例、实际单交图／团界、一般参数／log／floor 和 B_RS 最大预算的剩余接口及建议。这里记录的是本机正式构建和独立原题调用，未声称第二台机器复现。

## 最终审阅与展示证据

- [两家终审处置](reviews/C/DISPOSITION.md)及同目录原始请求、两份RAW与RESPONSE记录保存了准确模型、结束状态、读取范围和主代理处置。审阅者没有运行Lean；实际内核证据来自上述本机构建。
- [最终HTML](../../PROPERTY_B_GENERAL_LEAN_PILOT.html)内联阶段报告及后续范围，离线桌面1440×1000与手机390×844均通过；数学内容和顺序、全部链接与页面滚动均已核对。
- [fresh展示审计](../../PROPERTY_B_GENERAL_LEAN_PILOT.html.review.json)为PASS、零阻塞零警告，属于same-family/provisional的呈现审计，不替代数学审阅。截图、确定性浏览器检查和原审计在`.aris/traces/render-html/2026-10-21_general-lean-pilot_final/`。root另实际查看最终桌面顶部与手机概率段。

本阶段没有剩余数学或交付义务；导航和wiki已同步，Goal工具已实际返回status=complete，回执见GOAL_COMPLETION.json。**完整k≥17增长整数增益定理尚未形式化，不属于本阶段已完成范围。** 下一阶段不自动启动；旧35／36继续暂停，v2保持隔离。
