请与我讨论MathRSI workflow架构并给实质方案，只读设计审阅，不执行研究/不编辑。用户纠正：当前MathRSI master基本是研究规则，而不是真正ARIS式skill编排。更关键，"autoreview for求解路线"应是mathrsi base的一个subworkflow，由主数学求解workflow串起来，不只是最后proof-checker，不要把路线改进和证明真伪验收混成同一门。

请读 /Users/rfy_naiveai/Desktop/aris_main/skills/skills-codex/{idea-discovery,research-refine-pipeline,auto-review-loop,proof-checker}/SKILL.md（实际文件逐个），以及 /Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-research/SKILL.md、docs/ARIS_REUSE.md。主目录cwd Desktop可读取这两仓。源以实际SKILL为准，不以README概述为准。MathRSI已自包含30ARIS双端技能与详细PropertyB知识插件，用户不接受仅复制ARIS技能或再堆一层名字；MathRSI的阶段skills要以ARIS作为内部动作，加数学对应的执行过程与回流。

请明确设计：
1. 主workflow从用户定理/新问题/续接进入，何时调用子workflow、真实输入输出、怎样同turn推进；
2. 一个独立可调用的mathrsi-route-loop：提出几条足以解决同一义务的路线→Grok/Gemini挑战关键归约/适用性/端到端成本→便宜数学探针/反例/小实现→修路线或换表示→有限再评审→交一个可执行求解计划。给完整循环、终点与产物、何时从求解中回流。路线可以缺未证引理，但不可用评分或模型同意冒充主定理；
3. 路线loop与证明实现、mathrsi的确定性核验/对抗证明审阅、proof-checker现有repair loop、Lean、wiki如何衔接而不互相递归/重复审一遍；
4. 哪些应成为有实际职责的新MathRSI skills，哪些直接复用已有ARIS技能，不每个动词造空壳。用户坚持详细可执行、薄Python、自主推理、HERO；主脑负责全局，Sol承担可核验工作。
请给可实施的分层/阶段图、一个从真实路线受挫到重新交付下一数学任务的具体例子（可用PropertyB，共享同一H约束但不要重新算旧题），以及当前设计容易误解之处。约1500–2500中文字，准确标实际读取范围。不要制造Hash/评分平台或申请额外授权。
