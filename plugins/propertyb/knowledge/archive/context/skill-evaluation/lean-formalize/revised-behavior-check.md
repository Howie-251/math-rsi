# 修订版 lean-formalize：四个情景的有限行为检查

结论：当前指令能正确处理这四个情景，未发现会改变执行结果的实质歧义。

| 情景 | 应有处理 | 当前指令是否足够 |
|---|---|---|
| 用户明确要求 Grok 与 Gemini；Grok 有效返回、Gemini 失败，Lean 已完整检查 | 分别报告「形式证明已检查」「Grok 实际审阅范围与发现」「Gemini 审阅待完成」。失败不否定已检查的定理，也不能用另一家意见代替 Gemini，或声称整个要求的流程完成。 | 足够。核心流程、§4、§5，以及 adversarial-review 的 Checkpoint C 与 Failure and continuation 均明确区分这两类交付。重试遵循当前授权与工具规则，不自行形成轮询。 |
| 原命题为 `∀ ε, ∃ N, P ε N`，已证明更强的 `∃ N, ∀ ε, P ε N` | 保留原命题作为基准；在相同对象域、参数及假设下提供从更强命题返回原目标的蕴含桥接，并检查原导出声明与桥接后的类型、公理。不能仅因量词顺序不同就误报证明错误，也不能省略原目标的连接。 | 足够。§1 明确允许更强结果经蕴含建立原命题；verification-and-handoff 的 Audit the statement 明确要求蕴含或等价桥接，而非字面语法相同。 |
| 原命题允许空对象 | 保留空对象，按原结论处理；不能为了消除所谓 vacuity 增添非空假设。只有编码意外排除了原任务允许的输入、或改变命题含义时，才应报告对应问题。 | 足够。§1 保留原始基准并要求区分原假设与新增性质；Checkpoint A 将声明域内的边界对象视为真实输入；Resolve objections 要求以具体数学理由拒绝无关限制。因此「检查 vacuity」不构成修改原任务的授权。 |
| 导出的是 `def proof : Target := ...`，而非 `theorem` | 检查实际类型和证明体：合法的 `def proof : Target` 可以提供 `Target` 的证明；`def Target : Prop := ...` 只定义命题。对证明项照常执行目标对应、编译及传递公理审计。 | 足够。§5 已明确判断命题是否有证明项，而非依据 `theorem`、`lemma`、`def` 关键字。 |

范围：只阅读 `SKILL.md`、`references/adversarial-review.md` 和 `references/verification-and-handoff.md`。未修改技能或数学主工程，未调用外部模型，未联网。本次不需要验证新的 Lean 语法，因此没有运行 Lean；上述结论是技能执行指令的行为检查，不是新增证明核验或外部审阅。
