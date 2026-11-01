# 核心规格审阅记录

对象：[FORMAL_SPEC.md](../../FORMAL_SPEC.md)。审查的是目标、定义、等价模型、初等有限约化及概率方法接口；不验收主定理 m(5)≥33、多锁定具体公式或 link 修正。

结果：v0.2的数学内容已获两家第3轮确认，发布为正式规格v1.0。原始主目标保持不变，theorem_status仍为unproved。

## 实际审阅渠道

| 渠道 | 返回的模型记录 | effort | 元数据边界 |
|---|---|---|---|
|Grok MCP|grok-4.7-build|xhigh|记录返回实际model/effort；请求型号为grok-4.7|
|Antigravity MCP|gemini-3.8-flash-high|high|CLI选择标签Gemini 3.8 Flash (High)，effortSource=cli_selected_model_variant；不宣称独立服务端身份认证|
|补充Codex子代理|same-family|本轮继承配置|仅作provisional补充，不替代用户指定的两家模型|

两家外部模型属于相对Codex的不同模型家族；这里使用用户明确指定的独立MCP讨论，不冒称已配置ARIS正式reviewer overlay。模型共识不是数学证明。

## 第1轮：独立读规格

- [Grok原始意见](grok_spec_r1.md) / [带提示词与元数据](grok_spec_r1.json)
- [Gemini原始意见](antigravity_spec_r1.md) / [带提示词与元数据](antigravity_spec_r1.json)
- [输入快照v0.1](spec_v0.1.md)

两家分别核对D1–D3、T、E1–E2、B0、R1–R4、F与M1–M3，均给出spec_coherence: coherent、theorem_status: unproved。Grok另核对本地Grill原文Theorem 1；Gemini逐项写出小v的精确概率。

## 第2轮：交叉核对与具体方向检验

- [Grok原始意见](grok_spec_r2.md) / [元数据](grok_spec_r2.json)
- [Gemini原始意见](antigravity_spec_r2.md) / [元数据](antigravity_spec_r2.json)

两家核对对方理由，并给出同一个有效反例说明“存在critical pair”不蕴含贪心失败：两条五元边只交于x，排列先放第一条边其余四点，再放x，再放第二条边其余四点。算法只把x染蓝，两边均合法。

**这一轮出现了共同错误，不能照单接受。** Grok写固定v下两个边数命题“不必等价”；Gemini进一步写“仅在允许全局顶点扩充时成立”。第二轮提问的措辞也带有这个暗示。它们把“新顶点上补入不交边”的某种构造不适用于固定v，误当作其他补边方式也不可能。原v0.1仅限制了那段构造，并没有断言两个固定v命题不等价。

本地直接核对：当v≥8时，候选五元边数至少C(8,5)=56，可以添加任意不同的缺失边到32条，不需不交；添加边保持非二染色。v≤7时所有五元超图都可染。故固定v的两个全称命题也等价。

## v0.2：消除歧义与不必要依赖

新增上述固定v补边的短证明。R1先保留m≤32及度和5m≤160；R2合并去重、R3上界和R4下界均成立，得到19≤v≤25；在原顶点集补边到32保持点对覆盖和不可染，直接证明F⇒T。因此有限约化无需B0。文献基准仍作为背景保留，T及后续LOCK接口不变。

这不是把未证目标证明出来，只是给有限任务提供更直接、依赖更少的等价约化。

## 第3轮：仅审查实质修订

输入快照：[v0.2](spec_v0.2.md)。

- [Grok第3轮](grok_spec_r3.md) / [元数据](grok_spec_r3.json)
- [Gemini第3轮](antigravity_spec_r3.md) / [元数据](antigravity_spec_r3.json)

两家均明确纠正第2轮固定v不等价的断言，独立说明补边保持不可染和点对覆盖，确认无B0的有限约化及LOCK接口成立，给出spec_coherence: coherent、theorem_status: unproved。v1.0仅更新状态与审阅链接，数学内容保持已确认版本。

Gemini第3轮关于小v写了“总点数<5+5，任意五元超图二染色均无单色边”，该措辞不被采纳：v=9完全五元图已反驳前一个泛化，而全红染色反驳“任意染色合法”。规范一直使用正确的存在性论证：v≤7时选择两个大小至多4的色类。Gemini已在 [单项措辞更正](antigravity_spec_r4.md)（[元数据](antigravity_spec_r4.json)）明确撤回该句，采用规范中的存在性论证；这不要求修改规格。所有本轮规格异议及上述审阅措辞问题均已处置。

## 记录口径

快照中的相对路径沿用项目根目录语境。原始模型回答保持原样；它们的错误在本文记录处置，不回写成模型从未犯错。失败的早期Antigravity方法讨论调用不是成功审阅；后续规格审阅已真实成功，两个任务分开计数。
