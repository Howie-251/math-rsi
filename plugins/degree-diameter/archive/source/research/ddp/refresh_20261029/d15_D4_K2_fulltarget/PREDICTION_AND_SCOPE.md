# (15,4)15552源：完整K2整数覆盖模型准备

固定同一已验15552点源。此前R2必要门完成：648个literal freeport均spare1，
全部目标R2支持3..18、T0为空；这不保证整数可行。本次不做LP预热，直接保留全部
648个port和全部15552个目标，构建完整双侧覆盖条件。

每port两个selector A_i、B_i，共1296；各侧总数≤14，加入648条真正互斥子句
`¬A_i∨¬B_i`（不是正向的至少选一）。每目标t两行：`R3(A)∨R2(B)`、`R3(B)∨R2(A)`。
只合并完全相同的literal集合，不合并port、不成线、不加对称、不限制分数支撑。

输入只读 `../d15_D4_K2_route_gate/` 的FREE_ORDER及完整R2/R3转置缓存，不再读
源边表，不重算任何球或源直径。准备单worker CPU≤15秒，prepare-only、0solver。
root审阅后拟唯一solver120 / whole150 CPU调用，UNKNOWN即停；本目录不自动启动。
真SAT仍须完整cached-cover核验与root对实际新图验收，不能把SAT文本当图。
