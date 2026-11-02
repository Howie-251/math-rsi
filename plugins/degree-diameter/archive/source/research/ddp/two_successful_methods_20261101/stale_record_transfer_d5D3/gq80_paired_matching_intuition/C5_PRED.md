# C5 action、精确压缩与单侧覆盖容量：事前预测

root 新授权的唯一结构批，继承 readgate1.100792823 CPU，case cap10；新准备计0.25，单 worker 进程 hard CPU cap8。此前 a_0=3 局部预测没有执行，现为历史未选方向，不同时启动。

先仅用缓存40 pointvectors/40 lines 和实际交替矩阵 J，固定 seed202611010503，至多64个六 transvection products 寻找 A^5=±I；若为−I取−A，显式核 A≠I、A^5=I、A^T J A=J。它是本次新 symplectic action，不是重新生成或验证旧 field/GQ。绑定原 point labels、原 line4sets、两侧各8个5cycles与160条 incidence 的作用；失败即保留 UNKNOWN/反例，不换seed。

复用旧1560variables/1080exact far covers。逐 original edge orbit 建5edge block，只保 block内每vertex≤1 的块；每侧原8个奇数5orbit内部的16块不能构成等变matching，因而排除。预期每侧140 blocks、8 degree equations，合280/16；1080 far pairs 分成216个5orbits，用代表式并验证同orbit原式折成相同 block OR。**保留 collinear/concurrent blocks**，不套旧 girth5，不加尚未读proof的 cuts。

可推翻的容量预测：分别完整枚举两侧105×5^4=65625个 C5-perfect matchings，计算其对216far-orbit clauses 的贡献 mask；各侧最大 distinct covered 数之和小于216，形成内部重复已耗尽容量的障碍。若实际之和≥216，则此容量障碍预测被推翻，不能称 C5族无解。保存两个实际 argmax、overlap/uncovered、所有实际域计数及完整单侧mask记录。不做65625² joint join，不运行solver。

仅若两个所存 argmax 的实际 union 已覆盖216，立即生成80/200完整候选及matching/全部1080旧覆盖式 witness，交root fresh验收；否则不给新图。旧sourceD4/BFS/geometry/field重造0，未命中图0，不自动新action/seed/预算。
