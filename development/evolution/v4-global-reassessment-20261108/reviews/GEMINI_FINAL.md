### 实际阅读范围

已读取工作树当前实际文件：
- [`base/skills/mathrsi-research/references/global-reassessment.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-research/references/global-reassessment.md)（全文 1–105 行）
- [`base/skills/mathrsi-research/SKILL.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-research/SKILL.md)（全文 1–207 行，重点核对新增 `## 全局进展` 段 L51–58 及 `## 3` L149）
- [`base/skills/mathrsi-prove/SKILL.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-prove/SKILL.md)（L150–245，重点核对 `§4` L158 与 `§5` L205–207）
- [`base/skills/mathrsi-verify/SKILL.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-verify/SKILL.md)（L80–193，重点核对 `§5` L157–159、L167）
- [`base/skills/mathrsi-route-loop/SKILL.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-route-loop/SKILL.md)（L1–165，核对 `§Phase C` L118 与 `§Phase D` L143 对齐情况）
- [`docs/V4_CHANGES.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/V4_CHANGES.md)（全文 1–47 行，重点核对 `Subsequent v4 maintenance on main` L5–12）

---

### 逐项核查结论与最小修正建议

#### 1. 规约有效但无益是否还能轻易绕过？（总体成立，仅需补 2 处半句堵死“自产自销子义务”与“新规约充当新方法”）
- **已就位部分**：[`global-reassessment.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-research/references/global-reassessment.md#L5) L5、L19、L27、L66 已明确区分“规约成立”与“规约有用”，要求核算 `原对象数 × 每对象后继扩张`、生成/运输/存储/读回/独核/回接总成本，并规定同一原题瓶颈连续两批无决策增量或默认三批到达检查点即强制启动两位只读评估者。
- **仍可被绕过的真实漏洞与最小修正**：
  1. **防“新规约自生引理”冒充必要子义务闭合**：[`global-reassessment.md` L21](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-research/references/global-reassessment.md#L21) 写有“闭合一项真实必要子义务也有价值”。陷入局部规约的 agent 极易把**新规约自身引入的内部转换/格式桥接引理**报为“闭合了必要子义务”，从而每批都算有进展。
     - **最小修正（[`global-reassessment.md` L21](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-research/references/global-reassessment.md#L21)）**：将“应说明它处在完整闭合路径上，避免用不断新生的外围义务替代主瓶颈”收紧为：
       > “应说明它消去了**规约前原完成路径上既有的必要条件**或严格缩小了原题剩余联合域；**仅闭合新规约自身派生的内部转换或包装引理，不计为原题决策增量**。”
  2. **防“每轮换一个等价规约”重置单次有界展期**：[`global-reassessment.md` L87](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-research/references/global-reassessment.md#L87) 规定“同一未变方法、同一证据下只允许一次重评后的有界探针续行”。若 agent 把每次等价改写/新规约辩称为“换了新方法”，就能绕过“只准一次展期”。
     - **最小修正（[`global-reassessment.md` L87](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-research/references/global-reassessment.md#L87)）**：在“改名、增模型、换参数碎片不构成改法。”后补半句：
       > “**未改变原题关键未闭连接与后继联合规模的等价新规约，也不构成新方法或新证据。**”

#### 2. 是否误停必要计算？（直接通过，无需修改）
- [`global-reassessment.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-research/references/global-reassessment.md#L29-L37) L29、L31、L37、L89 与 [`mathrsi-prove/SKILL.md` L207](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-prove/SKILL.md#L207)、[`mathrsi-verify/SKILL.md` L157](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-verify/SKILL.md#L157) 已完整保护两类情形：（1）已核清无损归约、覆盖、有限域和端到端吞吐的完整计算计划，分块推进不重复触发两批/三批重评；（2）在途不可分有效计算安全完成或留断点，不按“停滞”直接杀进程。

#### 3. 作者 / dispatcher / checker 是否有冲突？（总体清晰，仅 `prove` §5 建议补半句优先级）
- **已就位部分**：评估者严格限定为一轮只读、不改源文件、不启后继阶段（[`global-reassessment.md` L69–73](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-research/references/global-reassessment.md#L69-L73)）；`verify` 明确只在 `proof-checker` 合同允许的安全返回点请求重判，不抢内部修复/复审调度、不插入并行写者（[`mathrsi-verify/SKILL.md` L159](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-verify/SKILL.md#L159)）；各阶段均沿直接 caller 上报唯一 dispatcher。
- **最小修正（[`mathrsi-prove/SKILL.md` §5 L205–207](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-prove/SKILL.md#L205-L207)）**：L205 允许 `prove` 遇无增益等式或需换表示时直接“回调 `mathrsi-route-loop`”，而 L207 要求两批无增量时“通过直接 caller 交唯一研究调度者”请求两位独立评估者。为防 `prove` 协调者在触发 L207 时自行先跑内层 `route-loop` 绕过独立双盲重评，建议在 L207 句中补半句：
  > “达到本条全局重评触发条件时，**直接回交唯一研究调度者启动两位独立评估者，不由本 prove 先行自启内层 route-loop 替代全局重评**。”

#### 4. 是否可执行与版本记录对齐？（直接通过）
- 派工模板、宿主原生 `spawn_agent` / `followup_task` / `REVIEWER_MCP` 调用边界、五类决定的紧接动作表、外部 reviewer 不可用时的 native 独立会话降级与“不自动解禁昂贵旧路线扩批”均具体可执行。
- [`docs/V4_CHANGES.md` L5–12](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/V4_CHANGES.md#L5-L12) 对 `main` 后续维护与固定 `v4` tag 的边界、技能数与不宣称测速表述准确无误。
