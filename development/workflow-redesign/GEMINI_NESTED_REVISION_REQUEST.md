用户刚进一步澄清了架构，请据此修订，不再沿用上一答的单个mathrsi-review-loop包办一切：
主workflow下面是几组subworkflow，各自组合MathRSI技能＋ARIS适配。尤其"autoreview for求解路线"是独立子能力，主流程会串起来，求解途中也能回调；不是最终证明审计。
我们现按5组实现：
1 mathrsi-prepare：mathrsi-specify(初步/恢复)→mathrsi-survey(ARIS lit/wiki等)→specify定稿；
2 mathrsi-route-loop：真正循环改进求解方法，产出ROUTE_REPORT(方法、未证义务、探针、实际批评/修订、第一批具体任务)；
3 mathrsi-prove：formula-derivation/proof-writer、domain plugin、并行作者与精确检查，真去证明；困难路线回调route-loop；
4 mathrsi-verify：先按需mathrsi-assemble，独立算术/覆盖、完整proof-checker自己的修复回路，按需lean-formalize；局部实质缺口回prove，早期形式化可返回单义务证据，不机械跳最终交付；
5 mathrsi-handoff：完整可读证明、复算/按需HTML包、持续wiki和恢复。Wiki在每阶段实质进展就更新。
8个新技能（prepare/specify/survey/route-loop/prove/verify/assemble/handoff），其中有复合有叶，ARIS副本不改。

请重点实质共同编写 (a) route-loop内一轮的真实执行草案，及它如何与prove和verify接棒；(b) 主入口5阶段的简洁实际调用串；(c) 用一个已有失败证书→保留共同H约束→派出可执行引理任务的例子走一轮，别捏造新数学结果。
纠正上一答几处不采纳的限制：Root可以根据具体证据认定模型误读并保存反驳，不能让模型拥有数学真理否决权；只是不能改原审阅或伪造其PASS。局部轮次预算耗尽不自动暂停整个Goal；指定reviewer不可用也不妨碍其它独立工作。纯解析研究不强制先跑确定性checker；反例要区分原题反例、候选引理反例、必要松弛反模型。不要为流程新造强制JSON状态机、假想CLI flags、每步审批或按模型打分选择定理。
本轮请700–1400中文字的准确流程建议，避免重复制几千字原草案；确认这个嵌套分工是否合理，指出真实接口缺口即可。
