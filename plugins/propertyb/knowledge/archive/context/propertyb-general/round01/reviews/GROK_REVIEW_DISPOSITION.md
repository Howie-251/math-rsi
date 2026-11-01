# Grok旧首轮恢复结果：数学处置与使用范围

2026-10-21。原请求为`GROK_PROMPT.txt`，原文为`GROK_RECOVERED_REPLY.md`，原生身份与完成证据为`GROK_RECOVERY_METADATA.json`。本处置依据root本轮核查指令记录；不修改原始回复，也不涉及正在运行的新round02审阅。

## 可采用范围

root核查：A/B的主体有效。最小顶点反例的点对覆盖归约、关联Gram团秩界、Turán单交图上界，以及RS同一重染算法的FKG端项与有向单交对精确积分，可以连接为原H的充分判据。原回复只静态读取首轮材料，未运行程序或Lean，不能据此记成新完整候选或研究Goal已经验收。

## 两处纠正

1. 原回复说“p=1……没有结论”过强。`CORE_THEOREM.md`允许`0<p≤1`，p=1时端项`1-a_k(p)^{M/2^{k-1}}`为0，剩余积分界只要严格小于1，同样给出Property B。真正不给出该充分结论的是**总失败上界等于1**，不能把端点p=1与这个等号混同。
2. 原回复说“补边……不能保持非B”错误。非B性对增加边单调：原非B子图仍在，增加约束不会产生proper染色。这里不应补边，是因为证明直接保留实际m≤M已足够；固定顶点集可能没有足够多的不同k集可补，补边也会改变实际单交图、度数与临界性等结构。不能将“不必要／结构不保留”写成“非B性不保留”。

以上不改变A/B主链，但引用时采用root完整稿中的正确表述，不直接复述这两句话。

## C不作为已证比较定理

原C给出k≥10⁴的+1论证候选，其中使用多个“约”“至多约”和未完整展开的指数余量比较。本轮不将其作为严格证明进口。root独立完成的`proofs/propertyb-general/UNIFORM_INTEGER_GAIN.md`（范围k≥17）已替代该候选；它与`CORE_THEOREM.md`属于随后形成的新完整材料，不在本次旧首轮审阅范围内。

原回复还明确未超过Grill的强界，未核所有具体k的强基线包络、Schmidt原文或2026综述全文。上述未解项不因A/B认可消失。

## trace判定

旧调用有原生完整assistant正文与`turn_ended / completed`，因此记录`review_completed=true`。原MCP envelope及`stopReason`没有恢复，字段保留null，不合成`end_turn`。

原prompt的A/B/C/D范围中，C没有形成可采用的完整严格证明，且D只给有边界的未发现记录。因此整次调用不加`review_scope_complete`或`review_positive`，trace验收保持`provisional`；A/B的有效审阅范围和root纠正独立保留。本trace不是对新k≥17定理的认证。
