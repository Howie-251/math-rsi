# 双循环58方向初筛：旧结果已覆盖，不重开

2026-10-18。结论：**不选作下一机制，不启动枚举或SAT。**

所提两个 `Z29` 轨道、各自任意反演对称内部连接集、任意跨轨道offset集合，已经被项目的完整解析结果排除。旧证明允许两个轨道的内部步长不同，并不只排除Cayley情形；`t=6` 的30次表示覆盖29点及后续矛盾也已写入旧证明，不是新的待枚举剩余域。

精确来源：

- [CYCLIC_LIFT_CONSTRUCTION.md](../../../../proofs/dd82/construction/CYCLIC_LIFT_CONSTRUCTION.md)，章节“Proof: two orbits on 58 vertices”，覆盖整个上述作用族。
- [wiki claim: dd82-small-cyclic-lift-obstructions](../../../../research-wiki/claims/dd82-small-cyclic-lift-obstructions.md)，2026-10-11登记为`verified`，明确不是任意58点排除，也不是Lean结果。
- [2026-10-11构造进展](../../../../context/dd82/CONSTRUCTION_PROGRESS_20261011.md)，已记载二/三/四轨道循环族的排除及当时审阅记录。
- [2026-10-13构造进展](../../../../context/dd82/CONSTRUCTION_PROGRESS_20261013.md)，已记载既有C29排除曾阻止重复搜索建议。

此次仅核对方向与旧结果的范围一致，没有重跑、重新认证或展开替代证明。归一化、近铺砌枚举及候选展开检查均无需新增。该方向否决不影响正在执行的F5补全，也不排除不具有此作用的58点图。

## 对下一构造方向的建议

只读检查了当前`gap_map.md`、wiki的16项idea目录、73项experiment目录、有关完整图构造的实际记录，以及2026-10-11/13的进展总结。**这批现有材料中没有找到可诚实推荐为“尚未尝试、具有具体新生成规则”的新机制；本次推荐数为0。**

仍开放的一般false-twin58、自由C5、其他VT60、HS增广剩余分支、固定边界补全等，并不等于已有新的可执行构造理由。已有自由化、完整变量模型、不同目标函数及多边交换记录，也不能通过换名称当作未试路线。具体依据见 [gap map](../../../../research-wiki/gap_map.md)、[joint-boundary旧机制](../../../../research-wiki/ideas/dd82-joint-boundary-completion.md)及[全图加权交换旧机制](../../../../research-wiki/ideas/dd82-fullgraph60-dynamic-pair-weights.md)。

建议先使用当前F5实际返回对象作判断；若它没有给出可用的新结构，当前缺口是新的数学构造结构或能改变生成规则的推导，而不是再从上述旧族中挑一个未运行编号。这里不声称已穷尽所有可能构造思路，也不建议自动退到F4、换seed或延长旧搜索。
