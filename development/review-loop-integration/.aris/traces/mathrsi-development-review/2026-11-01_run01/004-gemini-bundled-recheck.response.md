### 六项修订逐条复核结论

本轮已直接静态读取 8 份修订后的 `SKILL.md` 对应段落，上轮提出的全部具体执行缺口均已妥善解决，且避免了机械配额与冗余文件：

1. **`mathrsi-prove` 先写主干 caller 再派发（已解决）**
   - 见 [`mathrsi-prove/SKILL.md` L24](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-prove/SKILL.md#L24) 与 [§2 L42](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-prove/SKILL.md#L42)：已明确要求发出调用前先在现用草稿落下“任取原对象 $H$ 已知性质 → 引理 $L$ 所需输入 → 拿到 $L$ 后推出当前结论”的真实 caller 并标明未证箭头，再从中抽出声明与允许进口（可直接放委派消息或沿用已有 `STATEMENT.md`/上下文文件，不强制新造双文件），回收后立即代回原 caller 核对新增前提。

2. **`specify` 三检索方向与进口二分 ＆ `survey` 依赖导向转深读（已解决）**
   - 见 [`mathrsi-specify/SKILL.md` §2 L72](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-specify/SKILL.md#L72) 与 [§3 L93](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-specify/SKILL.md#L93)：已补齐按需从“对象异名/等价表述、当前或近邻参数结论/反例、候选工具原证明条件”提取检索面，并在定稿时严格拆开“文献在 $A$ 下证 $B$”与“原输入 $H$ 是否满足 $A$（及首个待证连接与 caller 位置）”。
   - 见 [`mathrsi-survey/SKILL.md` §3 L130](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-survey/SKILL.md#L130)：已改为发现决定基线、关键工具或疑似反例的来源即转入 §4 深读，并在重复结果增加且关键依赖已有来源时停止扩泛词；不设死板的“1–2 轮 / 2–5 篇”配额，防止漏掉关键来源或为凑数空转。

3. **`verify` §2 默认分流与证据职责边界（已解决）**
   - 见 [`mathrsi-verify/SKILL.md` §2 L81](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-verify/SKILL.md#L81) 与 [L87](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-verify/SKILL.md#L87)：已写明算术/固定证书走 §1 确定性核验（同時保留分类完整性与原对象连接的数学论证义务）、推进中局部归约疑问走有界 `research-review` slot（显式保留原件审阅与同会话证据澄清/反驳）、完整候选或自足局部定理直入 §3 `proof-checker` 而不重复跑 `research-review`，既消除机械叠加，又保留不同义务组合多证据的灵活性。

4. **`handoff` §3 正文内联阅读输入与 TeX 派生关系（已解决）**
   - 见 [`mathrsi-handoff/SKILL.md` §3 L55](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-handoff/SKILL.md#L55) 与 [L67](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-handoff/SKILL.md#L67)：已明确完整证明阅读页的渲染输入必须包含定义、引理和证明正文（不拿摘要 `HANDOFF` 当证明页渲染），且允许以 ` PROOF.tex` 为唯一 canonical 正文时派生忠实阅读稿而不另立第二份可改数学的正文；配合原 §4（现 [L71–98](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-handoff/SKILL.md#L71-L98)）的独立副本复算与打包说明，执行链条已完整。

5. **`route-loop` Phase D 续接模板、跨轮直转 C 与 RR Step 3/4 数学适配（已解决）**
   - 见 [`mathrsi-route-loop/SKILL.md` Phase A L48–53](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-route-loop/SKILL.md#L48-L53) 与 [Phase D L94–105](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-route-loop/SKILL.md#L94-L105)：已显式写出 `research-review` Step 3/4 的数学适配边界、Phase D 保存会话续接 prompt 模板，以及“当 Phase D 已明确下一轮具体实作问题与最低修法时，外层可直接作为下一轮 Phase C 输入消费，不就同一证据重发 Phase A”。

6. **`research` 阶段返回短答复示例 ＆ `assemble` 有限命题—证据映射（已解决）**
   - 见 [`mathrsi-research/SKILL.md` §1 L71](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-research/SKILL.md#L71) 与 [`mathrsi-assemble/SKILL.md` §1 L47](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-assemble/SKILL.md#L47)：已分别补入不建新文件的四要素接棒短答复示例，以及“单项旁注、多程序/多分支列对照表”的有限命题—脚本—输入域—证书映射要求。

---

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