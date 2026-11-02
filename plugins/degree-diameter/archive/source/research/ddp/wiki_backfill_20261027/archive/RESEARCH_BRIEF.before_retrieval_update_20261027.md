# DD Portfolio research brief

## Problem Statement
4≤Δ≤12，D∈{3,4,5}，按有数学依据的机制找超过最新公开下界的完整简单无向图。27格是选题池，不要求全部求解或精确最优。唯一入口context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md。

## Constraints
旧N(8,2)暂停，保留57≤N≤61及全部证据等级。最多两条主机制、合计≤8CPU workers；无哈希。保存完整边表、独立全源验证；Lean后于真实数学发现。约每小时更新原research/progress.html，仅报告，不要求换题。

## Current research

第二轮新增105、254、128点三个实际构造入口均未达目标；105源的完整两边交换和九点度完成已收束。1664点提升在原始短路容量处停止。33/32点控制图的有限生成仍未过必要容量，未展开891/864点图。新增均匀字典积和384/8424参数入口已在必要条件处停止。已验证新下界仍为0。

用户追问构造选择是数学直觉还是盲猜。当前应如实区分：度数、阶数和必要容量有严格依据，但正向覆盖直觉仍偏弱；例如Q64减少部分交换短词碰撞有具体依据，PSL群阶过门槛且中心平凡只够支持短试，不能证明比其他群更值得。后续选择必须说明已有的覆盖保证、尚属推测的部分，以及怎样用结果改变下一动作，不能把未被排除当作成功证据。

按 BREADTH_STRATEGY_20261027.md 继续比较结构；最新路径在 NEXT_SESSION.md。

## Evidence and review

Latest actual scoped strategy/filter review: reviews/ddp/breadth_strategy_20261027015855_disposition.json. The later next-mechanism reply has substantive unsupported claims and is not accepted as proof or a validated new direction. Older review descriptions below are historical.

Gemini互审通路于 2026-10-27 01:48:31 UTC 实测成功；桥接回执为 gemini-3.8-flash-high / high。此次只检查256点构造的点数、度数和左作用，不覆盖816/930完整排除、共同斜率结论或最新Q64中心提升成果。最近实质互审仍是10月26日的陪集塔路线；其两处数学错误已撤回或由本地推导及BFS修正，不能把调用SUCCESS当成全部数学通过。
已知650代数恢复不是新纪录，也未声称其公开首创。固定族的失败不排除一般图。两轮实际Gemini回执逐项处置：一个容量断言已由保存图反例否定并被撤回，后续BB公式有遗漏；不以模型赞同作为证明，不称全审通过。无新Grok或Lean。旧h7、谱成果及RAW缺口原样保留，不恢复旧任务。

## Background
启动包context/DD_PORTFOLIO_START_20261026/；唯一知识库research-wiki/，当前状态NEXT_SESSION.md。旧brief归档context/dd82/archive/portfolio_transition_20261026/RESEARCH_BRIEF.md。
