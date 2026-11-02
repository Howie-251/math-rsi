# 固定42342基图的 Q-line 单点扩张候选池

从已恢复的675条 selected Q-line witnesses 得到 **649个不同中心**。本次固定当前完整42342图，不改变旧边，枚举这649个 flat planes 中全部81条不经中心的奇异直线，得到52569条不同原始 lines。筛后有 **7条不同 lines / 7组不同 mandatory folded-pinsets** 满足度数限制，均有10个 pins；已全部交给 root 作完整R4验收。

冻结的 P_Qline_degree_pool“该中心范围内至少存在一组有现存度余量的 line pins”得到支持，范围仅是必要度条件。尚未生成42343点图，未计算任何距离或 anchors，不能据此认定超过当前(12,5)下界42342。

## 固定参数及全枚举

输入只读 `h9_quadric_center/RESULT.json` 的终态675条 records（pending为空），选定 witnesses 不替换。649个 normalized 中心 y 去重后，各取首条原始 selected line 基 x,z；Π_y=span(y,x,z)。枚举 a,b∈F9，生成

`L_(a,b)=span(x−a*y, z−b*y)`，

即 dual 坐标(1,a,b)对应的全部81条不经 y 的射影线。中心坐标与原selected线基来自现存结果；有限域/10点生成调用上批 `geometry.py`。只复用 point/fold 小缓存，没有重建 points 或 H9 incidence。全部52569个生成 span 通过奇异线检查，并逐项确认不满足 H9 六个 Plücker 等式。

度数取当前**完整42342图**（245217边）的每行邻接数，不是只取共同核心 K 中的度。mandatory pins 是该 line 的10个原 points 的 π 像去重。要求每个 pin 当前度<12、pins数≤12；因 line 只有10个 points，新增点自身的度条件在本族自动满足。没有把 source extras 作为新 pins，也没有增加 anchors。

## 完整计数

| 项目 | 数量 |
|---|---:|
| 输入675条 witnesses 中重复中心记录 | 26 |
| 不同中心 / 全部处理中心 | 649 / 649 |
| 原始枚举 / 不同原10-point tuples | 52569 / 52569 |
| 重复原 line tuples | 0 |
| 不同 folded-pin tuples | 51366 |
| folded-pin重复（按原始line计） | 1203 |
| 含至少一个当前满度12 pin 的原lines | 52562 |
| 新增点自身degree>12而排除 | 0 |
| degree-feasible原lines / 不同pinsets | 7 / 7 |

全部 line 像大小：10点52433条、7点136条。7个通过者的像都为10点。按不同 folded-pinset 计，51359组因满度 pins 被排，7组保留。每个中心的枚举计数、满度pin数量分布与12个排除样例在 `RESULT.json`；所有7个通过者的完整 pins、当前度数、原10-point labels、定义基与中心/dual参数在 `pool.json` 和 `RESULT.json.pool`。

字典序首个通过组为

`[452,6195,10312,12353,13822,21068,24695,29805,36474,38101]`，

当前度数为 `[11,11,11,11,11,11,11,11,10,11]`。其中心原point label5618，dual(1,0,6)，可直接由 saved basis 与 fold cache 重新生成，无需源邻接来拟合 line。

## 覆盖范围与交接

既有 Q-line 路由证明保证新点对共同旧核心 K 的≤5覆盖；当前完整 base 另有986个 extras，不能据 oldcore 保证自动断言这些新—新类别全覆盖。root 将以7组完整 mandatory pins 为固定候选，对完整42342图作一次R4验收；本代理没有提前评分或生成新图。

degree-infeasible 的52562条仅在**固定当前 source + 本次649中心的81-line族**内不可直接添加；不排除别的中心、selected-line替代见证、改变旧图或一般Q-line构造。本次未扩展到全部66430中心，亦未筛选新的中心池。上轮每个源附件只找首条合格 line，未证明其唯一，所以649只是冻结见证产生的范围。

单worker CPU **2.017526283秒**，已完整枚举，不耗满30秒预算；`pending=[]`。新图0，新下界0，无BFS、R4评分、anchors优化或哈希。终态、完整pool与生成代码均保存本目录；不修改旧675 witnesses、中心结果、Wiki或root计划。
