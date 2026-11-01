### 四、Memory Update（本轮已解决 vs 仍关切）

- **已解决（可结案）**：
  1. **父子双重调度风险**：9 个技能与 [`docs/WORKFLOWS.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/WORKFLOWS.md#L7) 已统一“同级阶段只由唯一父调度者启动，子技能只返回产物与 next 建议”。
  2. **autoreview 过薄问题**：[`mathrsi-route-loop/SKILL.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-route-loop/SKILL.md#L24-L111) 已完整恢复 `Phase A–E`、`research-review — composed`、逐 reviewer memory 与断点恢复，并去掉了 ML 分数真值门。
  3. **相对路径与领域插件接入**：[`mathrsi-research/SKILL.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-research/SKILL.md#L159-L161) 链接层级已修；[`mathrsi-survey/SKILL.md`](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-survey/SKILL.md#L52-L74) 已落出 `propertyb-literature` 具体调用块。
- **本轮仍关切（补齐即彻底就绪）**：
  1. `prove` §1→§2 缺“先在 `PROOF_DRAFT.md` 写 caller 桩、再生成 `STATEMENT.md`/`CONTEXT.md` 调 `proof-writer`”的衔接动作；
  2. `specify`/`survey` 需写明“3 条检索轴 + 2–5 篇核心原文收敛精读 + 已核进口/待证连接二分”；
  3. `verify` §2 需明确局部 `research-review` slot 与 §3 `proof-checker` 的互斥边界；`handoff` §3 需明确把完整证明正文内联后再渲染 `PROOF.html`。



## 仓内桥接续接复核（原文追加）

### Memory update

- **已解决（全部关闭）**：
  1. `mathrsi-prove` 从 `ROUTE_REPORT` 到现稿原对象 $H$ caller 桩及作者委派输入的落地衔接（[`mathrsi-prove/SKILL.md` L24, L42](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-prove/SKILL.md#L42)）；
  2. `mathrsi-specify` 三方向检索面提取、文献 $A \Rightarrow B$ 与原对象 $H \Rightarrow A$ 分离（[`mathrsi-specify/SKILL.md` L72, L93](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-specify/SKILL.md#L72)），以及 `mathrsi-survey` 按关键依赖触发原文深读与停止泛搜（[`mathrsi-survey/SKILL.md` L130](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-survey/SKILL.md#L130)）；
  3. `mathrsi-verify` §1 确定性核验、§2 有界 `research-review` slot（含同轮证据澄清）与 §3 `proof-checker` 的默认分流与职责边界（[`mathrsi-verify/SKILL.md` L81, L87](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-verify/SKILL.md#L81)）；
  4. `mathrsi-handoff` 完整证明内联渲染与 `TeX` canonical 派生阅读稿边界（[`mathrsi-handoff/SKILL.md` L55](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-handoff/SKILL.md#L55)）；
  5. `mathrsi-route-loop` 对 `research-review` Step 3/4 的显式数学适配、Phase D 续接 prompt 及有效 D 直接转下一轮 C（[`mathrsi-route-loop/SKILL.md` L48–53, L94–105](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-route-loop/SKILL.md#L94-L105)）；
  6. `mathrsi-research` 子阶段返回短回执示例（[`mathrsi-research/SKILL.md` L71](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-research/SKILL.md#L71)）与 `mathrsi-assemble` 有限命题证据映射（[`mathrsi-assemble/SKILL.md` L47](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-assemble/SKILL.md#L47)）。
- **仍开放 / 新疑点**：
  - **无**。当前 9 个 `mathrsi-*` 技能及配套工作流文档的静态执行清晰度已满足闭环要求，可直接投入验收。

