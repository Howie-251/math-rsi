# 当前 (15,3)=1620：实际全 15 正则，无保边增点入口

取到当前作者的实际小型 literal 与完整 recipe，度数检查支持 metadata-based 正则性预测：1620 点、12150 边，全部 degree15。free=0、free slots=0、minSatN=15，zero-fault 和 one-fault 原型均为 0。保全部旧边且最大度仍为 15 时，任何旧点都不能接新边；任意新增点或助手组也无法与旧图相连。只关闭这一实际源的保边扩张，不否定改变旧边的操作或一般更大 (15,3) 图。

## 真实来源与奇纤维的对照

当前 primary 为 [Bhakar 作者仓库](https://github.com/f4t4nt/degree-diameter-graphs/tree/main/graphs/deg15/dia3)，实际 [README](README.author.md)、[construction.json](construction.author.json) 与 [原边表](source1620.author.edges.txt) 均已本地绑定。原边表一次下载 105809 字节；当前 source 的阶数不是由因式分解猜测。相关现有台账未见该当前源已恢复。

作者配方是 60 点、5 正则 controller 上的 F3³ route-chart lift。controller 是三底点 Schreier 图的 Z20 lift，五个符号为 a,a⁻¹,b,b⁻¹,s；每条 dart 在目标 27 点块中给出一条三点仿射线。实际 literal 的 60 个连续 27 点块都没有内部边，每点向固定 5 个相邻块各接 3 点，相邻块间恰有 81 条边。因此所有顶点的 15 度完全由外部线路占满。

这与刚分析的 972 源不同。972 的四条外线路给外部度 12，再由块内 matching 加最多 1 度；奇数 27 上的内部 involution 固定点成为 degree12 free 点。1620 的 s 虽然在三底点 Schreier 底图的顶点 2 处画为 semi-edge，但提升后作用是 (2,g)→(2,g+10)，配的是两个不同 controller cells，不是奇数 27 块内部的 involution。奇数纤维本身不保证空位。

## 本轮完成与未做的事项

实际结构 profile CPU 0.023142107 秒。源的公开 D3 继承作者结果，没有旧源单根或全源 BFS；actual D 保持空值。没有 R2 缓存、必要覆盖测试、LP/MIP、候选图或边修改。基线 1620 使用父代理 2026-10-27 21:10 主表刷新，未再次刷新主表。

[事前条件与 metadata-based 预测](PREDICTION.json) 明确区分了“若有内部 involution 则可能留下空位”和实际配方已经给出的五条外线路；[SOURCE_PROFILE](SOURCE_PROFILE.json) 是完整 literal 的实际 degree/fiber profile，[SOURCE_FACTS](SOURCE_FACTS.json) 保留来源与精确关闭范围，[profile.py](profile.py) 可复现这个单次无 BFS 的结构检查。[header 边表](source1620.header.edges) 只是同一作者 literal 的规范化本地接口。

本源的保边入口到此停止，不追加其它源、字段或模板。
