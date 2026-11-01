# Gemini 4 设计讨论：处置与准确范围

2026-11-01。使用 ARIS `research-review`，用户指定 Gemini 4。

两轮均经 Antigravity MCP 实际完成。返回模型 `gemini-4-argon-high`，CLI 选择 `Gemini 4 Argon (High)`，effort `high`、来源 `cli_selected_model_variant`；状态均为 `SUCCESS`。原生线程 `975a38ef-7cd2-4ec5-b539-fe67999bc403`。这是跨模型家族的架构讨论与设计修订；没有执行程序、证明新数学命题或实测效率。模型标识来自桥接返回的 CLI 记录。

## 阅读与记录

- 第一轮：[请求](GEMINI_REQUEST.md)、[完整回复](GEMINI_ROUND1.md)、[原始返回](GEMINI_ROUND1.raw.json)。输入为 [BRIEF.md](BRIEF.md) 与 [EVIDENCE_NOTES.md](EVIDENCE_NOTES.md)。
- 第二轮：[针对性纠正](GEMINI_ROUND2_REQUEST.md)、[完整回复](GEMINI_ROUND2.md)、[原始返回](GEMINI_ROUND2.raw.json)。
- 第一轮回复报告读取底稿／札记、研究经验／失败地图、m6与m8/m9沉淀、Lean工作流及harness总结共八份文件。没有要求其执行计算或审计现有数学结论。
- 主代理另读相关原始经验页并以 Python Fraction 核对错误示例，实际结果为 `49/1989`。

## 采纳的建议

1. base、领域插件、单题工作区分层；本轮核心与验收保持稳定，改进提案另行评估后纳入后续版本。
2. 插件必须传递瓶颈原因与下一步决策依据，而非只报告总分；允许符号性瓶颈与未知松弛量。
3. 停滞时恢复同一原对象的共同约束，检查上游选点／归约是否能排除坏型，再决定是否扩大计算。
4. 探索与核验分开描述范围；早做实际输入连接，有明确新信息时允许持续攻关。
5. 复用 ARIS 与现有 wiki／脚本，先检验工作流机制，之后才评价跨任务效率与 RSI。

## 纠正与未采纳

- **首轮示例错误。** Gemini 自行补入 `C_raw=45/221` 和“已扫描380/380”，所引材料没有这些运行事实。示例给出的数字实际使总界下降 `49/1989>0`，与其写的0矛盾。第二轮已明确撤回。原始回复保留；成稿只引用真实失败地图或明确标作示意的非数值接口。
- **首轮止损规则过强。** “只有三种计算合法”“未接 caller 的计算一律无效”“每轮必须排除失败见证”会阻碍探索。第二轮接受修订为有界探索、记录新增信息、触发重新决策。未把过强禁令写入成稿。
- **证据不是单一等级。** 独立算术、覆盖证明、模型审阅与 Lean／原题对齐各检查不同属性。第二轮接受此纠正；标准三公理不能单独判定原命题被证明。
- **没有统一数值评分要求。** slack 适合本领域部分界；一般证明可报告符号性缺口或尚不清楚的障碍。没有“所有数学任务必然组合爆炸”的断言。
- **技能来源纠正。** 首轮 `.gemini/config/skills/...` 不是本机 Codex 规范入口；第二轮又建议引用项目旧 `aris-skill-drafts/lean-formalize`，仍不采纳。正确本机入口为 `/Users/rfy_naiveai/.codex/skills/lean-formalize/SKILL.md`；上游源为 `/Users/rfy_naiveai/Desktop/aris_main/skills/skills-codex/lean-formalize/SKILL.md`。旧草案只保留历史。
- **不自动执行 meta 技能。** 可以借鉴提案与合入分离；本轮没有调用 `meta-optimize`／`meta-apply`，没有启动其审批、修改或发布过程。成稿也未硬编码“一轮必诊断成功”或“下一任务前必须合入”等未经实测要求。

## 结论与边界

Gemini 支持总体架构，并在第二轮接受所提出的关键纠正。成稿 [MATH_RSI_DESIGN.md](../../MATH_RSI_DESIGN.md) 由主代理核对来源后整合，已收录有效接口建议和局部退回全局的机制；没有再把未改变的全文重复送审。

首轮记录为需修订，第二轮记录为修订后的设计原则获得跨家族支持。后者不代表新 harness 已实现、效率已验证或全文每个历史事实被 Gemini 独立复算。旧35 Lean／36研究继续暂停，未建立新 Goal，不操作 v2。
