# ARIS实际编排阅读与本轮采用

本轮以本机ARIS固定源`c485faa59a68e51c6575dea67ca57abc7a6a2b9c`和本仓相同字节副本为准；也打开了用户指定的公开仓库确认主入口。阅读由Root与三名Sol分工完成，不宣称Root逐字读遍整个上游所有技能。

Root读完整Codex idea-discovery、AGENT_GUIDE、贡献约定和output-composition，查看实际proof-checker入口与当前适配；三份分工底稿记录其完整原文范围：[pipeline](ARIS_PIPELINE_WORKFLOWS.md)、[proof](ARIS_PROOF_WORKFLOWS.md)、[other workflows](ARIS_OTHER_WORKFLOWS.md)。本轮包含主编排、选题/方法细化、实验桥接/审阅、论文与其它组合流程，以及proof/writer/checker/Lean/wiki的相关合同；未使用的全部技能不需为了篇数通读。

## 从ARIS保留什么

W1的关键是实际传产物：research-lit输出进入idea报告，候选交查新和review，再把选择交refine，后者产生FINAL_PROPOSAL及EXPERIMENT_PLAN等真实材料。父级读取这些内容再继续，同一轮AUTO_PROCEED不等用户再次说继续；技能名清单与一句箭头链不等于执行。

组合输出必须显式声明。支持composed的child返回独有正文，由指定writer合入；磁盘有报告不自动进入composed模式。原始review不因合并正文而删除。上游未支持的flag不虚构。任务恢复读实际产物和状态，而非把旧“运行中”当事实。

审阅原文、输入范围、实际路由和修复结果是可消费产物。路线提出以后要实际推导/试探，带新证据回到原疑问，不靠重复询问得到一致。证明checker已有完整source-unit、义务审计和修复回路，caller应调用并消费真实结果，而非自造同名PASS。

## 数学适配怎样落实

主流程改为五子工作流。prepare将初步题目、广搜和定稿接起来；route-loop拥有数学路线的独立对抗迭代；prove实际推导/执行并接caller；verify调用assemble/领域独核/proof-checker/按需Lean；handoff接真实结论及证据。八个新增入口分别有可独立执行的职责，ARIS原能力保持完整且不改字节。

ML中的GPU pilot、训练健康、经验分数和投稿ready门不迁作数学真值门。route-loop复用取证、backend、trace和review-fix机制，明确是数学适配的单slot，不宣称执行了完整原ML auto-review-loop。最终proof-checker仍按它自己完整合同执行，不在外层再套共识循环。

宿主差异按真实源码保留：当前proof-checker主线Phase3复用thread，Codex镜像fresh；部分flag只在主线；Markdown不能直接假设有完整TeX theorem inventory。新verify reference给无损转写/原稿对应及修复回写动作，真实audit不被caller伪造。

## 经验支撑

[六条实际项目转折](REAL_PROJECT_TRANSITIONS.md)是本轮技能执行动作的依据。T33局部caller核验后回剩余分支；ECC目录覆盖组合文献上限和互异代表；全域漏删检查与拒绝见证各解决一种疑问；必要pair门足够就立即结束更高阶计算；一般k回原文纠正基线再接实际结构；完成新Main后只修真实正文错误，不重开正确数学。未解参数作为停滞/范围教训保留。

这不是宣称所有上游workflow都适合数学，也不是已测通用RSI收益。固定副本、可调用入口、具体行为试用和模型静态阅读的范围在本目录验证与处置记录中分别报告。
