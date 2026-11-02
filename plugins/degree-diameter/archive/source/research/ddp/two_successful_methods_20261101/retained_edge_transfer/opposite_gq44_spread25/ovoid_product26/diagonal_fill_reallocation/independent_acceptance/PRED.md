# 独立核验预测：唯一7532图，先登记再执行

2026-11-01。已读root PREDICTION_AND_SCOPE；不修改producer或root文件。

**P1。** 实际候选严格等于已接受7531边集删除17条(flag diagonal clone, own filler)后，再加hub7531到所有17 fillers的边；保留7242源H的全部90525边。真实diagonal由ORDERED_CENTERS.is_incident_flag与spread_index确定，不假j=i。所有clone只连其原U openN；flag raw Cartesian25含self，必须去self，不把它作为真正U pin。

预测n7532/m97750，degree histogram17:1/24:17/25:289/26:7225。对全部289clones+hub做且只做290次普通radius3 BFS，旧根0。逐根比对diag(1,24,418,7089)、offdiag(1,25,441,7065)、hub(1,17,425,7089)，任何差异原样记录；hist预测与实际全覆盖的数学判定分别记账。

**纸面攻击重点。** 克隆使用N_U(c)仍能在U内替换端点覆盖U和其他clone；diag clone到自己删去的filler可经同point的另一个flag两步；到其他filler的H短路不能先走自己的filler，否则两个不同filler在两步内相通，与pinsets不交矛盾。hub经旗标覆盖所有旧点与clone。prefix从H直接逐个加modified clone、hub最后，不能用从旧7531删除边的单调性代替证明。

读取H、已接受7531、实际新7532各一次，只核本次输入绑定/精确delta，不重跑旧图BFS或几何。旧独验非D2采用Moore677而非保存某个pair；本次直接从290个授权新根BFS保存一个实际distance3 witness，再以Moore上界作纸面交叉说明，不另跑旧根。

总预算20CPU含程序准备执行、单worker；0field/旧geometry/旧根BFS/Lean/solver，0其他候选或自动续算。producer已通知实际closed后才执行。
