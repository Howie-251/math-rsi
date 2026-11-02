# N2：针对已保存失败旧点对的第三删边补偿

事前预测：从已经保存的六个 N2 双删边/4star 新根覆盖通过但 old-old 失败的基例中，至少一个本次变体能同时修好该基例的首失败旧点对，并保住新根到全部 41 个旧点的 3 步覆盖。完整 42 点图是否成功另行检验，不预言必有新纪录。

冻结规则：继承基例的两条不交 source 旧 cut edges 及四 pins P。取 p∈P、source 旧边 {a,b} 的一个方向 (a,b)，a,b 均不在 P，且 p-a 为 source 原非边。删除第三旧边 a-b 与 star-p，添加 p-a 与 star-b。于是 a、b、p 各失一得一，star 仍为 4 度；最终为 42 点、84 边、全 4 regular。第三条 cut 与原两 cut 顶点不交。此规则增加定向 old-old repair，超出已经严格关闭的同 N2 两 cut + 4star 规则。

六个基例及其首失败旧 pair 只读取保存的 N2_ALL_PAIR_PARAMETERS.tsv / N2_ALL_PAIR_STAGES.tsv，原双 cut 批不重跑；source 仅 parse 一次作为新构造输入，源 D3/regular 合法性继承。每个允许参数变体先查其保存的旧 pair 的实际最短距离，再查新根 R3，通过后逐个查全部 41 旧根至首失败。第一完整 hit 保存 raw 42/84、参数和全部 42 根结果后停止。本批若完整无 hit，只排这个六基例上的定向第三 cut/repair 有限规则，不排其他 source、其他 repair 或一般 (4,3)。

参数域不跨基例做 literal 去重；记录全部实际基例/p/a/b，因此不同参数可能产生同一图，不能将参数数冒作非同构图数。上界 6×4×2×82=3936。单 worker，总 5 CPU 秒含准备保守计 0.15 和实际进程；脚本 CPU hard cap 4 秒。0 source D3 BFS、0 原 6150 双 cut 重跑、0 N3/第二 repair/seed/solver/Lean/远程调用。
