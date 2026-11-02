# 真实R4矩阵的分数下界门未决

使用前一批2755目标、13057guard的完整现成mask，包含8105259个非零关系，不造新球、源直径BFS或候选图。本批区分强一阶proxy需5guards与实际R4覆盖预算的障碍，原四guardSAT不重启。

唯一完整LP在20秒limit返回time limit reached/primal_status None，workerCPU22.439896875。没有返回可用权重，未生成精确对偶或分数可行性证书。因此不能声称真实覆盖数>4，也不能声称存在≤4的分数覆盖。既有完整整数问题保持UNKNOWN。

PREDICTION.md已说明若出现权重必须用整权重全矩阵核对；该后续阶段没有触发。所有作业终态，本门停止，不续LP或追加分数截断。无新图、BFS、SAT续算或Lean实例。
