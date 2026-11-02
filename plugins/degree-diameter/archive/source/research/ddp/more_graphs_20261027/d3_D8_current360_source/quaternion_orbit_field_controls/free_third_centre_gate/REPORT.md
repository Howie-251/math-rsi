# 放开 semi3 的一个 normal 向量：关键槽仍不足

本批只解除上一轮通用模块证明指出的一个绑定：将 base3 的 semi-edge normal 从 j·e1 改成独立 w∈F5²。Q8部分仍为 -1；其余配方全部固定：i=[[0,1],[4,0]]、j=[[0,2],[2,0]]，semi2=e1、semi4=-e2、cross1→3=(e2,-j)。这是 literal affine translation part，不除以二。

事前冻结的预测为“至少一个 w 令 D9 关键槽的 endpoint image 达到25”。目标槽仍是 source(base2,1) 到 target(base2,-1)。没有重跑 source360 的 BFS，没有改矩阵、其它 normal、field 或 base；旧 torsor 模型的20形式端点文件没有覆盖。

## 新自由模块与完整范围

取整数 Hamilton quaternion 环 R，改用 R·e1⊕R·w 的八整数系数。cross1→3 normal=-i·e1；semi2=e1；semi3=w；semi4=i·e1。右乘 normal 仍按 n→n+h·a 递推，逆边为 -h^-1·a，semi-edge仍自逆。相邻逆 dart 消去保持完整 affine endpoint；因此所有 NB≤9 前缀捕获全部可在九步达到的端点，沿用已证明的 controller 唯一逆 dart 条件。

本次重新生成的是这个新八系数模块的路线表达式：全部1534个 NB≤9 前缀，关键槽29条路线。它们只给22个不同整数系数端点。对任意目标表示及两个被评价的向量 z、w，实际端点都是这22个系数的像，故实际不同端点≤22<25。

这个形式上界已经排除同一 one-free-semi3 normal 关系下的25状态覆盖；不依赖当前固定矩阵求值产生的额外碰撞。它没有解除其它 normal 关系，也不是对所有独立电压 assignment 的界。

## 全部25个 w 的实际小算术

仍按冻结范围，对固定 q5 矩阵、z=e1 完整评价全部 w=(x,y)，x、y各0..4，顺序 x优先再y。每个系数 (A,B) 评价为 ρ(A)e1+ρ(B)w。结果为：

| w 的 x | y=0 | y=1 | y=2 | y=3 | y=4 |
|---:|---:|---:|---:|---:|---:|
| 0 | 12 | 16 | 15 | 15 | 12 |
| 1 | 9 | 13 | 12 | 12 | 15 |
| 2 | 12 | 13 | 15 | 16 | 14 |
| 3 | 11 | 16 | 15 | 16 | 14 |
| 4 | 9 | 16 | 16 | 16 | 17 |

最大17，passer0。事前“存在完整25像”的预测被反驳。没有根据较大像挑参数造图，也没有进入其它 normal 的自由化或 solver。

## 证据与计数口径

[PREDICTION.json](PREDICTION.json) 保留原预测；[FORMAL_ENDPOINTS.json](FORMAL_ENDPOINTS.json) 保存29条路线及22个八整数系数；[EVALUATIONS.json](EVALUATIONS.json) 保存全部25个 image/missing 集；[RESULT.json](RESULT.json) 与 [terminal.json](terminal.json) 均为完整终态。程序为 [run.py](run.py)。

CPU0.010288600秒。新增形式模块枚举1次、25项小算术；source BFS、目标图、目标 BFS、solver 均为0。没有导出1000点图，actual_n/actual_D/普通无序坏对为空。29是关键路线数，22是形式端点数，17是某个必要槽的最大实际像，均不是全图坏对或独立方法数量。

固定 one-free-semi3 规则到此停止；一般 cubic 图及不同完整连接规则未被排除。
