# Property B 两次下界的经验整理

2026-10-13。用户要求提炼m(5)≥33、m(5)≥34两次研究中可用于继续提高下界的方法、失败与效率经验。本目录保存证据整理和审阅，正式阅读页沿用唯一research-wiki。

## 阅读入口

1. [方法总览](../../research-wiki/PROPERTY_B_RESEARCH_LESSONS.md)：数学机制、迁移边界、真实输入连接、执行与审阅方法。
2. [失败地图](../../research-wiki/PROPERTY_B_FAILURE_ATLAS.md)：14条具体失败或未采用路线，逐条给范围、依据、修复或重试条件。
3. [下一下界指南](../../research-wiki/PROPERTY_B_NEXT_BOUND_PLAYBOOK.md)：T34→m(5)≥35的新义务地图和下一轮应先产出的结果。

## 原始分工

- [MATH_TRANSFER.md](MATH_TRANSFER.md)：从T32/T33证明和模块抽取可迁移数学；后附主代理核实的审阅补充。
- [FAILURES_EVIDENCE.md](FAILURES_EVIDENCE.md)：原始失败记录的逐条证据整理。
- [LEAN_AND_EXECUTION.md](LEAN_AND_EXECUTION.md)：真实caller、参数化、分类表示、分块、资源争抢和构建审计经验。

这三份笔记由同家族子代理分工整理，主代理核对、整合；其意见属于same-family/provisional，不新增定理验收。历史运行时长保留原上下文，不充当新性能基准。

## 本次纸面准备与计算

[SMALL_VERTEX_34_NOTE.md](SMALL_VERTEX_34_NOTE.md)给出34边时17/18点的一次事件交叠修复。组合公式由[check_boundary_arithmetic.py](check_boundary_arithmetic.py)精确复算，结果在[NO_LOCK_BOUNDARY_CHECK.json](NO_LOCK_BOUNDARY_CHECK.json)，还包括19/20点旧无锁界的迁移及19点cap阈值。没有搜索输入超图，没有新Lean定理。

21点旧δ≤7内部依赖总度等号的选点义务经审阅后补齐；20点新单位伙伴范围、24/25点低度数量变化见下一下界指南。这些是新参数下的必要条件和待证入口，不代表相应超图已构造或新目标已解决。

## 知识库和状态同步

本次Grok与Gemini均有效返回；实际读取范围、两项迁移遗漏的补充、精确复算及reviewer笔误处置见[REVIEW_RECONCILIATION.md](REVIEW_RECONCILIATION.md)。原回应完整保留。它们没有执行Lean，也没有把下一档纸面准备认证为新下界。

通过ARIS规范helper更新[下一阈值idea](../../research-wiki/ideas/propertyb-five-34-edge-threshold.md)、长期精确值方向及三条范围明确的历史失败idea；写入参数保存在[WIKI_UPDATES.json](WIKI_UPDATES.json)。原wiki未重建，T32/T33 verified claims保持原结论；新idea为proposed/pending。

发现旧最终接口地图残留pending状态后，已按实际执行摘要同步。原文保存在[INTERFACE_MAP_BEFORE_STATUS_SYNC.md](INTERFACE_MAP_BEFORE_STATUS_SYNC.md)，长期精确值旧idea保存在[EXACT_VALUE_IDEA_BEFORE_UPDATE.md](EXACT_VALUE_IDEA_BEFORE_UPDATE.md)。同步后重建原T33交接zip，仅改变说明，未改Lean源码或重新运行构建。

本轮没有创建、恢复或替换Goal。T33保持完成；更高下界的正式研究可从上述三页开始。
