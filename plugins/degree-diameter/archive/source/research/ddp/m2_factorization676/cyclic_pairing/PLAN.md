# 唯一跟进：selected-block 循环错位配对

前一同 index 候选的全局 block-index 守恒产生 73,060 个异 index 叶对缺陷。本次有明确结构修改：保留同一 K26 一因子颜色、每端 selected-block 集合、bonus 颜色及 rank-mod4 端口规则，仅把 group pair 两端的块匹配改为循环 shift 1。

每条 group pair 先按 group 标签 `g<h` 定向。颜色 t 的 selected list 为 `[(c+j) mod5 : j=0..q−1]`，`c=t mod5`，bonus `t<5` 时 q=4，其余 q=3。lower group 的第 k 个 selected block 连接 higher group 的第 `(k+1) modq` 个 selected block。集合两端均仍用尽，所以每个 block 保持 16 个外部关联，每个 group pair 保持三或四条边；实际 leaf 端口仍将各 block 的关联按 `(对端group,对端block,color)` 排序后以 rank mod4 分配。

仅生成这个确定性候选，单核预算不超过 30 CPU 秒，不试 shift2、反方向、其他端口方案、随机种子或修复队列。原对角候选、650图及旧扩张图保持不变。

完整展开后独立通用全源 BFS 和 Python 分型检查 degree/simple/connected/diameter/bad pairs；从独立边表额外统计 520 点普通 leafgraph 和 130 点 block quotient 的连通分量。解除已证守恒只改变真实失败条件，并不预先保证直径五。
