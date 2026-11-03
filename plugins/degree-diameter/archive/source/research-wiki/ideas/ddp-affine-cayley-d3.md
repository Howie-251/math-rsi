---
type: idea
node_id: idea:ddp-affine-cayley-d3
title: "仿射Cayley三直径：两个固定群范围关闭"
stage: active
outcome: pending
added: 2026-10-27T00:14:22Z
based_on: ["paper:ddp-record-sources-20261026"]
target_gaps: ["gap:DDP1", "gap:DDP2"]
tags: ["ddp", "cayley", "diameter3"]
---

# 仿射Cayley三直径：两个固定群范围关闭

**stage:** `active`  ·  **outcome:** `pending`

## Thesis
已验证新下界仍为0。固定群816的全部度数≤12、直径≤3 Cayley范围已完整计算排除；此前930固定群的度数≤11范围也已关闭。两者均不排除一般同阶图或其他群。 816最后7124个等价类的10747252152个规范输入全部完成，10041562788合法，全部纤维覆盖失败，0 BFS、0图。四个worker含准备和汇总共966.508 CPU秒。结合原容量筛、四/六逆对完整结果、五逆对的相位17自动同构和紧纤维降维，全部67115个符号存活模式均关闭。五逆对原模式计数为28+314+2168+13865=16375。度数不足12可添加17个反射中的未用项升到12且不增距离，故同样被排除。

## Key risks
全部已启动批次与保存图验收均已结束，无在途作业或待验图。共同斜率的246项试验在启动前被纸面障碍取消，没有运行或失败记录。已闭固定群和局部邻域不重跑；124/172完整加法电压族、多个匹配同时改变以及一般图仍开放。单独改变匹配斜率会损失边且本批明显恶化，不能据此自动追加相同扰动。下一构造须改变实际覆盖结构，不能把参数量或坏对下降替代新下界。旧DD82、旧塔、M1/M3与旧匹配路线暂停；Goal ACTIVE，Lean后于真正发现。 812/820旧有限profile之外仍开放，无自动重启队列。

## Connections
_Edges are recorded in `graph/edges.jsonl`; summarize here for human readers._

