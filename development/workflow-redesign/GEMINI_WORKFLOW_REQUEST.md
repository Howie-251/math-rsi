我们正在按用户要求重做MathRSI真正的多skill数学workflow，不是规则论文或复制技能目录。请实际读 /Users/rfy_naiveai/Desktop/aris_main/skills/skills-codex/idea-discovery/SKILL.md、skills/skills-codex/research-pipeline/SKILL.md、skills/skills-codex/auto-review-loop/SKILL.md、skills/skills-codex/proof-orchestrator/SKILL.md，以及 /Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-research/SKILL.md。只读，不编辑文件或启动研究。

用户重点：每个有意义阶段有实际技能；MathRSI技能将ARIS作为内部能力按数学适配，再组合为一键解决数学问题的强workflow；包括持续wiki、adversarial auto review loop、按需Lean、之前实际经验。不要简单克隆一份ML流水线或用review分数判断定理真伪。薄Python，不造状态机平台。Self-contained实现已有30ARIS技能双宿主和PropertyB完整知识库，保留它们。

拟新增6个实质数学阶段技能（请审视边界，不用为了数量加空壳）：
mathrsi-specify：初步问题/恢复，文献后固定精确FORMAL_SPEC；
mathrsi-survey：使用research-lit/wiki-enrich/research-wiki做异名、前后引用链、反例勘误、原文条件和方法图；
mathrsi-prove：选择路线、证明义务、formula-derivation/proof-writer、领域plugin具体方法/检查器、并行作者与立即整合，复杂跨run才proof-orchestrator；
mathrsi-review-loop：完整数学对抗loop，确定性检查＋research-review/proof-checker按阶段使用→保存原回应→具体修复→复跑受影响验证→复核；退出为当前义务闭合、反例、需新数学、预算或指定审阅未完成，各自返回正确父阶段；不照搬MLscore或固定GPU；
mathrsi-assemble：把已核引理接成原命题完整文稿，调用proof-writer/citation核查，发现实际输入断裂退prove；
mathrsi-handoff：可读完整证明、精确状态、复算、wiki/恢复、按需render-html/打包。
已有lean-formalize直接承担形式化阶段，无须空壳重命名。总控应有每阶段确切调用示例、传入实际文件、子技能落什么、Root读取何处决定下一步/回退/并行、默认同turn继续。已有状态优先恢复，不要求新建固定8文件或人为审批。

请作为实质共同作者，产出：(1) 最小合理阶段图与职责调整（如需要）；(2) 中文总控workflow的可落地完整草案，约1500–2500字，按实际阶段执行，以调用/传递/消费为主，约定另放reference；(3) 新mathrsi-review-loop最重要的完整回路和与ARIS原循环的精确区别。不要虚构运行结果、已做审阅或源码里没有的命令。ARIS源以SKILL正文为准，不以README旧摘要当行为。注意保留原题，非构造存在性也合法，不把所有问题变有限分类或默认Lean。
