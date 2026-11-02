# 唯一确定性 3/4 重数一因子骨架

本次只展开和测量一个完整候选；单核总预算不超过 30 CPU 秒，不使用随机种子、端口方案队列或后续修复。原 650/676 对象不变。

groups 是 `Z25 ∪ {∞}`，以 0–24 和 25 表示。颜色 `t∈Z25` 的一因子为 `(∞,t)` 及 `(t+i,t−i)`（模 25，`i=1..12`）。这些 25 个一因子恰覆盖 `K26` 的全部 325 条 group pairs。

对颜色 t，令 `c=t mod5`。每个对应 group pair 在双方相同 block index `c,c+1,c+2 mod5` 各连接一次。在五个 bonus 颜色 `t=0..4`，再在 block `c+3 mod5` 连接一次。因此 65 个 group pairs 有四条块边，260 个有三条。

固定一个 group 的 block b，基础规则中包含 b 的三个 class 各有五个颜色，给 15 个关联；bonus 中唯一 `c=b−3 mod5` 再给一个，总计 16 个。对每个 block 独立把其 16 个关联按 `(对端group,对端block,color)` 升序排序；第 j 个关联（j 从 0 开始）分给 leaf port `j mod4`。这是本次唯一端口规则，每个 port 恰有四条叶边。

标签为每个 group g 的 26 个连续点：head=`26g`；block b=`26g+1+b`；leaf `(b,p)`=`26g+6+4b+p`。每 group 添加五条 head–block 边和二十条 block–leaf 边。外部叶边共 1040 条，树边 650 条，总计 676 点、1690 边，所有顶点预期五度。

先在生成中完整核对一因子覆盖、group-pair 3/4 重数、block 16 关联和端口四度。保存全部颜色、块关联、端口参数及完整边表。用现有 `verify_graph FILE 5 5` 全源检查，并独立从边表重新建立邻接，全源 BFS 按 head/block/leaf 分解距离超过五的无序对。度数正确和 group-pair 覆盖只说明预置结构成立，不预先保证直径五。
