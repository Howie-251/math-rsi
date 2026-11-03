# 唯一循环错位配块候选：分量障碍解除，直径仍为七

本次按新增授权，仅改变原一因子骨架的块匹配：对每个按标签定向的 lower→higher group pair，把 selected list 的第 k 个块接到第 `(k+1) modq` 个块，q 为三或四。颜色、一因子、每端 selected-block 集合、bonus 颜色和端口 rank-mod4 规则全部保留。生成程序、完整参数及计划保存在本目录；原候选不变。仅生成一个候选，没有其他 shift、方向、端口或种子方案。

每端集合均被完美匹配用尽，故每个 block 仍有 16 个外部关联。完整边表实际核实：676 点、1,690 边，简单连通、全部五度；普通叶图为 520 点 4 正则。325 个 group pairs 中仍是 260 对三条叶边、65 对四条。原同 index 配对导致的组件障碍确已解除：**叶图只有一个 520 点连通分量，block 商图只有一个 130 点连通分量**。

通用全源检查器及独立 Python 全源 BFS 一致得到直径 **7**，共有 **27,142** 个无序点对距离超过五。因此该对象仍不是 (5,5) 新下界。它比对角方案的 103,041 坏对少，但仍远多于此前从650扩张的2,172坏对；连通和同 index 障碍解除不等于短路径覆盖。

| 点对类型 | 距离超过五的无序对 |
|---|---:|
| head–head | 0 |
| head–block | 588 |
| head–leaf | 1,018 |
| block–block | 268 |
| block–leaf | 8,172 |
| leaf–leaf | 17,096 |
| 合计 | 27,142 |

有序距离谱（距离 0 至 7）为 `(676,3380,13314,49494,140426,195402,53616,668)`。407 个顶点偏心率六，269 个为七。head–block、head–leaf 覆盖仍有实际缺失，并未因叶图连通而自动解决。

完整对象为 `candidate.edges`；所有 27,142 坏对保存在 `candidate.bad_pairs.tsv`。`candidate.independent_validation.json` 含全图/类型距离谱、每点缺失数、所有 head 的距离谱，以及叶图和 block 商图的完整连通分量。`candidate.parameters.json` 含完整块匹配、端口排序及标签。

实际成本：生成 0.03442 CPU 秒，通用全源检查 0.01686 CPU 秒，独立 Python 全源检查/分型/分量计算 0.45999 CPU 秒，共 0.51126 CPU 秒，低于 30 CPU 秒预算。生成和独立检查返回 0；通用检查返回 1，含义是直径五不合格。所有范围已完整完成，无追加搜索。

```text
python research/ddp/m2_factorization676/cyclic_pairing/generate.py
computations/ddp/verify_graph research/ddp/m2_factorization676/cyclic_pairing/candidate.edges 5 5
python research/ddp/m2_factorization676/cyclic_pairing/validate.py
```
