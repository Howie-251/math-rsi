# 实际结构反馈

预测得到支持。signatures 21、62 各自给出 20 点 30 边的二层图；全部返回词直接绑定先前保存的 NB 词，没有重新计词或重跑 64 个签名门。每个顶点的长度至多 6 返回词恰为 empty 加三个简单五边形的正反两向，共 7 条。全图恰有 12 个 canonical 五边形，每点属于 3 个、每条边属于 2 个。

两个签名的实际证书中，face 0 的沿边邻面依次为 `[1,6,8,10,2]`；相邻 rim faces 共享一条边，非相邻 rim faces 不共享边，给出显式 6-face odd wheel。完整点标签、边、返回词 ID、integer coefficient parity 和面绑定保存在各 `signatureNN/` 文件中。面编号一致不代表这里另外证明了两图同构。

附加整数检验也完成：对确定的 19-edge spanning tree，以其余 11 条有向边为 cycle 坐标，faces 0..10 的整数矩阵 determinant 均为 −1。因此这些具体 face cycles 生成各图的完整整数 cycle lattice，而不只是有理向量空间。矩阵及全部 12 面行均保留。

下一步可使用这里的真实面接口作电压障碍推导；本脚本没有搜索 C7 参数，也没有将结构预测直接登记为 C14 全族 NO。它没有生成 140 点候选或新增成果图。新进程 0.019572274 CPU 秒，计准备 0.10 及 root/paper postprocess 后 wholecase 为 3.679050812/5 CPU 秒，所有数值进程终态停止。
