---
type: idea
node_id: idea:ddp-counterexample-gates-20261026
title: "在多参数构造中检验承重覆盖保证"
stage: active
outcome: pending
added: 2026-10-26T16:00:19Z
based_on: ["paper:ddp-record-sources-20261026", "paper:mizuno2026_new_lower_bounds", "paper:przybocki2026_doubly_saturated_ramsey"]
target_gaps: ["gap:DDP2"]
tags: ["ddp"]
---

# 在多参数构造中检验承重覆盖保证

**stage:** `active`  ·  **outcome:** `pending`

## Thesis
复用现有`dd82-counterexample-guided-research`方法节点，不覆盖其n61历史。新应用是检验一项生成规则是否真的保证度数、路径覆盖、群逆向一致性或补全，而不是重开n61谱搜索。

例如，对“每种底点对存在一条满秩路线，所以全图D步覆盖”这种尚未证明的保证，主动寻找满足原前提、却有纤维目标不可达的实例。该反例反驳生成保证，不说明全部degree/diameter图不存在。

对“条件H足以补全”的断言，补全UNKNOWN不算反例；必须实际证明该对象不可补全，或直接指出生成器承诺的具体结论失败。限定循环/群族搜索未命中也不是全域证明。

只在承重推断处使用，不给每个小引理增加机械审阅关卡。找到反例后，它要改变规则或证明前提，不能只把该对象禁掉再盲搜。完整原图、抽象商、群词覆盖与数值近似分别记账。

本文是建议，尚未产生本轮新反例。与新Goal、对应公开构造文献和既有U5节点建立关系即可，不另建通用反例平台。

## Key risks
No complete new graph yet; partial coverage and finite subclass failure do not settle the original problem.


<!-- REFRESH_20261029_PRECEDENCE -->
## 2026-10-29策略适用说明

以下2026-10-26/27“当前0新图／27格／快速比较”是历史阶段记录，不是现在的结果或自动派发队列。当前继承103例／3参数、Lean0，开放表范围与[新版策略](ddp-open-parameter-construction-20261026.md)适用。反例只攻击具体承重保证；有实际问题可深入，不强迫机械短试／快速换题。旧实验和暂停D2边界保留，不重跑历史。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._


## Local provenance and inherited scope

[PRIOR_WORK_LEDGER](../../context/DD_PORTFOLIO_START_20261026/PRIOR_WORK_LEDGER.md); [latest human comments](../DD82_PROGRESS_AND_COMMENTS_20261018.md).

Local lookup found no pre-existing dd82-counterexample-guided-research wiki node. The historical U5 is preserved at [user snapshot](../../context/DD_PORTFOLIO_START_20261026/references/user_snapshots/dd82-counterexample-guided-research.md); its general method is imported here, its n61 queue stays paused.
