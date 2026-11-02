# 3645→3646单cut最大star：完整NO，障碍在新根覆盖

原source是actual3645/20044、max11/D4，只有7个10度free vertices，旧保边任意非空扩张已NO。这次改变生成规则：删除任一旧edge uv，新点连原7free及u/v，最大9个pin；其它oldedges保留。端点与free重叠也合法。最大star支配该cut下全部合法子star。

预测原201插入点内部的645条edge可能有一个能补齐原free-R3遗留的743个缺点。实际完整20044条旧edge全部失败；插入层645也0pass，预测被推翻。最优cut(108,1643)仍漏305，故0候选进入旧旧D4检查，不能把结果说成旧路线损坏。

此次复用1993个已存sourceR3支持，新增1652个缺root的半径3查询；原7free并、sourceD4验证及所有旧UNKNOWN均未重跑。保存了20044行实际结果和全support cache。一次输入metadata用roots/new_roots不同字段的准备错误发生在编译/数值之前，已保存并保守计.1CPU；没有重置数值timer。

一次读取结果还给出更具体限制：单cut两端在743 holes上最大覆盖量，前3444点内部边438、跨插入层边356、插入层内部边338。若两cuts都避开前3444点内部边，则合并最多356+356=712<743；即使共享端点，最大F7+cutends新星至多11pins且合法，也必漏至少31。因此两cut-onlystar若想成必须含一条前3444点内部边。没有枚举两cut，也不声称含这种边就能成功。

完整NO范围仅固定source、删恰一条旧edge、一个新点且只加new-old spokes、无其它旧旧repair。源图不同、更多删改和一般(11,4)/3646没有排除。finalcase2.943111119/15CPU（含cachedpostprocess保守.05），无solver/Lean/ARIS/新target BFS。

停止本singlecut族，不自动加第二cut或repair。下一转自然364的多helper合作机制，先确认旧1–13helper排除范围与14helper结构，而不是继续修这743点缺口。
