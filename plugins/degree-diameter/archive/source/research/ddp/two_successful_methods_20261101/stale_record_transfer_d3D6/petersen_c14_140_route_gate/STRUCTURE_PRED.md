# 两个 surviving parity signatures 的具体结构预测

本批开始前登记。继承已完成的 1900 条有向非回退词和 64 个 parity 门，仅读取，不重新生成或枚举。

对 signatures 21、62，按顶点 `2*v+p` 和已经冻结的六 cotree bits 构造实际 20 点二层图。预测每个顶点长度至多 6 的返回词恰有 7 条：empty，以及三个简单五边形的两种方向；全图恰有 12 个五边形，每点属于 3 个，每条边属于 2 个。预测任一选定 central face 的五个沿边邻面构成一个五圈，给出完整 6-face odd wheel，而非根据 tight count 直接假定 dodecahedron。

只绑定保存词的路径及其 integer coefficient parity，不运行 C7 电压搜索、图 BFS 或 140 点图生成。允许的附加便宜检验：固定 20 点图的一棵树，以 11 个非树边为整数 cycle 坐标，取 11 个 face-cycle rows，计算一个 11×11 exact integer minor；只有实际 determinant 为 ±1 时才记录整数 cycle lattice 生成结论。

预算沿用 wholecase 5 CPU 秒：此前 3.495753483，root/paper postprocess 合计另 0.063725055；本脚本准备保守计 0.10，实际进程另计，CPU soft/hard cap 均 1 秒。任何预测失败保留具体反例并停止，不改变模型来支持预测。没有 C14 全族结论自动成立：odd-wheel 的电压推论由独立纸面审阅连接。
